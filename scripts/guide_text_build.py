# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 11 «Текст, который читают» — премиум-PDF (фикс-A4).
Живой текст против канцелярии: приёмы, структура поста и продающего, запрещённые фразы,
готовые промпты для Claude, разборы до/после. Ниша примеров — ИИ/контент. Без выдуманных цифр.
База CSS — из v2. Запуск: python3 scripts/guide_text_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "text-chitayut"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-text-chitayut.html"

EXTRA = r"""
.kick2{display:block;margin-top:14px;font-weight:800;font-size:8.5pt;letter-spacing:.14em;text-transform:uppercase;color:var(--o)}
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.prompt code{font-size:9.2pt}
.phr{display:flex;flex-wrap:wrap;gap:7px;margin:11px 0}
.phr span{font-size:9.6pt;color:#8a7d6c;background:#f3ece0;border:1px solid var(--line);border-radius:8px;padding:6px 11px;text-decoration:line-through;text-decoration-color:#cf7b53}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:10px 0}
.pair .c{border-radius:12px;padding:12px 14px;font-size:9.8pt;line-height:1.5}
.pair .bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.pair .good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.pair .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:6px}
.pair .bad .l{color:#c56b43}.pair .good .l{color:var(--o)}
.rec{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:9px 0;align-items:start}
.rec .n{width:22px;height:22px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}
.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.rec .t i{font-style:normal;color:var(--muted)}
.rec .t em{font-style:normal;color:var(--o);font-weight:700}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · текст, который читают</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>Разбор:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def biz(txt, lbl="Бизнес"):
    return f'<div class="biz"><b>{lbl}</b>{txt}</div>'

def rec(n, title, body):
    return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{title}</b><p>{body}</p></div></div>'

def pair(bad, good, bl="Канцелярия", gl="Живой"):
    return (f'<div class="pair"><div class="c bad"><span class="l">✕ {bl}</span>{bad}</div>'
            f'<div class="c good"><span class="l">✓ {gl}</span>{good}</div></div>')

P = []

# P1 · Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 11</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Текст, который <span style="color:var(--o2)">читают.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Живой текст против канцелярии. Приёмы, структура поста и продающего, запрещённые фразы и готовые промпты для Claude — с разборами до/после.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Приёмы</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Структуры</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Промпты</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">До / после</span>
    </div>
  </div>
</section>""")

# P2 · Что внутри
P.append(page("Что внутри", 2, """
  <span class="kick">Тетрадь под карусель «Текст, который читают»</span>
  <h2>Тебя бросают на третьей строке</h2>
  <p class="lead">Не из-за темы. Текст звучит как канцелярия — гладко, длинно, ни о чём — и читатель уходит раньше, чем дошёл до сути. Эта тетрадь — как писать так, чтобы дочитывали и переходили к делу.</p>
  <div class="flow">
    <div class="node"><b>Хук</b><span>первая строка</span></div><div class="arr">→</div>
    <div class="node"><b>Мысль</b><span>одна, сильная</span></div><div class="arr">→</div>
    <div class="node"><b>Пример</b><span>из практики</span></div><div class="arr">→</div>
    <div class="node"><b>Шаг</b><span>что сделать</span></div>
  </div>
  <div class="term"><b>Канцелярия</b> — <span>гладкие общие фразы без смысла: «важно понимать», «в современном мире». Звучит солидно, а сказать нечего.</span></div>
  <div class="term"><b>Живой текст</b> — <span>сильное начало, короткие фразы, одна мысль, конкретика. Так говорят вслух — так и читают.</span></div>
  <div class="callout result"><div class="h">Что на выходе</div><p>Готовый пост и продающий текст без штампов, список запрещённых фраз и промпт-редактор для Claude, который делает твой текст живым за один проход.</p></div>
"""))

# P3 · Диагноз
P.append(page("Диагноз", 3, """
  <span class="kick">Почему не читают</span>
  <h2>Виноват не текст. Разгон.</h2>
  <p class="lead">Читатель решает за пару секунд. Если первые строки — это раскачка и штампы, он уходит, даже если дальше было сильно. Четыре вещи убивают текст:</p>
  <div class="rec"><div class="n">1</div><div class="t"><b>Разгон в начале</b><p>«В этом посте я хочу рассказать…» — читатель ждёт сути, а её всё нет.</p></div></div>
  <div class="rec"><div class="n">2</div><div class="t"><b>Штампы и клише</b><p>«Важно понимать», «в современном мире» — слова, которые подходят чему угодно и не значат ничего.</p></div></div>
  <div class="rec"><div class="n">3</div><div class="t"><b>Длинные предложения</b><p>Три мысли в одном предложении — читатель теряет нить и бросает.</p></div></div>
  <div class="rec"><div class="n">4</div><div class="t"><b>Много мыслей сразу</b><p>Один текст пытается сказать всё — не запоминается ничего.</p></div></div>
  <p class="note">Хорошая новость: это чинится не талантом, а приёмами. Их — на следующей странице.</p>
"""))

