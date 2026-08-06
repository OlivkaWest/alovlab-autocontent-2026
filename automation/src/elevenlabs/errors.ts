export type ElevenErrorKind =
  | "missing_key"
  | "invalid_key"
  | "voice_not_found"
  | "rate_limit"
  | "timeout"
  | "network"
  | "bad_response"
  | "bad_request"
  | "quota";

const RETRIABLE: ElevenErrorKind[] = ["rate_limit", "timeout", "network", "bad_response"];

const HUMAN: Record<ElevenErrorKind, string> = {
  missing_key: "ElevenLabs не подключён: не задан ELEVENLABS_API_KEY.",
  invalid_key: "ElevenLabs отклонил ключ. Проверь ELEVENLABS_API_KEY.",
  voice_not_found: "Голос ElevenLabs не найден. Проверь ELEVENLABS_VOICE_ID.",
  rate_limit: "ElevenLabs ограничил частоту запросов. Повторим позже.",
  timeout: "ElevenLabs не ответил вовремя. Повторим.",
  network: "Сеть недоступна. Повторим.",
  bad_response: "ElevenLabs вернул неожиданный ответ. Повторим.",
  bad_request: "ElevenLabs отклонил запрос (проверь голос, model_id и формат).",
  quota: "Исчерпан лимит символов ElevenLabs.",
};

export class ElevenError extends Error {
  kind: ElevenErrorKind;
  retriable: boolean;
  status?: number;
  constructor(kind: ElevenErrorKind, detail?: string, status?: number) {
    super(HUMAN[kind] + (detail ? ` (${detail})` : ""));
    this.name = "ElevenError";
    this.kind = kind;
    this.retriable = RETRIABLE.includes(kind);
    this.status = status;
  }
  get human(): string {
    return HUMAN[this.kind];
  }
}
