import { describe, it, expect } from "vitest";
import { routeScene, buildGenerationPlan } from "../src/generators/router";
import { Scene, ReelsScript } from "../src/store/types";
import { DayContent } from "../src/content/adapter";

const emptyContent = DayContent.parse({ date: "2026-08-05", found: true });
const withCard = DayContent.parse({ date: "2026-08-05", found: true, carousel_png: ["/x/02_problem.png"] });

function scene(over: Partial<Scene>): Scene {
  return Scene.parse({ id: "s1", durationSeconds: 4, type: "avatar", spokenText: "t", onScreenText: "", visualSource: "avatar", cameraMotion: "", transition: "", subtitle: "", disabled: false, ...over });
}

describe("scene router", () => {
  it("аватарная сцена → heygen, без подмены аватара", () => {
    const r = routeScene(scene({ type: "avatar" }), emptyContent);
    expect(r.generator).toBe("heygen");
    expect(r.fallback_generator).toBeNull();
    expect(r.requires_avatar).toBe(true);
  });

  it("broll с готовой карточкой → higgsfield, fallback grok", () => {
    const r = routeScene(scene({ type: "broll", visualSource: "card:1", durationSeconds: 8, cameraMotion: "push-in + highlight" }), withCard);
    expect(r.generator).toBe("higgsfield");
    expect(r.fallback_generator).toBe("grok");
    expect(r.source_assets.length).toBe(1);
  });

  it("простая короткая карточка → ffmpeg (не тратим кредиты)", () => {
    const r = routeScene(scene({ type: "broll", visualSource: "card:1", durationSeconds: 3, cameraMotion: "slow push-in" }), withCard);
    expect(r.generator).toBe("ffmpeg");
  });

  it("broll без кадра → grok (text-to-video)", () => {
    const r = routeScene(scene({ type: "broll", visualSource: "broll:x", durationSeconds: 8 }), emptyContent);
    expect(r.generator).toBe("grok");
    expect(r.fallback_generator).toBe("higgsfield");
  });

  it("allowGrok=false → без grok уходим в ffmpeg", () => {
    const r = routeScene(scene({ type: "broll", visualSource: "broll:x", durationSeconds: 8 }), emptyContent, { allowGrok: false });
    expect(r.generator).toBe("ffmpeg");
  });

  it("buildGenerationPlan суммирует и не считает disabled", () => {
    const script = ReelsScript.parse({
      title: "t", durationSeconds: 12, goal: "save", mode: "avatar_broll", hook: "h", avatarScript: "a", voiceoverScript: "v", cta: "c",
      scenes: [scene({ id: "a", type: "avatar" }), scene({ id: "b", type: "broll", visualSource: "broll:x", durationSeconds: 8, disabled: true })],
    });
    const plan = buildGenerationPlan("2026-08-05", script, emptyContent, 1);
    expect(plan.scenes.length).toBe(1);
    expect(plan.scenes[0].generator).toBe("heygen");
  });
});
