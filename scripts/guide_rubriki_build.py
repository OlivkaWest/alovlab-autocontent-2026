# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 17 «Рубрики вместо случайностей» — премиум-PDF (фикс-A4).
Система рубрик вместо случайного контента: 4 опоры 2:1:1:1, базовые рубрики AlovLab,
анатомия рубрики, 4 промпта Claude (сетка → выпуски → неделя → банк хуков), до/после,
бланк сетки и плана недели, чек-лист. Ядро — «конвейер, а не генерации».
Честность: без выдуманных цифр. База CSS — из v2. Запуск: python3 scripts/guide_rubriki_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "rubriki"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-rubriki.html"

EXTRA = r"""
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.prompt code{font-size:9.1pt}
.rec{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:8px 0;align-items:start}
.rec .n{width:22px;height:22px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}
.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:9px 0}
.pair .c{border-radius:12px;padding:11px 13px;font-size:9.6pt;line-height:1.48}
.pair .bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.pair .good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.pair .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:5px}
.pair .bad .l{color:#c56b43}.pair .good .l{color:var(--o)}
.form{background:#13100a;border:1px solid rgba(255,150,80,.28);border-left:3px solid var(--o);border-radius:12px;padding:14px 16px;margin:11px 0}
.form .r{display:flex;flex-wrap:wrap;gap:9px;align-items:center;font-size:11pt;color:#ffd9b8;font-weight:700}
.form .r span{background:rgba(255,255,255,.06);border:1px solid rgba(255,150,80,.3);border-radius:8px;padding:5px 11px}
.form .r i{color:var(--o2);font-style:normal;font-weight:800}
.form .cap{margin-top:9px;font-size:9.3pt;color:#b9ad9b;line-height:1.4}
/* четыре опоры */
.opora{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:10px 0}
.opora .o4{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:12px;padding:11px 13px}
.opora .o4 .t{font-weight:800;font-size:11pt;color:var(--ink);display:flex;align-items:center;justify-content:space-between;line-height:1}
.opora .o4 .t i{font-style:normal;color:#fff;font-size:8.5pt;font-weight:800;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:6px;padding:3px 8px}
.opora .o4 p{margin-top:6px;font-size:9.3pt;line-height:1.4;color:var(--body)}
/* неделя-полоса */
.wk{display:grid;grid-template-columns:repeat(5,1fr);gap:7px;margin:12px 0}
.wk .d{border-radius:10px;padding:10px 6px;text-align:center;background:#fff;border:1px solid var(--line)}
.wk .d.p2{border-color:var(--o);background:var(--o-tint)}
.wk .d b{display:block;font-size:7.6pt;letter-spacing:.03em;text-transform:uppercase;color:var(--o);font-weight:800}
.wk .d span{display:block;margin-top:5px;font-size:9pt;color:var(--ink);font-weight:700;line-height:1.15}
/* действия (шаги) */
.act{margin:10px 0 4px}
.act .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:7px 0;align-items:start}
.act .s .k{width:20px;height:20px;border-radius:6px;background:#ece0cc;color:#8a6127;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;line-height:1;margin-top:1px}
.act .s p{font-size:9.6pt;line-height:1.44;color:var(--body)}
.act .s p b{color:var(--ink);font-weight:800}
.act .s p em{font-style:normal;color:var(--o);font-weight:700}
.actlbl{display:block;font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin:6px 0 2px}
"""
CSS = V2CSS + EXTRA

VOICE = "[ГОЛОС] живо, короткие фразы, конкретика, без штампов и эмодзи-мусора."

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · рубрики вместо случайностей</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>Разбор:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def biz(txt, lbl="Пример"):
    return f'<div class="biz"><b>{lbl}</b>{txt}</div>'

def rec(n, title, body):
    return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{title}</b><p>{body}</p></div></div>'

def pair(bad, good, bl="Случайность", gl="Рубрика"):
    return (f'<div class="pair"><div class="c bad"><span class="l">✕ {bl}</span>{bad}</div>'
            f'<div class="c good"><span class="l">✓ {gl}</span>{good}</div></div>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def act(lbl, steps):
    body = "".join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i, t in enumerate(steps, 1))
    return f'<span class="actlbl">{lbl}</span><div class="act">{body}</div>'

