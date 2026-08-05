import path from "node:path";
import fs from "node:fs";
import type { Card } from "../store/types";

export const CARD_WIDTH = 1080;
export const CARD_HEIGHT = 1350; // Instagram 4:5

// Фирменные цвета AlovLab (взяты 1:1 из css/styles.css лендинга).
const BRAND = {
  bg: "#0b0a09",
  bg2: "#100e0c",
  surface: "#16130f",
  text: "#f4f0e8",
  text2: "#cbc3b5",
  muted: "#948b7d",
  orange: "#e8672a",
  orangeHi: "#ff8a3d",
  line: "rgba(244,240,232,0.10)",
};

// Абсолютный путь к шрифтам лендинга (../../assets/fonts от studio/src/carousel).
function fontsDir(): string {
  return path.resolve(__dirname, "..", "..", "..", "assets", "fonts");
}

function fontFace(): string {
  const dir = fontsDir();
  const files: Array<[string, number]> = [
    ["manrope-cyrillic-400.woff2", 400],
    ["manrope-cyrillic-500.woff2", 500],
    ["manrope-cyrillic-700.woff2", 700],
    ["manrope-cyrillic-800.woff2", 800],
  ];
  return files
    .filter(([f]) => fs.existsSync(path.join(dir, f)))
    .map(
      ([f, w]) => `@font-face{font-family:"Manrope";font-weight:${w};font-display:block;
        src:url("file://${path.join(dir, f)}") format("woff2");}`
    )
    .join("\n");
}

function esc(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

// Подсветка ключевой фразы оранжевым внутри body.
function highlight(body: string, accent: string): string {
  const safe = esc(body);
  if (!accent) return safe;
  const a = esc(accent.trim());
  if (!a) return safe;
  const idx = safe.toLowerCase().indexOf(a.toLowerCase());
  if (idx === -1) return safe;
  return (
    safe.slice(0, idx) +
    `<span class="accent">${safe.slice(idx, idx + a.length)}</span>` +
    safe.slice(idx + a.length)
  );
}

function counter(index: number, total: number): string {
  const n = String(index + 1).padStart(2, "0");
  const t = String(total).padStart(2, "0");
  return `${n} / ${t}`;
}

/** HTML одной карточки 1080×1350 в стиле AlovLab. */
export function cardHtml(card: Card, total: number): string {
  const isCover = card.role === "cover";
  const isCta = card.role === "cta";
  const titleSize = isCover ? 108 : 76;
  const bodySize = isCover ? 44 : 46;

  return `<!doctype html><html lang="ru"><head><meta charset="utf-8">
<style>
${fontFace()}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:${CARD_WIDTH}px;height:${CARD_HEIGHT}px;}
body{
  font-family:"Manrope",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
  background:
    radial-gradient(1200px 700px at 78% -8%, rgba(232,103,42,0.16), transparent 60%),
    linear-gradient(160deg, ${BRAND.bg2}, ${BRAND.bg});
  color:${BRAND.text};
  -webkit-font-smoothing:antialiased;
}
.card{
  width:${CARD_WIDTH}px;height:${CARD_HEIGHT}px;
  padding:96px 92px;display:flex;flex-direction:column;
  ${isCover || isCta ? "justify-content:center;" : "justify-content:flex-start;"}
}
.top{display:flex;align-items:center;justify-content:space-between;
  position:absolute;top:72px;left:92px;right:92px;}
.brand{font-weight:800;letter-spacing:0.02em;font-size:30px;color:${BRAND.text2};}
.brand b{color:${BRAND.orange};}
.count{font-weight:700;font-size:28px;color:${BRAND.muted};
  border:1px solid ${BRAND.line};border-radius:999px;padding:8px 20px;}
.kicker{font-size:30px;font-weight:700;color:${BRAND.orange};
  text-transform:uppercase;letter-spacing:0.14em;margin-bottom:28px;}
.title{font-size:${titleSize}px;font-weight:800;line-height:1.04;
  letter-spacing:-0.015em;margin-bottom:${isCover ? 40 : 36}px;
  ${isCover ? "" : "max-width:900px;"}}
.body{font-size:${bodySize}px;font-weight:500;line-height:1.34;color:${BRAND.text2};
  max-width:860px;}
.accent{color:${BRAND.orangeHi};font-weight:700;}
.rule{height:6px;width:120px;background:linear-gradient(90deg,${BRAND.orangeHi},${BRAND.orange});
  border-radius:6px;margin-bottom:44px;}
.foot{position:absolute;bottom:70px;left:92px;right:92px;
  display:flex;justify-content:space-between;align-items:center;
  font-size:26px;color:${BRAND.muted};font-weight:600;}
.foot .cta{color:${BRAND.orange};}
</style></head>
<body><div class="card">
  <div class="top">
    <div class="brand"><b>AlovLab</b> · Автоконтент</div>
    <div class="count">${counter(card.index, total)}</div>
  </div>
  ${isCover || isCta ? "" : `<div class="kicker">${esc(roleKicker(card.role))}</div>`}
  ${isCover || isCta ? "" : `<div class="rule"></div>`}
  <div class="title">${esc(card.title)}</div>
  ${card.body ? `<div class="body">${highlight(card.body, card.accent)}</div>` : ""}
  <div class="foot">
    <span>alovlab.ru</span>
    ${isCta ? '<span class="cta">t.me/AlovLab</span>' : "<span>@alovlab</span>"}
  </div>
</div></body></html>`;
}

function roleKicker(role: Card["role"]): string {
  const map: Record<string, string> = {
    problem: "Проблема",
    insight: "Разворот",
    solution: "Метод",
    example: "Пример",
    action: "Шаг",
    cover: "",
    cta: "",
  };
  return map[role] || "";
}

/** Имя PNG-файла карточки: 01_cover.png, 02_problem.png … */
export function cardFileName(card: Card): string {
  const n = String(card.index + 1).padStart(2, "0");
  return `${n}_${card.role}.png`;
}
