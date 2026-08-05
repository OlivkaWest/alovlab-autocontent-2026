# -*- coding: utf-8 -*-
"""
AlovLab · рендер премиальной карусели (6 слайдов) в фирменный HTML.
Структура одним постом: обложка → провокация → связка → неделя → пик → CTA.

Запуск:
  python3 scripts/carousel_render.py restaurant       # рендер по конфигу бизнеса
Затем:
  node scripts/carousel_shoot.js exports/carousels/restaurant/restaurant.html \
       exports/carousels/restaurant                    # экспорт slide-01..06.png (1080x1350)

Новый бизнес = новый словарь в CONFIGS (не повторяем нишу от карусели к карусели).
Фото-слоты: config["photos"] = {"cover_rich": "<путь.png>", "pik": "<путь.png>"} —
если файл существует, он вшивается как кадр; иначе рисуется дизайн-графика.
Правило проекта: на карусели НЕ пишем футер «Автоконтент 2026 / t.me/AlovLab».
Кадры — концепт-дизайн, не «результат клиента». Цена студии не называется.
"""
import base64, pathlib, sys, json

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")

RANGES = {"cyrillic":"U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin":"U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192"}
faces=""
for w in (400,500,700,800):
    for sub in ("cyrillic","latin"):
        faces+=("@font-face{font-family:'Manrope';font-weight:%d;font-display:swap;"
                "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}\n"
                % (w, b64(FONTS/f'manrope-{sub}-{w}.woff2'), RANGES[sub]))

GRAIN = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E"
         "%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E"
         "%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.55'/%3E%3C/svg%3E\")")

MARK = f'<span class="mark"><img class="mki" src="data:image/png;base64,{LOGO}" alt=""><span class="mw">Alov<b>Lab</b></span></span>'
def snum(n): return f'<span class="snum">0{n}<b> / 06</b></span>'

def plate():
    return ("""<svg class="plate" viewBox="0 0 140 150" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g stroke="#ffd3a4" stroke-width="2.4" fill="none" stroke-linecap="round">
    <path d="M56 66C50 56 62 50 56 40C50 31 60 25 56 15" opacity=".8"/>
    <path d="M70 64C64 53 76 47 70 36C64 27 74 21 70 11" opacity=".95"/>
    <path d="M84 66C78 56 90 50 84 40C78 31 88 25 84 15" opacity=".7"/>
  </g>
  <path d="M48 96C52 80 88 80 92 96" stroke="#ffb877" stroke-width="2.4" fill="none"/>
  <ellipse cx="70" cy="100" rx="50" ry="13" stroke="#ffe2c4" stroke-width="2.6"/>
  <ellipse cx="70" cy="97" rx="34" ry="8" stroke="#e8862f" stroke-width="2"/>
</svg>""")

def plate_cheap():
    return ("""<svg class="plate" viewBox="0 0 140 150" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="70" cy="94" rx="42" ry="10" stroke="#8b9199" stroke-width="2"/>
  <ellipse cx="70" cy="92" rx="27" ry="6" stroke="#6c7178" stroke-width="1.6"/>
  <path d="M56 91h28" stroke="#6c7178" stroke-width="2" stroke-linecap="round"/>
</svg>""")

PLAY = '<span class="play"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span>'
CAP = '<span class="reel-cap"><i></i><b></b></span>'

def reel(kind="premium", plate_art=False, extra="", plate_fn=None, photo=None):
    if photo and pathlib.Path(photo).exists():
        style = f' style="background-image:url(data:image/png;base64,{b64(photo)})"'
        return f'<span class="reel reel--photo {extra}"{style}>{PLAY}{CAP}</span>'
    inner = (plate_fn or plate)() if plate_art else ""
    return f'<span class="reel reel--{kind} {extra}">{inner}{PLAY}{CAP}</span>'

