import fs from "node:fs";
import path from "node:path";
import { config } from "../config";
import { createLogger } from "../logger";
import { ElevenError } from "./errors";
import { synthSilentMp3, buildAudioConcatArgs, runFfmpeg, assertSafeArg } from "../video/ffmpeg";
import type { VoiceScript } from "./voice-script";

const log = createLogger("elevenlabs");
const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

// Cloudflare перед api.elevenlabs.io отбивает запросы без «браузерного» User-Agent.
const USER_AGENT =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) alovlab-automation/1.0";
// Пауза между сегментами длинного скрипта — чтобы серия запросов не выглядела флудом.
const SEGMENT_GAP_MS = 600;

// Проверка, что байты — это mp3 (ID3-тег или MPEG frame sync), а не HTML-заглушка Cloudflare.
function isMp3(buf: Buffer): boolean {
  if (buf.length < 4) return false;
  if (buf[0] === 0x49 && buf[1] === 0x44 && buf[2] === 0x33) return true; // "ID3"
  if (buf[0] === 0xff && (buf[1] & 0xe0) === 0xe0) return true; // MPEG frame sync
  return false;
}

// Русская речь ≈ 2.5 слова/сек — оценка длительности сегмента для mock.
export function estimateSeconds(text: string): number {
  const words = text.trim().split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(words / 2.5));
}

function voiceSettings(): Record<string, unknown> {
  try {
    const p = path.join(config.repoRoot, "assets", "voices", "ilya-alov", "settings.json");
    return JSON.parse(fs.readFileSync(p, "utf8")).voice_settings || {};
  } catch {
    return { stability: 0.45, similarity_boost: 0.85 };
  }
}

/** Генерирует одну реплику в mp3 (mock — тишина нужной длины; real — ElevenLabs TTS). */
export async function generateSegment(text: string, dest: string): Promise<string> {
  fs.mkdirSync(path.dirname(dest), { recursive: true });

  if (config.elevenlabs.mock) {
    const ok = await synthSilentMp3(dest, estimateSeconds(text)).catch(() => false);
    if (!ok) fs.writeFileSync(dest, Buffer.from("ALOVLAB-MOCK-MP3"));
    return dest;
  }

  if (!config.elevenlabs.apiKey) throw new ElevenError("missing_key");
  if (!config.elevenlabs.voiceId) throw new ElevenError("voice_not_found");

  const url =
    `${config.elevenlabs.apiBase}/v1/text-to-speech/${encodeURIComponent(config.elevenlabs.voiceId)}` +
    `?output_format=${encodeURIComponent(config.elevenlabs.outputFormat)}`;
  const body = { text, model_id: config.elevenlabs.modelId, voice_settings: voiceSettings() };

  const MAX = 5;
  let delay = 800;
  for (let attempt = 0; attempt <= MAX; attempt++) {
    try {
      const res = await fetch(url, {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "xi-api-key": config.elevenlabs.apiKey,
          accept: "audio/mpeg",
          "user-agent": USER_AGENT,
        },
        body: JSON.stringify(body),
      });
      if (res.status === 401) throw new ElevenError("invalid_key");
      if (res.status === 404) throw new ElevenError("voice_not_found");
      // 429/403/408/409 — частота или защита Cloudflare: ждём дольше и повторяем.
      if ((res.status === 429 || res.status === 403 || res.status === 408 || res.status === 409) && attempt < MAX) {
        log.warn(`ElevenLabs HTTP ${res.status} (защита/лимит) — пауза ${delay}мс и повтор ${attempt + 1}/${MAX}`);
        await sleep(delay);
        delay = Math.min(delay * 2, 15000);
        continue;
      }
      if (!res.ok) {
        const body = (await res.text().catch(() => "")).slice(0, 300);
        // 400/422 — ошибка запроса, повторять бессмысленно; показываем причину.
        if (res.status === 400 || res.status === 422) throw new ElevenError("bad_request", body, res.status);
        if (res.status >= 500 && attempt < MAX) { await sleep(delay); delay = Math.min(delay * 2, 15000); continue; }
        throw new ElevenError("bad_response", `HTTP ${res.status}: ${body}`, res.status);
      }
      const ctype = (res.headers.get("content-type") || "").toLowerCase();
      const buf = Buffer.from(await res.arrayBuffer());
      // Cloudflare иногда отдаёт 200 с HTML-заглушкой «Just a moment…» вместо аудио.
      // Проверяем и заголовок, и сигнатуру файла — битый сегмент не должен попасть в склейку.
      if (!isMp3(buf) && !ctype.includes("audio") && !ctype.includes("mpeg")) {
        const preview = buf.toString("utf8").slice(0, 160).replace(/\s+/g, " ");
        if (attempt < MAX) {
          log.warn(`ElevenLabs вернул не аудио (${ctype || "?"}) — пауза ${delay}мс и повтор ${attempt + 1}/${MAX}`);
          await sleep(delay);
          delay = Math.min(delay * 2, 15000);
          continue;
        }
        throw new ElevenError("bad_response", `ответ не аудио (${ctype || "?"}): ${preview}`);
      }
      if (buf.length < 256) throw new ElevenError("bad_response", "пустое аудио");
      fs.writeFileSync(dest, buf);
      return dest;
    } catch (err) {
      if (err instanceof ElevenError && !err.retriable) throw err;
      if (attempt >= MAX) throw err instanceof ElevenError ? err : new ElevenError("network", String(err));
      await sleep(delay); delay = Math.min(delay * 2, 15000);
    }
  }
  throw new ElevenError("network", "исчерпаны попытки");
}

