# -*- coding: utf-8 -*-
"""AlovLab · showcase-карусель «Промпт решает: дорого или дёшево».
На КАЖДОМ слайде: рисунок темы + ПОЛЬЗА (для чего/бизнес) + НЕЙРОСЕТЬ + готовый ПРОМПТ + разбор.
Стиль showcase. RU кроме AlovLab и промптов (EN). Запуск: python3 scripts/carousel_showcase_prompts.py
"""
import pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, icon, ICONS, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "prompts"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "prompts.html"

EXTRA = r"""
.hsm .head h2{font-size:36px}
.info{position:relative;z-index:4;margin-top:16px;display:grid;grid-template-columns:70px 1fr;gap:15px;align-items:center}
.info .ill{width:70px;height:70px;border-radius:15px;flex:0 0 auto;display:grid;place-items:center;
 background:radial-gradient(circle at 50% 34%,rgba(255,160,80,.28),rgba(22,13,7,.92) 62%);
 border:1px solid rgba(255,160,90,.28);box-shadow:inset 0 -10px 20px rgba(255,120,40,.25),0 10px 26px -10px rgba(255,110,30,.3)}
.info .ill svg{width:60%;height:60%}
.info .rows{display:flex;flex-direction:column;gap:6px}
.info .r{font-size:12.5px;line-height:1.25;color:#fff;font-weight:600}
.info .r b{display:inline-block;min-width:74px;color:var(--o2);font-weight:800;text-transform:uppercase;font-size:9.5px;letter-spacing:.05em}
.pbox{position:relative;z-index:4;margin-top:16px;background:#120c06;border:1px solid rgba(255,150,80,.28);
 border-left:3px solid var(--o);border-radius:14px;padding:16px 18px}
.pbox .tag{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px;margin-bottom:11px}
.pbox code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:12px;line-height:1.52;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pbox .ru{margin-top:11px;padding-top:10px;border-top:1px solid rgba(255,255,255,.1);font-size:11.5px;line-height:1.4;color:#b9ad9b}
.pbox .ru b{color:#fff}
"""
CSS = CSS0 + EXTRA

# рисунки тем (line-art, оранжевый; используют #ig из DEFS слайда)
SUB = {
 "dish":  '<svg viewBox="0 0 100 100" fill="none"><ellipse cx="50" cy="64" rx="33" ry="9" stroke="url(#ig)" stroke-width="5"/><path d="M35 60c3-12 27-12 30 0" stroke="url(#ig)" stroke-width="5"/><path d="M45 42c-3-8 4-11 2-19M55 44c-2-6 3-9 2-15" stroke="url(#ig)" stroke-width="4" opacity=".85" stroke-linecap="round"/></svg>',
 "bottle":'<svg viewBox="0 0 100 100" fill="none"><rect x="38" y="36" width="24" height="42" rx="6" stroke="url(#ig)" stroke-width="5"/><rect x="44" y="22" width="12" height="14" rx="2" stroke="url(#ig)" stroke-width="5"/><path d="M44 52h12" stroke="url(#ig)" stroke-width="4" stroke-linecap="round"/></svg>',
 "portrait":'<svg viewBox="0 0 100 100" fill="none"><circle cx="50" cy="40" r="13" stroke="url(#ig)" stroke-width="5"/><path d="M27 78c0-14 10-21 23-21s23 7 23 21" stroke="url(#ig)" stroke-width="5"/></svg>',
 "interior":'<svg viewBox="0 0 100 100" fill="none"><path d="M50 20v13M41 33h18l-4 11H45z" stroke="url(#ig)" stroke-width="4.5" stroke-linejoin="round"/><path d="M28 76h44M35 76V56h30v20" stroke="url(#ig)" stroke-width="4.5" stroke-linejoin="round"/></svg>',
 "ring":  '<svg viewBox="0 0 100 100" fill="none"><circle cx="50" cy="60" r="19" stroke="url(#ig)" stroke-width="5"/><path d="M42 34l8-11 8 11-8 8z" stroke="url(#ig)" stroke-width="4.5" stroke-linejoin="round"/></svg>',
}

def cover(hw, ho, sub, ic):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb big">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">AlovLab · промпты для картинок</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
  {FOOT}
