# -*- coding: utf-8 -*-
"""AlovLab · showcase-карусель «Midjourney и Nano Banana: что чем делать» (экспертная).
На каждом слайде: рисунок темы + КАКОЙ инструмент и почему + бизнес + готовый промпт с синтаксисом + приём.
Nano Banana = image-модель Google (редактура/консистентность/текст). Midjourney = премиум с нуля.
Стиль showcase. RU кроме подписи AlovLab и промптов (EN). Запуск: python3 scripts/carousel_showcase_prompts.py
"""
import pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, icon, ICONS, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "prompts"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "prompts.html"

EXTRA = r"""
.hsm .head h2{font-size:35px}
.info{position:relative;z-index:4;margin-top:15px;display:grid;grid-template-columns:66px 1fr;gap:14px;align-items:center}
.info .ill{width:66px;height:66px;border-radius:15px;display:grid;place-items:center;
 background:radial-gradient(circle at 50% 34%,rgba(255,160,80,.28),rgba(22,13,7,.92) 62%);
 border:1px solid rgba(255,160,90,.28);box-shadow:inset 0 -10px 20px rgba(255,120,40,.25),0 10px 26px -10px rgba(255,110,30,.3)}
.info .ill svg{width:60%;height:60%}
.info .rows{display:flex;flex-direction:column;gap:6px}
.info .r{font-size:12.5px;line-height:1.25;color:#fff;font-weight:600}
.info .r b{display:inline-block;min-width:72px;color:var(--o2);font-weight:800;text-transform:uppercase;font-size:9.5px;letter-spacing:.05em}
.info .r i{font-style:normal;color:#b9ad9b}
.pbox{position:relative;z-index:4;margin-top:14px;background:#120c06;border:1px solid rgba(255,150,80,.28);
 border-left:3px solid var(--o);border-radius:14px;padding:15px 17px}
.pbox .tag{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px;margin-bottom:10px}
.pbox code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:11.5px;line-height:1.5;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pbox .ru{margin-top:10px;padding-top:9px;border-top:1px solid rgba(255,255,255,.1);font-size:11px;line-height:1.38;color:#b9ad9b}
.pbox .ru b{color:#fff}
.pbox .tip{margin-top:7px;font-size:11px;line-height:1.35;color:var(--o2);font-weight:700}

.vs{position:relative;z-index:4;margin-top:18px;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.vp{background:#140e07;border:1px solid rgba(255,150,80,.22);border-radius:16px;padding:16px 15px}
.vp .nm{font-weight:800;font-size:16px;color:var(--o2);margin-bottom:9px}
.vp .row{font-size:12px;color:#cfc3b2;line-height:1.3;padding:7px 0;border-top:1px solid rgba(255,255,255,.07)}
.vp .row:first-of-type{border-top:none}

.pipe{position:relative;z-index:4;margin-top:18px;display:flex;flex-direction:column;gap:9px}
.pipe .step{display:grid;grid-template-columns:104px 1fr;gap:12px;align-items:center;background:#140e07;
 border:1px solid rgba(255,150,80,.18);border-radius:13px;padding:13px 15px}
.pipe .step .k{font-weight:800;font-size:13px;color:#fff}
.pipe .step .v{font-size:12.5px;color:var(--o2);font-weight:700}
"""
CSS = CSS0 + EXTRA

SUB = {
 "dish":  '<svg viewBox="0 0 100 100" fill="none"><ellipse cx="50" cy="64" rx="33" ry="9" stroke="url(#ig)" stroke-width="5"/><path d="M35 60c3-12 27-12 30 0" stroke="url(#ig)" stroke-width="5"/><path d="M45 42c-3-8 4-11 2-19M55 44c-2-6 3-9 2-15" stroke="url(#ig)" stroke-width="4" opacity=".85" stroke-linecap="round"/></svg>',
 "edit":  '<svg viewBox="0 0 100 100" fill="none"><rect x="22" y="30" width="42" height="34" rx="6" stroke="url(#ig)" stroke-width="5"/><path d="M58 68l16-16 6 6-16 16-8 2z" stroke="url(#ig)" stroke-width="4.5" stroke-linejoin="round"/></svg>',
 "consist":'<svg viewBox="0 0 100 100" fill="none"><circle cx="40" cy="42" r="11" stroke="url(#ig)" stroke-width="4.5"/><circle cx="62" cy="42" r="11" stroke="url(#ig)" stroke-width="4.5" opacity=".55"/><path d="M24 76c0-11 8-18 16-18s16 7 16 18" stroke="url(#ig)" stroke-width="4.5"/></svg>',
 "portrait":'<svg viewBox="0 0 100 100" fill="none"><circle cx="50" cy="40" r="13" stroke="url(#ig)" stroke-width="5"/><path d="M27 78c0-14 10-21 23-21s23 7 23 21" stroke="url(#ig)" stroke-width="5"/></svg>',
 "text":  '<svg viewBox="0 0 100 100" fill="none"><path d="M28 32h44M50 32v42M40 74h20" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/></svg>',
}

def cover(hw, ho, sub, ic):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb big">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">AlovLab · нейросети для картинок</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
  {FOOT}
