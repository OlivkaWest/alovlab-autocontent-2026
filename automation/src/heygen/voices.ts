import { config } from "../config";
import { heygenFetch, type RetryOptions } from "./client";
import { MOCK_VOICES } from "./mock";
import type { HeygenVoice } from "./types";

/** Список доступных голосов (или mock). Русский голос не подменяем англоязычным. */
export async function listVoices(opts?: RetryOptions): Promise<HeygenVoice[]> {
  if (config.heygen.mock) return MOCK_VOICES;
  const res = await heygenFetch("/v2/voices", {}, opts);
  const raw: any[] = res?.data?.voices ?? res?.voices ?? [];
  return raw.map((v) => ({
    voiceId: String(v.voice_id ?? v.id ?? ""),
    name: String(v.name ?? v.display_name ?? v.voice_id ?? ""),
    language: v.language ?? v.locale ?? "",
    gender: v.gender ?? "",
  }));
}
