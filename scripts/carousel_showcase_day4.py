# -*- coding: utf-8 -*-
"""AlovLab · День 4 «Угол, а не тема» в SHOWCASE-стиле (стеклянный орб).
Обложка + 5 углов (ошибка/миф/цена/взгляд изнутри/вопрос) + CTA. RU, кроме AlovLab.
Переиспользует стиль из carousel_showcase_render. Запуск: python3 scripts/carousel_showcase_day4.py
"""
import pathlib
from carousel_showcase_render import (CSS, DEFS, FOOT, sparks, rings, icon, ICONS, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-04-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-04-showcase.html"

# новые иконки под углы (stroke-варианты — задаём stroke на путях, fill=none)
ICONS.update({
 "target": '<g fill="none" stroke="url(#ig)" stroke-width="7"><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="15"/></g><circle cx="50" cy="50" r="5"/>',
 "warn":   '<path d="M50 20 82 76H18z" fill="none" stroke="url(#ig)" stroke-width="7" stroke-linejoin="round"/><rect x="46" y="40" width="8" height="20" rx="4"/><circle cx="50" cy="67" r="4.5"/>',
 "myth":   '<circle cx="50" cy="50" r="28" fill="none" stroke="url(#ig)" stroke-width="7"/><path d="M31 31 69 69" stroke="url(#ig)" stroke-width="7" stroke-linecap="round"/>',
 "price":  '<circle cx="50" cy="54" r="26" fill="none" stroke="url(#ig)" stroke-width="7"/><path d="M50 54V38M50 54l13 8" fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/><rect x="42" y="16" width="16" height="8" rx="4"/>',
 "eye":    '<path d="M18 50c11-17 53-17 64 0-11 17-53 17-64 0z" fill="none" stroke="url(#ig)" stroke-width="7" stroke-linejoin="round"/><circle cx="50" cy="50" r="9"/>',
 "quest":  '<path d="M37 39a13 13 0 1 1 19 11c-4 3-6 5-6 11" fill="none" stroke="url(#ig)" stroke-width="7" stroke-linecap="round"/><circle cx="50" cy="74" r="5"/>',
})

def cover(hw, ho, sub, ic):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb big">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">AlovLab · как найти угол</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
  {FOOT}
</article>"""

def ang(num, hw, ho, bl, bm, ic):
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">Заход</span><span class="pg">{num}<b> / 5</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="body"><span class="l">{bl}</span> <span class="m">{bm}</span></div>
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
 cover("Угол,", "а не тема.", "Тема у всех одна. Смотрят того, кто зашёл с другой стороны.", "target"),
 ang(1,"Угол","ошибки","Где человек сам себе мешает —","«Ты снимаешь сам, хотя нейросеть уже умеет».","warn"),
 ang(2,"Угол","мифа","Слом убеждения — заходит сильнее всего —","«Дорогой ролик — не про камеру».","myth"),
 ang(3,"Угол","цены","Сколько уже потрачено впустую —","«Смена и команда — за вечер на ноутбуке».","price"),
 ang(4,"Взгляд","изнутри","Что обычно не говорят вслух —","«Что вырезают из красивых туториалов».","eye"),
 ang(5,"Вопрос","новичка","С чего вообще начать —","«Открыл нейросеть впервые — и что дальше?».","quest"),
 cta("Собери","5 углов.",
     ["<b>одна тема</b> → пять заходов → один рабочий",
      "8 типов углов и критерий силы — в тетради",
      "разложи свою тему за 15 минут"],
     "Тетрадь → t.me/AlovLab"),
]

HTML = f"""<title>Угол, а не тема · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 4 · 7 августа · showcase-стиль</span>
    <h1>Одним постом: обложка → 5 углов → CTA. Instagram и Telegram, 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
