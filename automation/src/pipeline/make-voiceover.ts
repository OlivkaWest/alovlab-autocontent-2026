import fs from "node:fs";
import path from "node:path";
import { subDir, writeVersioned, appendLog } from "../project/day-store";
import { voiceReady } from "../config";
import { buildVoiceScript, voiceScriptToMd } from "../elevenlabs/voice-script";
import { generateVoiceover } from "../elevenlabs/client";
import { createLogger } from "../logger";

const log = createLogger("voiceover");

export interface VoiceoverOut {
  ok: boolean;
  message?: string;
  voiceScriptPath?: string;
  fullPath?: string;
  segments?: number;
}

/**
 * Готовит озвучку моим голосом по тексту: адаптация под речь → voice_script →
 * ElevenLabs → полная дорожка. Используется командой `voiceover` и внутри reel/podcast.
 */
export async function makeVoiceover(
  date: string,
  rawText: string,
  opts: { label?: string; delivery?: string; pace?: string } = {}
): Promise<VoiceoverOut> {
  const v = voiceReady();
  if (!v.ready) return { ok: false, message: v.message };
  if (!rawText.trim()) return { ok: false, message: "Пустой текст для озвучки." };

  const label = opts.label || "voiceover";
  const audioDir = subDir(date, "reels", "audio");

  const vs = buildVoiceScript(rawText, { delivery: opts.delivery, pace: opts.pace });
  const { path: vsJson } = writeVersioned(audioDir, `voice_script_${label}`, "json", JSON.stringify(vs, null, 2));
  fs.writeFileSync(path.join(audioDir, `voice_script_${label}.md`), voiceScriptToMd(vs), "utf8");

  const res = await generateVoiceover(vs, path.join(audioDir, label), label);
  appendLog(date, `Озвучка «${label}»: ${vs.segments.length} сегм. → ${path.basename(res.fullPath)}`);
  log.info(`voiceover ${label} → ${res.fullPath}`);

  return { ok: true, voiceScriptPath: vsJson, fullPath: res.fullPath, segments: vs.segments.length };
}
