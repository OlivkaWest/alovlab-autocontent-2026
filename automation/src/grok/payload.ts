import fs from "node:fs";
import { GrokError } from "./errors";
import type { GrokVideoInput } from "./types";

export const MAX_GROK_DURATION = 10;

/**
 * Формирует тело запроса генерации видео xAI.
 * ВНИМАНИЕ: точная схema эндпоинта видео xAI должна быть сверена с официальной
 * документацией перед реальным запуском (см. README, раздел Grok). Здесь —
 * нейтральный, читаемый payload; поля маппятся при подтверждении схемы.
 */
export function buildGrokPayload(model: string, input: GrokVideoInput): Record<string, unknown> {
  const prompt = (input.prompt || "").trim();
  if (!prompt) throw new GrokError("bad_response", "пустой промпт");
  if (input.durationSeconds < 1 || input.durationSeconds > MAX_GROK_DURATION) {
    throw new GrokError("unsupported", `длительность вне диапазона 1..${MAX_GROK_DURATION}с`);
  }
  const payload: Record<string, unknown> = {
    model,
    prompt,
    duration: input.durationSeconds,
    aspect_ratio: input.aspectRatio,
    resolution: input.resolution,
  };
  if (input.negativePrompt) payload.negative_prompt = input.negativePrompt;
  if (input.mode === "image_to_video") {
    if (!input.imagePath || !fs.existsSync(input.imagePath)) {
      throw new GrokError("bad_response", "нет исходного изображения для image-to-video");
    }
    // Реальный вызов кодирует изображение по требованиям API (base64/URL) при подтверждении схемы.
    payload.image = `file://${input.imagePath}`;
  }
  return payload;
}
