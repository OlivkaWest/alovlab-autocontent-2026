# -*- coding: utf-8 -*-
"""AlovLab · методичка «Собрал Telegram-бота, а кодить не умею» (премиум-PDF, фикс-A4).
По GLOBAL-METHODOLOGY-RULE: реальный workflow (Claude пишет код, @BotFather выдаёт токен, хостинг),
промпты с [переменными]+уровни, плохо/хорошо, честность (токен/данные/ложные обещания), ACTION+CHECK,
мост в курс + «Путь в команду AlovLab». Без выдуманных цифр.
Запуск: python3 scripts/guide_tgbot_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "tg-bot"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-tg-bot.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.midwrap{width:100%}
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.3pt;line-height:1.4;color:var(--ink);margin-top:3px;max-width:none}
.lvls{margin:10px 0 2px}
.lvls .row{display:grid;grid-template-columns:120px 1fr;gap:10px;align-items:start;margin:7px 0}
.lvls .row .k{font-weight:800;font-size:9pt;color:var(--o);padding-top:2px}
.lvls .row p{margin:0;font-size:9.8pt;line-height:1.42;color:var(--body)}
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
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · собрал Telegram-бота</span>'
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
  <div style="position:absolute;right:-4%;top:20%;width:56%;height:44%;border-radius:26px;border:1px solid rgba(255,140,60,.28);background:linear-gradient(160deg,rgba(255,140,60,.10),rgba(255,140,60,0));box-shadow:0 30px 90px rgba(0,0,0,.5)"></div>
  <div style="position:absolute;right:4%;top:24%;width:46%;color:#ffb98a;font-weight:800;font-size:10pt;letter-spacing:.02em">
     AlovLab bot<div style="height:10px"></div>
     <div style="font-weight:700;font-size:22pt;color:#fff;line-height:1.1">Привет!<br>Забери гайд<br>или оставь <span style="color:var(--o2)">заявку</span></div>
     <div style="margin-top:14px;display:inline-block;background:linear-gradient(150deg,var(--o2),var(--o));color:#160e07;font-weight:800;font-size:9pt;padding:7px 14px;border-radius:9px">Забрать гайд</div>
  </div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд</div>
    <h1 style="font-weight:800;font-size:32pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Собрал Telegram-бота. Кодить не умею.</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:40ch">Claude пишет код, ты берёшь токен у BotFather и запускаешь. Ни одной строки кода своими руками.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Один вечер</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Без программиста</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Промпт внутри</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("01","Что ты соберёшь","03"),("02","Миф про программирование","04"),("03","Что нужно (бесплатно)","05"),
 ("04","Как это работает: 4 этапа","06"),("05","Этап 1 · Промпт-бриф бота","07"),
 ("06","Этап 2 · Получи и прочитай код","08"),("07","Этап 3 · Токен у BotFather","09"),
 ("08","Этап 4 · Запусти бота","10"),("09","Как ставить задачу: плохо/хорошо","11"),
 ("10","Что поручить боту","12"),("11","Честно: токен и данные","13"),
 ("12","Хостинг: чтобы бот не спал","14"),("13","Частые ошибки и фиксы","15"),
 ("14","Сделай сейчас + проверка","16"),("15","Дальше — на курсе","17"),
 ("16","Путь в команду AlovLab","18"),("17","Контакты","19"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:12px;padding:8px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:10pt;width:26px">{a}</span>'
               f'<span style="font-weight:600;font-size:11.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:10pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Маршрут гайда</h1>'
    '<p class="lead">Семнадцать шагов от пустого чата до живого бота, который отвечает в Telegram.</p>'
    f'<div style="margin-top:6px">{rows}</div>'))

# 03 result
P.append(page("Шаг 01 · Результат", 3,
    head("Шаг 01", "Что ты соберёшь за вечер",
         "Рабочего Telegram-бота: он здоровается по /start, показывает кнопки и отвечает на сообщения.")
    + '<div class="flow"><div class="node"><b>Опиши</b><span>задачу</span></div><div class="arr">→</div>'
      '<div class="node"><b>Получи код</b><span>от Claude</span></div><div class="arr">→</div>'
      '<div class="node"><b>Токен</b><span>@BotFather</span></div><div class="arr">→</div>'
      '<div class="node"><b>Запусти</b><span>бот живой</span></div></div>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Что это</div><div class="ch">Бот с кнопками</div><p>Приветствие, кнопки-действия, ответ на сообщение.</p></div>'
      '<div class="card"><div class="ct">Для чего</div><div class="ch">Лид-магнит · заявки</div><p>Выдать гайд подписчику, собрать контакт, ответить на частый вопрос.</p></div>'
      '<div class="card"><div class="ct">Сколько кода</div><div class="ch">Ноль строк</div><p>Код пишет Claude, ты им только пользуешься.</p></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>Бот в Telegram, который отвечает на /start, показывает кнопки и реагирует на сообщения. Работает у тебя на компьютере или на бесплатном хостинге.</p></div>'))

# 04 myth
P.append(page("Шаг 02 · Миф", 4,
    head("Шаг 02", "Бот — это не программирование",
         "Барьер в голове, а не в технологии.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Миф</div><b>«Нужно учить Python, нанимать разработчика, ждать неделями и платить вперёд.»</b> Поэтому бота откладывают.</div>'
      '<div class="box good"><div class="lbl">Как есть</div><b>Нужно чётко описать, что бот должен делать.</b> Остальное пишет Claude: код, кнопки, обработку сообщений.</div></div>'
    + '<p>Ты не открываешь редактор кода с нуля. Ты пишешь на русском, что нужно, и получаешь готовый файл бота. Твоя работа — описать задачу и один раз пройти техническую часть (токен, запуск).</p>'
    + '<div class="term"><b>Честно.</b> <span>Первый код обычно рабочий, но не идеальный. Метод в том, чтобы получить каркас за минуты и доводить его короткими правками, как с сайтом. Это и есть навык, который ты освоишь.</span></div>'
    + '<div class="mns"><div class="m move"><div class="h">Твоя работа</div><p>Описать, что бот делает, получить токен, запустить, поправить словами.</p></div>'
      '<div class="m stay"><div class="h">Работа Claude</div><p>Написать код на Python, обработать кнопки и сообщения, объяснить, как запускать.</p></div></div>'))

# 05 need
P.append(page("Шаг 03 · Подготовка", 5,
    head("Шаг 03", "Что нужно. И почти всё бесплатно",
         "Минимум инструментов, ничего сложного заранее ставить не нужно.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Нейросеть</div><div class="ch">Claude / Claude Code</div><p>Пишет код бота и объясняет, как запускать.</p></div>'
      '<div class="card"><div class="ct">Telegram</div><div class="ch">@BotFather</div><p>Официальный бот Telegram, выдаёт токен за минуту, бесплатно.</p></div>'
      '<div class="card"><div class="ct">Python</div><div class="ch">Установлен на компьютере</div><p>Понадобится, чтобы запустить готовый код (шаг 08).</p></div></div>'
    + '<h3>Собери это заранее (10 минут)</h3>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Что бот делает.</b> Одна ясная задача: выдаёт гайд, принимает заявку, отвечает на вопрос.</div></div>'
      '<div class="step"><div class="sx"><b>Текст приветствия.</b> Что бот говорит по команде /start.</div></div>'
      '<div class="step"><div class="sx"><b>Название бота.</b> Как он будет называться в Telegram (например AlovLab bot).</div></div>'
      '<div class="step"><div class="sx"><b>Куда слать заявки.</b> Твой контакт или чат, куда бот пересылает сообщения.</div></div></div>'))

# 06 method
P.append(page("Шаг 04 · Метод", 6,
    head("Шаг 04", "Как это работает: 4 этапа",
         "Весь путь укладывается в один вечер.")
    + '<div class="scene"><div class="sn">1</div><div><div class="sh">Опиши задачу</div>'
      '<div class="sd">Промпт-бриф: что бот делает, какие кнопки, что отвечает. <b>Каркас на следующей странице.</b></div></div><span class="stag">Промпт</span></div>'
    + '<div class="scene"><div class="sn">2</div><div><div class="sh">Получи код</div>'
      '<div class="sd">Claude возвращает готовый файл бота на Python с пояснениями.</div></div><span class="stag">Код</span></div>'
    + '<div class="scene"><div class="sn">3</div><div><div class="sh">Возьми токен</div>'
      '<div class="sd">У @BotFather в Telegram, команда /newbot, за минуту, бесплатно.</div></div><span class="stag">Токен</span></div>'
    + '<div class="scene"><div class="sn">4</div><div><div class="sh">Запусти</div>'
      '<div class="sd">Вставляешь токен в код, запускаешь файл, бот отвечает вживую.</div></div><span class="stag">Запуск</span></div>'
    + '<div class="callout check"><div class="h">Правило вечера</div>'
      '<div class="row">Сначала весь каркас бота, потом мелкие правки словами.</div>'
      '<div class="row">Токен никому не показывай и не публикуй — это ключ к твоему боту.</div></div>'))

# 07 prompt
brief = ("Напиши Telegram-бота на Python (библиотека python-telegram-bot). Что делает: по команде /start "
         "приветствует текстом [ТЕКСТ ПРИВЕТСТВИЯ] и показывает кнопки [КНОПКА 1] и [КНОПКА 2]. По кнопке [КНОПКА 1] "
         "присылает [ЧТО ВЫДАЁТ, например ссылку на гайд]. По кнопке [КНОПКА 2] бот просит написать сообщение и "
         "пересылает его мне в чат [МОЙ ЮЗЕРНЕЙМ ИЛИ ID]. Добавь обработку ошибок и понятные комментарии в коде. "
         "Токен вынеси в отдельную переменную BOT_TOKEN в начале файла. Дай готовый код одним файлом и короткую "
         "пошаговую инструкцию для новичка, как его запустить на компьютере.")
P.append(page("Этап 1 · Промпт", 7,
    head("Этап 1", "Промпт-бриф бота",
         "Скопируй, поменяй слова в [СКОБКАХ] и отправь Claude. Это каркас всего бота.")
    + prompt("Промпт-бриф · СКОПИРОВАТЬ", brief)
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Текст приветствия, название кнопок, что бот выдаёт, куда пересылать заявки.</p></div>'
      '<div class="c out"><b>Что получить</b><p>Готовый файл bot.py с приветствием, кнопками, обработкой сообщений и инструкцией запуска.</p></div></div>'
    + '<div class="lvls"><div class="row"><span class="k">Быстрый</span><p>Отправь бриф как есть, поменяв скобки. Хватит для первой рабочей версии.</p></div>'
      '<div class="row"><span class="k">Про</span><p>Добавь: «сохраняй заявки в текстовый файл» или «добавь третью кнопку [НАЗВАНИЕ]».</p></div>'
      '<div class="row"><span class="k">Advanced</span><p>Попроси: «добавь команду /help со списком возможностей» и «логируй ошибки в отдельный файл».</p></div></div>'))

# 08 read code
P.append(page("Этап 2 · Код", 8,
    head("Этап 2", "Получи и прочитай код",
         "Не обязательно понимать каждую строку. Важно узнать, где токен и как запускать.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Сохрани код</b> в файл с именем <code style="font-family:ui-monospace,monospace">bot.py</code> в отдельную папку на компьютере.</div></div>'
      '<div class="step"><div class="sx"><b>Найди строку с токеном</b> — обычно вверху файла, что-то вроде <code style="font-family:ui-monospace,monospace">BOT_TOKEN = "..."</code>.</div></div>'
      '<div class="step"><div class="sx"><b>Прочитай инструкцию запуска</b>, которую дал Claude вместе с кодом — обычно это установка одной библиотеки и команда запуска.</div></div>'
      '<div class="step"><div class="sx"><b>Не понимаешь шаг</b> — прямо спроси Claude: «объясни это простыми словами для новичка».</div></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>У тебя есть файл bot.py с понятной структурой: где токен, где приветствие, где кнопки. Пока без токена бот ещё не запущен — это следующий шаг.</p></div>'))

# 09 botfather
P.append(page("Этап 3 · Токен", 9,
    head("Этап 3", "Возьми токен у @BotFather",
         "Официальный способ Telegram создать бота. Занимает минуту.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Найди в Telegram бота <code style="font-family:ui-monospace,monospace">@BotFather</code></b> через поиск — это официальный бот Telegram с синей галочкой.</div></div>'
      '<div class="step"><div class="sx"><b>Напиши команду <code style="font-family:ui-monospace,monospace">/newbot</code></b> и следуй подсказкам: имя бота, затем короткое имя пользователя, которое должно заканчиваться на <code style="font-family:ui-monospace,monospace">bot</code>.</div></div>'
      '<div class="step"><div class="sx"><b>BotFather пришлёт токен</b> — длинную строку из цифр и букв. Это ключ к твоему боту.</div></div>'
      '<div class="step"><div class="sx"><b>Скопируй токен</b> и вставь в код вместо <code style="font-family:ui-monospace,monospace">BOT_TOKEN = "..."</code>.</div></div></div>'
    + '<div class="warn"><div class="h">Важно</div><ul>'
      '<li>Никому не показывай токен и не публикуй его в соцсетях или репозиториях.</li>'
      '<li class="ok">Если случайно показал — в BotFather есть команда /revoke, чтобы получить новый токен.</li></ul></div>'))

# 10 launch
P.append(page("Этап 4 · Запуск", 10,
    head("Этап 4", "Запусти бота",
         "Финальный шаг — включить код на компьютере.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Установи библиотеку,</b> которую указал Claude в инструкции — обычно одна команда в терминале.</div></div>'
      '<div class="step"><div class="sx"><b>Запусти файл</b> bot.py — командой из инструкции Claude.</div></div>'
      '<div class="step"><div class="sx"><b>Найди своего бота в Telegram</b> по имени пользователя, которое задал у BotFather.</div></div>'
      '<div class="step"><div class="sx"><b>Напиши /start</b> — бот должен поздороваться и показать кнопки.</div></div></div>'
    + '<div class="callout result"><div class="h">Готово</div><p>Пока код запущен на твоём компьютере, бот отвечает. Закрыл терминал — бот заснул. Как сделать, чтобы он работал всегда — на странице 14.</p></div>'
    + '<p class="note">Не отвечает — не паникуй. Проверь: токен вставлен правильно, библиотека установлена, нет ошибки в терминале. Скопируй текст ошибки и отдай Claude — попроси починить.</p>'))

# 11 good/bad
P.append(page("Шаг 05 · Как просить", 11,
    head("Шаг 05", "Как ставить задачу: плохо и хорошо",
         "Бот получается ровно настолько, насколько ясно ты объяснил.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Плохо</div>«Сделай бота для моего бизнеса.»<br><br>Непонятно, что бот делает, какие кнопки, куда слать заявки. Выходит общий шаблон.</div>'
      '<div class="box good"><div class="lbl">Хорошо</div>«Бот для мастера маникюра. По /start здоровается и предлагает кнопки "Записаться" и "Цены". "Записаться" пересылает сообщение мне в чат. "Цены" присылает готовый текст с прайсом.»</div></div>'
    + '<h3>Формула хорошей задачи</h3>'
    + '<div class="flow"><div class="node"><b>Что делает</b><span>одна задача</span></div><div class="arr">+</div>'
      '<div class="node"><b>Кнопки</b><span>какие и что делают</span></div><div class="arr">+</div>'
      '<div class="node"><b>Ответы</b><span>что говорит</span></div><div class="arr">+</div>'
      '<div class="node"><b>Заявки</b><span>куда слать</span></div></div>'
    + '<p>Чем конкретнее вводные, тем меньше правок потом. Промпт-бриф со страницы 07 уже собран по этой формуле.</p>'))

# 12 what to give bot
P.append(page("Шаг 06 · Применение", 12,
    head("Шаг 06", "Что поручить боту",
         "Три рабочих сценария под контент и продажи.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Лид-магнит</div><div class="ch">Выдаёт гайд</div><p>Новый подписчик пишет /start и сразу получает файл или ссылку.</p></div>'
      '<div class="card"><div class="ct">Приём заявок</div><div class="ch">Собирает контакт</div><p>Кнопка «Оставить заявку» пересылает тебе имя и сообщение клиента.</p></div>'
      '<div class="card"><div class="ct">Автоответ</div><div class="ch">FAQ</div><p>Отвечает на частые вопросы: цены, адрес, как записаться.</p></div></div>'
    + '<p>Можно совместить все три в одном боте — именно так устроен промпт-бриф на странице 07 (две кнопки под разные сценарии, легко добавить третью).</p>'))

# 13 honest
P.append(page("Шаг 07 · Честность", 13,
    head("Шаг 07", "Честно: токен и данные",
         "Бот работает с реальными людьми и их сообщениями — тут есть правила.")
    + '<div class="warn"><div class="h">Так нельзя</div><ul>'
      '<li>Публиковать токен бота в открытом доступе (репозиторий, скриншот, форум).</li>'
      '<li>Собирать личные данные людей без явного согласия и объяснения зачем.</li>'
      '<li>Обещать ботом то, что он не умеет («бот запишет вас автоматически», если это делаешь ты вручную).</li></ul></div>'
    + '<div class="warn"><div class="h" style="color:#8fd08a">Так правильно</div><ul>'
      '<li class="ok">Токен хранишь только у себя, при утечке — /revoke у BotFather.</li>'
      '<li class="ok">В приветствии честно пишешь, что делает бот и что будет с сообщением.</li>'
      '<li class="ok">Если бот пересылает заявки тебе лично — так и скажи в тексте кнопки.</li></ul></div>'))

# 14 hosting
P.append(page("Шаг 08 · Хостинг", 14,
    head("Шаг 08", "Чтобы бот работал всегда",
         "Код на твоём компьютере засыпает, когда ты его выключаешь. Решение — недорогой или бесплатный хостинг.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Спроси Claude:</b> «назови 2–3 простых способа бесплатно или недорого разместить Telegram-бота на Python, и дай инструкцию для новичка под [НАЗВАНИЕ СЕРВИСА]».</div></div>'
      '<div class="step"><div class="sx"><b>Загрузи туда файл bot.py</b> по инструкции — обычно это загрузка файла и указание команды запуска.</div></div>'
      '<div class="step"><div class="sx"><b>Проверь, что бот отвечает,</b> даже когда твой компьютер выключен.</div></div></div>'
    + '<div class="callout result"><div class="h">Готово</div><p>Бот работает круглосуточно, независимо от твоего компьютера. Это уже полноценный рабочий инструмент.</p></div>'
    + '<p class="note">Разные сервисы хостинга периодически меняют бесплатные условия — уточняй актуальные у Claude перед выбором.</p>'))

# 15 errors
P.append(page("Шаг 09 · Ошибки", 15,
    head("Шаг 09", "Частые ошибки и фиксы", "Пять граблей первого бота.")
    + '<div class="fix">'
      '<div class="r"><b>Бот не отвечает вообще.</b> Фикс: проверь, что токен вставлен без лишних пробелов и кавычек.</div>'
      '<div class="r"><b>Ошибка при запуске в терминале.</b> Фикс: скопируй текст ошибки целиком и отдай Claude с просьбой починить.</div>'
      '<div class="r"><b>Кнопки не нажимаются.</b> Фикс: попроси Claude «проверь обработку нажатий кнопок и почини».</div>'
      '<div class="r"><b>Бот отвечает не тем текстом.</b> Фикс: покажи Claude, что сейчас отвечает бот и как должно быть.</div>'
      '<div class="r"><b>Бот засыпает, когда закрываешь ноутбук.</b> Фикс: перенеси на хостинг (страница 14).</div></div>'
    + '<p class="note">Приём оплаты и сложные сценарии внутри бота — разбираем в части 2 (в Telegram).</p>'))

# 16 action
P.append(page("Шаг 10 · Действие", 16,
    head("Шаг 10", "Сделай сейчас", "За один заход собери и запусти первую версию.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Заполни промпт-бриф</b> со страницы 07 под свою задачу.</div></div>'
      '<div class="step"><div class="sx"><b>Получи код</b> и сохрани как bot.py.</div></div>'
      '<div class="step"><div class="sx"><b>Возьми токен</b> у @BotFather и вставь в код.</div></div>'
      '<div class="step"><div class="sx"><b>Запусти</b> и напиши /start своему боту.</div></div></div>'
    + '<div class="callout check"><div class="h">Проверь себя перед показом другим</div>'
      '<div class="row">Бот отвечает на /start понятным текстом.</div>'
      '<div class="row">Кнопки нажимаются и делают то, что обещано.</div>'
      '<div class="row">Токен нигде не опубликован.</div>'
      '<div class="row">Приветствие честно объясняет, что делает бот.</div>'
      '<div class="row">Заявки долетают туда, куда нужно.</div></div>'))

# 17 course
P.append(page("Дальше", 17,
    head("Дальше", "Бот — это один результат. А есть система",
         "Ты собрал бота за вечер. На курсе собираешь метод под любые задачи автоматизации.")
    + '<p>Один бот — хорошо. Но сила не в одной генерации, а в системе: как ставить задачи нейросети, как связать бота с заявками, оплатой, рассылкой. Это часть курса «Нейросети и ChatGPT для каждого».</p>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Бот + рассылка</div><p>Как бот сам напоминает подписчикам и прогревает.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Приём оплаты</div><p>Как подключить к боту простую оплату.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Конвейер</div><p>Бот, сайт, контент и автоматизация как одна система.</p></div></div>'
    + '<p>Бот за вечер — это только вход. Дальше ты перестаёшь искать «сделайте мне бота» и делаешь сам.</p>'))

# 18 team
P.append(page("Команда", 18,
    head("Путь дальше", "Путь в команду AlovLab",
         "Если начало получаться и хочется делать это для других — есть куда расти.")
    + '<div class="team"><div class="h">Собираешь ботов уверенно?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты: собирают ботов и автоматизацию под задачи брендов, набивают портфолио на живых кейсах и растут в ремесле рядом с командой.</p>'
      '<div class="dirs"><span>Telegram-боты</span><span>Автоматизация</span><span>AI-ассистенты</span><span>Контент-конвейеры</span></div>'
      '<p style="margin-top:8px">Это работа и практика, а не обещание трудоустройства. Но дорога открыта: покажи, что умеешь довести результат.</p></div>'
    + '<p>Бизнесу, которому нужен бот или автоматизация под ключ, а не «сам за вечер» — это уже AlovLab Studio. Отправляешь бриф, сборку и конвейер берём на себя.</p>'))

# 19 contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Автоконтент</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Не заказывай бота. Собери сам за вечер.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Промпт-бриф и эта методичка — бесплатно в Telegram. Нужен бот под бизнес под ключ — отправь бриф в студию.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Бриф студии · @alovlab</span>
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">alovlab.ru</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))
