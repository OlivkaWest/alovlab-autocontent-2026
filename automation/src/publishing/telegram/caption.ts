import { findBannedPhrases } from "../../content/style";

export interface CaptionInput {
  kind: "reel" | "podcast" | "audiopost";
  title: string;
  hook: string;
  body?: string;
  cta?: string;
  link?: string;
  durationSeconds?: number;
  timecodes?: Array<{ at: string; label: string }>;
}

// Живая подпись без канцелярщины и штампов «в новом выпуске мы поговорим».
export function buildCaption(input: CaptionInput): string {
  const lines: string[] = [];
  lines.push(`<b>${escapeHtml(input.hook || input.title)}</b>`);
  lines.push("");
  if (input.body) lines.push(escapeHtml(input.body.trim()));
  if (input.timecodes?.length) {
    lines.push("");
    for (const t of input.timecodes) lines.push(`${t.at} — ${escapeHtml(t.label)}`);
  }
  if (input.cta) {
    lines.push("");
    lines.push(escapeHtml(input.cta.trim()));
  }
  if (input.link) lines.push(input.link);
  return lines.join("\n").trim();
}

function escapeHtml(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

/** Проверка подписи на канцелярщину (для интерфейса). */
export function auditCaption(text: string) {
  return findBannedPhrases(text, "telegram_caption");
}
