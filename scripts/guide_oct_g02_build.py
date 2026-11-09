# -*- coding: utf-8 -*-
"""AlovLab · Октябрь 2026 · Методичка G02 «Формат и точность ответа» (дни 4-7 календаря) — v2.
Исправления по ревью: минимум 13 содержательных страниц (было 8), полный кейс «помощник для
ответов клиентам AlovLab» (глава 5), исправлена инструкция главы 4 («даю три варианта» -> корректная
формулировка), реальные источники с URL+датой, снята непроверенная формулировка про «реальные
проекты под задачи брендов», кликабельное оглавление (PDF-якоря), убран декоративный «Скопировать»
(промпты — в отдельном prompts.txt).
Запуск: python3 scripts/guide_oct_g02_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "guides" / "G02-format-i-tochnost"
OUT = OUTDIR / "workbook.html"

EXTRA = r"""
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.3pt;line-height:1.4;color:var(--ink);margin-top:3px;max-width:none}
.fix{display:grid;gap:8px;margin:10px 0}
.fix .r{background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 13px;font-size:9.8pt;line-height:1.45;color:var(--body)}
.fix .r b{color:var(--ink)}
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:16px 19px;margin:10px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12.5pt;color:#fff;margin-bottom:6px}.team p{font-size:9.8pt;line-height:1.5;color:#cdbfa8;max-width:none}
.team .dirs{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 3px}
.team .dirs span{font-size:8.4pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:4px 10px}
.msg{background:#fff;border:1px solid var(--line);border-left:3px solid var(--muted);border-radius:0 11px 11px 0;padding:10px 14px;margin:8px 0;font-size:9.8pt;line-height:1.5;color:var(--body);font-style:italic}
.msg b{font-style:normal;color:var(--ink)}
.redact{background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 13px;margin:8px 0}
.redact .row{display:flex;justify-content:space-between;gap:10px;font-size:9.3pt;padding:4px 0;border-top:1px solid var(--line2)}
.redact .row:first-child{border-top:none}
.redact .row b{color:var(--ink);min-width:34%}
.redact .row span{color:var(--muted)}
.redact .row.keep span{color:#3f7d34}
.redact .row.cut span{color:#c0492a}
a.tocref{color:inherit;text-decoration:none}
a.tocref:hover{text-decoration:underline}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False, pid=None):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    idattr = f' id="{pid}"' if pid else ''
    return (f'<section class="page"{idattr}><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · Формат и точность ответа</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None, ref=None):
    """Тёмная плашка без декоративной кнопки «Скопировать» — есть prompts.txt с тем же текстом."""
    r = f'<div class="ru">{ru}</div>' if ru else ''
    reftag = f'<span class="copy">{ref}</span>' if ref else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>{reftag}</div>'
            f'<code>{code}</code>{r}</div>')

PROMPTS_TXT = []  # collect (title, text) for prompts.txt export
def register_prompt(title, text):
    PROMPTS_TXT.append((title, text))

P = []

# 01 Cover
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">Октябрь 2026 · Неделя 1, дни 4–7 · G02</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:17ch">Формат и точность ответа</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Что нельзя вставлять в чат. Почему ответы разные. Как задать формат. Полный кейс: помощник для ответов клиентам. Сборка в личного помощника.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">5 глав</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Полный рабочий кейс</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Капстоун недели 1</span>
    </div>
  </div>
</section>""")

# 02 TOC — real clickable anchors
toc = [
 ("Г1","Что нельзя вставлять в чат","ch1","03"),("Г2","Почему ответы разные","ch2","04"),
 ("Г3","Как управлять форматом ответа","ch3","05"),("Г3","Пример формата","ch3b","06"),
 ("Г4","Капстоун: сборка чат-помощника","ch4","07"),("Г4","Шаблон сборки","ch4b","08"),
 ("Г5","Кейс: обращение клиента","ch5a","09"),("Г5","Инструкция помощнику","ch5b","10"),
 ("Г5","Варианты ответа + критерии","ch5c","11"),("Г5","Неудачный ответ и исправление","ch5d","12"),
 ("Г5","Полный цикл целиком","ch5e","13"),("—","Упражнение и проверка","exercise","14"),
 ("—","Частые ошибки","errors","15"),("—","Сделай сейчас","action","16"),
 ("—","Источники","sources","17"),("—","Дальше — на курсе","course","18"),
 ("—","Путь в команду AlovLab","team","19"),("—","Контакты","contacts","20"),
]
rows = "".join(f'<a class="tocref" href="#{pid}"><div style="display:flex;align-items:baseline;gap:10px;padding:5.5px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:9pt;width:24px">{a}</span>'
               f'<span style="font-weight:600;font-size:9.8pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:9pt">{c}</span></div></a>' for a,b,pid,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Пять глав, один рабочий кейс</h1>'
    '<p class="lead">Дни 4–7 календаря AlovLab на октябрь. Оглавление кликабельно — переходит на страницу.</p>'
    f'<div style="margin-top:2px">{rows}</div>'))

# 03 Chapter 1
P.append(page("Глава 1 · Приватность", 3,
    head("Глава 1", "Что нельзя вставлять в чат",
         "Для кого: любой, кто работает с чужими данными. Результат: проверенная привычка обезличивания.")
    + '<table class="ref"><tr><th>№</th><th>Категория</th><th>Пример</th></tr>'
      '<tr><td>1</td><td><b>Пароли/доступы</b></td><td>Даже «временный» токен</td></tr>'
      '<tr><td>2</td><td><b>Договоры без обезличивания</b></td><td>ФИО, суммы, реквизиты сторон</td></tr>'
      '<tr><td>3</td><td><b>Финансы клиента</b></td><td>Выписки, доходы, платёжные данные</td></tr>'
      '<tr><td>4</td><td><b>Медданные</b></td><td>Диагнозы, история болезни</td></tr>'
      '<tr><td>5</td><td><b>Чужие личные данные</b></td><td>Телефон/адрес без согласия человека</td></tr></table>'
    + '<p class="note">Вместо этого — обезличивай: «Клиент А» вместо имени, «N рублей» вместо суммы, сохраняй только структуру задачи. Полный пример обезличивания — глава 5.</p>',
    pid="ch1"))

# 04 Chapter 2
gpt_var_src = "OpenAI Developer Community, «Why is GPT-4 giving different answers with same prompt & temperature=0?»"
gpt_var_url = "https://community.openai.com/t/why-is-gpt-4-giving-different-answers-with-same-prompt-temperature-0/143513"
P.append(page("Глава 2 · Вариативность", 4,
    head("Глава 2", "Почему ответы разные",
         "Для кого: любой пользователь ChatGPT. Результат: использовать вариативность осознанно.")
    + '<p>Модель выбирает следующее слово вероятностно, а не по жёсткой таблице — поэтому один и тот же промпт может дать разные, но одинаково валидные ответы. Это не ошибка и не признак «плохой» модели.<sup>[1]</sup></p>'
    + prompt("ПРОМПТ НА НЕСКОЛЬКО ВАРИАНТОВ",
             "[твой обычный рабочий запрос]\nДай два-три разных варианта ответа, не один. Пронумеруй их.")
    + '<div class="callout result"><div class="h">Что должно получиться</div><p>Для важного текста — выбор из нескольких вариантов, а не единственная попытка.</p></div>'
    + '<p class="note">[1] Источник — см. «Источники», стр. 17.</p>',
    pid="ch2"))
register_prompt("Глава 2 · Промпт на несколько вариантов",
                "[твой обычный рабочий запрос]\nДай два-три разных варианта ответа, не один. Пронумеруй их.")

# 05 Chapter 3a
P.append(page("Глава 3 · Формат", 5,
    head("Глава 3", "Как управлять форматом ответа",
         "Для кого: тот, кто переделывает ответы руками. Результат: формат задан заранее, не правится потом.")
    + '<div class="gb"><div class="box bad"><div class="lbl">Без формата</div>Сплошной текст — читать можно, использовать нужно после ручной переделки.</div>'
      '<div class="box good"><div class="lbl">С форматом</div>Та же просьба + «оформи как таблицу» — готовый результат сразу.</div></div>',
    pid="ch3"))

# 06 Chapter 3b
P.append(page("Глава 3 · Пример", 6,
    prompt("ШАБЛОН ФОРМАТА",
           "[твой вопрос]\nОформи ответ как: [таблица / нумерованный список / шаблон с полями: ...].")
    + '<p class="note">«Покрасивее» — не формат. Формат — это конкретная структура, которую можно назвать одним словом: таблица, список, шаблон.</p>',
    pid="ch3b"))
register_prompt("Глава 3 · Шаблон формата",
                "[твой вопрос]\nОформи ответ как: [таблица / нумерованный список / шаблон с полями: ...].")

# 07 Chapter 4a
P.append(page("Глава 4 · Капстоун", 7,
    head("Глава 4", "Капстоун: сборка личного чат-помощника",
         "Для кого: тот, кто прошёл главы G01 и G02. Результат: один настроенный чат под свою задачу.")
    + '<div class="flow"><div class="node"><b>Инструкции</b><span>роль+контекст</span></div><div class="arr">→</div>'
      '<div class="node"><b>Ограничения</b><span>+формат</span></div><div class="arr">→</div>'
      '<div class="node"><b>Проверка</b><span>3 шага Г3 (G01)</span></div><div class="arr">→</div>'
      '<div class="node"><b>Помощник</b><span>готов к работе</span></div></div>'
    + '<p>Это не новый инструмент — это настроенный разговор под конкретную повторяющуюся задачу, использующий все приёмы недели. Полный рабочий пример такого помощника — глава 5.</p>',
    pid="ch4"))

# 08 Chapter 4b — FIXED instruction bug
P.append(page("Глава 4 · Шаблон", 8,
    prompt("ШАБЛОН СБОРКИ",
           "Я [роль], моя задача: [конкретная повторяющаяся задача].\n[Контекст, который нужен для этой задачи].\nОграничения: [что нельзя].\nФормат ответа: [структура].\nЕсли данных не хватает — спрашивай, не додумывай.\nЕсли задача важная — дай мне два-три разных варианта, не один.")
    + '<div class="callout check"><div class="h">Проверка перед использованием</div><p>Помощник настроен под одну твою реальную задачу, не абстрактно «для всего».</p></div>',
    pid="ch4b"))
register_prompt("Глава 4 · Шаблон сборки чат-помощника",
                "Я [роль], моя задача: [конкретная повторяющаяся задача].\n[Контекст, который нужен для этой задачи].\nОграничения: [что нельзя].\nФормат ответа: [структура].\nЕсли данных не хватает — спрашивай, не додумывай.\nЕсли задача важная — дай мне два-три разных варианта, не один.")

# ============ Chapter 5: full worked case ============
CLIENT_MSG = ("Здравствуйте! Меня зовут Марина, мой номер +7 999 123-45-67. Веду инстаграм для своей "
              "студии маникюра, около 800 подписчиков. Очень хочу разобраться в нейросетях, но боюсь, "
              "что это сложно и дорого. С чего лучше начать?")

# 09 ch5a — intro + client message + what to remove
P.append(page("Глава 5 · Кейс", 9,
    head("Глава 5", "Полный кейс: помощник для ответов клиентам AlovLab",
         "Учебный пример от начала до конца — на вымышленном обращении. Ниже показан весь цикл: от исходного сообщения до отправленного ответа.")
    + '<div class="msg"><b>Входящее сообщение (учебный пример, не реальный клиент):</b><br>«' + CLIENT_MSG + '»</div>'
    + '<div class="redact">'
      '<div class="row cut"><b>Имя «Марина»</b><span>убрать → «Клиент А»</span></div>'
      '<div class="row cut"><b>Номер телефона</b><span>убрать полностью — не нужен для черновика ответа</span></div>'
      '<div class="row keep"><b>«Студия маникюра, ~800 подписчиков»</b><span>оставить — нужный контекст, не чувствительные данные</span></div>'
      '<div class="row keep"><b>«Боюсь, что сложно и дорого»</b><span>оставить — это и есть суть вопроса</span></div></div>'
    + '<p class="note">Правило обезличивания — то же самое, что в главе 1: убираем то, что идентифицирует человека, оставляем то, что нужно для содержательного ответа.</p>',
    pid="ch5a"))

# 10 ch5b — filled instruction + where to paste
FILLED_INSTR = ("Я готовлю черновики ответов клиентам AlovLab (курс «Нейросети и ChatGPT для каждого», Нейромонах Илья Алов).\n"
"Клиент А написал: \"Очень хочу разобраться в нейросетях, но боюсь, что это сложно и дорого. С чего лучше начать? У меня студия маникюра в инстаграме, около 800 подписчиков.\"\n"
"Составь черновик ответа. Тон простой и спокойный, без канцелярита и без давления.\n"
"Не придумывай цену, сроки или состав курса — используй только факты, которые я укажу отдельно.\n"
"Факты о курсе: 6 видеоуроков, 6 направлений (Слова, Изображения, Видео, Звук, Аватары, Знания), три тарифа с разным уровнем поддержки, гарантия возврата 14 дней.\n"
"Формат: 3-5 предложений, отвечает и на страх \"сложно\", и на вопрос \"с чего начать\", заканчивается одним конкретным следующим шагом, без \"оплатите сейчас\".\n"
"Дай два разных варианта, не один.")
P.append(page("Глава 5 · Инструкция", 10,
    prompt("ЗАПОЛНЕННАЯ ИНСТРУКЦИЯ", FILLED_INSTR)
    + '<div class="term"><b>Куда вставить и как начать.</b> <span>В тот же настроенный чат-помощник из главы 4 (или новый чат с этой инструкцией). Цену и точный состав тарифов не храни в инструкции навсегда — сверяй перед каждым использованием, тарифы могут измениться (то же правило честности, что и во всех остальных главах — см. «Источники»).</span></div>',
    pid="ch5b"))
register_prompt("Глава 5 · Заполненная инструкция помощнику (пример)", FILLED_INSTR)

# 11 ch5c — 2 example answers + comparison criteria + output format
ANSWER1 = ("Марина, это правда не так сложно, как кажется — большинство начинает с одного простого приёма "
"и уже через день видит результат. Специально для тех, кто в начале пути, есть модуль «Земля Слов» — "
"с него удобно стартовать, не тратя сразу много. Расскажите, что для вас сейчас самое узкое место — "
"тексты, фото для студии или видео?")
ANSWER2 = ("Марина, страх понятный, почти все с этого начинают. По деньгам всё прозрачно — три уровня "
"доступа, можно начать с малого и посмотреть, подходит ли формат. По содержанию курс как раз про такие "
"задачи, как ваши — тексты и визуал для соцсетей студии. Что вам сейчас важнее всего — фото, тексты "
"постов или видео-контент?")
P.append(page("Глава 5 · Варианты", 11,
    head("Глава 5", "Два варианта ответа + критерии сравнения", "Иллюстративные варианты, не результат реального теста продукта — оба сгенерированы для примера этой методички.")
    + f'<div class="io"><div class="c"><b>Вариант 1</b><p>{ANSWER1}</p></div>'
      f'<div class="c out"><b>Вариант 2</b><p>{ANSWER2}</p></div></div>'
    + '<table class="ref"><tr><th>Критерий</th><th>На что смотреть</th></tr>'
      '<tr><td><b>Честность про «сложно»</b></td><td>Конкретика вместо общих слов</td></tr>'
      '<tr><td><b>Аккуратность с ценой</b></td><td>Ни один вариант не называет цифр, которых не было в фактах</td></tr>'
      '<tr><td><b>Один следующий шаг</b></td><td>Ровно один вопрос клиенту в конце, не два-три</td></tr></table>'
    + '<div class="callout result"><div class="h">Формат результата</div><p>Черновик читает и при необходимости правит человек (Илья или менеджер) — это не автоматическая отправка без просмотра.</p></div>',
    pid="ch5c"))

# 12 ch5d — bad answer + fix
BAD = "Марина, у нас сейчас акция −50%! Курс стоит всего 14 990 ₽, успейте купить до конца недели, не упустите шанс!"
P.append(page("Глава 5 · Ошибка", 12,
    head("Глава 5", "Неудачный ответ и исправление", "")
    + '<div class="gb"><div class="box bad"><div class="lbl">Плохо</div>«' + BAD + '»</div>'
      '<div class="box good"><div class="lbl">Что не так</div>Цена и акция выдуманы — их не было в заданных фактах. «Успейте/не упустите» — давление и срочность, которая ничем не подтверждена.</div></div>'
    + '<p class="note">Исправление: убрать цену и акцию полностью (их не было в исходных фактах), убрать слова, создающие искусственную срочность, оставить открытый вопрос вместо нажима.</p>',
    pid="ch5d"))

# 13 ch5e — full cycle summary
P.append(page("Глава 5 · Итог", 13,
    head("Глава 5", "Полный цикл на одном обращении", "")
    + '<div class="flow"><div class="node"><b>Обращение</b><span>входящее</span></div><div class="arr">→</div>'
      '<div class="node"><b>Очистка</b><span>убрать личные данные</span></div><div class="arr">→</div>'
      '<div class="node"><b>Помощник</b><span>инструкция+факты</span></div><div class="arr">→</div>'
      '<div class="node"><b>2 варианта</b><span>сравнить по критериям</span></div><div class="arr">→</div>'
      '<div class="node"><b>Человек</b><span>правит и отправляет</span></div></div>'
    + '<p>Ни один шаг не пропускается: без очистки данных — риск приватности (глава 1), без сравнения вариантов — риск взять первый попавшийся (глава 2), без проверки фактов о курсе — риск выдуманной цены (глава 5, «неудачный ответ»).</p>',
    pid="ch5e"))

# 14 exercise
P.append(page("Упражнение", 14,
    head("Упражнение", "Самостоятельная практика + образец решения",
         "Пройди тот же цикл на другом обращении.")
    + '<div class="msg"><b>Задание (учебное обращение для тренировки):</b><br>«Здравствуйте, интересует автоматизация контента для нашего бренда, можно подробнее?»</div>'
    + '<div class="io"><div class="c"><b>Что сделать</b><p>Очисти данные (если есть), собери инструкцию с фактами про AlovLab Studio, получи 2 варианта, сравни, поправь.</p></div>'
      '<div class="c out"><b>Образец решения (сверить после своей попытки)</b><p>Ответ честно называет направление (AI-реклама, аватары, автоматизация — подтверждённые CLAUDE.md факты), не называет цену Studio (её нет на сайте), заканчивается одним шагом: «Отправьте бриф — ответим в течение 24 часов, [контакт студии]».</p></div></div>'
    + '<div class="callout check"><div class="h">Проверка результата</div>'
      '<div class="row">Личные данные клиента (если были) не попали в промпт.</div>'
      '<div class="row">В ответе нет цифр/акций, которых не было в заданных фактах.</div>'
      '<div class="row">Ответ оставляет ровно один следующий шаг.</div>'
      '<div class="row">Сравнил минимум 2 варианта, не взял первый попавшийся.</div></div>',
    pid="exercise"))

# 15 errors
P.append(page("Ошибки", 15,
    head("Ошибки", "Частые ошибки глав 1–5", "")
    + '<div class="fix">'
      '<div class="r"><b>Глава 1.</b> «Обезличу потом» — данные уже отправлены в сервис к моменту, когда вспомнил.</div>'
      '<div class="r"><b>Глава 2.</b> Берёшь первый ответ как единственно верный для важного текста.</div>'
      '<div class="r"><b>Глава 3.</b> Просишь «красивее» вместо конкретного формата — снова переделываешь руками.</div>'
      '<div class="r"><b>Глава 4.</b> Настраиваешь помощника «под всё сразу» — получаешь снова обобщённый инструмент.</div>'
      '<div class="r"><b>Глава 5.</b> Даёшь помощнику придумывать цену/сроки вместо того, чтобы задать факты явно — риск отправить клиенту выдумку.</div></div>',
    pid="errors"))

# 16 action
P.append(page("Сделай сейчас", 16,
    head("Действие", "Сделай сейчас", "Собери своего помощника и пройди цикл на реальном (или тренировочном) обращении.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Проверь последние 10 чатов</b> на пункты из главы 1.</div></div>'
      '<div class="step"><div class="sx"><b>Собери шаблон сборки</b> из главы 4 под одну свою повторяющуюся задачу.</div></div>'
      '<div class="step"><div class="sx"><b>Пройди полный цикл главы 5</b> на своём обращении — от очистки данных до правки человеком.</div></div></div>',
    pid="action"))

# 17 sources — real URL + date
P.append(page("Источники", 17,
    head("Источники", "Статус проверки", "Честно про то, что проверено, а что нет.")
    + f'<table class="ref"><tr><th>№</th><th>Утверждение</th><th>Источник</th></tr>'
      f'<tr><td>1</td><td>Модель отвечает по-разному на один промпт (глава 2)</td><td>{gpt_var_src}<br><a href="{gpt_var_url}">{gpt_var_url}</a><br>Дата проверки: 30.09.2026</td></tr></table>'
    + '<div class="warn"><div class="h">Остальное</div><ul>'
      '<li>Категории данных (глава 1) — общий принцип защиты персональных данных, не привязан к продукту, отдельного источника не требует.</li>'
      '<li>Факты о курсе (глава 5) — из внутреннего документа проекта (CLAUDE.md), тарифы на октябрь не переподтверждены вживую (сайт недоступен из среды на дату сборки).</li>'
      '<li>Все примеры глав 1, 2, 5 — учебные, не результат реального клиентского проекта или теста продукта.</li></ul></div>',
    pid="sources"))

# 18 course
P.append(page("Дальше", 18,
    head("Дальше", "Модуль «Земля Слов» на курсе",
         "Поддержка на курсе: закрытый Telegram-канал + ИИ-ассистент по курсу (все тарифы), личное менторство — тариф ПРО.")
    + '<div class="warn"><div class="h">Честно про цену</div><ul><li>Тарифы на октябрь не переподтверждены вживую — цену здесь не называем, проверь на alovlab.ru.</li></ul></div>',
    pid="course"))

# 19 team — softened, no unconfirmed outcome claim
P.append(page("Команда", 19,
    head("Путь дальше", "Путь в команду AlovLab",
         "Если настройка чат-помощников — то, что нравится собирать, у AlovLab есть открытый путь для сильных учеников.")
    + '<div class="team"><div class="h">Хочешь применять этот навык не только для себя?</div>'
      '<p>AlovLab открыт для учеников, которые хотят двигаться дальше отдельных приёмов: можно заявить о себе команде и претендовать на участие в реальных задачах под бренды по мере появления подходящих проектов.</p>'
      '<div class="dirs"><span>Промпт-системы</span><span>Контент-ассистенты</span><span>Автоматизация</span></div>'
      '<p style="margin-top:8px">Это путь, а не готовое место и не обещание трудоустройства — конкретные проекты появляются по мере надобности бренда, не гарантированно и не по расписанию.</p></div>',
    pid="team"))

# 20 contacts
P.append(f"""<section class="page page--dark" id="contacts" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Октябрь 2026</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Неделя 1 готова. Дальше — визуал</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Методичка G03 (дни 8–9) — кинематографичные изображения промптом. Все промпты этой методички — в prompts.txt рядом с PDF.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))

# prompts.txt export
lines = ["AlovLab · G02 «Формат и точность ответа» — все промпты этой методички, копипаст-готовые.\n"]
for title, text in PROMPTS_TXT:
    lines.append(f"### {title}\n{text}\n")
(OUTDIR / "prompts.txt").write_text("\n".join(lines), encoding="utf-8")
print("prompts.txt:", len(PROMPTS_TXT), "prompts")
