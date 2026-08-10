# -*- coding: utf-8 -*-
"""AlovLab · обложка закрытого канала курса под закреп (showcase). 4:5, 1080x1350.
Тематический знак «вход» + метки пути (кабинет · ассистент · чат). python3 scripts/cover_channel.py"""
import pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "covers"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "channel-cover.html"

EXTRA = r"""
.cover .sub{max-width:30ch}
.path{position:relative;z-index:4;margin-top:22px;display:flex;flex-direction:column;gap:13px}
.path .pi{display:flex;align-items:baseline;gap:12px}
.path .pi i{width:9px;height:9px;border-radius:50%;background:var(--o2);flex:0 0 auto;position:relative;top:-2px;
 box-shadow:0 0 8px 1px rgba(255,140,60,.7)}
.path .pi b{font-weight:800;font-size:20px;color:#fff}
.path .pi span{font-size:14.5px;color:#8a8177;font-weight:500}
"""
CSS = CSS0 + EXTRA

# знак «вход»: стрелка входит в дверь
ENTER = ('<svg viewBox="0 0 100 100" style="width:46%;height:46%;position:absolute;left:27%;top:27%;z-index:3" '
         'fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">'
         '<rect x="50" y="18" width="32" height="64" rx="5"/>'
         '<path d="M16 50h30M34 38l12 12-12 12"/>'
         '<circle cx="56" cy="50" r="3" fill="url(#ig)" stroke="none"/></svg>')

def pi(b, s):
    return f'<div class="pi"><i></i><b>{b}</b> <span>· {s}</span></div>'

SLIDE = f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb">{ENTER}</div></div></div>
  <div class="top"><span class="eb">AlovLab · закрытый канал курса</span></div>
  <div class="head"><h2><span class="w">Вы</span><span class="o">внутри.</span></h2></div>
  <div class="sub">Курс «Нейросети и ChatGPT для каждого».</div>
  <div class="path">
    {pi("Личный кабинет", "уроки и материалы")}
    {pi("Ассистент", "вопросы по курсу")}
    {pi("Этот чат", "общение и команда")}
  </div>
  {FOOT}
</article>"""

HTML = f"""<title>Обложка канала · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page"><div class="grid">{SLIDE}</div></div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB")
