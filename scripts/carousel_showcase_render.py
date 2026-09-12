# -*- coding: utf-8 -*-
"""AlovLab · showcase-карусель «Что нейросеть делает за тебя» (обучающая, RU).
Премиальный стиль: стеклянный 3D-шар с иконкой, кольца, искры, градиент-заголовок.
Всё на CSS/SVG. Подпись AlovLab — единственное на латинице. 4:5 (Instagram + Telegram).
Запуск: python3 scripts/carousel_showcase_render.py
"""
import base64, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
OUTDIR = ROOT / "exports" / "carousels" / "ai-za-tebya"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "ai-za-tebya.html"

RANGES = {"cyrillic":"U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin":"U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192"}
faces=""
for w in (400,500,700,800):
    for sub in ("cyrillic","latin"):
        fp=FONTS/f'manrope-{sub}-{w}.woff2'
        if fp.exists():
            faces+=("@font-face{font-family:'Manrope';font-weight:%d;font-display:swap;"
                    "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}\n"
                    % (w, b64(fp), RANGES[sub]))

SPARKS = [(12,20,3,.5,0),(22,58,2,.4,0),(30,78,4,.55,1),(18,86,2,.35,0),(40,30,2,.4,0),
          (48,72,3,.45,0),(58,20,2,.35,0),(66,64,4,.5,1),(72,40,2,.4,0),(80,74,3,.45,0),
          (86,30,2,.4,0),(90,58,3,.5,1),(64,88,2,.35,0),(34,46,2,.3,0),(78,16,2,.4,0),(10,44,2,.35,0)]
def sparks():
    return "".join(f'<span style="position:absolute;left:{x}%;top:{y}%;width:{s}px;height:{s}px;border-radius:50%;'
                   f'background:#ff9a4d;opacity:{o};filter:blur({bl}px);box-shadow:0 0 6px 1px rgba(255,140,60,.6)"></span>'
                   for x,y,s,o,bl in SPARKS)

D = "#170d06"  # тёмная «дырка» в иконках
ICONS = {
 "bulb": f'<path d="M50 16a22 22 0 0 0-13 39c3 3 5 6 5 10h16c0-4 2-7 5-10a22 22 0 0 0-13-39z"/><rect x="42" y="70" width="16" height="7" rx="3"/><rect x="44" y="81" width="12" height="6" rx="3"/>',
 "text": '<rect x="22" y="26" width="56" height="8" rx="4"/><rect x="22" y="44" width="56" height="8" rx="4"/><rect x="22" y="62" width="36" height="8" rx="4"/>',
 "image": f'<rect x="20" y="26" width="60" height="48" rx="9"/><circle cx="38" cy="44" r="7" fill="{D}"/><path d="M26 71l18-18 12 10 8-6 10 10v4z" fill="{D}"/>',
 "video": f'<rect x="20" y="26" width="60" height="48" rx="11"/><path d="M44 39l21 11-21 11z" fill="{D}"/>',
 "voice": '<rect x="20" y="45" width="6" height="10" rx="3"/><rect x="32" y="36" width="6" height="28" rx="3"/><rect x="44" y="26" width="6" height="48" rx="3"/><rect x="56" y="34" width="6" height="32" rx="3"/><rect x="68" y="43" width="6" height="14" rx="3"/>',
 "avatar": '<circle cx="50" cy="38" r="14"/><path d="M26 80c0-14 11-24 24-24s24 10 24 24z"/>',
 "spark": '<path d="M50 14l7 24 24 7-24 7-7 24-7-24-24-7 24-7z"/>',
}
def icon(k):
    return (f'<svg viewBox="0 0 100 100" style="width:46%;height:46%;position:absolute;left:27%;top:27%;z-index:3" '
            f'fill="url(#ig)" stroke="none">{ICONS[k]}</svg>')

