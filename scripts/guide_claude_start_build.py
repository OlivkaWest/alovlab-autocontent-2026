# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 1 (28.08) «Первый запуск Claude Code» — премиум-PDF (фикс-A4).
Лид-магнит DISCOVERY: от чёрного экрана до первого результата без кода. Метод «пишешь задачу, не код».
Полная дорожная карта: установка → первый промпт → 5 первых задач (каждая с промптом) → как говорить →
если пошло не так → чек-лист. Честность: реальные возможности Claude Code, актуальные шаги — в доке.
База CSS — v2. Запуск: python3 scripts/guide_claude_start_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "claude-start"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-claude-start.html"

EXTRA = r"""
.rec{display:grid;grid-template-columns:24px 1fr;gap:12px;margin:9px 0;align-items:start}
.rec .n{width:24px;height:24px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.44;color:var(--body)}
.prompt code{font-size:8.8pt;line-height:1.52}
.act{margin:9px 0 2px}
.act .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:6px 0;align-items:start}
.act .s .k{width:20px;height:20px;border-radius:6px;background:#ece0cc;color:#8a6127;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;line-height:1;margin-top:1px}
.act .s p{font-size:9.5pt;line-height:1.42;color:var(--body)}.act .s p b{color:var(--ink);font-weight:800}.act .s p em{font-style:normal;color:var(--o);font-weight:700}
.actlbl{display:block;font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin:6px 0 2px}
.term{display:grid;grid-template-columns:auto 1fr;gap:9px;align-items:baseline;background:#fff;border:1px solid var(--line);border-left:3px solid var(--o2);border-radius:10px;padding:9px 13px;margin:8px 0}
.term b{font-weight:800;color:var(--ink);font-size:10pt}.term span{font-size:9.5pt;line-height:1.42;color:var(--body)}
.qa{margin:8px 0}
.qa .r{background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 13px;margin:7px 0}
.qa .r .p{font-weight:800;color:var(--ink);font-size:9.7pt;margin-bottom:4px}
.qa .r .p i{color:#c56b43;font-style:normal}
.qa .r .s{font-size:9.5pt;line-height:1.45;color:var(--body)}
.qa .r .s b{color:var(--o);font-weight:700}
.road{margin:9px 0}
.road .r{display:grid;grid-template-columns:26px 1fr auto;gap:12px;align-items:center;padding:9px 0;border-bottom:1px solid var(--line)}
.road .r:last-child{border-bottom:0}
.road .r .n{width:26px;height:26px;border-radius:8px;background:#13100a;color:var(--o2);font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center}
.road .r b{font-weight:800;color:var(--ink);font-size:10.3pt}.road .r p{font-size:9pt;color:var(--muted);margin-top:1px}
.road .r .pg{font-size:8.5pt;font-weight:700;color:var(--faint);letter-spacing:.04em}
.mono{font-family:'DejaVu Sans Mono',ui-monospace,monospace;background:#13100a;color:#eee;border-radius:8px;padding:3px 8px;font-size:9pt;font-weight:700}
.mono i{color:#57d07a;font-style:normal}
"""
CSS = V2CSS + EXTRA
VOICE = "[ГОЛОС] простым языком, без терминов."

def page(section, num, inner):
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main">{inner}</div>'
            f'<div class="pf"><span>AlovLab · первый запуск Claude Code</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')
def head(kick,h2,lead=None):
    l=f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def rec(n,t,b): return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{t}</b><p>{b}</p></div></div>'
def act(lbl,steps): return f'<span class="actlbl">{lbl}</span><div class="act">'+''.join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i,t in enumerate(steps,1))+'</div>'
def prompt(tag,code,ru=None):
    ru_html=f'<div class="ru"><b>Подсказка:</b> {ru}</div>' if ru else ''
    return f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span><span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>'
def qa(items):
    return '<div class="qa">'+''.join(f'<div class="r"><div class="p"><i>«{p}»</i></div><div class="s">{s}</div></div>' for p,s in items)+'</div>'
def road(items):
    return '<div class="road">'+''.join(f'<div class="r"><div class="n">{n}</div><div><b>{t}</b><p>{d}</p></div><div class="pg">{pg}</div></div>' for n,t,d,pg in items)+'</div>'
def taskpage(section,num,kick,h2,lead,steps,ptag,pcode,phint):
    return page(section,num, head(kick,h2,lead)+act("Что делаешь",steps)+prompt(ptag,pcode,phint))

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 1</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:16ch">Первый запуск <span style="color:var(--o2)">Claude&nbsp;Code.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:46ch">От чёрного экрана до первого результата — без единой строчки кода. Ты не пишешь код, ты объясняешь задачу словами. Установка, первый запрос и 5 первых задач с готовыми промптами.</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Дорожная карта</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">6 промптов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Для новичка</span>
    </div>
  </div>