CSS_TMPL = r"""
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#0c0a07;--card:#131009;--tag:#221a11;--o:#e8672a;--o2:#ff7a33;
--text:#f7f2e9;--muted:#a99e8c;--dim:#7a6f5e;--line:rgba(247,242,233,.10);--gold:#d59a4e;}
html{background:#0d0b08}
body{font-family:'Manrope',system-ui,sans-serif;background:#0d0b08;color:var(--text);
-webkit-font-smoothing:antialiased;padding:clamp(18px,3.5vw,44px) clamp(12px,3vw,30px)}
.page{max-width:1000px;margin:0 auto}
.lead{margin-bottom:24px}
.lead .eb{font-weight:800;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--o2)}
.lead h1{font-weight:800;font-size:clamp(19px,3.2vw,26px);letter-spacing:-.015em;margin:9px 0 0;line-height:1.3}
.lead h1 b{color:var(--o2)}
.grid{display:flex;flex-wrap:wrap;gap:22px;justify-content:center}

.slide{position:relative;width:min(540px,92vw);aspect-ratio:4/5;border-radius:22px;overflow:hidden;
background:var(--card);border:1px solid var(--line);padding:26px 24px;display:flex;flex-direction:column;
box-shadow:0 22px 46px -26px rgba(0,0,0,.85)}
.slide--warm{background:radial-gradient(120% 82% at 82% 12%,#2a2013 0%,#161009 46%,var(--ink) 100%)}

.mark{display:inline-flex;align-items:center;gap:8px;position:relative;z-index:3}
.mark .mki{width:26px;height:26px;border-radius:7px;flex:0 0 auto;display:block}
.mark .mw{font-weight:800;font-size:14px;color:#fff;letter-spacing:.005em}
.mark .mw b{color:var(--o2);font-weight:800}
.snum{position:absolute;top:26px;right:24px;font-weight:800;font-size:12px;color:var(--dim);letter-spacing:.06em;z-index:3;font-variant-numeric:tabular-nums}
.snum b{color:var(--o2)}
.eyebrow{font-weight:800;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-top:15px}
.eyebrow b{color:var(--o2)}
.h{font-weight:800;letter-spacing:-.028em;color:#fff;line-height:1.04}
.a{color:var(--o2)}
.sub{font-size:13.5px;line-height:1.5;color:var(--muted);max-width:32ch}

.reel{position:relative;aspect-ratio:9/16;border-radius:13px;overflow:hidden;flex:0 0 auto;
background:linear-gradient(158deg,#3c2614 0%,#1d1108 54%,#0c0805 100%);
border:1px solid rgba(255,180,120,.16);box-shadow:0 16px 30px -16px #000, inset 0 0 50px rgba(0,0,0,.45)}
.reel::before{content:"";position:absolute;inset:0;background:radial-gradient(85% 55% at 68% 20%, rgba(255,150,70,.30), transparent 62%);z-index:1}
.reel::after{content:"";position:absolute;inset:0;z-index:2;background:__GRAIN__;opacity:.06;mix-blend-mode:overlay}
.reel--photo{background-size:cover;background-position:center}
.reel--photo::before{background:linear-gradient(transparent 40%,rgba(0,0,0,.35))}
.reel--dull{background:linear-gradient(158deg,#2c2c2f,#1b1b1d 58%,#141416);border-color:rgba(255,255,255,.06);filter:saturate(.5)}
.reel--dull::before{background:radial-gradient(80% 50% at 50% 40%, rgba(255,255,255,.05), transparent 60%)}
.reel--rich{background:linear-gradient(155deg,#4c2d15 0%,#20130a 52%,#0b0704 100%)}
.reel--rich::before{background:radial-gradient(82% 58% at 62% 26%,rgba(255,165,85,.5),transparent 60%)}
.reel--cheap{background:linear-gradient(160deg,#26282c,#191a1d 60%,#131315);border-color:rgba(255,255,255,.05);filter:saturate(.35) brightness(.92)}
.reel--cheap::before{background:radial-gradient(70% 45% at 50% 46%,rgba(205,214,224,.06),transparent 60%)}
.reel--cheap .play{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.12)}
.reel--cheap .reel-cap i{background:rgba(255,255,255,.3)}
.vignette::after{box-shadow:inset 0 0 70px 10px rgba(0,0,0,.6)}
.play{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);z-index:4;width:38px;height:38px;border-radius:50%;
background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);display:grid;place-items:center}
.play svg{width:16px;height:16px;fill:#fff;margin-left:2px}
.reel-cap{position:absolute;left:9px;right:9px;bottom:9px;z-index:4;display:flex;align-items:center;gap:6px}
.reel-cap i{width:5px;height:5px;border-radius:50%;background:var(--o2);flex:0 0 auto}
.reel-cap b{height:5px;border-radius:3px;background:rgba(255,255,255,.4);flex:1}
.plate{position:absolute;left:50%;top:47%;transform:translate(-50%,-50%);z-index:3;width:58%;height:auto;opacity:.92}
.cover-viz .cvi:nth-child(2){transform:translateY(-20px)}
.cover-viz .cvi:nth-child(2) .reel{box-shadow:0 26px 46px -18px rgba(0,0,0,.85),0 0 48px -12px rgba(232,103,42,.5)}

.slide--cover .h{font-size:40px;margin-top:18px}
.cover-viz{margin-top:auto;display:grid;grid-template-columns:1fr 1fr;gap:14px;align-items:end}
.cvi{display:flex;flex-direction:column;gap:8px}
.cvi .reel{width:100%}
.cvi-lab{font-weight:800;font-size:12px;letter-spacing:.04em;text-align:center}
.cvi-lab.bad{color:var(--dim)} .cvi-lab.good{color:var(--o2)}

.slide--prov .mid{margin-top:14px}
.slide--prov .h{font-size:31px}
.slide--prov .sub{margin-top:9px}
.prov-viz{margin-top:auto;display:flex;justify-content:center;gap:12px}
.prov-viz .reel{width:31%}
.prov-viz .reel:nth-child(2){width:37%;align-self:flex-start}

.body-mid{flex:1;display:flex;flex-direction:column;gap:12px;margin-top:12px}
.h--md{font-size:27px}
.stack{flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:12px}
.icard{background:#1b150d;border:1px solid var(--line);border-radius:12px;padding:12px 13px;display:grid;grid-template-columns:1fr 34px;gap:11px;align-items:center}
.ic-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}
.tag{font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:var(--o2);background:rgba(232,103,42,.14);border:1px solid rgba(232,103,42,.3);border-radius:6px;padding:3px 7px}
.en{font-weight:700;font-size:8px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim)}
.ic-h{font-weight:800;font-size:14px;line-height:1.2;color:#fff}
.ic-sub{font-size:11px;line-height:1.35;color:var(--muted);margin-top:4px}
.icard .reel{width:34px;border-radius:8px}
.icard .reel .play{width:16px;height:16px} .icard .reel .play svg{width:7px;height:7px}

.rows4{flex:1;display:flex;flex-direction:column;justify-content:space-between}
.r4{display:grid;grid-template-columns:70px 1fr;gap:11px;padding:9px 0;border-top:1px solid var(--line);align-items:start}
.r4:first-child{border-top:none}
.r4-lg{font-weight:800;font-size:11px;color:#fff} .r4-en{font-weight:700;font-size:8px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-top:2px}
.r4-h{font-weight:800;font-size:12.5px;line-height:1.2;color:#fff} .r4-sub{font-size:10.5px;line-height:1.3;color:var(--muted);margin-top:2px}
.week-strip{margin-top:12px;display:flex;align-items:center;gap:7px}
.week-strip .reel{width:38px;border-radius:7px}
.week-strip .reel .play{display:none} .week-strip .reel .reel-cap{display:none}
.week-badge{margin-left:auto;font-weight:800;font-size:10.5px;color:var(--o2);background:rgba(232,103,42,.12);border:1px solid rgba(232,103,42,.3);border-radius:999px;padding:5px 10px;white-space:nowrap}

.pik2{flex:1;display:flex;flex-direction:column;gap:12px;margin-top:12px}
.hero-frame{position:relative;flex:1;min-height:0;border-radius:16px;overflow:hidden;
background:linear-gradient(158deg,#4a2c15 0%,#1d1108 54%,#0c0805 100%);
border:1px solid rgba(255,180,120,.2);box-shadow:inset 0 0 80px rgba(0,0,0,.5)}
.hero-frame.reel--photo{background-size:cover;background-position:center}
.hero-frame::before{content:"";position:absolute;inset:0;z-index:1;background:radial-gradient(72% 55% at 60% 30%,rgba(255,160,80,.42),transparent 62%)}
.hero-frame.reel--photo::before{background:linear-gradient(transparent 30%,rgba(0,0,0,.5))}
.hero-frame::after{content:"";position:absolute;inset:0;z-index:2;background:__GRAIN__;opacity:.06;mix-blend-mode:overlay}
.hero-frame .play{position:absolute;left:50%;top:40%;transform:translate(-50%,-50%);z-index:4;width:58px;height:58px;border-radius:50%;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.32);display:grid;place-items:center}
.hero-frame .play svg{width:23px;height:23px;fill:#fff;margin-left:3px}
.hero-frame .plate{position:absolute;left:50%;top:40%;transform:translate(-50%,-50%);z-index:3;width:30%;opacity:.92}
.hero-cap{position:absolute;left:0;right:0;bottom:0;z-index:5;padding:16px;background:linear-gradient(transparent,rgba(9,6,3,.92))}
.hero-cap .hero-h{font-weight:800;font-size:15px;line-height:1.24;color:#fff;margin-top:8px}
.pik-note{font-size:11.5px;color:var(--dim);line-height:1.4}

.slide--cta{background:radial-gradient(120% 82% at 50% 18%,#2c2012,#150f08 52%,var(--ink))}
.cta-mid{flex:1;display:flex;flex-direction:column;justify-content:center;gap:14px;margin-top:8px}
.cta-logo{width:46px;height:46px}
.cta-h{font-weight:800;font-size:29px;line-height:1.08;color:#fff;letter-spacing:-.02em}
.cta-dirs{display:flex;flex-wrap:wrap;gap:6px}
.cta-dirs span{font-size:11px;font-weight:700;color:var(--muted);background:rgba(247,242,233,.05);border:1px solid var(--line);border-radius:7px;padding:5px 9px}
.cta-btn{align-self:flex-start;font-weight:800;font-size:14.5px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:11px;padding:12px 18px;box-shadow:0 12px 26px -12px rgba(232,103,42,.75)}
.cta-strip{display:flex;gap:8px;margin-top:2px} .cta-strip .reel{width:44px;border-radius:8px}
.cta-strip .reel .play{width:18px;height:18px} .cta-strip .reel .play svg{width:8px;height:8px}
.notes{margin-top:28px;padding-top:18px;border-top:1px solid var(--line);font-size:12.5px;color:var(--dim);line-height:1.7}
.notes b{color:var(--muted);font-weight:700}
"""

