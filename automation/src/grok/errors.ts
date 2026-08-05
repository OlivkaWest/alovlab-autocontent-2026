// Ошибки Grok (xAI) с признаком временной и русскими сообщениями.
export type GrokErrorKind =
  | "missing_key"
  | "invalid_key"
  | "rate_limit"
  | "timeout"
  | "network"
  | "bad_response"
  | "video_failed"
  | "download_failed"
  | "unsupported";

const RETRIABLE: GrokErrorKind[] = ["rate_limit", "timeout", "network", "bad_response"];

const HUMAN: Record<GrokErrorKind, string> = {
  missing_key: "Grok не подключён: не задан XAI_API_KEY.",
  invalid_key: "xAI отклонил ключ. Проверь XAI_API_KEY.",
  rate_limit: "xAI ограничил частоту запросов. Повторим позже.",
  timeout: "xAI не ответил вовремя. Повторим.",
  network: "Сеть недоступна. Повторим.",
  bad_response: "xAI вернул неожиданный ответ. Повторим.",
  video_failed: "Grok не смог собрать сцену. Упрости промпт или используй запасной генератор.",
  download_failed: "Не удалось скачать сцену Grok.",
  unsupported:
    "Функция видео xAI не подтверждена официальной документацией. Проверь актуальные endpoints перед реальным запуском.",
};

export class GrokError extends Error {
  kind: GrokErrorKind;
  retriable: boolean;
  status?: number;
  constructor(kind: GrokErrorKind, detail?: string, status?: number) {
    super(HUMAN[kind] + (detail ? ` (${detail})` : ""));
    this.name = "GrokError";
    this.kind = kind;
    this.retriable = RETRIABLE.includes(kind);
    this.status = status;
  }
  get human(): string {
    return HUMAN[this.kind];
  }
}
