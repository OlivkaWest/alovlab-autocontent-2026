# -*- coding: utf-8 -*-
"""AlovLab · методичка «Сайт за вечер на нейросети — без кода» (премиум-PDF, фикс-A4).
По GLOBAL-METHODOLOGY-RULE: самостоятельный продукт, реальный workflow (не магия одним промптом),
рабочие промпты с переменными [...] + что вставить/что получить + уровни, пример плохо/хорошо,
ACTION BLOCK + QUALITY CHECK, честный контент, мост в курс + «Путь в команду AlovLab». Без выдуманных цен.
Запуск: python3 scripts/guide_site_build.py
Рендер PDF: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "site-vecher"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-site-vecher.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.midwrap{width:100%}
.lvl{display:inline-block;font-weight:800;font-size:7.6pt;letter-spacing:.05em;text-transform:uppercase;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:20px;padding:3px 11px;margin:2px 6px 6px 0}
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
.big{font-weight:800;font-size:15pt;line-height:1.2;color:var(--ink);margin:6px 0}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · сайт за вечер на нейросети</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None):
    r = f'<div class="ru">{ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{r}</div>')

P = []

# ---------- 01 · Обложка (dark, без фото — CSS) ----------
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:absolute;right:-6%;top:20%;width:62%;height:46%;border-radius:18px;border:1px solid rgba(255,140,60,.28);
       background:linear-gradient(160deg,rgba(255,140,60,.10),rgba(255,140,60,0));box-shadow:0 30px 90px rgba(0,0,0,.5)"></div>
  <div style="position:absolute;right:2%;top:24%;width:52%;color:#ffb98a;font-weight:800;font-size:10pt;letter-spacing:.02em">
     &lt;/&gt; index.html<div style="height:8px"></div>
     <div style="font-weight:700;font-size:26pt;color:#fff;line-height:1.06">Твой<br>оффер<br><span style="color:var(--o2)">за вечер</span></div>
     <div style="margin-top:12px;display:inline-block;background:linear-gradient(150deg,var(--o2),var(--o));color:#160e07;font-weight:800;font-size:10pt;padding:8px 16px;border-radius:9px">Оставить заявку</div>
  </div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.04;letter-spacing:-.02em;color:#fff;max-width:15ch">Сайт за вечер на нейросети. Без кода.</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:40ch">Ты описываешь словами, нейросеть пишет код и собирает рабочую страницу. Ты правишь фразами и публикуешь. Ни одной строки кода.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Один вечер</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Без программиста</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Промпт-бриф внутри</span>
    </div>
  </div>
</section>""")

# ---------- 02 · Содержание ----------
toc = [
 ("01","Что ты соберёшь","03"),("02","Миф про код","04"),("03","Что нужно (бесплатно)","05"),
 ("04","Как это работает: 4 этапа","06"),("05","Этап 1 · Промпт-бриф сайта","07"),
 ("06","Этап 2 · Открой страницу","08"),("07","Этап 3 · Правь словами","09"),
 ("08","Как ставить задачу: плохо/хорошо","10"),("09","Контент честно","11"),
 ("10","Этап 4 · Опубликуй бесплатно","12"),("11","Частые ошибки и фиксы","13"),
 ("12","Сделай сейчас + проверка","14"),("13","Дальше — на курсе","15"),
 ("14","Путь в команду AlovLab","16"),("15","Контакты","17"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:12px;padding:8px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:10pt;width:26px">{a}</span>'
               f'<span style="font-weight:600;font-size:11.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:10pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Маршрут гайда</h1>'
    '<p class="lead">Пятнадцать шагов от пустого экрана до опубликованного сайта. Иди по порядку, каждый шаг опирается на предыдущий.</p>'
    f'<div style="margin-top:6px">{rows}</div>'))