def render(cfg):
    ph = cfg.get("photos", {})
    def p(slot): return ph.get(slot)

    # 1 · cover
    rich = reel('rich', plate_art=True, extra='vignette', photo=p('cover_rich'))
    cheap = reel('cheap', plate_art=True, plate_fn=plate_cheap, photo=p('cover_cheap'))
    cl = cfg.get("cover_labels", ("как есть","как должно быть"))
    s1 = f"""    <article class="slide slide--cover slide--warm">
      {MARK}{snum(1)}
      <h2 class="h">{cfg['cover_h']}</h2>
      <div class="cover-viz">
        <div class="cvi">{cheap}<span class="cvi-lab bad">{cl[0]}</span></div>
        <div class="cvi">{rich}<span class="cvi-lab good">{cl[1]}</span></div>
      </div>
    </article>"""

    # 2 · provocation
    s2 = f"""    <article class="slide slide--prov slide--warm">
      {MARK}{snum(2)}
      <div class="mid">
        <div class="eyebrow"><b>{cfg.get('prov_eyebrow','Провокация')}</b></div>
        <h2 class="h">{cfg['prov_h']}</h2>
        <p class="sub">{cfg['prov_sub']}</p>
      </div>
      <div class="prov-viz">{reel('dull')}{reel('premium', plate_art=True, extra='vignette', photo=p('prov'))}{reel('dull')}</div>
    </article>"""

    # 3 · svyazka
    cards=""
    for i,(tag,en,h,sub) in enumerate(cfg['svyazka']):
        thumb = reel('premium', plate_art=(i==1), photo=p(f'svyazka_{i}'))
        cards+=(f'<div class="icard"><div><div class="ic-top"><span class="tag">{tag}</span><span class="en">{en}</span></div>'
                f'<div class="ic-h">{h}</div><div class="ic-sub">{sub}</div></div>{thumb}</div>')
    s3 = f"""    <article class="slide">
      {MARK}{snum(3)}
      <div class="eyebrow">{cfg.get('svyazka_eyebrow','Кейс')} · <b>Связка</b></div>
      <div class="body-mid">
        <h2 class="h h--md">Одна идея —<br><span class="a">целая кампания.</span></h2>
        <div class="stack">{cards}</div>
      </div>
    </article>"""

    # 4 · nedelya
    rows="".join(f'<div class="r4"><div><div class="r4-lg">{lg}</div><div class="r4-en">{en}</div></div>'
                 f'<div><div class="r4-h">{h}</div><div class="r4-sub">{sub}</div></div></div>' for lg,en,h,sub in cfg['nedelya'])
    strip="".join(reel('premium' if i in (1,3,5) else 'dull') for i in range(7))
    s4 = f"""    <article class="slide">
      {MARK}{snum(4)}
      <div class="eyebrow">{cfg.get('nedelya_eyebrow','Из одного вечера съёмки')}</div>
      <div class="body-mid">
        <h2 class="h h--md">Неделя контента —<br><span class="a">за вечер.</span></h2>
        <div class="rows4">{rows}</div>
        <div class="week-strip">{strip}<span class="week-badge">1 идея → 7 роликов</span></div>
      </div>
    </article>"""

    # 5 · pik
    pik_photo = p('pik')
    hero_cls = "hero-frame reel--photo" if (pik_photo and pathlib.Path(pik_photo).exists()) else "hero-frame"
    hero_style = f' style="background-image:url(data:image/png;base64,{b64(pik_photo)})"' if (pik_photo and pathlib.Path(pik_photo).exists()) else ""
    hero_inner = PLAY if hero_style else (plate()+PLAY)
    s5 = f"""    <article class="slide slide--warm">
      {MARK}{snum(5)}
      <div class="eyebrow">Пик · <b>Герой недели</b></div>
      <div class="pik2">
        <h2 class="h h--md">{cfg['pik_h']}</h2>
        <div class="{hero_cls}"{hero_style}>
          {hero_inner}
          <div class="hero-cap">
            <div class="ic-top"><span class="tag">Геройный ролик</span><span class="en">Hero Film</span></div>
            <div class="hero-h">{cfg['pik_cap']}</div>
          </div>
        </div>
        <p class="pik-note">{cfg['pik_note']}</p>
      </div>
    </article>"""

    # 6 · cta
    cta_h = cfg.get('cta_h', 'Собери такую систему<br>под <span class="a">свой бренд.</span>')
    cta_sub = cfg.get('cta_sub', 'AlovLab Studio: реклама и промо, аватары и дикторы, визуальный брендинг, автоматизация контента. Опиши задачу в брифе — вернёмся с решением за 24 часа.')
    s6 = f"""    <article class="slide slide--cta">
      {MARK}{snum(6)}
      <div class="cta-mid">
        <img class="cta-logo" src="data:image/png;base64,{LOGO}" alt="AlovLab">
        <h2 class="cta-h">{cta_h}</h2>
        <p class="sub">{cta_sub}</p>
        <div class="cta-strip">{reel('premium')}{reel('premium', plate_art=True)}{reel('premium')}{reel('dull')}</div>
        <div class="cta-dirs"><span>Реклама</span><span>Аватары</span><span>Брендинг</span><span>Автоматизация</span></div>
        <span class="cta-btn">Отправить бриф → @alovlab</span>
      </div>
    </article>"""

    css = faces + CSS_TMPL.replace("__GRAIN__", GRAIN)
    slides="\n".join([s1,s2,s3,s4,s5,s6])
    return f"""<title>Карусель · {cfg['label']} · AlovLab</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{css}</style>
<div class="page">
  <div class="lead">
    <span class="eb">AlovLab · карусель · пример: {cfg['label'].lower()}</span>
    <h1>Публиковать <b>ОДНИМ постом</b>: 1 обложка → 2 провокация → 3 связка → 4 неделя → 5 пик → 6 CTA.</h1>
  </div>
  <div class="grid">
{slides}
  </div>
  <div class="notes"><b>Кейс:</b> {cfg['label']} — пример пользы ИИ в бизнесе (ниши не повторяются). <b>Выход:</b> бриф студии → @alovlab. <b>Честность:</b> кадры — концепт-дизайн; цена студии не называется.</div>
</div>
"""

