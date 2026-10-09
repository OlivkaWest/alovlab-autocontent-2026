# -*- coding: utf-8 -*-
"""AlovLab · Методичка «Формат ответа: промпты и скрипты» — углублённая версия к рилсу 06.10.2026.
Реюз G02 гл.3 в пакете рилса даёт только 2 страницы (одна техника на одном примере). Эта методичка
по явному запросу пользователя ("методичку обьемную... с проптами и скриптами") — отдельный,
более глубокий продукт: 3 полных рабочих промпта на разные типы формата (таблица/список/шаблон),
библиотека готовых "скриптов"-концовок под частые ситуации, advanced-связка с ролью/контекстом (G01).
Та же система A4-страниц + автонумерация страниц, что в guide_instagram10_build.py (во избежание
overflow полных промптов на одной странице — см. тот скрипт для истории бага).
Запуск: python3 scripts/guide_day06_format_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>
"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "reels-extra" / "day-06" / "guide"
OUTDIR.mkdir(parents=True, exist_ok=True)
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
a.tocref{color:inherit;text-decoration:none}
a.tocref:hover{text-decoration:underline}
.cont{font-size:8pt;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#cbb39d;margin-bottom:8px}
.scriptbox{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 15px;margin:9px 0}
.scriptbox .sn{display:inline-flex;align-items:center;gap:8px;margin-bottom:6px}
.scriptbox .sn b{width:24px;height:24px;border-radius:7px;background:var(--ink);color:#fff;font-size:10pt;font-weight:800;display:grid;place-items:center}
.scriptbox .sn span{font-weight:800;font-size:10.5pt;color:var(--ink)}
.scriptbox code{display:block;font-family:ui-monospace,Menlo,monospace;font-size:9.6pt;line-height:1.5;color:#8a5a2a;background:#f1e9db;border-radius:8px;padding:9px 11px;margin-top:4px}
.scriptbox p{font-size:9.3pt;color:var(--muted);margin:5px 0 0;max-width:none}
"""
CSS = V2CSS + EXTRA
TOPIC = "Формат ответа: промпты и скрипты"

def page(section, num, inner, pid=None):
    idattr = f' id="{pid}"' if pid else ''
    return (f'<section class="page"{idattr}><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main">{inner}</div>'
            f'<div class="pf"><span>AlovLab · {TOPIC}</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None):
    r = f'<div class="ru">{ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span></div>'
            f'<code>{code}</code>{r}</div>')

def script_item(n, title, code, note):
    return (f'<div class="scriptbox"><div class="sn"><b>{n}</b><span>{title}</span></div>'
            f'<code>{code}</code><p>{note}</p></div>')

PROMPTS_TXT = []
def register_prompt(title, text):
    PROMPTS_TXT.append((title, text))

CONTENT = []
def add(toc_label, toc_title, pid, section, html):
    CONTENT.append((toc_label, toc_title, pid, section, html))

# ---------- Результат ----------
add("01", "Что ты сделаешь к концу", "result", "Результат",
    head("Результат", "Что ты сделаешь к концу методички",
         "Для кого: получаешь ответ от нейронки и переделываешь его руками, прежде чем использовать.")
    + '<div class="chain" style="display:flex;align-items:center;flex-wrap:wrap;gap:6px;margin:10px 0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px">'
      '<b style="font-size:9.5pt;font-weight:800;color:var(--ink);background:var(--o-tint);border-radius:8px;padding:4px 9px">вопрос</b>'
      '<span style="color:var(--o);font-weight:800">→</span>'
      '<b style="font-size:9.5pt;font-weight:800;color:var(--ink);background:var(--o-tint);border-radius:8px;padding:4px 9px">+ строка формата</b>'
      '<span style="color:var(--o);font-weight:800">→</span>'
      '<b style="font-size:9.5pt;font-weight:800;color:var(--ink);background:var(--o-tint);border-radius:8px;padding:4px 9px">готовый результат</b></div>'
    + '<p>Рилс на 06.10 показал один приём на одном примере: добавить «оформи как таблицу» в конец вопроса. Здесь тот же приём разложен в систему: 3 типа формата с полными рабочими промптами, библиотека готовых коротких «скриптов»-концовок под частые ситуации, и как собрать формат вместе с ролью и контекстом в один мощный запрос.</p>'
    + '<div class="cards c2">'
      '<div class="card"><div class="ct">Было</div><div class="ch">Просишь «покрасивее»</div><p>Получаешь текст, который всё равно приходится переделывать руками под свою задачу.</p></div>'
      '<div class="card"><div class="ch">Стало</div><div class="ct">Просишь конкретный формат</div><p>Таблица, список или шаблон с полями, готовый к использованию сразу, без правок.</p></div></div>')

