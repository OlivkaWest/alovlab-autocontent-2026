import { config, maskSecret } from "../config";
import { createLogger } from "../logger";
import { HeygenError, classifyStatus, type HeygenErrorKind } from "./errors";

const log = createLogger("heygen-client");

export interface RetryOptions {
  retries?: number; // сколько раз повторять временные ошибки
  baseDelayMs?: number; // старт бэкоффа
  timeoutMs?: number; // таймаут одного запроса
  sleep?: (ms: number) => Promise<void>; // для тестов
}

const defaultSleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

/**
 * HTTP-запрос к HeyGen с таймаутом и retry с экспоненциальным бэкоффом.
 * Повторяем ТОЛЬКО временные ошибки. Не запускаем бесконечные повторы.
 */
export async function heygenFetch(
  pathname: string,
  init: { method?: string; body?: unknown } = {},
  opts: RetryOptions = {}
): Promise<any> {
  if (!config.heygen.apiKey) throw new HeygenError("missing_key");

  const retries = opts.retries ?? 3;
  const baseDelay = opts.baseDelayMs ?? 500;
  const timeoutMs = opts.timeoutMs ?? 30000;
  const sleep = opts.sleep ?? defaultSleep;
  const url = `${config.heygen.apiBase}${pathname}`;

  let lastErr: HeygenError | null = null;
  for (let attempt = 0; attempt <= retries; attempt++) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    try {
      const res = await fetch(url, {
        method: init.method || "GET",
        headers: {
          "content-type": "application/json",
          "x-api-key": config.heygen.apiKey,
          accept: "application/json",
        },
        body: init.body ? JSON.stringify(init.body) : undefined,
        signal: controller.signal,
      });
      clearTimeout(timer);

      if (!res.ok) {
        const kind: HeygenErrorKind = classifyStatus(res.status);
        const detail = await res.text().catch(() => "");
        const err = new HeygenError(kind, detail.slice(0, 200), res.status);
        if (err.retriable && attempt < retries) {
          lastErr = err;
          const delay = baseDelay * 2 ** attempt;
          log.warn(`HeyGen ${res.status} (${maskSecret(config.heygen.apiKey)}), повтор через ${delay}мс`);
          await sleep(delay);
          continue;
        }
        throw err;
      }
      return await res.json();
    } catch (err: any) {
      clearTimeout(timer);
      if (err instanceof HeygenError) {
        if (err.retriable && attempt < retries) {
          lastErr = err;
          await sleep(baseDelay * 2 ** attempt);
          continue;
        }
        throw err;
      }
      // Сеть/таймаут
      const kind: HeygenErrorKind = err?.name === "AbortError" ? "timeout" : "network";
      const wrapped = new HeygenError(kind, String(err?.message || err));
      if (attempt < retries) {
        lastErr = wrapped;
        await sleep(baseDelay * 2 ** attempt);
        continue;
      }
      throw wrapped;
    }
  }
  throw lastErr ?? new HeygenError("unknown");
}

/** Проверка соединения с HeyGen (список аватаров как ping). */
export async function checkConnection(opts?: RetryOptions): Promise<boolean> {
  if (config.heygen.mock) return true;
  await heygenFetch("/v2/avatars", {}, { retries: 1, ...opts });
  return true;
}
