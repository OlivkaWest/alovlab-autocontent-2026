import { describe, it, expect } from "vitest";
import { buildSubtitles, toSrt, wrapTwoLines } from "../src/reels/subtitles";
import { toAss } from "../src/reels/ass";
import { ReelsScript } from "../src/store/types";

const script = ReelsScript.parse({
  title: "t", durationSeconds: 10, goal: "save", mode: "avatar_broll",
  hook: "h", avatarScript: "a", voiceoverScript: "v", cta: "c",
  scenes: [
    { id: "s1", durationSeconds: 4, type: "avatar", spokenText: "Один пост из идеи — это любитель", onScreenText: "", visualSource: "avatar", cameraMotion: "", transition: "", subtitle: "Один пост из идеи — это любитель", disabled: false },
    { id: "s2", durationSeconds: 6, type: "broll", spokenText: "Профи достаёт три", onScreenText: "", visualSource: "card:1", cameraMotion: "", transition: "", subtitle: "Профи достаёт три", disabled: false },
  ],
});

describe("subtitles", () => {
  it("строит кью с растущими таймкодами", () => {
    const cues = buildSubtitles(script);
    expect(cues.length).toBeGreaterThan(0);
    for (let i = 1; i < cues.length; i++) expect(cues[i].startMs).toBeGreaterThanOrEqual(cues[i - 1].startMs);
    expect(cues[0].startMs).toBe(0);
  });

  it("SRT валидной формы", () => {
    const srt = toSrt(buildSubtitles(script));
    expect(srt).toMatch(/00:00:00,000 --> /);
    expect(srt).toContain("1\n");
  });

  it("ASS содержит стиль и события", () => {
    const ass = toAss(buildSubtitles(script));
    expect(ass).toContain("[V4+ Styles]");
    expect(ass).toContain("Dialogue:");
  });

  it("wrapTwoLines не длиннее двух строк", () => {
    const wrapped = wrapTwoLines("Одна сильная тема может кормить блог неделю если разложить её по форматам");
    expect(wrapped.split("\n").length).toBeLessThanOrEqual(2);
  });
});