# ---------- Почему это работает ----------
add("02", "Почему это работает", "why", "Почему",
    head("Почему", "Формат это не украшение, это инструкция",
         "Коротко, без теории сверх нужного.")
    + '<p>Нейронка не читает твои мысли о том, как ты будешь использовать ответ. Без указания формата она выбирает тот вид текста, который статистически чаще всего встречался при ответе на похожие вопросы, обычно это связный абзац. Абзац удобно читать, но неудобно использовать: вставлять в таблицу, пересылать клиенту, отмечать пункты.</p>'
    + '<div class="gb"><div class="box bad"><div class="lbl">Без формата</div>«Чтобы вырасти в продажах, нужно работать над качеством продукта, развивать команду, слушать клиентов и постоянно анализировать рынок.»</div>'
      '<div class="box good"><div class="lbl">С форматом</div>Та же мысль, но в таблице: действие, как часто, кто отвечает. Три строки, видно сразу, что делать дальше.</div></div>'
    + '<p class="note">Дальше три рабочих промпта под три самых частых формата: таблица, список, шаблон с полями.</p>')

# ============ Глава 1: Таблица ============
TABLE_PROMPT = ("КОНТЕКСТ: Ты помощник, который оформляет текстовый ответ в виде таблицы для удобного использования.\n\n"
"ЦЕЛЬ: Превратить мой вопрос или уже готовый текст в таблицу с понятными столбцами без потери содержания.\n\n"
"ВХОДНЫЕ ДАННЫЕ:\n"
"Вопрос или текст: [что нужно оформить]\n"
"Нужные столбцы (если знаешь заранее): [например Что сделать, Срок, Ответственный]\n\n"
"ОГРАНИЧЕНИЯ:\n"
"Не сокращай содержание ради красоты таблицы.\n"
"Если непонятно, какие столбцы нужны, сначала предложи 2 варианта набора столбцов на выбор,\n"
"не угадывай единственный молча.\n\n"
"ЛОГИКА РАБОТЫ:\n"
"1. Найди повторяющиеся категории информации в ответе.\n"
"2. Выбери от 3 до 5 столбцов, которые реально разделяют эти категории.\n"
"3. Перенеси содержание построчно, не теряя смысл ради краткости ячеек.\n\n"
"КРИТЕРИИ КАЧЕСТВА:\n"
"Таблицу можно читать без исходного текста рядом.\n"
"Ни одна ячейка не пустая без причины.\n\n"
"ФОРМАТ ОТВЕТА:\n"
"Таблица с заголовками столбцов, одна строка пояснения под ней, почему выбраны именно эти столбцы.")
add("Г1", "Формат «Таблица»", "ch1a", "Глава 1 · Таблица",
    head("Глава 1", "Формат «Таблица»: полный промпт",
         "Для кого: вопрос содержит несколько однотипных пунктов (шаги, варианты, сравнение), которые удобнее видеть рядом, а не друг под другом в тексте.")
    + prompt("ПОЛНЫЙ ПРОМПТ · ФОРМАТ ТАБЛИЦА", TABLE_PROMPT))
register_prompt("Глава 1 · Формат «Таблица» (полный промпт)", TABLE_PROMPT)

add("Г1", "Таблица, пример", "ch1b", "Глава 1 · Пример",
    head("Глава 1", "До и после (иллюстративный пример)", "")
    + '<div class="io"><div class="c"><b>Без формата</b><p>«Для роста продаж важно: работать над продуктом, развивать команду, слушать клиентов, следить за рынком.» Абзац, не видно, с чего начать сегодня.</p></div>'
      '<div class="c out"><b>С форматом «Таблица»</b><p>Действие / Как часто / Кто отвечает. Три строки: «Проверить отзывы» еженедельно менеджер, «Сравнить цены конкурентов» раз в месяц маркетолог, «Отчёт по продажам» ежедневно продавец.</p></div></div>'
    + '<p class="note">Учебный пример для методички, не разбор реального запроса клиента AlovLab.</p>')