CSS = faces + r"""
*{margin:0;padding:0;box-sizing:border-box}
:root{--o:#e8672a;--o2:#ff8a3d;--o3:#ffb066}
html{background:#0a0806}
body{font-family:'Manrope',system-ui,sans-serif;background:#0a0806;color:#fff;-webkit-font-smoothing:antialiased;
padding:clamp(18px,3.5vw,44px) clamp(12px,3vw,30px)}
.page{max-width:1160px;margin:0 auto}
.lead{margin-bottom:24px}.lead .eb{font-weight:800;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--o2)}
.lead h1{font-weight:800;font-size:clamp(18px,3vw,24px);margin:9px 0 0;line-height:1.3;color:#fff}
.grid{display:flex;flex-wrap:wrap;gap:22px;justify-content:center}

.slide{position:relative;width:min(540px,92vw);aspect-ratio:4/5;border-radius:22px;overflow:hidden;
background:
 radial-gradient(70% 42% at 88% 6%, rgba(255,130,40,.38), transparent 58%),
 radial-gradient(60% 45% at 50% 84%, rgba(255,110,35,.22), transparent 62%),
 linear-gradient(180deg,#0d0a07,#080605);
padding:42px 44px;display:flex;flex-direction:column;border:1px solid rgba(255,140,60,.08)}

.top{display:flex;justify-content:space-between;align-items:center;padding-bottom:16px;border-bottom:1px solid rgba(255,255,255,.12);position:relative;z-index:4}
.top .eb{font-weight:800;font-size:13.5px;letter-spacing:.15em;text-transform:uppercase;color:#8c8378}
.top .pg{font-weight:800;font-size:16px;color:var(--o2);font-variant-numeric:tabular-nums}
.top .pg b{color:#6a6157}

.head{margin-top:24px;position:relative;z-index:4}
.head h2{font-weight:800;text-transform:uppercase;letter-spacing:-.01em;line-height:.98;font-size:47px;
 transform:scaleX(.9);transform-origin:left}
.head h2 .w{color:#fff;display:block}
.head h2 .o{display:block;background:linear-gradient(180deg,var(--o3),var(--o));-webkit-background-clip:text;background-clip:text;color:transparent}
.body{margin-top:18px;font-size:16.5px;line-height:1.4;max-width:32ch;position:relative;z-index:4}
.body .l{color:#fff;font-weight:600}
.body .m{color:#8a8177;font-weight:500}

.stage{position:absolute;inset:0;z-index:2;pointer-events:none}
.rings{position:absolute;left:50%;top:76%;transform:translate(-50%,-50%);z-index:1}
.rings i{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);border-radius:50%;border:1px solid rgba(255,140,60,.10)}
.orbw{position:absolute;left:50%;top:76%;transform:translate(-50%,-50%);z-index:3}
.orb{width:162px;height:162px;border-radius:50%;position:relative;
 background:
  radial-gradient(circle at 50% 34%, rgba(255,165,80,.42), rgba(26,16,8,.92) 58%),
  radial-gradient(circle at 50% 118%, rgba(255,120,40,.6), transparent 52%);
 box-shadow: inset 0 -22px 44px rgba(255,120,40,.4), inset 0 14px 32px rgba(0,0,0,.65),
  inset 0 0 0 1px rgba(255,160,90,.25), 0 26px 70px rgba(255,110,30,.28);}
.orb.big{width:210px;height:210px}
.orb::before{content:"";position:absolute;top:9%;left:24%;width:44%;height:26%;border-radius:50%;
 background:radial-gradient(circle, rgba(255,255,255,.3), transparent 70%);filter:blur(4px);z-index:4}
.orb::after{content:"";position:absolute;left:20%;right:20%;bottom:-8%;height:20px;border-radius:50%;
 background:radial-gradient(circle, rgba(255,130,50,.6), transparent 70%);filter:blur(7px)}

.foot{margin-top:auto;display:flex;align-items:center;gap:9px;position:relative;z-index:4}
.foot .mk{width:26px;height:26px;border-radius:7px}
.foot .wm{position:relative;font-weight:800;font-size:19px;color:#e9e2d8;letter-spacing:.01em}
.foot .wm::after{content:"";position:absolute;left:0;right:0;bottom:-8px;height:3px;border-radius:2px;
 background:linear-gradient(90deg,var(--o),transparent)}
.sparks{position:absolute;inset:0;z-index:1;pointer-events:none}

/* обложка */
.cover .head h2{font-size:52px}
.cover .sub{margin-top:20px;font-size:19px;line-height:1.4;color:#b9ad9b;max-width:26ch;position:relative;z-index:4}
/* cta */
.cta .clist{margin-top:20px;display:flex;flex-direction:column;gap:11px;position:relative;z-index:4}
.cta .clist .li{display:flex;gap:11px;align-items:flex-start;font-size:16px;color:#b9ad9b;line-height:1.35;max-width:34ch}
.cta .clist .li i{width:8px;height:8px;border-radius:50%;background:var(--o2);flex:0 0 auto;margin-top:6px;box-shadow:0 0 8px 1px rgba(255,140,60,.7)}
.cta .clist .li b{color:#fff;font-weight:700}
.cta .btn{position:relative;z-index:4;align-self:flex-start;margin-top:26px;font-weight:800;font-size:17px;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));border-radius:13px;padding:16px 26px;box-shadow:0 16px 34px -12px rgba(232,103,42,.8)}
"""

