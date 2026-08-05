import { config } from "../config";
import { createLogger } from "../logger";

const log = createLogger("llm");

// Абстракция над текстовой моделью. Проект не привязан к одному провайдеру:
// по умолчанию работает офлайн-движок (template) — ключ не нужен, всё тестируется.
// Если LLM_PROVIDER=anthropic и есть ключ — можно подключить реальную модель.

export interface LlmMessage {
  role: "system" | "user";
  content: string;
}

/**
 * Возвращает сырой ответ модели или null, если провайдер = template
 * (тогда генератор использует встроенный шаблонный движок).
 */
export async function maybeComplete(messages: LlmMessage[]): Promise<string | null> {
  if (config.llm.provider !== "anthropic") return null;
  if (!config.llm.anthropicKey) {
    log.warn("LLM_PROVIDER=anthropic, но ANTHROPIC_API_KEY пуст — работаем на шаблонном движке");
    return null;
  }
  try {
    const system = messages.filter((m) => m.role === "system").map((m) => m.content).join("\n\n");
    const user = messages.filter((m) => m.role === "user").map((m) => m.content).join("\n\n");
    const res = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-api-key": config.llm.anthropicKey,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: config.llm.anthropicModel,
        max_tokens: 4096,
        system,
        messages: [{ role: "user", content: user }],
      }),
    });
    if (!res.ok) {
      log.error(`Anthropic ответил ${res.status} — падаем на шаблонный движок`);
      return null;
    }
    const data = (await res.json()) as { content?: Array<{ text?: string }> };
    const text = data.content?.map((c) => c.text || "").join("") || "";
    return text || null;
  } catch (err) {
    log.error("LLM запрос упал — шаблонный движок", String(err));
    return null;
  }
}

/** Достаёт первый JSON-объект из текста модели (модель может обернуть его в ```). */
export function extractJson(text: string): string | null {
  const fenced = text.match(/```(?:json)?\s*([\s\S]*?)```/i);
  const candidate = fenced ? fenced[1] : text;
  const start = candidate.indexOf("{");
  const end = candidate.lastIndexOf("}");
  if (start === -1 || end === -1 || end <= start) return null;
  return candidate.slice(start, end + 1);
}
