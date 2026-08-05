import { newId } from "../store/projects";
import { Scene, ReelsScript, type Carousel } from "../store/types";
import { checkHook, findBannedPhrases, type StyleIssue } from "../content/style";

export interface ScriptIssue {
  field: string;
  message: string;
}

// Границы длительности сцен по типовой структуре (сек).
const SCENE_BOUNDS: Record<string, [number, number]> = {
  hook: [2, 4],
  problem: [3, 5],
  breakdown: [5, 10],
  solution: [5, 10],
  cta: [2, 4],
};

/** Клампит число в диапазон. */
export function clamp(v: number, lo: number, hi: number): number {
  return Math.max(lo, Math.min(hi, v));
}

/**
 * Валидирует сценарий: обязательные поля, непустые сцены, длительности.
 * Возвращает список проблем (пустой = всё ок).
 */
export function validateScript(script: unknown): { ok: boolean; issues: ScriptIssue[] } {
  const issues: ScriptIssue[] = [];
  const parsed = ReelsScript.safeParse(script);
  if (!parsed.success) {
    for (const e of parsed.error.issues) {
      issues.push({ field: e.path.join("."), message: e.message });
    }
    return { ok: false, issues };
  }
  const s = parsed.data;
  if (!s.hook.trim()) issues.push({ field: "hook", message: "Пустой хук" });
  if (!s.cta.trim()) issues.push({ field: "cta", message: "Пустой CTA" });

  const active = s.scenes.filter((sc) => !sc.disabled);
  if (active.length === 0) {
    issues.push({ field: "scenes", message: "Нет ни одной активной сцены" });
  }
  s.scenes.forEach((sc, i) => {
    if (!sc.disabled && !sc.spokenText.trim() && !sc.onScreenText.trim()) {
      issues.push({ field: `scenes[${i}]`, message: "Пустая сцена: нет ни речи, ни текста на экране" });
    }
    if (sc.durationSeconds < 1) {
      issues.push({ field: `scenes[${i}].durationSeconds`, message: "Слишком короткая сцена" });
    }
  });

  return { ok: issues.length === 0, issues };
}

/** Проверка стиля сценария (канцелярщина + запрещённый хук). */
export function auditScriptStyle(script: ReelsScript): StyleIssue[] {
  const issues: StyleIssue[] = [];
  issues.push(...checkHook(script.hook));
  issues.push(...findBannedPhrases(script.avatarScript, "avatarScript"));
  issues.push(...findBannedPhrases(script.voiceoverScript, "voiceoverScript"));
  script.scenes.forEach((sc, i) => {
    issues.push(...findBannedPhrases(sc.spokenText, `scenes[${i}].spokenText`));
  });
  return issues;
}

/**
 * Чинит частично-битый сценарий: доливает id, клампит длительности,
 * гарантирует минимум одну сцену. Проект не должен падать из-за модели.
 */
export function repairScript(raw: any, fallback: ReelsScript): ReelsScript {
  const src = raw && typeof raw === "object" ? raw : {};
  const scenesRaw: any[] = Array.isArray(src.scenes) && src.scenes.length ? src.scenes : fallback.scenes;

  const scenes = scenesRaw.map((sc: any, i: number) =>
    Scene.parse({
      id: typeof sc?.id === "string" && sc.id ? sc.id : newId("scene"),
      durationSeconds: clamp(Number(sc?.durationSeconds ?? sc?.duration_seconds ?? 4) || 4, 1, 20),
      type: sc?.type === "broll" ? "broll" : "avatar",
      spokenText: String(sc?.spokenText ?? sc?.spoken_text ?? ""),
      onScreenText: String(sc?.onScreenText ?? sc?.on_screen_text ?? ""),
      visualSource: String(sc?.visualSource ?? sc?.visual_source ?? "avatar"),
      cameraMotion: String(sc?.cameraMotion ?? sc?.camera_motion ?? ""),
      transition: String(sc?.transition ?? ""),
      subtitle: String(sc?.subtitle ?? sc?.spokenText ?? sc?.spoken_text ?? ""),
      disabled: Boolean(sc?.disabled ?? false),
    })
  );

  return ReelsScript.parse({
    title: String(src.title || fallback.title),
    durationSeconds: clamp(Number(src.durationSeconds ?? src.duration_seconds ?? fallback.durationSeconds) || fallback.durationSeconds, 10, 120),
    goal: String(src.goal || fallback.goal),
    mode: src.mode === "avatar_only" ? "avatar_only" : "avatar_broll",
    hook: String(src.hook || fallback.hook),
    avatarScript: String(src.avatarScript ?? src.avatar_script ?? fallback.avatarScript),
    voiceoverScript: String(src.voiceoverScript ?? src.voiceover_script ?? fallback.voiceoverScript),
    cta: String(src.cta || fallback.cta),
    scenes,
  });
}

/** Пропорционально раскидывает целевую длительность по сценам с учётом границ. */
export function fitDurations(kinds: Array<keyof typeof SCENE_BOUNDS>, target: number): number[] {
  const mins = kinds.map((k) => SCENE_BOUNDS[k][0]);
  const maxs = kinds.map((k) => SCENE_BOUNDS[k][1]);
  const minSum = mins.reduce((a, b) => a + b, 0);
  const maxSum = maxs.reduce((a, b) => a + b, 0);
  const t = clamp(target, minSum, maxSum);
  // Распределяем «лишнее» сверх минимумов пропорционально запасу до максимума.
  const slack = maxs.map((m, i) => m - mins[i]);
  const slackSum = slack.reduce((a, b) => a + b, 0) || 1;
  let extra = t - minSum;
  const out = mins.map((m, i) => {
    const add = Math.round((slack[i] / slackSum) * extra);
    return clamp(m + add, mins[i], maxs[i]);
  });
  return out;
}

/** Привязывает сцены-разбор к карточкам карусели (visual_source = card:N). */
export function assignCardsToScenes(script: ReelsScript, carousel: Carousel | null): ReelsScript {
  if (!carousel || carousel.cards.length === 0) return script;
  let cardPtr = 1; // 0 — обложка, начинаем со смысловых
  for (const sc of script.scenes) {
    if (sc.type === "broll" && sc.visualSource.startsWith("card")) {
      const card = carousel.cards[Math.min(cardPtr, carousel.cards.length - 1)];
      sc.visualSource = `card:${card.index}`;
      cardPtr++;
    }
  }
  return script;
}
