import { describe, it, expect } from "vitest";
import { buildCreateVideoPayload, normalizeStatus, MAX_SCRIPT_CHARS } from "../src/heygen/payload";
import { classifyStatus, HeygenError } from "../src/heygen/errors";

const base = { script: "Привет", avatarId: "av_1", voiceId: "vo_1", language: "ru", width: 1080, height: 1920 };

describe("HeyGen payload", () => {
  it("собирает корректное тело v2", () => {
    const p: any = buildCreateVideoPayload(base);
    expect(p.video_inputs[0].character.avatar_id).toBe("av_1");
    expect(p.video_inputs[0].voice.voice_id).toBe("vo_1");
    expect(p.dimension).toEqual({ width: 1080, height: 1920 });
  });
  it("бросает понятную ошибку на пустом avatar_id", () => {
    expect(() => buildCreateVideoPayload({ ...base, avatarId: "" })).toThrow(HeygenError);
  });
  it("бросает на слишком длинном сценарии", () => {
    expect(() => buildCreateVideoPayload({ ...base, script: "a".repeat(MAX_SCRIPT_CHARS + 1) })).toThrow(/длинн/);
  });
  it("bg по умолчанию тёмный", () => {
    const p: any = buildCreateVideoPayload(base);
    expect(p.video_inputs[0].background.value).toBe("#0b0a09");
  });
});

describe("normalizeStatus", () => {
  it("completed → 100% и url", () => {
    const s = normalizeStatus("v1", { data: { status: "completed", video_url: "http://x/y.mp4" } });
    expect(s.status).toBe("completed");
    expect(s.progress).toBe(100);
    expect(s.videoUrl).toBe("http://x/y.mp4");
  });
  it("failed → error", () => {
    const s = normalizeStatus("v1", { data: { status: "failed", error: { message: "boom" } } });
    expect(s.status).toBe("failed");
    expect(s.error).toBe("boom");
  });
});

describe("classifyStatus", () => {
  it("маппит HTTP-коды", () => {
    expect(classifyStatus(401)).toBe("invalid_key");
    expect(classifyStatus(402)).toBe("insufficient_credits");
    expect(classifyStatus(429)).toBe("rate_limit");
    expect(classifyStatus(500)).toBe("bad_response");
  });
  it("retriable флаг", () => {
    expect(new HeygenError("rate_limit").retriable).toBe(true);
    expect(new HeygenError("invalid_key").retriable).toBe(false);
  });
});
