import fs from "node:fs";
import path from "node:path";
import { config, maskSecret } from "../../config";
import { createLogger } from "../../logger";

const log = createLogger("telegram");

export type TelegramMethod = "sendAudio" | "sendVideo" | "sendDocument" | "sendPhoto" | "sendMessage";

export interface PublishInput {
  method: TelegramMethod;
  filePath?: string; // локальный файл (audio/video/photo/document)
  caption?: string;
  parseMode?: "HTML" | "MarkdownV2";
  // метаданные аудио
  title?: string;
  performer?: string;
  durationSeconds?: number;
  thumbnail?: string;
}

export interface PublishResult {
  mode: "draft" | "live";
  ok: boolean;
  method: TelegramMethod;
  payloadPath?: string;
  messageId?: number;
  error?: string;
}

function payloadFor(input: PublishInput) {
  const p: Record<string, unknown> = {
    method: input.method,
    chat_id: config.telegram.channelId || "(TELEGRAM_CHANNEL_ID)",
    parse_mode: input.parseMode || "HTML",
  };
  if (input.caption) p.caption = input.caption;
  if (input.filePath) p.file = path.basename(input.filePath);
  if (input.title) p.title = input.title;
  if (input.performer) p.performer = input.performer;
  if (input.durationSeconds) p.duration = Math.round(input.durationSeconds);
  if (input.thumbnail) p.thumbnail = path.basename(input.thumbnail);
  return p;
}

/**
 * Публикация в Telegram через Bot API. По умолчанию режим DRAFT:
 * реальный запрос НЕ отправляется, payload и подпись сохраняются на диск.
 * LIVE — только при TELEGRAM_PUBLISH_MODE=live и пройденных проверках.
 */
export async function publish(input: PublishInput, outDir: string): Promise<PublishResult> {
  fs.mkdirSync(outDir, { recursive: true });
  const payload = payloadFor(input);
  const payloadPath = path.join(outDir, `telegram_${input.method}_payload.json`);
  fs.writeFileSync(payloadPath, JSON.stringify(payload, null, 2), "utf8");

  if (config.telegram.publishMode !== "live") {
    log.info(`[draft] ${input.method} → payload сохранён (${maskSecret(config.telegram.botToken)})`);
    return { mode: "draft", ok: true, method: input.method, payloadPath };
  }

  // LIVE
  if (!config.telegram.botToken) return { mode: "live", ok: false, method: input.method, error: "нет TELEGRAM_BOT_TOKEN" };
  if (!config.telegram.channelId) return { mode: "live", ok: false, method: input.method, error: "нет TELEGRAM_CHANNEL_ID" };
  if (input.filePath && !fs.existsSync(input.filePath)) {
    return { mode: "live", ok: false, method: input.method, error: `файл не найден: ${input.filePath}` };
  }

  try {
    const url = `https://api.telegram.org/bot${config.telegram.botToken}/${input.method}`;
    const form = new FormData();
    form.append("chat_id", config.telegram.channelId);
    if (input.caption) form.append("caption", input.caption);
    form.append("parse_mode", input.parseMode || "HTML");
    if (input.title) form.append("title", input.title);
    if (input.performer) form.append("performer", input.performer);
    if (input.durationSeconds) form.append("duration", String(Math.round(input.durationSeconds)));
    if (input.filePath) {
      const field = input.method === "sendAudio" ? "audio" : input.method === "sendVideo" ? "video" : input.method === "sendPhoto" ? "photo" : "document";
      const bytes = fs.readFileSync(input.filePath);
      form.append(field, new Blob([bytes]), path.basename(input.filePath));
    }
    const res = await fetch(url, { method: "POST", body: form });
    const data: any = await res.json().catch(() => ({}));
    if (!res.ok || !data.ok) {
      return { mode: "live", ok: false, method: input.method, error: `Telegram: ${data.description || res.status}`, payloadPath };
    }
    return { mode: "live", ok: true, method: input.method, messageId: data.result?.message_id, payloadPath };
  } catch (err) {
    return { mode: "live", ok: false, method: input.method, error: String(err), payloadPath };
  }
}

/**
 * Публикация альбома фото (карточки карусели) через sendMediaGroup.
 * До 10 фото за раз. Подпись — на первой карточке. Draft — только payload.
 */
export async function publishMediaGroup(photos: string[], caption: string, outDir: string): Promise<PublishResult> {
  fs.mkdirSync(outDir, { recursive: true });
  const files = photos.filter((p) => fs.existsSync(p)).slice(0, 10);
  const media = files.map((f, i) => ({
    type: "photo",
    media: `attach://photo${i}`,
    ...(i === 0 && caption ? { caption, parse_mode: "HTML" } : {}),
  }));
  const payloadPath = path.join(outDir, "telegram_sendMediaGroup_payload.json");
  fs.writeFileSync(payloadPath, JSON.stringify({ method: "sendMediaGroup", chat_id: config.telegram.channelId || "(TELEGRAM_CHANNEL_ID)", media: media.map((m, i) => ({ ...m, media: path.basename(files[i]) })) }, null, 2), "utf8");

  if (config.telegram.publishMode !== "live") {
    log.info(`[draft] sendMediaGroup (${files.length} фото) → payload сохранён`);
    return { mode: "draft", ok: true, method: "sendPhoto", payloadPath };
  }
  if (!config.telegram.botToken || !config.telegram.channelId) {
    return { mode: "live", ok: false, method: "sendPhoto", error: "нет TELEGRAM_BOT_TOKEN/CHANNEL_ID", payloadPath };
  }
  if (!files.length) return { mode: "live", ok: false, method: "sendPhoto", error: "нет карточек для альбома", payloadPath };

  try {
    const form = new FormData();
    form.append("chat_id", config.telegram.channelId);
    form.append("media", JSON.stringify(media));
    files.forEach((f, i) => form.append(`photo${i}`, new Blob([fs.readFileSync(f)]), path.basename(f)));
    const res = await fetch(`https://api.telegram.org/bot${config.telegram.botToken}/sendMediaGroup`, { method: "POST", body: form });
    const data: any = await res.json().catch(() => ({}));
    if (!res.ok || !data.ok) return { mode: "live", ok: false, method: "sendPhoto", error: `Telegram: ${data.description || res.status}`, payloadPath };
    return { mode: "live", ok: true, method: "sendPhoto", messageId: data.result?.[0]?.message_id, payloadPath };
  } catch (err) {
    return { mode: "live", ok: false, method: "sendPhoto", error: String(err), payloadPath };
  }
}

/** Проверки перед первой реальной публикацией. */
export function livePreflight(): { ok: boolean; issues: string[] } {
  const issues: string[] = [];
  if (config.telegram.publishMode !== "live") issues.push("TELEGRAM_PUBLISH_MODE=draft (по умолчанию безопасно)");
  if (!config.telegram.botToken) issues.push("нет TELEGRAM_BOT_TOKEN");
  if (!config.telegram.channelId) issues.push("нет TELEGRAM_CHANNEL_ID");
  return { ok: issues.length === 0, issues };
}
