import fs from "node:fs";
import { SubtitleCue, type ReelsScript, type Scene } from "../store/types";

// Короткие смысловые блоки: не длиннее ~42 символов и не больше 2 строк.
const MAX_LINE = 42;

function splitIntoCues(text: string): string[] {
  const clean = text.replace(/\s+/g, " ").trim();
  if (!clean) return [];
  const words = clean.split(" ");
  const chunks: string[] = [];
  let cur = "";
  for (const w of words) {
    if ((cur + " " + w).trim().length > MAX_LINE * 2) {
      if (cur) chunks.push(cur.trim());
      cur = w;
    } else {
      cur = (cur + " " + w).trim();
    }
  }
  if (cur) chunks.push(cur.trim());
  return chunks;
}

/** Разбивает строку на максимум 2 строки для показа снизу. */
export function wrapTwoLines(text: string): string {
  if (text.length <= MAX_LINE) return text;
  const words = text.split(" ");
  let line1 = "";
  let i = 0;
  for (; i < words.length; i++) {
    if ((line1 + " " + words[i]).trim().length > MAX_LINE) break;
    line1 = (line1 + " " + words[i]).trim();
  }
  const line2 = words.slice(i).join(" ");
  return line2 ? `${line1}\n${line2}` : line1;
}

/**
 * Строит субтитры из сцен: по каждой активной сцене — короткие блоки,
 * равномерно распределённые внутри её длительности.
 */
export function buildSubtitles(script: ReelsScript): SubtitleCue[] {
  const cues: SubtitleCue[] = [];
  let cursorMs = 0;
  let index = 1;
  for (const scene of script.scenes as Scene[]) {
    const durMs = Math.round(scene.durationSeconds * 1000);
    if (scene.disabled) {
      cursorMs += durMs;
      continue;
    }
    const source = scene.subtitle || scene.spokenText || scene.onScreenText;
    const blocks = splitIntoCues(source);
    if (blocks.length === 0) {
      cursorMs += durMs;
      continue;
    }
    const per = Math.floor(durMs / blocks.length);
    blocks.forEach((b, i) => {
      const start = cursorMs + i * per;
      const end = i === blocks.length - 1 ? cursorMs + durMs : start + per - 40;
      cues.push(SubtitleCue.parse({ index: index++, startMs: start, endMs: Math.max(end, start + 300), text: b }));
    });
    cursorMs += durMs;
  }
  return cues;
}

function msToSrtTime(ms: number): string {
  const h = Math.floor(ms / 3600000);
  const m = Math.floor((ms % 3600000) / 60000);
  const s = Math.floor((ms % 60000) / 1000);
  const millis = ms % 1000;
  const pad = (n: number, l = 2) => String(n).padStart(l, "0");
  return `${pad(h)}:${pad(m)}:${pad(s)},${pad(millis, 3)}`;
}

/** Экспорт SRT. */
export function toSrt(cues: SubtitleCue[]): string {
  return (
    cues
      .map((c) => `${c.index}\n${msToSrtTime(c.startMs)} --> ${msToSrtTime(c.endMs)}\n${wrapTwoLines(c.text)}`)
      .join("\n\n") + "\n"
  );
}

/** Экспорт JSON с таймкодами. */
export function toJson(cues: SubtitleCue[]): string {
  return JSON.stringify(cues, null, 2);
}

export function writeSubtitleFiles(cues: SubtitleCue[], srtPath: string, jsonPath: string): void {
  fs.writeFileSync(srtPath, toSrt(cues), "utf8");
  fs.writeFileSync(jsonPath, toJson(cues), "utf8");
}