</section>""")

# 02 Что внутри
P.append(page("Что внутри",2,
  head("Тетрадь под карусель «5 вещей без кода»","Чёрный экран — не для программистов",
    "Claude Code выглядит страшно: чёрное окно, курсор. Кажется, тут нужно уметь программировать. Не нужно. Ты пишешь словами, что тебе нужно, — а он делает работу по шагам и спрашивает разрешение.")
  + '<div class="term"><b>Claude&nbsp;Code</b><span>помощник, который живёт в окне-терминале и умеет сам делать задачи на компьютере: собрать документ, навести порядок в файлах, сделать страницу.</span></div>'
  + '<div class="term"><b>Терминал</b><span>то самое чёрное окно. Раньше туда писали команды. Теперь ты пишешь обычными словами.</span></div>'
  + '<div class="callout result"><div class="h">Что на выходе</div><p>Ты поставишь Claude Code, сделаешь первый запуск и доведёшь до готового файла хотя бы одну из пяти задач. И заберёшь промпты, чтобы повторять.</p></div>'
))

# 03 Как это работает
P.append(page("Как это работает",3,
  head("Один принцип","Ты не пишешь код — ты пишешь задачу",
    "Порог входа не «выучи программирование», а «сформулируй задачу». Дальше всё идёт по одной понятной цепочке — и на каждом шаге решаешь ты.")
  + '<div class="formula" style="display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin:10px 0">'
    '<span style="font-weight:800;font-size:10pt;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:9px;padding:8px 12px">Задача словами</span>'
    '<b style="color:var(--o2);font-size:12pt">→</b>'
    '<span style="font-weight:800;font-size:10pt;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:9px;padding:8px 12px">Он предлагает план</span>'
    '<b style="color:var(--o2);font-size:12pt">→</b>'
    '<span style="font-weight:800;font-size:10pt;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:9px;padding:8px 12px">Делает шаг</span>'
    '<b style="color:var(--o2);font-size:12pt">→</b>'
    '<span style="font-weight:800;font-size:10pt;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:9px;padding:8px 12px">Спрашивает тебя</span>'
    '<b style="color:var(--o2);font-size:12pt">→</b>'
    '<span style="font-weight:800;font-size:10pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:9px;padding:8px 12px">Результат</span></div>'
  + '<span class="kick" style="display:block;margin-top:12px">3 правила спокойного новичка</span>'
  + rec(1,"Проси план первым","Пусть сначала скажет, что собирается делать. Так ты видишь, понял ли он.")
  + rec(2,"Разрешай по шагу","Не давай менять всё сразу. Одно действие — одно твоё «да».")
  + rec(3,"Ничего не бойся","Он спрашивает перед изменениями. Работай в отдельной папке — всё видно и можно отменить.")
))

# 04 Установка
P.append(page("Установка",4,
  head("Поставить один раз","Как включить Claude Code",
    "Займёт несколько минут. Если какой-то шаг выглядит иначе — это нормально, инструменты обновляются: сверься с официальной инструкцией, ссылка внизу.")
  + act("Шаги",[
      "Заведи аккаунт Anthropic и подписку (claude.ai).",
      "Поставь Node.js (это «движок», нужен один раз) — с сайта nodejs.org, версия LTS.",
      "Открой терминал и вставь команду установки (справа).",
      "Набери <b>claude</b> и войди в свой аккаунт — откроется то самое окно.",
      "Готово. Дальше — только слова."])
  + '<div style="margin:6px 0 2px"><span class="mono"><i>npm</i> install -g @anthropic-ai/claude-code</span></div>'
  + '<div style="margin:8px 0 2px"><span class="mono"><i>claude</i></span> <span style="font-size:9pt;color:var(--muted)">— запуск</span></div>'
  + '<p class="note">Актуальные шаги для твоей системы (Windows / Mac) — в официальной доке: <b>code.claude.com/docs</b>. Там же — как работать в браузере, если не хочешь ставить на компьютер.</p>'
))

# 05 Первый запуск — промпт 0
P.append(page("Первый запуск",5,
  head("Промпт №0 · настрой помощника","Первое, что ты напишешь",
    "Не бросайся сразу задачей. Сначала настрой помощника под себя — задай правила. Вставь этот промпт первым, и дальше он будет вести себя спокойно и по шагам.")
  + prompt("Промпт · вставь первым",
    "Ты — мой помощник в Claude Code. Я не программист.\n"
    "Отвечай простым языком, без терминов.\n"
    "Правила работы:\n"
    "1) на любую мою задачу сначала предложи короткий план шагами;\n"
    "2) делай по одному шагу;\n"
    "3) перед изменением файлов спрашивай подтверждение;\n"
    "4) не понял — задай вопрос, не угадывай.\n"
    "Готов? Жди мою первую задачу.\n" + VOICE,
    "этот промпт делает всю дальнейшую работу безопасной. Сохрани его — он твой стартовый.")
))

# 06 Дорожная карта
P.append(page("Дорожная карта",6,
  head("5 первых задач","С чего начать — по возрастанию",
    "Не пытайся сделать всё сразу. Пройди задачи по порядку — от самой простой. Каждая — на своей странице с готовым промптом.")
  + road([
      ("1","Текст → аккуратный документ","самое простое: превратить свалку текста в файл","стр. 07"),
      ("2","Порядок в файлах","разложить и переименовать за тебя","стр. 08"),
      ("3","Простая страница","одностраничник из твоего текста","стр. 09"),
      ("4","Данные → таблица и вывод","свести цифры и объяснить их","стр. 10"),
      ("5","Повторяемое → одна команда","научить делать одинаково каждый раз","стр. 11"),
    ])
  + '<p class="note">Сделал одну до готового файла — уже победа. Остальные добьёшь в своём темпе.</p>'
))

# 07-11 · задачи
P.append(taskpage("Задача 1 · документ",7,"Самое простое","Куча текста → аккуратный документ",
  "Есть заметки, куски, голосом надиктованное — и надо это в нормальный вид: прайс, коммерческое, инструкцию.",
  ["Скопируй свой сырой текст.","Вставь промпт и текст в Claude Code.","Посмотри план → скажи «да».","Открой готовый файл, попроси поправить, что не так."],
  "Промпт · документ",
  "Вот сырой текст: [ВСТАВЬ ТЕКСТ].\n"
  "Собери из него аккуратный документ: заголовок, разделы, списки.\n"
  "Сохрани файлом. Сначала покажи план, потом собери.\n"
  "Спроси подтверждение перед сохранением.\n" + VOICE,
  "не диктуй формат — скажи, для чего документ (прайс, КП), и дай ему собрать."))

P.append(taskpage("Задача 2 · файлы",8,"Порядок","Наведи порядок в файлах — сам",
  "Папка, где сто файлов с именами «финал», «финал2», «новое_точно». Пусть разберёт и разложит.",
  ["Положи файлы в одну папку, запусти там Claude Code.","Вставь промпт.","Прочитай предложенный план — что куда.","Скажи «да» только когда согласен. Ничего не двигает без тебя."],
  "Промпт · порядок",
  "В этой папке беспорядок. Посмотри, что за файлы,\n"
  "и предложи, как разложить по папкам и переименовать понятно.\n"
  "Сначала покажи план — что куда. Ничего не двигай без моего «да».\n" + VOICE,
  "делай это на копии папки, пока не привыкнешь. Так спокойнее."))

P.append(taskpage("Задача 3 · страница",9,"Из текста","Простая страница из твоего текста",
  "Нужен простой одностраничник: визитка, страница-оффер, приглашение. Без дизайнера и конструктора.",
  ["Подготовь текст: заголовок, пара абзацев, кнопка.","Вставь промпт с текстом.","Попроси показать, как выглядит.","Скажи, что поменять — цвет, размер, порядок блоков."],
  "Промпт · страница",
  "Сделай простую одностраничную HTML-страницу по тексту:\n"
  "[ВСТАВЬ]. Нужно: заголовок, 2–3 блока, кнопка «написать мне».\n"
  "Тёмный фон, аккуратно, читаемо. Покажи, как выглядит.\n" + VOICE,
  "не знаешь слов — не надо. Опиши словами «хочу как визитка, спокойно и дорого»."))

P.append(taskpage("Задача 4 · таблица",10,"Данные","Сырые данные → таблица и вывод",
  "Есть список заказов, расходов, клиентов — вперемешку. Нужна таблица и понятный вывод, а не каша.",
  ["Собери данные в одном месте (текст или файл).","Вставь промпт.","Получи таблицу + короткие выводы.","Попроси сохранить таблицу файлом."],
  "Промпт · таблица",
  "Вот данные: [ВСТАВЬ или укажи файл].\n"
  "Сведи их в таблицу, посчитай итоги и напиши 3 вывода\n"
  "простыми словами: что работает, а что нет.\n"
  "Сначала план, потом делай. Сохрани таблицу файлом.\n" + VOICE,
  "проси именно «выводы простыми словами» — иначе получишь просто числа."))

P.append(taskpage("Задача 5 · повтор",11,"Автоматизация","Один раз объяснил — делает всегда",
  "Задачу, которую делаешь часто (одинаковый отчёт, оформление поста), можно один раз объяснить — и повторять одним словом. Это мостик к скиллам (День 3).",
  ["Выбери задачу, которую повторяешь.","Пройди её с Claude Code один раз.","Попроси сохранить шаги как инструкцию.","В следующий раз просто назови её — он повторит."],
  "Промпт · повтор",
  "Задачу [КАКУЮ] я делаю часто и хочу, чтобы ты выполнял\n"
  "её одинаково. Опиши шаги, которые ты сделал, и сохрани их\n"
  "как инструкцию, чтобы в следующий раз я сказал одно слово —\n"
  "а ты повторил всё по ней.\n" + VOICE,
  "это и есть «конвейер»: не одна генерация, а повторяемый результат. Разберём глубже в Дне 3."))

# 12 Как говорить
P.append(page("Как говорить",12,
  head("Техника формулировки","5 приёмов, чтобы он понимал с первого раза",
    "Claude Code делает ровно то, что ты попросил. Значит, всё решает, как ты просишь. Пять простых приёмов.")
  + rec(1,"Говори задачу, а не решение","«Нужен прайс из этого текста» лучше, чем «сделай таблицу 3 на 5». Пусть думает как.")
  + rec(2,"Дай контекст","Для кого, зачем, в каком виде на выходе. Чем понятнее цель — тем точнее результат.")
  + rec(3,"Проси план первым","«Сначала план, потом делай». Увидишь, туда ли он пошёл, до того как что-то менять.")
  + rec(4,"Одна задача за раз","Не вали пять дел в один запрос. По одному — чище и понятнее.")
  + rec(5,"Не понял — переспроси","«Объясни проще» или «покажи пример». Это нормально и не стыдно.")
))

# 13 Если пошло не так
P.append(page("Если пошло не так",13,
  head("Спокойно","Частые затыки — и что сказать",
    "Ничего не ломается насовсем. Почти всё чинится одной фразой. Вот шпаргалка.")
  + qa([
     ("Сделал не то","<b>Скажи:</b> «Стоп. Ты понял задачу как X, а мне нужно Y. Переделай этот шаг.»"),
     ("Слишком много непонятных слов","<b>Скажи:</b> «Объясни простым языком, без терминов, как для новичка.»"),
     ("Полез менять файлы сам","<b>Напомни правило:</b> «Спрашивай подтверждение перед изменением файлов.»"),
     ("Большой запутанный ответ","<b>Скажи:</b> «Разбей на маленькие шаги и делай по одному.»"),
     ("Боюсь что-то испортить","<b>Приём:</b> работай в отдельной папке или на копии. Изменения видно, и их можно отменить."),
    ])
))

# 14 Проверь себя
P.append(page("Проверь себя",14,
  head("Ориентир","Что должно получиться")
  + '<div class="callout result"><div class="h">Хороший первый день</div><p>Ты поставил Claude Code, настроил помощника промптом №0 и довёл до готового файла хотя бы одну задачу из пяти. Файл лежит у тебя, ты знаешь, как попросить поправить.</p></div>'
  + '<div class="callout" style="margin-top:10px"><div class="h">Если застрял на установке</div><p>Это самый частый стоп. Не мучайся в одиночку: открой code.claude.com/docs, а вопросы задавай прямо Claude — он проведёт по шагам под твою систему.</p></div>'
  + '<p class="note">Цель дня — не стать программистом. Цель — один раз получить результат словами и понять: так можно.</p>'
))

# 15 Чек-лист
P.append(page("Чек-лист · первый запуск",15,
  head("Контроль","Отметь, что сделал")
  + '<div class="callout check"><div class="h">Чек-лист «первый запуск»</div>'
    '<div class="row">Поставил Claude Code и запустил <b>claude</b></div>'
    '<div class="row">Вставил первым промпт №0 (правила: план → шаг → подтверждение)</div>'
    '<div class="row">Прошёл хотя бы 1 задачу из 5 до готового файла</div>'
    '<div class="row">Просил план до того, как он что-то менял</div>'
    '<div class="row">Подтверждал по шагу, не разрешал менять всё сразу</div>'
    '<div class="row">Сохранил себе рабочие промпты</div>'
    '<div class="row">Понял главное: пишешь задачу, а не код</div>'
    '</div>'
  + '<p class="note">Отметил хотя бы первые три — первый запуск состоялся. Остальное придёт с практикой.</p>'
))

# 16 CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:25pt;line-height:1.12;margin:18px 0 8px">Пишешь задачу —<br><span style="color:var(--o2)">получаешь результат.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Это только первый запуск. Как собирать результат стабильно — конвейером, а не с одной удачной попытки — учим на курсе AlovLab «Нейросети и ChatGPT для каждого».</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Промпты — в комментариях под постом</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Первый запуск Claude Code · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
