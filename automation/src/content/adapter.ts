import fs from "node:fs";
import path from "node:path";
import { z } from "zod";
import { config } from "../config";
import { dayDir } from "../project/day-store";

// Материалы одного дня, собранные из реальных файлов проекта.
export const DayCard = z.object({ role: z.string().default(""), title: z.string(), body: z.string().default("") });
export const DayContent = z.object({
  date: z.string(),
  found: z.boolean(),
  topic: z.string().default(""),
  content_type: z.string().default(""),
  goal: z.string().default(""),
  audience: z.string().default(""),
  platform: z.string().default("instagram"),
  desired_action: z.string().default(""),
  cta: z.string().default(""),
  links: z.array(z.string()).default([]),
  notes: z.string().default(""),
  reels_duration_seconds: z.number().default(30),
  card_count: z.number().default(7),
  cards: z.array(DayCard).default([]),
  post: z.string().default(""),
  visuals: z.array(z.string()).default([]),
  carousel_png: z.array(z.string()).default([]),
  script_path: z.string().nullable().default(null),
  missing: z.array(z.string()).default([]),
});
export type DayContent = z.infer<typeof DayContent>;

function readIfExists(p: string): string | null {
  return fs.existsSync(p) ? fs.readFileSync(p, "utf8") : null;
}

// Разбирает markdown карусели: карточки по "## Заголовок" + текст под ним.
function parseCarouselMd(md: string): Array<z.infer<typeof DayCard>> {
  const cards: Array<z.infer<typeof DayCard>> = [];
  const blocks = md.split(/^##\s+/m).slice(1);
  for (const b of blocks) {
    const [head, ...rest] = b.split("\n");
    const roleMatch = head.match(/^\[([a-z_]+)\]\s*(.*)$/i);
    cards.push({
      role: roleMatch ? roleMatch[1].toLowerCase() : "",
      title: (roleMatch ? roleMatch[2] : head).trim(),
      body: rest.join("\n").trim(),
    });
  }
  return cards;
}

function listFiles(dir: string, exts: string[]): string[] {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => exts.some((e) => f.toLowerCase().endsWith(e)))
    .map((f) => path.join(dir, f))
    .sort();
}

/**
 * get_content_by_date — главный вход адаптера.
 * Читает существующую структуру дня. Ничего не выдумывает: чего нет,
 * попадает в missing[]. Если дня нет вообще — found=false.
 */
export function getContentByDate(date: string): DayContent {
  const dir = dayDir(date);
  const missing: string[] = [];

  if (!fs.existsSync(dir)) {
    return DayContent.parse({ date, found: false, missing: ["весь день (папка не найдена)"] });
  }

  const source = path.join(dir, "source");
  const metaRaw = readIfExists(path.join(source, "meta.json"));
  const meta = metaRaw ? safeJson(metaRaw) : {};

  const carouselMd =
    readIfExists(path.join(source, "carousel.md")) || readIfExists(path.join(dir, "carousel", "carousel.md"));
  const cards = carouselMd ? parseCarouselMd(carouselMd) : [];
  if (!cards.length) missing.push("текст карусели");

  const post = readIfExists(path.join(source, "post.md")) || "";
  if (!post) missing.push("текст поста");

  const visuals = listFiles(path.join(dir, "visuals"), [".png", ".jpg", ".jpeg", ".webp", ".mp4", ".mov"]);
  const carouselPng = listFiles(path.join(dir, "carousel"), [".png", ".jpg", ".jpeg"]);
  if (!visuals.length && !carouselPng.length) missing.push("визуалы/карточки");

  // Существующий сценарий (последняя версия), если есть.
  const reels = path.join(dir, "reels");
  let scriptPath: string | null = null;
  if (fs.existsSync(reels)) {
    const scripts = fs.readdirSync(reels).filter((f) => /^reels_script(_v\d+)?\.json$/.test(f)).sort();
    if (scripts.length) scriptPath = path.join(reels, scripts[scripts.length - 1]);
  }

  return DayContent.parse({
    date,
    found: true,
    topic: str(meta.topic) || firstCardTitle(cards),
    content_type: str(meta.content_type) || "educational_reels",
    goal: str(meta.goal) || "reach",
    audience: str(meta.audience),
    platform: str(meta.platform) || "instagram",
    desired_action: str(meta.desired_action),
    cta: str(meta.cta),
    links: Array.isArray(meta.links) ? meta.links.map(String) : [],
    notes: str(meta.notes),
    reels_duration_seconds: Number(meta.reels_duration_seconds) || 30,
    card_count: Number(meta.card_count) || cards.length || 7,
    cards,
    post,
    visuals,
    carousel_png: carouselPng,
    script_path: scriptPath,
    missing,
  });
}

function safeJson(s: string): any {
  try {
    return JSON.parse(s);
  } catch {
    return {};
  }
}
function str(v: unknown): string {
  return typeof v === "string" ? v : "";
}
function firstCardTitle(cards: Array<z.infer<typeof DayCard>>): string {
  return cards[0]?.title || "";
}
export type { DayContent as DayContentType };

/**
 * Строит индекс дата → материалы по реальным папкам content/.
 * Пишет content/index.json. Выдуманные материалы не добавляет.
 */
export function buildIndex(): Record<string, unknown> {
  const root = config.contentRoot;
  const index: Record<string, unknown> = {};
  if (fs.existsSync(root)) {
    for (const month of fs.readdirSync(root)) {
      const mdir = path.join(root, month);
      if (!fs.statSync(mdir).isDirectory() || !/^\d{4}-\d{2}$/.test(month)) continue;
      for (const day of fs.readdirSync(mdir)) {
        if (!/^\d{4}-\d{2}-\d{2}$/.test(day)) continue;
        const c = getContentByDate(day);
        index[day] = {
          topic: c.topic,
          content_type: c.content_type,
          status_path: path.relative(root, path.join(mdir, day, "status.json")),
          carousel_present: c.cards.length > 0 || c.carousel_png.length > 0,
          visuals_present: c.visuals.length > 0,
          missing: c.missing,
        };
      }
    }
  }
  fs.mkdirSync(root, { recursive: true });
  fs.writeFileSync(path.join(root, "index.json"), JSON.stringify(index, null, 2), "utf8");
  return index;
}