# P4 · 8 приёмов
P.append(page("8 приёмов живого текста", 4, """
  <span class="kick">Приёмы · применяй по чек-листу</span>
  <h2>Как оживить любой текст</h2>
  <div class="rec"><div class="n">1</div><div class="t"><b>Сильное начало</b><p>Первое слово уже работает. <i>«В этом посте про промпты…»</i> → <em>«Промпт решает всё. Вот три рабочих.»</em></p></div></div>
  <div class="rec"><div class="n">2</div><div class="t"><b>Короткие фразы</b><p>Одна мысль — одно предложение. Точка вместо запятой добавляет воздуха.</p></div></div>
  <div class="rec"><div class="n">3</div><div class="t"><b>Конкретика вместо общих слов</b><p><i>«повышает эффективность»</i> → <em>«черновик за один проход, ты только правишь»</em>.</p></div></div>
  <div class="rec"><div class="n">4</div><div class="t"><b>Глаголы вместо канцелярита</b><p><i>«осуществление настройки»</i> → <em>«настрой»</em>. Живая речь — это действия.</p></div></div>
  <div class="rec"><div class="n">5</div><div class="t"><b>Один смысл на текст</b><p>Одна идея. Всё, что не про неё, — в другой пост.</p></div></div>
  <div class="rec"><div class="n">6</div><div class="t"><b>Ритм</b><p>Чередуй длину фраз и абзацев. Монотонность усыпляет.</p></div></div>
  <div class="rec"><div class="n">7</div><div class="t"><b>Режь вводные</b><p><i>«на самом деле», «в принципе», «как бы»</i> — слова-паразиты. Убери — фраза станет твёрже.</p></div></div>
  <div class="rec"><div class="n">8</div><div class="t"><b>Читай вслух</b><p>Где споткнулся — там и переписал. Ухо честнее глаза.</p></div></div>
"""))

# P5 · Запрещённые фразы
P.append(page("Запрещённые фразы", 5, """
  <span class="kick">Стоп-лист</span>
  <h2>Вырезать без сожаления</h2>
  <p class="lead">Эти фразы — маркеры канцелярии. Увидел у себя — удали или замени конкретикой. Смысла в них нет, только разгон.</p>
  <div class="phr">
    <span>В современном мире</span><span>Важно понимать</span><span>Как известно</span><span>Стоит отметить</span>
    <span>Давайте разберёмся</span><span>Нейросети стремительно развиваются</span><span>Будущее уже здесь</span>
    <span>Откройте для себя</span><span>Уникальная возможность</span><span>Инновационное решение</span>
    <span>Выведите бизнес на новый уровень</span><span>Наша команда экспертов</span><span>Взаимовыгодное сотрудничество</span>
  </div>
  <div class="biz"><b>Замена</b>Вместо штампа — факт, пример или действие. «Инновационное решение» → что именно оно делает. «Наша команда экспертов» → кто и что сделал.</div>
  <p class="note">И два правила: не начинай с приветствия и «в этом посте», не заканчивай каждый текст вопросом.</p>
"""))

# P6 · Структура поста
P.append(page("Структура поста", 6, """
  <span class="kick">Пост · 800–1500 знаков</span>
  <h2>Шесть блоков, которые дочитывают</h2>
  <div class="scene"><div class="sn">1</div><div><div class="sh">Хук</div><div class="sd">Первая строка цепляет: ошибка, конфликт, конкретный результат.</div></div><span class="stag">1 строка</span></div>
  <div class="scene"><div class="sn">2</div><div><div class="sh">Ситуация</div><div class="sd">Коротко — о чём речь и почему это про читателя.</div></div><span class="stag">контекст</span></div>
  <div class="scene"><div class="sn">3</div><div><div class="sh">Одна сильная мысль</div><div class="sd">Ядро поста. Одна идея, сформулированная просто.</div></div><span class="stag">ядро</span></div>
  <div class="scene"><div class="sn">4</div><div><div class="sh">Пример из практики</div><div class="sd">Живая деталь — что реально было. Доказательство вместо обещаний.</div></div><span class="stag">факт</span></div>
  <div class="scene"><div class="sn">5</div><div><div class="sh">Как применить сегодня</div><div class="sd">Конкретный шаг, который читатель сделает прямо сейчас.</div></div><span class="stag">действие</span></div>
  <div class="scene"><div class="sn">6</div><div><div class="sh">Естественный призыв</div><div class="sd">Мягкий шаг в Telegram за конкретным — без давления.</div></div><span class="stag">CTA</span></div>
"""))

