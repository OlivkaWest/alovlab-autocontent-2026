# -*- coding: utf-8 -*-
"""Обложка Reels «Прогрев» 9:16 — кадр уголёк + хук. Рендер: story_shoot.js → 1080×1920."""
import base64, pathlib
from carousel_showcase_render import CSS as CSS0, LOGO, ROOT
OUT = ROOT / "exports" / "covers" / "progrev"; OUT.mkdir(parents=True, exist_ok=True)
EMBER = ROOT / "content/carousel-assets/day-21/ChatGPT Image 24 авг. 2026 г., 13_00_24.png"
img = "data:image/png;base64," + base64.b64encode(EMBER.read_bytes()).decode()
CSS = CSS0 + r"""
.story{position:relative;width:540px;height:960px;overflow:hidden;background:#0a0806;font-family:'Manrope',sans-serif}
.story .bg{position:absolute;inset:0;background-image:url(IMG);background-size:cover;background-position:50% 64%}
.story .scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,5,4,.93) 6%,rgba(6,5,4,.55) 30%,rgba(6,5,4,0) 50%,rgba(6,5,4,0) 82%,rgba(6,5,4,.6) 100%)}
.story .hd{position:absolute;left:34px;right:34px;top:40px}
.story .hd h1{font-weight:800;font-size:60px;line-height:.94;letter-spacing:-.02em;text-transform:uppercase;color:#fff;text-shadow:0 3px 22px rgba(0,0,0,.8)}
.story .hd h1 .o{color:#ff7a1a}
.story .pl{display:inline-block;margin-top:16px;background:rgba(10,8,6,.72);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);border-radius:8px;padding:9px 15px}
.story .pl b{font-weight:800;font-size:30px;letter-spacing:-.01em;text-transform:uppercase;color:#fff}
.story .pl b i{color:#ff7a1a;font-style:normal}
.story .lg{margin-top:18px;display:flex;align-items:center;gap:8px;opacity:.95}
.story .lg img{width:30px;height:30px;border-radius:8px}
.story .lg b{font-weight:800;font-size:17px;color:#fff}.story .lg b i{color:#ff7a1a;font-style:normal}
""".replace("IMG", img)
HTML = (f'<meta charset="utf-8"><style>{CSS}</style>'
        f'<div class="story"><div class="bg"></div><div class="scrim"></div>'
        f'<div class="hd"><h1>Ты теряешь <span class="o">лида после</span> скачивания.</h1>'
        f'<div class="pl"><b>Не до. <i>После.</i></b></div>'
        f'<div class="lg"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div></div></div>')
(OUT / "cover.html").write_text(HTML, encoding="utf-8")
print("HTML:", OUT / "cover.html")
