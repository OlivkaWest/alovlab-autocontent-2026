import { describe, it, expect } from "vitest";
import { adaptForSpeech, applyPronunciation, buildVoiceScript } from "../src/elevenlabs/voice-script";
import { estimateSeconds } from "../src/elevenlabs/client";
import { ElevenError } from "../src/elevenlabs/errors";

describe("voice-script адаптация под речь", () => {
  it("убирает ссылки, скобки и markdown", () => {
    const out = adaptForSpeech("Смотри [сюда](https://x.ru) (важно) **жирный** и https://y.ru конец");
    expect(out).not.toMatch(/http/);
    expect(out).not.toContain("(");
    expect(out).not.toContain("*");
    expect(out).toContain("Смотри");
  });

  it("применяет словарь произношения, длинные ключи первыми", () => {
    const out = applyPronunciation("Открой Claude Code и HeyGen", { "Claude Code": "Клод Код", Claude: "Клод", HeyGen: "Хэй Джен" });
    expect(out).toContain("Клод Код");
    expect(out).toContain("Хэй Джен");
    expect(out).not.toContain("Claude");
  });

  it("buildVoiceScript даёт сегменты и модель", () => {
    const vs = buildVoiceScript("Первый абзац.\n\nВторой абзац про AlovLab.");
    expect(vs.segments.length).toBeGreaterThanOrEqual(2);
    expect(vs.model_id).toBeTruthy();
    expect(vs.segments[0].id).toMatch(/segment_01/);
  });

  it("estimateSeconds растёт с длиной", () => {
    expect(estimateSeconds("одно слово тут")).toBeGreaterThanOrEqual(1);
    expect(estimateSeconds("раз два три четыре пять шесть семь восемь девять десять")).toBeGreaterThan(estimateSeconds("раз два"));
  });

  it("ElevenError: retriable флаг", () => {
    expect(new ElevenError("rate_limit").retriable).toBe(true);
    expect(new ElevenError("invalid_key").retriable).toBe(false);
  });
});
