import fs from "node:fs";
import path from "node:path";
import { config } from "../config";
import { voiceReady } from "../config";
import { buildVoiceScript, voiceScriptToMd } from "../elevenlabs/voice-script";
import { generateVoiceover } from "../elevenlabs/client";
import { buildCaption } from "../publishing/telegram/caption";
import { publish } from "../publishing/telegram/client";
import { nextVersionPath } from "../project/day-store";
import { probe } from "../video/verify";
import { createLogger } from "../logger";

const log = createLogger("podcast-file");

export interface FilePodcastResult {
  ok: boolean;
  scriptFile: string;
  reason?: string;
  title?: string;
  audioPath?: string | null;
  voiceScriptPath?: string;
  captionPath?: string;
  telegramDraft?: string;
  durationSeconds?: number | null;
  segments?: number;
  incomplete?: string[];
}

interface ParsedScript {
  title: string;
  narration: string;
  description: string;
}

/**
 * Разбирает готовый markdown-подкаст (например content/carousels/day-07/podcast.md):
 * — заголовок из первого "# ...";
 * — речь из секции "## Сценарий ..." (до следующего "## " или "---");
 * — короткое описание из секции "## Короткое описание ...".
 * Если явной секции сценария нет — читаем всё тело, срезая мета-строки.
 */
export function parseScriptMarkdown(md: string): ParsedScript {
  const lines = md.split(/\r?\n/);
  const title = (lines.find((l) => /^#\s+/.test(l)) || "").replace(/^#\s+/, "").trim();

  const sections: Array<{ head: string; body: string[] }> = [];
  let cur: { head: string; body: string[] } | null = null;
  for (const line of lines) {
    const h2 = line.match(/^##\s+(.*)$/);
    if (h2) {
      cur = { head: h2[1].trim(), body: [] };
      sections.push(cur);
    } else if (cur) {
      cur.body.push(line);
    }
  }

  const pick = (re: RegExp) => sections.find((s) => re.test(s.head));
  const scriptSec = pick(/сценар|script|монолог|речь/i);
  const descSec = pick(/описан|description|анонс/i);

  // Тело секции до горизонтальной черты "---".
  const bodyBefore = (body: string[]) => {
    const out: string[] = [];
    for (const l of body) {
      if (/^\s*---\s*$/.test(l)) break;
      out.push(l);
    }
    return out.join("\n").trim();
  };

  let narration: string;
  if (scriptSec) {
    narration = bodyBefore(scriptSec.body);
  } else {
    // Нет секции — берём всё после front-matter (строки "**Ключ:**" и "---").
    narration = lines
      .filter((l) => !/^#\s/.test(l) && !/^\*\*[^*]+:\*\*/.test(l) && !/^\s*---\s*$/.test(l))
      .join("\n")
      .trim();
  }
  const description = descSec ? bodyBefore(descSec.body) : "";
  return { title, narration, description };
}

/**
 * Отдаёт готовый markdown-скрипт в озвучку: verbatim, слово-в-слово.
 * mp3 и подпись кладутся рядом со скриптом. Ничего не переписывает —
 * только адаптация под речь (ссылки/скобки/markdown) и словарь произношения.
 */
export async function makePodcastFromFile(
  scriptFile: string,
  opts: { publish?: boolean; cta?: string; link?: string } = {}
): Promise<FilePodcastResult> {
  const abs = path.isAbsolute(scriptFile) ? scriptFile : path.join(config.repoRoot, scriptFile);
  if (!fs.existsSync(abs)) return { ok: false, scriptFile, reason: `Файл не найден: ${scriptFile}` };

  const md = fs.readFileSync(abs, "utf8");
  const parsed = parseScriptMarkdown(md);
  if (!parsed.narration) return { ok: false, scriptFile, reason: "В файле не найден текст для озвучки." };

  const dir = path.dirname(abs);
  const base = path.basename(abs).replace(/\.md$/i, "");
  const incomplete: string[] = [];

  // 1. Голосовой сценарий (verbatim → адаптация под речь).
  const vs = buildVoiceScript(parsed.narration, { delivery: "confident", pace: "medium" });
  const voiceScriptPath = path.join(dir, `${base}.voice_script.md`);
  fs.writeFileSync(voiceScriptPath, voiceScriptToMd(vs), "utf8");

  // 2. Озвучка
  const v = voiceReady();
  let audioPath: string | null = null;
  let durationSeconds: number | null = null;
  if (v.ready) {
    const res = await generateVoiceover(vs, path.join(dir, `${base}.segments`), base);
    const { path: mp3 } = nextVersionPath(dir, base, "mp3");
    fs.copyFileSync(res.fullPath, mp3);
    audioPath = mp3;
    const pr = await probe(mp3).catch(() => null);
    durationSeconds = pr?.durationSeconds ?? null;
    log.info(`Озвучено (${config.elevenlabs.mock ? "mock" : "real"}): ${path.basename(mp3)} (${durationSeconds ?? "?"}с, ${vs.segments.length} сегм.)`);
  } else {
    incomplete.push(`Озвучка не выполнена: ${v.message}`);
  }

  // 3. Подпись для Telegram
  const hook = parsed.narration.split(/\n{2,}/).find(Boolean)?.split(/(?<=[.!?…])\s/)[0]?.trim() || parsed.title;
  const caption = buildCaption({
    kind: "podcast",
    title: parsed.title || base,
    hook,
    body: parsed.description || undefined,
    cta: opts.cta,
    link: opts.link,
    durationSeconds: durationSeconds ?? undefined,
  });
  const captionPath = path.join(dir, `${base}.telegram_caption.md`);
  fs.writeFileSync(captionPath, caption, "utf8");

  // 4. Публикация (по умолчанию draft — реальная отправка только в live).
  let telegramDraft: string | undefined;
  if (opts.publish !== false && audioPath) {
    const pub = await publish(
      {
        method: "sendAudio",
        filePath: audioPath,
        caption,
        title: parsed.title || base,
        performer: "Илья Алов — Нейромонах",
        durationSeconds: durationSeconds ?? undefined,
      },
      dir
    );
    telegramDraft = pub.payloadPath;
    if (!pub.ok && pub.error) incomplete.push(`Аудио не отправлено: ${pub.error}`);
    if (config.telegram.publishMode === "draft") incomplete.push("Telegram: режим draft (реальная отправка выключена)");
  }

  return {
    ok: Boolean(audioPath),
    scriptFile,
    title: parsed.title || base,
    audioPath,
    voiceScriptPath,
    captionPath,
    telegramDraft,
    durationSeconds,
    segments: vs.segments.length,
    incomplete,
  };
}
