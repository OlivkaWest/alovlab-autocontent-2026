import { newId } from "../store/projects";
import { ReelsScript, Scene, type Brief, type Carousel, type VideoMode } from "../store/types";
import { maybeComplete, extractJson } from "../content/llm";
import { validateScript, repairScript, fitDurations, assignCardsToScenes } from "./scenes";
import { createLogger } from "../logger";

const log = createLogger("script-gen");

export interface ScriptOptions {
  mode?: VideoMode;
  product?: string; // ссылка или продукт для CTA
  style?: string; // стиль подачи
}

// Пятисценная структура из брифа (п.7). broll-сцены заполняются карточками.
function templateScript(brief: Brief, carousel: Carousel | null, opts: ScriptOptions): ReelsScript {
  const mode: VideoMode = opts.mode || "avatar_broll";
  const target = brief.reelsDurationSeconds;
  const kinds = ["hook", "problem", "breakdown", "solution", "cta"] as const;
  const durs = fitDurations([...kinds], target);

  const brollType = mode === "avatar_only" ? "avatar" : "broll";

  const hook = "Один пост из идеи — это любитель. Профи достаёт три.";
  const avatarFinal = "Следующую идею не сжигай. Размножь.";
  const voiceover =
    "Ты берёшь нормальную тему, публикуешь один пост и идёшь искать следующую. " +
    "Хотя внутри уже лежат карусель, Reels и серия Stories. " +
    "Сначала достань конфликт. Потом разложи его по форматам. Одна мысль. Несколько точек входа.";

  const cta =
    opts.product
      ? `Забирай метод и шаблоны: ${opts.product}`
      : "Сохрани. Следующую идею не сжигай.";

  const scenes: Scene[] = [
    Scene.parse({
      id: newId("scene"),
      durationSeconds: durs[0],
      type: "avatar",
      spokenText: hook,
      onScreenText: "Любитель vs профи",
      visualSource: "avatar",
      cameraMotion: "slow push-in",
      transition: "cut",
      subtitle: hook,
    }),
    Scene.parse({
      id: newId("scene"),
      durationSeconds: durs[1],
      type: brollType,
      spokenText: "Ты берёшь нормальную тему, публикуешь один пост и идёшь искать следующую.",
      onScreenText: "Один пост — и дальше",
      visualSource: brollType === "broll" ? "card:1" : "avatar",
      cameraMotion: "slow pan",
      transition: "soft cut",
      subtitle: "Один пост — и ты уже ищешь новую тему",
    }),
    Scene.parse({
      id: newId("scene"),
      durationSeconds: durs[2],
      type: brollType,
      spokenText: "Хотя внутри уже лежат карусель, Reels и серия Stories.",
      onScreenText: "Карусель · Reels · Stories",
      visualSource: brollType === "broll" ? "card:2" : "avatar",
      cameraMotion: "push-in + highlight",
      transition: "soft cut",
      subtitle: "Внутри уже лежат карусель, Reels и Stories",
    }),
    Scene.parse({
      id: newId("scene"),
      durationSeconds: durs[3],
      type: brollType,
      spokenText: "Сначала достань конфликт. Потом разложи его по форматам.",
      onScreenText: "Конфликт → форматы",
      visualSource: brollType === "broll" ? "card:3" : "avatar",
      cameraMotion: "scale key element",
      transition: "soft cut",
      subtitle: "Сначала конфликт. Потом форматы",
    }),
    Scene.parse({
      id: newId("scene"),
      durationSeconds: durs[4],
      type: "avatar",
      spokenText: avatarFinal,
      onScreenText: "Размножь",
      visualSource: "avatar",
      cameraMotion: "hold",
      transition: "logo outro",
      subtitle: avatarFinal,
    }),
  ];

  const script = ReelsScript.parse({
    title: brief.theme.trim(),
    durationSeconds: durs.reduce((a, b) => a + b, 0),
    goal: brief.goal,
    mode,
    hook,
    avatarScript: `${hook} … ${avatarFinal}`,
    voiceoverScript: voiceover,
    cta,
    scenes,
  });

  return assignCardsToScenes(script, carousel);
}

function llmPrompt(brief: Brief, carousel: Carousel | null, opts: ScriptOptions): string {
  const cardsText = carousel
    ? carousel.cards.map((c) => `- [${c.role}] ${c.title}: ${c.body}`).join("\n")
    : "(карусели нет)";
  return [
    "Ты — сценарист вертикальных Reels для AlovLab. Пишешь как речь человека, не как статью.",
    "Живо, коротко, спокойная уверенность. Никакой канцелярщины.",
    "Хук за 2-4 секунды создаёт конфликт. Запрещены вступления вроде «сегодня я расскажу».",
    "Reels НЕ читает карусель вслух: та же тема, но острее и с одной главной мыслью.",
    `Тема: ${brief.theme}`,
    `Аудитория: ${brief.audience || "не указана"}`,
    `Цель: ${brief.goal}. Желаемая длительность: ${brief.reelsDurationSeconds} сек.`,
    `Режим видео: ${opts.mode || "avatar_broll"}.`,
    opts.product ? `Продукт/ссылка для CTA: ${opts.product}` : "",
    "Текст карусели:",
    cardsText,
    "Верни СТРОГО JSON:",
    '{"title":"","duration_seconds":30,"goal":"","hook":"","avatar_script":"","voiceover_script":"","cta":"","scenes":[{"id":"scene_01","duration_seconds":3,"type":"avatar|broll","spoken_text":"","on_screen_text":"","visual_source":"avatar|card:N","camera_motion":"","transition":"","subtitle":""}]}',
    "Ровно 5 сцен: hook(avatar), проблема, разбор(broll), решение(broll), cta(avatar).",
  ]
    .filter(Boolean)
    .join("\n");
}

/**
 * Генерирует сценарий Reels. Возвращает валидный ReelsScript.
 * LLM-путь: до 2 попыток, битый JSON чинится repairScript, при провале — шаблон.
 */
export async function generateScript(
  brief: Brief,
  carousel: Carousel | null,
  opts: ScriptOptions = {}
): Promise<ReelsScript> {
  const fallback = templateScript(brief, carousel, opts);

  const maxAttempts = 2;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    const raw = await maybeComplete([
      { role: "system", content: "Отвечай только валидным JSON, без пояснений." },
      { role: "user", content: llmPrompt(brief, carousel, opts) },
    ]);
    if (!raw) break; // провайдер = template → сразу шаблон

    const json = extractJson(raw);
    if (!json) {
      log.warn(`Попытка ${attempt}: в ответе модели нет JSON`);
      continue;
    }
    let parsed: unknown;
    try {
      parsed = JSON.parse(json);
    } catch {
      log.warn(`Попытка ${attempt}: битый JSON, чиним`);
      const repaired = repairScript(safeLooseParse(json), fallback);
      if (validateScript(repaired).ok) return assignCardsToScenes(repaired, carousel);
      continue;
    }
    const repaired = repairScript(parsed, fallback);
    const check = validateScript(repaired);
    if (check.ok) return assignCardsToScenes(repaired, carousel);
    log.warn(`Попытка ${attempt}: сценарий не прошёл валидацию`, check.issues);
  }

  return fallback;
}

// Мягкий парс: вырезаем висячие запятые перед закрывающими скобками.
function safeLooseParse(json: string): unknown {
  try {
    return JSON.parse(json.replace(/,\s*([}\]])/g, "$1"));
  } catch {
    return {};
  }
}

export { templateScript };
