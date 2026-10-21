# -*- coding: utf-8 -*-
"""AlovLab · методичка «Работа с Claude над Telegram-ботом» (премиум-PDF, фикс-A4).
Полный профессиональный playbook под реальный сценарий карусели «Bot Field Notes»:
бот записи на консультацию, диаграмма состояний, секреты через .env, обязательные тесты, хостинг.
По GLOBAL-METHODOLOGY-RULE: реальный workflow, мастер-промпт целиком, честность (не заявлять
непроверенную интеграцию), чек-листы, мост в курс + «Путь в команду AlovLab».
Запуск: python3 scripts/guide_tgbot_fieldnotes_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "tg-bot-fieldnotes"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-claude-bot-playbook.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.midwrap{width:100%}
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.3pt;line-height:1.4;color:var(--ink);margin-top:3px;max-width:none}
.warn{background:#13100a;border-radius:14px;padding:15px 18px;margin:10px 0;color:#f4efe6}
.warn .h{font-weight:800;font-size:10pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o2);margin-bottom:7px}
.warn ul{margin:0;padding-left:0;list-style:none}
.warn li{position:relative;padding:4px 0 4px 20px;font-size:9.5pt;line-height:1.42;color:#eae4da;max-width:none}
.warn li:before{content:"✕";position:absolute;left:0;color:var(--o2);font-weight:800}
.warn li.ok:before{content:"✔"}
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:16px 19px;margin:10px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12.5pt;color:#fff;margin-bottom:6px}.team p{font-size:9.8pt;line-height:1.5;color:#cdbfa8;max-width:none}
.team .dirs{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 3px}
.team .dirs span{font-size:8.4pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:4px 10px}
table.ref{width:100%;border-collapse:separate;border-spacing:0;margin:9px 0;font-size:9pt;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
table.ref th{background:var(--ink);color:#fff;font-weight:800;text-transform:uppercase;letter-spacing:.04em;font-size:7.4pt;text-align:left;padding:8px 10px}
table.ref td{padding:7px 10px;border-top:1px solid var(--line2);color:var(--body);vertical-align:top;line-height:1.32}
table.ref td b{color:var(--ink)}
table.ref td code{font-family:ui-monospace,Menlo,monospace;font-size:8pt;color:#8a5a2a}
table.ref tr:nth-child(even) td{background:#fbf7f0}
.filetree{background:var(--dark);border-radius:14px;padding:14px 18px;margin:10px 0;font-family:ui-monospace,Menlo,monospace;font-size:9.5pt;color:#ffd9b8;line-height:1.7}
.filetree .c{color:#8fd08a}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · работа с Claude над ботом</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None):
    r = f'<div class="ru">{ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{r}</div>')

P = []

# 01 Cover
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:absolute;right:6%;top:22%;width:52%;color:#ffb98a;font-family:ui-monospace,monospace;font-size:9pt;line-height:1.9">
     &gt; claude "собери бота"<br>&gt; /start → тема → имя<br>&gt; → контакт → заявка<br><span style="color:var(--o2)">&gt; 4 теста ✓</span>
  </div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · профессиональный playbook</div>
    <h1 style="font-weight:800;font-size:30pt;line-height:1.06;letter-spacing:-.02em;color:#fff;max-width:16ch">Работа с Claude над Telegram-ботом</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Не «напиши код». Полная дисциплина: сценарий, состояния, секреты, тесты, деплой. Разбор на реальном примере — бот записи на консультацию.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Мастер-промпт целиком</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Диаграмма состояний</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">4 обязательных теста</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("01","Что ты соберёшь","03"),("02","Модель: кто кому отвечает","04"),
 ("03","Сценарий: одно действие на шаг","05"),("04","Диаграмма состояний","06"),
 ("05","Мастер-промпт целиком","07"),("06","Анатомия хорошего промпта","08"),
 ("07","Что должен отдать Claude","09"),("08","Секреты: токен и .env","10"),
 ("09","Регистрация у BotFather","11"),("10","Локальный запуск","12"),
 ("11","4 обязательных теста","13"),("12","Обработка сбоев","14"),
 ("13","Плохой промпт vs хороший","15"),("14","Хостинг: 24/7","16"),
 ("15","Честность в AI-инженерии","17"),("16","Ошибки и фиксы","18"),
 ("17","Сделай сейчас + проверка","19"),("18","Дальше — на курсе","20"),
 ("19","Путь в команду AlovLab","21"),("20","Контакты","22"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:10px;padding:6px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:9.5pt;width:24px">{a}</span>'
               f'<span style="font-weight:600;font-size:10.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:9.5pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Маршрут playbook</h1>'
    '<p class="lead">Двадцать шагов: от постановки задачи до бота, который работает 24/7 и не роняет твой токен в чужие руки.</p>'
    f'<div style="margin-top:4px">{rows}</div>'))

# 03 result
P.append(page("Шаг 01 · Результат", 3,
    head("Шаг 01", "Что ты соберёшь",
         "Бота, который принимает заявки на консультацию: выбор темы, имя, контакт, заявка администратору. С обработкой ошибок и без единой утечки токена.")
    + '<div class="flow"><div class="node"><b>Опиши</b><span>сценарий</span></div><div class="arr">→</div>'
      '<div class="node"><b>Получи</b><span>проект</span></div><div class="arr">→</div>'
      '<div class="node"><b>Проверь</b><span>4 теста</span></div><div class="arr">→</div>'
      '<div class="node"><b>Запусти</b><span>заявка принята</span></div></div>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Что это</div><div class="ch">Проект, не файл</div><p>bot.py + requirements.txt + .env.example + .gitignore + README.</p></div>'
      '<div class="card"><div class="ct">Для чего</div><div class="ch">Приём заявок</div><p>Диалог за 4 шага, заявка приходит тебе лично в Telegram.</p></div>'
      '<div class="card"><div class="ct">Дисциплина</div><div class="ch">Как у разработчика</div><p>Секреты вне кода, тесты перед показом, честный README.</p></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>Рабочий прототип: /start запускает диалог, каждый шаг ждёт ответ, в конце заявка приходит администратору. Готов к переносу на хостинг.</p></div>'))

# 04 model
P.append(page("Шаг 02 · Модель", 4,
    head("Шаг 02", "Модель: кто кому отвечает",
         "У бота четыре звена. Claude пишет только одно из них — код. Остальное решаешь ты.")
    + '<table class="ref"><tr><th>Звено</th><th>Кто это</th><th>Что делает</th></tr>'
      '<tr><td><b>Человек</b></td><td>твой клиент</td><td>пишет /start, отвечает на вопросы бота</td></tr>'
      '<tr><td><b>Telegram</b></td><td>платформа</td><td>доставляет сообщения между человеком и твоим кодом</td></tr>'
      '<tr><td><b>Твой код</b></td><td>bot.py</td><td>ведёт диалог по сценарию, хранит состояние</td></tr>'
      '<tr><td><b>Админ</b></td><td>ты</td><td>получает готовую заявку личным сообщением</td></tr></table>'
    + '<div class="term"><b>Важно.</b> <span>Если код не запущен — диалог обрывается на полпути, и человек застревает. Поэтому сначала проверяешь запуск и только потом показываешь бота другим.</span></div>'
    + '<p class="note">Вывод: сначала схема (кто кому что говорит), потом генерация кода. Не наоборот.</p>'))

# 05 scenario
P.append(page("Шаг 03 · Сценарий", 5,
    head("Шаг 03", "Одно действие на шаг",
         "«Умный бот, который всё понимает» — плохая постановка задачи. Хорошая — точный сценарий.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>/start.</b> Бот здоровается и предлагает выбрать одну из трёх тем консультации.</div></div>'
      '<div class="step"><div class="sx"><b>Тема.</b> Человек выбирает кнопкой. Бот запоминает выбор и просит имя.</div></div>'
      '<div class="step"><div class="sx"><b>Имя → контакт.</b> Два простых вопроса подряд, каждый ждёт текстовый ответ.</div></div>'
      '<div class="step"><div class="sx"><b>Подтверждение → заявка.</b> Бот показывает итог, затем отправляет тебе личное сообщение.</div></div></div>'
    + '<div class="callout check"><div class="h">Правило</div>'
      '<div class="row">Каждый шаг должен иметь ожидаемый ответ. Если человек прислал не то — бот переспрашивает, а не ломается.</div>'
      '<div class="row">/cancel работает на любом шаге и прерывает сценарий чисто, без зависшего состояния.</div></div>'))

# 06 diagram
P.append(page("Шаг 04 · Диаграмма", 6,
    head("Шаг 04", "Диаграмма состояний",
         "Нарисуй это до генерации кода — так сразу видно дыры в сценарии.")
    + '<table class="ref"><tr><th>Состояние</th><th>Ждёт</th><th>Дальше</th></tr>'
      '<tr><td><b>/start</b></td><td>команду запуска</td><td>→ ТЕМА</td></tr>'
      '<tr><td><b>ТЕМА</b></td><td>нажатие кнопки</td><td>→ ИМЯ</td></tr>'
      '<tr><td><b>ИМЯ</b></td><td>текст (не пустой)</td><td>→ КОНТАКТ</td></tr>'
      '<tr><td><b>КОНТАКТ</b></td><td>текст или номер</td><td>→ ЗАЯВКА → АДМИНУ</td></tr></table>'
    + '<p>Каждая строка таблицы — это то, что ты отдаёшь Claude как техническое задание, а не как смутное пожелание «сделай удобно».</p>'
    + '<div class="callout result"><div class="h">Зачем это нужно</div><p>Если позже бот работает не так — ты сразу видишь, в каком состоянии он застрял, и просишь Claude починить конкретный переход, а не «почини всё».</p></div>'))

# 07 master prompt
master = ("Собери проект Telegram-бота на Python для приёма заявок на консультацию.\n\n"
"Сценарий: /start → выбор одной из трёх тем → имя → контакт → подтверждение → приватное сообщение с заявкой "
"администратору. На каждом шаге работает /cancel. Обработай пустой ввод, неожиданный тип сообщения, повторный "
"/start и сбой отправки администратору.\n\n"
"Токен и ID администратора считывай из переменных окружения. Не записывай токен в код, логи или Git. Выдай bot.py, "
"requirements.txt, .env.example без секретов, .gitignore и README с командами запуска для Windows и macOS/Linux. "
"Для локального прототипа используй long polling, не включай одновременно webhook.\n\n"
"Покажи четыре ручных теста: /start, пустой ответ, /cancel, получение заявки администратором. Не заявляй об "
"успешной интеграционной проверке без реального токена. Отдельно опиши публикацию на хостинге: переменные "
"окружения, перезапуск процесса, мониторинг ошибок. Сначала покажи план файлов и сценарий, потом код.")
P.append(page("Шаг 05 · Мастер-промпт", 7,
    head("Шаг 05", "Мастер-промпт целиком",
         "Это не шаблон с [СКОБКАМИ] — это цельное техническое задание. Меняй тему бота, структуру оставляй.")
    + prompt("Мастер-промпт · СКОПИРОВАТЬ", master)
    + '<p class="note">Обрати внимание на порядок требований: сначала сценарий и файлы, потом код, потом честные тесты, потом хостинг. Такой порядок сам по себе дисциплинирует Claude не торопиться с ответом.</p>'))

# 08 anatomy
P.append(page("Шаг 06 · Анатомия", 8,
    head("Шаг 06", "Проси не код. Проси проект.",
         "Шесть требований, которые спасают от переделок — разбор мастер-промпта по частям.")
    + '<table class="ref"><tr><th>№</th><th>Требование</th><th>Зачем</th></tr>'
      '<tr><td>01</td><td><b>Цель</b></td><td>Claude знает, что вообще делает бот — приём заявок, не абстракция.</td></tr>'
      '<tr><td>02</td><td><b>Путь</b></td><td>start → контакт: чёткая последовательность шагов диалога.</td></tr>'
      '<tr><td>03</td><td><b>Сбои</b></td><td>пустой ввод, /cancel: код не падает на реальных людях.</td></tr>'
      '<tr><td>04</td><td><b>Секреты</b></td><td>из окружения: токен не утечёт в код или Git.</td></tr>'
      '<tr><td>05</td><td><b>Запуск</b></td><td>команды по шагам для двух систем — ты не гадаешь.</td></tr>'
      '<tr><td>06</td><td><b>Проверка</b></td><td>5 сценариев (включая хостинг) — бот проверен, не просто написан.</td></tr></table>'
    + '<p>Убери любой из шести пунктов — и получишь код, который выглядит рабочим, но подведёт на первом реальном пользователе.</p>'))

# 09 deliverables
P.append(page("Шаг 07 · Файлы", 9,
    head("Шаг 07", "Что должен отдать Claude",
         "Не один кусок кода, а запускаемый комплект. Если инструкции запуска нет — проект ещё не готов.")
    + '<div class="filetree">bot.py <span class="c"># сценарий и обработка сообщений</span><br>'
      'requirements.txt <span class="c"># зависимости проекта</span><br>'
      '.env.example <span class="c"># поля для секретов, без значений</span><br>'
      '.gitignore <span class="c"># защита секретов от случайного коммита</span><br>'
      'README.md <span class="c"># команды запуска Windows + macOS/Linux</span></div>'
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Ничего — это результат мастер-промпта, не отдельный запрос.</p></div>'
      '<div class="c out"><b>Что получить</b><p>Пять файлов, которые вместе образуют рабочий проект, готовый к git init.</p></div></div>'
    + '<p class="note">Если Claude прислал только код без README и .env.example — попроси прямо: «дай остальные файлы проекта из требований».</p>'))

# 10 secrets
P.append(page("Шаг 08 · Секреты", 10,
    head("Шаг 08", "Токен = ключ от бота",
         "Токен даёт полный доступ к боту от твоего имени. Обращайся с ним как с паролем.")
    + '<table class="ref"><tr><th>Где</th><th>Токен</th></tr>'
      '<tr><td>В коде (bot.py)</td><td><b>НЕТ</b> — никогда не пиши токен прямой строкой</td></tr>'
      '<tr><td>В .env (не в Git)</td><td><b>ДА</b> — локальный файл с реальным токеном</td></tr>'
      '<tr><td>В .env.example (в Git)</td><td>НЕТ — только имя переменной без значения</td></tr>'
      '<tr><td>В общем чате или скриншоте</td><td><b>НИКОГДА</b></td></tr></table>'
    + '<div class="warn"><div class="h">Если токен всё же утёк</div><ul>'
      '<li class="ok">Зайди к @BotFather, команда /revoke — старый токен умирает, получаешь новый.</li>'
      '<li class="ok">Обнови .env новым токеном, перезапусти бота.</li></ul></div>'
    + '<p>.gitignore из мастер-промпта как раз существует, чтобы .env физически не мог попасть в Git, даже если ты забудешь об этом в спешке.</p>'))

# 11 botfather
P.append(page("Шаг 09 · BotFather", 11,
    head("Шаг 09", "Регистрация у @BotFather",
         "Официальный способ Telegram создать бота. Занимает минуту.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Найди <code style="font-family:ui-monospace,monospace">@BotFather</code></b> в Telegram — официальный бот с синей галочкой.</div></div>'
      '<div class="step"><div class="sx"><b>Команда <code style="font-family:ui-monospace,monospace">/newbot</code></b> — задай имя и юзернейм, который должен заканчиваться на «bot».</div></div>'
      '<div class="step"><div class="sx"><b>Получи токен</b> — длинная строка цифр и букв. Это и есть твой ключ доступа.</div></div>'
      '<div class="step"><div class="sx"><b>Узнай свой Telegram ID</b> (для переменной администратора) — спроси у любого бота вроде @userinfobot.</div></div>'
      '<div class="step"><div class="sx"><b>Впиши оба значения в .env,</b> не в .env.example и не в код.</div></div></div>'))

# 12 local run
P.append(page("Шаг 10 · Запуск", 12,
    head("Шаг 10", "Локальный запуск",
         "Для прототипа — long polling. Не включай одновременно webhook, это конфликтует.")
    + '<div class="mns"><div class="m move"><div class="h">Polling (для теста)</div><p>Бот сам спрашивает Telegram: «есть новые сообщения?». Просто, работает на любом компьютере, не нужен публичный адрес.</p></div>'
      '<div class="m stay"><div class="h">Webhook (для продакшна)</div><p>Telegram сам стучится к боту по адресу. Нужен публичный сервер с HTTPS. Разбираем на курсе.</p></div></div>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Установи зависимости</b> из requirements.txt командой из README.</div></div>'
      '<div class="step"><div class="sx"><b>Запусти bot.py</b> — командой из README для своей системы.</div></div>'
      '<div class="step"><div class="sx"><b>Напиши /start</b> своему боту в Telegram и пройди сценарий целиком.</div></div></div>'))

# 13 tests
P.append(page("Шаг 11 · Проверка", 13,
    head("Шаг 11", "«Работает» надо доказать",
         "Пройди путь клиента. И сломай его специально — не только удачный сценарий.")
    + '<table class="ref"><tr><th>Ввод</th><th>Ожидаемый результат</th></tr>'
      '<tr><td><b>/start</b></td><td>открылся первый шаг, показаны кнопки тем</td></tr>'
      '<tr><td><b>пусто</b></td><td>бот просит повторить, диалог не ломается</td></tr>'
      '<tr><td><b>/cancel</b></td><td>сценарий остановлен, состояние сброшено</td></tr>'
      '<tr><td><b>заявка</b></td><td>админ получил её личным сообщением</td></tr></table>'
    + '<div class="callout check"><div class="h">Правило</div>'
      '<div class="row">Если хотя бы один тест красный — верни Claude точное описание, что пошло не так, а не общее «не работает».</div>'
      '<div class="row">Тестируй с реального телефона, не только с компьютера — там другая клавиатура и другой темп ввода.</div></div>'))

# 14 errors
P.append(page("Шаг 12 · Сбои", 14,
    head("Шаг 12", "Обработка сбоев",
         "Реальные люди присылают боту не то, что ты ожидал. Четыре сценария из мастер-промпта.")
    + '<div class="fix">'
      '<div class="r"><b>Пустой ввод.</b> Человек нажал «отправить», не написав текст. Бот вежливо просит повторить, не роняется.</div>'
      '<div class="r"><b>Неожиданный тип сообщения.</b> Прислали фото вместо текста. Бот объясняет, что ждёт, и не теряет прогресс.</div>'
      '<div class="r"><b>Повторный /start.</b> Человек передумал и начал заново. Старое состояние сбрасывается чисто, без дублей.</div>'
      '<div class="r"><b>Сбой отправки администратору.</b> Например, ты заблокировал бота. Клиент должен увидеть, что заявка не потерялась молча.</div></div>'
    + '<p class="note">Если Claude не покрыл один из этих случаев — прямо укажи на него, ссылаясь на этот список.</p>'))

# 15 good/bad
P.append(page("Шаг 13 · Как просить", 15,
    head("Шаг 13", "Плохой промпт против хорошего",
         "Разница не в длине, а в точности.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Плохо</div>«Сделай бота для записи на консультацию.»<br><br>Нет сценария, нет требований к секретам, нет тестов. Получишь код, который выглядит рабочим и подводит на первом же пустом сообщении.</div>'
      '<div class="box good"><div class="lbl">Хорошо</div>Мастер-промпт со страницы 07: точный сценарий по шагам, требования к секретам, список тестов, требование честности про непроверенную интеграцию.</div></div>'
    + '<p>Хороший промпт для инженерной задачи — это техническое задание, а не пожелание. Ты не обязан уметь программировать, но обязан уметь точно описать, что должно происходить на каждом шаге.</p>'))

# 16 hosting
P.append(page("Шаг 14 · Хостинг", 16,
    head("Шаг 14", "Чтобы бот работал 24/7",
         "Локальный запуск живёт, пока открыт терминал. Для постоянной работы — хостинг.")
    + '<div class="mns"><div class="m move"><div class="h">Локально</div><p>Для теста. Закрыл терминал — бот замолчал. Быстро проверить сценарий.</p></div>'
      '<div class="m stay"><div class="h">На хостинге</div><p>Работает 24/7, есть мониторинг ошибок. Для реального использования.</p></div></div>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Спроси Claude:</b> «назови 2–3 простых способа разместить Python-бота на long polling, дай инструкцию для новичка».</div></div>'
      '<div class="step"><div class="sx"><b>Задай переменные окружения</b> на хостинге (токен, ID администратора) — так же, как в .env, но через панель сервиса.</div></div>'
      '<div class="step"><div class="sx"><b>Настрой автоперезапуск процесса</b> — если бот упадёт из-за сети, он должен подняться сам.</div></div>'
      '<div class="step"><div class="sx"><b>Проверь мониторинг ошибок</b> — чтобы узнать о сбое раньше, чем это заметит клиент.</div></div></div>'))

# 17 honesty
P.append(page("Шаг 15 · Честность", 17,
    head("Шаг 15", "Честность в AI-инженерии",
         "Мастер-промпт неспроста требует: не заявлять об успешной проверке без реального токена.")
    + '<div class="warn"><div class="h">Так нельзя</div><ul>'
      '<li>Просить Claude «подтвердить», что интеграция протестирована, если токен ещё не вставлен.</li>'
      '<li>Публиковать бота без прогона всех 4 тестов вручную.</li>'
      '<li>Молча пропускать случаи из раздела «Обработка сбоев», потому что «и так сойдёт».</li></ul></div>'
    + '<div class="warn"><div class="h" style="color:#8fd08a">Так правильно</div><ul>'
      '<li class="ok">Тестируешь с реальным токеном сам, своими руками, перед показом другим.</li>'
      '<li class="ok">Если Claude написал «должно работать» — это гипотеза, не факт. Проверяешь и только потом веришь.</li>'
      '<li class="ok">Честно пишешь в README, что это прототип, если это прототип.</li></ul></div>'
    + '<p>Это тот же принцип, что и во всей нашей работе: ИИ ускоряет, а не подтверждает результат вместо тебя.</p>'))

# 18 errors round2
P.append(page("Шаг 16 · Ошибки", 18,
    head("Шаг 16", "Частые ошибки и фиксы",
         "Пять граблей, которые встречаются чаще всего.")
    + '<div class="fix">'
      '<div class="r"><b>Забыл .gitignore, токен попал в историю Git.</b> Фикс: /revoke у BotFather, новый токен, .gitignore с самого начала следующего проекта.</div>'
      '<div class="r"><b>Webhook и polling включены одновременно.</b> Фикс: выключи webhook (setWebhook с пустым url) перед локальным polling.</div>'
      '<div class="r"><b>Бот теряет состояние между сообщениями.</b> Фикс: попроси Claude явно показать, где и как хранится состояние диалога.</div>'
      '<div class="r"><b>README без команд для твоей ОС.</b> Фикс: прямо укажи систему — Windows, macOS или Linux — и попроси команды под неё.</div>'
      '<div class="r"><b>Тесты не проводились, но бот «вроде работает».</b> Фикс: пройди все 4 теста со страницы 13 прежде, чем показывать бота другим.</div></div>'))

# 19 action
P.append(page("Шаг 17 · Действие", 19,
    head("Шаг 17", "Сделай сейчас",
         "За один вечер пройди путь от задачи до работающего прототипа.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Опиши свои 4 шага диалога</b> по образцу диаграммы со страницы 06 — под свою задачу, не обязательно консультации.</div></div>'
      '<div class="step"><div class="sx"><b>Собери мастер-промпт</b> по формуле со страницы 07–08 и отправь Claude.</div></div>'
      '<div class="step"><div class="sx"><b>Запусти локально</b> и пройди диалог сам целиком.</div></div>'
      '<div class="step"><div class="sx"><b>Пройди 4 проверки</b> со страницы 13, прежде чем показать кому-то ещё.</div></div></div>'
    + '<div class="callout check"><div class="h">Проверь перед показом другим</div>'
      '<div class="row">Токен нигде не виден в коде, логах или Git.</div>'
      '<div class="row">Все 4 теста пройдены вручную, не только «по ощущениям».</div>'
      '<div class="row">README объясняет запуск понятно даже не программисту.</div>'
      '<div class="row">Заявка реально доходит до администратора.</div></div>'))

# 20 course
P.append(page("Дальше", 20,
    head("Дальше", "Один бот — это один инструмент. А есть система",
         "Ты прошёл дисциплину постановки задачи для ИИ. На курсе применяешь её ко всему контент-конвейеру.")
    + '<p>Сценарий, диаграмма состояний, честные тесты — этот метод работает не только для ботов. Курс «Нейросети и ChatGPT для каждого» учит собирать систему целиком: тексты, визуал, видео, звук, аватары — и то, что ты только что прошёл, боты и автоматизацию.</p>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Webhook + продакшн</div><p>Как перенести бота с polling на настоящий сервер.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Приём оплаты</div><p>Как подключить к боту простую оплату.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Конвейер</div><p>Бот, сайт, контент и автоматизация как одна система.</p></div></div>'
    + '<div class="callout result"><div class="h">Сейчас скидка 50% на тариф ПРО</div><p>49 990 ₽ вместо 99 990 ₽, до 30 сентября. Начать — alovlab.ru.</p></div>'))

# 21 team
P.append(page("Команда", 21,
    head("Путь дальше", "Путь в команду AlovLab",
         "Если начало получаться и хочется делать это для других — есть куда расти.")
    + '<div class="team"><div class="h">Собираешь ботов с такой дисциплиной?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты: собирают ботов и автоматизацию под задачи брендов, набивают портфолио на живых кейсах и растут рядом с командой.</p>'
      '<div class="dirs"><span>Telegram-боты</span><span>Автоматизация</span><span>AI-ассистенты</span><span>Контент-конвейеры</span></div>'
      '<p style="margin-top:8px">Это работа и практика, а не обещание трудоустройства. Но дорога открыта: покажи, что доводишь результат до проверенного продакшна.</p></div>'
    + '<p>Бизнесу, которому нужен бот или автоматизация под ключ — это AlovLab Studio. Отправляешь бриф, сборку и конвейер берём на себя.</p>'))

# 22 contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Автоконтент</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Один бот — инструмент. Система — это курс.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Скидка 50% на тариф ПРО до 30 сентября — 49 990 ₽ вместо 99 990 ₽. Нужен бот под бизнес под ключ — отправь бриф в студию.</p>
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
