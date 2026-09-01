# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 5 «Разбор конкурента с ИИ: от ссылки до 20 тем» — премиум-PDF (фикс-A4).
По GLOBAL METHODOLOGY RULE: самостоятельный продукт, конкретный результат, workflow, промпты с переменными
и уровнями (Быстрый/Про/Advanced), пример, плохо/хорошо, ACTION, QUALITY CHECK, курс-мост под тему,
блок «Путь в команду AlovLab». Честность: только видимое, UNKNOWN где нет данных; без выдуманных цифр.
Запуск: python3 scripts/guide_competitor_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "competitor"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-competitor.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.rec{display:grid;grid-template-columns:26px 1fr;gap:12px;margin:8px 0;align-items:start}
.rec .n{width:26px;height:26px;border-radius:8px;background:#13100a;color:var(--o2);font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.prompt code{font-size:8.7pt;line-height:1.5}
.lvl{display:inline-block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:20px;padding:4px 12px;margin-bottom:6px}
.vars{background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 13px;margin:8px 0}
.vars b{color:var(--ink);font-weight:800;font-size:9.2pt}.vars p{font-size:9.4pt;line-height:1.44;color:var(--body);margin-top:3px}
.vars code{background:#efe6d8;color:#8a5a27;border-radius:5px;padding:1px 6px;font-weight:700;font-size:8.8pt}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:9px 0}
.pair .c{border-radius:12px;padding:11px 13px;font-size:9.3pt;line-height:1.46}
.pair .bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.pair .good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.pair .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:5px}
.pair .bad .l{color:#c56b43}.pair .good .l{color:var(--o)}
.ex{border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:9px 0}
.ex .r{display:grid;grid-template-columns:150px 1fr;gap:12px;padding:11px 15px;border-bottom:1px solid var(--line);align-items:baseline}
.ex .r:last-child{border-bottom:0}.ex .r.hi{background:var(--o-tint)}
.ex .r b{font-weight:800;font-size:8.3pt;letter-spacing:.03em;text-transform:uppercase;color:var(--muted)}
.ex .r.hi b{color:var(--o)}.ex .r p{font-size:9.4pt;line-height:1.4;color:var(--ink)}
.action{background:#13100a;border-radius:14px;padding:14px 18px;margin:9px 0;color:#f4efe6}
.action .h{font-weight:800;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;color:var(--o2);margin-bottom:8px}
.action .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:6px 0;align-items:start}
.action .s .k{width:20px;height:20px;border-radius:6px;background:var(--o);color:#160e07;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;margin-top:1px}
.action .s p{font-size:9.6pt;line-height:1.4;color:#eae4da}
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:15px 18px;margin:9px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12pt;color:#fff;margin-bottom:6px}
.team p{font-size:9.6pt;line-height:1.5;color:#cdbfa8}
.team .dirs{display:flex;flex-wrap:wrap;gap:6px;margin:9px 0 3px}
.team .dirs span{font-size:8.4pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:4px 10px}
"""
CSS = V2CSS + EXTRA
VOICE = "[ГОЛОС] живо, без штампов; чего не видно, помечай UNKNOWN."

def page(section, num, inner, mid=False):
    mc = ' mid' if mid else ''
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{mc}">{inner}</div>'
            f'<div class="pf"><span>AlovLab · разбор конкурента с ИИ</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')
def head(kick,h2,lead=None):
    l=f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def recn(n,t,b): return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{t}</b><p>{b}</p></div></div>'
def prompt(tag,code,ru=None):
    ru_html=f'<div class="ru"><b>Подсказка:</b> {ru}</div>' if ru else ''
    return f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span><span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>'
def action(steps):
    return '<div class="action"><div class="h">Сделай сейчас</div>'+''.join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i,t in enumerate(steps,1))+'</div>'

P=[]

# 01 Обложка (сильный результат)
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 5</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:17ch">Разбор конкурента с ИИ: <span style="color:var(--o2)">от ссылки до 20 тем.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:46ch">За 30 минут вскрываешь чужую воронку, находишь его дыры и собираешь 15–20 готовых тем под свою нишу. Готовые промпты, реальный workflow и пример внутри.</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Workflow из 8 шагов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 уровня промптов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">20 тем на выходе</span>
    </div>
  </div>
</section>""")

# 02 Что ты сделаешь
P.append(page("Что ты сделаешь",2,
  head("Результат","К концу тетради у тебя на руках",
    "Не «разберёшься в конкурентах», а конкретный результат, который можно применить сегодня.")
  + recn("1","Карта конкурента","оффер, аудитория, хуки, воронка — по одной ссылке.")
  + recn("2","Таблица позиционирования","где он сильный, где слабый, чем вы отличаетесь.")
  + recn("3","Контент-дыры","темы и форматы, которые он НЕ закрывает — твой вход.")
  + recn("4","20 тем под свою нишу","отранжированные, готовые в контент-план.")
  + '<p class="note">Если к концу ты не собрал хотя бы список тем — вернись к workflow и пройди шаги заново.</p>'
))

# 03 Как это работает
P.append(page("Как это работает",3,
  head("Коротко","ИИ читает то, что видно, и раскладывает по полкам",
    "Ты даёшь ИИ то, что реально доступно: ссылку, а лучше текст/скрины страниц конкурента. Он не гадает — раскладывает по схеме и честно помечает, где данных нет.")
  + '<div class="callout result"><div class="h">Логика</div><p>Задача → инструмент → промпт → результат. Инструмент выбираем под задачу: для структурного разбора удобен Claude, подойдёт и ChatGPT. Модель — актуальная на момент работы (проверь ряд в приложении).</p></div>'
  + '<p class="note">Если ИИ не открывает ссылку — скопируй текст страницы или приложи скриншоты. Это нормальный рабочий приём.</p>'
))

# 04 Что понадобится
P.append(page("Что понадобится",4,
  head("Инструменты","Минимум, чтобы начать")
  + recn("1","Claude или ChatGPT","аккаунт и доступ к актуальной модели.")
  + recn("2","2–5 конкурентов","ссылки на сайт, канал, посты, лендинг.")
  + recn("3","Текст/скрины страниц","на случай, если ИИ не открывает ссылку напрямую.")
  + recn("4","Своя ниша и оффер","чтобы темы получились под тебя, а не в вакууме.")
  + '<div class="callout"><div class="h">Minimum effective workflow</div><p>Хватит одного конкурента и одного промпта, чтобы получить первый результат. Остальное — усиление.</p></div>'
))

# 05 Workflow
P.append(page("Workflow",5,
  head("Пошаговый процесс","8 шагов от ссылки до тем",
    "Промпт — часть процесса, а не вся магия. Вот весь путь.")
  + recn("1","Собрать конкурентов","2–5 ссылок или текстов.")
  + recn("2","Дать ИИ данные","ссылку, а лучше текст/скрин страниц.")
  + recn("3","Разбор позиционирования","оффер, аудитория, хуки, воронка.")
  + recn("4","Повторяющиеся темы","о чём он пишет чаще всего.")
  + recn("5","Контент-дыры","чего НЕ делает или делает слабо.")
  + recn("6","Идеи","превратить дыры в темы под твою нишу.")
  + recn("7","Ранжировать","по интересу аудитории и простоте.")
  + recn("8","Контент-план","разложить топ-темы по неделям.")
))

# 06 Основной промпт (Быстрый)
P.append(page("Промпт · быстрый",6,
  head("Уровень 1","Разбор одного конкурента за минуту")
  + '<span class="lvl">Быстрый · за минуты</span>'
  + '<div class="vars"><b>Что вставить:</b><p><code>[ССЫЛКА/ТЕКСТ]</code> — страница конкурента. <code>[НИША]</code> — твоя. <b>Что получишь:</b> карту по 5 пунктам + список его дыр.</p></div>'
  + prompt("Промпт · Claude/ChatGPT",
    "Разбери конкурента: [ССЫЛКА/ТЕКСТ]. Разложи по схеме:\n"
    "1) оффер — что продаёт и как формулирует ценность;\n"
    "2) аудитория — на кого, боли и язык;\n"
    "3) хуки — чем цепляет в первых строках (типы);\n"
    "4) воронка — куда ведёт и чем закрывает;\n"
    "5) гэпы — чего НЕ делает или делает слабо.\n"
    "Только по тому, что реально видно. Нет данных — пиши UNKNOWN.\n"
    "В конце: что из этого взять под нишу [НИША].\n" + VOICE,
    "если ИИ не открыл ссылку — вставь текст страницы прямо в чат.")
, mid=True))

# 07 Пример
P.append(page("Пример",7,
  head("Как это выглядит","Задача → результат")
  + '<div class="ex">'
    '<div class="r"><b>Задача</b><p>разобрать студию AI-контента, найти вход для эксперта по нейросетям.</p></div>'
    '<div class="r"><b>Входные</b><p>текст лендинга + 5 постов конкурента (скопированы в чат).</p></div>'
    '<div class="r"><b>Промпт</b><p>быстрый разбор по 5 пунктам (стр. 6).</p></div>'
    '<div class="r"><b>Что получили</b><p>оффер «делаем ролики под ключ», хуки только про «вау-результат», воронка сразу на заявку.</p></div>'
    '<div class="r"><b>Что исправили</b><p>попросили отдельно выписать, о чём он НЕ пишет — обучение и «как повторить самому».</p></div>'
    '<div class="r hi"><b>Финал</b><p>дыра найдена: он продаёт услугу, но не учит. Наш вход — контент «сделай сам», 12 тем.</p></div>'
    '</div>'
, mid=True))

# 08 Промпт Про
P.append(page("Промпт · про",8,
  head("Уровень 2","Таблица позиционирования: ты против него")
  + '<span class="lvl">Про · глубже</span>'
  + '<div class="vars"><b>Что вставить:</b><p><code>[КОНКУРЕНТ]</code> и <code>[ТВОЙ ОФФЕР]</code>. <b>Что получишь:</b> таблицу, где видно, где он сильнее, где ты, и чем отстроиться.</p></div>'
  + prompt("Промпт · Claude/ChatGPT",
    "Сравни меня и конкурента таблицей. Мой оффер: [ТВОЙ ОФФЕР].\n"
    "Конкурент: [КОНКУРЕНТ / текст]. Колонки: параметр, конкурент, я,\n"
    "вывод. Параметры: оффер, аудитория, цена/ценность, хуки,\n"
    "форматы, воронка, слабые места. Затем 3 способа отстроиться\n"
    "от него под нишу [НИША]. Только по фактам, без выдумок.\n" + VOICE,
    "«слабые места» и «способы отстроиться» — самое ценное. На них строим контент.")
, mid=True))

# 09 Advanced
P.append(page("Промпт · advanced",9,
  head("Уровень 3","Несколько конкурентов → 20 тем")
  + '<span class="lvl">Advanced · система</span>'
  + '<div class="vars"><b>Что вставить:</b><p><code>[КОНКУРЕНТЫ 1..N]</code> — тексты/ссылки. <b>Что получишь:</b> сводные дыры рынка + 20 отранжированных тем в план.</p></div>'
  + prompt("Промпт · Claude/ChatGPT",
    "Вот 3–5 конкурентов: [КОНКУРЕНТЫ]. Сделай сводный разбор:\n"
    "1) общие темы, которые пишут все (перегрето);\n"
    "2) контент-дыры — чего не делает НИКТО или почти никто;\n"
    "3) 20 тем под нишу [НИША], бьющих в дыры;\n"
    "4) отранжируй по потенциалу: интерес аудитории + простота;\n"
    "5) топ-8 разложи в контент-план на 2 недели.\n"
    "Только по видимому; нет данных — UNKNOWN.\n" + VOICE,
    "перегретые темы не берём как есть — только с новым углом. Дыры = быстрый рост.")
, mid=True))

# 10 Плохо / хорошо
P.append(page("Плохо / хорошо",10,
  head("Разница","Слабый запрос против рабочего")
  + '<div class="pair"><div class="c bad"><span class="l">✕ Слабый</span>«Ты эксперт по маркетингу. Проанализируй конкурентов.»<br><br>Итог: вода, общие слова, ноль конкретики.</div>'
    '<div class="c good"><span class="l">✓ Рабочий</span>Схема из 5 пунктов + «только видимое, UNKNOWN где нет данных» + «что взять под нишу».<br><br>Итог: карта, дыры, темы.</div></div>'
  + '<p class="note">Правило: чем конкретнее схема и ограничения, тем меньше воды. «Проанализируй» — это не задача, это пожелание.</p>'
))

# 11 Checklist
P.append(page("Checklist",11,
  head("Quality check","Проверь разбор перед тем, как строить контент")
  + '<div class="callout check"><div class="h">Чек-лист разбора</div>'
    '<div class="row">Есть все 5 пунктов: оффер, аудитория, хуки, воронка, гэпы</div>'
    '<div class="row">Гэпы конкретные, а не «мало контента»</div>'
    '<div class="row">Где нет данных — стоит UNKNOWN, а не выдумка</div>'
    '<div class="row">Есть таблица «ты против него» и 3 способа отстроиться</div>'
    '<div class="row">Темы бьют в дыры, а не повторяют перегретое</div>'
    '<div class="row">Темы отранжированы и разложены в план</div>'
    '<div class="row">Ничего не взято как «факт о клиенте» без источника</div>'
    '</div>'
))

# 12 Сделай сейчас
P.append(page("Сделай сейчас",12,
  head("Практика","20 минут — и у тебя первый результат")
  + action([
      "Открой Claude или ChatGPT, возьми одного конкурента.",
      "Вставь текст его страницы и быстрый промпт (стр. 6).",
      "Выпиши его 3 главные дыры.",
      "Прогони advanced-промпт (стр. 9) и получи 20 тем.",
      "Отметь топ-5 и поставь в план на неделю."])
  + '<p class="note">Сделал шаги 1–3 — разбор уже есть. Дошёл до 5 — у тебя контент-план из чужих дыр.</p>'
))

# 13 Что дальше
P.append(page("Что дальше",13,
  head("Рост навыка","Разбор конкурента — это только вход",
    "Ты научился читать чужую воронку. Дальше этот навык превращается в систему.")
  + recn("→","Из тем — в контент","каждую тему прогоняешь через промпт-каркас и собираешь пост/рил/карусель.")
  + recn("→","Из разбора — в стратегию","дыры рынка становятся твоим позиционированием, а не разовой идеей.")
  + recn("→","Из ручного — в конвейер","разбор+темы+сборка ставятся на поток скиллами (см. тетрадь Дня 3).")
))

# 14 Курс (адаптирован под тему)
P.append(page("Курс AlovLab",14,
  head("Продолжение","Здесь один workflow. На курсе — вся система",
    "В этой тетради ты разобрал конкурента и собрал темы. Это один навык из большой системы.")
  + '<div class="callout result"><div class="h">Курс «Нейросети и ChatGPT для каждого»</div><p>Идём дальше разбора: собираем систему, где ИИ помогает искать темы, писать структуру, делать визуал и готовить публикацию — от исследования рынка до готового контента и продаж. Маркетинг и SMM на нейросетях как навык, а не разовый промпт.</p></div>'
  + '<p class="note">Забирай промпт и методичку в комментариях под постом (Telegram и ВК). Хочешь всю систему — она внутри курса.</p>'
))

# 15 Путь в команду
P.append(page("Путь в команду AlovLab",15,
  head("Навык может стать профессией","Сильных студентов мы хотим видеть рядом")
  + '<div class="team"><div class="h">Не просто научиться, а начать работать</div>'
    '<p>Мы не хотим только показать кнопки. Ты выбираешь направление, набираешь реальные навыки и собираешь портфолио на настоящих задачах.</p>'
    '<div class="dirs"><span>AI Marketing</span><span>SMM + AI</span><span>AI Content</span><span>Prompt Engineering</span><span>AI Video</span><span>AI Agents</span></div>'
    '<p style="margin-top:8px">Лучших и наиболее активных студентов мы рассматриваем для участия в проектах AlovLab и совместной работы. Без обещаний «всем гарантированно» — по навыку и результату.</p></div>'
  + '<p class="note">Путь простой: пришёл разобраться в ИИ → научился делать результат → выбрал направление → получил реальные задачи → собрал портфолио → стал специалистом.</p>'
, mid=True))

# 16 Финал/контакты
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:25pt;line-height:1.12;margin:18px 0 8px">Не листай конкурента.<br><span style="color:var(--o2)">Разбери его.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Промпты, workflow и 20 тем — вся тетрадь дня. Систему контента на нейросетях собираем на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Промпт + методичка — в комментариях</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru · Бриф → @alovlab</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Разбор конкурента с ИИ · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
