# -*- coding: utf-8 -*-
"""AlovLab · День 7 «Связка недели: одна идея — семь дней» в SHOWCASE-стиле.
Обложка → проблема → причина → ошибка → 7 ролей → пример (ниша ИИ/контент) → промпт → CTA.
RU кроме AlovLab. Пример — «Дело не в модели, а в связке», НЕ питание. Запуск: python3 scripts/carousel_showcase_day7.py
"""
import pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, icon, ICONS, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-07-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-07-showcase.html"

EXTRA = r"""
.hsm .head h2{font-size:38px}
.pu{position:relative;z-index:4;margin-top:14px;display:inline-block;font-weight:800;font-size:11px;text-transform:uppercase;
 letter-spacing:.03em;color:var(--o2);background:rgba(232,103,42,.13);border:1px solid rgba(232,103,42,.3);border-radius:20px;padding:8px 14px}
.pbox{position:relative;z-index:4;margin-top:15px;background:#120c06;border:1px solid rgba(255,150,80,.28);
 border-left:3px solid var(--o);border-radius:14px;padding:16px 18px}
.pbox .tag{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px;margin-bottom:11px}
.pbox code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:12px;line-height:1.5;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pbox .ru{margin-top:11px;padding-top:10px;border-top:1px solid rgba(255,255,255,.1);font-size:11.5px;line-height:1.4;color:#b9ad9b}
.pbox .ru b{color:#fff}
/* список ролей / дней */
.mlist{position:relative;z-index:4;margin-top:16px;margin-bottom:6px;display:flex;flex-direction:column;gap:8px}
.mrow{display:flex;align-items:center;gap:13px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:13px;padding:10px 15px}
.mrow .n{flex:0 0 auto;width:30px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:11px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));text-transform:uppercase;letter-spacing:.02em}
.mrow .t{display:flex;flex-direction:column;gap:1px;min-width:0}
.mrow .t b{font-weight:700;font-size:15px;color:#fff;line-height:1.15}
.mrow .t span{font-weight:500;font-size:12.5px;color:#8a8177;line-height:1.2}
/* пример-неделя */
.wk{position:relative;z-index:4;margin-top:16px;display:flex;flex-direction:column;gap:9px}
.idea{font-weight:700;font-size:15px;color:#fff;line-height:1.35;background:#130c06;border:1px solid rgba(255,150,80,.3);
 border-left:3px solid var(--o);border-radius:12px;padding:13px 15px}
.idea b{color:var(--o2);text-transform:uppercase;font-size:10px;letter-spacing:.05em;display:block;margin-bottom:5px}
.wrow{display:flex;align-items:center;gap:12px;border-bottom:1px solid rgba(255,255,255,.07);padding:7px 2px}
.wrow:last-child{border-bottom:none}
.wrow .d{flex:0 0 auto;width:40px;font-weight:800;font-size:12px;color:var(--o2);text-transform:uppercase}
.wrow .r{font-weight:700;font-size:13.5px;color:#fff;min-width:96px}
.wrow .x{font-size:12px;color:#8a8177;line-height:1.25}
"""
CSS = CSS0 + EXTRA

ICONS.update({
 "link":  '<circle cx="39" cy="50" r="16" fill="none" stroke="url(#ig)" stroke-width="7"/><circle cx="61" cy="50" r="16" fill="none" stroke="url(#ig)" stroke-width="7"/>',
 "redo":  '<path d="M76 40a27 27 0 1 0 3 18" fill="none" stroke="url(#ig)" stroke-width="7" stroke-linecap="round"/><path d="M77 24v18H59" fill="none" stroke="url(#ig)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>',
 "sys":   '<rect x="16" y="40" width="20" height="20" rx="5" fill="none" stroke="url(#ig)" stroke-width="6"/><rect x="64" y="40" width="20" height="20" rx="5" fill="none" stroke="url(#ig)" stroke-width="6"/><path d="M36 50h28" stroke="url(#ig)" stroke-width="6"/><path d="M56 44l8 6-8 6" fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
 "fork":  '<circle cx="50" cy="72" r="6"/><path d="M50 66V52" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/><path d="M50 52 26 30M50 52 74 30M50 52 20 46M50 52 80 46" fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/>',
})

