// Ошибки HeyGen с понятными русскими сообщениями и признаком «временная».
export type HeygenErrorKind =
  | "missing_key"
  | "invalid_key"
  | "egress_blocked"
  | "avatar_unavailable"
  | "voice_unavailable"
  | "rate_limit"
  | "insufficient_credits"
  | "timeout"
  | "network"
  | "bad_response"
  | "video_failed"
  | "download_failed"
  | "unknown";

// Какие ошибки имеет смысл повторять (временные).
const RETRIABLE: HeygenErrorKind[] = ["rate_limit", "timeout", "network", "bad_response"];

const HUMAN: Record<HeygenErrorKind, string> = {
  missing_key: "HeyGen не подключён: не задан API-ключ. Добавь HEYGEN_API_KEY в настройки проекта.",
  invalid_key: "HeyGen отклонил ключ. Проверь HEYGEN_API_KEY.",
  egress_blocked:
    "Сеть окружения блокирует api.heygen.com (egress-политика). Ключ ни при чём. " +
    "Добавь api.heygen.com (и api.x.ai) в разрешённые хосты окружения Claude Code или запусти automation/ локально.",
  avatar_unavailable: "Аватар недоступен. Проверь HEYGEN_AVATAR_ID.",
  voice_unavailable: "Голос недоступен. Проверь HEYGEN_VOICE_ID.",
  rate_limit: "HeyGen ограничил частоту запросов. Повторим чуть позже.",
  insufficient_credits: "На аккаунте HeyGen не хватает кредитов.",
  timeout: "HeyGen не ответил вовремя. Повторим.",
  network: "Сеть недоступна. Повторим.",
  bad_response: "HeyGen вернул неожиданный ответ. Повторим.",
  video_failed: "HeyGen не смог собрать видео. Перегенерируй сцену.",
  download_failed: "Не удалось скачать готовое видео.",
  unknown: "Неизвестная ошибка HeyGen.",
};

export class HeygenError extends Error {
  kind: HeygenErrorKind;
  status?: number;
  retriable: boolean;

  constructor(kind: HeygenErrorKind, detail?: string, status?: number) {
    super(HUMAN[kind] + (detail ? ` (${detail})` : ""));
    this.name = "HeygenError";
    this.kind = kind;
    this.status = status;
    this.retriable = RETRIABLE.includes(kind);
  }

  /** Человеческое сообщение без stack trace для интерфейса. */
  get human(): string {
    return HUMAN[this.kind];
  }
}

/** Классифицирует HTTP-статус в тип ошибки. */
export function classifyStatus(status: number): HeygenErrorKind {
  if (status === 401 || status === 403) return "invalid_key";
  if (status === 402) return "insufficient_credits";
  if (status === 404) return "avatar_unavailable";
  if (status === 429) return "rate_limit";
  if (status >= 500) return "bad_response";
  return "unknown";
}