# P7 · Структура продающего
P.append(page("Продающий текст", 7, """
  <span class="kick">Продающий · не дави</span>
  <h2>Начни с задачи клиента, не с себя</h2>
  <p class="lead">Продающий текст — не про то, какие вы молодцы. Он про задачу человека и простой следующий шаг. Пять блоков:</p>
  <div class="scene"><div class="sn">1</div><div><div class="sh">Контекст</div><div class="sd">Ситуация клиента его словами. Он узнаёт себя.</div></div><span class="stag">кто и где</span></div>
  <div class="scene"><div class="sn">2</div><div><div class="sh">Проблема</div><div class="sd">Что мешает — конкретно, без нагнетания.</div></div><span class="stag">боль</span></div>
  <div class="scene"><div class="sn">3</div><div><div class="sh">Гипотеза</div><div class="sd">Как может быть иначе — идея решения.</div></div><span class="stag">поворот</span></div>
  <div class="scene"><div class="sn">4</div><div><div class="sh">Решение</div><div class="sd">Что предлагаешь и почему это закрывает проблему.</div></div><span class="stag">оффер</span></div>
  <div class="scene"><div class="sn">5</div><div><div class="sh">Простой следующий шаг</div><div class="sd">Одно понятное действие. Не «купите», а «напишите/забирайте».</div></div><span class="stag">шаг</span></div>
  <div class="biz"><b>Правило</b>Не начинай с рассказа о себе. Первая мысль — про клиента и его задачу.</div>
"""))

# P8 · Хуки
P.append(page("8 типов хуков", 8, """
  <span class="kick">Первая строка · чередуй типы</span>
  <h2>Восемь способов зацепить</h2>
  <table>
    <tr><th>Тип</th><th>Пример первой строки</th></tr>
    <tr><td><b>Ошибка</b></td><td>«Ты пишешь пост не с той строки.»</td></tr>
    <tr><td><b>Разрушение мифа</b></td><td>«ИИ не пишет за тебя. Он пишет черновик.»</td></tr>
    <tr><td><b>Конфликт</b></td><td>«Живой текст и канцелярия — одна мысль, две подачи.»</td></tr>
    <tr><td><b>Конкретный результат</b></td><td>«Абзац канцелярии — в живой за один промпт.»</td></tr>
    <tr><td><b>Наблюдение из практики</b></td><td>«Замечаю: бросают всегда на третьей строке.»</td></tr>
    <tr><td><b>Провокация</b></td><td>«Твой текст скучный не из-за темы.»</td></tr>
    <tr><td><b>Вопрос новичка</b></td><td>«Почему мой пост читают три человека?»</td></tr>
    <tr><td><b>До / после</b></td><td>«Было: “в современном мире…”. Стало: по делу.»</td></tr>
  </table>
  <p class="note">Правило хука: вынеси самую острую мысль в первую строку, убери разгон. Первое слово уже работает.</p>
"""))

# P9 · До/после
P.append(page("До / после", 9,
  '<span class="kick">Разборы · одна мысль, две подачи</span>'
  '<h2>Канцелярия → живой</h2>'
  + pair(
    '«В современном мире нейросети являются важным инструментом для повышения эффективности создания контента.»',
    '«Нейросеть накидает черновик. Ты правишь — и постишь. Без возни с чистого листа.»')
  + pair(
    '«Наша команда экспертов предлагает взаимовыгодное сотрудничество по вопросам контента.»',
    '«Соберём тебе контент под ключ: идея, текст, визуал. Пишешь задачу — присылаем план.»')
  + pair(
    '«Стоит отметить, что использование ИИ открывает уникальные возможности для бизнеса.»',
    '«ИИ снимает рутину: карточки, посты, ответы. Освобождает вечер — вот и вся магия.»')
  + '<p class="note">Смысл везде сохранён. Ушли разгон, штампы и отглагольные — пришли короткие фразы и конкретика.</p>'
))