def cover(hw, ho, sub, ic):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb big">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">AlovLab · система вместо хаоса</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
  {FOOT}
</article>"""

def blk(eb, hw, ho, bl, bm, ic):
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">{eb}</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="body"><span class="l">{bl}</span> <span class="m">{bm}</span></div>
  {FOOT}
</article>"""

ROLES = [
 ("1","Польза","приём, который сработает сразу"),
 ("2","Позиция","как надо — и как нет"),
 ("3","Связка","разбор одной рабочей связки"),
 ("4","Кейс","что реально вышло, с деталью"),
 ("5","Практика","повтори за мной, по шагам"),
 ("6","Приглашение","мягкий шаг: гайд, промпт"),
 ("7","Итог","вывод недели одной мыслью"),
]
def roles_slide():
    rows="".join(f'<div class="mrow"><div class="n">{n}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>'
                 for n,t,s in ROLES)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Решение · 7 ролей</span></div>
  <div class="head"><h2><span class="w">Одна идея —</span><span class="o">семь ролей.</span></h2></div>
  <div class="mlist">{rows}</div>
  {FOOT}
</article>"""

WEEK = [
 ("Пн","Польза","промпт, который даёт «дорогой» кадр новичку"),
 ("Вт","Позиция","почему винят модель, а решает система"),
 ("Ср","Связка","разбор: Midjourney → Nano Banana"),
 ("Чт","Кейс","до/после — обычное фото → премиум-кадр"),
 ("Пт","Приглашение","забери разбор связок в тетради"),
]
def example_slide():
    rows="".join(f'<div class="wrow"><div class="d">{d}</div><div class="r">{r}</div><div class="x">{x}</div></div>'
                 for d,r,x in WEEK)
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый пример</span></div>
  <div class="head"><h2><span class="w">Одна идея —</span><span class="o">вся неделя.</span></h2></div>
  <div class="wk">
    <div class="idea"><b>Идея недели</b>«Дело не в модели, а в связке».</div>
    {rows}
  </div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт</span></div>
  <div class="head"><h2><span class="w">Промпт:</span><span class="o">идея на неделю.</span></h2></div>
  <div class="pu">Польза · блогер · эксперт · SMM · бизнес</div>
  <div class="pbox"><span class="tag">Claude / ChatGPT</span><code>Идея недели: [ТВОЯ ИДЕЯ].
Разложи её на 7 дней контента — по одной роли на день:
польза, позиция, связка, кейс, практика, приглашение, итог.
К каждому дню — формат (Reels/пост/карусель) и один хук.
Ничего не выдумывай сверх идеи. Живой русский, коротко.</code>
    <div class="ru"><b>Разбор:</b> вставляешь одну идею — получаешь готовую неделю с форматами и хуками. Собирать, а не выдумывать.</div></div>
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
 cover("Сто постов", "не спасут.", "Слабую идею не вытянет объём. Вытянет связка: одна идея на всю неделю.", "link"),
 blk("Проблема","Один пост","выстрелил.","А дальше — снова с нуля. Один раз повезло,","повторить не смог: не знаешь, почему сработало.","redo"),
 blk("Причина","Удача не","масштабируется.","Отдельные хиты не складываются в результат.","Повторяемость даёт не талант, а система.","sys"),
 blk("Ошибка","Ты ищешь","семь тем.","А нужна одна. Каждый день новая тема — это хаос.","Сила не в количестве, а в глубине одной идеи.","fork"),
 roles_slide(),
 example_slide(),
 prompt_slide(),
 cta("Собери","связку.",
     ["<b>одна идея</b> → семь дней → ноль паники по утрам",
      "шаблон связки и лист самооценки недели — в тетради",
      "разложи свою идею за один вечер"],
     "Тетрадь → t.me/AlovLab"),
]

HTML = f"""<title>Связка недели · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 7 · 10 августа · showcase-стиль</span>
    <h1>Одним постом: обложка → проблема → 7 ролей → пример → промпт → CTA. Instagram и Telegram, 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
