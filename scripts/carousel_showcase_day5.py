# -*- coding: utf-8 -*-
"""AlovLab · День 5 «Конфликт вместо информации» в SHOWCASE-стиле (стеклянный орб).
Обложка → проблема → причина → ошибка → 6 механик → до/после (ниша ИИ/контент) → промпт → CTA.
RU, кроме AlovLab. Примеры — в нише ИИ/контент, НЕ питание. Запуск: python3 scripts/carousel_showcase_day5.py
"""
import pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, icon, ICONS, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-05-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-05-showcase.html"

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

/* список из 6 механик */
.mch .head{margin-top:20px}
.mch .head h2{font-size:35px}
.mlist{position:relative;z-index:4;margin-top:16px;margin-bottom:6px;display:flex;flex-direction:column;gap:8px}
.mrow{display:flex;align-items:center;gap:13px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:13px;padding:10px 15px}
.mrow .n{flex:0 0 auto;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:13px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o))}
.mrow .t{display:flex;flex-direction:column;gap:1px;min-width:0}
.mrow .t b{font-weight:700;font-size:15px;color:#fff;line-height:1.15}
.mrow .t span{font-weight:500;font-size:12.5px;color:#8a8177;line-height:1.2}

/* до/после — сплит */
.split{position:relative;z-index:4;margin-top:18px;display:flex;flex-direction:column;gap:12px}
.sfact{font-weight:600;font-size:14px;color:#b9ad9b;line-height:1.35}
.sfact b{color:#fff}
.scard{border-radius:14px;padding:15px 17px;position:relative}
.scard .lab{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.09em;text-transform:uppercase;padding:4px 9px;border-radius:6px;margin-bottom:9px}
.scard .q{font-weight:700;font-size:16.5px;line-height:1.28}
.scard .r{margin-top:7px;font-weight:500;font-size:12.5px;line-height:1.3}
.scard.cold{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1)}
.scard.cold .lab{background:rgba(255,255,255,.1);color:#9a9084}
.scard.cold .q{color:#8f867b}
.scard.cold .r{color:#6f675d}
.scard.hot{background:#130c06;border:1px solid rgba(255,150,80,.32);border-left:3px solid var(--o)}
.scard.hot .lab{background:linear-gradient(150deg,var(--o2),var(--o));color:#160e07}
.scard.hot .q{color:#fff}
.scard.hot .r{color:#c7a184}
"""
CSS = CSS0 + EXTRA

# stroke-иконки под тему конфликта
ICONS.update({
 "swipe":  '<rect x="34" y="16" width="32" height="68" rx="8" fill="none" stroke="url(#ig)" stroke-width="6"/><path d="M50 64V40M41 49l9-9 9 9" fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
 "search": '<circle cx="45" cy="45" r="20" fill="none" stroke="url(#ig)" stroke-width="7"/><path d="M60 60 79 79" stroke="url(#ig)" stroke-width="8" stroke-linecap="round"/>',
 "tense":  '<circle cx="20" cy="50" r="5"/><circle cx="80" cy="50" r="5"/><path d="M20 50Q50 78 80 50" fill="none" stroke="url(#ig)" stroke-width="6"/><path d="M20 50H80" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="3" stroke-dasharray="4 6"/>',
 "collide":'<path d="M12 50h26M38 50l-10-9M38 50l-10 9" fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M88 50H62M62 50l10-9M62 50l10 9" fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="50" cy="50" r="5.5"/>',
})

def cover(hw, ho, sub, ic):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb big">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">AlovLab · как удержать внимание</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
  {FOOT}
</article>"""

def blk(num, eb, hw, ho, bl, bm, ic):
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">{eb}</span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="body"><span class="l">{bl}</span> <span class="m">{bm}</span></div>
  {FOOT}
</article>"""

MECH = [
 ("Слом убеждения", "«а разве не наоборот?»"),
 ("Цена против качества", "дорого ≠ лучше"),
 ("Хаос против системы", "не больше, а иначе"),
 ("Любитель против профи", "новичок жмёт — профи думает"),
 ("Смена точки зрения", "проблема не там, где искал"),
 ("Что теряешь из-за ошибки", "цена привычки продолжать"),
]

def mech_slide():
    rows="".join(f'<div class="mrow"><div class="n">{i}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>'
                 for i,(t,s) in enumerate(MECH,1))
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Решение · 6 механик</span></div>
  <div class="head"><h2><span class="w">Возьми факт.</span><span class="o">Добавь конфликт.</span></h2></div>
  <div class="mlist">{rows}</div>
  {FOOT}
</article>"""

def demo_slide():
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">До / после</span></div>
  <div class="head"><h2><span class="w">Один факт —</span><span class="o">два поста.</span></h2></div>
  <div class="split">
    <div class="sfact"><b>Факт:</b> нейросеть делает контент быстрее и дешевле команды.</div>
    <div class="scard cold"><span class="lab">Информация</span><div class="q">«5 нейросетей, которые ускорят твой контент»</div><div class="r">Польза есть. Человек кивает — и листает.</div></div>
    <div class="scard hot"><span class="lab">Конфликт · слом убеждения</span><div class="q">«Ты платишь дизайнеру за то, что промпт делает за вечер»</div><div class="r">Смысл тот же — но досматривают и спорят.</div></div>
  </div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт</span></div>
  <div class="head"><h2><span class="w">Промпт:</span><span class="o">конфликт из факта.</span></h2></div>
  <div class="pu">Польза · блогер · эксперт · SMM · бизнес</div>
  <div class="pbox"><span class="tag">Claude / ChatGPT</span><code>Ты редактор: превращаешь сухой факт в текст с напряжением.
Мой факт: [ФАКТ]. Во что аудитория уже верит: [УБЕЖДЕНИЕ].
Не меняя смысл, столкни факт с этим убеждением.
Дай по одной первой строке на 6 механик: слом убеждения,
цена/качество, хаос/система, любитель/профи, смена точки
зрения, цена ошибки. Живой русский, без крика. Отметь сильнейшую.</code>
    <div class="ru"><b>Разбор:</b> вставь свой факт и убеждение аудитории — получишь 6 заходов с конфликтом и сильнейший. Смысл факта не раздуваем.</div></div>
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
 cover("Полезный.", "Поэтому листают.", "Факты можно погуглить. Внимание держит не польза, а напряжение.", "swipe"),
 blk(1,"Проблема","Ты выдаёшь","факты.","Советы, списки, «5 способов». Человек кивает —","и листает дальше. Польза есть, а внимания нет.","search"),
 blk(2,"Причина","Держит не польза.","Держит напряжение.","Мозг проматывает всё, что не создаёт вопроса.","Остаётся то, что осталось незакрытым: спор, разрыв.","tense"),
 blk(3,"Ошибка","Ты объясняешь.","А надо — сталкивать.","Объяснение усыпляет: всё встало на полку.","Столкновение будит: две вещи не сходятся — и не уйдёшь.","collide"),
 mech_slide(),
 demo_slide(),
 prompt_slide(),
 cta("Перепиши","один пост.",
     ["<b>не пиши новый</b> — возьми старый полезный пост",
      "6 механик, пример от слабого к сильному и промпт — в тетради",
      "вынеси спор в первую строку → факт тот же, напряжение есть"],
     "Тетрадь → t.me/AlovLab"),
]

HTML = f"""<title>Конфликт вместо информации · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 5 · 8 августа · showcase-стиль</span>
    <h1>Одним постом: обложка → проблема → 6 механик → до/после → промпт → CTA. Instagram и Telegram, 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
