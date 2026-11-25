# -*- coding: utf-8 -*-
"""Собирает премиальный HTML-исходник методички (тёмная тема AlovLab) для печати в PDF."""
import base64, pathlib, re, markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
MD = ROOT / "content" / "guides" / "higgsfield-restaurant-reel.md"
OUTDIR = ROOT / "exports" / "guides"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "higgsfield-restaurant-reel.html"

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
HERO = b64(ROOT / "content/carousel-assets/restaurant/hf_20260805_131843_164fe080-d862-4b73-a1b7-dbe6f4662e9f.png")

RANGES = {"cyrillic":"U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin":"U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192"}
faces=""
for w in (400,500,700,800):
    for sub in ("cyrillic","latin"):
        faces+=("@font-face{font-family:'Manrope';font-weight:%d;font-display:swap;"
                "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}\n"
                % (w, b64(FONTS/f'manrope-{sub}-{w}.woff2'), RANGES[sub]))

md_text = MD.read_text(encoding="utf-8")
# первый H1 и подзаголовок уводим на обложку — вырезаем из тела
body_md = re.sub(r"^# .*?\n(### .*?\n)?", "", md_text, count=1, flags=re.S)
html_body = markdown.markdown(body_md, extensions=["tables", "fenced_code", "sane_lists"])
# чек-лист: "[ ] " -> класс .chk
html_body = html_body.replace("<li>[ ] ", '<li class="chk">')

CSS = faces + r"""
@page { size: A4; margin: 15mm 14mm; }
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#0d0b08;--o:#e8672a;--o2:#ff7a33;--text:#f4efe6;--muted:#b3a898;--dim:#7c7060;--line:rgba(244,239,230,.12);--card:#17120b;}
html,body{background:#0d0b08}
body{font-family:'Manrope',system-ui,sans-serif;color:var(--text);-webkit-font-smoothing:antialiased;font-size:11pt;line-height:1.55}

/* обложка */
.cover{position:relative;height:267mm;border-radius:10px;overflow:hidden;display:flex;flex-direction:column;
background:radial-gradient(120% 70% at 80% 8%,#2a2013,#160f08 55%,var(--ink));page-break-after:always}
.cover-hero{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.55}
.cover-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,11,8,.35) 0%,rgba(13,11,8,.2) 40%,rgba(13,11,8,.96) 88%)}
.cover-top{position:relative;z-index:2;padding:20mm 16mm 0}
.brand{display:inline-flex;align-items:center;gap:9px}
.brand img{width:30px;height:30px;border-radius:8px}
.brand b{font-weight:800;font-size:15pt;color:#fff}.brand b i{color:var(--o2);font-style:normal}
.cover-bottom{position:relative;z-index:2;margin-top:auto;padding:0 16mm 20mm}
.kicker{font-weight:800;font-size:9.5pt;letter-spacing:.16em;text-transform:uppercase;color:var(--o2);margin-bottom:10px}
.cover h1{font-weight:800;font-size:33pt;line-height:1.04;letter-spacing:-.02em;color:#fff;max-width:16ch}
.cover .sub{margin-top:14px;font-size:12.5pt;line-height:1.45;color:var(--muted);max-width:34ch}
.cover .sig{margin-top:20px;font-weight:700;font-size:10pt;color:var(--dim);letter-spacing:.04em}

/* тело */
.doc{padding-top:2mm}
h2{font-weight:800;font-size:17pt;letter-spacing:-.01em;color:#fff;margin:22px 0 10px;padding-top:8px;
border-top:1px solid var(--line);page-break-after:avoid}
h2:first-of-type{border-top:none}
h3{font-weight:800;font-size:12.5pt;color:var(--o2);margin:16px 0 8px;page-break-after:avoid}
p{margin:8px 0}
strong{color:#fff;font-weight:700}
em{color:var(--muted);font-style:italic}
ul,ol{margin:8px 0 8px 20px}li{margin:4px 0}
li::marker{color:var(--o)}
a{color:var(--o2)}

blockquote{margin:10px 0;padding:10px 14px;border-left:3px solid var(--o);background:rgba(232,103,42,.08);
border-radius:0 8px 8px 0;color:#fff;font-size:11.5pt;page-break-inside:avoid}
blockquote p{margin:3px 0}

pre{background:#120d07;border:1px solid rgba(255,150,80,.28);border-left:3px solid var(--o);border-radius:8px;
padding:11px 13px;margin:9px 0;overflow-x:auto;page-break-inside:avoid}
pre code{font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:9pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
:not(pre)>code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:9.5pt;background:rgba(255,150,80,.12);
color:#ffcaa0;padding:1px 5px;border-radius:5px}

table{width:100%;border-collapse:collapse;margin:10px 0;font-size:9.5pt;page-break-inside:avoid}
th{background:rgba(232,103,42,.14);color:var(--o2);font-weight:800;text-transform:uppercase;letter-spacing:.04em;
font-size:8pt;text-align:left;padding:7px 9px;border-bottom:1px solid var(--line)}
td{padding:7px 9px;border-bottom:1px solid var(--line);color:var(--text);vertical-align:top}
tr:nth-child(even) td{background:rgba(244,239,230,.03)}

li.chk{list-style:none;position:relative;padding-left:26px;margin:5px 0}
li.chk::before{content:"";position:absolute;left:0;top:2px;width:15px;height:15px;border-radius:4px;
border:1.5px solid var(--o);background:rgba(232,103,42,.1)}
ul:has(li.chk){margin-left:2px;columns:1}

h2,h3{page-break-inside:avoid}

.contacts{margin-top:26px;padding:24px 20px;border-radius:12px;page-break-inside:avoid;text-align:center;
background:radial-gradient(120% 100% at 50% 0%,#2a2013,#160f08 60%,var(--ink));border:1px solid rgba(232,103,42,.28)}
.contacts img{width:48px;height:48px;border-radius:12px}
.contacts .ct-h{font-weight:800;font-size:15pt;color:#fff;margin:13px 0 6px}
.contacts .ct-sub{color:var(--muted);font-size:10.5pt;margin:0 auto 16px;max-width:44ch}
.chips{display:flex;gap:9px;justify-content:center;flex-wrap:wrap}
.chips a{font-weight:800;font-size:10pt;text-decoration:none;padding:9px 15px;border-radius:9px;
color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o))}
.chips a.ghost{color:var(--o2);background:transparent;border:1px solid rgba(232,103,42,.5)}
"""

