# -*- coding: utf-8 -*-
"""AlovLab · День 9 (12.08) «Факты, а не вода» — IMAGE-FORWARD карусель.
Каждый слайд = готовая картинка пользователя на всю площадь + тонкая плашка AlovLab
(рубрика + N/8 + лого), где нужно — короткий русский заголовок и промпт-карточка.
Картинки лежат в content/carousel-assets/day-09-perplexity/_res/s1..s7.jpg (1080×1350).
Честность: img-3 (s3-панель) оставлена по прямому решению пользователя.
RU кроме AlovLab и промпта. Запуск: python3 scripts/carousel_showcase_day9.py"""
import base64, pathlib
from carousel_showcase_render import CSS as CSS0, LOGO, ROOT, rings

ASSETS = ROOT / "content" / "carousel-assets" / "day-09-perplexity" / "_res"
def img(n): return "data:image/jpeg;base64," + base64.b64encode((ASSETS / f"s{n}.jpg").read_bytes()).decode()
IMG = {n: img(n) for n in range(1, 8)}

OUTDIR = ROOT / "exports" / "carousels" / "day-09-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-09-showcase.html"

EXTRA = r"""
.slide{position:relative;width:min(540px,92vw);aspect-ratio:4/5;border-radius:22px;overflow:hidden;
 background:#0a0806;font-family:'Manrope',system-ui,sans-serif;color:#fff}
.slide .bg{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0}
.scrT{position:absolute;top:0;left:0;right:0;height:42%;z-index:1;pointer-events:none;
 background:linear-gradient(180deg,rgba(5,3,2,.94),rgba(5,3,2,.5) 46%,transparent)}
.scrB{position:absolute;bottom:0;left:0;right:0;height:46%;z-index:1;pointer-events:none;
 background:linear-gradient(0deg,rgba(5,3,2,.95),rgba(5,3,2,.48) 50%,transparent)}
/* верхняя плашка */
.top{position:absolute;top:22px;left:23px;right:23px;display:flex;justify-content:space-between;align-items:center;z-index:4}
.eb{font-weight:800;font-size:11.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--o2);
 background:rgba(18,11,6,.62);border:1px solid rgba(232,103,42,.36);border-radius:20px;padding:7px 13px}
.pg{font-weight:800;font-size:15px;color:#fff;background:rgba(18,11,6,.55);border:1px solid rgba(255,255,255,.1);
 border-radius:20px;padding:6px 12px;font-variant-numeric:tabular-nums}
.pg b{color:var(--o2)}
/* лого */
.foot{position:absolute;left:24px;bottom:22px;display:flex;align-items:center;gap:9px;z-index:4}
.foot .mk{width:30px;height:30px;border-radius:8px}
.foot .wm{position:relative;font-weight:800;font-size:17px;letter-spacing:.02em}
.foot .wm::after{content:"";position:absolute;left:0;right:0;bottom:-7px;height:3px;border-radius:2px;
 background:linear-gradient(90deg,var(--o),transparent)}
/* заголовок */
.hl{position:absolute;left:24px;right:24px;z-index:4}
.hl.t{top:72px}.hl.b{bottom:82px}
.hl h2{font-weight:800;text-transform:uppercase;line-height:1.0;font-size:41px;letter-spacing:-.012em;
 text-shadow:0 2px 22px rgba(0,0,0,.6)}
.hl h2 .o{display:block;background:linear-gradient(180deg,var(--o3),var(--o));-webkit-background-clip:text;background-clip:text;color:transparent}
.hl p{margin-top:13px;font-size:16px;line-height:1.4;color:#e0d6c8;max-width:29ch;font-weight:500;text-shadow:0 1px 10px rgba(0,0,0,.7)}
/* нижняя объединённая плашка (для слайдов с собственным заголовком в кадре) */
.barB{position:absolute;left:23px;right:23px;bottom:22px;display:flex;justify-content:space-between;align-items:center;z-index:4}
.barB .lg{display:flex;align-items:center;gap:9px}
.barB .lg .mk{width:30px;height:30px;border-radius:8px}
.barB .lg .wm{position:relative;font-weight:800;font-size:17px}
.barB .lg .wm::after{content:"";position:absolute;left:0;right:0;bottom:-7px;height:3px;border-radius:2px;background:linear-gradient(90deg,var(--o),transparent)}
.barB .rt{display:flex;align-items:center;gap:9px}
/* промпт-карточка */
.pcard{position:absolute;left:24px;right:24px;bottom:78px;z-index:4;background:rgba(9,6,3,.86);
 border:1px solid rgba(255,150,80,.32);border-left:3px solid var(--o);border-radius:14px;padding:14px 16px}
.pcard .tag{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px;margin-bottom:10px}
.pcard code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:11.5px;line-height:1.5;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pcard .ru{margin-top:10px;padding-top:9px;border-top:1px solid rgba(255,255,255,.12);font-size:11px;line-height:1.4;color:#c2b6a4}
.pcard .ru b{color:#fff}
/* CTA */
.slide.cta .bg{filter:brightness(.34) saturate(.85)}
.slide.cta .stage{position:absolute;inset:0;z-index:1;display:grid;place-items:center;pointer-events:none}
.slide.cta .rings{position:absolute;top:58%;left:50%;transform:translate(-50%,-50%)}
.slide.cta .rings i{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);border-radius:50%;border:1px solid rgba(255,140,60,.5)}
.slide.cta .clist{position:absolute;left:26px;right:26px;bottom:150px;z-index:4;display:flex;flex-direction:column;gap:11px}
.slide.cta .li{display:flex;gap:11px;align-items:flex-start;font-size:15.5px;color:#e0d6c8;line-height:1.34;text-shadow:0 1px 10px rgba(0,0,0,.7)}
.slide.cta .li i{width:8px;height:8px;border-radius:50%;background:var(--o2);flex:0 0 auto;margin-top:6px;box-shadow:0 0 8px 1px rgba(255,140,60,.7)}
.slide.cta .li b{color:#fff}
.slide.cta .btn{position:absolute;left:26px;bottom:78px;z-index:4;font-weight:800;font-size:16px;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));border-radius:13px;padding:15px 24px;box-shadow:0 16px 34px -12px rgba(232,103,42,.8)}
"""
CSS = CSS0 + EXTRA