# ---------- 03 · Что ты соберёшь ----------
P.append(page("Шаг 01 · Результат", 3,
    head("Шаг 01", "Что ты соберёшь за вечер",
         "Одностраничный сайт-лендинг, который реально открывается в браузере и работает на телефоне. Один файл, одна ссылка.")
    + '<div class="flow">'
      '<div class="node"><b>Опиши</b><span>словами</span></div><div class="arr">→</div>'
      '<div class="node"><b>Получи</b><span>страницу</span></div><div class="arr">→</div>'
      '<div class="node"><b>Правь</b><span>фразами</span></div><div class="arr">→</div>'
      '<div class="node"><b>Опубликуй</b><span>ссылка</span></div></div>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Что это</div><div class="ch">Лендинг 1 страница</div><p>Экран-оффер, выгоды, как работает, отзывы, вопросы, форма заявки.</p></div>'
      '<div class="card"><div class="ct">Для чего</div><div class="ch">Продукт · услуга · я</div><p>Курс, мастер, кофейня, портфолио, инфопродукт, локальный бизнес.</p></div>'
      '<div class="card"><div class="ct">Сколько кода</div><div class="ch">Ноль строк</div><p>Ты пишешь фразы, код пишет нейросеть.</p></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>Рабочая страница по твоей ссылке: заголовок с оффером, кнопка, блоки с пользой и форма заявки. Открывается на компьютере и на телефоне, читается, кнопки нажимаются.</p></div>'))

