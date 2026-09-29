# -*- coding: utf-8 -*-
"""AlovLab · 30-дневная система · День 1 · «5 настроек ChatGPT, которые меняют каждый ответ» (премиум-PDF).
По GLOBAL-METHODOLOGY-RULE: паспорт урока, готовый пример, метод, инструменты, пошаговый урок,
промпты, разбор до/после, практика, ошибки, чек-лист, материалы, применение, итог, источники.
Запуск: python3 scripts/guide_30days_day01_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "plans" / "2026-09-29_30-days" / "days" / "day-01"
OUT = OUTDIR / "workbook.html"

EXTRA = r"""
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.3pt;line-height:1.4;color:var(--ink);margin-top:3px;max-width:none}
table.ref{width:100%;border-collapse:separate;border-spacing:0;margin:9px 0;font-size:9pt;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
table.ref th{background:var(--ink);color:#fff;font-weight:800;text-transform:uppercase;letter-spacing:.04em;font-size:7.4pt;text-align:left;padding:8px 10px}
table.ref td{padding:6.5px 10px;border-top:1px solid var(--line2);color:var(--body);vertical-align:top;line-height:1.3}
table.ref td b{color:var(--ink)}
table.ref tr:nth-child(even) td{background:#fbf7f0}
.warn{background:#13100a;border-radius:14px;padding:15px 18px;margin:10px 0;color:#f4efe6}
.warn .h{font-weight:800;font-size:10pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o2);margin-bottom:7px}
.warn ul{margin:0;padding-left:0;list-style:none}
.warn li{position:relative;padding:4px 0 4px 20px;font-size:9.5pt;line-height:1.42;color:#eae4da;max-width:none}
.warn li:before{content:"!";position:absolute;left:0;color:var(--o2);font-weight:800}
.fix{display:grid;gap:8px;margin:10px 0}
.fix .r{background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 13px;font-size:9.8pt;line-height:1.45;color:var(--body)}
.fix .r b{color:var(--ink)}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · 5 настроек ChatGPT</span>'
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
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">30 дней · День 1 из 30</div>
    <h1 style="font-weight:800;font-size:28pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:17ch">5 настроек ChatGPT, которые меняют каждый ответ</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Настрой личный контекст один раз — вместо того чтобы объяснять его в каждом новом чате.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">15–20 минут</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Базовый уровень</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Готовый шаблон внутри</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("А","Паспорт урока","03"),("Б","Готовый результат","03"),("В","Как устроен метод","04"),
 ("Г","Инструменты и подготовка","04"),("Д","Шаг 1–2: инструкции и память","05"),
 ("Д","Шаг 3–4: проекты и модель","06"),("Д","Шаг 5: временный чат","07"),
 ("Е","Готовые промпты","08"),("Ж","Разбор одного примера","09"),
 ("З","Самостоятельная практика","10"),("И","Ошибки и исправления","10"),
 ("К","Проверка результата","11"),("Л","Рабочие материалы","11"),
 ("М","Применение в работе","12"),("Н","Итог и следующий шаг","12"),
 ("О","Источники и статус проверки","13"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:10px;padding:6px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:9.5pt;width:22px">{a}</span>'
               f'<span style="font-weight:600;font-size:10.3pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:9.5pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Маршрут урока</h1>'
    '<p class="lead">От паспорта урока до полного чек-листа — 13 разделов, один практический результат.</p>'
    f'<div style="margin-top:4px">{rows}</div>'))

# 03 Паспорт + Готовый результат
P.append(page("А–Б · Паспорт", 3,
    head("Раздел А", "Паспорт урока",
         "Для кого, что решаем, что получится на выходе — прежде чем открывать настройки.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Для кого</div><div class="ch">Любой пользователь ChatGPT</div><p>Пользуешься больше месяца и получаешь усреднённые ответы «как для всех».</p></div>'
      '<div class="card"><div class="ct">Задача</div><div class="ch">Настроить контекст один раз</div><p>Вместо того чтобы объяснять себя в каждом новом чате.</p></div>'
      '<div class="card"><div class="ct">Время</div><div class="ch">15–20 минут</div><p>Базовый уровень, без технической подготовки.</p></div></div>'
    + '<div class="hr"></div>'
    + head("Раздел Б", "Готовый результат", "Учебный пример заполненных кастомных инструкций — не твои личные данные, а образец структуры.")
    + prompt("УЧЕБНЫЙ ПРИМЕР · СКОПИРОВАТЬ",
             "Я фрилансер-маркетолог, работаю с малым бизнесом в сфере услуг.\nОтвечай кратко, по делу, без вступлений вроде \"конечно!\" и \"отличный вопрос!\".\nЕсли данных не хватает для точного ответа — спрашивай, а не додумывай за меня.\nТехнические термины объясняй простыми словами, я не программист.\nКогда даёшь план действий — нумеруй шаги, не пиши сплошным текстом.")
    ))

# 04 Метод + Инструменты
P.append(page("В–Г · Метод", 4,
    head("Раздел В", "Как устроен метод",
         "По умолчанию ChatGPT не хранит ничего личного между чатами. Пять настроек это меняют.")
    + '<p>Что решает человек: какой контекст дать, как назвать проекты, какую модель выбрать. Что делает нейросеть: применяет контекст автоматически, пока настройки включены. Что нужно проверять вручную: память иногда хранит устаревшие факты — это не чинится само.</p>'
    + '<div class="hr"></div>'
    + head("Раздел Г", "Инструменты и подготовка", "Платных инструментов не требуется — только сам ChatGPT.")
    + '<div class="warn"><div class="h">Проверить перед публикацией</div><ul>'
      '<li>Состав функций по бесплатному/платным тарифам может отличаться и меняется со временем.</li>'
      '<li>Точные названия пунктов меню — сверить с текущим интерфейсом на дату публикации.</li></ul></div>'))

# 05 Шаг 1-2
P.append(page("Д · Шаги 1–2", 5,
    head("Шаг 1", "Кастомные инструкции",
         "Единственное место, которое ChatGPT читает в каждом новом чате без напоминаний.")
    + '<div class="io"><div class="c"><b>Что вводим</b><p>Роль/задача + 2–4 правила стиля ответа.</p></div>'
      '<div class="c out"><b>Как проверить</b><p>Новый чат, нейтральный вопрос — ответ пришёл в заданном тоне?</p></div></div>'
    + '<div class="term"><b>Если не получилось.</b> <span>Проверь, что поле реально сохранилось — выйди из настроек и открой заново.</span></div>'
    + '<div class="hr"></div>'
    + head("Шаг 2", "Память", "Без неё каждый чат — разговор с человеком, который видит тебя впервые.")
    + '<div class="io"><div class="c"><b>Что вводим</b><p>Ничего сразу — заполняется по ходу разговоров, либо прямо: «Запомни, что я...».</p></div>'
      '<div class="c out"><b>Как проверить</b><p>Вопрос «что ты знаешь обо мне» в новом чате.</p></div></div>'))

# 06 Шаг 3-4
P.append(page("Д · Шаги 3–4", 6,
    head("Шаг 3", "Проекты", "Одна папка на одну задачу вместо тридцати разрозненных чатов.")
    + '<div class="io"><div class="c"><b>Что вводим</b><p>Название проекта по задаче + первые чаты внутрь.</p></div>'
      '<div class="c out"><b>Как проверить</b><p>Через день открой проект — вчерашний разговор на месте без поиска.</p></div></div>'
    + '<div class="hr"></div>'
    + head("Шаг 4", "Модель под задачу", "Быстрая экономит время. С рассуждением — точность на сложной задаче.")
    + '<table class="ref"><tr><th>Задача</th><th>Модель</th></tr>'
      '<tr><td>Быстрый фактический вопрос</td><td><b>Быстрая</b></td></tr>'
      '<tr><td>Многошаговый план/стратегия</td><td><b>С рассуждением</b></td></tr>'
      '<tr><td>Разовый черновик текста</td><td><b>Быстрая</b></td></tr>'
      '<tr><td>Анализ большого объёма условий</td><td><b>С рассуждением</b></td></tr></table>'))

# 07 Шаг 5
P.append(page("Д · Шаг 5", 7,
    head("Шаг 5", "Временный чат", "Не сохраняется и не используется для памяти — для приватного и разового.")
    + '<div class="io"><div class="c"><b>Что вводим</b><p>Любой тестовый вопрос во временном режиме.</p></div>'
      '<div class="c out"><b>Как проверить</b><p>После закрытия — новый обычный чат не должен «помнить» его содержание.</p></div></div>'
    + '<div class="term"><b>Не путать.</b> <span>«Не сохраняется после закрытия» и «не помнит внутри одного открытого диалога» — разные вещи. Пока чат открыт, он держит контекст внутри себя нормально.</span></div>'))

# 08 Промпты
P.append(page("Е · Промпты", 8,
    head("Раздел Е", "Готовые промпты", "Шаблон с переменными + заполненный пример + промпты для проверки.")
    + prompt("ШАБЛОН · СКОПИРОВАТЬ",
             "Я [твоя роль/профессия]. Отвечай [кратко / развёрнуто], [формат: шаги / списки / текст].\nЕсли данных не хватает — [спрашивай / делай предположение и указывай его].\n[Своё правило, например: без канцелярита].")
    + prompt("ПРОВЕРКА ПАМЯТИ · СКОПИРОВАТЬ",
             "Что ты знаешь обо мне на основе наших прошлых разговоров? Перечисли конкретно, без общих фраз.")
    ))

# 09 Разбор примера
P.append(page("Ж · Разбор", 9,
    head("Раздел Ж", "Полный разбор одного примера", "Иллюстративный пример, не результат реального теста продукта.")
    + '<div class="gb"><div class="box bad"><div class="lbl">До настройки</div>«Как мне написать пост для соцсетей о новой услуге?» → общий совет: «расскажите о преимуществах, добавьте призыв к действию» — годится всем и никому конкретно.</div>'
      '<div class="box good"><div class="lbl">После настройки</div>Тот же вопрос → ответ учитывает нишу (малый бизнес услуг), тон без канцелярита, формат по шагам — как задано в инструкциях.</div></div>'
    + '<p class="note">Разница не в «более умном» ChatGPT — в том, что не нужно вручную адаптировать общий совет под свою ситуацию каждый раз.</p>'))

# 10 Практика + Ошибки start
P.append(page("З–И · Практика и ошибки", 10,
    head("Раздел З", "Самостоятельная практика",
         "Заполни инструкции, включи память, создай проект. Задай один рабочий вопрос до/после.")
    + '<div class="callout result"><div class="h">Что должно получиться</div><p>Заполненные инструкции, включённая память (проверено вопросом), один проект с чатом внутри.</p></div>'
    + '<div class="hr"></div>'
    + head("Раздел И", "Ошибки и исправления", "Пять симптомов, с которыми реально сталкиваются на этом уроке.")
    + '<div class="fix">'
      '<div class="r"><b>Ответы не меняются.</b> Поле не сохранилось — выйди из настроек и открой заново.</div>'
      '<div class="r"><b>Ссылается на устаревшее.</b> Память не чистится сама — удали вручную в списке воспоминаний.</div>'
      '<div class="r"><b>Не видно модели с рассуждением.</b> Может быть ограничением тарифа/региона, не ошибкой.</div></div>'))

# 11 Ошибки cont + Проверка + Материалы
P.append(page("И–Л · Проверка и материалы", 11,
    '<div class="fix">'
    '<div class="r"><b>Временный чат «помнит».</b> Это нормально внутри одного открытого диалога — путают с памятью между чатами.</div>'
    '<div class="r"><b>Инструкции не работают в проекте.</b> У проекта может быть свой контекст поверх общих настроек.</div></div>'
    + '<div class="hr"></div>'
    + head("Раздел К", "Проверка результата", "Наблюдаемые критерии, не «получилось красиво».")
    + '<div class="callout check"><div class="h">Чек-лист</div>'
      '<div class="row">Инструкции заполнены и остаются на месте после повторного открытия.</div>'
      '<div class="row">На «что ты знаешь обо мне» — конкретные факты, не общие фразы.</div>'
      '<div class="row">Создан минимум один проект с чатом внутри.</div>'
      '<div class="row">Могу назвать пример задачи под каждую модель.</div></div>'))

# 12 Применение + Итог
P.append(page("М–Н · Применение", 12,
    head("Раздел М", "Применение в работе",
         "Не отдельная услуга — фундамент, который экономит время каждый день.")
    + '<p>Фрилансер с несколькими клиентами использует проекты, чтобы не путать контекст. Автор контента — инструкции, чтобы голос бренда не плыл между чатами. Это также база для дня 4 (промпт-система) и дня 23 (личный агент) этого месяца.</p>'
    + '<div class="hr"></div>'
    + head("Раздел Н", "Итог и следующий шаг", "Личный контекст настроен. Дальше — точечная настройка под каждую задачу.")
    + '<p>День 2: «Роль решает всё» — как формулировка роли в самом промпте меняет качество конкретного ответа.</p>'))

# 13 Источники
P.append(page("О · Источники", 13,
    head("Раздел О", "Источники и статус проверки",
         "Честно про то, что проверено, а что нет.")
    + '<div class="warn"><div class="h">Статус проверки</div><ul>'
      '<li>Составлено по общедоступной, широко документированной механике ChatGPT — не редкие функции.</li>'
      '<li>Точные названия пунктов меню и доступность по тарифам НЕ проверялись напрямую в интерфейсе на 29.09.2026.</li>'
      '<li>Требуется точечная проверка непосредственно перед публикацией.</li>'
      '<li>Оба примера (разделы Б и Ж) — учебные, не результат реального теста продукта.</li></ul></div>'))

# 14 Contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · 30 дней · День 1 из 30</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Настрой один раз. Дальше — точнее каждый день.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">День 2 продолжает эту же мысль на уровне промпта. Вопросы и разбор — в Telegram.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))
