# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 9 «Факты, а не вода» — премиум-PDF (фикс-A4).
Как искать и проверять факты через Perplexity, что считать источником, бланк фактуры,
готовые промпты и разборы. ЧЕСТНОСТЬ в основе: показываем ФОРМУ факта (утверждение →
цифра → источник → год), а НЕ выдуманные данные. Ниша примеров — ИИ/контент.
База CSS — из v2. Запуск: python3 scripts/guide_facts_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "fakty-ne-voda"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-fakty-ne-voda.html"

EXTRA = r"""
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.prompt code{font-size:9.2pt}
.rec{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:9px 0;align-items:start}
.rec .n{width:22px;height:22px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}
.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.rec .t i{font-style:normal;color:var(--muted)}
.rec .t em{font-style:normal;color:var(--o);font-weight:700}
.form{background:#13100a;border:1px solid rgba(255,150,80,.28);border-left:3px solid var(--o);border-radius:12px;padding:14px 16px;margin:11px 0}
.form .r{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:11pt;color:#ffd9b8;font-weight:700}
.form .r span{background:rgba(255,255,255,.06);border:1px solid rgba(255,150,80,.3);border-radius:8px;padding:5px 11px}
.form .r i{color:var(--o2);font-style:normal;font-weight:800}
.form .cap{margin-top:9px;font-size:9.3pt;color:#b9ad9b;line-height:1.4}
.sig{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.sig .s{display:grid;grid-template-columns:15px 1fr;gap:12px;align-items:start;background:#fff;border:1px solid var(--line);border-radius:11px;padding:11px 14px}
.sig .s .d{width:13px;height:13px;border-radius:50%;margin-top:3px}
.sig .s.g .d{background:#3f9d5f}.sig .s.y .d{background:#d99a2b}.sig .s.r{background:#faf0ea;border-color:#eccdb9}.sig .s.r .d{background:#c9503a}
.sig .s b{font-weight:800;color:var(--ink);font-size:10.3pt}
.sig .s p{margin-top:2px;font-size:9.5pt;line-height:1.4;color:var(--body)}
.phr{display:flex;flex-wrap:wrap;gap:7px;margin:11px 0}
.phr span{font-size:9.6pt;color:#8a7d6c;background:#f3ece0;border:1px solid var(--line);border-radius:8px;padding:6px 11px}
.phr span::before{content:"✕ ";color:#cf7b53;font-weight:800}
table.blank td{height:24px}
table.blank td.e{color:var(--faint)}
.cards3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:9px;margin:11px 0}
.cards3 .c{background:#fff;border:1px solid var(--line);border-radius:11px;padding:11px 13px}
.cards3 .c b{display:block;font-weight:800;font-size:10pt;color:var(--ink);margin-bottom:4px}
.cards3 .c.f b{color:#3f9d5f}.cards3 .c.o b{color:#d99a2b}.cards3 .c.a b{color:#c9503a}
.cards3 .c p{font-size:9pt;line-height:1.4;color:var(--body)}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · факты, а не вода</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>Разбор:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def biz(txt, lbl="Бизнес"):
    return f'<div class="biz"><b>{lbl}</b>{txt}</div>'

def rec(n, title, body):
    return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{title}</b><p>{body}</p></div></div>'

P = []

# P1 · Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 9</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Факты, <span style="color:var(--o2)">а не вода.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Как за 15 минут собрать фактуру по теме через Perplexity: что считать источником, как проверить, и бланк, куда складывать. С готовыми промптами.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Где искать</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Как проверить</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Бланк</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Промпты</span>
    </div>
  </div>
</section>""")

# P2 · Что внутри
P.append(page("Что внутри", 2, """
  <span class="kick">Тетрадь под карусель «Факты, а не вода»</span>
  <h2>Под текстом должна быть фактура</h2>
  <p class="lead">Текст звучит пусто не потому, что ты плохо пишешь. Под ним нет опоры: цифр, источников, конкретики. Эта тетрадь — как собрать фактуру за 15 минут и не выдумать ни одной цифры.</p>
  <div class="flow">
    <div class="node"><b>Тема</b><span>узко</span></div><div class="arr">→</div>
    <div class="node"><b>Perplexity</b><span>факты + ссылки</span></div><div class="arr">→</div>
    <div class="node"><b>Проверка</b><span>источник</span></div><div class="arr">→</div>
    <div class="node"><b>Бланк</b><span>лист фактуры</span></div>
  </div>
  <div class="term"><b>Фактура</b> — <span>проверяемые опоры текста: цифры, даты, имена, ссылки. То, что держит слова.</span></div>
  <div class="term"><b>Вода</b> — <span>эпитеты без опоры: «полезно», «эффективно». Звучит, но проверить нечего.</span></div>
  <div class="callout result"><div class="h">Что на выходе</div><p>Лист фактуры на 7 проверенных фактов с источниками, три промпта для Perplexity и правило, которое держит тебя честным: нет источника — нет факта.</p></div>
"""))