# ---------- 04 · Миф про код ----------
P.append(page("Шаг 02 · Миф", 4,
    head("Шаг 02", "Сайт — это не про код",
         "Главный барьер в голове, а не в технологии. Разберём, что реально нужно.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Миф</div><b>«Нужно учить программирование, нанимать студию, ждать месяц и платить вперёд.»</b> Поэтому сайт откладывают на год.</div>'
      '<div class="box good"><div class="lbl">Как есть</div><b>Нужно уметь объяснить задачу.</b> Что продаёшь, кому, какие блоки, какой стиль. Остальное собирает нейросеть.</div></div>'
    + '<p>Нейросеть вроде Claude умеет писать код и сразу собирать готовую HTML-страницу. Ты не открываешь редактор кода и не разбираешься в тегах. Ты пишешь на русском, что хочешь получить, и получаешь файл, который открывается в браузере.</p>'
    + '<div class="term"><b>Важно честно.</b> <span>Это не «магия одним словом». Первый черновик редко идеальный. Метод в том, чтобы получить каркас за минуту и довести его короткими правками. Именно это ты и освоишь ниже.</span></div>'
    + '<div class="mns"><div class="m move"><div class="h">Твоя работа</div><p>Поставить задачу и править словами: оффер, выгоды, порядок блоков, стиль, мобилка.</p></div>'
      '<div class="m stay"><div class="h">Работа нейросети</div><p>Написать HTML и CSS, собрать секции, сверстать адаптив, поправить по твоим фразам.</p></div></div>'))

# ---------- 05 · Что нужно ----------
P.append(page("Шаг 03 · Подготовка", 5,
    head("Шаг 03", "Что нужно. И всё бесплатно",
         "Ничего не покупаешь и не устанавливаешь ради старта. Хватит браузера.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Инструмент</div><div class="ch">Нейросеть с кодом</div><p>Claude (claude.ai) или Claude Code. Умеет вернуть готовый файл страницы.</p></div>'
      '<div class="card"><div class="ct">Где смотреть</div><div class="ch">Браузер</div><p>Любой. Открываешь в нём готовый HTML-файл и сразу видишь сайт.</p></div>'
      '<div class="card"><div class="ct">Где выложить</div><div class="ch">Бесплатный хостинг</div><p>Сервисы, куда можно перетащить один файл и получить ссылку. Шаги в конце гайда.</p></div></div>'
    + '<h3>Собери это заранее (15 минут)</h3>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Оффер в одну строку.</b> Что ты даёшь и кому. Пример: «Собираю сайты за вечер для мастеров и локального бизнеса».</div></div>'
      '<div class="step"><div class="sx"><b>3 выгоды.</b> Почему к тебе, а не мимо. Коротко и конкретно.</div></div>'
      '<div class="step"><div class="sx"><b>Контакт для заявки.</b> Телеграм, телефон или форма. Куда придёт клиент.</div></div>'
      '<div class="step"><div class="sx"><b>1–2 своих фото</b> (если есть). Свои или со стоков с лицензией. Чужие из интернета не берём.</div></div></div>'
    + '<p class="note">Если пока нечего продавать — собери сайт-визитку о себе или портфолио. Метод тот же.</p>'))

# ---------- 06 · Как это работает ----------
P.append(page("Шаг 04 · Метод", 6,
    head("Шаг 04", "Как это работает: 4 этапа",
         "Весь путь укладывается в один вечер. Ниже каждый этап отдельно, с промптами.")
    + '<div class="scene"><div class="sn">1</div><div><div class="sh">Опиши задачу</div>'
      '<div class="sd">Один промпт-бриф: кто ты, что продаёшь, какие блоки, какой стиль. <b>Каркас со следующей страницы.</b></div></div><span class="stag">Промпт</span></div>'
    + '<div class="scene"><div class="sn">2</div><div><div class="sh">Получи и открой</div>'
      '<div class="sd">Нейросеть возвращает готовый файл. Сохраняешь, открываешь в браузере, смотришь.</div></div><span class="stag">Браузер</span></div>'
    + '<div class="scene"><div class="sn">3</div><div><div class="sh">Правь словами</div>'
      '<div class="sd">Короткие фразы: «кнопку крупнее», «выгоды проще», «на телефоне удобно». Повторяешь, пока не нравится.</div></div><span class="stag">Правки</span></div>'
    + '<div class="scene"><div class="sn">4</div><div><div class="sh">Опубликуй</div>'
      '<div class="sd">Заливаешь один файл на бесплатный хостинг, получаешь ссылку. Сайт живой.</div></div><span class="stag">Ссылка</span></div>'
    + '<div class="callout check"><div class="h">Правило вечера</div>'
      '<div class="row">Сначала каркас целиком, потом правки. Не вылизывай первый экран, пока нет всей страницы.</div>'
      '<div class="row">Одна правка — одна фраза. Так видно, что именно изменилось.</div></div>'))

# ---------- 07 · Этап 1: промпт-бриф ----------
brief = ("Собери одностраничный лендинг на чистом HTML и CSS в одном файле, без внешних библиотек. "
         "Проект: [ЧТО ПРОДАЁШЬ]. Аудитория: [КТО КЛИЕНТ]. Главный оффер: [ОФФЕР В ОДНУ СТРОКУ]. "
         "Блоки по порядку: 1) экран-заголовок с оффером и кнопкой «[ТЕКСТ КНОПКИ]»; 2) три выгоды; "
         "3) как это работает в 3 шага; 4) отзывы (оставь заглушки, я вставлю реальные); 5) частые вопросы; "
         "6) форма заявки (имя, контакт, кнопка); 7) футер с контактами [ТВОЙ КОНТАКТ]. "
         "Стиль: [ТЁМНЫЙ или СВЕТЛЫЙ], акцентный цвет [ЦВЕТ], крупная типографика, много воздуха, адаптив под телефон. "
         "Тексты живые и короткие, без канцелярита. Верни один готовый файл index.html, который открывается в браузере.")
P.append(page("Этап 1 · Промпт", 7,
    head("Этап 1", "Промпт, который собирает сайт",
         "Скопируй, поменяй только слова в [СКОБКАХ] и отправь нейросети. Это каркас всей страницы.")
    + prompt("Промпт-бриф · СКОПИРОВАТЬ", brief)
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Свой продукт, аудиторию, оффер в одну строку, текст кнопки, контакт, стиль и цвет.</p></div>'
      '<div class="c out"><b>Что получить</b><p>Готовый файл index.html: экран-оффер, выгоды, шаги, отзывы, вопросы, форма и футер. Открывается сразу.</p></div></div>'
    + '<div class="lvls"><div class="row"><span class="k">Быстрый</span><p>Отправь бриф как есть, поменяв скобки. Хватит для первой рабочей версии.</p></div>'
      '<div class="row"><span class="k">Про</span><p>Добавь: «сделай hero на весь экран», «кнопка ведёт к форме», «добавь плавные появления блоков».</p></div>'
      '<div class="row"><span class="k">Advanced</span><p>Попроси: «сделай два варианта первого экрана на выбор» и «добавь мета-теги и заголовок вкладки для [НАЗВАНИЕ]».</p></div></div>'))

# ---------- 08 · Этап 2: открой ----------
P.append(page("Этап 2 · Открой", 8,
    head("Этап 2", "Получи файл и открой страницу",
         "Нейросеть вернёт код страницы. Твоя задача — увидеть её в браузере.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Скопируй код</b> или скачай файл, который дала нейросеть.</div></div>'
      '<div class="step"><div class="sx"><b>Сохрани его как <code style="font-family:ui-monospace,monospace">index.html</code></b> на рабочий стол. Если копировал текст — вставь в «Блокнот» и сохрани с расширением .html.</div></div>'
      '<div class="step"><div class="sx"><b>Открой двойным кликом.</b> Файл откроется в браузере — это уже твой сайт, только пока на твоём компьютере.</div></div>'
      '<div class="step"><div class="sx"><b>Проверь на телефоне логику:</b> в браузере на компьютере сузь окно — блоки должны перестраиваться в одну колонку.</div></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>Страница открывается, видно оффер, кнопку и все блоки. Что-то кривое или не нравится — это нормально, чиним на следующем шаге словами.</p></div>'
    + '<p class="note">Не понравился весь стиль сразу — не переписывай вручную. Вернись к нейросети и опиши, что не так.</p>'))

# ---------- 09 · Этап 3: правь словами ----------
P.append(page("Этап 3 · Правки", 9,
    head("Этап 3", "Сайт правится фразами",
         "Не трогай код. Пиши нейросети короткие правки и получай обновлённый файл.")
    + prompt("Правка 1 · первый экран", "Сделай первый экран мощнее: оффер в одну строку крупным шрифтом, под ним короткое пояснение, кнопка большая и заметная. Убери лишние слова.")
    + prompt("Правка 2 · выгоды", "Перепиши три выгоды под [АУДИТОРИЮ]. Проще и конкретнее, каждая выгода одним коротким предложением про результат для клиента.")
    + prompt("Правка 3 · мобилка", "Проверь, что на телефоне всё читается: крупный текст, кнопки удобные для пальца, блоки в одну колонку, ничего не вылезает за край.")
    + '<div class="lvls"><div class="row"><span class="k">Ещё правки</span><p>«замени цвет акцента на [ЦВЕТ]», «добавь блок отзывов», «сделай форму короче: только имя и контакт», «добавь секцию про меня».</p></div></div>'))

# ---------- 10 · плохо/хорошо ----------
P.append(page("Шаг 05 · Как просить", 10,
    head("Шаг 05", "Как ставить задачу: плохо и хорошо",
         "Сайт получается ровно настолько, насколько ясно ты объяснил. Сравни.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Плохо</div>«Сделай красивый сайт.»<br><br>Нейросеть угадывает за тебя: непонятно кто клиент, что за оффер, какие блоки. Выходит общо и мимо.</div>'
      '<div class="box good"><div class="lbl">Хорошо</div>«Лендинг для мастера маникюра в [ГОРОД]. Оффер: запись за 30 секунд. Блоки: оффер+кнопка, 3 выгоды, работы, отзывы, форма. Стиль светлый, акцент персиковый, мобилка удобная.»</div></div>'
    + '<h3>Формула хорошей задачи</h3>'
    + '<div class="flow"><div class="node"><b>Кто клиент</b><span>аудитория</span></div><div class="arr">+</div>'
      '<div class="node"><b>Оффер</b><span>одна строка</span></div><div class="arr">+</div>'
      '<div class="node"><b>Блоки</b><span>по порядку</span></div><div class="arr">+</div>'
      '<div class="node"><b>Стиль</b><span>цвет · тон</span></div></div>'
    + '<p>Чем конкретнее вводные, тем меньше правок потом. Первый бриф со страницы 07 уже собран по этой формуле — просто заполни скобки честно.</p>'))

# ---------- 11 · контент честно ----------
P.append(page("Шаг 06 · Честность", 11,
    head("Шаг 06", "Контент кладёшь честно",
         "Нейросеть собирает каркас. Правду в него кладёшь ты. Это и репутация, и закон.")
    + '<div class="warn"><div class="h">Так нельзя</div><ul>'
      '<li>Придумывать отзывы и «кейсы клиентов», которых не было.</li>'
      '<li>Ставить чужие фото из интернета без прав.</li>'
      '<li>Писать выдуманные цифры: «1000 клиентов», «−70%», если их нет.</li>'
      '<li>Обещать то, чего не делаешь.</li></ul></div>'
    + '<div class="warn"><div class="h" style="color:#8fd08a">Так правильно</div><ul>'
      '<li class="ok">Отзывы — только реальные, с согласия людей.</li>'
      '<li class="ok">Фото — свои или со стоков с лицензией.</li>'
      '<li class="ok">Тексты — про то, что ты реально даёшь.</li>'
      '<li class="ok">Заглушки в отзывах оставь пустыми, пока нет настоящих.</li></ul></div>'
    + '<p>Нейросети можно прямо написать: «в блоке отзывов оставь пустые карточки-заглушки с подписью, я вставлю реальные позже». Так на сайте не появится вранья.</p>'))

# ---------- 12 · публикация ----------
P.append(page("Этап 4 · Публикация", 12,
    head("Этап 4", "Опубликуй бесплатно",
         "Пока сайт живёт на твоём компьютере — его никто не видит. Дадим ему ссылку.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Возьми бесплатный хостинг для статических сайтов.</b> Спроси нейросеть: «назови 2–3 бесплатных сервиса, куда можно загрузить один HTML-файл и получить ссылку, и дай короткую инструкцию для новичка».</div></div>'
      '<div class="step"><div class="sx"><b>Загрузи файл</b> <code style="font-family:ui-monospace,monospace">index.html</code>. Обычно это перетащить файл в окно или нажать Upload.</div></div>'
      '<div class="step"><div class="sx"><b>Получи ссылку</b> вида your-site.site. Открой её с телефона — проверь, что всё работает.</div></div>'
      '<div class="step"><div class="sx"><b>Разошли ссылку.</b> В шапку профиля, в сообщения клиентам, в комментарий под постом.</div></div></div>'
    + '<div class="callout result"><div class="h">Готово</div><p>У тебя есть живой сайт по ссылке, собранный за вечер. Дальше его можно улучшать теми же фразами в любой момент.</p></div>'))

# ---------- 13 · ошибки ----------
P.append(page("Шаг 07 · Ошибки", 13,
    head("Шаг 07", "Частые ошибки и фиксы", "Пять граблей, на которые наступают в первый вечер.")
    + '<div class="fix">'
      '<div class="r"><b>Просишь всё сразу и переделываешь бесконечно.</b> Фикс: сначала каркас целиком, потом по одной правке.</div>'
      '<div class="r"><b>Правишь код руками и всё ломается.</b> Фикс: не трогай код, описывай правку словами нейросети.</div>'
      '<div class="r"><b>Текст «вода» и канцелярит.</b> Фикс: попроси «перепиши живым языком, короткими фразами, без штампов».</div>'
      '<div class="r"><b>На телефоне разъезжается.</b> Фикс: «сделай адаптив: одна колонка, крупные кнопки, отступы по краям».</div>'
      '<div class="r"><b>Форма никуда не ведёт.</b> Фикс: «сделай, чтобы кнопка открывала мой [ТЕЛЕГРАМ/ПОЧТУ]» или оставь контакт текстом.</div></div>'
    + '<p class="note">Форма с реальным приёмом заявок в базу или в бота — это уже вторая часть. Её разбираем на курсе и в продолжении.</p>'))

# ---------- 14 · action + check ----------
P.append(page("Шаг 08 · Действие", 14,
    head("Шаг 08", "Сделай сейчас", "Не откладывай. За один заход собери первую версию.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Заполни промпт-бриф</b> со страницы 07 под свой продукт.</div></div>'
      '<div class="step"><div class="sx"><b>Получи страницу</b> и открой её в браузере.</div></div>'
      '<div class="step"><div class="sx"><b>Сделай 3 правки словами:</b> первый экран, выгоды, мобилка.</div></div>'
      '<div class="step"><div class="sx"><b>Опубликуй</b> и открой ссылку с телефона.</div></div></div>'
    + '<div class="callout check"><div class="h">Проверь себя перед публикацией</div>'
      '<div class="row">Оффер понятен за 3 секунды: что это и для кого.</div>'
      '<div class="row">Есть заметная кнопка и понятно, что будет после клика.</div>'
      '<div class="row">На телефоне читается, кнопки удобные, ничего не вылезает.</div>'
      '<div class="row">Ни одного выдуманного отзыва или числа.</div>'
      '<div class="row">Есть рабочий контакт для заявки.</div></div>'))

# ---------- 15 · мост в курс ----------
P.append(page("Дальше", 15,
    head("Дальше", "Сайт — это один результат. А есть система",
         "Ты собрал страницу за вечер. На курсе собираешь не одну страницу, а метод под любые задачи.")
    + '<p>Один сайт — хорошо. Но сила не в одной генерации, а в системе: как ставить задачи нейросети, как доводить результат, как собирать под себя конвейер из текста, кода, картинок и видео. Это и есть «Нейросети и ChatGPT для каждого».</p>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Форма → заявка</div><p>Как довести сайт до реальных заявок и приёма сообщений.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Сайт + бот</div><p>Как подключить простого бота, который отвечает клиентам.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Конвейер</div><p>Текст, код, визуал, видео и голос как одна система под тебя.</p></div></div>'
    + '<p>Курс устроен как шесть «Земель»: Слова, Изображения, Видео, Звук, Аватары, Знания. Сайт за вечер — это только вход. Дальше ты перестаёшь искать «сделайте мне» и делаешь сам.</p>'))

# ---------- 16 · путь в команду ----------
P.append(page("Команда", 16,
    head("Путь дальше", "Путь в команду AlovLab",
         "Если у тебя начало получаться и хочется делать это для других — есть куда расти.")
    + '<div class="team"><div class="h">Собираешь сайты уверенно?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты: собирают лендинги и автоматизацию под задачи брендов, набивают портфолио на живых кейсах и растут в ремесле рядом с командой.</p>'
      '<div class="dirs"><span>Лендинги под бизнес</span><span>Автоматизация</span><span>AI-ассистенты</span><span>Контент-конвейеры</span></div>'
      '<p style="margin-top:8px">Это работа и практика, а не обещание трудоустройства. Но дорога открыта: покажи, что умеешь довести результат.</p></div>'
    + '<p>Бизнесу, которому нужен сайт или автоматизация под ключ, а не «сам за вечер» — это уже AlovLab Studio. Отправляешь бриф, а сборку и конвейер берём на себя.</p>'))

# ---------- 17 · контакты ----------
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Автоконтент</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Не ищи «сделайте мне сайт». Собери сам за вечер.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Промпт-бриф и эта методичка — забирай в комментариях под постом. Нужен сайт под бизнес под ключ — отправь бриф в студию.</p>
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
