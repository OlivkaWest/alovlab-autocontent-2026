import { config } from "../config";
import { heygenFetch, type RetryOptions } from "./client";
import { normalizeStatus } from "./payload";
import { mockGetStatus } from "./mock";
import type { HeygenVideoState } from "./types";

/** Получает статус видео (или mock), приведённый к единому виду. */
export async function getVideoStatus(videoId: string, opts?: RetryOptions): Promise<HeygenVideoState> {
  if (config.heygen.mock || videoId.startsWith("mock_")) {
    return mockGetStatus(videoId);
  }
  const res = await heygenFetch(`/v1/video_status.get?video_id=${encodeURIComponent(videoId)}`, {}, opts);
  return normalizeStatus(videoId, res);
}
