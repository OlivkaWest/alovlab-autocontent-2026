import type { GenerationPlan } from "../generators/router";

export interface CostEstimate {
  grokScenes: number;
  higgsfieldScenes: number;
  heygenScenes: number;
  ffmpegScenes: number;
  generatedSeconds: number;
  estimateUsd: number | null; // null = точная цена неизвестна, не выдумываем
  note: string;
  overLimit: boolean;
}

/**
 * Оценка стоимости генерации. Точные тарифы xAI/HeyGen на видео здесь НЕ зашиты:
 * если цена неизвестна — возвращаем null и честно об этом пишем.
 */
export function estimateCost(plan: GenerationPlan, maxUsd: number | null): CostEstimate {
  const grok = plan.scenes.filter((s) => s.generator === "grok");
  const higgs = plan.scenes.filter((s) => s.generator === "higgsfield");
  const heygen = plan.scenes.filter((s) => s.generator === "heygen");
  const ffmpeg = plan.scenes.filter((s) => s.generator === "ffmpeg" || s.generator === "existing_asset");
  const generatedSeconds = [...grok, ...higgs].reduce((a, s) => a + s.duration_seconds, 0);

  return {
    grokScenes: grok.length,
    higgsfieldScenes: higgs.length,
    heygenScenes: heygen.length,
    ffmpegScenes: ffmpeg.length,
    generatedSeconds,
    estimateUsd: null,
    note:
      "Точная стоимость зависит от актуальных тарифов HeyGen/xAI и модели Higgsfield. " +
      "Она не зашита в код — сверься с тарифами перед платным запуском.",
    overLimit: maxUsd !== null ? false : false, // без известной цены превышение не декларируем
  };
}