# --------------------------------------------------------------------------
CONFIGS = {
  "restaurant": {
    "label": "Авторский ресторан",
    "cover_h": 'Дорогой продукт.<br>Дешёвый <span class="a">контент.</span>',
    "cover_labels": ("как есть", "как должно быть"),
    "prov_h": 'Гость выбирает<br>ресторан по <span class="a">ленте.</span>',
    "prov_sub": "Ещё до того, как попробовал. Первое впечатление — не тарелка. Первый кадр.",
    "svyazka_eyebrow": "Авторский ресторан",
    "svyazka": [
      ("Идея","Campaign Idea",'Продать не ужин. Продать <span class="a">вечер, который помнят.</span>',"Кампания начинается не с кухни. С чувства, за которым возвращаются."),
      ("Сценарий","Script Ready",'Пар над тарелкой <span class="a">рассказывает</span> историю блюда.',"За 15 секунд — от первого штриха повара до подачи в зал."),
      ("Визуал","Visual System",'Не фото еды. <span class="a">Атмосфера,</span> в которую хочется вернуться.',"Тёплый свет, текстуры, детали. Один почерк во всех роликах."),
    ],
    "nedelya": [
      ("REELS","30 sec film",'Почему в зале пусто по <span class="a">будням.</span>',"Проблема не в кухне. В тишине бренда."),
      ("КЕЙС","Content system",'<span class="a">Одна съёмка</span> вместо ежедневных.',"Один вечер превращается в неделю контента."),
      ("AI-АВАТАР","AI avatar",'Шеф говорит с гостями <span class="a">каждый день.</span>',"Один аватар. Десятки роликов. Голос заведения."),
      ("BACKSTAGE","Production",'Где кончается сток и <span class="a">начинается вкус.</span>',"Идея, свет, кадры и сборка — как продакшн."),
      ("ОФФЕР","Brand launch",'Не снимай ролик. Собери <span class="a">витрину бренда.</span>',"Одна идея должна работать не один день."),
    ],
    "pik_h": 'Один ролик<br><span class="a">наполняет зал.</span>',
    "pik_cap": "Пар над фирменным блюдом. Голос шефа. Свет, в котором хочется остаться.",
    "pik_note": "Не распыляй бюджет на десять средних. Собери один сильный — и разложи на неделю.",
    "photos": {
      "cover_rich": "content/carousel-assets/restaurant/hf_20260805_131843_164fe080-d862-4b73-a1b7-dbe6f4662e9f.png",
      "prov":       "content/carousel-assets/restaurant/hf_20260805_131843_164fe080-d862-4b73-a1b7-dbe6f4662e9f.png",
      "pik":        "content/carousel-assets/restaurant/hf_20260805_131843_27649360-b457-42af-a557-5abcdd8446fa.png",
    },
  },
}

if __name__ == "__main__":
    bid = sys.argv[1] if len(sys.argv) > 1 else "restaurant"
    cfg = CONFIGS.get(bid)
    if not cfg:
        # allow external JSON config: python3 carousel_render.py path/to/config.json
        cfg = json.loads(pathlib.Path(bid).read_text(encoding="utf-8"))
        bid = cfg.get("id", "custom")
    outdir = ROOT / "exports" / "carousels" / bid
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / f"{bid}.html"
    out.write_text(render(cfg), encoding="utf-8")
    print("HTML:", out)
