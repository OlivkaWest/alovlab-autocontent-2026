import fs from "node:fs";
import path from "node:path";
import { config } from "../config";
import { createLogger } from "../logger";
import { ElevenError } from "./errors";
import { synthSilentMp3, buildAudioConcatArgs, runFfmpeg, assertSafeArg } from "../video/ffmpeg";
import type { VoiceScript } from "./voice-script";

const log = createLogger("elevenlabs");
const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

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

  let delay = 500;
  for (let attempt = 0; attempt <= 3; attempt++) {
    try {
      const res = await fetch(url, {
        method: "POST",
        headers: { "content-type": "application/json", "xi-api-key": config.elevenlabs.apiKey, accept: "audio/mpeg" },
        body: JSON.stringify(body),
      });
      if (res.status === 401) throw new ElevenError("invalid_key");
      if (res.status === 404) throw new ElevenError("voice_not_found");
      if (res.status === 429 && attempt < 3) { await sleep(delay); delay *= 2; continue; }
      if (!res.ok) {
        if (res.status >= 500 && attempt < 3) { await sleep(delay); delay *= 2; continue; }
        throw new ElevenError("bad_response", `HTTP ${res.status}`, res.status);
      }
      const buf = Buffer.from(await res.arrayBuffer());
      if (buf.length < 256) throw new ElevenError("bad_response", "пустое аудио");
      fs.writeFileSync(dest, buf);
      return dest;
    } catch (err) {
      if (err instanceof ElevenError && !err.retriable) throw err;
      if (attempt >= 3) throw err instanceof ElevenError ? err : new ElevenError("network", String(err));
      await sleep(delay); delay *= 2;
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
  for (const seg of vs.segments) {
    const f = path.join(outDir, `${seg.id}.mp3`);
    await generateSegment(seg.text, f);
    segFiles.push(f);
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
      headers: { "xi-api-key": config.elevenlabs.apiKey },
    });
    if (res.status === 401) return { ok: false, message: new ElevenError("invalid_key").human };
    if (res.status === 404) return { ok: false, message: new ElevenError("voice_not_found").human };
    return { ok: res.ok };
  } catch (err) {
    return { ok: false, message: String(err) };
  }
}
