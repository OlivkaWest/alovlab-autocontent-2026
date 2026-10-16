# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 5 «Разбор конкурента с ИИ: от ссылки до 20 тем» — премиум-PDF (фикс-A4).
v2 (пересборка): сквозной ЖИВОЙ пример на собирательном конкуренте, глубокие рабочие промпты,
реально показаны заполненный разбор, таблица позиционирования, 20 тем и план на 2 недели.
По GLOBAL METHODOLOGY RULE. Честность: конкурент — учебный собирательный образ, без выдуманных цифр охватов;
показываем метод и его выход, где данных нет — UNKNOWN.
Запуск: python3 scripts/guide_competitor_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "competitor"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-competitor.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.rec{display:grid;grid-template-columns:26px 1fr;gap:12px;margin:7px 0;align-items:start}
.rec .n{width:26px;height:26px;border-radius:8px;background:#13100a;color:var(--o2);font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.prompt code{font-size:8.2pt;line-height:1.5}
.lvl{display:inline-block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:20px;padding:4px 12px;margin-bottom:6px}
.vars{background:#fff;border:1px solid var(--line);border-radius:11px;padding:9px 13px;margin:8px 0}
.vars b{color:var(--ink);font-weight:800;font-size:9.2pt}.vars p{font-size:9.3pt;line-height:1.42;color:var(--body);margin-top:3px}
.vars code{background:#efe6d8;color:#8a5a27;border-radius:5px;padding:1px 6px;font-weight:700;font-size:8.6pt}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:9px 0}
.pair .c{border-radius:12px;padding:11px 13px;font-size:9.3pt;line-height:1.46}
.pair .bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.pair .good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.pair .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:5px}
.pair .bad .l{color:#c56b43}.pair .good .l{color:var(--o)}
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
/* --- живой пример --- */
.demo{display:inline-flex;align-items:center;gap:7px;font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:#7a4a1e;background:#f3e4d1;border-radius:20px;padding:4px 11px;margin-bottom:8px}
.cprofile{background:#fff;border:1px solid var(--line);border-radius:13px;padding:14px 16px;margin:9px 0}
.cprofile .nm{font-weight:800;font-size:12.5pt;color:var(--ink)}
.cprofile .sub{font-size:9pt;color:var(--muted);margin-top:2px}
.cprofile .row{display:grid;grid-template-columns:118px 1fr;gap:12px;padding:7px 0;border-top:1px solid var(--line);align-items:baseline;margin-top:8px}
.cprofile .row b{font-weight:800;font-size:8.2pt;letter-spacing:.03em;text-transform:uppercase;color:var(--muted)}
.cprofile .row p{font-size:9.4pt;line-height:1.4;color:var(--ink)}
.fill{border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:9px 0;background:#fff}
.fill .r{display:grid;grid-template-columns:120px 1fr;gap:12px;padding:9px 15px;border-bottom:1px solid var(--line);align-items:baseline}
.fill .r:last-child{border-bottom:0}.fill .r.hi{background:var(--o-tint)}
.fill .r b{font-weight:800;font-size:8.2pt;letter-spacing:.03em;text-transform:uppercase;color:var(--muted)}
.fill .r.hi b{color:var(--o)}.fill .r p{font-size:9.3pt;line-height:1.4;color:var(--ink)}
.fill .r em{font-style:italic;color:var(--body)}
table.pt{width:100%;border-collapse:collapse;margin:9px 0;font-size:8.7pt}
table.pt th{background:#13100a;color:#f0e6d8;font-weight:800;font-size:7.6pt;letter-spacing:.04em;text-transform:uppercase;padding:8px 9px;text-align:left}
table.pt td{border:1px solid var(--line);padding:7px 9px;line-height:1.34;color:var(--ink);vertical-align:top}
table.pt tr:nth-child(even) td{background:#faf6ef}
table.pt td.win{background:var(--o-tint);font-weight:700;color:#8a4a1a}
.gap{display:grid;grid-template-columns:20px 1fr;gap:10px;margin:6px 0;align-items:start}
.gap .k{width:20px;height:20px;border-radius:6px;background:var(--o);color:#160e07;font-weight:800;font-size:9pt;display:flex;align-items:center;justify-content:center;margin-top:1px}
.gap p{font-size:9.4pt;line-height:1.4;color:var(--ink)}.gap p b{color:var(--o)}
.tgrp{margin:7px 0}
.tgrp .gh{font-weight:800;font-size:8.4pt;letter-spacing:.04em;text-transform:uppercase;color:var(--o);margin-bottom:4px}
.tgrp ol{margin:0;padding-left:0;list-style:none;counter-reset:t}
.tgrp li{position:relative;padding:3px 0 3px 26px;font-size:9.2pt;line-height:1.35;color:var(--ink);counter-increment:t}
.tgrp li:before{content:counter(t);position:absolute;left:0;top:3px;width:18px;height:18px;border-radius:5px;background:#efe6d8;color:#8a5a27;font-weight:800;font-size:7.6pt;display:flex;align-items:center;justify-content:center}
.plan{border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:9px 0;background:#fff}
.plan .wk{background:#13100a;color:var(--o2);font-weight:800;font-size:8.4pt;letter-spacing:.05em;text-transform:uppercase;padding:7px 15px}
.plan .r{display:grid;grid-template-columns:52px 1fr 84px;gap:10px;padding:8px 15px;border-bottom:1px solid var(--line);align-items:baseline}
.plan .r:last-child{border-bottom:0}
.plan .r .d{font-weight:800;font-size:8.4pt;color:var(--muted)}
.plan .r .t{font-size:9.2pt;line-height:1.32;color:var(--ink)}
.plan .r .f{font-size:7.8pt;font-weight:700;text-align:right;color:var(--o);text-transform:uppercase;letter-spacing:.03em}
"""
CSS = V2CSS + EXTRA
VOICE = "Пиши живо и по делу, без воды и штампов. Где данных нет — UNKNOWN, не додумывай."

def page(section, num, inner, mid=False):
    mc = ' mid' if mid else ''
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{mc}">{body}</div>'
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
DEMO = '<span class="demo">● живой пример</span>'

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 5</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:17ch">Разбор конкурента с ИИ: <span style="color:var(--o2)">от ссылки до 20 тем.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:46ch">За 30 минут вскрываешь чужую воронку, находишь его дыры и собираешь 20 готовых тем под свою нишу. Внутри — 3 рабочих промпта и сквозной живой разбор конкурента от начала до плана.</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 промпта в полную силу</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Живой пример</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">20 тем + план</span>
    </div>
  </div>
</section>""")

# 02 Что ты сделаешь
P.append(page("Что ты сделаешь",2,
  head("Результат","К концу тетради у тебя на руках",
    "Не «разберёшься в конкурентах», а конкретный результат, который применяешь сегодня.")
  + recn("1","Карта конкурента","оффер, аудитория, хуки, воронка — по одной ссылке.")
  + recn("2","Таблица «ты против него»","где он сильный, где слабый, чем ты отстраиваешься.")
  + recn("3","Список контент-дыр","темы и форматы, которые он НЕ закрывает — твой вход.")
  + recn("4","20 тем под свою нишу","отранжированы, топ-8 разложен в план на 2 недели.")
  + '<div class="callout result"><div class="h">Как читать эту тетрадь</div><p>Слева — промпт и метод. Справа по ходу — <b>живой разбор</b> одного конкурента от «кто это» до готового плана. Ты видишь не только «что вставить», а что реально выходит.</p></div>'
))

# 03 Как это работает
P.append(page("Как это работает",3,
  head("Коротко","ИИ читает то, что видно, и раскладывает по полкам",
    "Ты даёшь ИИ доступное: ссылку, а лучше текст или скрины страниц конкурента. Он не гадает — раскладывает по схеме и честно помечает, где данных нет.")
  + '<div class="callout result"><div class="h">Логика</div><p>Задача → инструмент → промпт → результат. Для структурного разбора удобен Claude, подойдёт и ChatGPT. Модель — актуальная на момент работы.</p></div>'
  + '<p class="note">Если ИИ не открывает ссылку — скопируй текст страницы или приложи скриншоты. Это нормальный рабочий приём, а не костыль.</p>'
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

# 06 Промпт 1 — Быстрый (глубокий)
P.append(page("Промпт · быстрый",6,
  head("Уровень 1 · промпт","Разбор одного конкурента")
  + '<span class="lvl">Быстрый · за минуты</span>'
  + '<div class="vars"><b>Что вставить:</b><p><code>[ССЫЛКА/ТЕКСТ]</code> — страница конкурента. <code>[НИША]</code>, <code>[ЦА]</code> — твои. <b>Что получишь:</b> карту по 5 пунктам + 5 ходов отстройки.</p></div>'
  + prompt("Промпт · Claude/ChatGPT",
    "Ты аналитик контента и маркетинга. Разбираешь конкурента только по\n"
    "тому, что реально видно, и ничего не выдумываешь.\n\n"
    "Конкурент: [ССЫЛКА или вставленный текст его страницы и постов].\n"
    "Моя ниша: [НИША]. Моя аудитория: [ЦА].\n\n"
    "Сделай разбор строго по структуре:\n"
    "1. ОФФЕР. Что продаёт и как формулирует ценность. Дословные фразы\n"
    "   бери в кавычки.\n"
    "2. АУДИТОРИЯ. На кого нацелен, какие боли и желания давит, каким\n"
    "   языком говорит.\n"
    "3. ХУКИ. 3-5 приёмов, которыми цепляет в первых строках. У каждого\n"
    "   пометь тип: страх, результат, любопытство, конфликт.\n"
    "4. ВОРОНКА. Куда ведёт, чем закрывает, какой следующий шаг.\n"
    "5. ГЭПЫ. Чего НЕ делает или делает слабо: темы, форматы, глубина.\n\n"
    "В конце: 5 конкретных ходов, которыми я отстроюсь под нишу [НИША].\n"
    + VOICE,
    "не открыл ссылку — вставь текст страницы прямо в чат. ГЭПЫ читай внимательно: это твой вход.")
))

# 07 Живой пример — знакомство с конкурентом
P.append(page("Живой пример · 1",7,
  DEMO + head("Знакомимся","Кого разбираем")
  + '<div class="cprofile"><div class="nm">Канал «Нейросети для новичка»</div>'
    '<div class="sub">Собирательный конкурент в нише обучения ИИ. Учебный образ — без реальных цифр охватов.</div>'
    '<div class="row"><b>Формат</b><p>Reels «говорящая голова + текст на экране», единый шаблон.</p></div>'
    '<div class="row"><b>Продукт</b><p>3-дневный марафон «Освой ChatGPT и начни зарабатывать».</p></div>'
    '<div class="row"><b>Что видно</b><p>лендинг марафона, закреп с гайдом «100 промптов», лента Reels.</p></div>'
    '<div class="row"><b>Что вставили</b><p>текст лендинга + 6 подписей под Reels скопировали прямо в чат.</p></div></div>'
  + '<p class="note">Дальше — ровно то, что вернул ИИ по промпту со стр. 6. Ничего не приукрашивали.</p>'
, mid=True))

# 08 Живой пример — заполненная карта
P.append(page("Живой пример · 2",8,
  DEMO + head("Что вернул ИИ","Карта конкурента")
  + '<div class="fill">'
    '<div class="r"><b>Оффер</b><p>«Освой ChatGPT за 3 дня и начни зарабатывать на нейросетях». Ценность через скорость и деньги.</p></div>'
    '<div class="r"><b>Аудитория</b><p>новички 25–45, боятся отстать, хотят подработку. Язык простой, обещания быстрых денег.</p></div>'
    '<div class="r"><b>Хуки</b><p>«5 нейросетей, которые заменят сотрудника» <em>(результат)</em>; «Ты платишь за то, что ИИ делает бесплатно» <em>(страх)</em>; «Скопируй этот промпт» <em>(халява)</em>.</p></div>'
    '<div class="r"><b>Воронка</b><p>Reels → подписка → бесплатный гайд «100 промптов» → приглашение на марафон → продажа.</p></div>'
    '<div class="r hi"><b>Гэпы</b><p>только ChatGPT (ноль про Claude, агентов, видео); всё на «вау-кнопках», нет системы; один формат; ничего для бизнеса; не учит проверять факты.</p></div>'
    '</div>'
  + '<p class="note">Пять пунктов — и уже видно, где он слабый. Гэпы подсвечены: с них и заходим.</p>'
, mid=True))

# 09 Промпт 2 — Про (таблица позиционирования)
P.append(page("Промпт · про",9,
  head("Уровень 2 · промпт","Таблица «ты против него»")
  + '<span class="lvl">Про · глубже</span>'
  + '<div class="vars"><b>Что вставить:</b><p><code>[ТВОЙ ОФФЕР]</code> и разбор конкурента из промпта 1. <b>Что получишь:</b> таблицу сравнения + 3 способа отстроиться.</p></div>'
  + prompt("Промпт · Claude/ChatGPT",
    "Ты контент-стратег. Сравни меня и конкурента таблицей.\n\n"
    "Мой оффер: [ТВОЙ ОФФЕР]. Моя ниша: [НИША].\n"
    "Разбор конкурента: [вставь результат промпта 1].\n\n"
    "Построй таблицу. Колонки: параметр, конкурент, я, вывод.\n"
    "Параметры: оффер, инструменты, подача, формат, аудитория,\n"
    "глубина, слабое место.\n"
    "В колонке «вывод» по каждой строке пиши, кто сильнее и почему.\n\n"
    "Затем отдельно: 3 способа отстроиться под нишу [НИША], бьющих\n"
    "именно в его слабые места.\n"
    + VOICE,
    "строка «слабое место» и блок «способы отстроиться» — самое ценное. На них строим контент.")
))

# 10 Живой пример — заполненная таблица
P.append(page("Живой пример · 3",10,
  DEMO + head("Что вернул ИИ","Таблица позиционирования")
  + '<table class="pt"><tr><th>Параметр</th><th>Конкурент</th><th>Ты (AlovLab)</th><th>Вывод</th></tr>'
    '<tr><td>Оффер</td><td>«быстро и деньги», марафон</td><td>система: конвейер контента на ИИ</td><td class="win">глубина ↔ скорость</td></tr>'
    '<tr><td>Инструменты</td><td>только ChatGPT</td><td>Claude, Midjourney, агенты</td><td class="win">шире стек</td></tr>'
    '<tr><td>Подача</td><td>вау-кнопки</td><td>метод «делаю на глазах»</td><td class="win">доверие практика</td></tr>'
    '<tr><td>Формат</td><td>один шаблон</td><td>10 форматов-сериалов</td><td class="win">разнообразие</td></tr>'
    '<tr><td>Аудитория</td><td>новичок-подработка</td><td>новичок + бизнес B2B</td><td class="win">два потока</td></tr>'
    '<tr><td>Глубина</td><td>поверхность</td><td>методички + курс</td><td class="win">экспертность</td></tr>'
    '<tr><td>Слабое место</td><td>ноль системы, один инструмент</td><td>—</td><td class="win">← бьём сюда</td></tr>'
    '</table>'
  + '<p class="note">Оранжевым — где перевес твой. Это не «мы лучше», это карта, куда заходить контентом.</p>'
, mid=True))

# 11 Живой пример — дыры в ходы
P.append(page("Живой пример · 4",11,
  DEMO + head("Из таблицы — в ходы","5 дыр, в которые заходим")
  + '<div class="gap"><div class="k">1</div><p><b>Claude.</b> У него ноль. Весь пласт Claude, Claude Code, Skills — свободен.</p></div>'
  + '<div class="gap"><div class="k">2</div><p><b>Система вместо фишек.</b> Он про разовые кнопки. Ты — про конвейер, который выдаёт результат стабильно.</p></div>'
  + '<div class="gap"><div class="k">3</div><p><b>Реальная работа под задачу.</b> У него «5 нейросетей вообще». Ты показываешь, как ИИ делает конкретное дело на глазах.</p></div>'
  + '<div class="gap"><div class="k">4</div><p><b>Бизнес / B2B.</b> Он только про подработку новичка. Аватары, озвучка, агенты под бренд — его нет.</p></div>'
  + '<div class="gap"><div class="k">5</div><p><b>Честность и навык.</b> Он не учит проверять факты. Ты — учишь ловить, где ИИ врёт, и думать головой.</p></div>'
  + '<p class="note">Пять дыр = пять кластеров тем. Дальше промпт превращает их в 20 конкретных заголовков.</p>'
, mid=True))

# 12 Промпт 3 — Advanced (20 тем)
P.append(page("Промпт · advanced",12,
  head("Уровень 3 · промпт","Из дыр — в 20 тем и план")
  + '<span class="lvl">Advanced · система</span>'
  + '<div class="vars"><b>Что вставить:</b><p><code>[ДЫРЫ]</code> из промпта 2, <code>[НИША]</code>, <code>[ЦА]</code>. <b>Что получишь:</b> 20 тем, ранжирование и план на 2 недели.</p></div>'
  + prompt("Промпт · Claude/ChatGPT",
    "Ты контент-стратег. Есть найденные дыры конкурентов (ниже).\n"
    "Ниша: [НИША]. Аудитория: [ЦА].\n\n"
    "Дыры и слабые места: [ДЫРЫ].\n\n"
    "Сделай:\n"
    "1. 20 ТЕМ под нишу, бьющих в эти дыры. Каждая тема: цепляющий\n"
    "   заголовок + одно предложение сути. Сгруппируй по дырам.\n"
    "2. РАНЖИРОВАНИЕ по формуле: интерес аудитории (1-5) плюс простота\n"
    "   съёмки (1-5) минус перегретость (1-5).\n"
    "3. ТОП-8 разложи в контент-план на 2 недели, по 4 в неделю,\n"
    "   с типом контента: Reels, пост или карусель.\n\n"
    "Перегретые темы не бери как есть, только с новым углом.\n"
    + VOICE,
    "20 тем — это не разовый список, это твой контент-банк на месяц вперёд.")
))

# 13 Живой пример — 20 тем
P.append(page("Живой пример · 5",13,
  DEMO + head("Что вернул ИИ","20 тем под нишу — по дырам")
  + '<div class="tgrp"><div class="gh">Дыра 1 · Claude</div><ol>'
    '<li>Claude против ChatGPT: кто пишет живее</li>'
    '<li>Собери свой Claude Skill за 10 минут</li>'
    '<li>Claude разбирает конкурента по ссылке</li>'
    '<li>Дал Claude папку — получил готовый проект</li></ol></div>'
  + '<div class="tgrp"><div class="gh">Дыра 2 · Система / конвейер</div><ol>'
    '<li>Не генерация, а конвейер: контент на потоке</li>'
    '<li>Один промпт-каркас на весь контент-план</li>'
    '<li>Как собрал неделю Reels за вечер</li></ol></div>'
  + '<div class="tgrp"><div class="gh">Дыра 3 · Реальная работа</div><ol>'
    '<li>ИИ смонтировал видео сам</li>'
    '<li>Промпт, который пишет не как ИИ</li>'
    '<li>5 ошибок, из-за которых ИИ отвечает водой</li>'
    '<li>Claude чинит мой текст за 30 секунд</li></ol></div>'
  + '<div class="tgrp"><div class="gh">Дыра 4 · Бизнес / B2B</div><ol>'
    '<li>AI-аватар на 90 языках за один день</li>'
    '<li>Озвучка и дубляж роликов нейросетью</li>'
    '<li>Агент, который отвечает клиентам сам</li>'
    '<li>Контент-конвейер под бренд: как устроен</li></ol></div>'
  + '<div class="tgrp"><div class="gh">Дыра 5 · Честность / навык + заработок</div><ol>'
    '<li>Почему ИИ врёт и как это ловить</li>'
    '<li>Дело не в модели: почему у новичка выходит дёшево</li>'
    '<li>Не бойся инструмента: заменит ли ИИ тебя</li>'
    '<li>Сколько реально платят за AI-контент</li>'
    '<li>Первый заказ на нейросетях: с чего начать</li></ol></div>'
))

# 14 Живой пример — план на 2 недели
P.append(page("Живой пример · 6",14,
  DEMO + head("Что вернул ИИ","Топ-8 → план на 2 недели")
  + '<div class="plan"><div class="wk">Неделя 1</div>'
    '<div class="r"><span class="d">Пн</span><span class="t">ИИ смонтировал видео сам</span><span class="f">Reels</span></div>'
    '<div class="r"><span class="d">Ср</span><span class="t">Claude против ChatGPT: кто пишет живее</span><span class="f">Reels</span></div>'
    '<div class="r"><span class="d">Пт</span><span class="t">Не генерация, а конвейер</span><span class="f">Карусель</span></div>'
    '<div class="r"><span class="d">Вс</span><span class="t">5 ошибок, из-за которых ИИ отвечает водой</span><span class="f">Reels</span></div></div>'
  + '<div class="plan"><div class="wk">Неделя 2</div>'
    '<div class="r"><span class="d">Пн</span><span class="t">Собери свой Claude Skill за 10 минут</span><span class="f">Reels</span></div>'
    '<div class="r"><span class="d">Ср</span><span class="t">Дело не в модели: почему у новичка дёшево</span><span class="f">Reels</span></div>'
    '<div class="r"><span class="d">Пт</span><span class="t">AI-аватар на 90 языках за день</span><span class="f">Карусель · B2B</span></div>'
    '<div class="r"><span class="d">Вс</span><span class="t">Почему ИИ врёт и как это ловить</span><span class="f">Reels</span></div></div>'
  + '<p class="note">Из одной ссылки конкурента — готовый план на 2 недели. Остальные 12 тем идут в банк на следующий месяц.</p>'
))

# 15 Плохо / хорошо
P.append(page("Плохо / хорошо",15,
  head("Разница","Слабый запрос против рабочего")
  + '<div class="pair"><div class="c bad"><span class="l">✕ Слабый</span>«Ты эксперт по маркетингу. Проанализируй конкурентов.»<br><br>Итог: вода, общие слова, ноль конкретики.</div>'
    '<div class="c good"><span class="l">✓ Рабочий</span>Схема из 5 пунктов + «только видимое, UNKNOWN где нет данных» + «что взять под нишу».<br><br>Итог: карта, дыры, темы.</div></div>'
  + '<p class="note">Правило: чем конкретнее схема и ограничения, тем меньше воды. «Проанализируй» — это не задача, это пожелание.</p>'
))

# 16 Checklist
P.append(page("Checklist",16,
  head("Quality check","Проверь разбор перед тем, как строить контент")
  + '<div class="callout check"><div class="h">Чек-лист разбора</div>'
    '<div class="row">Есть все 5 пунктов: оффер, аудитория, хуки, воронка, гэпы</div>'
    '<div class="row">Гэпы конкретные, а не «мало контента»</div>'
    '<div class="row">Где нет данных — стоит UNKNOWN, а не выдумка</div>'
    '<div class="row">Есть таблица «ты против него» и способы отстроиться</div>'
    '<div class="row">Темы бьют в дыры, а не повторяют перегретое</div>'
    '<div class="row">Темы отранжированы и топ-8 разложен в план</div>'
    '<div class="row">Ничего не взято как «факт о клиенте» без источника</div>'
    '</div>'
))

# 17 Сделай сейчас
P.append(page("Сделай сейчас",17,
  head("Практика","20 минут — и у тебя первый результат")
  + action([
      "Открой Claude или ChatGPT, возьми одного конкурента.",
      "Вставь текст его страницы и промпт 1 (стр. 6).",
      "Выпиши его 3 главные дыры.",
      "Прогони промпт 3 (стр. 12) и получи 20 тем.",
      "Отметь топ-8 и поставь в план на 2 недели."])
  + '<p class="note">Сделал шаги 1–3 — разбор уже есть. Дошёл до 5 — у тебя контент-план из чужих дыр.</p>'
))

# 18 Что дальше
P.append(page("Что дальше",18,
  head("Рост навыка","Разбор конкурента — это только вход",
    "Ты научился читать чужую воронку. Дальше этот навык превращается в систему.")
  + recn("→","Из тем — в контент","каждую тему прогоняешь через промпт-каркас и собираешь пост/рил/карусель.")
  + recn("→","Из разбора — в стратегию","дыры рынка становятся твоим позиционированием, а не разовой идеей.")
  + recn("→","Из ручного — в конвейер","разбор + темы + сборка ставятся на поток скиллами (см. тетрадь Дня 3).")
))

# 19 Курс
P.append(page("Курс AlovLab",19,
  head("Продолжение","Здесь один workflow. На курсе — вся система",
    "В этой тетради ты разобрал конкурента и собрал темы. Это один навык из большой системы.")
  + '<div class="callout result"><div class="h">Курс «Нейросети и ChatGPT для каждого»</div><p>Идём дальше разбора: собираем систему, где ИИ помогает искать темы, писать структуру, делать визуал и готовить публикацию — от исследования рынка до готового контента и продаж. Маркетинг и SMM на нейросетях как навык, а не разовый промпт.</p></div>'
  + '<p class="note">Забирай промпты и методичку в комментариях под постом (Telegram и ВК). Хочешь всю систему — она внутри курса.</p>'
))

# 20 Путь в команду
P.append(page("Путь в команду AlovLab",20,
  head("Навык может стать профессией","Сильных студентов мы хотим видеть рядом")
  + '<div class="team"><div class="h">Не просто научиться, а начать работать</div>'
    '<p>Мы не хотим только показать кнопки. Ты выбираешь направление, набираешь реальные навыки и собираешь портфолио на настоящих задачах.</p>'
    '<div class="dirs"><span>AI Marketing</span><span>SMM + AI</span><span>AI Content</span><span>Prompt Engineering</span><span>AI Video</span><span>AI Agents</span></div>'
    '<p style="margin-top:8px">Лучших и наиболее активных студентов мы рассматриваем для участия в проектах AlovLab и совместной работы. Без обещаний «всем гарантированно» — по навыку и результату.</p></div>'
  + '<p class="note">Путь простой: пришёл разобраться в ИИ → научился делать результат → выбрал направление → получил реальные задачи → собрал портфолио → стал специалистом.</p>'
, mid=True))

# 21 Финал
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:25pt;line-height:1.12;margin:18px 0 8px">Не листай конкурента.<br><span style="color:var(--o2)">Разбери его.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">3 промпта, живой разбор и 20 тем — вся тетрадь дня. Систему контента на нейросетях собираем на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Промпты + методичка — в комментариях</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru · Бриф → @alovlab</span>
  </div>
</section>""")

html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(P)}</body></html>"
OUT.write_text(html, encoding="utf-8")
kb = len(html.encode("utf-8"))//1024
print(f"HTML: {OUT} {kb} KB | pages: {len(P)}")