# P10 · Промпт-редактор
P.append(page("Промпт · редактор", 10,
  '<span class="kick">Этап · оживить текст</span>'
  '<h2>Claude — редактор живого текста</h2>'
  '<p class="lead">Главный промпт тетради. Даёшь свой абзац — получаешь версию, которую дочитывают. Дальше правишь под свой голос.</p>'
  + prompt("Готовый промпт · Claude",
    "Ты редактор, который делает текст живым и человеческим.\n"
    "Перепиши абзац: сильное начало (первое слово цепляет),\n"
    "короткие фразы, одна мысль на предложение, конкретика\n"
    "вместо общих слов. Убери канцелярию и клише («в современном\n"
    "мире», «важно понимать», «стоит отметить»). Не дави и не\n"
    "продавай в лоб. Смысл и факты сохрани — воду убери.\n"
    "Верни 2 варианта. Текст: [ВСТАВЬ АБЗАЦ]",
    "два варианта дают выбор тона. Не бери вслепую — оставь то, что звучит как ты.")
  + biz("любой текст: посты, описания товара, письма, продающие страницы, ответы клиентам.")
))

# P11 · Промпт-пост
P.append(page("Промпт · пост", 11,
  '<span class="kick">Этап · собрать пост</span>'
  '<h2>Пост по структуре — с нуля</h2>'
  '<p class="lead">Когда нужен не разбор, а готовый пост. Промпт держит структуру из тетради и живой голос.</p>'
  + prompt("Готовый промпт · Claude",
    "Напиши пост 800–1200 знаков по структуре: хук (одно\n"
    "предложение) → ситуация → одна сильная мысль → пример\n"
    "из практики → как применить сегодня → мягкий призыв.\n"
    "Тема: [ТЕМА]. Аудитория: [КТО]. Голос: живой, короткие\n"
    "фразы, конкретика, без штампов. Не начинай с «в этом посте»\n"
    "и приветствия. Не заканчивай вопросом.",
    "заполни [ТЕМА] и [КТО] — получишь каркас. Пример из практики впиши свой, настоящий.")
  + biz("эксперт — прогрев и польза; магазин — посты о товаре; услуга — кейсы и разборы.")
))

# P12 · Промпт-продающий
P.append(page("Промпт · продающий", 12,
  '<span class="kick">Этап · продать без давления</span>'
  '<h2>Продающий текст от задачи клиента</h2>'
  '<p class="lead">Промпт ведёт по структуре «контекст → проблема → гипотеза → решение → шаг» и запрещает начинать с рассказа о себе.</p>'
  + prompt("Готовый промпт · Claude",
    "Напиши продающий текст по структуре: контекст клиента →\n"
    "его проблема → гипотеза → решение → простой следующий шаг.\n"
    "Начни с задачи клиента, не с рассказа о продукте. Без\n"
    "давления, срочности и клише. Живой голос, короткие фразы.\n"
    "Продукт: [ЧТО]. Клиент: [КТО]. Следующий шаг: [ДЕЙСТВИЕ].",
    "«следующий шаг» — не «купи», а лёгкое действие: написать, забрать, попробовать.")
  + biz("услуги и продукты, где решение сложнее кнопки: студия, консалтинг, курсы, b2b.")
))

# P13 · Чек-лист
P.append(page("Чек-лист · честность", 13, """
  <span class="kick">Контроль перед публикацией</span>
  <h2>Проверь текст за минуту</h2>
  <div class="callout check"><div class="h">Чек-лист живого текста</div>
    <div class="row">Первая строка цепляет — без приветствия и «в этом посте»</div>
    <div class="row">Одна мысль на текст; всё лишнее вырезано</div>
    <div class="row">Короткие фразы, есть ритм; прочитал вслух — не споткнулся</div>
    <div class="row">Ни одной фразы из стоп-листа</div>
    <div class="row">Есть конкретика и пример из практики, а не общие слова</div>
    <div class="row">Призыв мягкий, один, в Telegram за конкретным</div>
  </div>
  <p class="note">Честно: примеры до/после — учебные, в нише ИИ/контента. Никаких выдуманных цифр и результатов клиентов. Факты в своём тексте бери только настоящие.</p>
"""))

# P14 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Пиши так,<br>чтобы <span style="color:var(--o2)">дочитывали.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:46ch;margin:0 auto 20px">Приёмы, структура поста и продающего, стоп-лист фраз и три промпта для Claude — вся тетрадь дня. Прогони свой текст и выложи живой.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Текст, который читают · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