# ============ Глава 2: Список ============
LIST_PROMPT = ("КОНТЕКСТ: Ты помощник, который превращает ответ в чёткую последовательность шагов.\n\n"
"ЦЕЛЬ: Оформить ответ как нумерованный список действий, который можно выполнять по порядку, не перечитывая абзац целиком.\n\n"
"ВХОДНЫЕ ДАННЫЕ:\n"
"Задача: [что нужно сделать]\n"
"Сколько шагов примерно ожидаешь (если знаешь): [число или диапазон]\n\n"
"ОГРАНИЧЕНИЯ:\n"
"Каждый пункт списка, одно конкретное действие, не абзац рассуждений.\n"
"Не совмещай два разных действия в одном пункте ради короткого списка.\n\n"
"ЛОГИКА РАБОТЫ:\n"
"1. Раздели ответ на отдельные действия в порядке, в котором их нужно выполнять.\n"
"2. Начинай каждый пункт с глагола действия (сделай, проверь, напиши).\n"
"3. Если шаг требует уточнения, добавь его тут же в скобках, не отдельным абзацем ниже.\n\n"
"КРИТЕРИИ КАЧЕСТВА:\n"
"Любой шаг можно выполнить сразу, не возвращаясь к остальному тексту за контекстом.\n"
"Порядок шагов логичен, поздний шаг не требует того, что появится только в следующем.\n\n"
"ФОРМАТ ОТВЕТА:\n"
"Нумерованный список, без вступления перед ним и без вывода после.")
add("Г2", "Формат «Список»", "ch2a", "Глава 2 · Список",
    head("Глава 2", "Формат «Список»: полный промпт",
         "Для кого: нужна последовательность конкретных действий, а не рассказ про тему.")
    + prompt("ПОЛНЫЙ ПРОМПТ · ФОРМАТ СПИСОК", LIST_PROMPT))
register_prompt("Глава 2 · Формат «Список» (полный промпт)", LIST_PROMPT)

add("Г2", "Список, пример", "ch2b", "Глава 2 · Пример",
    head("Глава 2", "До и после (иллюстративный пример)", "")
    + '<div class="io"><div class="c"><b>Без формата</b><p>«Перед публикацией стоит проверить текст на ошибки, посмотреть, подходит ли обложка, и убедиться, что ссылка работает, а также свериться с планом публикаций.»</p></div>'
      '<div class="c out"><b>С форматом «Список»</b><p>1. Проверь текст на ошибки. 2. Проверь обложку под формат площадки. 3. Проверь, что ссылка открывается. 4. Сверься с планом публикаций на эту неделю.</p></div></div>'
    + '<p class="note">Учебный пример, не реальный чек-лист публикации конкретного клиента.</p>')

# ============ Глава 3: Шаблон с полями ============
TEMPLATE_PROMPT = ("КОНТЕКСТ: Ты помощник, который оформляет ответ как шаблон с заполненными полями для повторяющейся задачи.\n\n"
"ЦЕЛЬ: Превратить разовый ответ в шаблон, который я смогу использовать многократно, просто меняя значения полей.\n\n"
"ВХОДНЫЕ ДАННЫЕ:\n"
"Повторяющаяся задача: [например ответ клиенту, отчёт, бриф]\n"
"Что обычно меняется от раза к разу: [перечисли через запятую]\n\n"
"ОГРАНИЧЕНИЯ:\n"
"Поля шаблона называй словами задачи, не общими словами вроде поле 1 и поле 2.\n"
"Не включай в шаблон то, что никогда не меняется, это часть текста, а не поле.\n\n"
"ЛОГИКА РАБОТЫ:\n"
"1. Отдели в ответе то, что повторяется от раза к разу, от того, что меняется.\n"
"2. Назови каждое изменяемое место конкретным полем в квадратных скобках.\n"
"3. Собери целиком: неизменная часть плюс поля на своих местах.\n\n"
"КРИТЕРИИ КАЧЕСТВА:\n"
"Шаблон можно заполнить за 1 минуту, не задумываясь, что значит каждое поле.\n"
"Готовый результат после заполнения не требует дополнительной правки структуры.\n\n"
"ФОРМАТ ОТВЕТА:\n"
"Шаблон целиком с полями в квадратных скобках, одна строка под ним: что вписать в каждое поле.")
add("Г3", "Формат «Шаблон с полями»", "ch3a", "Глава 3 · Шаблон",
    head("Глава 3", "Формат «Шаблон с полями»: полный промпт",
         "Для кого: одна и та же задача повторяется регулярно (ответ клиенту, короткий отчёт, бриф), и каждый раз пишешь заново с нуля.")
    + prompt("ПОЛНЫЙ ПРОМПТ · ШАБЛОН С ПОЛЯМИ", TEMPLATE_PROMPT))