MK = f'<img class="mk" src="data:image/png;base64,{LOGO}">'
def foot():   return f'<div class="foot">{MK}<span class="wm">AlovLab</span></div>'
def top(eb, pg): return f'<div class="top"><span class="eb">{eb}</span><span class="pg">{pg}<b> / 8</b></span></div>'
def barB(eb, pg):
    return (f'<div class="barB"><div class="lg">{MK}<span class="wm">AlovLab</span></div>'
            f'<div class="rt"><span class="eb">{eb}</span><span class="pg">{pg}<b> / 8</b></span></div></div>')
def hl(pos, w, o, p=""):
    sub = f'<p>{p}</p>' if p else ""
    return f'<div class="hl {pos}"><h2><span class="w">{w}</span><span class="o">{o}</span></h2>{sub}</div>'

def bg(n): return f'<div class="bg" style="background-image:url({IMG[n]})"></div>'

# 1 · Обложка — s2 (FACTS FIRST NOT FLUFF)
S1 = f"""<article class="slide">{bg(2)}<div class="scrT"></div><div class="scrB"></div>
 {top('AlovLab · факты, а не вода','1')}
 {hl('t','Вода — это не','стиль. Это лень.','Текст звучит пусто не потому, что ты плохо пишешь. Под ним просто нет фактуры.')}
 {foot()}</article>"""

# 2 · Проблема — s4 (буллшит-слова)
S2 = f"""<article class="slide">{bg(4)}<div class="scrT"></div><div class="scrB"></div>
 {top('Проблема','2')}
 {hl('b','Текст звучит','общо.','«Инновационный», «эффективный», «качественный» — слова, которые подходят чему угодно и не значат ничего.')}
 {foot()}</article>"""

# 3 · Причина — s5 (пустой Evidence)
S3 = f"""<article class="slide">{bg(5)}<div class="scrT"></div><div class="scrB"></div>
 {top('Причина','3')}
 {hl('b','Под текстом','пусто.','Красивое резюме есть, а доказательств — нет. Словам не на чём стоять.')}
 {foot()}</article>"""

# 4 · Ошибка — s6 (переписываешь vs собираешь) — свой заголовок в кадре
S4 = f"""<article class="slide">{bg(6)}<div class="scrB"></div>
 {barB('Ошибка · день 9','4')}</article>"""

# 5 · Метод — s7 (5 шагов) — свой заголовок в кадре
S5 = f"""<article class="slide">{bg(7)}<div class="scrB"></div>
 {barB('Метод · Perplexity','5')}</article>"""

# 6 · Форма факта — s3 (вода vs факт)
S6 = f"""<article class="slide">{bg(3)}<div class="scrT"></div><div class="scrB"></div>
 {top('Форма факта','6')}
 {hl('t','Не эпитет —','а фактура.','Факт всегда конкретен и проверяем: цифра + источник + дата. Нет источника — нет факта.')}
 {foot()}</article>"""

# 7 · Промпт — s1 (рабочий стол) + промпт-карточка
S7 = f"""<article class="slide">{bg(1)}<div class="scrT"></div><div class="scrB"></div>
 {top('Готовый промпт · Perplexity','7')}
 {hl('t','Собери факты','под свою тему.')}
 <div class="pcard"><span class="tag">Perplexity · скопировать</span><code>Собери 7 проверенных фактов по теме: [ТВОЯ ТЕМА].
Только с источниками (ссылка + дата). Приоритет —
официальные данные и исследования. Формат каждого:
факт → цифра → источник → год. Исключи рекламу и мнения.</code>
  <div class="ru"><b>Разбор:</b> узкая тема + требование источника + жёсткий формат = лист фактуры, а не пересказ рекламы.</div></div>
 {foot()}</article>"""

# 8 · CTA
S8 = f"""<article class="slide cta">{bg(1)}
 <div class="scrT"></div><div class="scrB" style="height:100%"></div>
 <div class="stage"><div class="rings">{rings()}</div></div>
 {top('Дальше','8')}
 {hl('t','Сначала факты —','потом текст.')}
 <div class="clist">
  <div class="li"><i></i><span><b>7 фактов с источниками</b> за 15 минут — бланк в тетради дня</span></div>
  <div class="li"><i></i><span>как искать и проверять: что считать источником, а что — рекламой</span></div>
  <div class="li"><i></i><span>инструмент дня — Perplexity</span></div>
 </div>
 <div class="btn">Тетрадь дня → t.me/AlovLab</div>
 {foot()}</article>"""

SLIDES = [S1, S2, S3, S4, S5, S6, S7, S8]

HTML = f"""<title>Факты, а не вода · День 9 · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 9 · 12 августа · image-forward</span>
    <h1>Факты, а не вода: обложка → проблема → причина → ошибка → метод (Perplexity) → форма факта → промпт → CTA. 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
