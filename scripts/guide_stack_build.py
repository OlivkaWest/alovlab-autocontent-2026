# -*- coding: utf-8 -*-
"""AlovLab · шпаргалка-лид-магнит Дня 6 «Какая нейросеть под задачу» — компактный премиум-PDF (фикс-A4).
Пара к карусели «ChatGPT против Claude». По GLOBAL METHODOLOGY RULE (кратко): конкретный результат — карта выбора,
готовый промпт, честная разбивка сильных сторон, мост в курс + путь в команду. Честность: модели проверены 09.2026
(Claude: Opus 5, Sonnet 5, Haiku 4.5, Claude Code; ChatGPT: GPT-5.6 Sol/Luna, Deep Research), без выдуманных цифр.
Запуск: python3 scripts/guide_stack_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "stack"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-stack.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.rec{display:grid;grid-template-columns:26px 1fr;gap:12px;margin:7px 0;align-items:start}
.rec .n{width:26px;height:26px;border-radius:8px;background:#13100a;color:var(--o2);font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.prompt code{font-size:8.6pt;line-height:1.55}
table.pt{width:100%;border-collapse:collapse;margin:9px 0;font-size:9.4pt}
table.pt th{background:#13100a;color:#f0e6d8;font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;padding:9px 12px;text-align:left}
table.pt td{border:1px solid var(--line);padding:9px 12px;line-height:1.34;color:var(--ink);vertical-align:middle}
table.pt tr:nth-child(even) td{background:#faf6ef}
table.pt td.tool{font-weight:800;color:#8a4a1a}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:9px 0}
.two .col{border:1px solid var(--line);border-radius:13px;padding:14px 16px;background:#fff}
.two .col.warm{background:#fff7ef;border-color:#eccdb9}
.two .col .h{font-weight:800;font-size:11.5pt;color:var(--ink);margin-bottom:8px}
.two .col ul{margin:0;padding-left:0;list-style:none}
.two .col li{position:relative;padding:5px 0 5px 18px;font-size:9.5pt;line-height:1.38;color:var(--ink)}
.two .col li:before{content:"";position:absolute;left:0;top:11px;width:7px;height:7px;border-radius:2px;background:var(--o)}
.two .col .mdl{margin-top:9px;font-size:8.6pt;color:var(--muted);line-height:1.4}
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:15px 18px;margin:9px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12pt;color:#fff;margin-bottom:6px}
.team p{font-size:9.6pt;line-height:1.5;color:#cdbfa8}
.team .dirs{display:flex;flex-wrap:wrap;gap:6px;margin:9px 0 3px}
.team .dirs span{font-size:8.4pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:4px 10px}
.stp{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:9px 0;align-items:start;width:100%}
.stp .kk{width:22px;height:22px;border-radius:7px;background:var(--o);color:#160e07;font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center;margin-top:1px}
.stp p{font-size:9.9pt;line-height:1.45;color:var(--ink)}.stp p b{color:var(--ink)}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    mc = ' mid' if mid else ''
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{mc}">{body}</div>'
            f'<div class="pf"><span>AlovLab · какая нейросеть под задачу</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')
def head(kick,h2,lead=None):
    l=f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">Шпаргалка · День 6</div>
    <h1 style="font-weight:800;font-size:30pt;line-height:1.06;letter-spacing:-.02em;color:#fff;max-width:18ch">ChatGPT или Claude: <span style="color:var(--o2)">что выбрать под задачу.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:46ch">Хватит спорить, кто лучше. Внутри карта «задача → инструмент», правило выбора за 5 секунд и готовый промпт. Сохрани и не гадай.</p>
  </div>
</section>""")

# 02 Карта задача → инструмент
P.append(page("Карта выбора",2,
  head("Главное","Задача → кто справится лучше",
    "Сохрани эту таблицу. Дальше просто смотри в неё перед стартом.")
  + '<table class="pt"><tr><th>Твоя задача</th><th>Кто берёт</th></tr>'
    '<tr><td>Написать живой пост, статью, письмо</td><td class="tool">Claude</td></tr>'
    '<tr><td>Разобрать большой PDF, договор, отчёт</td><td class="tool">Claude</td></tr>'
    '<tr><td>Код, автоматизация, агент</td><td class="tool">Claude Code</td></tr>'
    '<tr><td>Сгенерить картинку под пост</td><td class="tool">ChatGPT</td></tr>'
    '<tr><td>Быстрый ресёрч по свежим источникам</td><td class="tool">ChatGPT · Deep Research</td></tr>'
    '<tr><td>Говорить голосом на ходу</td><td class="tool">ChatGPT</td></tr>'
    '<tr><td>Не знаешь, с чего начать</td><td class="tool">Возьми оба, сравни на своей задаче</td></tr>'
    '</table>'
  + '<p class="note">Это не «кто круче». Это «что ты делаешь прямо сейчас». Инструмент — под задачу, не наоборот.</p>'
, mid=True))

