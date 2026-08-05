import { HeygenError } from "./errors";
import type { CreateVideoInput, HeygenVideoState, HeygenVideoStatus } from "./types";

// Разумный предел длины реплики одной сцены (защита от «слишком длинный сценарий»).
export const MAX_SCRIPT_CHARS = 1500;

/**
 * Формирует тело запроса /v2/video/generate для HeyGen.
 * Чистая функция — легко тестируется, никаких сетевых вызовов.
 */
export function buildCreateVideoPayload(input: CreateVideoInput): Record<string, unknown> {
  const text = (input.script || "").trim();
  if (!text) throw new HeygenError("unknown", "пустой текст сцены");
  if (text.length > MAX_SCRIPT_CHARS) {
    throw new HeygenError("unknown", `слишком длинный сценарий (${text.length} символов, лимит ${MAX_SCRIPT_CHARS})`);
  }
  if (!input.avatarId) throw new HeygenError("avatar_unavailable", "пустой avatar_id");
  if (!input.voiceId) throw new HeygenError("voice_unavailable", "пустой voice_id");

  const background =
    input.background && /^#[0-9a-fA-F]{6}$/.test(input.background)
      ? { type: "color", value: input.background }
      : { type: "color", value: "#0b0a09" };

  const payload: Record<string, unknown> = {
    video_inputs: [
      {
        character: {
          type: "avatar",
          avatar_id: input.avatarId,
          avatar_style: "normal",
        },
        voice: {
          type: "text",
          input_text: text,
          voice_id: input.voiceId,
        },
        background,
      },
    ],
    dimension: { width: input.width, height: input.height },
    title: input.title || "AlovLab Reels",
  };
  if (input.engine) payload.engine = input.engine;
  return payload;
}

/** Приводит разные формы ответа статуса HeyGen к единому HeygenVideoState. */
export function normalizeStatus(videoId: string, data: any): HeygenVideoState {
  const d = data?.data ?? data ?? {};
  const rawStatus = String(d.status ?? "").toLowerCase();
  let status: HeygenVideoStatus;
  switch (rawStatus) {
    case "completed":
    case "success":
    case "done":
      status = "completed";
      break;
    case "failed":
    case "error":
      status = "failed";
      break;
    case "processing":
    case "rendering":
      status = "processing";
      break;
    default:
      status = "pending";
  }
  return {
    videoId,
    status,
    videoUrl: d.video_url ?? d.video_url_caption ?? null,
    progress:
      status === "completed" ? 100 : typeof d.progress === "number" ? d.progress : status === "processing" ? 50 : 5,
    creditsUsed: typeof d.credits_used === "number" ? d.credits_used : typeof d.duration === "number" ? d.duration : null,
    error: d.error ? String(d.error?.message ?? d.error) : null,
  };
}
