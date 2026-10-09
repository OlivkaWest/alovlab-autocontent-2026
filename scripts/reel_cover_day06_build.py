# -*- coding: utf-8 -*-
"""AlovLab · Обложки Reels на 06.10.2026 (RU+EN), 1080x1920 (9:16).
Чисто типографика (без Higgsfield) — сетевой блок на upload.higgsfield.ai/*.cloudfront.net
подтверждён в этой среде ранее в сессии (та же причина, что у инстаграм-карусели этого дня).
Тёмный кинематографичный фон (радиальный градиент, фирменный оранжевый), как у обложки
reels-extra/day-02 (та тоже тёмная, просто с фото-фоном из Higgsfield, которого здесь нет).
Запуск: python3 scripts/reel_cover_day06_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/cover_shoot.js <html> <outdir>
"""
import base64, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "reels-extra" / "day-06" / "cover"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "covers.html"

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
FONTS = ROOT / "assets" / "fonts"

RANGES = {"cyrillic": "U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin": "U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192"}
faces = ""
for w in (400, 500, 700, 800):
    for sub in ("cyrillic", "latin"):
        fp = FONTS / f"manrope-{sub}-{w}.woff2"
        if fp.exists():
            faces += ("@font-face{font-family:'Manrope';font-weight:%d;font-display:swap;"
                      "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}\n"
                      % (w, b64(fp), RANGES[sub]))

CSS = faces + r"""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0d0b07}
.cover{position:relative;width:540px;height:960px;overflow:hidden;background:#13100A;
 font-family:'Manrope',system-ui,sans-serif;display:flex;flex-direction:column}
.cover::before{content:"";position:absolute;inset:0;
 background:radial-gradient(130% 70% at 50% 0%,rgba(218,95,30,.45),rgba(19,16,10,0) 58%),
 linear-gradient(180deg,#1c160d,#0d0b07)}
.brand{position:relative;z-index:2;display:flex;align-items:center;gap:8px;padding:48px 36px 0}
.brand img{width:26px;height:26px;border-radius:7px}
.brand b{font-weight:800;font-size:14pt;color:#fff}
.brand b i{color:#ff7a33;font-style:normal}
.mid{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 36px}
.kick{font-weight:800;font-size:11pt;letter-spacing:.16em;text-transform:uppercase;color:#ff9a52;margin-bottom:16px}
.ttl{font-weight:800;font-size:40pt;line-height:1.08;letter-spacing:-.02em;color:#fff}
.ttl i{color:#ff7a33;font-style:normal;display:block}
.sub{position:relative;z-index:2;padding:0 36px 52px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:30ch}
.badge{position:relative;z-index:2;margin:0 36px 44px;display:inline-flex;align-self:flex-start;
 font-size:10pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.28);border-radius:22px;padding:8px 16px}
"""

html = f"""<!doctype html><html lang=ru><head><meta charset=utf-8><style>{CSS}</style></head><body>

<div class="cover" data-name="cover-ru">
  <div class="brand"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div>
  <div class="mid">
    <div class="kick">Приём дня</div>
    <div class="ttl">ФОРМАТ,<br>НЕ<br><i>«ПОКРАСИВЕЕ»</i></div>
  </div>
  <div class="sub">Одна строка в промпте, и ответ готов к использованию сразу</div>
  <div class="badge">Reels · 06.10</div>
</div>

<div class="cover" data-name="cover-en">
  <div class="brand"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div>
  <div class="mid">
    <div class="kick">Today's technique</div>
    <div class="ttl">ASK FOR<br><i>A FORMAT,</i><br>NOT "NICER"</div>
  </div>
  <div class="sub">One line in your prompt, and the answer is ready to use</div>
  <div class="badge">Reels · Oct 6</div>
</div>

</body></html>"""
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT)
