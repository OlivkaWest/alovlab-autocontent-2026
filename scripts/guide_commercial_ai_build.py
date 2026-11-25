# -*- coding: utf-8 -*-
"""AlovLab · методичка «PRODUCTION PACK: дорогая AI-реклама» — под Reels/карусель commercial-ai.
Как из одной нейросети получить не сток, а кадр, который купит бренд. Сквозной кейс — премиум-
кроссовки. Режиссёрский бриф, референс-борд, готовые промпты по конвейеру (Nano Banana Pro →
Seedance 2.5 → Gemini Omni Flash → Veo 3.1 → Runway Gen-4.5 → Higgsfield), deliverables и лестница
ценности. Модели сверены на 11.08.2026.

ВИЗУАЛЬНОЕ ПРАВИЛО: фотореал = доказательство, SVG = только объяснение (подписи, выноски, waveform).
Все продуктовые кадры — реальные фото одного и того же кроссовка (content/carousel-assets/commercial/).
Премиум фикс-A4, светлые страницы, тёмные плашки под промпты. База CSS — из v2.
Запуск: python3 scripts/guide_commercial_ai_build.py"""
import base64, math, pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "commercial-ai-pack"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-commercial-ai-pack.html"
ASSET = ROOT / "content" / "carousel-assets" / "commercial"