# P3 · Диагноз
P.append(page("Диагноз", 3, """
  <span class="kick">Почему звучит пусто</span>
  <h2>Эпитеты вместо фактов</h2>
  <p class="lead">Пустой текст — это текст без опор. Вместо конкретики — общие слова, которые подходят чему угодно. Читатель это чувствует и не верит.</p>
  <div class="rec"><div class="n">1</div><div class="t"><b>Общие слова</b><p>«Полезно», «качественно», «эффективно» — ничего не сказано и не проверить.</p></div></div>
  <div class="rec"><div class="n">2</div><div class="t"><b>Цифры из головы</b><p>«Экономит кучу времени» — сколько? откуда? Выдуманная цифра хуже, чем никакой.</p></div></div>
  <div class="rec"><div class="n">3</div><div class="t"><b>Пересказ рекламы</b><p>Берёшь «факт» из чужого поста, а там — реклама без источника.</p></div></div>
  <div class="rec"><div class="n">4</div><div class="t"><b>Нет пруфа</b><p>Утверждение есть, ссылки нет. Читателю нечем поверить, тебе — нечем защититься.</p></div></div>
  <p class="note">Чинится не «писать красивее», а собрать фактуру до текста. Как — дальше.</p>
"""))

# P4 · Что такое факт
P.append(page("Что такое факт", 4,
  '<span class="kick">Форма факта</span>'
  '<h2>Утверждение, которое можно проверить</h2>'
  '<p class="lead">Факт всегда конкретен и имеет адрес. Если нельзя ткнуть в источник — это не факт, а мнение или реклама.</p>'
  '<div class="form"><div class="r"><span>утверждение</span><i>→</i><span>цифра / дата / имя</span><i>→</i><span>источник</span><i>→</i><span>год</span></div>'
  '<div class="cap">Форма, а не выдумка. Конкретику и ссылку подставляешь реальные — из Perplexity.</div></div>'
  '<div class="cards3">'
  '<div class="c f"><b>Факт</b><p>проверяемое утверждение с источником и датой.</p></div>'
  '<div class="c o"><b>Мнение</b><p>«я считаю», «кажется» — без пруфа. Не выдавай за факт.</p></div>'
  '<div class="c a"><b>Реклама</b><p>«лучший на рынке» — источник сам продавец. Не источник.</p></div>'
  '</div>'
  + biz("везде, где убеждаешь: посты, продающие тексты, коммерческие, лендинги, ответы клиентам.")
))

# P5 · Где искать
P.append(page("Где искать", 5,
  '<span class="kick">Инструмент дня · Perplexity</span>'
  '<h2>Ищи там, где видно источник</h2>'
  '<p class="lead">Perplexity ищет в интернете и сразу показывает, откуда взял — ссылки под ответом. Можно кликнуть и проверить. Обычный чат так не делает — поэтому для фактуры берём Perplexity.</p>'
  '<div class="rec"><div class="n">1</div><div class="t"><b>Официальные данные и документация</b><p>Сайт продукта, гос-статистика, первоисточник. Высшая проба.</p></div></div>'
  '<div class="rec"><div class="n">2</div><div class="t"><b>Исследования и отчёты</b><p>С методологией и датой. Смотри, кто и когда проводил.</p></div></div>'
  '<div class="rec"><div class="n">3</div><div class="t"><b>Качественные СМИ и эксперты</b><p>Если ссылаются на первоисточник — годится. Если друг на друга — нет.</p></div></div>'
  + '<p class="note">Важно: любой ИИ может ошибиться и «придумать» ссылку. Поэтому источник обязателен, и по нему нужно перейти и проверить глазами.</p>'
))

