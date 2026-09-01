# -*- coding: utf-8 -*-
"""AlovLab · методичка Дня 6 «Какая нейросеть под задачу» — премиум-PDF (фикс-A4).
v2 (пересборка): рецепт под каждую задачу (когда→как→готовый промпт→что получишь), 5 промптов, живой пример,
плотные страницы. Пара к карусели «ChatGPT против Claude». По GLOBAL METHODOLOGY RULE.
Честность: модели проверены 09.2026 (Claude: Opus 5, Sonnet 5, Haiku 4.5, Claude Code; ChatGPT: GPT-5.6 Sol/Luna,
Deep Research), без выдуманных цифр. Запуск: python3 scripts/guide_stack_build.py"""
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
.prompt code{font-size:8.5pt;line-height:1.55}
table.pt{width:100%;border-collapse:collapse;margin:9px 0;font-size:9.4pt}
table.pt th{background:#13100a;color:#f0e6d8;font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;padding:9px 12px;text-align:left}
table.pt td{border:1px solid var(--line);padding:9px 12px;line-height:1.32;color:var(--ink);vertical-align:middle}
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
.stp{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:8px 0;align-items:start;width:100%}
.stp .kk{width:22px;height:22px;border-radius:7px;background:var(--o);color:#160e07;font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center;margin-top:1px}
.stp p{font-size:9.8pt;line-height:1.44;color:var(--ink)}.stp p b{color:var(--ink)}
.tool-tag{display:inline-block;font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:20px;padding:4px 12px;margin-bottom:6px}
.win{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:10px;padding:10px 14px;margin:9px 0}
.win b{font-weight:800;color:var(--ink);font-size:9.2pt}.win p{font-size:9.4pt;line-height:1.42;color:var(--body);margin-top:2px}
.flow{border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:9px 0;background:#fff}
.flow .r{display:grid;grid-template-columns:110px 1fr;gap:12px;padding:9px 15px;border-bottom:1px solid var(--line);align-items:baseline}
.flow .r:last-child{border-bottom:0}.flow .r.hi{background:var(--o-tint)}
.flow .r b{font-weight:800;font-size:8.2pt;letter-spacing:.03em;text-transform:uppercase;color:var(--muted)}
.flow .r.hi b{color:var(--o)}.flow .r p{font-size:9.4pt;line-height:1.38;color:var(--ink)}
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
def prompt(code,ru=None):
    ru_html=f'<div class="ru"><b>Что получишь:</b> {ru}</div>' if ru else ''
    return f'<div class="prompt"><div class="plbl"><span class="tag">Промпт · скопировать</span><span class="copy">›</span></div><code>{code}</code>{ru_html}</div>'
def recipe(section,num,tool,h2,when,steps,code,got):
    inner = (f'<span class="tool-tag">{tool}</span>'
             + f'<h2>{h2}</h2>'
             + f'<div class="win"><b>Когда:</b><p>{when}</p></div>'
             + ''.join(f'<div class="stp"><div class="kk">{i}</div><p>{s}</p></div>' for i,s in enumerate(steps,1))
             + prompt(code, got))
    return page(section,num,inner,mid=True)

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">Методичка · День 6</div>
    <h1 style="font-weight:800;font-size:30pt;line-height:1.06;letter-spacing:-.02em;color:#fff;max-width:18ch">ChatGPT или Claude: <span style="color:var(--o2)">что выбрать под задачу.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:47ch">Карта выбора, правило за 5 секунд и 5 готовых промптов под конкретные задачи: живой текст, разбор документа, код, картинка, ресёрч. Плюс живой пример от задачи до результата.</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Карта задача → инструмент</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">5 промптов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Живой пример</span>
    </div>
  </div>
</section>""")

# 02 Что ты сможешь
P.append(page("Что ты сможешь",2,
  head("Результат","К концу — не «понял разницу», а умеешь",
    "Методичка даёт не мнение «кто круче», а рабочий навык выбора и готовые промпты.")
  + '<div class="rec"><div class="n">1</div><div class="t"><b>Выбирать инструмент за 5 секунд</b><p>по карте «задача → инструмент», без споров и гадания.</p></div></div>'
  + '<div class="rec"><div class="n">2</div><div class="t"><b>5 готовых промптов</b><p>под живой текст, разбор документа, код, картинку и ресёрч. Скопировал, подставил, погнал.</p></div></div>'
  + '<div class="rec"><div class="n">3</div><div class="t"><b>Собирать связку под задачу</b><p>когда одна задача требует двух инструментов подряд (пример внутри).</p></div></div>'
  + '<p class="note">Сохрани карту на стр. 3, дальше просто открывай нужный рецепт под свою задачу.</p>'
, mid=True))

# 03 Карта
P.append(page("Карта выбора",3,
  head("Главное","Задача → кто справится лучше",
    "Сохрани таблицу. Дальше — рецепт под каждую строку.")
  + '<table class="pt"><tr><th>Твоя задача</th><th>Кто берёт</th></tr>'
    '<tr><td>Написать живой пост, статью, письмо</td><td class="tool">Claude · стр. 5</td></tr>'
    '<tr><td>Разобрать большой PDF, договор, отчёт</td><td class="tool">Claude · стр. 6</td></tr>'
    '<tr><td>Код, автоматизация, агент</td><td class="tool">Claude Code · стр. 7</td></tr>'
    '<tr><td>Сгенерить картинку под пост</td><td class="tool">ChatGPT · стр. 8</td></tr>'
    '<tr><td>Свежий ресёрч по источникам</td><td class="tool">ChatGPT · стр. 9</td></tr>'
    '<tr><td>Говорить голосом на ходу</td><td class="tool">ChatGPT</td></tr>'
    '<tr><td>Не знаешь, с чего начать</td><td class="tool">Возьми оба, сравни</td></tr>'
    '</table>'
  + '<p class="note">Это не «кто круче». Это «что ты делаешь прямо сейчас». Инструмент — под задачу, не наоборот.</p>'
))

# 04 Правило задачи
P.append(page("Правило задачи",4,
  head("Метод","Выбор за 5 секунд",
    "Не «какая нейросеть лучше», а «какая под ЭТУ задачу». Три шага.")
  + '<div class="stp"><div class="kk">1</div><p><b>Назови задачу.</b> Одним предложением: что нужно на выходе.</p></div>'
  + '<div class="stp"><div class="kk">2</div><p><b>Определи тип.</b> Текст, документ, код, картинка, поиск или голос.</p></div>'
  + '<div class="stp"><div class="kk">3</div><p><b>Возьми из карты.</b> Открой стр. 3 и иди в рецепт под свой тип.</p></div>'
  + '<div class="win"><b>Мысль:</b><p>Проигрывает не тот, кто выбрал «не ту» нейросеть, а тот, кто одну тянет на всё.</p></div>'
, mid=True))

# 05 Рецепт: живой текст → Claude
P.append(recipe("Рецепт · текст",5,"Claude","Живой текст, который читают",
  "Пост, письмо, статья, описание. Нужно, чтобы звучало по-человечески, а не как нейросеть.",
  ["Открой Claude (Sonnet 5 хватит), вставь свой черновик или тему.",
   "Дай промпт-редактор ниже, добавь, для кого текст.",
   "Получишь вариант, попроси «сделай живее и короче» ещё раз, если надо."],
  "Перепиши этот текст живой человеческой речью.\n"
  "Убери канцелярит и штампы. Короткие фразы, разный ритм,\n"
  "одна мысль на абзац. Сильное первое предложение.\n"
  "Не пиши как нейросеть, без восклицаний без причины.\n"
  "Для кого: [ЦА]. Текст: [ВСТАВЬ ТЕКСТ].",
  "чистый текст без воды и AI-штампов, готовый в пост."))

# 06 Рецепт: разбор документа → Claude
P.append(recipe("Рецепт · документ",6,"Claude","Разобрать большой документ",
  "PDF, договор, отчёт, длинная статья. Читать целиком некогда, нужна выжимка и суть.",
  ["Открой Claude, приложи файл или вставь текст документа.",
   "Дай промпт ниже, впиши свою цель (что важно найти).",
   "Уточни: «покажи 3 риска» или «сделай тезисы для поста» под задачу."],
  "Вот документ: [ПРИЛОЖИ ФАЙЛ ИЛИ ВСТАВЬ ТЕКСТ].\n"
  "Сделай выжимку под цель: [ЦЕЛЬ].\n"
  "Дай: 5 главных пунктов, что важно для цели,\n"
  "что требует решения или вызывает вопросы.\n"
  "Только по тексту. Где данных нет, так и напиши.",
  "карта документа за минуту вместо часа чтения."))

# 07 Рецепт: код/автоматизация → Claude Code
P.append(recipe("Рецепт · код",7,"Claude Code","Код и автоматизация без программиста",
  "Нужен скрипт, бот, таблица-автомат, парсер, мелкая автоматизация рутины.",
  ["Опиши задачу простыми словами, что на входе и что на выходе.",
   "Дай промпт ниже, приложи примеры данных, если есть.",
   "Проси объяснять по шагам и запускать, пока не заработает."],
  "Собери [что нужно: скрипт / бот / таблицу], который делает [ЗАДАЧА].\n"
  "На входе: [ЧТО ЕСТЬ]. На выходе нужно: [ЧТО ХОЧУ].\n"
  "Объясни по шагам, что делает код, и как это запустить.\n"
  "Я не программист, пиши понятно.",
  "рабочий инструмент под твою рутину, а не теория про код."))

# 08 Рецепт: картинка → ChatGPT
P.append(recipe("Рецепт · картинка",8,"ChatGPT","Картинка под пост прямо в чате",
  "Обложка, иллюстрация, визуал под пост. Быстро и без отдельного сервиса.",
  ["Открой ChatGPT, включи генерацию изображения.",
   "Дай промпт ниже: что, стиль, формат, настроение.",
   "Не вышло с первого раза — уточни деталь и повтори."],
  "Сгенерируй картинку: [ЧТО НА КАРТИНКЕ].\n"
  "Стиль: [например, фотореализм / минимализм].\n"
  "Формат: [9:16 / 1:1 / 4:5]. Настроение: [какое].\n"
  "Без текста на картинке, чистая композиция, место под заголовок.",
  "готовый визуал под пост, дальше добавляешь заголовок сам."))

# 09 Рецепт: ресёрч → ChatGPT Deep Research
P.append(recipe("Рецепт · ресёрч",9,"ChatGPT · Deep Research","Свежий ресёрч по источникам",
  "Собрать данные по теме, сравнить, проверить свежие факты со ссылками.",
  ["Открой ChatGPT, включи Deep Research.",
   "Дай промпт ниже, впиши тему и период.",
   "Проверь ссылки в ответе, факты без источника не бери."],
  "Собери данные по теме: [ТЕМА] за [ПЕРИОД].\n"
  "Только проверяемые источники со ссылками.\n"
  "Сведи в таблицу: факт, источник, дата.\n"
  "В конце: 3 вывода и что осталось непонятным.",
  "готовая фактура со ссылками, а не пересказ по памяти."))

# 10 Живой пример
P.append(page("Живой пример",10,
  head("Как это в жизни","Одна задача, два инструмента подряд",
    "Смотри, как правило работает, когда задача требует связки.")
  + '<div class="flow">'
    '<div class="r"><b>Задача</b><p>нужен пост про запуск + обложка к нему.</p></div>'
    '<div class="r"><b>Шаг 1 · тип</b><p>текст → это Claude. Кидаю тему, беру промпт-редактор (стр. 5).</p></div>'
    '<div class="r"><b>Получил</b><p>живой пост без канцелярита, за пару правок.</p></div>'
    '<div class="r"><b>Шаг 2 · тип</b><p>картинка → это ChatGPT. Беру промпт под визуал (стр. 8).</p></div>'
    '<div class="r"><b>Получил</b><p>обложку под пост, добавил заголовок сам.</p></div>'
    '<div class="r hi"><b>Итог</b><p>одна задача, два инструмента, каждый под свой тип. Это и есть стек.</p></div>'
    '</div>'
  + '<p class="note">Не одна нейросеть на всё, а нужная под каждый шаг. Так работает конвейер, а не «магия одной кнопки».</p>'
, mid=True))

# 11 Честная разбивка + чек
P.append(page("Сильные стороны",11,
  head("Честно","У каждого своя зона")
  + '<div class="two">'
    '<div class="col warm"><div class="h">Claude — текст, документы, код</div><ul>'
    '<li>Длинные документы и файлы — держит нить</li>'
    '<li>Живой текст, не пахнет нейросетью</li>'
    '<li>Код и агенты через Claude Code</li>'
    '<li>Аккуратно идёт по инструкции</li></ul>'
    '<div class="mdl">Opus 5 под сложное, Sonnet 5 на каждый день, Haiku 4.5 когда быстро.</div></div>'
    '<div class="col"><div class="h">ChatGPT — картинки, голос, поиск</div><ul>'
    '<li>Картинки прямо в чате</li>'
    '<li>Голосовой режим на ходу</li>'
    '<li>Deep Research и веб по источникам</li>'
    '<li>Огромная экосистема и привычка</li></ul>'
    '<div class="mdl">Флагман GPT-5.6 (Sol), на бесплатном — Luna.</div></div>'
    '</div>'
  + '<div class="callout check"><div class="h">Проверь себя</div>'
    '<div class="row">Назвал задачу одним предложением</div>'
    '<div class="row">Определил тип: текст / документ / код / картинка / поиск</div>'
    '<div class="row">Взял инструмент из карты, а не по привычке</div>'
    '<div class="row">Использовал готовый промпт под задачу</div></div>'
))

# 12 Курс + путь в команду
P.append(page("Дальше",12,
  head("Продолжение","Здесь рецепты. На курсе — система",
    "Методичка учит выбирать под задачу. Курс — собирать из этого рабочий конвейер.")
  + '<div class="callout result"><div class="h">Курс «Нейросети и ChatGPT для каждого»</div><p>Не одна модель, а система: где текст, где код, где картинка, где поиск. Собираем контент и рабочие процессы на нейросетях от идеи до публикации, а не заучиваем кнопки.</p></div>'
  + '<div class="team"><div class="h">Навык может стать профессией</div>'
    '<p>Сильных студентов хотим видеть рядом. Выбираешь направление, набираешь реальные навыки, собираешь портфолио на настоящих задачах.</p>'
    '<div class="dirs"><span>AI Marketing</span><span>SMM + AI</span><span>AI Content</span><span>Prompt Engineering</span><span>AI Video</span><span>AI Agents</span></div>'
    '<p style="margin-top:8px">Лучших и наиболее активных студентов мы рассматриваем для участия в проектах AlovLab и совместной работы. Без обещаний «всем гарантированно» — по навыку и результату.</p></div>'
))

# 13 Финал
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