def opora(cards):
    body = "".join(f'<div class="o4"><div class="t">{t}<i>{tag}</i></div><p>{p}</p></div>' for t, tag, p in cards)
    return f'<div class="opora">{body}</div>'

P = []

# P1 · Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 17</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Рубрики вместо <span style="color:var(--o2)">случайностей.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Как перестать придумывать контент с нуля каждый день. Четыре опоры 2:1:1:1, готовые рубрики, анатомия выпуска и промпты, которые собирают твою сетку и неделю.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">4 опоры</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Сетка рубрик</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">План недели</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">4 промпта</span>
    </div>
  </div>
</section>""")

# P2 · Что внутри
P.append(page("Что внутри", 2,
  head("Тетрадь под карусель «Рубрики вместо случайностей»", "Не ищи тему — крути рубрику",
    "Контент по вдохновению выгорает: каждый день начинаешь с пустого экрана. Рубрики превращают это в конвейер — повторяемую систему, которая выдаёт результат стабильно.")
  + '<div class="flow">'
    '<div class="node"><b>Reels</b><span>охват</span></div><div class="arr">→</div>'
    '<div class="node"><b>Профиль</b><span>мост</span></div><div class="arr">→</div>'
    '<div class="node"><b>Telegram</b><span>оффер</span></div><div class="arr">→</div>'
    '<div class="node"><b>Заявка</b><span>курс / бриф</span></div>'
    '</div>'
  + '<div class="term"><b>Опора</b> — <span>тип контента по задаче: польза, смысл, практика, приглашение. Четыре опоры держат весь контент.</span></div>'
  + '<div class="term"><b>Рубрика</b> — <span>повторяемый формат внутри опоры со своим названием и структурой. Зритель узнаёт её и ждёт следующий выпуск.</span></div>'
  + '<div class="callout result"><div class="h">Что на выходе</div><p>Своя сетка из 4 рубрик под нишу, план недели по пропорции 2:1:1:1 и банк заголовков — система, которую крутишь месяцами, а не придумываешь заново.</p></div>'
))

# P3 · Диагноз
P.append(page("Диагноз", 3,
  head("Почему выгораешь", "Контент по вдохновению", "Проблема не в лени и не в нехватке идей. Проблема в том, что нет системы — и каждый пост рождается заново.")
  + rec(1, "Пустой экран по утрам", "«Что сегодня постить» — вопрос, который отнимает больше сил, чем сам пост.")
  + rec(2, "Каждый раз с нуля", "Ищешь тему, формат, заход — всё заново. Ничего не переиспользуется.")
  + rec(3, "Зритель не понимает, за чем пришёл", "Сегодня разбор, завтра мотивация, послезавтра мем. Нет узнавания — нет привычки возвращаться.")
  + rec(4, "К пятнице — пусто", "Вдохновение кончается быстрее недели. Появляются пропуски, а за ними — чувство вины.")
  + '<p class="note">Хорошая новость: контент — это не творческий порыв, а процесс. А процесс можно собрать из повторяемых рубрик.</p>'
))

# P4 · Сдвиг
P.append(page("Сдвиг", 4,
  head("Одна замена", "Не тема. Рубрика", "Пока гоняешься за темой — каждый день начинаешь с нуля. Как только крутишь рубрику — тема находится сама, внутри понятной рамки.")
  + pair('Ищешь искру: «о чём бы сегодня». Нашёл — на день хватило. Завтра снова пустой экран.',
         'Крутишь маховик: у тебя 4 рубрики. Сегодня «ИИ сделал сам» — осталось выбрать, что показать. Рамка уже есть.',
         "Искра", "Маховик")
  + '<div class="term"><b>Конвейер, а не генерации</b> — <span>ценность не в одном красивом посте, а в системе, которая выдаёт результат стабильно. Рубрика — деталь этого конвейера.</span></div>'
  + '<p class="note">Рубрика не убивает творчество — она освобождает его. Не тратишь силы на «что», вкладываешь их в «как сильнее».</p>'
))

# P5 · Четыре опоры
P.append(page("Четыре опоры", 5,
  head("Фундамент", "На чём стоит весь контент", "Любой сильный контент опирается на одну из четырёх задач. Держи все четыре — и профиль работает и на охват, и на доверие, и на заявку.")
  + opora([
      ("Польза", "×2", "Приём, разбор, инструкция — зритель уносит результат. Это ядро охвата, поэтому её вдвое больше."),
      ("Смысл", "×1", "Взгляд Ильи: как надо и как нет. Строит доверие и отделяет тебя от «ещё одного эксперта»."),
      ("Практика", "×1", "Что реально вышло в работе, с деталью. Доказательство вместо обещаний."),
      ("Приглашение", "×1", "Мягкий шаг: гайд, интенсив, бриф. Не чаще одного раза за 3–4 поста."),
    ])
  + '<p class="note">Опора — это <b>зачем</b> пост. Рубрика — <b>как</b> он выглядит. Сначала опоры, потом под каждую — рубрика.</p>'
))

# P6 · Пропорция недели
P.append(page("Пропорция 2:1:1:1", 6,
  head("Ритм недели", "Как 2:1:1:1 ложится на неделю", "Пять единиц контента в неделю. Две — польза, по одной — смысл, практика, приглашение. Это здоровый баланс: полезно, но не пресно; продающе, но не навязчиво.")
  + '<div class="wk">'
    '<div class="d p2"><b>Пн</b><span>Польза</span></div>'
    '<div class="d"><b>Вт</b><span>Смысл</span></div>'
    '<div class="d p2"><b>Ср</b><span>Польза</span></div>'
    '<div class="d"><b>Чт</b><span>Практика</span></div>'
    '<div class="d"><b>Пт</b><span>Пригла&shy;шение</span></div>'
    '</div>'
  + '<div class="callout check"><div class="h">Почему так</div>'
    '<div class="row">Польза ×2 — она даёт охват, её всегда больше</div>'
    '<div class="row">Приглашение ×1 — один мягкий шаг в неделю, без давления</div>'
    '<div class="row">Дни — ориентир, а не закон: держи пропорцию, а не расписание</div>'
    '</div>'
  + biz("это скелет. Формат под каждый день выбираешь сам: Reels для охвата, пост или карусель — для смысла и практики.", "Как читать")
))

# P7 · Базовые рубрики AlovLab
P.append(page("Базовые рубрики", 7,
  head("Готовый костяк", "Четыре рубрики AlovLab", "Их можно взять как есть или переложить под свою нишу. Каждая закреплена за опорой — вместе они закрывают пропорцию.")
  + '<div class="scene"><div class="sn">1</div><div><div class="sh">«ИИ сделал сам»</div><div class="sd">Демонстрация результата + метод: нейросеть делает работу на глазах, ты показываешь, как повторить. Ядро, приоритет.</div></div><span class="stag">польза</span></div>'
  + '<div class="scene"><div class="sn">2</div><div><div class="sh">«Дело не в модели»</div><div class="sd">Почему у новичка выходит дёшево и что решает на самом деле. Голос наставника, а не продавца.</div></div><span class="stag">смысл</span></div>'
  + '<div class="scene"><div class="sn">3</div><div><div class="sh">«Связка недели»</div><div class="sd">Узкий разбор одной рабочей связки инструментов, которую применил в деле.</div></div><span class="stag">практика</span></div>'
  + '<div class="scene"><div class="sn">4</div><div><div class="sh">«Не бойся инструмента»</div><div class="sd">Спокойная провокация про страх и замену: мягкий заход к гайду или интенсиву.</div></div><span class="stag">приглашение</span></div>'
  + '<p class="note">Названия — узнаваемость. Зритель видит «ИИ сделал сам» и уже знает, что будет разбор с результатом.</p>'
))

# P8 · Анатомия рубрики
P.append(page("Анатомия рубрики", 8,
  head("Собери свою", "Из чего состоит рубрика", "Чтобы рубрика повторялась, у неё должна быть жёсткая рамка. Шесть полей — и она готова крутиться месяцами.")
  + rec(1, "Название", "Короткое, узнаваемое. «Связка недели», а не «полезный контент про инструменты».")
  + rec(2, "Опора", "К какой из четырёх относится: польза / смысл / практика / приглашение.")
  + rec(3, "Формат", "Reels, пост или карусель. Один формат на рубрику — так проще собирать.")
  + rec(4, "О чём", "Одна фраза: что зритель всегда получает в этой рубрике.")
  + rec(5, "Структура выпуска", "Повторяемый скелет: хук → проблема → приём → результат → CTA.")
  + rec(6, "Выход воронки", "Куда ведёт: курс (какой тариф) или бриф студии. Каждый выпуск работает на заявку.")
))

# P9 · Промпт 1
P.append(page("Промпт 1 · сетка", 9,
  head("Этап · собрать сетку рубрик", "Claude соберёт костяк под нишу", "Первый шаг: получить 4 рубрики, разложенные по опорам. Дальше ты только правишь под свой голос.")
  + act("Что делаешь", [
      "Открываешь Claude, вставляешь промпт ниже.",
      "Подставляешь <b>[ТВОЯ НИША]</b> — например «нейросети для контента» или «кофейня у дома».",
      "Получаешь 4 рубрики, <em>выбираешь названия</em>, которые звучат по-твоему.",
      "Переносишь в бланк на стр. 14 — это твой постоянный костяк.",
    ])
  + prompt("Промпт · Claude",
    "Собери 4 повторяемые рубрики под опоры 2:1:1:1\n"
    "(2 польза · 1 смысл · 1 практика · 1 приглашение) для ниши [ТВОЯ].\n"
    "По каждой рубрике дай: название, опору, формат (reels/пост/\n"
    "карусель), о чём (1 фраза), пример темы выпуска.\n"
    "Рубрики должны крутиться из недели в неделю — это конвейер,\n"
    "а не разовые идеи.\n" + VOICE,
    "получаешь костяк, который крутишь месяцами. Название — чтобы зритель узнавал рубрику с первого кадра.")
))

# P10 · Промпт 2
P.append(page("Промпт 2 · выпуски", 10,
  head("Этап · наполнить рубрику", "Claude придумает выпуски", "Костяк есть. Теперь под одну рубрику собираешь запас конкретных выпусков — чтобы не думать «а что в этот вторник».")
  + act("Что делаешь", [
      "Берёшь одну рубрику из своей сетки (стр. 14).",
      "Подставляешь её <b>название, опору и формат</b> в промпт.",
      "Получаешь 5 выпусков — <em>складываешь в запас</em> на месяц вперёд.",
      "Повторяешь для каждой рубрики — банк тем готов.",
    ])
  + prompt("Промпт · Claude",
    "Возьми рубрику «[НАЗВАНИЕ]» (опора: [ОПОРА], формат: [ФОРМАТ]).\n"
    "Придумай 5 конкретных выпусков. По каждому: тема, боль зрителя,\n"
    "один приём или мысль, чем полезно. Каждый выпуск —\n"
    "самостоятельный, без воды и повторов. Ниша: [ТВОЯ].\n" + VOICE,
    "5 выпусков на рубрику × 4 рубрики = запас на месяц. Пустого экрана больше нет.")
))

# P11 · Промпт 3
P.append(page("Промпт 3 · неделя", 11,
  head("Этап · собрать неделю", "Claude разложит неделю по 2:1:1:1", "Из запаса выпусков собираешь конкретную неделю в нужной пропорции — с днями, форматами и черновиками хуков.")
  + act("Что делаешь", [
      "Вставляешь список своих рубрик в промпт.",
      "Claude раскладывает <b>5 единиц по дням</b> в пропорции 2:1:1:1.",
      "Проверяешь: приглашение — <em>один раз</em> за неделю, мягко.",
      "Переносишь в план недели (стр. 14) и идёшь снимать.",
    ])
  + prompt("Промпт · Claude",
    "Собери контент-неделю по пропорции 2:1:1:1 из моих рубрик:\n"
    "[СПИСОК РУБРИК]. Разложи таблицей по дням: день · опора ·\n"
    "рубрика · формат · тема · черновик хука. Приглашение — один\n"
    "раз за неделю, мягко, без давления. Ниша: [ТВОЯ].\n" + VOICE,
    "на выходе — готовая сетка недели. Остаётся снять и опубликовать, а не придумывать.")
))

# P12 · Промпт 4
P.append(page("Промпт 4 · хуки", 12,
  head("Этап · банк заголовков", "Claude даст первые строки", "Хук решает, досмотрят или пролистнут. Под каждую рубрику собираешь банк сильных первых строк разных типов.")
  + act("Что делаешь", [
      "Берёшь рубрику и просишь 10 хуков разного типа.",
      "Отбираешь <b>3–4 самых острых</b>, остальные — в запас.",
      "Правило: первое слово уже цепляет, <em>без «привет» и «в этом посте»</em>.",
      "Ставишь хук в начало выпуска — рамка рубрики + свежий заход.",
    ])
  + prompt("Промпт · Claude",
    "Для рубрики «[НАЗВАНИЕ]» дай 10 сильных первых строк (хуков).\n"
    "Чередуй типы: ошибка · разрушение мифа · конкретный результат ·\n"
    "вопрос новичка · до/после. Без приветствий и «в этом посте».\n"
    "Каждый хук — одна строка, первое слово уже цепляет. Ниша: [ТВОЯ].\n" + VOICE,
    "8 типов хуков чередуешь между выпусками — рубрика повторяется, а заход всегда свежий.")
))

# P13 · До / после
P.append(page("До / после", 13,
  head("Разбор", "Случайность против рубрики")
  + pair('«Сегодня 5 нейросетей, завтра — про мотивацию, потом — мем». Зритель не понимает, за чем подписан, и не ждёт следующий пост.',
         '«Вторник — “ИИ сделал сам”». Зритель знает: будет разбор с результатом. Узнаёт рубрику и возвращается за ней.')
  + '<span class="kick" style="display:block;margin-top:14px">Под свою нишу</span>'
  + '<div class="pair"><div class="c good"><span class="l">Эксперт</span>«Разбор недели» · «Ошибка новичка» · «Как я делаю» · «Забирай шаблон»</div>'
    '<div class="c good"><span class="l">Кофейня</span>«Напиток недели» · «Как мы варим» · «Гость дня» · «Загляни на чашку»</div></div>'
  + '<div class="pair"><div class="c good"><span class="l">Услуга</span>«Кейс недели» · «Так делать нельзя» · «До/после» · «Разбор брифа»</div>'
    '<div class="c good"><span class="l">Магазин</span>«Находка недели» · «Как выбрать» · «Распаковка» · «Подборка в канале»</div></div>'
))

# P14 · Бланк
P.append(page("Бланк · собери систему", 14,
  head("Шаблон · заполни под себя", "Сетка рубрик")
  + opora([
      ("Польза ×2", "рубрика", "Название: ______________  ·  формат: ______"),
      ("Смысл ×1", "рубрика", "Название: ______________  ·  формат: ______"),
      ("Практика ×1", "рубрика", "Название: ______________  ·  формат: ______"),
      ("Приглашение ×1", "рубрика", "Название: ______________  ·  формат: ______"),
    ])
  + '<span class="kick" style="display:block;margin-top:12px">План недели</span>'
  + '<div class="wk">'
    '<div class="d p2"><b>Пн · Польза</b><span>________</span></div>'
    '<div class="d"><b>Вт · Смысл</b><span>________</span></div>'
    '<div class="d p2"><b>Ср · Польза</b><span>________</span></div>'
    '<div class="d"><b>Чт · Практика</b><span>________</span></div>'
    '<div class="d"><b>Пт · Пригл.</b><span>________</span></div>'
    '</div>'
  + '<p class="note">Заполнил сетку и неделю — у тебя система, а не случайности. Дальше только крути маховик.</p>'
))

# P15 · Чек-лист
P.append(page("Чек-лист · честность", 15,
  head("Контроль", "Система или хаос")
  + '<div class="callout check"><div class="h">Чек-лист рубрик</div>'
    '<div class="row">Есть 4 рубрики, закреплённые за опорами</div>'
    '<div class="row">Пропорция недели держится: 2 польза · 1 смысл · 1 практика · 1 приглашение</div>'
    '<div class="row">У каждой рубрики — своё название и повторяемая структура</div>'
    '<div class="row">Приглашение — не чаще 1 из 3–4 постов, без давления</div>'
    '<div class="row">Каждый выпуск ведёт в Telegram за конкретным и имеет выход воронки</div>'
    '<div class="row">Виден принцип «конвейер, а не генерации»</div>'
    '</div>'
  + '<p class="note">Честно: рубрики — не про то, чтобы постить больше. Про то, чтобы постить стабильно и узнаваемо. Примеры в тетради — учебные, без выдуманных цифр и обещаний.</p>'
))

# P16 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Собери сетку —<br>не лови <span style="color:var(--o2)">искру.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:47ch;margin:0 auto 20px">Четыре опоры, готовые рубрики, план недели и промпты для Claude — вся тетрадь дня. Перестань придумывать контент с нуля и запусти конвейер.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Рубрики вместо случайностей · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