EXTRA = r"""
.stage{display:flex;align-items:center;gap:12px;margin:2px 0 6px}
.stage .b{font-weight:800;font-size:9pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));
 padding:5px 11px;border-radius:20px;letter-spacing:.04em;white-space:nowrap}
.stage .t{font-weight:800;font-size:9pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.paramwrap{background:#fff;border:1px solid var(--line);border-radius:11px;padding:6px 14px;margin:10px 0}
.prompt code{font-size:9pt}
/* ---- фото-кадр ---- */
.frame{position:relative;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#0d0a07;line-height:0}
.frame.good{border:2px solid var(--o);box-shadow:0 16px 40px -18px rgba(218,95,30,.55)}
.frame img{width:100%;height:100%;object-fit:cover;display:block}
.frame .ov{position:absolute;inset:0;line-height:normal}
/* ---- сплит сток/commercial ---- */
.shots{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0}
.shots .frame{aspect-ratio:16/11}
.shots .cap{margin-top:8px;font-size:9.2pt;line-height:1.35;color:var(--body)}
.shots .cap b{color:var(--ink);font-weight:800}
/* ---- 5 опор / референс-борд ---- */
.cells{display:grid;grid-template-columns:repeat(5,1fr);gap:9px;margin:13px 0}
.cells .c .lb{font-weight:800;font-size:8pt;letter-spacing:.03em;color:var(--o);text-transform:uppercase;margin-bottom:5px}
.cells .c .lb i{display:block;font-style:normal;font-weight:700;font-size:9.5pt;color:var(--ink);text-transform:none;margin-top:1px}
.cells .frame{aspect-ratio:3/4}
.cells .cp{margin-top:6px;font-size:8pt;line-height:1.3;color:var(--body)}
.refcard .tag{position:absolute;left:8px;top:8px;background:rgba(10,8,6,.82);color:#ffd9b8;font-weight:800;font-size:8pt;letter-spacing:.04em;padding:3px 8px;border-radius:6px}
/* ---- master с локами ---- */
.masterwrap{display:grid;grid-template-columns:1.55fr 1fr;gap:16px;align-items:center;margin:12px 0}
.masterwrap .frame{aspect-ratio:16/11}
.locks{display:flex;flex-direction:column;gap:8px}
.locks .l{background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 12px}
.locks .l b{display:block;font-weight:800;font-size:9.5pt;color:var(--ink);letter-spacing:.02em}
.locks .l span{font-size:8.6pt;line-height:1.3;color:var(--body)}
.locks .l b i{font-style:normal;color:var(--o);margin-right:6px}
/* ---- overlay-чипы (@ref, метки движения) ---- */
.chips{position:absolute;left:12px;top:12px;display:flex;flex-direction:column;gap:6px}
.chip{background:rgba(10,8,6,.72);border:1px solid rgba(255,150,80,.35);color:#ffe4c8;font-weight:800;
 font-size:8.5pt;letter-spacing:.03em;padding:4px 9px;border-radius:7px;backdrop-filter:blur(2px)}
.chip i{font-style:normal;color:var(--o2);margin-right:5px}
.mk{position:absolute;color:#ffe4c8;font-weight:800;font-size:8pt;letter-spacing:.05em;text-shadow:0 1px 4px #000}
/* ---- before/after ---- */
.ba{display:grid;grid-template-columns:1fr 34px 1fr;gap:8px;align-items:center;margin:13px 0}
.ba .frame{aspect-ratio:4/3}
.ba .arw{font-size:20pt;color:var(--o);text-align:center;font-weight:800}
.ba .cap{margin-top:7px;font-size:9pt;line-height:1.3}
.ba .cap b{font-weight:800}
.ba .bad b{color:#b64a37}.ba .good b{color:#2f8f57}
.ba .cap span{color:var(--body)}
/* ---- deliverables ---- */
.dgrid{display:flex;flex-direction:column;gap:9px;margin:11px 0}
.drow{display:grid;grid-template-columns:88px 1fr;gap:11px;align-items:center}
.drow .h{font-weight:800;font-size:9pt;color:var(--ink);line-height:1.15}
.drow .h span{display:block;font-weight:700;font-size:7.5pt;color:var(--o);text-transform:uppercase;letter-spacing:.03em;margin-top:2px}
.thumbs{display:flex;gap:6px;height:82px}
.thumbs.big{height:132px}
.thumbs .frame{height:100%;flex:none;aspect-ratio:9/12;border-radius:9px}
.thumbs .frame.wide{aspect-ratio:16/9}
.thumbs .sb{height:100%;flex:none;aspect-ratio:9/12;border:1px solid var(--line);border-radius:9px;background:#fff;display:flex;align-items:center;justify-content:center}
.play{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.play b{width:24px;height:24px;border-radius:50%;background:rgba(255,255,255,.9);color:#160e07;display:flex;align-items:center;justify-content:center;font-size:10pt}
/* ---- лестница ценности ---- */
.lad{display:flex;flex-direction:column;gap:7px;margin:10px 0}
.lad .l{display:grid;grid-template-columns:132px 1fr 150px;gap:14px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:10px;padding:11px 14px}
.lad .l .nm{font-weight:800;font-size:10.5pt;color:var(--ink);line-height:1.15}
.lad .l .track{height:12px;border-radius:6px;background:#f1e9db;overflow:hidden}
.lad .l .track i{display:block;height:100%;border-radius:6px;background:linear-gradient(90deg,var(--o),var(--o2))}
.lad .l:nth-child(1) .track i{width:25%;opacity:.5}.lad .l:nth-child(2) .track i{width:50%;opacity:.72}
.lad .l:nth-child(3) .track i{width:75%;opacity:.88}.lad .l:nth-child(4) .track i{width:100%}
.lad .l .ds{font-size:9pt;color:var(--body);text-align:right;line-height:1.35}
"""
CSS = V2CSS + EXTRA

def b64(name):
    return base64.b64encode((ASSET / name).read_bytes()).decode()

def frame(name, good=False, cls="", pos="center", overlay="", style=""):
    c = "frame good" if good else "frame"
    if cls: c += " " + cls
    st = f' style="{style}"' if style else ""
    return (f'<div class="{c}"{st}><img src="data:image/jpeg;base64,{b64(name)}" '
            f'style="object-position:{pos}">{overlay}</div>')

def shot_cell(name, cap, good=False):
    return f'<div>{frame(name, good=good)}<div class="cap">{cap}</div></div>'

def waveform(w=210, h=54, n=52, seed=3, color="#ff9a4d"):
    bars = []
    for i in range(n):
        v = abs(math.sin(i * 1.7 + seed) * 0.6 + math.sin(i * 0.47 + 1) * 0.4)
        bh = 5 + v * (h - 9)
        x = 4 + i * ((w - 8) / n)
        bars.append(f'<rect x="{x:.1f}" y="{(h-bh)/2:.1f}" width="2.2" height="{bh:.1f}" rx="1.1" fill="{color}"/>')
    return f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none" style="width:100%;height:100%">{"".join(bars)}</svg>'

