import { newId } from "../store/projects";
import { Carousel, Brief, Card, type CardRole, type ContentGoal } from "../store/types";
import { auditStyle } from "./style";
import { maybeComplete, extractJson } from "./llm";
import { createLogger } from "../logger";

const log = createLogger("carousel-gen");

// CTA под конкретную цель контента — говорим по-человечески.
const CTA_BY_GOAL: Record<ContentGoal, string> = {
  reach: "Сохрани, чтобы не потерять. И покажи тому, кто пилит по одному посту.",
  subscribe: "Подпишись — дальше разберём, как собрать контент-завод из одной идеи.",
  save: "Сохрани. Следующую идею не сжигай.",
  comment: "Напиши в комментах свою тему — разложу её по форматам.",
  telegram: "Забирай разбор и шаблоны в Telegram: t.me/AlovLab.",
  course_sale: "На интенсиве «Автоконтент 2026» собираем такой конвейер под твой продукт.",
  studio_lead: "Нужен контент-поток под ключ — оставь заявку в AI-студию AlovLab.",
  warmup: "Завтра покажу, как из этой же идеи вышли Reels и серия Stories.",
};

// План ролей карточек: всегда начинаем обложкой, заканчиваем CTA.
function rolePlan(count: number): CardRole[] {
  const middle: CardRole[] = ["problem", "insight", "solution", "example", "action"];
  const plan: CardRole[] = ["cover"];
  for (let i = 0; i < count - 2; i++) plan.push(middle[i % middle.length]);
  plan.push("cta");
  return plan;
}

const ROLE_HEADINGS: Record<CardRole, string> = {
  cover: "Обложка",
  problem: "Проблема",
  insight: "Разворот",
  solution: "Метод",
  example: "Пример",
  action: "Шаг",
  cta: "Действие",
};

function templateCard(role: CardRole, index: number, brief: Brief): Card {
  const theme = brief.theme.trim();
  const base: Record<CardRole, { title: string; body: string; accent: string }> = {
    cover: {
      title: theme,
      body: "Одна тема — несколько единиц контента. Разбираем, как не сливать идею в один пост.",
      accent: theme,
    },
    problem: {
      title: "Где ты теряешь результат",
      body: "Берёшь сильную тему, делаешь один пост и идёшь искать следующую. Идея отработала на десять процентов.",
      accent: "один пост",
    },
    insight: {
      title: "Что на самом деле внутри темы",
      body: "В одной мысли уже лежат карусель, Reels и серия Stories. Ты просто не достал их.",
      accent: "карусель, Reels и Stories",
    },
    solution: {
      title: "Метод: сначала конфликт",
      body: "Достаём главный конфликт темы. Он держит внимание и в карусели, и в ролике.",
      accent: "главный конфликт",
    },
    example: {
      title: "Как это выглядит",
      body: "Одна идея разложена по форматам: длинное объяснение — в карусель, острая мысль — в Reels.",
      accent: "разложена по форматам",
    },
    action: {
      title: "Твой следующий шаг",
      body: "Возьми свою тему. Найди в ней конфликт. Раздели на форматы. Собери за один заход.",
      accent: "раздели на форматы",
    },
    cta: {
      title: "Не сжигай идеи по одной",
      body: CTA_BY_GOAL[brief.goal],
      accent: "",
    },
  };
  const c = base[role];
  return { id: newId("card"), index, role, title: c.title, body: c.body, accent: c.accent };
}

function templateCarousel(brief: Brief): Carousel {
  const plan = rolePlan(brief.cardCount);
  const cards = plan.map((role, i) => templateCard(role, i, brief));
  return Carousel.parse({
    title: brief.theme.trim(),
    cards,
    cta: CTA_BY_GOAL[brief.goal],
    caption:
      `${brief.theme.trim()}. Разбираем на пальцах и даём метод. ` +
      `${CTA_BY_GOAL[brief.goal]}`,
  });
}

function llmPrompt(brief: Brief): string {
  return [
    "Ты — редактор AlovLab. Пишешь живо, коротко, спокойно и уверенно.",
    "Запрещена канцелярщина и шаблонные AI-фразы.",
    `Тема: ${brief.theme}`,
    `Аудитория: ${brief.audience || "не указана"}`,
    `Цель: ${brief.goal}`,
    `Количество карточек: ${brief.cardCount}`,
    "Верни СТРОГО JSON вида:",
    '{"title":"","caption":"","cta":"","cards":[{"role":"cover|problem|insight|solution|example|action|cta","title":"","body":"","accent":""}]}',
    `Ровно ${brief.cardCount} карточек, первая role=cover, последняя role=cta.`,
  ].join("\n");
}

/**
 * Генерирует карусель из брифа. По умолчанию — офлайн-движок.
 * Если подключён LLM и вернул валидный JSON — используем его, иначе шаблон.
 */
export async function generateCarousel(brief: Brief): Promise<Carousel> {
  const validated = Brief.parse(brief);

  const raw = await maybeComplete([
    { role: "system", content: "Отвечай только валидным JSON без пояснений." },
    { role: "user", content: llmPrompt(validated) },
  ]);

  if (raw) {
    const json = extractJson(raw);
    if (json) {
      try {
        const parsed = JSON.parse(json) as {
          title?: string;
          caption?: string;
          cta?: string;
          cards?: Array<{ role?: string; title?: string; body?: string; accent?: string }>;
        };
        if (parsed.cards?.length) {
          const cards: Card[] = parsed.cards.map((c, i) =>
            Card.parse({
              id: newId("card"),
              index: i,
              role: (c.role as CardRole) || "insight",
              title: c.title || "",
              body: c.body || "",
              accent: c.accent || "",
            })
          );
          return Carousel.parse({
            title: parsed.title || validated.theme,
            cards,
            cta: parsed.cta || CTA_BY_GOAL[validated.goal],
            caption: parsed.caption || "",
          });
        }
      } catch (err) {
        log.warn("LLM вернул битый JSON для карусели — берём шаблон", String(err));
      }
    }
  }

  return templateCarousel(validated);
}

/** Возвращает предупреждения по стилю карусели (для интерфейса). */
export function auditCarouselStyle(carousel: Carousel) {
  return auditStyle({
    texts: carousel.cards.flatMap((c) => [
      { text: c.title, where: `card#${c.index}.title` },
      { text: c.body, where: `card#${c.index}.body` },
    ]),
  });
}
