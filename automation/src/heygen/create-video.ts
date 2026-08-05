import { config } from "../config";
import { createLogger } from "../logger";
import { heygenFetch, type RetryOptions } from "./client";
import { buildCreateVideoPayload } from "./payload";
import { mockCreateVideo } from "./mock";
import { HeygenError } from "./errors";
import type { CreateVideoInput } from "./types";

const log = createLogger("heygen-create");

/** Создаёт видео в HeyGen (или mock). Возвращает video_id. */
export async function createVideo(input: CreateVideoInput, opts?: RetryOptions): Promise<{ videoId: string; mock: boolean }> {
  const payload = buildCreateVideoPayload(input); // валидирует вход, кидает понятную ошибку

  if (config.heygen.mock) {
    const { videoId } = mockCreateVideo(input);
    log.info(`[mock] создано видео ${videoId}`);
    return { videoId, mock: true };
  }

  const res = await heygenFetch("/v2/video/generate", { method: "POST", body: payload }, opts);
  const videoId = res?.data?.video_id ?? res?.video_id;
  if (!videoId) throw new HeygenError("bad_response", "в ответе нет video_id");
  log.info(`Создано видео ${videoId}`);
  return { videoId: String(videoId), mock: false };
}