DEFS = ('<svg width="0" height="0"><defs><linearGradient id="ig" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="#ffc089"/><stop offset="1" stop-color="#f0712a"/></linearGradient></defs></svg>')
def rings():
    return "".join(f'<i style="width:{s}px;height:{s}px;opacity:{max(.04,.18-0.03*i):.2f}"></i>' for i,s in enumerate([300,420,540,680]))
FOOT = f'<div class="foot"><img class="mk" src="data:image/png;base64,{LOGO}"><span class="wm">AlovLab</span></div>'

def cap(num, total, hw, ho, bl, bm, ic):
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">Возможность</span><span class="pg">{num}<b> / {total}</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="body"><span class="l">{bl}</span> <span class="m">{bm}</span></div>
  {FOOT}
</article>"""

def cover(hw, ho, sub, ic):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb big">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">AlovLab · нейросети для контента</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
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

SLIDES = [
 cover("Что нейросеть", "делает за тебя.", "Шесть задач, которые съедали весь день. Теперь — минуты.", "spark"),
 cap(1,6,"Придумает","идеи","Десятки идей и заходов под твою тему —","за минуту, а не за вечер мозгового штурма в одиночку.","bulb"),
 cap(2,6,"Напишет","текст","Хук, сценарий, описание поста в твоём голосе —","если задать стиль и пару примеров, как ты пишешь.","text"),
 cap(3,6,"Соберёт","картинку","Обложку, фон, продукт по описанию —","свет, ракурс, материал за один проход, без сотни попыток.","image"),
 cap(4,6,"Оживит","фото в видео","Статичный кадр превращает в кинокадр —","с плавным движением камеры и живым тёплым светом.","video"),
 cap(5,6,"Озвучит","голосом","Читает текст живым голосом —","на 90+ языках, без диктора и студии звукозаписи.","voice"),
 cap(6,6,"Сделает","аватара","Говорящий двойник ведёт ролики каждый день —","в кадре ты, а снимать ничего не нужно.","avatar"),
 cta("Научись","управлять этим.",
     ["<b>6 «Земель»</b> — от текста до аватаров, по шагам",
      "готовые промпты и разборы под каждую задачу",
      "от «никогда не пробовал» до своей системы контента"],
     "Курс → t.me/AlovLab"),
]

HTML = f"""<title>Что нейросеть делает за тебя · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · showcase · «Что нейросеть делает за тебя»</span>
    <h1>Публиковать <b>ОДНИМ постом</b>: обложка → 6 возможностей → CTA. Instagram и Telegram, 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
