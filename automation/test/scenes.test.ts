import { describe, it, expect } from "vitest";
import { validateScript, repairScript, fitDurations, clamp } from "../src/reels/scenes";
import { generateScript } from "../src/reels/script-generator";
import { Brief } from "../src/store/types";

const brief = Brief.parse({ theme: "Одна идея — это не один пост", goal: "save", cardCount: 7, reelsDurationSeconds: 30 });

describe("script generation + validation", () => {
  it("генерирует валидный сценарий из брифа (template)", async () => {
    const s = await generateScript(brief, null, {});
    expect(s.scenes.length).toBe(5);
    expect(s.hook.length).toBeGreaterThan(3);
    expect(validateScript(s).ok).toBe(true);
  });

  it("длительность близка к целевой", async () => {
    const s = await generateScript(brief, null, {});
    expect(Math.abs(s.durationSeconds - 30)).toBeLessThanOrEqual(8);
  });

  it("validateScript ловит пустой хук и пустые сцены", () => {
    const bad = {
      title: "x", durationSeconds: 20, goal: "save", mode: "avatar_broll",
      hook: "", avatarScript: "a", voiceoverScript: "v", cta: "c",
      scenes: [{ id: "s1", durationSeconds: 3, type: "avatar", spokenText: "", onScreenText: "", visualSource: "avatar", cameraMotion: "", transition: "", subtitle: "", disabled: false }],
    };
    const res = validateScript(bad);
    expect(res.ok).toBe(false);
    expect(res.issues.some((i) => i.field === "hook")).toBe(true);
  });

  it("repairScript чинит битый ответ модели (snake_case, без id)", async () => {
    const fallback = await generateScript(brief, null, {});
    const raw = {
      title: "T", duration_seconds: 999, hook: "H", cta: "C",
      scenes: [{ duration_seconds: 50, type: "broll", spoken_text: "речь", on_screen_text: "текст" }],
    };
    const fixed = repairScript(raw, fallback);
    expect(fixed.scenes[0].id).toMatch(/scene/);
    expect(fixed.scenes[0].durationSeconds).toBeLessThanOrEqual(20);
    expect(fixed.durationSeconds).toBeLessThanOrEqual(120);
    expect(validateScript(fixed).ok).toBe(true);
  });

  it("fitDurations укладывает сцены в цель и границы", () => {
    const d = fitDurations(["hook", "problem", "breakdown", "solution", "cta"], 30);
    expect(d).toHaveLength(5);
    expect(d[0]).toBeGreaterThanOrEqual(2);
    expect(d[0]).toBeLessThanOrEqual(4);
    expect(d.reduce((a, b) => a + b, 0)).toBeLessThanOrEqual(33);
  });

  it("clamp", () => {
    expect(clamp(50, 1, 20)).toBe(20);
    expect(clamp(0, 1, 20)).toBe(1);
  });
});
