import type { SubtitleCue } from "../store/types";
import { wrapTwoLines } from "./subtitles";

function msToAss(ms: number): string {
  const h = Math.floor(ms / 3600000);
  const m = Math.floor((ms % 3600000) / 60000);
  const s = Math.floor((ms % 60000) / 1000);
  const cs = Math.floor((ms % 1000) / 10);
  const pad = (n: number, l = 2) => String(n).padStart(l, "0");
  return `${h}:${pad(m)}:${pad(s)}.${pad(cs)}`;
}

/**
 * Экспорт ASS: крупный белый текст снизу, безопасный отступ, максимум 2 строки.
 * Стиль AlovLab: белый основной, оранжевый акцент можно добавлять вручную тегом.
 */
export function toAss(cues: SubtitleCue[]): string {
  const header = [
    "[Script Info]",
    "ScriptType: v4.00+",
    "PlayResX: 1080",
    "PlayResY: 1920",
    "WrapStyle: 2",
    "",
    "[V4+ Styles]",
    "Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Alignment, MarginL, MarginR, MarginV, Outline, Shadow",
    // Alignment 2 = снизу по центру; MarginV 220 = безопасный отступ, не перекрывает лицо
    "Style: Alov,Manrope,64,&H00FFFFFF,&H00000000,&H64000000,1,2,80,80,220,4,1",
    "",
    "[Events]",
    "Format: Layer, Start, End, Style, Text",
  ].join("\n");

  const events = cues
    .map((c) => `Dialogue: 0,${msToAss(c.startMs)},${msToAss(c.endMs)},Alov,${wrapTwoLines(c.text).replace(/\n/g, "\\N")}`)
    .join("\n");

  return `${header}\n${events}\n`;
}
