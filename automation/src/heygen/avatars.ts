import { config } from "../config";
import { heygenFetch, type RetryOptions } from "./client";
import { MOCK_AVATARS } from "./mock";
import type { HeygenAvatar } from "./types";

/** Список доступных аватаров (или mock). */
export async function listAvatars(opts?: RetryOptions): Promise<HeygenAvatar[]> {
  if (config.heygen.mock) return MOCK_AVATARS;
  const res = await heygenFetch("/v2/avatars", {}, opts);
  const raw: any[] = res?.data?.avatars ?? res?.avatars ?? [];
  return raw.map((a) => ({
    avatarId: String(a.avatar_id ?? a.id ?? ""),
    name: String(a.avatar_name ?? a.name ?? a.avatar_id ?? ""),
    previewUrl: a.preview_image_url ?? a.preview_url ?? "",
  }));
}