register_prompt("Глава 3 · Формат «Шаблон с полями» (полный промпт)", TEMPLATE_PROMPT)

add("Г3", "Шаблон, пример", "ch3b", "Глава 3 · Пример",
    head("Глава 3", "Готовый шаблон (иллюстративный пример)", "")
    + prompt("ПРИМЕР ГОТОВОГО ШАБЛОНА", "Здравствуйте, [имя клиента].\nСпасибо за вопрос про [тема вопроса].\n[Короткий ответ по сути, 2-3 предложения].\nСледующий шаг: [что сделать клиенту или нам].")
    + '<p class="note">Заполняешь только 4 поля, остальное уже написано один раз. Учебный пример, не переписка реального клиента AlovLab.</p>')

SCRIPT_LIBRARY = [
    ("Ответ клиенту", "Оформи как короткое сообщение клиенту: 1 абзац понимания его вопроса, 1 абзац решения, 1 строка следующего шага."),
    ("Контент-план", "Оформи как таблицу: Дата, Тема, Формат, Хук."),
    ("Сравнение вариантов", "Оформи как таблицу сравнения: Критерий, Вариант А, Вариант Б."),
    ("Статус задачи", "Оформи как 3 пункта: Сделано, В процессе, Дальше."),
    ("Короткая версия для сторис", "Сократи до 3 строк, каждая не длиннее 8 слов."),
]
for _n, (_title, _code) in enumerate(SCRIPT_LIBRARY, 1):
    register_prompt(f"Скрипт-библиотека {_n} · {_title}", _code)

# ---------- Скрипт-библиотека 1/2 ----------
add("04", "Скрипт-библиотека 1/2", "scripts1", "Скрипты",
    head("Библиотека", "Готовые скрипты-концовки (1/2)",
         "Не целый промпт, а одна строка, которую добавляешь в конец своего обычного рабочего запроса.")
    + script_item(1, "Ответ клиенту", "Оформи как короткое сообщение клиенту: 1 абзац понимания его вопроса, 1 абзац решения, 1 строка следующего шага.", "Для переписки, где нужен готовый к отправке текст, не разбор темы.")
    + script_item(2, "Контент-план", "Оформи как таблицу: Дата, Тема, Формат, Хук.", "Для планирования публикаций на неделю или месяц вперёд.")
    + script_item(3, "Сравнение вариантов", "Оформи как таблицу сравнения: Критерий, Вариант А, Вариант Б.", "Когда выбираешь между двумя или тремя опциями и нужно видеть разницу рядом."),
    )

# ---------- Скрипт-библиотека 2/2 ----------
add("05", "Скрипт-библиотека 2/2", "scripts2", "Скрипты",
    head("Библиотека", "Готовые скрипты-концовки (2/2)", "")
    + script_item(4, "Статус задачи", "Оформи как 3 пункта: Сделано, В процессе, Дальше.", "Для апдейта себе или команде без длинного пересказа.")
    + script_item(5, "Короткая версия для сторис", "Сократи до 3 строк, каждая не длиннее 8 слов.", "Когда тот же ответ нужен в сторис или подписи, не только в полном виде.")
    + '<div class="callout result"><div class="h">Как использовать библиотеку</div><p>Один скрипт, одна строка в конце твоего обычного запроса. Не нужно переписывать весь промпт заново под каждую ситуацию, меняется только последняя строка.</p></div>')