def wavecard():
    return (f'<div class="frame refcard" style="background:#0d0a07;display:flex;align-items:center;padding:0 8px">'
            f'{waveform()}<span class="tag">@ref5</span></div>')

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · production pack · дорогая AI-реклама</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>По-русски:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def stage(b, t):
    return f'<div class="stage"><span class="b">{b}</span><span class="t">{t}</span></div>'

def biz(txt, lbl="Бизнес"):
    return f'<div class="biz"><b>{lbl}</b>{txt}</div>'

P = []

# ---------- P1 · Обложка ----------
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:absolute;inset:0;opacity:.5;background-image:url(data:image/jpeg;base64,{b64('commercial.jpg')});background-size:cover;background-position:center;mask-image:linear-gradient(0deg,#000,transparent 62%);-webkit-mask-image:linear-gradient(0deg,#000,transparent 62%)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · production pack · набор промптов</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.06;letter-spacing:-.02em;color:#fff;max-width:17ch">Одна нейросеть — два ценника. Как собрать рекламу, которую <span style="color:var(--o2)">купит бренд.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#e2d8c9;max-width:44ch">Разница не в модели, а в режиссуре. Сквозной кейс — премиум-кроссовки: бриф, референс-борд и готовые промпты на весь конвейер.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Бриф</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Референсы</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Промпты</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Сборка</span>
    </div>
  </div>
</section>""")

# ---------- P2 · Что внутри + карта конвейера ----------
P.append(page("Что внутри", 2, """
  <span class="kick">Пак под ролик «Одна нейросеть. Два ценника.»</span>
  <h2>Не генерация, а собранная реклама</h2>
  <p class="lead">Бренд платит не за «умею нейросеть». Он платит за кадр, который не стыдно поставить рядом с логотипом. Этот пак — как его получить: один режиссёрский бриф проходит через весь конвейер моделей.</p>
  <div class="flow">
    <div class="node"><b>Master</b><span>Nano Banana Pro</span></div><div class="arr">→</div>
    <div class="node"><b>Сцена</b><span>Seedance 2.5</span></div><div class="arr">→</div>
    <div class="node"><b>Правка</b><span>Gemini Omni</span></div><div class="arr">→</div>
    <div class="node"><b>Звук</b><span>Veo 3.1</span></div><div class="arr">→</div>
    <div class="node"><b>Сборка</b><span>Higgsfield</span></div>
  </div>
  <div class="term"><b>Сток-кадр</b> — <span>ровный свет, объект по центру, ноль истории. Модель получила «сделай красиво» и выдала среднее. Такой кадр тонет в ленте.</span></div>
  <div class="term"><b>Commercial-кадр</b> — <span>свет, камера, действие и звук заданы, а не случайны. Та же нейросеть, но у неё есть режиссёр. Такой кадр бренд покупает.</span></div>
  <div class="callout result"><div class="h">Что на выходе</div><p>Готовый режиссёрский бриф, референс-борд на 5 карточек и промпты на каждый этап — переносишь на свой продукт и собираешь ролик, который продаёт кампанию, а не генерацию.</p></div>
"""))

# ---------- P3 · Сток против commercial (ФОТО) ----------
P.append(page("Диагноз", 3,
  '<span class="kick">Главная ошибка брифа</span>'
  '<h2>Один продукт. Два кадра.</h2>'
  '<p class="lead">Слева и справа — один и тот же кроссовок и одна нейросеть. Разница только в задании: сток модель угадывает, commercial — исполняет по режиссуре.</p>'
  '<div class="shots">'
  + shot_cell("stock.jpg", "<b>AI-сток.</b> Ровный свет, объект по центру, нет истории.")
  + shot_cell("commercial.jpg", "<b>Commercial.</b> Свет, камера, действие, атмосфера.", good=True)
  + '</div>'
  '<div class="gb">'
  '<div class="box bad"><div class="lbl">✕ Сток-промпт</div>«Сделай дорогую рекламу белых кроссовок. Кинематографично. Премиально. Как Nike.» — модель угадывает. Свет плоский, камера случайная, истории нет.</div>'
  '<div class="box good"><div class="lbl">✓ Режиссёрский промпт</div>Заданы свет, ракурс, действие, среда и звук. Модель не угадывает — исполняет. Кадр читается как реклама.</div>'
  '</div>'
))

# ---------- P4 · Режиссёрский бриф — 5 опор (ФОТО) ----------
def cell(lb, sub, img_or_wave, cp, is_wave=False):
    inner = (f'<div class="frame" style="aspect-ratio:3/4;background:#0d0a07;display:flex;align-items:center;padding:0 4px">{waveform(h=44)}</div>'
             if is_wave else frame(img_or_wave))
    return f'<div class="c"><div class="lb">{lb}<i>{sub}</i></div>{inner}<div class="cp">{cp}</div></div>'
P.append(page("Режиссёрский бриф", 4,
  '<span class="kick">Шаблон · заполняешь под свой продукт</span>'
  '<h2>Пять опор одного кадра</h2>'
  '<p class="lead">До первой генерации реши пять вещей. Дальше все модели работают на общий замысел, а не вразнобой. Это и есть бриф — визуально.</p>'
  '<div class="cells">'
  + cell("1", "Продукт", "ref-product.jpg", "геометрия, лого, материал")
  + cell("2", "Свет", "ref-light.jpg", "тёмная студия, тёплый rim")
  + cell("3", "Камера", "ref-camera.jpg", "низкий наезд, плавное движение")
  + cell("4", "Среда", "ref-env.jpg", "мокрый бетон, отражение")
  + cell("5", "Звук", None, "натяжение шнурков, шаг", is_wave=True)
  + '</div>'
  '<div class="callout check"><div class="h">Проверь бриф</div>'
  '<div class="row">Все пять опор заданы конкретикой, а не эпитетами («дорого», «премиально»)</div>'
  '<div class="row">Продукт описан так, что модель не тронет геометрию и лого</div>'
  '<div class="row">Один язык света и одна логика камеры на весь ролик</div>'
  '</div>'
))

# ---------- P5 · Референс-борд (ФОТО @ref) ----------
def refcard(tag, name, img):
    ov = '<span class="tag">' + tag + '</span>'
    return f'<div class="c"><div class="lb">{tag}<i>{name}</i></div>{frame(img, cls="refcard", overlay=ov)}</div>'
P.append(page("Референс-борд", 5,
  '<span class="kick">До 50 референсов · собираем 5 ключевых</span>'
  '<h2>Дорогой кадр — это референсы</h2>'
  '<p class="lead">Seedance 2.5 берёт до 50 референсов. Тебе хватит пяти — каждый закрывает одну опору брифа. В промпте они адресуются как <b>@ref1…@ref5</b>: модель знает, откуда брать что.</p>'
  '<div class="cells">'
  + refcard("@ref1", "продукт", "ref-product.jpg")
  + refcard("@ref2", "свет", "ref-light.jpg")
  + refcard("@ref3", "камера", "ref-camera.jpg")
  + refcard("@ref4", "среда", "ref-env.jpg")
  + f'<div class="c"><div class="lb">@ref5<i>ритм/звук</i></div>{wavecard()}</div>'
  + '</div>'
  + biz("Референсы — не «вдохновение», а инструкция. Один референс = одно решение. Смешаешь пять идей в одном кадре — модель усреднит и вернёт сток.", "Приём")
))

# ---------- P6 · Nano Banana Pro · master (ФОТО + локи) ----------
P.append(page("Этап 1 · Master · Nano Banana Pro", 6,
  stage("Этап 1", "Master-кадр · product lock") +
  "<h2>Nano Banana Pro — эталон продукта</h2>"
  "<p class=\"lead\">Первый кадр — не реклама, а <b>референс правды о продукте</b>: точная геометрия, лого, подошва. Он станет @ref1 для сцены.</p>"
  '<div class="masterwrap">'
  + frame("master.jpg")
  + '<div class="locks">'
    '<div class="l"><b><i>◆</i>LOGO LOCK</b><span>лого держится 1:1, без искажений</span></div>'
    '<div class="l"><b><i>◆</i>GEOMETRY</b><span>силуэт и пропорции — точные</span></div>'
    '<div class="l"><b><i>◆</i>MATERIAL</b><span>текстура кожи читается</span></div>'
    '<div class="l"><b><i>◆</i>SOLE</b><span>подошва и протектор без изменений</span></div>'
  '</div></div>'
  + prompt("Готовый промпт · Nano Banana Pro",
    "A single white premium sneaker, clean 3/4 hero angle, seamless warm-neutral "
    "studio backdrop, soft even key light, razor-sharp logo, stitching and sole "
    "tread, exact geometry, photoreal 1:1 product master. Lock the silhouette.",
    "чистый master-кадр: точная геометрия, лого, подошва, ровный свет, 1:1. Это референс продукта (@ref1), не финальная реклама.")
))

# ---------- P7 · Seedance 2.5 · сцена (ФОТО + @ref чипы) ----------
com_overlay = ('<div class="ov"><div class="chips">'
  '<span class="chip"><i>@ref1</i>PRODUCT</span>'
  '<span class="chip"><i>@ref2</i>LIGHT</span>'
  '<span class="chip"><i>@ref3</i>CAMERA</span>'
  '<span class="chip"><i>@ref4</i>ENVIRONMENT</span>'
  '</div></div>')
P.append(page("Этап 2 · Сцена · Seedance 2.5", 7,
  stage("Этап 2", "Сцена · кинокадр из референсов") +
  "<h2>Seedance 2.5 — режиссура в промпте</h2>"
  "<p class=\"lead\">Master-кадр и референсы света, камеры и среды собираются в одну сцену. Каждый @ref несёт своё решение — модель исполняет бриф.</p>"
  + frame("commercial.jpg", good=True, overlay=com_overlay, style="aspect-ratio:16/9;margin:12px 0")
  + prompt("Готовый промпт · Seedance 2.5",
    "@ref1 product — keep geometry, sole, logo, white 1:1.\n"
    "@ref2 lighting: dark studio, narrow warm rim, deep blacks.\n"
    "Extreme low-angle macro on wet concrete; laces slowly self-tighten;\n"
    "controlled lateral dolly; rim light travels the material; hard cut\n"
    "to a first step, asphalt ripples. Native SFX: lace tension, wet step.",
    "продукт из @ref1 неизменен; свет из @ref2; низкий макро на мокром бетоне, шнурки затягиваются, боковой dolly, rim скользит по материалу, склейка на первый шаг, нативный звук.")
))

# ---------- P8 · Gemini Omni · before/after (ФОТО) ----------
P.append(page("Этап 3 · Правка · Gemini Omni Flash", 8,
  stage("Этап 3", "Правка · разговором, не заново") +
  "<h2>Gemini Omni Flash — режиссёрская правка</h2>"
  "<p class=\"lead\">Кадр почти готов, но света много и нет напряжения. Не перегенерируй — правь адресно. Разница видна без чтения:</p>"
  '<div class="ba">'
  f'<div><div class="bad">{frame("before.jpg")}</div><div class="cap bad"><b>BEFORE.</b> <span>слишком светло, плоско, нет глубины</span></div></div>'
  '<div class="arw">→</div>'
  f'<div><div class="good">{frame("after.jpg", good=True)}</div><div class="cap good"><b>AFTER.</b> <span>глубже тени, контраст, атмосфера</span></div></div>'
  '</div>'
  + prompt("Готовый промпт · conversational edit",
    "Keep the shoe, framing and camera path unchanged.\n"
    "Change only: reduce fill light 30%; deepen wet-asphalt reflections;\n"
    "add subtle mist; delay the hero light to the last second.\n"
    "Do not alter shoe geometry, logo, camera path or duration.",
    "оставь кроссовок, кадрирование и траекторию; поменяй только: заполняющий свет −30%, глубже отражения, лёгкая дымка, геройский свет — на последнюю секунду. Геометрию и лого не менять.")
))

# ---------- P9 · Veo 3.1 · hero + движение (ФОТО + overlay) ----------
hero_ov = ('<div class="ov">'
  '<span class="mk" style="left:12px;top:12px">КАМЕРА · low push-in</span>'
  '<span class="mk" style="right:12px;top:12px">HARD CUT</span>'
  '<svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%">'
  '<path d="M8 60 C30 40 60 34 88 30" stroke="#ffb877" stroke-width="0.7" fill="none" stroke-dasharray="2 1.5"/>'
  '<path d="M88 30 l-4 -0.5 M88 30 l-2.5 3" stroke="#ffb877" stroke-width="0.7" fill="none"/>'
  '<line x1="90" y1="14" x2="90" y2="86" stroke="#ffb877" stroke-width="0.5" stroke-dasharray="1.5 1.5"/>'
  '</svg>'
  '<div style="position:absolute;left:12px;right:12px;bottom:9px;height:26px">' + waveform(h=26) + '</div>'
  '<span class="mk" style="left:12px;bottom:38px;font-size:6.5pt">START</span>'
  '<span class="mk" style="left:38%;bottom:38px;font-size:6.5pt">LACE TENSION</span>'
  '<span class="mk" style="left:64%;bottom:38px;font-size:6.5pt">WET STEP</span>'
  '</div>')
P.append(page("Этап 4 · Звук и камера · Veo 3.1 · Runway", 9,
  stage("Этап 4", "Звук и камера · достраиваем премиум") +
  "<h2>Veo 3.1 — нативный звук в кадре</h2>"
  "<p class=\"lead\">Дорогое ощущение во многом держится на звуке. Veo 3.1 генерирует аудио прямо со сценой: SFX задаёшь в промпте. Runway Gen-4.5 берёт точную хореографию камеры.</p>"
  + frame("commercial.jpg", good=True, overlay=hero_ov, style="aspect-ratio:16/9;margin:12px 0")
  + prompt("Готовый промпт · Veo 3.1 (image-to-video)",
    "[from the hero frame] Cinematic 15s. Native audio: low sub-bass swell, one\n"
    "lace-tension creak, a wet-asphalt footstep on the hard cut. Camera: slow low\n"
    "push-in, then hard cut to the first step. Keep product unchanged. 4K.",
    "из геройского кадра, 15 сек, нативный звук (саб-бас, скрип шнурка, шаг по асфальту на склейке); камера — медленный низкий наезд, затем жёсткая склейка; продукт не менять.")
))

# ---------- P10 · Карта моделей ----------
P.append(page("Карта моделей · сборка", 10, """
  <span class="kick">Что чем делать</span>
  <h2>Каждому этапу — свой инструмент</h2>
  <p class="lead">Ошибка — тянуть весь ролик в одну модель. Конвейер сильнее: каждая закрывает то, в чём она лучшая, а Higgsfield собирает результат.</p>
  <table>
    <tr><th>Этап</th><th>Модель</th><th>Зачем именно она</th></tr>
    <tr><td><b>Master продукта</b></td><td>Nano Banana Pro</td><td>точная геометрия, лого и текст без искажений, до 4K</td></tr>
    <tr><td><b>Сцена</b></td><td>Seedance 2.5</td><td>до 50 референсов, кинокадр и звук из одного промпта</td></tr>
    <tr><td><b>Правка</b></td><td>Gemini Omni Flash</td><td>адресный edit разговором, без потери кадра</td></tr>
    <tr><td><b>Звук</b></td><td>Veo 3.1</td><td>нативное аудио image-to-video, 4K</td></tr>
    <tr><td><b>Камера</b></td><td>Runway Gen-4.5</td><td>точная хореография движения в промпте</td></tr>
    <tr><td><b>Сборка</b></td><td>Higgsfield</td><td>пресеты движения и финальная склейка</td></tr>
  </table>
  <p class="note">Модели и их возможности сверены на 11.08.2026. Названия и лимиты меняются — держись логики этапов (что фиксируем, что двигаем, чем правим), а не конкретных кнопок.</p>
"""))

# ---------- P11 · Deliverables (ФОТО-thumbnails) ----------
def thumbs(imgs, good_last=False, wide=False):
    out = []
    for i, im in enumerate(imgs):
        g = good_last and i == len(imgs) - 1
        out.append(frame(im, good=g, cls="wide" if wide else ""))
    return '<div class="thumbs">' + "".join(out) + '</div>'
PLAY = '<div class="play"><b>&#9654;</b></div>'
sb = '<div class="sb"><svg viewBox="0 0 40 54" style="width:70%"><rect x="4" y="6" width="32" height="20" rx="2" fill="none" stroke="#c9bda9" stroke-width="1.4"/><path d="M8 22 l7 -8 4 5 5 -6 6 9" fill="none" stroke="#c9bda9" stroke-width="1.4"/><rect x="4" y="32" width="32" height="4" rx="2" fill="#e6dccb"/><rect x="4" y="40" width="22" height="4" rx="2" fill="#e6dccb"/></svg></div>'
P.append(page("Что продаёшь бренду", 11,
  '<span class="kick">Deliverables · один ролик разным моделям</span>'
  '<h2>Клиент покупает не генерацию</h2>'
  '<p class="lead">Из одной собранной сцены нарезается пакет под всю кампанию — это и превращает «умею нейросеть» в услугу.</p>'
  '<div class="dgrid">'
  f'<div class="drow"><div class="h">Hero Film<span>9:16</span></div><div class="thumbs big">{frame("commercial.jpg", good=True, cls="wide", overlay=PLAY)}</div></div>'
  f'<div class="drow"><div class="h">Cutdowns<span>3× · 6 сек</span></div>{thumbs(["commercial.jpg","commercial.jpg","commercial.jpg"])}</div>'
  f'<div class="drow"><div class="h">Hooks<span>5× · первые сек</span></div>{thumbs(["commercial.jpg","after.jpg","commercial.jpg","after.jpg","commercial.jpg"])}</div>'
  f'<div class="drow"><div class="h">Frames<span>4× продукт</span></div>{thumbs(["master.jpg","stock.jpg","master.jpg","stock.jpg"])}</div>'
  f'<div class="drow"><div class="h">Storyboard<span>раскадровка</span></div><div class="thumbs">{sb}{sb}{sb}</div></div>'
  f'<div class="drow"><div class="h">Sound<span>звук.режиссура</span></div><div class="thumbs"><div class="frame wide" style="aspect-ratio:16/9;background:#0d0a07;display:flex;align-items:center;padding:0 10px">{waveform(h=40)}</div></div></div>'
  '</div>'
))

# ---------- P12 · Чек-лист bad/good (ФОТО) ----------
P.append(page("Чек-лист · честность", 12,
  '<span class="kick">Контроль перед сдачей</span>'
  '<h2>Сток или commercial — проверь кадр</h2>'
  '<div class="shots" style="margin-top:12px">'
  f'<div>{frame("stock.jpg")}<div class="cap"><b>BAD · AI-сток.</b> Ровный свет, по центру, нет действия и звука — теряется в ленте.</div></div>'
  f'<div>{frame("commercial.jpg", good=True)}<div class="cap"><b>GOOD · commercial.</b> Характерный свет, среда, движение, звук — брендовый кадр.</div></div>'
  '</div>'
  '<div class="callout check"><div class="h">Чек-лист режиссуры</div>'
  '<div class="row">Свет задан (rim, глубокие чёрные), а не ровная заливка</div>'
  '<div class="row">Камера — одно осмысленное движение; в кадре есть действие-событие</div>'
  '<div class="row">Продукт неизменен: геометрия, лого, подошва, цвет</div>'
  '<div class="row">Звук нативный, задан в промпте; формат 9:16, нарезаны Hook и Cutdown</div>'
  '</div>'
  '<p class="note">Честно: кадры кроссовка — концепт-дизайн под кейс, не «результат клиента». Никаких выдуманных цифр и цен.</p>'
))

# ---------- P13 · CTA ----------
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center;padding:0">
  <div style="position:absolute;inset:0;opacity:.38;background-image:url(data:image/jpeg;base64,{b64('commercial.jpg')});background-size:cover;background-position:center;mask-image:radial-gradient(70% 60% at 50% 45%,#000,transparent 78%);-webkit-mask-image:radial-gradient(70% 60% at 50% 45%,#000,transparent 78%)"></div>
  <div style="position:relative;z-index:2;padding:0 26mm">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Собери commercial,<br>не стыдно <span style="color:var(--o2)">бренду.</span></h2>
  <p style="color:#cabfae;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Весь пак: режиссёрский бриф, референс-борд, готовые промпты (Nano Banana Pro · Seedance 2.5 · Gemini Omni · Veo 3.1 · Runway), карта моделей и чек-лист bad→good.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Забрать пак → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Реклама под бренд → бриф @alovlab</span>
  </div>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>PRODUCTION PACK · дорогая AI-реклама · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