</article>"""

def prm(num, total, hw, ho, ill, net, biz, code, ru):
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Промпт</span><span class="pg">{num}<b> / {total}</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="info"><div class="ill">{SUB[ill]}</div>
    <div class="rows"><div class="r"><b>Нейросеть</b> {net}</div><div class="r"><b>Бизнес</b> {biz}</div></div></div>
  <div class="pbox"><span class="tag">Скопировать</span><code>{code}</code><div class="ru"><b>Разбор:</b> {ru}</div></div>
  {FOOT}
</article>"""

def cta(hw, ho, items, btn):
    lis="".join(f'<div class="li"><i></i><span>{t}</span></div>' for t in items)
    return f"""<article class="slide cta">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings" style="top:120%">{rings()}</div></div>
  <div class="top"><span class="eb">Дальше</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="clist">{lis}</div>
  <div class="btn">{btn}</div>
  {FOOT}
</article>"""

FORMULA = """[объект]        — что в кадре
[действие]      — что делает / остаётся стабильным
[камера]        — 85mm, макро, ракурс
[свет]          — тёплый боковой / контровой
[стиль]         — editorial, food commercial
[ограничения]   — no plastic, no distortion"""

SLIDES = [
 cover("Промпт решает —", "дорого или дёшево.",
       "Не «сделай красиво». Точная инструкция: объект, свет, ракурс, материал, стиль.", "spark"),
 f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Формула</span><span class="pg">0 / 5</span></div>
  <div class="head"><h2><span class="w">Формула</span><span class="o">премиум-кадра</span></h2></div>
  <div class="pbox"><span class="tag">Структура</span><code>{FORMULA}</code>
    <div class="ru"><b>Разбор:</b> одна деталь = одна инструкция. Чем точнее — тем дороже кадр и меньше попыток.</div></div>
  {FOOT}
</article>""",
 prm(1,5,"Дорогое","фото блюда","dish","Midjourney · Flux","ресторан · кафе · доставка",
   "A gourmet scallop on dark stone, warm amber side-light, delicate rising steam, glossy sauce highlights, shallow depth of field, moody near-black background with warm bokeh, 85mm, editorial food commercial, hyper-detailed, no plastic look.",
   "объект + тёплый боковой свет + пар + тёмный фон + макро-оптика + запрет «пластика»."),
 prm(2,5,"Премиум","карточка товара","bottle","Recraft · Flux · Midjourney","e-com · бренд · маркетплейс",
   "A luxury perfume bottle on wet black marble, soft top light with one warm rim light, subtle reflections and condensation, deep shadows, minimalist premium advertising, macro, ultra-detailed, balanced exposure.",
   "товар + мокрый отражающий стол + один контровой свет + минимализм + макро."),
 prm(3,5,"Обложечный","портрет","portrait","Flux · Midjourney","эксперт · коуч · личный бренд",
   "Editorial portrait of a confident founder in a dark studio, warm rim light on the face, soft key from camera-left, shallow depth of field, cinematic color grade, 85mm, natural skin texture, magazine-cover quality.",
   "портрет + тёмная студия + контровой + мягкий ключевой сбоку + натуральная кожа."),
 prm(4,5,"Кинематографичный","интерьер","interior","Midjourney · Flux","отель · ресторан · недвижимость",
   "Upscale restaurant interior at dusk, warm pendant lights and candle glow, deep perspective, warm bokeh, moody cinematic tones, architectural-digest style, realistic, balanced exposure, no distortion.",
   "интерьер + тёплые лампы + глубина + кинотон + без искажения геометрии."),
 prm(5,5,"Ювелирный","макро-кадр","ring","Midjourney · Flux","ювелирка · люкс · аксессуары",
   "Macro of a diamond ring on dark velvet, a single warm key light creating sharp sparkle and caustics, deep black background, luxury jewelry advertising, ultra-detailed, shallow depth of field, no blown highlights.",
   "украшение + чёрный бархат + один жёсткий свет для блеска + макро + без пересветов."),
 cta("Забери","набор промптов.",
     ["<b>готовые промпты</b> под еду, товар, портрет, интерьер, украшение",
      "формула, по которой соберёшь свой под любую нишу",
      "негатив-лист, чтобы не было «пластика» и артефактов"],
     "Промпты → t.me/AlovLab"),
]

HTML = f"""<title>Промпт решает: дорого или дёшево · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · showcase · высококачественные промпты</span>
    <h1>Одним постом: обложка → формула → 5 промптов (рисунок + нейросеть + бизнес + промпт) → CTA.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