# P6 · Метод 5 шагов
P.append(page("Метод · 15 минут", 6, """
  <span class="kick">Пять шагов · по порядку</span>
  <h2>Фактура за 15 минут</h2>
  <div class="rec"><div class="n">1</div><div class="t"><b>Сузь тему</b><p>«ИИ для контента» — слишком широко. «Форматы, которые генерирует [инструмент]» — вот это гуглится и проверяется.</p></div></div>
  <div class="rec"><div class="n">2</div><div class="t"><b>Проси факты и цифры со ссылками</b><p>Прямо в запросе: «с источниками, ссылка + дата». Без этого получишь общие слова.</p></div></div>
  <div class="rec"><div class="n">3</div><div class="t"><b>Проверь источник</b><p>Перейди по ссылке. Кто автор, когда, это первоисточник или пересказ, не реклама ли.</p></div></div>
  <div class="rec"><div class="n">4</div><div class="t"><b>Отсей мусор</b><p>Устаревшее, «одна статья без данных», мнения без пруфа, реклама — в корзину.</p></div></div>
  <div class="rec"><div class="n">5</div><div class="t"><b>Вынеси в лист</b><p>Факт → цифра → источник → год. Что не влезло в эту форму — не факт.</p></div></div>
"""))

# P7 · Проверь источник
P.append(page("Проверь источник", 7,
  '<span class="kick">Светофор надёжности</span>'
  '<h2>Дойди до первоисточника</h2>'
  '<p class="lead">Один и тот же «факт» может быть золотым или мусорным — всё решает источник. Оцени по светофору:</p>'
  '<div class="sig">'
  '<div class="s g"><div class="d"></div><div><b>Зелёный — бери</b><p>Первоисточник: официальный сайт, документация, исследование. Автор и дата видны, данные свежие.</p></div></div>'
  '<div class="s y"><div class="d"></div><div><b>Жёлтый — докопай</b><p>Пересказ или вторичка. Найди, на что ссылаются, и дойди до оригинала. Пока не дошёл — не используешь.</p></div></div>'
  '<div class="s r"><div class="d"></div><div><b>Красный — выброси</b><p>Реклама, аноним, нет даты, «одна статья». Даже если звучит красиво — это не источник.</p></div></div>'
  '</div>'
  + biz("правило одно для всех ниш: цитируешь цифру — рядом должна быть ссылка, по которой её видно.")
))

# P8 · Отсев мусора
P.append(page("Отсев мусора", 8, """
  <span class="kick">Что НЕ считать источником</span>
  <h2>Красные флаги</h2>
  <p class="lead">Эти вещи маскируются под факты, но опереться на них нельзя. Увидел — не бери.</p>
  <div class="phr">
    <span>реклама и промо</span><span>мнение без данных</span><span>одна случайная статья</span>
    <span>устаревшие цифры</span><span>«эксперты говорят» без имён</span><span>скриншот без ссылки</span>
    <span>«британские учёные»</span><span>пересказ пересказа</span><span>цифра без источника</span>
  </div>
  <div class="biz"><b>Приём</b>Спроси себя: «куда я ткну, если спросят пруф?» Некуда — значит, это не факт, а вода. Убирай или ищи источник.</div>
  <p class="note">И честно: если проверить нельзя — не выдумывай и не «додумывай» цифру. Лучше без числа, чем с фальшивым.</p>
"""))

# P9 · Бланк фактуры
P.append(page("Бланк фактуры", 9, """
  <span class="kick">Шаблон · заполняешь под свою тему</span>
  <h2>Лист фактуры</h2>
  <p class="lead">Складывай сюда всё, что прошло проверку. Одна строка — один факт. Пустая клетка «источник» = факт не готов.</p>
  <table class="blank">
    <tr><th>#</th><th>Факт</th><th>Цифра / дата</th><th>Источник (ссылка)</th><th>Год</th></tr>
    <tr><td>1</td><td class="e">…</td><td class="e">…</td><td class="e">…</td><td class="e">…</td></tr>
    <tr><td>2</td><td class="e">…</td><td class="e">…</td><td class="e">…</td><td class="e">…</td></tr>
    <tr><td>3</td><td class="e">…</td><td class="e">…</td><td class="e">…</td><td class="e">…</td></tr>
    <tr><td>4</td><td class="e">…</td><td class="e">…</td><td class="e">…</td><td class="e">…</td></tr>
    <tr><td>5</td><td class="e">…</td><td class="e">…</td><td class="e">…</td><td class="e">…</td></tr>
    <tr><td>6</td><td class="e">…</td><td class="e">…</td><td class="e">…</td><td class="e">…</td></tr>
    <tr><td>7</td><td class="e">…</td><td class="e">…</td><td class="e">…</td><td class="e">…</td></tr>
  </table>
  <p class="note">Заполнил 7 строк с источниками — у тебя фактура на целую серию постов, а не на один текст.</p>
"""))

