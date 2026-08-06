import fs from "node:fs";
import path from "node:path";
import { getContentByDate } from "../content/adapter";
import { subDir, writeVersioned, nextVersionPath, setStatus, appendLog } from "../project/day-store";
import { voiceReady, config } from "../config";
import { buildVoiceScript, voiceScriptToMd } from "../elevenlabs/voice-script";
import { generateVoiceover } from "../elevenlabs/client";
import { buildCaption } from "../publishing/telegram/caption";
import { publish, publishMediaGroup } from "../publishing/telegram/client";
import { probe } from "../video/verify";
import { renderCards } from "../carousel/render";
import { Card } from "../store/types";
import { createLogger } from "../logger";

const log = createLogger("podcast");

export type PodcastFormat = "audiopost" | "short" | "full";

export interface PodcastResult {
  ok: boolean;
  date: string;
  reason?: string;
  format?: PodcastFormat;
  scriptPath?: string;
  audioPath?: string | null;
  captionPath?: string;
  telegramDraft?: string;
  durationSeconds?: number | null;
  incomplete?: string[];
}

// Собирает текст подкаста из материала дня. Живая речь, без канцелярщины.
function podcastText(content: ReturnType<typeof getContentByDate>, format: PodcastFormat): string {
  const cards = content.cards;
  const by = (role: string) => cards.find((c) => c.role === role);
  const hook = (content.post.split("\n").find(Boolean) || content.topic).trim();
  const cta = content.cta || "Сохрани и загляни в Telegram AlovLab.";

  const blocks: string[] = [hook];
  if (format === "audiopost") {
    if (by("insight")) blocks.push(by("insight")!.body);
    blocks.push(cta);
    return blocks.filter(Boolean).join("\n\n");
  }
  // short / full
  for (const role of ["problem", "insight", "solution", "example", "action"]) {
    const c = by(role);
    if (c) blocks.push(`${c.title}. ${c.body}`);
  }
  if (format === "full" && content.post) blocks.push(content.post);
  blocks.push(cta);
  return blocks.filter(Boolean).join("\n\n");
}

/**
 * Делает подкаст дня: текст → адаптация под речь → ElevenLabs → mp3 → подпись →
 * Telegram-черновик. Без Studio API (single-voice TTS + монтаж).
 */
export async function makePodcast(date: string, opts: { format?: PodcastFormat } = {}): Promise<PodcastResult> {
  const content = getContentByDate(date);
  if (!content.found) return { ok: false, date, reason: `На ${date} материал в контент-плане не найден.` };

  const format: PodcastFormat = opts.format || "short";
  const v = voiceReady();
  const incomplete: string[] = [];
  const pDir = subDir(date, "podcast");

  // 1. Сценарий подкаста
  const rawText = podcastText(content, format);
  const vs = buildVoiceScript(rawText, { delivery: "confident", pace: "medium" });
  const { path: scriptPath } = writeVersioned(pDir, "script", "json", JSON.stringify(vs, null, 2));
  fs.writeFileSync(path.join(pDir, "voice_script.md"), voiceScriptToMd(vs), "utf8");

  // 2. Озвучка
  let audioPath: string | null = null;
  let durationSeconds: number | null = null;
  if (v.ready) {
    const res = await generateVoiceover(vs, path.join(pDir, "segments"), "podcast");
    const { path: podcastMp3 } = nextVersionPath(pDir, "podcast", "mp3");
    fs.copyFileSync(res.fullPath, podcastMp3);
    audioPath = podcastMp3;
    const pr = await probe(podcastMp3).catch(() => null);
    durationSeconds = pr?.durationSeconds ?? null;
    appendLog(date, `Подкаст (${format}) озвучен: ${path.basename(podcastMp3)} (${durationSeconds ?? "?"}с)`);
  } else {
    incomplete.push(`Озвучка не выполнена: ${v.message}`);
  }

  // 3. Подпись + Telegram-черновик
  const caption = buildCaption({
    kind: "podcast",
    title: content.topic,
    hook: rawText.split("\n").find(Boolean) || content.topic,
    body: `Разобрал тему «${content.topic}» голосом.`,
    cta: content.cta,
    link: content.links[0],
    durationSeconds: durationSeconds ?? undefined,
  });
  const captionPath = path.join(pDir, "telegram_caption.md");
  fs.writeFileSync(captionPath, caption, "utf8");

  // Карточки карусели → PNG (для альбома в Telegram). Требует Chromium (Playwright).
  let cardPngs: string[] = content.carousel_png;
  if (!cardPngs.length && content.cards.length) {
    try {
      const roles = ["cover", "problem", "insight", "solution", "example", "action", "cta"];
      const cards: Card[] = content.cards.map((dc, i) =>
        Card.parse({
          id: `card_${i}`,
          index: i,
          role: (dc.role && roles.includes(dc.role) ? dc.role : roles[Math.min(i, roles.length - 1)]) as Card["role"],
          title: dc.title,
          body: dc.body,
          accent: "",
        })
      );
      const rendered = await renderCards(cards, subDir(date, "carousel"));
      cardPngs = rendered.map((r) => r.file);
      appendLog(date, `Карточки для поста: ${cardPngs.length} PNG`);
    } catch (err) {
      incomplete.push("Карточки карусели не отрисованы (нужен Chromium: npx playwright install chromium).");
      appendLog(date, `Карточки не отрисованы: ${String(err).slice(0, 120)}`);
    }
  }

  // Публикуем: сначала альбом карточек, затем аудио твоим голосом.
  let album: Awaited<ReturnType<typeof publishMediaGroup>> | null = null;
  if (cardPngs.length) album = await publishMediaGroup(cardPngs, caption, pDir);

  const pub = await publish(
    {
      method: "sendAudio",
      filePath: audioPath ?? undefined,
      caption,
      title: content.topic,
      performer: "Илья Алов — Нейромонах",
      durationSeconds: durationSeconds ?? undefined,
    },
    pDir
  );

  if (album && !album.ok && album.error) incomplete.push(`Альбом карточек не отправлен: ${album.error}`);
  if (pub && !pub.ok && pub.error) incomplete.push(`Аудио не отправлено: ${pub.error}`);
  setStatus(date, content.found ? "content_ready" : "planned", "podcast_ready", `${format}, tg:${pub.mode}`);
  log.info(`Подкаст ${date} готов (${format}), карточек: ${cardPngs.length}, telegram ${pub.mode}`);

  return {
    ok: Boolean(audioPath),
    date,
    format,
    scriptPath,
    audioPath,
    captionPath,
    telegramDraft: pub.payloadPath,
    durationSeconds,
    incomplete: [...incomplete, ...(config.telegram.publishMode === "draft" ? ["Telegram: режим draft (реальная отправка выключена)"] : [])],
  };
}
