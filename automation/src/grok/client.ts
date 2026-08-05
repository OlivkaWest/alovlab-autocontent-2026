import fs from "node:fs";
import path from "node:path";
import { config } from "../config";
import { createLogger } from "../logger";
import { GrokError } from "./errors";
import { buildGrokPayload, MAX_GROK_DURATION } from "./payload";
import { mockCreate, mockStatus, mockDownload } from "./mock";
import type { GrokVideoInput, GrokVideoState } from "./types";

const log = createLogger("grok");
const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

export { MAX_GROK_DURATION };

/**
 * Создаёт задачу генерации видео в Grok (или mock).
 * Реальный путь намеренно ЗАКРЫТ, пока не подтверждён официальный endpoint xAI:
 * задай XAI_VIDEO_ENDPOINT в .env только после сверки с документацией.
 */
export async function grokCreateVideo(input: GrokVideoInput): Promise<{ requestId: string; mock: boolean }> {
  const payload = buildGrokPayload(config.grok.model, input); // валидирует вход

  if (config.grok.mock) {
    const { requestId } = mockCreate(input);
    log.info(`[mock] создана Grok-задача ${requestId}`);
    return { requestId, mock: true };
  }

  if (!config.grok.apiKey) throw new GrokError("missing_key");
  // Подтверждённый по докам xAI async-паттерн: POST /v1/videos/generations → request_id.
  // Путь переопределяется через XAI_VIDEO_ENDPOINT, если xAI изменит схему.
  const endpoint = process.env.XAI_VIDEO_ENDPOINT || "/v1/videos/generations";

  const res = await withRetry(() =>
    fetch(`${config.grok.apiBase}${endpoint}`, {
      method: "POST",
      headers: { "content-type": "application/json", authorization: `Bearer ${config.grok.apiKey}` },
      body: JSON.stringify(payload),
    })
  );
  const data = await res.json().catch(() => ({}));
  const requestId = (data as any)?.request_id ?? (data as any)?.id;
  if (!requestId) throw new GrokError("bad_response", "в ответе нет request_id");
  return { requestId: String(requestId), mock: false };
}

export async function grokGetStatus(requestId: string): Promise<GrokVideoState> {
  if (config.grok.mock || requestId.startsWith("grok_mock_")) return mockStatus(requestId);
  // Подтверждено: GET /v1/videos/{request_id} → status; "done" = готово, есть url и duration.
  const base = process.env.XAI_VIDEO_STATUS_ENDPOINT || "/v1/videos";
  const res = await withRetry(() =>
    fetch(`${config.grok.apiBase}${base}/${encodeURIComponent(requestId)}`, {
      headers: { authorization: `Bearer ${config.grok.apiKey}` },
    })
  );
  const d: any = await res.json().catch(() => ({}));
  const raw = String(d.status || "").toLowerCase();
  const status =
    raw === "done" || raw === "completed" || raw === "success"
      ? "completed"
      : raw === "failed" || raw === "error"
        ? "failed"
        : raw === "processing" || raw === "running"
          ? "processing"
          : "pending";
  const videoUrl = d.video_url ?? d.url ?? d.video?.url ?? (Array.isArray(d.videos) ? d.videos[0]?.url : null) ?? null;
  return { requestId, status, videoUrl, progress: status === "completed" ? 100 : 50, error: d.error ? String(d.error?.message ?? d.error) : null };
}

export async function grokDownload(videoUrl: string, destPath: string, requestId = ""): Promise<string> {
  fs.mkdirSync(path.dirname(destPath), { recursive: true });
  if (config.grok.mock || videoUrl.startsWith("mock://")) return mockDownload(requestId || "grok", destPath);
  const res = await fetch(videoUrl).catch((e) => {
    throw new GrokError("download_failed", String(e?.message || e));
  });
  if (!res.ok) throw new GrokError("download_failed", `HTTP ${res.status}`);
  const buf = Buffer.from(await res.arrayBuffer());
  if (buf.length < 1024) throw new GrokError("download_failed", "подозрительно маленький файл");
  fs.writeFileSync(destPath, buf);
  return destPath;
}

// Ретрай только временных ошибок, экспоненциальный бэкофф, ограниченный.
async function withRetry(fn: () => Promise<Response>, retries = 3): Promise<Response> {
  let delay = 500;
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const res = await fn();
      if (res.status === 401 || res.status === 403) throw new GrokError("invalid_key", "", res.status);
      if (res.status === 429 && attempt < retries) {
        await sleep(delay);
        delay *= 2;
        continue;
      }
      if (res.status >= 500 && attempt < retries) {
        await sleep(delay);
        delay *= 2;
        continue;
      }
      return res;
    } catch (err) {
      if (err instanceof GrokError && !err.retriable) throw err;
      if (attempt >= retries) throw err instanceof GrokError ? err : new GrokError("network", String(err));
      await sleep(delay);
      delay *= 2;
    }
  }
  throw new GrokError("network", "исчерпаны попытки");
}
