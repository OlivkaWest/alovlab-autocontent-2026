# -*- coding: utf-8 -*-
"""AlovLab · День 8 «Один запрос — два ответа» (бриф для ИИ) в SHOWCASE-стиле.
Обложка → проблема → причина → ошибка → бриф (3 части) → было/стало → промпт → CTA. Нумерация N/8.
RU кроме AlovLab. Запуск: python3 scripts/carousel_showcase_day8.py"""
import pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, icon, ICONS, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-08-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-08-showcase.html"

EXTRA = r"""
.hsm .head h2{font-size:37px}
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
/* список из 3 частей брифа */
.mlist{position:relative;z-index:4;margin-top:18px;display:flex;flex-direction:column;gap:11px}
.mrow{display:flex;align-items:center;gap:14px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:14px;padding:14px 16px}
.mrow .n{flex:0 0 auto;width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:14px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o))}
.mrow .t{display:flex;flex-direction:column;gap:2px;min-width:0}
.mrow .t b{font-weight:700;font-size:17px;color:#fff;line-height:1.15}
.mrow .t span{font-weight:500;font-size:13px;color:#8a8177;line-height:1.25}
/* до/после сплит */
.split{position:relative;z-index:4;margin-top:16px;display:flex;flex-direction:column;gap:12px}
.sfact{font-weight:600;font-size:14px;color:#b9ad9b;line-height:1.35}
.sfact b{color:#fff}
.scard{border-radius:14px;padding:14px 16px;position:relative}
.scard .lab{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.09em;text-transform:uppercase;padding:4px 9px;border-radius:6px;margin-bottom:8px}
.scard .q{font-weight:700;font-size:15.5px;line-height:1.3}
.scard .r{margin-top:6px;font-weight:500;font-size:12px;line-height:1.3}
.scard.cold{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1)}
.scard.cold .lab{background:rgba(255,255,255,.1);color:#9a9084}.scard.cold .q{color:#8f867b}.scard.cold .r{color:#6f675d}
.scard.hot{background:#130c06;border:1px solid rgba(255,150,80,.32);border-left:3px solid var(--o)}
.scard.hot .lab{background:linear-gradient(150deg,var(--o2),var(--o));color:#160e07}.scard.hot .q{color:#fff}.scard.hot .r{color:#c7a184}
"""
CSS = CSS0 + EXTRA

ICONS.update({
 "split": '<rect x="20" y="24" width="60" height="52" rx="9" fill="none" stroke="url(#ig)" stroke-width="6"/><path d="M50 24v52" stroke="url(#ig)" stroke-width="6"/>',
 "stamp": '<rect x="24" y="30" width="52" height="8" rx="4"/><rect x="24" y="46" width="52" height="8" rx="4"/><rect x="24" y="62" width="34" height="8" rx="4"/>',
 "mind":  '<path d="M30 82V56a20 20 0 0 1 40 0v26" fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/><circle cx="44" cy="52" r="3.4"/><circle cx="58" cy="52" r="3.4"/><path d="M45 65h12" stroke="url(#ig)" stroke-width="5" stroke-linecap="round"/>',
 "fork":  '<circle cx="50" cy="74" r="6"/><path d="M50 68V54" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/><path d="M50 54 28 32M50 54 72 32" fill="none" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/>',
})

def cover(hw, ho, sub, ic):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb big">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">AlovLab · как ставить задачу ИИ</span><span class="pg">1<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
  {FOOT}
</article>"""

def blk(eb, hw, ho, bl, bm, ic, pg):
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings">{rings()}</div><div class="orbw"><div class="orb">{icon(ic)}</div></div></div>
  <div class="top"><span class="eb">{eb}</span><span class="pg">{pg}<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="body"><span class="l">{bl}</span> <span class="m">{bm}</span></div>
  {FOOT}
</article>"""

BRIEF = [
 ("1","Контекст","кто ты, для кого, что за продукт"),
 ("2","Роль","кем должен быть ИИ: редактор, стратег"),
 ("3","Критерий","что считать хорошим и что запрещено"),
]
def brief_slide():
    rows="".join(f'<div class="mrow"><div class="n">{n}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>'
                 for n,t,s in BRIEF)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Решение</span><span class="pg">5<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Бриф — это</span><span class="o">три вещи.</span></h2></div>
  <div class="mlist">{rows}</div>
  {FOOT}
</article>"""

def demo_slide():
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">До / после</span><span class="pg">6<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Тот же запрос —</span><span class="o">другой ответ.</span></h2></div>
  <div class="split">
    <div class="sfact"><b>Задача:</b> «Напиши пост про новое меню».</div>
    <div class="scard cold"><span class="lab">Голый запрос</span><div class="q">«Мы рады представить наше новое меню»</div><div class="r">Модель заткнула пустоту самым средним. Картон.</div></div>
    <div class="scard hot"><span class="lab">Запрос + бриф</span><div class="q">Пасту крутят в круге пекорино при госте → бронь столика</div><div class="r">Тот же ИИ. Появились контекст, роль и критерий.</div></div>
  </div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт</span><span class="pg">7<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Шаблон</span><span class="o">брифа.</span></h2></div>
  <div class="pu">Польза · блогер · эксперт · SMM · бизнес</div>
  <div class="pbox"><span class="tag">Claude / ChatGPT</span><code>Контекст: ты [РОЛЬ] для [БИЗНЕС]. Аудитория: [КТО].
Продукт: [ЧТО], деталь: [ФИШКА].
Задача: [ЧТО НАПИСАТЬ].
Критерий: один хук, одна деталь, живой язык.
Запрещено: «мы рады», штампы, вода. Финал — [ДЕЙСТВИЕ].</code>
    <div class="ru"><b>Разбор:</b> три строки сверху над задачей — контекст, роль, критерий. Меняют не модель, а качество ответа.</div></div>
  {FOOT}
</article>"""

def cta(hw, ho, items, btn):
    lis="".join(f'<div class="li"><i></i><span>{t}</span></div>' for t in items)
    return f"""<article class="slide cta">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings" style="top:120%">{rings()}</div></div>
  <div class="top"><span class="eb">Дальше</span><span class="pg">8<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="clist">{lis}</div>
  <div class="btn">{btn}</div>
  {FOOT}
</article>"""

SLIDES = [
 cover("Один запрос —", "два ответа.", "Слева картон, справа живой текст. Модель одна и та же. Разницу делает бриф.", "split"),
 blk("Проблема","Просишь","«напиши пост».","А получаешь картон: «мы рады представить","наше новое меню» — так ИИ отвечает на голую строку.","stamp", 2),
 blk("Причина","ИИ не читает","мысли.","Нишу, гостя, тон, продукт ты держишь в голове.","ИИ их не видит — и затыкает пустоту средним.","mind", 3),
 blk("Ошибка","Ты меняешь","модель.","А менять надо бриф. Слабый ответ —","это слабо поставленная задача, а не слабый ИИ.","fork", 4),
 brief_slide(),
 demo_slide(),
 prompt_slide(),
 cta("Добавь","три строки.",
     ["<b>не переписывай</b> задачу — допиши сверху 3 строки",
      "контекст · роль · критерий — и отправь заново",
      "формула и шаблон под нишу — в тетради"],
     "Тетрадь → t.me/AlovLab"),
]

HTML = f"""<title>Один запрос — два ответа · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 8 · 11 августа · showcase-стиль</span>
    <h1>Одним постом: обложка → проблема → бриф (3 части) → было/после → промпт → CTA. Instagram и Telegram, 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
