import crypto from "node:crypto";
import { config } from "../config";
import { normalizeStatus } from "./payload";
import type { HeygenVideoState } from "./types";

/**
 * Проверяет подпись вебхука HeyGen, если задан секрет.
 * HeyGen подписывает тело HMAC-SHA256. Если секрет не задан — пропускаем проверку.
 */
export function verifyWebhookSignature(rawBody: string, signature: string | undefined): boolean {
  if (!config.heygen.webhookSecret) return true; // проверка отключена
  if (!signature) return false;
  const expected = crypto.createHmac("sha256", config.heygen.webhookSecret).update(rawBody).digest("hex");
  const a = Buffer.from(expected);
  const b = Buffer.from(signature.replace(/^sha256=/, ""));
  if (a.length !== b.length) return false;
  return crypto.timingSafeEqual(a, b);
}

/** Парсит тело вебхука в единый статус. */
export function parseWebhook(body: any): HeygenVideoState | null {
  const videoId = body?.event_data?.video_id ?? body?.video_id;
  if (!videoId) return null;
  const statusMap: Record<string, any> = {
    "avatar_video.success": { status: "completed", video_url: body?.event_data?.url },
    "avatar_video.fail": { status: "failed", error: body?.event_data?.msg },
  };
  const mapped = statusMap[body?.event_type] ?? body?.event_data ?? {};
  return normalizeStatus(String(videoId), mapped);
}