# ---------- Advanced ----------
ADV_PROMPT = ("Я [роль, например менеджер поддержки]. Моя задача: [повторяющаяся задача].\n"
"Контекст: [что нужно знать для этой задачи].\n"
"Ограничения: [что нельзя].\n"
"Формат ответа: [таблица / список / шаблон с полями, конкретно какой].\n"
"Если данных не хватает, спрашивай, не додумывай.")
add("06", "Advanced: формат + роль", "adv", "Advanced",
    head("Advanced", "Формат вместе с ролью и контекстом",
         "Три приёма вместе сильнее, чем каждый по отдельности: роль и контекст из методички G01, формат из этой.")
    + prompt("ПРОМПТ · РОЛЬ + КОНТЕКСТ + ФОРМАТ", ADV_PROMPT)
    + '<div class="callout check"><div class="h">Почему это сильнее одного формата</div>'
      '<div class="row">Роль и контекст определяют, что отвечать, формат определяет, в каком виде это прийдёт.</div>'
      '<div class="row">Настроив один раз такой запрос под свою регулярную задачу, дальше меняешь только входные данные, не структуру.</div></div>')
register_prompt("Advanced · Формат + роль + контекст", ADV_PROMPT)

# ---------- Чек-лист ----------
add("07", "Проверь себя", "check", "Проверь себя",
    head("Checklist", "Проверь себя",
         "Пройди по пунктам после первого реального использования.")
    + '<div class="callout check">'
      '<div class="row">В конце своего обычного запроса добавил одну строку формата, не переписал весь промпт.</div>'
      '<div class="row">Выбрал формат под задачу (таблица для сравнения, список для шагов, шаблон для повторяющегося), не наугад.</div>'
      '<div class="row">Результат пришёл готовым к использованию, без ручной переделки структуры.</div>'
      '<div class="row">Хотя бы один скрипт из библиотеки сохранил себе отдельно для повторного использования.</div></div>')

# ---------- Частые ошибки ----------
add("08", "Частые ошибки", "errors", "Ошибки",
    head("Ошибки", "Частые ошибки", "")
    + '<div class="fix">'
      '<div class="r"><b>Просишь «покрасивее».</b> Это не формат, это пожелание, модель не знает, что с ним делать конкретно.</div>'
      '<div class="r"><b>Формат «Таблица» на длинном рассуждении.</b> Если мысль одна и неразделимая, таблица из одной строки не нужна, оставь текст.</div>'
      '<div class="r"><b>Шаблон с общими полями.</b> «Поле 1», «поле 2» вместо конкретных названий, через месяц сам не вспомнишь, что куда вписывать.</div>'
      '<div class="r"><b>Один и тот же формат на всё.</b> Таблица хороша для сравнения, не для короткого ответа клиенту, выбирай под задачу.</div></div>')

