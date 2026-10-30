# -*- coding: utf-8 -*-
"""AlovLab · обширная методичка «Команды для ChatGPT: контент как система» (премиум-PDF, фикс-A4).
Библиотека команд-промптов: базовый профиль + ~17 команд по блокам (стратегия/идеи/производство/улучшение/продажи),
конвейер, честность, ошибки, action+check, мост в курс, путь в команду, шпаргалка. По GLOBAL-METHODOLOGY-RULE.
Запуск: python3 scripts/guide_chatgpt_commands_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "chatgpt-system"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-chatgpt-commands.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.midwrap{width:100%}
.cmd{margin:11px 0}
.cmd .h{display:flex;align-items:baseline;gap:10px;margin-bottom:3px}
.cmd .h .n{font-family:ui-monospace,Menlo,monospace;font-weight:800;font-size:12.5pt;color:var(--o)}
.cmd .h .d{font-size:9.5pt;color:var(--muted);line-height:1.3}
.pc{background:var(--dark);border-radius:12px;padding:11px 14px;margin:5px 0 0;color:#ffd9b8}
.pc code{display:block;font-family:'SF Mono',ui-monospace,Menlo,monospace;font-size:8.6pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap}
.pc .cp{font-weight:700;font-size:7pt;letter-spacing:.1em;text-transform:uppercase;color:#cbb39d;float:right}
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:9px 12px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.1pt;line-height:1.38;color:var(--ink);margin-top:3px;max-width:none}
.blocklbl{font-weight:800;font-size:8.5pt;letter-spacing:.12em;text-transform:uppercase;color:var(--o);margin:2px 0 8px}
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
.sheet{columns:2;column-gap:22px;margin:8px 0}
.sheet .r{break-inside:avoid;margin:5px 0;font-size:9pt;line-height:1.35}
.sheet .r b{font-family:ui-monospace,Menlo,monospace;color:var(--o);font-weight:800}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · команды для ChatGPT</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def cmd(name, desc, prompt):
    return (f'<div class="cmd"><div class="h"><span class="n">{name}</span><span class="d">{desc}</span></div>'
            f'<div class="pc"><span class="cp">скопировать</span><code>{prompt}</code></div></div>')

def cmdpage(section, num, blocklbl, lead, cmds):
    inner = head("Библиотека команд", blocklbl, lead) + '<div class="blocklbl" style="display:none"></div>' + "".join(cmds)
    return page(section, num, inner)

P = []

# 01 Cover
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:absolute;right:8%;top:24%;width:50%;color:#ffb98a;font-family:ui-monospace,monospace;font-size:11pt;line-height:1.8">/audiencemap<br>/contentmix<br>/leadidea<br>/funnelmap<br><span style="color:var(--o2)">/…ещё 13</span></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · полный урок</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:16ch">Команды для ChatGPT: контент как система</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">17 готовых команд-промптов: аудитория, идеи, производство, улучшение, продажи. Плюс как связать их в один конвейер.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">17 команд</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Конвейер</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Шпаргалка</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("01","Что ты получишь","03"),("02","Принцип: контекст + команда","04"),("03","Команда /profile","05"),
 ("04","Как пользоваться","06"),("05","Блок 1 · Стратегия","07"),("06","Блок 1 · Стратегия","08"),
 ("07","Блок 2 · Идеи","09"),("08","Блок 3 · Производство","10"),("09","Блок 3 · Производство","11"),
 ("10","Блок 4 · Улучшение","12"),("11","Блок 5 · Продажи","13"),
 ("12","Конвейер из команд","14"),("13","Честно: контекст решает","15"),("14","Ошибки и фиксы","16"),
 ("15","Сделай сейчас + проверка","17"),("16","Шпаргалка всех команд","18"),
 ("17","Дальше — на курсе","19"),("18","Путь в команду AlovLab","20"),("19","Контакты","21"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:10px;padding:6px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:9.5pt;width:24px">{a}</span>'
               f'<span style="font-weight:600;font-size:10.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:9.5pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Маршрут урока</h1>'
    '<p class="lead">Базовый профиль, 17 команд по пяти блокам, сборка в конвейер и шпаргалка на одной странице.</p>'
    f'<div style="margin-top:4px">{rows}</div>'))

# 03 result
P.append(page("Шаг 01 · Результат", 3,
    head("Шаг 01", "Что ты получишь", "Не десять случайных промптов, а библиотеку команд: короткое слово вместо длинного запроса, и ChatGPT делает конкретную работу.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Как это</div><div class="ch">Профиль + команда</div><p>Один раз грузишь контекст, дальше зовёшь команду одним словом.</p></div>'
      '<div class="card"><div class="ct">Сколько</div><div class="ch">17 команд</div><p>Аудитория, идеи, производство, улучшение, продажи.</p></div>'
      '<div class="card"><div class="ct">Бонус</div><div class="ch">Конвейер</div><p>Как связать команды в одну систему от идеи до заявки.</p></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>Ты перестаёшь каждый раз объяснять ChatGPT с нуля. Загрузил профиль, и любая задача решается одной командой: карта аудитории, план, сценарий рилса, оффер, воронка.</p></div>'))

# 04 principle
P.append(page("Шаг 02 · Принцип", 4,
    head("Шаг 02", "Принцип: контекст + команда", "Слабый результат не от того, что модель тупая. От того, что она не знает контекста.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Как НЕ надо</div>«Напиши пост.» «Дай 30 идей для Reels.» «Составь контент-план.»<br><br>Без контекста ChatGPT угадывает и выдаёт воду.</div>'
      '<div class="box good"><div class="lbl">Как надо</div>Сначала загружаешь <b>профиль</b> (кто ты, продукт, аудитория, цель). Потом запускаешь конкретную задачу <b>командой</b>.</div></div>'
    + '<p>Все команды ниже работают только после того, как ChatGPT знает контекст. Поэтому начинаем с команды /profile — её грузишь один раз в начале диалога.</p>'
    + '<div class="term"><b>Важно.</b> <span>Команды это не магические слова из системы ChatGPT. Это твои готовые промпты под коротким именем. ChatGPT понимает их, потому что ты один раз объяснил профиль и договорился о формате.</span></div>'))

# 05 /profile
P.append(page("Шаг 03 · Профиль", 5,
    head("Шаг 03", "Команда /profile", "Грузишь один раз в начале диалога. Дальше все команды опираются на неё.")
    + cmd("/profile", "базовый контекст о тебе и продукте",
          "Ты мой контент-стратег и копирайтер. Контекст: продукт [ЧТО ПРОДАЮ], аудитория [КТО, возраст, боль], площадки [IG/TG/VK], мой голос [КАК ЗВУЧУ], цель [ЧТО ХОЧУ]. Запомни это и учитывай во всех ответах. Дальше я буду давать короткие команды вида /имя. Если данных не хватает, задай мне вопрос, не выдумывай.")
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Свой продукт, аудиторию с болью, площадки, тон голоса, цель.</p></div>'
      '<div class="c out"><b>Что получить</b><p>ChatGPT запоминает контекст. Дальше команды работают точно, без объяснений каждый раз.</p></div></div>'
    + '<p class="note">В ChatGPT это удобно держать в «Проектах» или в кастомных инструкциях, чтобы профиль не терялся между диалогами.</p>'))

# 06 how to use
P.append(page("Шаг 04 · Как пользоваться", 6,
    head("Шаг 04", "Как пользоваться командами", "Один порядок для всех 17 команд.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Загрузи /profile</b> в начале диалога (или держи в Проекте ChatGPT).</div></div>'
      '<div class="step"><div class="sx"><b>Скопируй нужную команду</b> из библиотеки ниже.</div></div>'
      '<div class="step"><div class="sx"><b>Подставь слова в [СКОБКАХ]</b> под свою задачу.</div></div>'
      '<div class="step"><div class="sx"><b>Отправь.</b> Не понравилось — уточни одной фразой, ChatGPT доработает.</div></div>'
      '<div class="step"><div class="sx"><b>Сохраняй удачное</b> в свою мини-библиотеку команд.</div></div></div>'
    + '<div class="callout check"><div class="h">Правило</div>'
      '<div class="row">Одна команда = одна задача. Не мешай пять задач в одном запросе.</div>'
      '<div class="row">Факты и цифры из ответа проверяй сам. Команда усиливает, но не заменяет правду.</div></div>'))

# 07 block1 strategy (audiencemap, leadidea)
P.append(cmdpage("Блок 1 · Стратегия", 7, "Блок 1 · Стратегия и аудитория",
    "С чего начинается система: понять аудиторию и выстроить путь к заявке.",
    [cmd("/audiencemap","карта аудитории: что ей реально нужно",
        "Составь карту моей аудитории по блокам: проблемы, желания, вопросы, возражения, ситуации. По 5 пунктов в каждом, живым языком клиентов, а не маркетинговым. Вводные и материалы: [ОПИСАНИЕ АУДИТОРИИ + КОММЕНТАРИИ/ВОПРОСЫ/ПЕРЕПИСКИ]."),
     cmd("/leadidea","проблема аудитории → идея лид-магнита",
        "Возьми одну проблему или желание аудитории: [ВСТАВЬ]. Предложи 5 идей лид-магнита: мини-урок, чек-лист, инструкция, разбор, шаблон. Для каждого дай название и что внутри. Это должен быть логичный следующий шаг после моего контента.")]))

# 08 block1 (funnelmap + calendar bridge) -> put funnelmap here
P.append(cmdpage("Блок 1 · Стратегия", 8, "Блок 1 · Стратегия и аудитория",
    "Путь человека от просмотра до заявки и план на период.",
    [cmd("/funnelmap","воронка: от просмотра до заявки",
        "Собери структуру воронки: контент → подписка → лид-магнит → прогрев → заявка/продажа. Моя ситуация: продаю [ЧТО], лид-магнит [КАКОЙ], веду [ГДЕ], хочу переводить людей в [КУДА]. Для каждого этапа опиши, что я делаю и зачем, и где теряются люди."),
     cmd("/calendar","контент-план на период",
        "Собери контент-план на [НЕДЕЛЮ/МЕСЯЦ] под мою нишу: дата, формат, рубрика, тема, черновик хука. Держи пропорцию: польза, смысл/позиция, кейс, приглашение. Без повторов тем, с опорой на карту аудитории.")]))

# 09 block2 ideas (contentmix, hooks)
P.append(cmdpage("Блок 2 · Идеи", 9, "Блок 2 · Идеи и форматы",
    "Как из одной мысли получить много контента и сильные заходы.",
    [cmd("/contentmix","одна мысль → несколько единиц контента",
        "Возьми мысль, тему или мой старый пост: [ВСТАВЬ]. Разложи на форматы: Reels, карусель, пост, Telegram. Для каждого дай 3 варианта с разными хуками и углами под мою аудиторию. Коротко и конкретно."),
     cmd("/hooks","10 сильных хуков на тему",
        "Дай 10 сильных хуков на тему [ТЕМА]: типы — ошибка, разрушение мифа, конфликт, конкретный результат, вопрос новичка, до/после. Только первая строка, которая цепляет, без разгона и без приветствий.")]))

# 10 block3 production (reels, carousel)
P.append(cmdpage("Блок 3 · Производство", 10, "Блок 3 · Производство",
    "Готовые скелеты контента под твою тему.",
    [cmd("/reels","сценарий рилса по секундам",
        "Напиши сценарий Reels на тему [ТЕМА]: хук 0–2 сек, проблема, один приём (показать, а не рассказать), результат, CTA одной строкой. Двумя колонками: что говорю за кадром и что в кадре. Живая речь, без канцелярита."),
     cmd("/carousel","структура карусели",
        "Собери структуру карусели на тему [ТЕМА], 6–7 слайдов: обложка-хук, провокация, 3–4 слайда пользы (одна мысль на слайд), финал + CTA. Для каждого слайда дай заголовок и текст. Одна мысль на слайд, без воды.")]))

# 11 block3 production (post, caption)
P.append(cmdpage("Блок 3 · Производство", 11, "Блок 3 · Производство",
    "Тексты в ленту и подписи.",
    [cmd("/post","пост для ленты",
        "Напиши пост на тему [ТЕМА] для [IG/TG/VK]: хук в первой строке, одна сильная мысль, пример из практики, как применить сегодня, естественный CTA. Живой язык, 800–1200 знаков, без штампов."),
     cmd("/caption","описание + хэштеги",
        "Напиши короткое описание к [посту/рилсу] на тему [ТЕМА]: хук первой строкой, одна мысль, CTA одной строкой. Плюс 10 релевантных хэштегов. Без воды и без пересказа контента.")]))

# 12 block4 improve (rewrite, stronger, check, shorten)
P.append(cmdpage("Блок 4 · Улучшение", 12, "Блок 4 · Улучшение текста",
    "Доводка того, что уже написано.",
    [cmd("/rewrite","перепиши живым языком",
        "Перепиши этот текст живым языком, короткими фразами, без канцелярита и штампов: [ВСТАВЬ]. Сохрани смысл, усиль первую строку."),
     cmd("/stronger","усиль хук",
        "Усиль хук и первую строку этого текста: [ВСТАВЬ]. Дай 3 варианта, каждый цепляет с первого слова."),
     cmd("/check","проверь на воду и штампы",
        "Проверь текст на воду, штампы и канцелярит: [ВСТАВЬ]. Покажи слабые места и предложи, что убрать или переписать."),
     cmd("/shorten","сократи вдвое",
        "Сократи текст вдвое без потери смысла и силы: [ВСТАВЬ]. Оставь только то, что работает.")]))

# 13 block5 sales (offer, warmup, objections)
P.append(cmdpage("Блок 5 · Продажи", 13, "Блок 5 · Продажи и прогрев",
    "Как контент превращается в заявки.",
    [cmd("/offer","собери оффер",
        "Собери оффер на [ПРОДУКТ] для [АУДИТОРИЯ]: результат, для кого, что внутри, почему сейчас, следующий шаг. Без давления и штампов, живым языком."),
     cmd("/warmup","серия прогрева",
        "Собери серию прогрева из 5 сообщений в Telegram к [ПРОДУКТ]: боль, как устроено, кейс или пример, ответы на возражения, предложение + шаг. Каждое сообщение короткое и с одной мыслью."),
     cmd("/objections","ответы на возражения",
        "Дай ответы на 5 главных возражений по [ПРОДУКТ] (дорого, нет времени, не получится, уже пробовал, не для меня). По формуле: признай → назови страх → покажи результат → дай маленький шаг.")]))

# 14 conveyor
P.append(page("Шаг 05 · Конвейер", 14,
    head("Шаг 05", "Собери команды в конвейер", "По одной команде это удобно. Вместе это система от идеи до заявки.")
    + '<div class="flow" style="flex-wrap:wrap">'
      '<div class="node"><b>/audiencemap</b><span>кого</span></div><div class="arr">→</div>'
      '<div class="node"><b>/leadidea</b><span>что дать</span></div><div class="arr">→</div>'
      '<div class="node"><b>/calendar</b><span>план</span></div><div class="arr">→</div>'
      '<div class="node"><b>/contentmix</b><span>форматы</span></div></div>'
    + '<div class="flow" style="flex-wrap:wrap">'
      '<div class="node"><b>/reels /post</b><span>производство</span></div><div class="arr">→</div>'
      '<div class="node"><b>/rewrite /check</b><span>доводка</span></div><div class="arr">→</div>'
      '<div class="node"><b>/funnelmap</b><span>путь</span></div><div class="arr">→</div>'
      '<div class="node"><b>/warmup /offer</b><span>заявка</span></div></div>'
    + '<p>Слева направо: понял аудиторию, придумал лид-магнит, собрал план, размножил идеи в форматы, произвёл, довёл текст, выстроил воронку и прогрел до заявки. Каждый шаг это одна команда.</p>'
    + '<div class="callout result"><div class="h">Итог</div><p>Контент перестаёт существовать отдельно от продаж. Это и есть система, а не разовые посты.</p></div>'))

# 15 honest
P.append(page("Шаг 06 · Честность", 15,
    head("Шаг 06", "Честно: контекст решает", "Команды усиливают то, что ты в них кладёшь. Не больше.")
    + '<div class="warn"><div class="h">Так не сработает</div><ul>'
      '<li>Пустой профиль — команды дадут общий, никакой результат.</li>'
      '<li>Слепо доверять цифрам и «кейсам» из ответа — проверяй.</li>'
      '<li>Публиковать сгенерённые отзывы и результаты, которых не было.</li></ul></div>'
    + '<div class="warn"><div class="h" style="color:#8fd08a">Так сработает</div><ul>'
      '<li class="ok">Заполни профиль честно и подробно.</li>'
      '<li class="ok">Проверяй факты, цифры и обещания перед публикацией.</li>'
      '<li class="ok">Дорабатывай команды под свою нишу, это не догма.</li></ul></div>'
    + '<p>ИИ это сильный инструмент. Он остаётся сильным, только пока за ним стоит твоя правда и твой вкус.</p>'))

# 16 errors
P.append(page("Шаг 07 · Ошибки", 16,
    head("Шаг 07", "Ошибки и фиксы", "Пять граблей при работе с командами.")
    + '<div class="fix">'
      '<div class="r"><b>Забыл профиль, команды дают воду.</b> Фикс: грузи /profile в начале или держи в Проекте ChatGPT.</div>'
      '<div class="r"><b>Смешал пять задач в одном запросе.</b> Фикс: одна команда = одна задача.</div>'
      '<div class="r"><b>Ответ слишком общий.</b> Фикс: добавь деталей в [СКОБКИ] и примеры.</div>'
      '<div class="r"><b>Текст звучит как ИИ.</b> Фикс: прогони через /rewrite и /check.</div>'
      '<div class="r"><b>Собрал один раз и забыл.</b> Фикс: сохрани рабочие команды в свою библиотеку.</div></div>'
    + '<p class="note">Как собрать команды под свою нишу и связать в конвейер под ключ — разбираем на курсе и в части 2 (в Telegram).</p>'))

# 17 action
P.append(page("Шаг 08 · Действие", 17,
    head("Шаг 08", "Сделай сейчас", "За 15 минут прогони первый мини-конвейер.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Загрузи /profile</b> под себя.</div></div>'
      '<div class="step"><div class="sx"><b>Запусти /audiencemap</b> и выбери одну проблему.</div></div>'
      '<div class="step"><div class="sx"><b>Прогони /leadidea и /contentmix</b> по этой проблеме.</div></div>'
      '<div class="step"><div class="sx"><b>Собери /reels или /post</b> и доведи через /rewrite.</div></div></div>'
    + '<div class="callout check"><div class="h">Проверь себя</div>'
      '<div class="row">Профиль загружен, команды опираются на него.</div>'
      '<div class="row">Каждая команда решала одну задачу.</div>'
      '<div class="row">Тексты живые, без штампов (прогнал /check).</div>'
      '<div class="row">Есть связка: аудитория → лид-магнит → контент.</div>'
      '<div class="row">Рабочие команды сохранил себе.</div></div>'))

# 18 cheatsheet
P.append(page("Шпаргалка", 18,
    head("Шпаргалка", "Все команды одной страницей", "Сохрани и держи под рукой. Сначала /profile, дальше по задаче.")
    + '<div class="sheet">'
      '<div class="r"><b>/profile</b> — базовый контекст</div>'
      '<div class="r"><b>/audiencemap</b> — карта аудитории</div>'
      '<div class="r"><b>/leadidea</b> — идея лид-магнита</div>'
      '<div class="r"><b>/funnelmap</b> — воронка до заявки</div>'
      '<div class="r"><b>/calendar</b> — контент-план</div>'
      '<div class="r"><b>/contentmix</b> — мысль в форматы</div>'
      '<div class="r"><b>/hooks</b> — 10 хуков</div>'
      '<div class="r"><b>/reels</b> — сценарий рилса</div>'
      '<div class="r"><b>/carousel</b> — структура карусели</div>'
      '<div class="r"><b>/post</b> — пост в ленту</div>'
      '<div class="r"><b>/caption</b> — описание + хэштеги</div>'
      '<div class="r"><b>/rewrite</b> — живой язык</div>'
      '<div class="r"><b>/stronger</b> — усилить хук</div>'
      '<div class="r"><b>/check</b> — проверить на воду</div>'
      '<div class="r"><b>/shorten</b> — сократить вдвое</div>'
      '<div class="r"><b>/offer</b> — собрать оффер</div>'
      '<div class="r"><b>/warmup</b> — серия прогрева</div>'
      '<div class="r"><b>/objections</b> — ответы на возражения</div></div>'
    + '<p class="note">Полные тексты команд — на страницах 05–13. Здесь только имена для быстрого доступа.</p>'))

# 19 course
P.append(page("Дальше", 19,
    head("Дальше", "Команды — это навык. А есть система", "Ты собрал библиотеку. На курсе собираешь конвейер под свою нишу, а не отдельные промпты.")
    + '<p>17 команд экономят часы. Но сила в системе: как собрать команды под себя, связать в конвейер, подключить картинки, видео и голос. Это курс «Нейросети и ChatGPT для каждого»: шесть «Земель» от текста до аватара.</p>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Свои команды</div><p>Как собрать промпт-систему под нишу, а не копировать чужое.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Конвейер</div><p>Текст, визуал, видео, голос как одна система.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Продажи</div><p>Как довести контент до заявок и клиентов.</p></div></div>'
    + '<p>Эти команды это вход. Дальше ты перестаёшь искать чужие промпты и строишь свою систему.</p>'))

# 20 team
P.append(page("Команда", 20,
    head("Путь дальше", "Путь в команду AlovLab", "Начало получаться и хочется делать это для брендов — есть куда расти.")
    + '<div class="team"><div class="h">Собираешь контент-системы уверенно?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты: строят контент-конвейеры, промпт-системы и ассистентов под задачи брендов, набивают портфолио на живых кейсах и растут рядом с командой.</p>'
      '<div class="dirs"><span>Контент-конвейеры</span><span>Промпт-системы</span><span>AI-ассистенты</span><span>Автоматизация</span></div>'
      '<p style="margin-top:8px">Это работа и практика, а не обещание трудоустройства. Но дорога открыта: покажи, что доводишь результат.</p></div>'
    + '<p>Бизнесу, которому нужна контент-система под ключ — это AlovLab Studio. Отправляешь бриф, сборку берём на себя.</p>'))

# 21 contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Автоконтент</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Отдай контент системе, а не одной задаче.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Все 17 команд и конвейер — в этой методичке. Забирай в Telegram. Нужна контент-система под бренд — отправь бриф в студию.</p>
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
