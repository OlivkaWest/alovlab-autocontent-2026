# -*- coding: utf-8 -*-
"""AlovLab · обложка закрытого канала курса (showcase-стиль). 4:5, 1080x1350.
Запуск: python3 scripts/cover_channel.py"""
import pathlib
from carousel_showcase_render import (CSS, DEFS, FOOT, sparks, rings, icon, ROOT)

OUTDIR = ROOT / "exports" / "covers"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "channel-cover.html"

SLIDE = f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb big">{icon('spark')}</div></div></div>
  <div class="top"><span class="eb">AlovLab · закрытый канал курса</span></div>
  <div class="head"><h2><span class="w">Вы</span><span class="o">внутри.</span></h2></div>
  <div class="sub">Курс «Нейросети и ChatGPT для каждого». Осваиваем ИИ спокойно и по-настоящему.</div>
  {FOOT}
</article>"""

HTML = f"""<title>Обложка канала · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page"><div class="grid">{SLIDE}</div></div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB")