HTML = f"""<meta charset="utf-8">
<title>Higgsfield · Ресторанный Reels · AlovLab</title>
<style>{CSS}</style>
<section class="cover">
  <div class="cover-hero" style="background-image:url(data:image/png;base64,{HERO})"></div>
  <div class="cover-top">
    <span class="brand"><img src="data:image/png;base64,{LOGO}" alt=""><b>Alov<i>Lab</i></b></span>
  </div>
  <div class="cover-bottom">
    <div class="kicker">Практическая методичка AlovLab</div>
    <h1>Ресторан, который продаёт себя за 30 секунд</h1>
    <p class="sub">Как собрать кинематографичный Reels ресторана в Higgsfield AI — из четырёх картинок, аватара и закадрового голоса.</p>
    <div class="sig">Higgsfield AI · Image-to-Video · аватар Нейромонах</div>
  </div>
</section>
<div class="doc">
{html_body}
<section class="contacts">
  <img src="data:image/png;base64,{LOGO}" alt="AlovLab">
  <div class="ct-h">Сделал ролик — покажи. Застрял — приходи.</div>
  <div class="ct-sub">Гайды, промпт дня и разборы — в Telegram. Там же можно показать свои работы и задать вопрос.</div>
  <div class="chips">
    <a href="https://t.me/AlovLab">Telegram · t.me/AlovLab</a>
    <a class="ghost" href="https://vk.com/alovlab">VK · vk.com/alovlab</a>
    <a class="ghost" href="https://alovlab.ru">Сайт · alovlab.ru</a>
  </div>
</section>
</div>
"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB")
