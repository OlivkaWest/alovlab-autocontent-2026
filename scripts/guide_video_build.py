# -*- coding: utf-8 -*-
"""AlovLab · методичка «Ролик без камеры на нейросети» (премиум-PDF, фикс-A4).
По GLOBAL-METHODOLOGY-RULE: реальный workflow (сцены короткие, ролик — на монтаже), промпты с [переменными]
+ что вставить/получить + уровни, плохо/хорошо, честность (лицо-референс, текст отдельным слоем, права),
ACTION+CHECK, мост в курс (Земля Видео) + «Путь в команду AlovLab». Без выдуманных цифр.
Запуск: python3 scripts/guide_video_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "video-no-camera"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-video.html"

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
.scenes2{display:grid;gap:9px;margin:10px 0}
.sc{border:1px solid var(--line);border-radius:11px;padding:11px 14px;background:#fff}
.sc b{font-weight:800;font-size:10pt;color:var(--ink)}
.sc code{display:block;font-family:ui-monospace,Menlo,monospace;font-size:8pt;line-height:1.4;color:#8a5a2a;background:#faf3ea;border-radius:7px;padding:7px 9px;margin-top:5px;white-space:pre-wrap}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · ролик без камеры на нейросети</span>'
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
  <div style="position:absolute;right:6%;top:22%;width:52%;height:40%;border-radius:18px;border:1px solid rgba(255,140,60,.28);background:linear-gradient(160deg,rgba(255,140,60,.10),rgba(255,140,60,0))"></div>
  <div style="position:absolute;right:26%;top:38%;width:64px;height:64px;border-radius:50%;border:2px solid var(--o2);display:grid;place-items:center;color:var(--o2);font-size:22pt">▶</div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.04;letter-spacing:-.02em;color:#fff;max-width:15ch">Ролик без камеры на нейросети</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:40ch">Ты описываешь сцены словами, нейросеть их снимает, ты собираешь ролик на монтаже. Без камеры, актёров и площадки.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">9:16 · вертикаль</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Промпты сцен внутри</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Метод, не магия</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("01","Что ты соберёшь","03"),("02","Миф про съёмку","04"),("03","Что нужно","05"),
 ("04","Метод: 4 этапа","06"),("05","Этап 1 · Промпт сцены","07"),
 ("06","5 готовых сцен","08"),("07","Этап 2 · Генерация","09"),
 ("08","Этап 3 · Монтаж","10"),("09","Промпт сцены: плохо/хорошо","11"),
 ("10","Честно и по закону","12"),("11","Ошибки и фиксы","13"),
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
    '<p class="lead">Пятнадцать шагов от пустого экрана до готового ролика. Иди по порядку.</p>'
    f'<div style="margin-top:6px">{rows}</div>'))

# 03 Result
P.append(page("Шаг 01 · Результат", 3,
    head("Шаг 01", "Что ты соберёшь", "Короткий кинематографичный ролик 9:16 на 15–30 секунд: несколько сгенерённых сцен, музыка и подписи. Годится под рекламу, Reels, заставку бренда.")
    + '<div class="flow"><div class="node"><b>Опиши</b><span>сцену</span></div><div class="arr">→</div>'
      '<div class="node"><b>Сгенерь</b><span>3–6 сек</span></div><div class="arr">→</div>'
      '<div class="node"><b>Собери</b><span>монтаж</span></div><div class="arr">→</div>'
      '<div class="node"><b>Опубликуй</b><span>9:16</span></div></div>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Что это</div><div class="ch">Ролик из сцен</div><p>4–6 коротких сцен, склеенных в один клип под музыку.</p></div>'
      '<div class="card"><div class="ct">Для чего</div><div class="ch">Реклама · Reels</div><p>Промо товара, заставка, b-roll, короткая история бренда.</p></div>'
      '<div class="card"><div class="ct">Съёмка</div><div class="ch">Ноль</div><p>Ни камеры, ни актёров, ни площадки. Ты режиссёр, не оператор.</p></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>Вертикальный ролик, который выглядит как дорогая реклама: смена красивых кадров, ровный тёплый грейд, музыка и короткие подписи. Собран за вечер одним человеком.</p></div>'))

# 04 Myth
P.append(page("Шаг 02 · Миф", 4,
    head("Шаг 02", "Видео — не про камеру", "Барьер в голове: кажется, что нужна съёмка. На деле нужна режиссура кадра.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Миф</div><b>«Нужна камера, актёры, локация, свет и монтажёр. Дорого и долго.»</b> Поэтому ролик откладывают.</div>'
      '<div class="box good"><div class="lbl">Как есть</div><b>Нужно описать кадр.</b> Что в кадре, свет, движение камеры, настроение. Сцену снимает нейросеть.</div></div>'
    + '<p>Нейросети для видео (Higgsfield, Veo, Seedance и другие) генерят короткую сцену по текстовому описанию. Ты не снимаешь и не держишь камеру. Ты ставишь кадр словами и собираешь сцены в ролик.</p>'
    + '<div class="term"><b>Честно.</b> <span>Это не «полный фильм одной кнопкой». Нейросеть даёт короткие сцены по 3–6 секунд. Красивый ролик рождается на монтаже, когда ты склеиваешь сцены в темп музыки. Именно это ты и освоишь.</span></div>'
    + '<div class="mns"><div class="m move"><div class="h">Твоя работа</div><p>Придумать сцены, описать кадр, выбрать удачные дубли, собрать на монтаже.</p></div>'
      '<div class="m stay"><div class="h">Работа нейросети</div><p>Снять сцену по описанию: свет, движение, фактуру, атмосферу.</p></div></div>'))

# 05 Need
P.append(page("Шаг 03 · Подготовка", 5,
    head("Шаг 03", "Что нужно", "Минимум: браузер и нейросеть для видео. Для монтажа — простой редактор.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Видео-нейросеть</div><div class="ch">Генерит сцены</div><p>Higgsfield, Veo, Seedance и др. Дают короткий кадр по тексту.</p></div>'
      '<div class="card"><div class="ct">Сценарий</div><div class="ch">ChatGPT / Claude</div><p>Помогает придумать сцены и написать промпты под кадр.</p></div>'
      '<div class="card"><div class="ct">Монтаж</div><div class="ch">Редактор</div><p>Любой: телефонный или на компьютере. Склейка, музыка, подписи.</p></div></div>'
    + '<h3>Собери заранее (10 минут)</h3>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Идея ролика в одну строку.</b> Что рекламируем или показываем. Пример: «атмосфера кофейни премиум».</div></div>'
      '<div class="step"><div class="sx"><b>4–6 сцен списком.</b> Establishing, крупный план, деталь, портрет, финал.</div></div>'
      '<div class="step"><div class="sx"><b>Единый стиль.</b> Один грейд (например тёплый закат), чтобы сцены смотрелись как один фильм.</div></div>'
      '<div class="step"><div class="sx"><b>Фото для лица</b> (если нужен человек) — своё, как reference, чтобы сохранить идентичность.</div></div></div>'
    + '<p class="note">Часть видео-нейросетей платные по кредитам. Начни с бесплатных лимитов или одной сцены, чтобы поймать метод.</p>'))

# 06 Method
P.append(page("Шаг 04 · Метод", 6,
    head("Шаг 04", "Метод: 4 этапа", "Весь путь укладывается в вечер. Дальше каждый этап отдельно.")
    + '<div class="scene"><div class="sn">1</div><div><div class="sh">Опиши сцену</div><div class="sd">Промпт кадра: <b>что в кадре, свет, движение камеры, настроение, длительность.</b></div></div><span class="stag">Промпт</span></div>'
    + '<div class="scene"><div class="sn">2</div><div><div class="sh">Сгенерь</div><div class="sd">Нейросеть снимает сцену 3–6 сек, 9:16. Делаешь 2–3 дубля, берёшь лучший.</div></div><span class="stag">Видео</span></div>'
    + '<div class="scene"><div class="sn">3</div><div><div class="sh">Собери</div><div class="sd">Склейка сцен в темп музыки, короткие подписи, единый грейд.</div></div><span class="stag">Монтаж</span></div>'
    + '<div class="scene"><div class="sn">4</div><div><div class="sh">Опубликуй</div><div class="sd">Экспорт 9:16 в Reels, VK Клипы, Shorts.</div></div><span class="stag">9:16</span></div>'
    + '<div class="callout check"><div class="h">Правило вечера</div>'
      '<div class="row">Сначала все сцены, потом монтаж. Не вылизывай одну сцену, пока нет всех.</div>'
      '<div class="row">Один грейд и один темп на весь ролик — тогда он смотрится как реклама, а не набор клипов.</div></div>'))

# 07 Scene prompt
scene = ("Cinematic vertical 9:16 shot. Сцена: [ЧТО В КАДРЕ]. Камера: [медленный наезд / облёт / статика]. "
         "Свет: [тёплый закат / студийный / неон]. Движение: [что двигается в кадре]. Настроение: дорогое, "
         "реалистичное, кинематографичное, без искажений. Длительность 5 секунд. No text, no watermark, no distorted faces.")
P.append(page("Этап 1 · Промпт", 7,
    head("Этап 1", "Промпт, который снимает сцену", "Скопируй, поменяй слова в [СКОБКАХ] и отправь видео-нейросети.")
    + prompt("Промпт сцены · СКОПИРОВАТЬ", scene)
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Объект в кадре, движение камеры, свет, что двигается. Чем конкретнее, тем дороже кадр.</p></div>'
      '<div class="c out"><b>Что получить</b><p>Короткую кинематографичную сцену 5 секунд, 9:16, готовую к монтажу.</p></div></div>'
    + '<div class="lvls"><div class="row"><span class="k">Быстрый</span><p>Отправь как есть, поменяв скобки. Хватит для первой сцены.</p></div>'
      '<div class="row"><span class="k">Про</span><p>Добавь оптику и грейд: «85mm, малая глубина резкости», «тёплый киношный грейд, лёгкое зерно».</p></div>'
      '<div class="row"><span class="k">Advanced</span><p>Задай непрерывность: «та же цветовая гамма и свет, что в прошлой сцене» — чтобы кадры склеились как один фильм.</p></div></div>'))

# 08 5 scenes
P.append(page("Этап 1 · Сцены", 8,
    head("5 сцен", "Готовые промпты сцен", "Собери из них ролик: establishing → деталь → герой → финал. Меняй объекты под свою тему.")
    + '<div class="scenes2">'
      '<div class="sc"><b>1 · Establishing</b><code>city street at golden hour, warm sunlight, long shadows, slow push-in, cinematic grade, 9:16, photoreal</code></div>'
      '<div class="sc"><b>2 · Деталь / продукт</b><code>extreme close-up of a premium product on a dark reflective surface, warm rim light, slow orbit, macro, 9:16</code></div>'
      '<div class="sc"><b>3 · Герой (лицо — reference)</b><code>confident person in dark outfit, warm side light, shallow depth of field, slow push-in, keep face natural, 9:16</code></div>'
      '<div class="sc"><b>4 · Атмосфера</b><code>cinematic frame emerging from darkness, warm particles, soft light bloom, elegant reveal, 9:16</code></div>'
      '<div class="sc"><b>5 · Финал в телефоне</b><code>phone on a dark desk, warm rim light, screen plays a vertical ad, slow push-in to screen, 9:16</code></div></div>'
    + '<p class="note">Ко всем добавляй: «No text, no watermark, no distorted faces». Русские подписи — на монтаже, не в генерации.</p>'))

# 09 Generation
P.append(page("Этап 2 · Генерация", 9,
    head("Этап 2", "Генерируй сцены правильно", "Настройки, которые экономят кредиты и держат единый стиль.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Формат 9:16, длительность 5 секунд, motion средний.</b> Короткие сцены режутся легче и стоят дешевле.</div></div>'
      '<div class="step"><div class="sx"><b>Единый грейд на все сцены.</b> Задай один свет и цвет (например тёплый закат) во всех промптах.</div></div>'
      '<div class="step"><div class="sx"><b>Лицо — через reference-image.</b> Иначе нейросеть подставит чужого человека. Загрузи своё фото как основу.</div></div>'
      '<div class="step"><div class="sx"><b>Не вшивай русский текст в генерацию.</b> Он поплывёт. Все подписи добавишь на монтаже отдельным слоем.</div></div>'
      '<div class="step"><div class="sx"><b>Делай 2–3 дубля сцены</b> и бери лучший. Это нормально, так работают все.</div></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div><p>Папка из 4–6 коротких сцен в едином стиле, 9:16, без вшитого текста и без кривых лиц.</p></div>'))

# 10 Editing
P.append(page("Этап 3 · Монтаж", 10,
    head("Этап 3", "Собери ролик на монтаже", "Здесь набор сцен превращается в рекламу.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Выложи сцены в темп музыки.</b> Склейки на бит, каждая сцена 1–2 секунды, чтобы держать динамику.</div></div>'
      '<div class="step"><div class="sx"><b>Один грейд поверх всего.</b> Лёгкая цветокоррекция, чтобы сцены стали одним фильмом.</div></div>'
      '<div class="step"><div class="sx"><b>Короткие подписи</b> крупным шрифтом, отдельным слоем. Одна мысль на кадр.</div></div>'
      '<div class="step"><div class="sx"><b>Хук в первые 2 секунды.</b> Самая сильная сцена или фраза в начало, иначе пролистают.</div></div>'
      '<div class="step"><div class="sx"><b>Экспорт 9:16.</b> Проверь на телефоне: читается, не дёргается, звук на месте.</div></div></div>'
    + '<p class="note">Музыку бери из библиотек без авторских претензий или лицензионную. Чужой трек — риск блокировки.</p>'))

# 11 good/bad
P.append(page("Шаг 05 · Как просить", 11,
    head("Шаг 05", "Промпт сцены: плохо и хорошо", "Кадр выходит ровно настолько, насколько ты его описал.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Плохо</div>«Сделай красивое видео города.»<br><br>Непонятно: какой план, свет, движение. Выходит общо и дёшево.</div>'
      '<div class="box good"><div class="lbl">Хорошо</div>«Вертикаль 9:16, улица города на закате, тёплый свет, длинные тени, медленный наезд камеры, киногрейд, 5 секунд.»</div></div>'
    + '<h3>Формула кадра</h3>'
    + '<div class="flow"><div class="node"><b>Что в кадре</b><span>объект</span></div><div class="arr">+</div>'
      '<div class="node"><b>Камера</b><span>движение</span></div><div class="arr">+</div>'
      '<div class="node"><b>Свет</b><span>грейд</span></div><div class="arr">+</div>'
      '<div class="node"><b>Настроение</b><span>+ длина</span></div></div>'
    + '<p>Чем точнее вводные, тем меньше дублей. Промпт со страницы 07 уже собран по этой формуле.</p>'))

# 12 honest
P.append(page("Шаг 06 · Честность", 12,
    head("Шаг 06", "Честно и по закону", "Красивый ролик не должен вводить в заблуждение и нарушать права.")
    + '<div class="warn"><div class="h">Так нельзя</div><ul>'
      '<li>Выдавать сгенерённый товар за реальное фото продукта, если он отличается.</li>'
      '<li>Ставить чужую музыку без прав.</li>'
      '<li>Делать лицо реального человека без его согласия.</li>'
      '<li>Обещать в рекламе то, чего у продукта нет.</li></ul></div>'
    + '<div class="warn"><div class="h" style="color:#8fd08a">Так правильно</div><ul>'
      '<li class="ok">Своё лицо — через reference, чужое — только с согласия.</li>'
      '<li class="ok">Музыка без авторских претензий или лицензионная.</li>'
      '<li class="ok">Если продукт условный, показывай это как имидж-ролик, не как фото товара.</li>'
      '<li class="ok">Текст и обещания — правдивые.</li></ul></div>'
    + '<p>AI-видео это сильный инструмент. Сила остаётся силой, только пока зритель тебе доверяет.</p>'))

# 13 errors
P.append(page("Шаг 07 · Ошибки", 13,
    head("Шаг 07", "Ошибки и фиксы", "Пять граблей первого ролика.")
    + '<div class="fix">'
      '<div class="r"><b>Сцены не клеятся, выглядят вразнобой.</b> Фикс: один грейд и один свет во всех промптах.</div>'
      '<div class="r"><b>Лицо чужое или плывёт.</b> Фикс: reference-image и «keep face natural, no distortion».</div>'
      '<div class="r"><b>Текст в кадре кривой.</b> Фикс: не вшивай текст в генерацию, добавляй на монтаже.</div>'
      '<div class="r"><b>Ролик затянут и скучный.</b> Фикс: сцены по 1–2 сек, склейки на бит, сильный кадр в начало.</div>'
      '<div class="r"><b>Сожгли кредиты на длинные сцены.</b> Фикс: генери 5 секунд и 2–3 дубля, не длиннее.</div></div>'
    + '<p class="note">Озвучку и голос за кадром разбираем в части 2 (в Telegram): как добавить голос и дубляж.</p>'))

# 14 action+check
P.append(page("Шаг 08 · Действие", 14,
    head("Шаг 08", "Сделай сейчас", "За один заход собери первый ролик из 4 сцен.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Придумай 4 сцены</b> под свою тему.</div></div>'
      '<div class="step"><div class="sx"><b>Сгенерь каждую</b> по промпту со страницы 07–08, единый грейд.</div></div>'
      '<div class="step"><div class="sx"><b>Собери на монтаже:</b> темп, музыка, короткие подписи.</div></div>'
      '<div class="step"><div class="sx"><b>Опубликуй 9:16</b> и посмотри с телефона.</div></div></div>'
    + '<div class="callout check"><div class="h">Проверь перед публикацией</div>'
      '<div class="row">Первые 2 секунды цепляют, хочется досмотреть.</div>'
      '<div class="row">Сцены в едином стиле и грейде.</div>'
      '<div class="row">Подписи читаются, одна мысль на кадр.</div>'
      '<div class="row">Музыка без авторских рисков.</div>'
      '<div class="row">Ничего не выдаёт за реальную съёмку, если это не так.</div></div>'))

# 15 course
P.append(page("Дальше", 15,
    head("Дальше", "Ролик — это один результат. А есть система", "Ты собрал клип за вечер. На курсе собираешь метод под любые видео.")
    + '<p>Один ролик — хорошо. Но сила не в одной генерации, а в системе: как ставить кадр, как держать стиль, как собирать конвейер из сцен, голоса, аватара и монтажа. Это «Земля Видео» в курсе «Нейросети и ChatGPT для каждого».</p>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Голос и озвучка</div><p>Как добавить закадровый голос и дубляж к ролику.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Аватар</div><p>Цифровой двойник, который говорит в кадре.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Конвейер</div><p>Сцена → монтаж → публикация как повторяемая система.</p></div></div>'
    + '<p>Ролик без камеры — это вход. Дальше ты перестаёшь заказывать съёмку и собираешь видео сам.</p>'))

# 16 team
P.append(page("Команда", 16,
    head("Путь дальше", "Путь в команду AlovLab", "Начало получаться и хочется делать это для брендов — есть куда расти.")
    + '<div class="team"><div class="h">Снимаешь ролики уверенно?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты: собирают AI-рекламу и промо под бренды, набивают портфолио на живых кейсах и растут в ремесле рядом с командой.</p>'
      '<div class="dirs"><span>AI-реклама</span><span>Промо-ролики</span><span>Аватары и дубляж</span><span>Контент-конвейеры</span></div>'
      '<p style="margin-top:8px">Это работа и практика, а не обещание трудоустройства. Но дорога открыта: покажи, что доводишь ролик до результата.</p></div>'
    + '<p>Бизнесу, которому нужна AI-реклама под ключ, а не «сам за вечер» — это AlovLab Studio. Отправляешь бриф, продакшн и конвейер берём на себя.</p>'))

# 17 contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Автоконтент</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Не арендуй съёмку. Сними словами.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Промпты сцен и эта методичка — бесплатно в Telegram. Нужна AI-реклама под бренд — отправь бриф в студию.</p>
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
