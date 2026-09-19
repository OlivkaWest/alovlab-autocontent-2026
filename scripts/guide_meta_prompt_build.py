# -*- coding: utf-8 -*-
"""AlovLab · методичка «Мета-промпт: ИИ пишет промпты за тебя» (премиум-PDF, фикс-A4).
По GLOBAL-METHODOLOGY-RULE: реальный workflow, мета-промпт с уровнями, как отвечать на вопросы,
плохо/хорошо, честность (garbage in garbage out), action+check, мост в Землю Слов + путь в команду.
Запуск: python3 scripts/guide_meta_prompt_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "meta-prompt"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-meta-prompt.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.midwrap{width:100%}
.lvls{margin:10px 0 2px}
.lvls .row{display:grid;grid-template-columns:120px 1fr;gap:10px;align-items:start;margin:7px 0}
.lvls .row .k{font-weight:800;font-size:9pt;color:var(--o);padding-top:2px}
.lvls .row p{margin:0;font-size:9.8pt;line-height:1.42;color:var(--body)}
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
.warn{background:#13100a;border-radius:14px;padding:15px 18px;margin:10px 0;color:#f4efe6}
.warn .h{font-weight:800;font-size:10pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o2);margin-bottom:7px}
.warn ul{margin:0;padding-left:0;list-style:none}
.warn li{position:relative;padding:4px 0 4px 20px;font-size:9.5pt;line-height:1.42;color:#eae4da;max-width:none}
.warn li:before{content:"✕";position:absolute;left:0;color:var(--o2);font-weight:800}
.warn li.ok:before{content:"✔"}
.qa{display:grid;gap:8px;margin:10px 0}
.qa .q{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.qa .q b{font-weight:800;font-size:9.5pt;color:var(--o)}
.qa .q p{margin:2px 0 0;font-size:9.5pt;line-height:1.4;color:var(--ink);max-width:none}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · мета-промпт</span>'
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
  <div style="position:absolute;right:6%;top:24%;width:52%;height:34%;border-radius:16px;border:1px solid rgba(255,140,60,.28);background:linear-gradient(160deg,rgba(255,140,60,.10),rgba(255,140,60,0))"></div>
  <div style="position:absolute;right:10%;top:29%;width:44%;color:#ffb98a;font-family:ui-monospace,monospace;font-size:9pt;line-height:1.5">&gt; собери мне промпт...<br>&gt; какая цель?<br>&gt; кто аудитория?<br><span style="color:var(--o2)">&gt; готовый промпт ✓</span></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд</div>
    <h1 style="font-weight:800;font-size:32pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Мета-промпт: ИИ пишет промпты за тебя</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:40ch">Один промпт, который превращает нейросеть в твоего промпт-инженера. Ты описываешь задачу словами, сильный промпт собирает она.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Готовый мета-промпт</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Уровни</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Примеры</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("01","Что ты получишь","03"),("02","Почему промпты слабые","04"),("03","Что такое мета-промпт","05"),
 ("04","Метод: 4 шага","06"),("05","Сам мета-промпт","07"),
 ("06","Как отвечать на вопросы","08"),("07","Пример: слабо → сильно","09"),
 ("08","Где применять","10"),("09","Честно: мусор на входе","11"),
 ("10","Ошибки и фиксы","12"),("11","Сделай сейчас + проверка","13"),
 ("12","Дальше — на курсе","14"),("13","Путь в команду AlovLab","15"),("14","Контакты","16"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:12px;padding:8px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:10pt;width:26px">{a}</span>'
               f'<span style="font-weight:600;font-size:11.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:10pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Маршрут гайда</h1>'
    '<p class="lead">Четырнадцать шагов: от слабых запросов до промпт-машины, которая работает на тебя.</p>'
    f'<div style="margin-top:6px">{rows}</div>'))

# 03 result
P.append(page("Шаг 01 · Результат", 3,
    head("Шаг 01", "Что ты получишь", "Не десять промптов, а одну машину: нейросеть, которая сама собирает тебе сильный промпт под любую задачу.")
    + '<div class="flow"><div class="node"><b>Вставь</b><span>мета-промпт</span></div><div class="arr">→</div>'
      '<div class="node"><b>Ответь</b><span>на вопросы</span></div><div class="arr">→</div>'
      '<div class="node"><b>Получи</b><span>промпт</span></div><div class="arr">→</div>'
      '<div class="node"><b>Используй</b><span>результат</span></div></div>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Что это</div><div class="ch">Промпт-инженер</div><p>Нейросеть берёт роль и собирает промпт за тебя.</p></div>'
      '<div class="card"><div class="ct">Для чего</div><div class="ch">Любая задача</div><p>Тексты, картинки, код, видео-промпты, письма, посты.</p></div>'
      '<div class="card"><div class="ct">Сложность</div><div class="ch">Одна вставка</div><p>Копируешь мета-промпт один раз и пользуешься всегда.</p></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>Ты описываешь задачу простыми словами, нейросеть задаёт пару уточнений и выдаёт готовый промпт одним блоком. Дальше он делает результат заметно лучше твоих обычных запросов.</p></div>'))

# 04 why weak
P.append(page("Шаг 02 · Почему", 4,
    head("Шаг 02", "Почему твои промпты слабые", "Дело не в секретных словах. Дело в рамке, которую ты не задаёшь.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Миф</div><b>«Есть волшебные слова, которые надо знать.»</b> Люди копят чужие промпты и всё равно получают воду.</div>'
      '<div class="box good"><div class="lbl">Как есть</div><b>Нейросети не хватает рамки:</b> цель, аудитория, формат, ограничения. Дай рамку и ответ меняется.</div></div>'
    + '<p>Мета-промпт решает это за тебя: он заставляет нейросеть сначала выяснить рамку (задать вопросы), а потом собрать промпт. Ты не обязан знать, как формулировать. Формулирует она.</p>'
    + '<div class="term"><b>Честно.</b> <span>Мета-промпт не заменяет смысл. Если задача сырая, промпт будет аккуратный, но пустой. Сила в том, что вопросы вытаскивают из тебя детали, о которых ты бы не подумал.</span></div>'))

# 05 what is
P.append(page("Шаг 03 · Суть", 5,
    head("Шаг 03", "Что такое мета-промпт", "Это промпт, который делает промпты. Один раз настроил, дальше пользуешься.")
    + '<div class="mns"><div class="m move"><div class="h">Обычный промпт</div><p>Ты пишешь задачу и надеешься, что нейросеть догадается. Часто получаешь воду.</p></div>'
      '<div class="m stay"><div class="h">Мета-промпт</div><p>Ты просишь нейросеть стать промпт-инженером: она уточняет рамку и выдаёт готовый промпт.</p></div></div>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Роль.</b> Нейросеть становится промпт-инженером.</div></div>'
      '<div class="step"><div class="sx"><b>Вопросы.</b> Сначала выясняет цель, аудиторию, формат, детали.</div></div>'
      '<div class="step"><div class="sx"><b>Сборка.</b> Выдаёт финальный промпт одним блоком, готовый к копированию.</div></div>'
      '<div class="step"><div class="sx"><b>Объяснение.</b> Коротко говорит, что в промпте важно, чтобы ты понимал.</div></div></div>'))

# 06 method
P.append(page("Шаг 04 · Метод", 6,
    head("Шаг 04", "Метод: 4 шага", "Работает в любой нейросети с чатом (ChatGPT, Claude и др.).")
    + '<div class="scene"><div class="sn">1</div><div><div class="sh">Вставь мета-промпт</div><div class="sd">Скопируй его со следующей страницы и отправь в чат.</div></div><span class="stag">Вставка</span></div>'
    + '<div class="scene"><div class="sn">2</div><div><div class="sh">Ответь на вопросы</div><div class="sd">Нейросеть задаёт 3–5 уточнений. Отвечай простыми словами.</div></div><span class="stag">Рамка</span></div>'
    + '<div class="scene"><div class="sn">3</div><div><div class="sh">Получи промпт</div><div class="sd">Она выдаёт готовый промпт одним блоком. Копируешь.</div></div><span class="stag">Промпт</span></div>'
    + '<div class="scene"><div class="sn">4</div><div><div class="sh">Используй</div><div class="sd">Запускаешь этот промпт и получаешь сильный результат.</div></div><span class="stag">Результат</span></div>'
    + '<div class="callout check"><div class="h">Правило</div>'
      '<div class="row">Не пропускай вопросы. Именно они превращают сырую задачу в сильный промпт.</div>'
      '<div class="row">Отвечай честно и коротко. Нет ответа — так и напиши, нейросеть подставит разумное по умолчанию.</div></div>'))

# 07 the meta prompt
meta = ("Ты опытный промпт-инженер. Я опишу задачу простыми словами, а ты соберёшь для меня сильный промпт. "
        "Сначала задай мне 3–5 коротких уточняющих вопросов о цели, аудитории, формате ответа, тоне и важных деталях. "
        "Дождись моих ответов. После этого выдай финальный промпт одним блоком, готовым к копированию, "
        "а под ним коротко объясни, что в нём ключевое и как его можно докрутить. Моя задача: [ОПИШИ ЗАДАЧУ].")
P.append(page("Шаг 05 · Промпт", 7,
    head("Шаг 05", "Сам мета-промпт", "Скопируй, вставь в чат, в конце опиши свою задачу в [СКОБКАХ].")
    + prompt("Мета-промпт · СКОПИРОВАТЬ", meta)
    + '<div class="io"><div class="c"><b>Что вставить</b><p>В [ОПИШИ ЗАДАЧУ] — свою задачу простыми словами: «пост про запуск курса», «промпт для фото», «письмо клиенту».</p></div>'
      '<div class="c out"><b>Что получить</b><p>Пару вопросов, а затем готовый промпт одним блоком плюс объяснение, что в нём важно.</p></div></div>'
    + '<div class="lvls"><div class="row"><span class="k">Быстрый</span><p>Отправь как есть. Хватит для большинства задач.</p></div>'
      '<div class="row"><span class="k">Про</span><p>Добавь: «предложи два варианта промпта: короткий и подробный».</p></div>'
      '<div class="row"><span class="k">Advanced</span><p>Добавь: «учитывай ограничения модели и добавь в промпт критерии проверки результата».</p></div></div>'))

# 08 how to answer
P.append(page("Шаг 06 · Ответы", 8,
    head("Шаг 06", "Как отвечать на вопросы ИИ", "Пять рамок, которые решают качество промпта. Отвечай по ним.")
    + '<div class="qa">'
      '<div class="q"><b>Цель</b><p>Что должно произойти после. Продать, объяснить, развлечь, собрать заявки.</p></div>'
      '<div class="q"><b>Аудитория</b><p>Кто читает. Новичок, эксперт, клиент, подписчик. Их язык и боль.</p></div>'
      '<div class="q"><b>Формат</b><p>Что на выходе. Пост, список, таблица, сценарий, письмо, длина.</p></div>'
      '<div class="q"><b>Тон</b><p>Как звучать. Живой, строгий, дружеский, экспертный, без канцелярита.</p></div>'
      '<div class="q"><b>Детали</b><p>Факты, цифры, примеры, что обязательно включить и чего избегать.</p></div></div>'
    + '<p class="note">Не знаешь ответ — напиши «на твоё усмотрение». Нейросеть подставит разумное и объяснит выбор.</p>'))

# 09 example
P.append(page("Шаг 07 · Пример", 9,
    head("Шаг 07", "Пример: слабо и сильно", "Одна задача, два подхода. Разница в рамке.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Слабый запрос</div>«Напиши пост про мой курс.»<br><br>Нейросеть не знает цель, аудиторию, тон. Выходит общий текст ни о чём.</div>'
      '<div class="box good"><div class="lbl">Через мета-промпт</div>Вопросы: цель, аудитория, формат, тон. Ответы: «продать курс новичкам, пост для Telegram, живой тон, без канцелярита». Промпт собран под это.</div></div>'
    + '<p>Мета-промпт не пишет за тебя смысл. Он достаёт из тебя рамку и складывает её в чёткий промпт, который нейросеть понимает однозначно.</p>'
    + '<div class="callout result"><div class="h">Итог</div><p>Тот же запрос, но с рамкой, даёт текст под конкретную задачу, а не воду. И так с любой задачей: картинки, код, письма, сценарии.</p></div>'))

# 10 where
P.append(page("Шаг 08 · Применение", 10,
    head("Шаг 08", "Где применять", "Мета-промпт работает везде, где ты пишешь запрос нейросети.")
    + '<div class="cards c2">'
      '<div class="card"><div class="ct">Тексты</div><div class="ch">Посты, письма, офферы</div><p>Собрать промпт под площадку, аудиторию и тон.</p></div>'
      '<div class="card"><div class="ct">Картинки</div><div class="ch">Промпт для фото/арта</div><p>Описать сцену, стиль, свет, ограничения.</p></div>'
      '<div class="card"><div class="ct">Код</div><div class="ch">Задача разработчику-ИИ</div><p>Чётко сформулировать, что собрать и как проверить.</p></div>'
      '<div class="card"><div class="ct">Видео</div><div class="ch">Промпт сцены</div><p>Кадр, камера, свет, движение для видео-нейросети.</p></div></div>'
    + '<p>Один мета-промпт заменяет коллекцию из сотни чужих промптов. Ты не ищешь готовое, ты собираешь своё под задачу.</p>'))

# 11 honest
P.append(page("Шаг 09 · Честность", 11,
    head("Шаг 09", "Честно: мусор на входе", "Мета-промпт усиливает то, что ты в него кладёшь. Не больше.")
    + '<div class="warn"><div class="h">Так не сработает</div><ul>'
      '<li>Сырая задача без цели — промпт будет красивый, но пустой.</li>'
      '<li>Слепо доверять фактам — нейросеть может ошибиться, проверяй.</li>'
      '<li>Просить «сделай вирусно» без смысла — вирусность не берётся из воздуха.</li></ul></div>'
    + '<div class="warn"><div class="h" style="color:#8fd08a">Так сработает</div><ul>'
      '<li class="ok">Отвечай на вопросы честно и конкретно.</li>'
      '<li class="ok">Проверяй факты и цифры в результате сам.</li>'
      '<li class="ok">Дорабатывай промпт под себя, это не догма.</li></ul></div>'
    + '<p>Сильный промпт это половина дела. Вторая половина это твоя голова: смысл, правда, вкус.</p>'))

# 12 errors
P.append(page("Шаг 10 · Ошибки", 12,
    head("Шаг 10", "Ошибки и фиксы", "Четыре грабли новичка.")
    + '<div class="fix">'
      '<div class="r"><b>Нейросеть сразу пишет ответ, а не промпт.</b> Фикс: напомни «сначала задай вопросы, потом собери промпт».</div>'
      '<div class="r"><b>Промпт слишком общий.</b> Фикс: дай больше деталей в ответах, добавь примеры и ограничения.</div>'
      '<div class="r"><b>Промпт огромный и мутный.</b> Фикс: попроси «сделай короче и чётче, оставь только важное».</div>'
      '<div class="r"><b>Один раз собрал и забыл.</b> Фикс: сохрани удачные промпты, собери свою мини-библиотеку.</div></div>'
    + '<p class="note">Как собрать промпт-систему под нишу, а не разовые промпты, разбираем в части 2 (в Telegram).</p>'))

# 13 action
P.append(page("Шаг 11 · Действие", 13,
    head("Шаг 11", "Сделай сейчас", "За пять минут получи первый сильный промпт.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Скопируй мета-промпт</b> со страницы 07.</div></div>'
      '<div class="step"><div class="sx"><b>Опиши свою реальную задачу</b> в [СКОБКАХ] и отправь.</div></div>'
      '<div class="step"><div class="sx"><b>Ответь на вопросы</b> по пяти рамкам со страницы 08.</div></div>'
      '<div class="step"><div class="sx"><b>Запусти готовый промпт</b> и сравни с обычным запросом.</div></div></div>'
    + '<div class="callout check"><div class="h">Проверь себя</div>'
      '<div class="row">Нейросеть задала вопросы, а не сразу ответила.</div>'
      '<div class="row">В промпте видны цель, аудитория, формат и тон.</div>'
      '<div class="row">Результат заметно лучше обычного запроса.</div>'
      '<div class="row">Ты сохранил удачный промпт в свою библиотеку.</div></div>'))

# 14 course
P.append(page("Дальше", 14,
    head("Дальше", "Промпт — это один навык. А есть система", "Ты научил нейросеть собирать промпты. На курсе собираешь всю работу с текстом в систему.")
    + '<p>Один мета-промпт экономит часы. Но сила не в одном приёме, а в системе: как ставить задачи, как строить промпт-цепочки, как собрать промпт-машину под свою нишу. Это «Земля Слов» в курсе «Нейросети и ChatGPT для каждого».</p>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Цепочки</div><p>Как собрать сложную задачу из простых шагов.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Промпт-система</div><p>Не сто промптов, а одна машина под твою нишу.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Проверка</div><p>Как заставить ИИ проверять и чинить свой же результат.</p></div></div>'
    + '<p>Мета-промпт это вход. Дальше ты перестаёшь искать чужие промпты и собираешь свои под любую задачу.</p>'))

# 15 team
P.append(page("Команда", 15,
    head("Путь дальше", "Путь в команду AlovLab", "Начало получаться и хочется применять это для брендов — есть куда расти.")
    + '<div class="team"><div class="h">Собираешь промпты уверенно?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты: строят промпт-системы и ассистентов под задачи брендов, набивают портфолио на живых кейсах и растут рядом с командой.</p>'
      '<div class="dirs"><span>Промпт-системы</span><span>AI-ассистенты</span><span>Автоматизация</span><span>Контент-конвейеры</span></div>'
      '<p style="margin-top:8px">Это работа и практика, а не обещание трудоустройства. Но дорога открыта: покажи, что доводишь результат.</p></div>'
    + '<p>Бизнесу, которому нужна промпт-система или ассистент под ключ — это AlovLab Studio. Отправляешь бриф, сборку берём на себя.</p>'))

# 16 contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Автоконтент</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Не ищи чужие промпты. Собери свой.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Мета-промпт и разбор — бесплатно в Telegram. Нужна промпт-система под бренд — отправь бриф в студию.</p>
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