# 03 Честная разбивка сильных сторон
P.append(page("Сильные стороны",3,
  head("Честно","У каждого своя зона")
  + '<div class="two">'
    '<div class="col warm"><div class="h">Claude берёт, когда важен текст и код</div><ul>'
    '<li>Длинные документы и файлы — держит нить</li>'
    '<li>Живой текст, не пахнет нейросетью</li>'
    '<li>Код и агенты — собирает проект по папке</li>'
    '<li>Аккуратно идёт по инструкции</li></ul>'
    '<div class="mdl">Модели: Opus 5 под сложное, Sonnet 5 на каждый день, Haiku 4.5 когда нужно быстро.</div></div>'
    '<div class="col"><div class="h">ChatGPT берёт, когда нужен весь набор</div><ul>'
    '<li>Картинки прямо в чате</li>'
    '<li>Голосовой режим — говоришь, отвечает</li>'
    '<li>Deep Research и веб по свежим источникам</li>'
    '<li>Огромная экосистема и привычка</li></ul>'
    '<div class="mdl">Флагман GPT-5.6 (Sol), на бесплатном — Luna.</div></div>'
    '</div>'
  + '<p class="note">Оба сильные. Проигрывает не тот, кто выбрал «не ту» нейросеть, а тот, кто берёт одну на всё.</p>'
, mid=True))

# 04 Правило задачи + промпт
P.append(page("Правило задачи",4,
  head("Метод","Выбор за 5 секунд",
    "Не «какая нейросеть лучше», а «какая под ЭТУ задачу». Три шага.")
  + '<div class="stp"><div class="kk">1</div><p><b>Назови задачу.</b> Одним предложением: что нужно на выходе.</p></div>'
  + '<div class="stp"><div class="kk">2</div><p><b>Определи тип.</b> Текст, код, картинка, поиск или голос.</p></div>'
  + '<div class="stp"><div class="kk">3</div><p><b>Возьми из карты.</b> Открой стр. 2 и бери инструмент под тип.</p></div>'
  + '<div class="prompt"><div class="plbl"><span class="tag">Промпт · Claude/ChatGPT</span><span class="copy">скопировать</span></div>'
    '<code>Вот моя задача: [ЗАДАЧА].\n'
    'Скажи честно: ты сильна в ней или лучше взять другой инструмент.\n'
    'Если да, сделай. Если нет, скажи чем и почему.</code>'
    '<div class="ru"><b>Зачем:</b> сам инструмент подскажет, его это работа или нет. Экономит время на угадывании.</div></div>'
, mid=True))

# 05 Курс + путь в команду
P.append(page("Дальше",5,
  head("Продолжение","Здесь карта. На курсе — система",
    "Шпаргалка помогает выбрать. Курс учит собирать из нейросетей рабочий стек под свои задачи.")
  + '<div class="callout result"><div class="h">Курс «Нейросети и ChatGPT для каждого»</div><p>Не одна модель, а система: где текст, где код, где картинка, где поиск. Учим собирать контент и рабочие процессы на нейросетях, а не заучивать кнопки.</p></div>'
  + '<div class="team"><div class="h">Навык может стать профессией</div>'
    '<p>Сильных студентов хотим видеть рядом. Выбираешь направление, набираешь реальные навыки, собираешь портфолио на настоящих задачах.</p>'
    '<div class="dirs"><span>AI Marketing</span><span>SMM + AI</span><span>AI Content</span><span>Prompt Engineering</span><span>AI Video</span><span>AI Agents</span></div>'
    '<p style="margin-top:8px">Лучших и наиболее активных студентов мы рассматриваем для участия в проектах AlovLab и совместной работы. Без обещаний «всем гарантированно» — по навыку и результату.</p></div>'
))

# 06 Финал
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:24pt;line-height:1.14;margin:18px 0 8px">Сохрани карту.<br><span style="color:var(--o2)">Перестань спорить.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Инструмент — под задачу, не наоборот. А как собрать из нейросетей рабочий стек, разбираем на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Бриф → @alovlab</span>
  </div>
</section>""")

html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(P)}</body></html>"
OUT.write_text(html, encoding="utf-8")
print(f"HTML: {OUT} {len(html.encode('utf-8'))//1024} KB | pages: {len(P)}")