# P10 · Промпт сбора
P.append(page("Промпт · сбор фактов", 10,
  '<span class="kick">Этап · собрать фактуру</span>'
  '<h2>Perplexity — 7 фактов с источниками</h2>'
  '<p class="lead">Главный промпт тетради. Узкая тема + требование источника + жёсткий формат = лист фактуры, а не пересказ рекламы.</p>'
  + prompt("Готовый промпт · Perplexity",
    "Собери 7 проверенных фактов по теме: [ТВОЯ ТЕМА].\n"
    "Требования к каждому факту:\n"
    "— конкретика: цифра, дата или имя, а не общие слова;\n"
    "— источник: ссылка + название + год;\n"
    "— приоритет: официальные данные, документация, исследования.\n"
    "Исключи рекламу, мнения без данных и устаревшее.\n"
    "Формат: факт → цифра → источник → год.",
    "получишь список со ссылками. Не копируй вслепую — перейди и проверь каждый по светофору (стр. 7).")
  + biz("эксперт — факты по нише; магазин — характеристики и стандарты; услуга — нормы и сроки.")
))

# P11 · Промпт проверки
P.append(page("Промпт · проверка", 11,
  '<span class="kick">Этап · перепроверить</span>'
  '<h2>Fact-check одного факта</h2>'
  '<p class="lead">Когда факт важный или сомнительный — прогони отдельно. Заставь модель найти первоисточник и честно сказать, если не подтверждается.</p>'
  + prompt("Готовый промпт · Perplexity",
    "Перепроверь факт: «[ФАКТ]».\n"
    "Найди первоисточник (не пересказ). Ответь по пунктам:\n"
    "— подтверждается или нет;\n"
    "— точная цифра / формулировка;\n"
    "— источник: ссылка, автор, год;\n"
    "— это не реклама?\n"
    "Если подтвердить нельзя — так и напиши: «не подтверждается».",
    "«не подтверждается» — это нормальный ответ. Такой факт в текст не идёт. Пустое место честнее выдумки.")
))

# P12 · Промпт текст из фактов
P.append(page("Промпт · факты в текст", 12,
  '<span class="kick">Этап · превратить в текст</span>'
  '<h2>Текст только из своих фактов</h2>'
  '<p class="lead">Финал: собери текст, разрешив модели использовать ТОЛЬКО собранную фактуру. Так ИИ не «дорисует» цифру от себя.</p>'
  + prompt("Готовый промпт · Claude / Perplexity",
    "Напиши абзац по теме [ТЕМА], используя ТОЛЬКО эти факты:\n"
    "[ВСТАВЬ ЛИСТ ФАКТУРЫ С ИСТОЧНИКАМИ].\n"
    "Не добавляй цифр и утверждений, которых нет в списке.\n"
    "Живой голос, короткие фразы, конкретика вместо штампов.\n"
    "Где есть цифра — оставь ссылку на источник.",
    "это мост к тетради «Текст, который читают»: фактура + живая подача = текст, которому верят.")
))

# P13 · Пример прогона
P.append(page("Пример прогона", 13,
  '<span class="kick">Форма · подставь реальные ссылки</span>'
  '<h2>Как выглядит готовый лист</h2>'
  '<p class="lead">Пример формы для темы «нейросети для контента». Цифры и ссылки здесь — заглушки: их подставляешь реальные из Perplexity. Мы не выдумываем данные — показываем каркас.</p>'
  '<div class="form"><div class="r" style="display:block;line-height:2.1">'
  '1. <span>[инструмент] генерирует [формат]</span> — <i>[офиц. документация], [год]</i><br>'
  '2. <span>[возможность] появилась [дата]</span> — <i>[анонс/релиз], [год]</i><br>'
  '3. <span>[стандарт/лимит] = [число]</span> — <i>[страница помощи], [год]</i>'
  '</div><div class="cap">Каждая строка проверяема: есть конкретика и адрес источника. Нет адреса — строка не готова.</div></div>'
  '<div class="callout check"><div class="h">Чек-лист перед текстом</div>'
  '<div class="row">У каждого факта есть ссылка, по которой он виден</div>'
  '<div class="row">Цифры реальные, из источника, а не «на глаз»</div>'
  '<div class="row">Источник — первичный, свежий, не реклама</div>'
  '<div class="row">Что не подтвердилось — выброшено, а не «додумано»</div>'
  '</div>'
))

# P14 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Сначала факты —<br>потом <span style="color:var(--o2)">текст.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:46ch;margin:0 auto 20px">Метод сбора, светофор источников, бланк фактуры и три промпта для Perplexity — вся тетрадь дня. Собери 7 фактов и пиши то, чему верят.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Факты, а не вода · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
