# -*- coding: utf-8 -*-
"""AlovLab · методичка к карусели «9 промптов, после которых фото не палит ИИ» — премиум-PDF (фикс-A4).
Подробно: по 2 промпта на каждый из 9 стилей = 18 промптов + «где применить» + «как заработать».
Железное правило идентичности лица в каждом промпте. По GLOBAL-METHODOLOGY-RULE. Без выдуманных цен.
Запуск: python3 scripts/guide_photo_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "photo-9prompts"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-photo.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.rec{display:grid;grid-template-columns:26px 1fr;gap:12px;margin:7px 0;align-items:start}
.rec .n{width:26px;height:26px;border-radius:8px;background:#13100a;color:var(--o2);font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.prompt code{font-size:8.2pt;line-height:1.5}
.lvl{display:inline-block;font-weight:800;font-size:7.6pt;letter-spacing:.05em;text-transform:uppercase;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:20px;padding:3px 11px;margin:2px 0 5px}
.stylehead{display:flex;align-items:baseline;gap:10px;margin-bottom:2px}
.stylehead .num{font-weight:800;font-size:15pt;color:var(--o)}
.apply{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0 2px}
.apply .c{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.apply .c.earn{background:#fff7ef;border-color:#eccdb9}
.apply .c b{font-weight:800;font-size:8.2pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.apply .c.earn b{color:var(--o)}
.apply .c p{font-size:9.1pt;line-height:1.38;color:var(--ink);margin-top:3px}
.warn{background:#13100a;border-radius:14px;padding:15px 18px;margin:9px 0;color:#f4efe6}
.warn .h{font-weight:800;font-size:10pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o2);margin-bottom:7px}
.warn ul{margin:0;padding-left:0;list-style:none}
.warn li{position:relative;padding:4px 0 4px 20px;font-size:9.4pt;line-height:1.4;color:#eae4da}
.warn li:before{content:"✕";position:absolute;left:0;color:var(--o2);font-weight:800}
.warn li.ok:before{content:"✔";}
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:15px 18px;margin:9px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12pt;color:#fff;margin-bottom:6px}.team p{font-size:9.6pt;line-height:1.5;color:#cdbfa8}
.team .dirs{display:flex;flex-wrap:wrap;gap:6px;margin:9px 0 3px}
.team .dirs span{font-size:8.4pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:4px 10px}
.stp{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:8px 0;align-items:start;width:100%}
.stp .kk{width:22px;height:22px;border-radius:7px;background:var(--o);color:#160e07;font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center;margin-top:1px}
.stp p{font-size:9.8pt;line-height:1.44;color:var(--ink)}
table.pt{width:100%;border-collapse:collapse;margin:8px 0;font-size:9pt}
table.pt th{background:#13100a;color:#f0e6d8;font-weight:800;font-size:7.6pt;letter-spacing:.04em;text-transform:uppercase;padding:8px 10px;text-align:left}
table.pt td{border:1px solid var(--line);padding:7px 10px;line-height:1.32;color:var(--ink);vertical-align:top}
table.pt tr:nth-child(even) td{background:#faf6ef}
"""
CSS = V2CSS + EXTRA
LOCK = "Сохрани лицо, форму головы, глаза, нос, губы, тон кожи, возраст, причёску, бороду и характерные черты без изменений. Не омолаживай, не меняй форму лица, без пластиковой кожи."

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · фото не палит ИИ</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')
def head(kick,h2,lead=None):
    l=f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def prompt(tag,code):
    return f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span><span class="copy">скопировать</span></div><code>{code}</code></div>'

def style_page(num, sn, title, sub, p1tag, p1, p2tag, p2, apply_txt, earn_txt):
    inner = (f'<div class="stylehead"><span class="num">{sn}</span><span class="kick" style="margin:0">{title}</span></div>'
             + f'<h2 style="margin-top:2px">{sub}</h2>'
             + prompt(p1tag, p1) + prompt(p2tag, p2)
             + f'<div class="apply"><div class="c"><b>Где применить</b><p>{apply_txt}</p></div>'
               f'<div class="c earn"><b>Как заработать</b><p>{earn_txt}</p></div></div>')
    return page(f"Стиль {sn}", num, inner, mid=True)

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">Методичка · фото + ChatGPT</div>
    <h1 style="font-weight:800;font-size:30pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:18ch">18 промптов, после которых <span style="color:var(--o2)">фото не палит ИИ.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:47ch">9 стилей съёмки, по 2 промпта на каждый. С сохранением твоего лица. Плюс где это применить и как на этом реально зарабатывать.</p>
  </div>
