# -*- coding: utf-8 -*-
"""AlovLab · методичка «99 команд ChatGPT для продаж, маркетинга и роста бизнеса» (премиум-PDF, фикс-A4).
Продолжение карусели content/carousels/chatgpt-99: полный рабочий движок команд + весь список 99 как
живой справочник. По GLOBAL-METHODOLOGY-RULE: реальный workflow, мастер-промпт с переменными,
разбор good/bad, честность про природу «команд» в ChatGPT, ACTION BLOCK, мост в курс, «Путь в команду».
Запуск: python3 scripts/guide_chatgpt99_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "chatgpt-99"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-chatgpt-99-commands.html"

EXTRA = r"""
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.3pt;line-height:1.4;color:var(--ink);margin-top:3px;max-width:none}
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:16px 19px;margin:10px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12.5pt;color:#fff;margin-bottom:6px}.team p{font-size:9.8pt;line-height:1.5;color:#cdbfa8;max-width:none}
.team .dirs{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 3px}
.team .dirs span{font-size:8.4pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:4px 10px}
table.ref{width:100%;border-collapse:separate;border-spacing:0;margin:9px 0;font-size:9pt;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
table.ref th{background:var(--ink);color:#fff;font-weight:800;text-transform:uppercase;letter-spacing:.04em;font-size:7.4pt;text-align:left;padding:8px 10px}
table.ref td{padding:6.5px 10px;border-top:1px solid var(--line2);color:var(--body);vertical-align:top;line-height:1.3}
table.ref td b{color:var(--ink)}
table.ref td code{font-family:ui-monospace,Menlo,monospace;font-size:8.3pt;color:#8a5a2a}
table.ref tr:nth-child(even) td{background:#fbf7f0}
.pill{display:inline-block;font-weight:700;font-size:8pt;color:#fff;background:var(--o);border-radius:20px;padding:3px 10px;margin:0 6px 6px 0}
.tier{border:1px solid var(--line);border-radius:12px;padding:11px 14px;background:#fff;margin:7px 0}
.tier .th2{display:flex;justify-content:space-between;align-items:baseline}
.tier .tn{font-weight:800;font-size:10.5pt;color:var(--ink)}
.tier .tp{font-weight:800;font-size:10.5pt;color:var(--o)}
.tier p{font-size:9.3pt;color:var(--muted);margin:3px 0 0;max-width:none}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · 99 команд ChatGPT</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None):
    r = f'<div class="ru">{ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{r}</div>')

def reftable(rows):
    trs = "".join(f'<tr><td style="width:34px"><b>{n}</b></td><td style="width:230px"><code>{c}</code></td><td>{d}</td></tr>' for n, c, d in rows)
    return f'<table class="ref"><tr><th>№</th><th>Команда</th><th>Что даёт</th></tr>{trs}</table>'

P = []

# 01 Cover
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:absolute;right:6%;top:20%;width:52%;color:#ffb98a;font-family:ui-monospace,monospace;font-size:9pt;line-height:1.9">
     &gt; /marketingstrategy<br>&gt; /leadmagnet<br>&gt; /objectionhandler<br><span style="color:var(--o2)">&gt; 99 команд ✓</span>
  </div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · рабочий справочник</div>
    <h1 style="font-weight:800;font-size:29pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:17ch">99 команд ChatGPT для продаж, маркетинга и роста бизнеса</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Не список идей для вдохновения. Рабочий движок: как превратить любую из 99 команд в готовый промпт под свой бизнес — и полный справочник, чтобы не листать карусель в поиске нужной.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Универсальный промпт-движок</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 разбора до/после</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Все 99 команд по 9 блокам</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("01","Что такое эти «команды»","03"),("02","Как включить команду за 3 шага","04"),
 ("03","Универсальный промпт-движок","05"),("04","Уровни: Быстрый / Про / Advanced","06"),
 ("05","Разбор: /marketingstrategy","07"),("06","Разбор: /leadmagnet","08"),
 ("07","Разбор: /objectionhandler","09"),("08","Как встроить в неделю","10"),
 ("09","Плохо vs хорошо","11"),("10","Частые ошибки","12"),
 ("11","Карта 9 блоков","13"),("12","Блок 1 · Стратегия продаж и маркетинга","14"),
 ("13","Блок 2 · Клиенты и аудитория","15"),("14","Блок 3 · Бренд и позиционирование","16"),
 ("15","Блок 4 · Контент и соцсети","17"),("16","Блок 5 · Копирайтинг и реклама","18"),
 ("17","Блок 6 · Лидогенерация и продажи","19"),("18","Блок 7 · Психология продаж","20"),
 ("19","Блок 8 · Удержание клиентов и рост","21"),("20","Блок 9 · Аналитика и рост","22"),
 ("21","Сделай сейчас + проверка","23"),("22","Дальше — на курсе","24"),
 ("23","Путь в команду AlovLab","25"),("24","Контакты","26"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:10px;padding:5.5px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:9pt;width:22px">{a}</span>'
               f'<span style="font-weight:600;font-size:9.7pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:9pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Маршрут справочника</h1>'
    '<p class="lead">24 страницы: от того, как в принципе работают такие команды в ChatGPT, до полного списка всех 99 по блокам.</p>'
    f'<div style="margin-top:2px">{rows}</div>'))

# 03 honesty about commands
P.append(page("Шаг 01 · Суть", 3,
    head("Шаг 01", "Что такое эти «команды» на самом деле",
         "Важно сразу договориться о честности: это не встроенная функция ChatGPT. Это твоя личная библиотека промптов.")
    + '<p>ChatGPT не «знает» слово <code style="font-family:ui-monospace,monospace">/marketingstrategy</code> само по себе. Каждая команда в этом справочнике — короткое имя для конкретной рабочей задачи. Ты либо расшифровываешь её сам при каждом обращении, либо один раз настраиваешь чат так, чтобы он понимал сокращения.</p>'
    + '<div class="cards c2">'
      '<div class="card"><div class="ct">Так честно</div><div class="ch">Команда = ярлык задачи</div><p>Имя вроде «/leadmagnet» экономит тебе время на формулировку — ты сразу знаешь, какой результат просить.</p></div>'
      '<div class="card"><div class="ct">Так нечестно</div><div class="ch">«ChatGPT понимает 99 команд»</div><p>Нет встроенного списка команд ChatGPT. Работает промпт, который ты формулируешь по формуле ниже.</p></div></div>'
    + '<p class="note">Дальше в справочнике — как сделать так, чтобы имя команды реально запускало нужный результат, без путаницы.</p>'))

# 04 setup
P.append(page("Шаг 02 · Настройка", 4,
    head("Шаг 02", "Как включить любую команду за 3 шага",
         "Два рабочих способа — выбери свой уровень удобства.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Способ А — без настройки.</b> Каждый раз, когда хочешь использовать команду, бери её строку из справочника (блоки на стр. 14–22) и вставляй в чат вместе с промпт-движком со стр. 05. Работает сразу, в любом чате.</div></div>'
      '<div class="step"><div class="sx"><b>Способ Б — один раз настроить.</b> В ChatGPT открой Project (или Custom Instructions) и вставь туда весь список команд из этого справочника как «словарь». Дальше просто пишешь короткое имя команды и свой контекст — ChatGPT сам находит нужную строку в инструкциях.</div></div>'
      '<div class="step"><div class="sx"><b>Проверка.</b> Напиши в чат имя любой команды без контекста. Если модель уточняет: «для какого бизнеса и с какой целью?» — настройка сработала правильно, она ждёт твои данные, а не выдумывает их сама.</div></div></div>'
    + '<div class="term"><b>Важно.</b> <span>Если ChatGPT отвечает на голую команду сразу готовым текстом без единого уточняющего вопроса — он, скорее всего, придумал контекст сам. Такой ответ надо перепроверять, а не использовать как есть.</span></div>'))

# 05 engine
engine = ("Действуй как [РОЛЬ: маркетолог / копирайтер / специалист по продажам — выбери под задачу].\n\n"
"Команда: [/КОМАНДА, например /marketingstrategy].\n"
"Задача команды: [что должна дать команда — бери формулировку из справочника, стр. 14-22].\n\n"
"Контекст моего бизнеса:\n"
"— Ниша и продукт: [...]\n"
"— Целевая аудитория: [...]\n"
"— Тон коммуникации: [...]\n"
"— Что уже пробовал и не сработало (если есть): [...]\n\n"
"Формат ответа: [список / таблица / пошаговый план].\n"
"Ограничение: не выдумывай цифры, кейсы и факты, которых я не давал. Если данных не хватает — спроси, не додумывай.")
P.append(page("Шаг 03 · Движок", 5,
    head("Шаг 03", "Универсальный промпт-движок",
         "Одна формула открывает любую из 99 команд. Меняешь только команду и контекст, структуру — нет.")
    + prompt("Промпт-движок · СКОПИРОВАТЬ", engine)
    + '<p class="note">Строка «Ограничение» в конце — не формальность. Она прямо просит модель не подменять твои реальные данные выдумкой, и это работает в подавляющем большинстве случаев.</p>'))

# 06 levels
P.append(page("Шаг 04 · Уровни", 6,
    head("Шаг 04", "Быстрый / Про / Advanced",
         "Одна и та же команда даёт разную глубину в зависимости от того, сколько контекста ты вложил.")
    + '<div class="tier"><div class="th2"><span class="tn">Быстрый</span><span class="tp">1 минута</span></div><p>Только команда + одна строка контекста («для стоматологической клиники»). Годится для черновика, который сам доработаешь.</p></div>'
    + '<div class="tier"><div class="th2"><span class="tn">Про</span><span class="tp">5 минут</span></div><p>Полный промпт-движок со стр. 05, все поля заполнены. Готовый рабочий результат, не черновик.</p></div>'
    + '<div class="tier"><div class="th2"><span class="tn">Advanced</span><span class="tp">15+ минут</span></div><p>Про-уровень + диалог: просишь 2–3 варианта, сравниваешь, уточняешь тон и формат, потом фиксируешь финальную версию.</p></div>'
    + '<p>Для ежедневной рутины хватает «Быстрого». Для текста, который пойдёт клиенту или в рекламу, — минимум «Про».</p>'))

# 07 worked example 1
P.append(page("Шаг 05 · Разбор", 7,
    head("Шаг 05", "Разбор: /marketingstrategy",
         "Блок 1, команда №1. Пример — иллюстративный, не реальный кейс клиента.")
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Движок со стр. 05 + «Ниша: небольшая кофейня в спальном районе. Аудитория: жители района 25–45 лет. Цель: стабильный поток по будням днём. Тон: тёплый, без формализма.»</p></div>'
      '<div class="c out"><b>Что получить</b><p>Структуру стратегии: 3–4 направления (соцсети района, партнёрство с офисами рядом, программа лояльности, будничные акции), под каждое — конкретный первый шаг на неделю.</p></div></div>'
    + '<div class="gb"><div class="box bad"><div class="lbl">Плохо</div>Просто написать «/marketingstrategy» без контекста. Получишь общие фразы про «SMM и таргет», подходящие любому бизнесу и никакому конкретно.</div>'
      '<div class="box good"><div class="lbl">Хорошо</div>Заполненный движок с реальными деталями ниши и аудитории. Стратегия сразу привязана к спальному району и будничному трафику, а не абстрактна.</div></div>'))

# 08 worked example 2
P.append(page("Шаг 06 · Разбор", 8,
    head("Шаг 06", "Разбор: /leadmagnet",
         "Блок 6, команда №58. Показывает, как одна и та же команда меняется под уровень «Про».")
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Движок + «Продукт: онлайн-курс по фотографии для начинающих. Аудитория: те, кто купил телефон с хорошей камерой, но снимает на авто. Тон: простой, без снобизма.»</p></div>'
      '<div class="c out"><b>Что получить</b><p>2–3 варианта лид-магнита с заголовком и структурой (например: короткий гайд «5 настроек телефона, которые меняют фото» с чек-листом внутри) — не абстрактная идея, а то, что реально можно собрать за вечер.</p></div></div>'
    + '<p class="note">Если ответ предлагает лид-магнит «для широкой аудитории фотографов» — контекста было мало. Добавь ограничение аудитории и попроси переформулировать именно под новичков с телефоном.</p>'))

# 09 worked example 3
P.append(page("Шаг 07 · Разбор", 9,
    head("Шаг 07", "Разбор: /objectionhandler",
         "Блок 7, команда №67. Здесь особенно важно ограничение «не выдумывай» — возражения должны быть твои реальные.")
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Движок + «Продукт: курс английского для взрослых. Реальные возражения, которые слышу: дорого, уже пробовал — не получилось, нет времени.»</p></div>'
      '<div class="c out"><b>Что получить</b><p>Ответ на каждое из твоих трёх возражений отдельно, без общих формулировок «просто предложите скидку» — конкретные фразы, которые можно сказать клиенту голосом.</p></div></div>'
    + '<div class="term"><b>Важно.</b> <span>Перечисли модели именно свои реальные возражения от клиентов, не проси её «придумать возможные возражения» — иначе получишь список из учебника, а не то, что реально мешает твоим продажам.</span></div>'))

# 10 weekly workflow
P.append(page("Шаг 08 · Ритм", 10,
    head("Шаг 08", "Как встроить в неделю",
         "99 команд — это не «сделать всё сразу». Рабочий ритм на пробу, можно менять под себя.")
    + '<table class="ref"><tr><th>День</th><th>Блок</th><th>Зачем</th></tr>'
      '<tr><td><b>Понедельник</b></td><td>Блок 1 · Стратегия</td><td>Смотришь на неделю целиком, а не тушишь пожары</td></tr>'
      '<tr><td><b>Вторник</b></td><td>Блок 4 · Контент</td><td>Готовишь публикации на несколько дней вперёд</td></tr>'
      '<tr><td><b>Среда</b></td><td>Блок 5 · Копирайтинг</td><td>Тексты для рекламы и рассылок на неделю</td></tr>'
      '<tr><td><b>Четверг</b></td><td>Блок 6 · Лидогенерация</td><td>Холодные касания, follow-up по текущим лидам</td></tr>'
      '<tr><td><b>Пятница</b></td><td>Блок 9 · Аналитика</td><td>Смотришь, что сработало, планируешь следующую неделю</td></tr></table>'
    + '<p class="note">Блоки 2, 3, 7, 8 — не еженедельные, а «по случаю»: новый продукт, сложный клиент, спад продаж. Держи их под рукой, а не в расписании.</p>'))

# 11 good/bad general
P.append(page("Шаг 09 · Как просить", 11,
    head("Шаг 09", "Плохо против хорошо",
         "Разница не в длине команды, а в том, сколько твоего реального контекста в неё вложено.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Плохо</div>«/salescopy для моего продукта.» Ни ниши, ни аудитории, ни тона. ChatGPT либо спросит уточнения, либо (что хуже) сам придумает несуществующий продукт и напишет текст под него.</div>'
      '<div class="box good"><div class="lbl">Хорошо</div>Движок со стр. 05, все поля заполнены реальными данными, плюс прямое ограничение не выдумывать факты. Результат сразу привязан к твоему бизнесу.</div></div>'
    + '<p>Команда — это не заклинание. Это напоминание тебе самому, какую именно задачу сейчас решаешь, чтобы не формулировать промпт с нуля каждый раз.</p>'))

# 12 errors
P.append(page("Шаг 10 · Ошибки", 12,
    head("Шаг 10", "Частые ошибки",
         "Пять граблей, которые встречаются чаще всего у тех, кто впервые работает со справочником такого размера.")
    + '<div class="fix">'
      '<div class="r"><b>Команда без контекста.</b> Фикс: всегда движок со стр. 05, даже на «Быстром» уровне — минимум одна строка про бизнес.</div>'
      '<div class="r"><b>Слепое доверие цифрам в ответе.</b> Если ChatGPT называет конкретные проценты конверсии или суммы — это гипотеза, не факт. Проверяй по своим реальным данным.</div>'
      '<div class="r"><b>Использование одного и того же ответа для разных сегментов аудитории.</b> Фикс: для каждого сегмента — свой прогон команды с уточнённым контекстом.</div>'
      '<div class="r"><b>Пропуск блока 9 (Аналитика).</b> Без него не видно, что из остальных 88 команд реально сработало.</div>'
      '<div class="r"><b>Попытка применить все 99 команд за один день.</b> Фикс: ритм со стр. 10, не марафон.</div></div>'))

# 13 map of 9 blocks
blocks_overview = [
    ("1", "Стратегия продаж и маркетинга", "Фундамент твоего роста", "01–11"),
    ("2", "Клиенты и аудитория", "Пойми, для кого ты делаешь", "12–22"),
    ("3", "Бренд и позиционирование", "Стань заметным", "23–33"),
    ("4", "Контент и соцсети", "Делай контент, который работает", "34–44"),
    ("5", "Копирайтинг и реклама", "Слова, которые продают", "45–55"),
    ("6", "Лидогенерация и продажи", "Привлекай, общайся, закрывай", "56–66"),
    ("7", "Психология продаж и возражения", "Понимай людей — продавай легче", "67–77"),
    ("8", "Удержание клиентов и рост", "Расти на длинной дистанции", "78–88"),
    ("9", "Аналитика и продвинутый рост", "Принимай решения на данных", "89–99"),
]
btrs = "".join(f'<tr><td style="width:26px"><b>{n}</b></td><td>{t}<br><span style="color:var(--muted);font-size:8.3pt">{k}</span></td><td style="width:70px"><b>{r}</b></td></tr>' for n,t,k,r in blocks_overview)
P.append(page("Карта · Обзор", 13,
    head("Карта", "9 блоков, 99 команд",
         "Ниже — полный справочник по блокам. Каждая страница дальше разбирает один блок целиком.")
    + f'<table class="ref"><tr><th>№</th><th>Блок</th><th>Команды</th></tr>{btrs}</table>'
    + '<p class="note">Порядок блоков соответствует карусели: от стратегии и понимания клиента к аналитике и масштабированию.</p>'))

BLOCKS = [
    dict(title="Блок 1 · Стратегия продаж и маркетинга", kicker="Фундамент твоего роста", tagline="Стратегия превращает идеи в деньги.", rows=[
        (1,"/marketingstrategy","Полная маркетинговая стратегия"),(2,"/salesstrategy","Стратегия продаж"),
        (3,"/growthstrategy","Стратегия роста бренда"),(4,"/marketingplan","Пошаговый маркетинговый план"),
        (5,"/salesplan","План продаж"),(6,"/goToMarket","Вывод продукта на рынок"),
        (7,"/campaignplanner","План маркетинговой кампании"),(8,"/launchplan","Запуск продукта или услуги"),
        (9,"/growthhack","Креативные возможности для роста"),(10,"/marketingaudit","Аудит маркетинга"),
        (11,"/salesfunnel","Воронка продаж")]),
    dict(title="Блок 2 · Клиенты и аудитория", kicker="Пойми, для кого ты делаешь", tagline="Лучший маркетинг — это понимание людей.", rows=[
        (12,"/customeravatar","Портрет идеального клиента"),(13,"/buyerpersona","Образ покупателя"),
        (14,"/audienceinsight","Анализ потребностей аудитории"),(15,"/painpoints","Главные боли клиентов"),
        (16,"/buyermotivation","Что мотивирует покупать"),(17,"/customerjourney","Путь клиента"),
        (18,"/customerneeds","Неудовлетворённые потребности"),(19,"/objectionfinder","Типичные возражения"),
        (20,"/customerpsychology","Психология решений"),(21,"/segment","Разделение на сегменты"),
        (22,"/targeting","На какую аудиторию целиться")]),
    dict(title="Блок 3 · Бренд и позиционирование", kicker="Стань заметным", tagline="Сильный бренд притягивает клиентов.", rows=[
        (23,"/brandpositioning","Позиционирование бренда"),(24,"/valueproposition","Ценностное предложение"),
        (25,"/usp","Уникальное торговое предложение"),(26,"/brandvoice","Голос бренда"),
        (27,"/brandmessage","Главное сообщение"),(28,"/brandstory","История бренда"),
        (29,"/competitorpositioning","Позиционирование на фоне конкурентов"),(30,"/differentiator","Чем ты отличаешься"),
        (31,"/tagline","Обещание бренда"),(32,"/elevatorpitch","Маркетинговые слоганы"),
        (33,"/elevatorpitch","30-секундная презентация")]),
    dict(title="Блок 4 · Контент и соцсети", kicker="Делай контент, который работает", tagline="Контент — это внимание. А внимание — продажи.", rows=[
        (34,"/contentstrategy","Контент-стратегия"),(35,"/contentcalendar","Контент-план на 30 дней"),
        (36,"/socialstrategy","Стратегия постов"),(37,"/reelideas","Идеи коротких видео"),
        (38,"/postideas","Идеи вовлекающих постов"),(39,"/carousel","Обучающая карусель"),
        (40,"/hook","Цепляющие хуки"),(41,"/caption","Продающие подписи"),
        (42,"/contentrepurpose","Перепаковка контента"),(43,"/viralcontent","Идеи вирусного контента"),
        (44,"/engagement","Повышение вовлечённости")]),
    dict(title="Блок 5 · Копирайтинг и реклама", kicker="Слова, которые продают", tagline="Правильные слова = больше клиентов.", rows=[
        (45,"/adcopy","Убедительный рекламный текст"),(46,"/facebookad","Реклама для Facebook"),
        (47,"/googlead","Варианты объявлений"),(48,"/instagramad","Реклама для Instagram"),
        (49,"/landingpage","Текст для лендинга"),(50,"/headline","Сильные заголовки"),
        (51,"/salescopy","Продающий текст"),(52,"/emailcopy","Маркетинговые письма"),
        (53,"/productcopy","Описания продуктов"),(54,"/calltoaction","Мощные призывы к действию"),
        (55,"/abtestcopy","A/B варианты текстов")]),
    dict(title="Блок 6 · Лидогенерация и продажи", kicker="Привлекай, общайся, закрывай", tagline="Больше разговоров. Больше возможностей.", rows=[
        (56,"/leadgen","Стратегии привлечения лидов"),(57,"/prospecting","Поиск потенциальных клиентов"),
        (58,"/leadmagnet","Неотразимый лид-магнит"),(59,"/coldemail","Холодные письма"),
        (60,"/coldcall","Скрипт холодного звонка"),(61,"/linkedinoutreach","Сообщения для LinkedIn"),
        (62,"/followup","Эффективный follow-up"),(63,"/salespitch","Питч продаж"),
        (64,"/discoverycall","Скрипт диагностического звонка"),(65,"/qualification","Квалификация клиентов"),
        (66,"/closing","Как закрывать больше сделок")]),
    dict(title="Блок 7 · Психология продаж и возражения", kicker="Понимай людей — продавай легче", tagline="Люди говорят «нет» не навсегда. Нужно просто уметь говорить с ними.", rows=[
        (67,"/objectionhandler","Ответы на возражения"),(68,"/priceobjection","Работа с ценой"),
        (69,"/trustbuilder","Повышение доверия"),(70,"/urgency","Создание срочности"),
        (71,"/scarcity","Идеи дефицита"),(72,"/socialproof","Кейсы и отзывы"),
        (73,"/persuasion","Убеждающие сообщения"),(74,"/negotiation","Стратегии переговоров"),
        (75,"/closingquestions","Вопросы для решения о покупке"),(76,"/dealrescue","Возврат «зависших» сделок"),
        (77,"/emailsequence","Автоматическая email-цепочка")]),
    dict(title="Блок 8 · Удержание клиентов и рост", kicker="Расти на длинной дистанции", tagline="Удерживать клиентов дешевле, чем искать новых.", rows=[
        (78,"/welcomeemail","Приветственные письма"),(79,"/nurture","Прогрев лидов"),
        (80,"/abandonedcart","Возврат корзины"),(81,"/upsell","Стратегии допродаж"),
        (82,"/crosssell","Кросс-продажи"),(83,"/retention","Удержание клиентов"),
        (84,"/winback","Возврат неактивных клиентов"),(85,"/referral","Реферальная программа"),
        (86,"/marketingmetrics","Ключевые KPI"),(87,"/salesmetrics","KPI продаж"),
        (88,"/conversionaudit","Аудит воронки")]),
    dict(title="Блок 9 · Аналитика и продвинутый рост", kicker="Принимай решения на данных", tagline="Используй эти команды. Строй системный рост. Действуй.", rows=[
        (89,"/roianalysis","Оценка ROI маркетинговых кампаний"),(90,"/competitoranalysis","Анализ конкурентов"),
        (91,"/swot","SWOT-анализ"),(92,"/pricingstrategy","Ценовая стратегия"),
        (93,"/conversionoptimizer","Способы повысить конверсию"),(94,"/abtest","Идеи для A/B-тестов"),
        (95,"/funneloptimizer","Поиск слабых мест в воронке"),(96,"/automation","Какие задачи можно автоматизировать"),
        (97,"/partnerships","Возможности для партнёрств"),(98,"/scalemarketing","План масштабирования"),
        (99,"/marketingmastermind","Полный план роста для бизнеса")]),
]
for i, b in enumerate(BLOCKS):
    pnum = 14 + i
    P.append(page(f"Блок {i+1} · Справочник", pnum,
        head(f"Блок {i+1}", b["title"].split(" · ",1)[1], b["kicker"])
        + reftable(b["rows"])
        + f'<p class="note">{b["tagline"]}</p>'
        + ('<p class="note">Пункты 32 и 33 — «/elevatorpitch» дважды с разными описаниями, воспроизведено как в исходном референсе, не подменено.</p>' if i == 2 else '')))

# 23 action
P.append(page("Шаг 11 · Действие", 23,
    head("Шаг 11", "Сделай сейчас",
         "Не открывай все 9 блоков сразу. Пройди с одной команды, сегодня же.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Выбери одну боль</b> из своего бизнеса прямо сейчас — например, не хватает лидов или клиенты не закрываются.</div></div>'
      '<div class="step"><div class="sx"><b>Найди подходящую команду</b> в карте на стр. 13 — по нужному блоку.</div></div>'
      '<div class="step"><div class="sx"><b>Заполни движок</b> со стр. 05 своими реальными данными, не общими фразами.</div></div>'
      '<div class="step"><div class="sx"><b>Проверь результат</b> по чек-листу ниже, прежде чем использовать его в работе.</div></div></div>'
    + '<div class="callout check"><div class="h">Проверь перед использованием</div>'
      '<div class="row">В ответе нет цифр и фактов, которые ты не давал сам.</div>'
      '<div class="row">Текст звучит как твой бизнес, а не как шаблон «для любой компании».</div>'
      '<div class="row">Ты понимаешь, почему модель предложила именно это — а не просто копируешь не глядя.</div>'
      '<div class="row">Результат можно применить сегодня, а не «когда-нибудь потом».</div></div>'))

# 24 course bridge
P.append(page("Дальше", 24,
    head("Дальше", "Одна команда — это один результат. А есть система",
         "Ты прошёл движок для одной задачи. На курсе собираешь так весь маркетинг и контент бизнеса — не только промпты.")
    + '<p>99 команд закрывают отдельные задачи: текст, стратегия, разбор аудитории. Курс «Нейросети и ChatGPT для каждого» — про то, как связать это в конвейер: тексты, изображения, видео, звук, аватары, автоматизация одной системой, а не разрозненными промптами.</p>'
    + '<div class="tier"><div class="th2"><span class="tn">МИНИ</span><span class="tp">2 999 ₽</span></div><p>1-й модуль «Земля Слов» — промпт-инжиниринг с нуля, закрытый Telegram-канал, ИИ-ассистент по курсу.</p></div>'
    + '<div class="tier"><div class="th2"><span class="tn">БАЗОВЫЙ</span><span class="tp">14 990 ₽</span></div><p>6 видеоуроков (6 «Земель»: Слова, Изображения, Видео, Звук, Аватары, Знания), Telegram-канал, обновления материалов.</p></div>'
    + '<div class="tier"><div class="th2"><span class="tn">ПРО</span><span class="tp">49 990 ₽</span></div><p>Всё из Базового + доступ навсегда, сертификат, проверка заданий, личное менторство, приватный клуб.</p></div>'
    + '<p class="note">Гарантия возврата 14 дней. Регистрация и актуальные условия — alovlab.ru.</p>'))

# 25 team
P.append(page("Команда", 25,
    head("Путь дальше", "Путь в команду AlovLab",
         "Если научился собирать сильные промпты и хочешь применять это не только для себя — есть куда расти.")
    + '<div class="team"><div class="h">Уверенно работаешь с командами из этого справочника?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты: собирают маркетинговые и контентные системы под задачи брендов, набивают портфолио на живых кейсах и растут рядом с командой.</p>'
      '<div class="dirs"><span>Маркетинг-промпты</span><span>Контент-конвейеры</span><span>Копирайтинг</span><span>Аналитика</span></div>'
      '<p style="margin-top:8px">Это работа и практика, а не обещание трудоустройства. Но дорога открыта: покажи, что доводишь результат до реального применения, а не только до черновика.</p></div>'
    + '<p>Бизнесу, которому нужна такая система под ключ — это AlovLab Studio. Отправляешь бриф, сборку промпт-системы и конвейер берём на себя.</p>'))

# 26 contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Автоконтент</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">99 команд — это движок. Система — это курс.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Курс «Нейросети и ChatGPT для каждого» — тарифы от 2 999 ₽. Нужна такая система под бизнес под ключ — отправь бриф в студию.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Начать курс · alovlab.ru</span>
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Бриф студии · @alovlab</span>
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))