</article>"""

def prm(num, total, hw, ho, ill, net, netwhy, biz, code, ru, tip):
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Промпт</span><span class="pg">{num}<b> / {total}</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="info"><div class="ill">{SUB[ill]}</div>
    <div class="rows"><div class="r"><b>Нейросеть</b> {net} <i>· {netwhy}</i></div><div class="r"><b>Бизнес</b> <i>{biz}</i></div></div></div>
  <div class="pbox"><span class="tag">Скопировать</span><code>{code}</code>
    <div class="ru"><b>Разбор:</b> {ru}</div><div class="tip">{tip}</div></div>
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

# --- слайды ---
SLIDES = []

SLIDES.append(cover("Midjourney или", "Nano Banana?",
  "Один рисует премиум с нуля. Второй правит твоё фото и держит консистентность. Выбор — под задачу.", "spark"))

# 2 · что чем делать (vs)
SLIDES.append(f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Что чем делать</span><span class="pg">0 / 5</span></div>
  <div class="head"><h2><span class="w">Два инструмента —</span><span class="o">разные задачи.</span></h2></div>
  <div class="vs">
    <div class="vp"><div class="nm">Midjourney</div>
      <div class="row">рисует премиум с нуля</div><div class="row">эстетика и стиль</div>
      <div class="row">параметры: --ar, --sref, --stylize</div><div class="row">слабый текст на картинке</div></div>
    <div class="vp"><div class="nm">Nano Banana</div>
      <div class="row">правит твоё фото</div><div class="row">держит лицо и объект</div>
      <div class="row">понимает точные инструкции</div><div class="row">рендерит читаемый текст</div></div>
  </div>
</article>""")

SLIDES.append(prm(1,5,"Премиум","с нуля","dish","Midjourney","рисует с нуля","ресторан · e-com · бренд",
  "gourmet scallop on dark stone, warm amber side light, delicate rising steam, glossy sauce, shallow depth of field, moody near-black background, editorial food commercial, hyper-detailed --ar 4:5 --style raw --stylize 250",
  "--ar 4:5 формат · --style raw убирает «миджорнишность» · --stylize держит фотореализм.",
  "Приём: --sref &lt;ссылка&gt; — один стиль на всю ленту."))

SLIDES.append(prm(2,5,"Правки","на твоём фото","edit","Nano Banana","правит твоё фото","любой товар · карточки",
  "[загрузи фото товара] Replace the cluttered background with a clean warm-lit studio backdrop. Keep the product, its label and reflections exactly the same. Match the lighting to the product.",
  "Редактирует загруженный кадр и держит объект неизменным — Midjourney так не умеет.",
  "Приём: подгрузи 1–3 референса — смешает и сохранит детали."))

SLIDES.append(prm(3,5,"Один герой","в 10 кадрах","consist","Nano Banana","консистентность лица","личный бренд · эксперт",
  "[загрузи портрет] Place the same person in a dark upscale studio with warm rim light. Keep the exact face, hairstyle and outfit. Editorial magazine look, 85mm.",
  "Держит одно лицо на серии — аватар бренда и линейка постов из одного героя.",
  "Приём: в Midjourney так же — --cref &lt;ссылка&gt; --cw 100."))

SLIDES.append(prm(4,5,"Обложечный","портрет","portrait","Midjourney","эстетика с нуля","эксперт · фэшн · бренд",
  "editorial portrait of a confident founder, dark studio, warm rim light, soft key camera-left, 85mm, natural skin texture, cinematic color grade, magazine cover --ar 4:5 --style raw --stylize 200",
  "MJ даёт «дорогую» эстетику из ничего — но не редактирует твоё фото.",
  "Приём: --seed &lt;число&gt; — повторить и доснять кадр в том же стиле."))

SLIDES.append(prm(5,5,"Текст","и упаковка","text","Nano Banana · Ideogram","текст и упаковка","упаковка · баннеры · обложки",
  "[фон-референс] Add the headline 'ALOVLAB' in clean bold type, perfectly legible, integrated into the warm dark premium scene, subtle glow, no distortion.",
  "Nano Banana и Ideogram рендерят читаемый текст — Midjourney буквы ломает.",
  "Приём: сложную типографику бери в Ideogram."))

# 8 · дальше по конвейеру
SLIDES.append(f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Конвейер</span></div>
  <div class="head"><h2><span class="w">Картинка — старт.</span><span class="o">Дальше — конвейер.</span></h2></div>
  <div class="pipe">
    <div class="step"><span class="k">Картинка</span><span class="v">Midjourney · Nano Banana</span></div>
    <div class="step"><span class="k">Оживить в видео</span><span class="v">Higgsfield · Kling</span></div>
    <div class="step"><span class="k">Голос</span><span class="v">ElevenLabs</span></div>
    <div class="step"><span class="k">Говорящий аватар</span><span class="v">HeyGen</span></div>
  </div>
</article>""")

SLIDES.append(cta("Забери","набор промптов.",
  ["<b>шпаргалка</b> «что чем делать»: MJ · Nano Banana · Ideogram",
   "готовые промпты с параметрами под каждую задачу",
   "приёмы: --sref, --cref, редактура и консистентность"],
  "Промпты → t.me/AlovLab"))

HTML = f"""<title>Midjourney и Nano Banana · промпты · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · showcase · Midjourney и Nano Banana</span>
    <h1>Экспертно: какой инструмент под какую задачу + готовые промпты с синтаксисом и приёмами.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