</section>""")

# 02 Что ты сможешь
P.append(page("Что ты сможешь",2,
  head("Результат","К концу — своя мини-фотостудия в чате",
    "Из обычного фото с телефона делаешь дорогой кадр под любую задачу. Лицо остаётся твоим.")
  + '<div class="rec"><div class="n">1</div><div class="t"><b>18 рабочих промптов</b><p>9 стилей × 2 варианта: DSLR, кино, журнал, тревел, деловой, золотой час и другие.</p></div></div>'
  + '<div class="rec"><div class="n">2</div><div class="t"><b>Сохранение внешности</b><p>в каждом промпте зашито «не менять лицо» — без пластика и подмены.</p></div></div>'
  + '<div class="rec"><div class="n">3</div><div class="t"><b>Деньги</b><p>на каждой странице — где применить и как на этом заработать. В конце — сводка услуг.</p></div></div>'
))

# 03 Железное правило (identity lock)
P.append(page("Главное правило",3,
  head("Критично","Лицо должно остаться твоим",
    "Это разница между «вау, реальный снимок» и «фу, нейросеть слепила чужого». В каждый промпт вставляй блок сохранения внешности.")
  + '<div class="warn"><div class="h">Запрещаем ИИ</div><ul>'
    '<li>менять форму лица, головы и пропорции</li>'
    '<li>заменять тебя похожим человеком</li>'
    '<li>омолаживать и «улучшать» черты</li>'
    '<li>пластиковую кожу и переретушь</li>'
    '<li>случайно менять причёску, бороду, возраст</li>'
    '</ul></div>'
  + '<div class="win" style="background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:10px;padding:11px 14px;margin:9px 0"><b>Вставляй в любой промпт:</b><p style="font-size:9.3pt;line-height:1.45;color:var(--body);margin-top:3px">«'+LOCK+'»</p></div>'
))

# 04 Как работает
P.append(page("Как работает",4,
  head("Процесс","4 шага, дальше только меняешь скобки")
  + '<div class="stp"><div class="kk">1</div><p><b>Загрузи фото</b> в ChatGPT (лучше чёткое, с нормальным светом).</p></div>'
  + '<div class="stp"><div class="kk">2</div><p><b>Выбери стиль</b> из методички и скопируй промпт.</p></div>'
  + '<div class="stp"><div class="kk">3</div><p><b>Поменяй слова в [скобках]</b> под себя: локация, одежда, сцена.</p></div>'
  + '<div class="stp"><div class="kk">4</div><p><b>Не вышло с первого раза</b> — уточни деталь («больше света слева», «камера ниже») и повтори.</p></div>'
  + '<p class="note">Качество зависит от исходника и пары уточнений. Это workflow, а не «одна кнопка».</p>'
, mid=True))

# 05–13 стили
S = LOCK
P.append(style_page(5,"1","DSLR-ПОРТРЕТ","Как от фотографа, без фотографа",
  "Быстрый","Преврати моё фото в профессиональный DSLR-портрет. "+S+" Помести меня в [ЛОКАЦИЯ]. Реалистичный свет, естественная текстура кожи, малая глубина резкости, мягкое отделение от фона. Итог как снимок с профессиональной камеры, не генерация ИИ.",
  "Про","Сделай студийный DSLR-портрет, объектив 85mm f/1.4, свет как из софтбокса слева и лёгкий контровой сзади. "+S+" Фон [ФОН: тёмный/светлый], лёгкое боке, детальные глаза, естественные поры кожи, кинематографичный, но правдоподобный контраст.",
  "Аватарки, фото на сайт и визитку, обложки соцсетей, первое фото в профиле.",
  "Портреты на заказ, оформление профилей экспертам, хедшоты пакетом."))

P.append(style_page(6,"2","КИНО-КАДР","Стоп-кадр из дорогого фильма",
  "Быстрый","Преврати моё фото в кинематографичный кадр. Помести меня в [СЦЕНА]. "+S+" Драматичный, но реалистичный свет, естественные тени, малая глубина резкости, дорогая кино-композиция, правдоподобная цветокоррекция. Фактуры натуральные.",
  "Про","Кадр в стиле [РЕЖИССЁР/ФИЛЬМ: напр. неонуар], тёплые тени и холодные блики, дым/атмосфера в воздухе, анаморфные блики, зерно плёнки. "+S+" Композиция как в кино, взгляд в сторону, история в кадре.",
  "Контент для блога и Reels-обложек, афиши, атмосферные посты, тизеры.",
  "Креативы и обложки для блогеров и музыкантов, оформление каналов."))

P.append(style_page(7,"3","ЛАКШЕРИ LIFESTYLE","Дорогой Instagram-снимок",
  "Быстрый","Сделай премиальный lifestyle-снимок для сильного личного бренда. Помести меня в [ЛОКАЦИЯ], одень в [ОДЕЖДА]. "+S+" Сложный естественный свет, живая поза, дорогая композиция, малая глубина резкости, натуральная кожа. Дорого и по-журнальному, без пластиковой ретуши.",
  "Про","Lifestyle в [ЛОКАЦИЯ: пентхаус/яхта/лобби отеля], золотой люкс-свет, расслабленная уверенная поза, дорогие детали (часы, интерьер) в фокусе намёком. "+S+" Ощущение съёмки для личного бренда на миллион.",
  "Личный бренд эксперта, продажи через профиль, контент для запусков.",
  "Упаковка профилей экспертам и предпринимателям, контент-пакеты под запуск."))

P.append(style_page(8,"4","ТРЕВЕЛ БЕЗ ПОЕЗДКИ","Как будто снял фотограф на месте",
  "Быстрый","Создай профессиональный travel-снимок в [МЕСТО]. "+S+" Реалистично впиши меня в локацию: свет, тени, погода, перспектива, отражения, одежда и окружение совпадают. Живая travel-композиция, естественные цвета, глубина пространства.",
  "Про","Тревел-кадр в [МЕСТО] в [ВРЕМЯ СУТОК], я взаимодействую со сценой (иду/смотрю вдаль), реальная геометрия света под это место и время, детали локации на фоне. "+S+" Будто фотограф правда снял меня там.",
  "Тревел-блог без бюджета на поездки, географию контента, сторис.",
  "Контент для тревел-блогеров, промо турагентств, серии под аренду жилья."))

P.append(style_page(9,"5","ОБЛОЖКА ЖУРНАЛА","Editorial fashion-портрет",
  "Быстрый","Преврати фото в премиальный editorial fashion-портрет. Подбери [ОДЕЖДА/СТИЛЬ], уверенную журнальную позу, студийный свет, натуральную кожу, проработанные тени, дорогую композицию. "+S+" Выразительная, но реалистичная цветокоррекция. Как съёмка для крупного журнала.",
  "Про","Обложка журнала [НИША: fashion/бизнес/спорт], жёсткий рисующий свет, чистый цикорама-фон [ЦВЕТ], поза с характером, место сверху под логотип журнала. "+S+" Резкие детали, глянец без пластика.",
  "Фэшн/бьюти-контент, сильные обложки, персональный бренд.",
  "Превью для фотографов и моделей, обложки для медиа и артистов."))

P.append(style_page(10,"6","РЕСТАВРАЦИЯ СТАРОГО ФОТО","Спаси семейный архив",
  "Быстрый","Отреставрируй это старое фото, сохранив человека и реальные черты. Удали повреждения, шум, потерю резкости и дефекты. Восстанови естественный тон кожи, детали лица, одежду, фон и свет. "+S+" Как будто портрет сняли сегодня на современную камеру.",
  "Про","Реставрируй и мягко раскрась чёрно-белое фото в реалистичные натуральные цвета, сохрани эпоху и подлинность. Убери царапины и заломы, верни резкость глаз и волос. "+S+" Без осовременивания одежды и лиц, без выдуманных деталей.",
  "Семейные архивы, память о близких, подарочные наборы.",
  "Услуга «восстановление старых фото» — реальный спрос, продаётся за фото или пакетом; печать в подарок."))

P.append(style_page(11,"7","СМЕНА ЛОКАЦИИ","Тот же ты, другое место",
  "Быстрый","Оставь меня полностью узнаваемым, но замени окружение на [ЛОКАЦИЯ]. "+S+" Согласуй свет, тени, отражения, перспективу, атмосферу и взаимодействие одежды с новым пространством. Как настоящее фото, снятое именно там.",
  "Про","Перенеси меня из текущего фона в [ЛОКАЦИЯ], сохранив мою позу и одежду. Пересчитай направление и температуру света под новую сцену, добавь реалистичные контактные тени и рефлексы окружения. "+S+" Никаких «вырезано и вклеено».",
  "Предметно-имиджевые кадры, единый фон под ленту, ребрендинг профиля.",
  "Рекламные креативы для брендов, унификация фото команды под сайт."))

P.append(style_page(12,"8","ДЕЛОВОЙ ПОРТРЕТ","LinkedIn, сайт, личный бренд",
  "Быстрый","Преврати фото в профессиональный деловой портрет для сайта, LinkedIn или личного бренда. "+S+" Чистый профессиональный свет, уверенная живая поза, натуральная кожа, точные детали лица, аккуратное отделение от фона. Без чрезмерной ретуши, как настоящая бизнес-съёмка.",
  "Про","Корпоративный хедшот на [ФОН: серый/белый/офис в боке], деловой [ОДЕЖДА], доброжелательное уверенное выражение, свет с мягким заполнением, резкость по глазам. "+S+" Единый стиль под серию портретов команды.",
  "Резюме, сайт, LinkedIn, спикерские карточки, пресс-кит.",
  "Корпоративные хедшоты пакетом, съёмка команд для сайтов, апдейт профилей."))

P.append(style_page(13,"9","ЗОЛОТОЙ ЧАС","Тёплый закатный кадр",
  "Быстрый","Преврати фото в съёмку в золотой час. Помести меня в [ЛОКАЦИЯ]. "+S+" Низкий тёплый солнечный свет, мягкие золотые блики, реалистичные длинные тени, тёплые оттенки. Свет соответствует позиции солнца и геометрии сцены. Не фильтр, а настоящий закатный кадр.",
  "Про","Золотой час в [ЛОКАЦИЯ], контровой солнечный свет за спиной, лёгкая дымка и блик в объектив, тёплый рим-лайт по контуру, глаза остаются проработанными. "+S+" Естественный, дорогой, эмоциональный кадр.",
  "Lifestyle-контент, тёплые личные посты, обложки историй.",
  "Контент-пакеты под личный бренд, съёмочные наборы для блогеров."))

# 14 Как зарабатывать (сводка)
P.append(page("Деньги",14,
  head("Монетизация","Как из промптов сделать услугу")
  + '<table class="pt"><tr><th>Услуга</th><th>Кому продавать</th></tr>'
    '<tr><td>Упаковка профиля (аватар + 5–7 кадров)</td><td>эксперты, предприниматели, коучи</td></tr>'
    '<tr><td>Деловые портреты команды</td><td>компании, агентства, юрфирмы</td></tr>'
    '<tr><td>Восстановление старых фото</td><td>частные лица, подарки</td></tr>'
    '<tr><td>Рекламные креативы (смена локации/сцены)</td><td>малый бизнес, бренды</td></tr>'
    '<tr><td>Контент-пакет под запуск</td><td>блогеры, инфобизнес</td></tr>'
    '</table>'
  + '<p class="note">Цену смотри по своему рынку и качеству доработки. Честно: результат зависит от исходника и пары уточнений, не обещай «идеально с первого раза». Показывай реальные до/после — это продаёт лучше слов.</p>'
))

# 15 Курс + путь в команду
P.append(page("Дальше",15,
  head("Продолжение","Здесь промпты. На курсе — система")
  + '<div class="callout result"><div class="h">Курс «Нейросети и ChatGPT для каждого»</div><p>Учим собирать не один кадр, а поток: фото, видео, тексты и продажи на нейросетях. От промпта до услуги, за которую платят.</p></div>'
  + '<div class="team"><div class="h">Навык может стать профессией</div>'
    '<p>Сильных студентов хотим видеть рядом. Выбираешь направление, набираешь навыки, собираешь портфолио на реальных задачах.</p>'
    '<div class="dirs"><span>AI Photo</span><span>AI Content</span><span>AI Marketing</span><span>SMM + AI</span><span>AI Video</span><span>Prompt Engineering</span></div>'
    '<p style="margin-top:8px">Лучших и наиболее активных студентов мы рассматриваем для участия в проектах AlovLab и совместной работы. Без обещаний «всем гарантированно» — по навыку и результату.</p></div>'
))

# 16 Финал
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:24pt;line-height:1.14;margin:18px 0 8px">Не ищи промпт<br><span style="color:var(--o2)">каждый раз.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Сохрани эту методичку. Фото → выбрал стиль → скопировал промпт → поменял слова в скобках → погнал.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Бриф → @alovlab</span>
  </div>
</section>""")

html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(P)}</body></html>"
OUT.write_text(html, encoding="utf-8")
print(f"HTML: {OUT} {len(html.encode('utf-8'))//1024} KB | pages: {len(P)}")
