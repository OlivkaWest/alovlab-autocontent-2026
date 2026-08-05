import { z } from "zod";
import type { Scene, ReelsScript } from "../store/types";
import type { DayContent } from "../content/adapter";

// Куда отправляем сцену.
export const GENERATORS = ["heygen", "higgsfield", "grok", "ffmpeg", "existing_asset"] as const;
export const GeneratorName = z.enum(GENERATORS);
export type GeneratorName = z.infer<typeof GeneratorName>;

export const SceneRoute = z.object({
  scene_id: z.string(),
  type: z.string(),
  generator: GeneratorName,
  reason: z.string(),
  fallback_generator: GeneratorName.nullable(),
  requires_avatar: z.boolean(),
  requires_generation: z.boolean(),
  duration_seconds: z.number(),
  source_assets: z.array(z.string()).default([]),
  prompt: z.string().default(""),
  model: z.string().nullable().default(null),
});
export type SceneRoute = z.infer<typeof SceneRoute>;

export const GenerationPlan = z.object({
  date: z.string(),
  version: z.number(),
  mode: z.string(),
  total_duration_seconds: z.number(),
  scenes: z.array(SceneRoute),
});
export type GenerationPlan = z.infer<typeof GenerationPlan>;

// Есть ли у сцены готовый исходный визуал (карточка/картинка/видео).
function sourceAssetsForScene(scene: Scene, content: DayContent): string[] {
  const m = scene.visualSource.match(/card:(\d+)/);
  if (m) {
    const idx = Number(m[1]);
    const png = content.carousel_png.find((f) => f.includes(`/${String(idx + 1).padStart(2, "0")}`));
    if (png) return [png];
    if (content.carousel_png[idx]) return [content.carousel_png[idx]];
  }
  return [];
}

/**
 * Маршрутизирует одну сцену. Логика из брифа:
 *  — говорит Нейромонах → heygen;
 *  — есть готовый кадр → higgsfield (оживить), fallback grok;
 *  — кадра нет, нужна новая сцена → grok (text-to-video), fallback higgsfield;
 *  — хватает карточки/движения → ffmpeg (не тратим кредиты).
 */
export function routeScene(scene: Scene, content: DayContent, opts: { allowGrok?: boolean } = {}): SceneRoute {
  const allowGrok = opts.allowGrok !== false;
  const assets = sourceAssetsForScene(scene, content);
  const existingVideo = assets.find((a) => /\.(mp4|mov)$/i.test(a));

  if (scene.type === "avatar") {
    return SceneRoute.parse({
      scene_id: scene.id,
      type: "avatar",
      generator: "heygen",
      reason: "В кадре говорит Нейромонах — нужен постоянный аватар и точная русская речь.",
      fallback_generator: null, // аватар не подменяем чужим персонажем
      requires_avatar: true,
      requires_generation: true,
      duration_seconds: scene.durationSeconds,
      source_assets: [],
      prompt: scene.spokenText,
      model: null,
    });
  }

  if (existingVideo) {
    return SceneRoute.parse({
      scene_id: scene.id,
      type: "existing_asset",
      generator: "existing_asset",
      reason: "Для сцены уже есть готовое видео в материалах дня.",
      fallback_generator: "ffmpeg",
      requires_avatar: false,
      requires_generation: false,
      duration_seconds: scene.durationSeconds,
      source_assets: assets,
      prompt: "",
      model: null,
    });
  }

  if (assets.length) {
    // Есть готовая карточка/картинка → оживляем.
    // Если сцена простая (короткая, просто push-in) — хватит FFmpeg, кредиты не тратим.
    const simple = scene.durationSeconds <= 4 && /push|pan|scale|hold/i.test(scene.cameraMotion || "");
    if (simple) {
      return SceneRoute.parse({
        scene_id: scene.id,
        type: "broll",
        generator: "ffmpeg",
        reason: "Короткая сцена: достаточно аккуратного push-in по готовой карточке. Генерация видео не даст пользы.",
        fallback_generator: "higgsfield",
        requires_avatar: false,
        requires_generation: false,
        duration_seconds: scene.durationSeconds,
        source_assets: assets,
        prompt: "",
        model: null,
      });
    }
    return SceneRoute.parse({
      scene_id: scene.id,
      type: "image_to_video",
      generator: "higgsfield",
      reason: "Есть готовый кадр — оживляем его управляемым cinematic image-to-video с сохранением композиции.",
      fallback_generator: allowGrok ? "grok" : "ffmpeg",
      requires_avatar: false,
      requires_generation: true,
      duration_seconds: scene.durationSeconds,
      source_assets: assets,
      prompt: brollPrompt(scene),
      model: null, // выбирается после проверки доступных моделей Higgsfield
    });
  }

  // Готового визуала нет — создаём с нуля.
  if (allowGrok) {
    return SceneRoute.parse({
      scene_id: scene.id,
      type: "generated_broll",
      generator: "grok",
      reason: "Готового кадра нет — нужна новая сцена/метафора через text-to-video.",
      fallback_generator: "higgsfield",
      requires_avatar: false,
      requires_generation: true,
      duration_seconds: scene.durationSeconds,
      source_assets: [],
      prompt: brollPrompt(scene),
      model: null,
    });
  }

  return SceneRoute.parse({
    scene_id: scene.id,
    type: "broll",
    generator: "ffmpeg",
    reason: "Grok отключён и готового кадра нет — собираем текстовую сцену через FFmpeg.",
    fallback_generator: null,
    requires_avatar: false,
    requires_generation: false,
    duration_seconds: scene.durationSeconds,
    source_assets: [],
    prompt: "",
    model: null,
  });
}

function brollPrompt(scene: Scene): string {
  const base = scene.onScreenText || scene.spokenText;
  return `Vertical 9:16 cinematic B-roll. ${base}. Slow controlled camera, premium look, warm amber light, no readable text, no logos.`;
}

/** Собирает полный generation plan для сценария. */
export function buildGenerationPlan(date: string, script: ReelsScript, content: DayContent, version: number, opts: { allowGrok?: boolean } = {}): GenerationPlan {
  const scenes = script.scenes.filter((s) => !s.disabled).map((s) => routeScene(s, content, opts));
  return GenerationPlan.parse({
    date,
    version,
    mode: script.mode,
    total_duration_seconds: scenes.reduce((a, s) => a + s.duration_seconds, 0),
    scenes,
  });
}