export interface VoiceoverResult {
  segments: string[];
  fullPath: string;
  metadataPath: string;
}

/**
 * Генерирует озвучку по voice_script: сегменты + склеенная полная дорожка + метаданные.
 * Голос берётся ТОЛЬКО из ELEVENLABS_VOICE_ID — не подменяется.
 */
export async function generateVoiceover(vs: VoiceScript, outDir: string, label = "voiceover"): Promise<VoiceoverResult> {
  fs.mkdirSync(outDir, { recursive: true });
  const segFiles: string[] = [];
  for (let i = 0; i < vs.segments.length; i++) {
    const seg = vs.segments[i];
    const f = path.join(outDir, `${seg.id}.mp3`);
    await generateSegment(seg.text, f);
    segFiles.push(f);
    // Пауза между реальными запросами, чтобы длинный скрипт не упёрся в Cloudflare.
    if (!config.elevenlabs.mock && i < vs.segments.length - 1) await sleep(SEGMENT_GAP_MS);
  }

  // Склейка сегментов в полную дорожку
  const listFile = path.join(outDir, "segments.txt");
  fs.writeFileSync(listFile, segFiles.map((s) => `file '${assertSafeArg(s)}'`).join("\n"), "utf8");
  const fullPath = path.join(outDir, `full_${label}.mp3`);
  if (segFiles.length === 1) {
    fs.copyFileSync(segFiles[0], fullPath);
  } else {
    await runFfmpeg(buildAudioConcatArgs(listFile, fullPath)).catch((e) => {
      log.warn("Склейка озвучки не удалась, берём первый сегмент", String(e));
      fs.copyFileSync(segFiles[0], fullPath);
    });
  }

  const metadataPath = path.join(outDir, "generation_metadata.json");
  fs.writeFileSync(
    metadataPath,
    JSON.stringify(
      {
        voice_id: vs.voice_id || config.elevenlabs.voiceId || "(env)",
        model_id: vs.model_id,
        mock: config.elevenlabs.mock,
        segments: vs.segments.map((s, i) => ({ id: s.id, file: path.basename(segFiles[i]), chars: s.text.length })),
        total_chars: vs.segments.reduce((a, s) => a + s.text.length, 0),
      },
      null,
      2
    ),
    "utf8"
  );

  log.info(`Озвучка готова (${config.elevenlabs.mock ? "mock" : "real"}): ${fullPath}`);
  return { segments: segFiles, fullPath, metadataPath };
}

/** Проверка соединения/доступа к голосу (в mock всегда ок). */
export async function checkVoice(): Promise<{ ok: boolean; message?: string }> {
  if (config.elevenlabs.mock) return { ok: true };
  if (!config.elevenlabs.apiKey) return { ok: false, message: new ElevenError("missing_key").human };
  if (!config.elevenlabs.voiceId) return { ok: false, message: new ElevenError("voice_not_found").human };
  try {
    const res = await fetch(`${config.elevenlabs.apiBase}/v1/voices/${encodeURIComponent(config.elevenlabs.voiceId)}`, {
      headers: { "xi-api-key": config.elevenlabs.apiKey, "user-agent": USER_AGENT },
    });
    if (res.status === 401) return { ok: false, message: new ElevenError("invalid_key").human };
    if (res.status === 404) return { ok: false, message: new ElevenError("voice_not_found").human };
    return { ok: res.ok };
  } catch (err) {
    return { ok: false, message: String(err) };
  }
}