# ---------- Сделай сейчас ----------
add("09", "Сделай сейчас", "action", "Сделай сейчас",
    head("Действие", "Сделай сейчас",
         "Пройди за один присест, не откладывай.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Возьми свой последний рабочий запрос</b> к нейронке, на который пришёл неудобный абзац.</div></div>'
      '<div class="step"><div class="sx"><b>Добавь одну строку формата</b> из глав 1-3 или скрипт-библиотеки, подходящий под задачу.</div></div>'
      '<div class="step"><div class="sx"><b>Сохрани себе</b> тот скрипт, который сработал, под свою частую задачу.</div></div></div>')

# ---------- Источники ----------
add("10", "Источники", "sources", "Источники",
    head("Источники", "Честно про примеры в этой методичке", "")
    + '<div class="warn"><div class="h">Статус примеров</div><ul>'
      '<li>Все примеры глав 1-3 и скрипт-библиотеки (ответ клиенту, контент-план, статус задачи) — иллюстративные, собраны для методички, не разбор реальных задач клиентов AlovLab.</li>'
      '<li>Основная техника (одна строка формата в конце промпта) — та же, что показана в рилсе на 06.10.2026 и в методичке G02, глава 3; здесь расширена с одного примера до системы из 3 форматов и 5 готовых скриптов.</li></ul></div>')

# ---------- Курс ----------
add("11", "Дальше — на курсе", "course", "Дальше",
    head("Дальше", "Модуль «Земля Слов» на курсе",
         "Управление форматом ответа, часть промпт-инжиниринга, который разбирается на курсе подробнее, с заданиями и проверкой.")
    + '<p>Курс «Нейросети и ChatGPT для каждого»: 6 видеоуроков, 6 «Земель» (Слова, Изображения, Видео, Звук, Аватары, Знания). Поддержка: закрытый Telegram-канал и ИИ-ассистент по курсу на всех тарифах, личное менторство на тарифе ПРО.</p>'
    + '<div class="warn"><div class="h">Честно про цену</div><ul><li>Цену и состав тарифов проверяй на alovlab.ru перед тем как называть клиенту, здесь намеренно не фиксируем.</li></ul></div>')

# ---------- Команда ----------
add("12", "Путь в команду AlovLab", "team", "Команда",
    head("Путь дальше", "Путь в команду AlovLab",
         "Если тебе заходит настраивать такие системы не только для себя, у AlovLab есть открытый путь для сильных учеников.")
    + '<div class="team"><div class="h">Хочешь применять этот навык не только для себя?</div>'
      '<p>AlovLab открыт для учеников, которые хотят двигаться дальше отдельных приёмов: можно заявить о себе команде и претендовать на участие в реальных задачах под бренды по мере появления подходящих проектов.</p>'
      '<div class="dirs"><span>Промпт-системы</span><span>Контент-ассистенты</span><span>Автоматизация</span></div>'
      '<p style="margin-top:8px">Это путь, а не готовое место и не обещание трудоустройства: конкретные проекты появляются по мере надобности бренда, не гарантированно и не по расписанию.</p></div>')

# ============================================================
# Сборка
# ============================================================
P = []
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практическая методичка</div>
    <h1 style="font-weight:800;font-size:28pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:17ch">Формат ответа: промпты и скрипты</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Углублённая версия к рилсу 06.10.2026. 3 полных рабочих промпта, 5 готовых скриптов-концовок, связка с ролью и контекстом.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 формата</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">5 скриптов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Advanced-связка</span>
    </div>
  </div>
</section>""")

FIRST_CONTENT_NUM = 3
toc_rows = []
numbered = []
for i, (label, title, pid, section, html) in enumerate(CONTENT):
    num = FIRST_CONTENT_NUM + i
    numbered.append((label, title, pid, section, html, num))
    toc_rows.append(
        f'<a class="tocref" href="#{pid}"><div style="display:flex;align-items:baseline;gap:10px;padding:5.5px 0;border-bottom:1px solid var(--line2)">'
        f'<span style="font-weight:800;color:var(--o);font-size:9pt;width:24px">{label}</span>'
        f'<span style="font-weight:600;font-size:9.8pt;color:var(--ink)">{title}</span>'
        f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
        f'<span style="font-weight:700;color:var(--muted);font-size:9pt">{num:02d}</span></div></a>')

P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Формат ответа, системой</h1>'
    '<p class="lead">Рилс показал один приём на одном примере. Здесь, система из 3 форматов, библиотека готовых скриптов и advanced-связка с ролью и контекстом.</p>'
    f'<div style="margin-top:2px">{"".join(toc_rows)}</div>'))

for label, title, pid, section, html, num in numbered:
    P.append(page(section, num, html, pid=pid))

P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Формат это инструкция, не украшение</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Все промпты и скрипты этой методички — копипаст-готовые в prompts.txt рядом с этим файлом.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))

lines = ["AlovLab · «Формат ответа: промпты и скрипты» — все промпты и скрипты методички, копипаст-готовые.\n"]
for title, text in PROMPTS_TXT:
    lines.append(f"### {title}\n{text}\n")
(OUTDIR / "prompts.txt").write_text("\n".join(lines), encoding="utf-8")
print("prompts.txt:", len(PROMPTS_TXT), "prompts")
