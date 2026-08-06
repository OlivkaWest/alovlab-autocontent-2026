# -*- coding: utf-8 -*-
"""AlovLab · «showcase»-карусель: премиальный тёмный стиль со стеклянным 3D-шаром,
концентрическими кольцами, искрами и градиентным заголовком (по референсу).
Всё на CSS/SVG, без внешних картинок. Запуск: python3 scripts/carousel_showcase_render.py
"""
import base64, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
OUTDIR = ROOT / "exports" / "carousels" / "showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "showcase.html"

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

# искры (детерминированные позиции: left%, top%, размер px, прозрачность, блюр px)
SPARKS = [(12,20,3,.5,0),(22,58,2,.4,0),(30,78,4,.55,1),(18,86,2,.35,0),(40,30,2,.4,0),
          (48,72,3,.45,0),(58,20,2,.35,0),(66,64,4,.5,1),(72,40,2,.4,0),(80,74,3,.45,0),
          (86,30,2,.4,0),(90,58,3,.5,1),(64,88,2,.35,0),(34,46,2,.3,0),(78,16,2,.4,0),(10,44,2,.35,0)]
def sparks():
    out=""
    for x,y,s,o,bl in SPARKS:
        out+=(f'<span style="position:absolute;left:{x}%;top:{y}%;width:{s}px;height:{s}px;border-radius:50%;'
              f'background:#ff9a4d;opacity:{o};filter:blur({bl}px);box-shadow:0 0 6px 1px rgba(255,140,60,.6)"></span>')
    return out

ICONS = {
 "list": '<rect x="20" y="26" width="9" height="9" rx="2.5"/><rect x="36" y="27" width="44" height="7" rx="3.5"/>'
         '<rect x="20" y="45.5" width="9" height="9" rx="2.5"/><rect x="36" y="46.5" width="34" height="7" rx="3.5"/>'
         '<rect x="20" y="65" width="9" height="9" rx="2.5"/><rect x="36" y="66" width="40" height="7" rx="3.5"/>',
 "spark": '<path d="M50 16l6 22 22 6-22 6-6 22-6-22-22-6 22-6z"/><path d="M78 20l2.5 7 7 2.5-7 2.5-2.5 7-2.5-7-7-2.5 7-2.5z" opacity=".8"/>',
 "layers": '<path d="M50 20 82 38 50 56 18 38z"/><path d="M22 50l28 16 28-16" fill="none" stroke-width="6" opacity=".7"/>',
 "bolt": '<path d="M54 14 26 54h20l-6 32 32-44H50z"/>',
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
.top .eb{font-weight:800;font-size:15px;letter-spacing:.16em;text-transform:uppercase;color:#8c8378}
.top .pg{font-weight:800;font-size:16px;color:var(--o2);font-variant-numeric:tabular-nums}
.top .pg b{color:#6a6157}

.head{margin-top:26px;position:relative;z-index:4}
.head h2{font-weight:800;text-transform:uppercase;letter-spacing:-.01em;line-height:.95;font-size:49px;
 transform:scaleX(.86);transform-origin:left}
.head h2 .w{color:#fff;display:block}
.head h2 .o{display:block;background:linear-gradient(180deg,var(--o3),var(--o));-webkit-background-clip:text;background-clip:text;color:transparent}
.body{margin-top:18px;font-size:16px;line-height:1.34;max-width:32ch;position:relative;z-index:4}
.body .l{color:#fff;font-weight:600}
.body .m{color:#8a8177;font-weight:500}

.stage{position:absolute;inset:0;z-index:2;pointer-events:none}
.rings{position:absolute;left:50%;top:75%;transform:translate(-50%,-50%);z-index:1}
.rings i{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);border-radius:50%;border:1px solid rgba(255,140,60,.10)}
.orbw{position:absolute;left:50%;top:75%;transform:translate(-50%,-50%);z-index:3}
.orb{width:166px;height:166px;border-radius:50%;position:relative;
 background:
  radial-gradient(circle at 50% 34%, rgba(255,165,80,.42), rgba(26,16,8,.92) 58%),
  radial-gradient(circle at 50% 118%, rgba(255,120,40,.6), transparent 52%);
 box-shadow: inset 0 -22px 44px rgba(255,120,40,.4), inset 0 14px 32px rgba(0,0,0,.65),
  inset 0 0 0 1px rgba(255,160,90,.25), 0 26px 70px rgba(255,110,30,.28);}
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
"""

def ring_sizes(): return [300,420,540,680]
def slide(eb, num, total, hw, ho, body_l, body_m, ic):
    rings="".join(f'<i style="width:{s}px;height:{s}px;opacity:{max(.04, .18-0.03*i):.2f}"></i>' for i,s in enumerate(ring_sizes()))
    return f"""<article class="slide">
  <svg width="0" height="0"><defs><linearGradient id="ig" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffc089"/><stop offset="1" stop-color="#f0712a"/></linearGradient></defs></svg>
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings}</div>
    <div class="orbw"><div class="orb">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">{eb}</span><span class="pg">{num}<b> / {total}</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="body"><span class="l">{body_l}</span> <span class="m">{body_m}</span></div>
  <div class="foot"><img class="mk" src="data:image/png;base64,{LOGO}"><span class="wm">AlovLab</span></div>
</article>"""

SLIDES = [
 slide("Key feature","4","7","Understands","Complex instructions",
       "Instead of vague single-word prompts, it follows detailed multi-step instructions —",
       "lighting direction, camera angle, clothing material, background composition — all in one pass, without needing multiple regenerations.","list"),
 slide("Key feature","2","7","Keeps every","Detail sharp",
       "From skin texture to fabric weave, fine details stay crisp —",
       "even at full resolution, without the plastic, over-smoothed look.","spark"),
 slide("Key feature","5","7","One prompt,","Many angles",
       "Generate the same scene from multiple camera angles —",
       "the character, light and mood stay consistent across every frame.","layers"),
]

HTML = f"""<title>Showcase-стиль · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · showcase-стиль (демо визуала)</span>
    <h1>Повтор референса (слайд 4/7) + 2 соседних, чтобы проверить систему.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB")
