import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { chromium, type Browser } from "playwright-core";
import { createLogger } from "../logger";
import { cardHtml, cardFileName, CARD_WIDTH, CARD_HEIGHT } from "./template";
import type { Card } from "../store/types";

const log = createLogger("render");

// Имена исполняемого файла браузера в разных сборках (Linux/macOS/Chrome for Testing).
const CHROME_BINARIES = new Set(["chrome", "Chromium", "Google Chrome for Testing", "headless_shell"]);

// Bounded-поиск бинарника Chromium внутри каталога сборки (депта ограничена).
function findChromeBinary(root: string, depth = 0): string | undefined {
  if (depth > 6) return undefined;
  let entries: fs.Dirent[];
  try {
    entries = fs.readdirSync(root, { withFileTypes: true });
  } catch {
    return undefined;
  }
  for (const e of entries) {
    const full = path.join(root, e.name);
    if (e.isFile() && CHROME_BINARIES.has(e.name)) return full;
    // .app на macOS — это каталог, заходим внутрь
    if (e.isDirectory()) {
      const found = findChromeBinary(full, depth + 1);
      if (found) return found;
    }
  }
  return undefined;
}

/**
 * Ищет исполняемый Chromium в любом расположении и версии:
 * env → преднастроенный Playwright (/opt/pw-browsers) → кэш ms-playwright
 * (macOS ~/Library/Caches/ms-playwright, Linux ~/.cache/ms-playwright).
 */
function resolveChromium(): string | undefined {
  if (process.env.CHROMIUM_PATH && fs.existsSync(process.env.CHROMIUM_PATH)) {
    return process.env.CHROMIUM_PATH;
  }
  const bases = [
    process.env.PLAYWRIGHT_BROWSERS_PATH,
    "/opt/pw-browsers",
    path.join(os.homedir(), "Library", "Caches", "ms-playwright"),
    path.join(os.homedir(), ".cache", "ms-playwright"),
  ].filter(Boolean) as string[];

  for (const base of bases) {
    let dirs: string[];
    try {
      dirs = fs.readdirSync(base).filter((d) => d.startsWith("chromium")).sort().reverse();
    } catch {
      continue;
    }
    for (const d of dirs) {
      const found = findChromeBinary(path.join(base, d));
      if (found) return found;
    }
  }
  return undefined;
}

async function launch(): Promise<Browser> {
  const executablePath = resolveChromium();
  return chromium.launch({
    executablePath,
    args: ["--no-sandbox", "--disable-gpu", "--font-render-hinting=none"],
  });
}

export interface RenderedCard {
  file: string; // абсолютный путь
  name: string; // 01_cover.png
}

/**
 * Рендерит все карточки в PNG 1080×1350 без потери текста и обрезки.
 * Один файл — одна карточка, стабильные поля.
 */
export async function renderCards(cards: Card[], outDir: string): Promise<RenderedCard[]> {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await launch();
  const out: RenderedCard[] = [];
  try {
    const page = await browser.newPage({
      viewport: { width: CARD_WIDTH, height: CARD_HEIGHT },
      deviceScaleFactor: 1,
    });
    for (const card of cards) {
      await page.setContent(cardHtml(card, cards.length), { waitUntil: "load" });
      await page.evaluate(() => (document as any).fonts?.ready);
      const name = cardFileName(card);
      const file = path.join(outDir, name);
      await page.screenshot({
        path: file,
        clip: { x: 0, y: 0, width: CARD_WIDTH, height: CARD_HEIGHT },
      });
      out.push({ file, name });
    }
    await page.close();
    log.info(`Отрендерено карточек: ${out.length} → ${outDir}`);
  } finally {
    await browser.close();
  }
  return out;
}

/** Собирает превью-полосу всей карусели (первые карточки) в один PNG. */
export async function renderPreview(cards: Card[], outFile: string): Promise<string> {
  const browser = await launch();
  try {
    const thumbs = cards
      .slice(0, 6)
      .map((c) => `<div class="t">${cardHtmlThumb(c, cards.length)}</div>`)
      .join("");
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>
      *{margin:0;box-sizing:border-box}
      body{background:#0b0a09;display:flex;gap:16px;padding:24px}
      .t{width:216px;height:270px;overflow:hidden;border-radius:12px;
         border:1px solid rgba(244,240,232,0.12)}
      .t > *{transform:scale(0.2);transform-origin:top left}
    </style></head><body>${thumbs}</body></html>`;
    const width = 24 + cards.slice(0, 6).length * (216 + 16);
    const page = await browser.newPage({ viewport: { width, height: 318 } });
    await page.setContent(html, { waitUntil: "load" });
    await page.evaluate(() => (document as any).fonts?.ready);
    await page.screenshot({ path: outFile });
    await page.close();
    return outFile;
  } finally {
    await browser.close();
  }
}

// Уменьшенная вставка карточки для превью (тот же HTML, без внешней обёртки).
function cardHtmlThumb(card: Card, total: number): string {
  const full = cardHtml(card, total);
  const body = full.match(/<body>([\s\S]*)<\/body>/i)?.[1] || "";
  const style = full.match(/<style>([\s\S]*?)<\/style>/i)?.[1] || "";
  return `<div style="width:${CARD_WIDTH}px;height:${CARD_HEIGHT}px"><style>${style}</style>${body}</div>`;
}
