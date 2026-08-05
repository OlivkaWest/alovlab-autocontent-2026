import fs from "node:fs";
import path from "node:path";
import { config } from "../config";

// Адаптация письменного текста под живую озвучку + словарь произношения.

let dictCache: Record<string, string> | null = null;

export function loadPronunciation(): Record<string, string> {
  if (dictCache) return dictCache;
  const p = path.join(config.repoRoot, "assets", "voices", "ilya-alov", "pronunciation.json");
  try {
    dictCache = JSON.parse(fs.readFileSync(p, "utf8"));
  } catch {
    dictCache = {};
  }
  return dictCache!;
}

/** Применяет словарь произношения (только к голосовой версии, не к исходнику). */
export function applyPronunciation(text: string, dict = loadPronunciation()): string {
  let out = text;
  // Длинные ключи первыми, чтобы «Claude Code» сработал раньше «Claude».
  for (const key of Object.keys(dict).sort((a, b) => b.length - a.length)) {
    out = out.split(key).join(dict[key]);
  }
  return out;
}

/**
 * Готовит текст к озвучке: убирает ссылки, скобки, лишние пробелы,
 * markdown-разметку. Исходный текст не меняется — это отдельная голосовая версия.
 */
export function adaptForSpeech(text: string): string {
  let t = text;
  t = t.replace(/```[\s\S]*?```/g, " "); // код-блоки
  t = t.replace(/!?\[([^\]]*)\]\([^)]*\)/g, "$1"); // markdown-ссылки → текст
  t = t.replace(/https?:\/\/\S+/g, " "); // голые ссылки убираем
  t = t.replace(/[*_#>`]/g, ""); // markdown-символы
  t = t.replace(/\([^)]*\)/g, " "); // скобки
  t = t.replace(/[ \t]+/g, " ");
  t = t.replace(/\n{2,}/g, "\n\n");
  return t.trim();
}

export interface VoiceSegment {
  id: string;
  text: string;
  delivery: string;
  pace: string;
  pause_after_ms: number;
}

// Дробим по смыслу: по абзацам, длинные абзацы — по предложениям.
function segmentText(text: string): string[] {
  const paras = text.split(/\n{2,}/).map((s) => s.trim()).filter(Boolean);
  const out: string[] = [];
  for (const p of paras) {
    if (p.length <= 320) {
      out.push(p);
    } else {
      const sentences = p.split(/(?<=[.!?…])\s+/);
      let cur = "";
      for (const s of sentences) {
        if ((cur + " " + s).trim().length > 320) {
          if (cur) out.push(cur.trim());
          cur = s;
        } else cur = (cur + " " + s).trim();
      }
      if (cur) out.push(cur.trim());
    }
  }
  return out.length ? out : [text.trim()];
}

export interface VoiceScript {
  language: string;
  voice_id: string;
  model_id: string;
  segments: VoiceSegment[];
}

/** Строит voice_script (для сохранения в json) из готового текста. */
export function buildVoiceScript(
  rawText: string,
  opts: { delivery?: string; pace?: string } = {}
): VoiceScript {
  const speechText = applyPronunciation(adaptForSpeech(rawText));
  const parts = segmentText(speechText);
  return {
    language: "ru",
    voice_id: config.elevenlabs.voiceId,
    model_id: config.elevenlabs.modelId,
    segments: parts.map((text, i) => ({
      id: `segment_${String(i + 1).padStart(2, "0")}`,
      text,
      delivery: opts.delivery || "confident",
      pace: opts.pace || "medium",
      pause_after_ms: 300,
    })),
  };
}

/** Человеческий markdown голосового сценария. */
export function voiceScriptToMd(vs: VoiceScript): string {
  return (
    `# Голосовой сценарий\n\nГолос: ${vs.voice_id || "(ELEVENLABS_VOICE_ID)"} · модель: ${vs.model_id} · язык: ${vs.language}\n\n` +
    vs.segments.map((s) => `## ${s.id} [${s.delivery}, ${s.pace}]\n${s.text}`).join("\n\n") +
    "\n"
  );
}
