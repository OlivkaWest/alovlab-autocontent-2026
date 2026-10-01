# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 3 (30.08) «Собери свой Claude Skill» — премиум-PDF (фикс-A4).
Подробное создание скилла (имя/описание-триггер/инструкция) + правила + промпт-сборщик + отладка,
и 7 ГОТОВЫХ скиллов (карусель, reels-видео, пост, контент-план, разбор конкурента, возражения, лид-магнит).
Скиллы кодируют реальный движок AlovLab. Честность: без выдуманных цифр; структура SKILL.md реальная.
База CSS — v2. Запуск: python3 scripts/guide_claude_skills_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "claude-skills"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-claude-skills.html"

EXTRA = r"""
.rec{display:grid;grid-template-columns:24px 1fr;gap:12px;margin:9px 0;align-items:start}
.rec .n{width:24px;height:24px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.44;color:var(--body)}
.prompt code{font-size:8.6pt;line-height:1.5}
.act{margin:9px 0 2px}
.act .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:6px 0;align-items:start}
.act .s .k{width:20px;height:20px;border-radius:6px;background:#ece0cc;color:#8a6127;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;line-height:1;margin-top:1px}
.act .s p{font-size:9.5pt;line-height:1.42;color:var(--body)}.act .s p b{color:var(--ink);font-weight:800}.act .s p em{font-style:normal;color:var(--o);font-weight:700}
.actlbl{display:block;font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin:6px 0 2px}
.term{display:grid;grid-template-columns:auto 1fr;gap:9px;align-items:baseline;background:#fff;border:1px solid var(--line);border-left:3px solid var(--o2);border-radius:10px;padding:9px 13px;margin:8px 0}
.term b{font-weight:800;color:var(--ink);font-size:10pt}.term span{font-size:9.5pt;line-height:1.42;color:var(--body)}
.skmeta{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0 2px}
.skmeta .tag{font-size:8pt;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--o);background:var(--o-tint);border-radius:20px;padding:4px 11px}
.does{font-size:9.7pt;line-height:1.46;color:var(--body);margin:4px 0 2px}.does b{color:var(--ink);font-weight:800}
"""
CSS = V2CSS + EXTRA
VOICE = "[ГОЛОС] живо, коротко, без штампов."

def page(section, num, inner):
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main">{inner}</div>'
            f'<div class="pf"><span>AlovLab · собери свой Claude Skill</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')
def head(kick,h2,lead=None):
    l=f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def rec(n,t,b): return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{t}</b><p>{b}</p></div></div>'
def act(lbl,steps): return f'<span class="actlbl">{lbl}</span><div class="act">'+''.join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i,t in enumerate(steps,1))+'</div>'
def prompt(tag,code,ru=None):
    ru_html=f'<div class="ru"><b>Подсказка:</b> {ru}</div>' if ru else ''
    return f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span><span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>'
def skillpage(section,num,idx,name,does,md):
    inner=(f'<span class="kick">Готовый скилл {idx}/7</span><h2>{name}</h2>'
           f'<p class="does"><b>Что делает:</b> {does}</p>'
           + prompt("SKILL.md · скопировать в файл", md,
                    "положи в файл SKILL.md в папку скилла (см. стр. 16). Правь под свою нишу."))
    return page(section,num,inner)

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 3</div>
    <h1 style="font-weight:800;font-size:32pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:16ch">Собери свой <span style="color:var(--o2)">Claude&nbsp;Skill.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:46ch">Научи ИИ делать твою задачу одинаково — каждый раз. Подробно: как устроен скилл и как его собрать. Плюс 7 готовых скиллов под контент: карусель, reels, пост, план, разбор конкурента, возражения, лид-магнит.</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Как создать</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">7 готовых скиллов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Промпты внутри</span>
    </div>
  </div>
</section>""")

# 02 Что такое скилл
P.append(page("Что такое скилл",2,
  head("Основа","Скилл = форма для результата",
    "Скилл — это инструкция, которую ты пишешь один раз. Дальше Claude сам применяет её, когда задача подходит, и выдаёт одинаковый результат. Это конвейер, а не разовая генерация.")
  + '<div class="term"><b>SKILL.md</b><span>один файл, где живёт скилл: имя, когда включать и что делать.</span></div>'
  + '<div class="term"><b>Триггер</b><span>описание, по которому Claude понимает, что пора применить именно этот скилл.</span></div>'
  + '<div class="callout result"><div class="h">Что на выходе тетради</div><p>Ты поймёшь, как собрать любой скилл, и заберёшь 7 готовых — скопировал, подставил свою нишу, работает.</p></div>'
))

# 03 Анатомия
P.append(page("Анатомия",3,
  head("Три части","Из чего состоит SKILL.md",
    "Любой скилл — это три вещи в одном файле. Сверху — короткая «шапка» (имя и когда включать), ниже — инструкция.")
  + prompt("SKILL.md · каркас",
    "---\n"
    "name: имя-скилла\n"
    "description: Когда прошу [такую-то задачу] — про что скилл\n"
    "  и по каким запросам его применять.\n"
    "---\n"
    "# Что делать\n"
    "Пошаговая инструкция, как выполнять задачу одинаково:\n"
    "шаги, формат ответа, ограничения, пример вход → выход.\n",
    "«шапка» между --- — это имя и триггер; всё, что ниже, — инструкция для Claude.")
))

# 04 Часть 1 — имя
P.append(page("Часть 1 · имя",4,
  head("Как назвать","Имя — коротко и по задаче",
    "Имя не для красоты — по нему ты и Claude понимаете, за что отвечает скилл.")
  + rec(1,"Коротко, по делу","«карусель», «reels-сценарий», «разбор-конкурента». Не «супер-мега-ассистент».")
  + rec(2,"Одна задача — один скилл","Не пихай пять дел в один. Узкий скилл работает стабильнее.")
  + rec(3,"Латиницей, через дефис","name: alovlab-carousel. Так его удобно хранить и вызывать.")
  + '<p class="note">Хорошее имя = сразу ясно, когда его звать. Если название расплывчатое — скилл будет срабатывать не там.</p>'
))

# 05 Часть 2 — когда включать
P.append(page("Часть 2 · когда включать",5,
  head("Триггер","Описание — это когда включать",
    "Самая важная часть. По описанию Claude решает, применить скилл или нет. Пиши его как «когда прошу …».")
  + rec(1,"Начни с «Когда прошу…»","«Когда прошу собрать карусель, слайды, визуальный пост из нескольких слайдов».")
  + rec(2,"Перечисли синонимы запроса","Разные слова, которыми ты просишь то же самое. Больше попаданий.")
  + rec(3,"Ограничь область","Скажи, когда НЕ применять, если легко перепутать с другим скиллом.")
  + '<div class="callout"><div class="h">Пример триггера</div><p>description: Когда прошу сценарий рилс, короткого видео, reels, shorts или видео для охвата.</p></div>'
))

# 06 Часть 3 — что делать
P.append(page("Часть 3 · что делать",6,
  head("Инструкция","Что делать — по шагам",
    "Тело скилла. Опиши, как ты выполняешь задачу, чтобы результат был одинаковым каждый раз.")
  + rec(1,"Шаги по порядку","Разбей задачу на понятные шаги. Claude пройдёт по ним.")
  + rec(2,"Формат ответа","Скажи, в каком виде отдать результат: таблица, список, файл.")
  + rec(3,"Ограничения и тон","Что нельзя (штампы, выдуманные цифры), каким голосом писать.")
  + rec(4,"Пример вход → выход","Один короткий пример: что подаёшь и что ждёшь на выходе. Это резко повышает точность.")
))

# 07 Правила
P.append(page("Правила хорошего скилла",7,
  head("Чтобы срабатывал стабильно","7 правил")
  + rec(1,"Узкий, не универсальный","Один скилл — одна задача.")
  + rec(2,"Триггер конкретный","«Когда прошу…» + синонимы. Размытый триггер = мимо.")
  + rec(3,"Шаги, а не абзац","Списком, по порядку — так повторяемость выше.")
  + rec(4,"Есть пример вход→выход","Показать образец сильнее, чем описать.")
  + rec(5,"Зашей тон и запреты","Голос, стоп-слова, «без выдуманных цифр».")
  + rec(6,"Правь после теста","Сработал не так — уточни инструкцию, не переписывай с нуля.")
  + rec(7,"Честность внутри","Скилл не должен выдумывать факты. Нет данных — пусть пишет UNKNOWN.")
))

# 08 Промпт-сборщик
P.append(page("Собрать с Claude",8,
  head("Промпт","Claude соберёт скилл за тебя",
    "Не хочешь писать вручную — опиши задачу, и Claude соберёт SKILL.md по всем правилам.")
  + prompt("Промпт · сборщик скилла",
    "Помоги собрать Claude Skill под мою повторяемую задачу: [ОПИШИ].\n"
    "Сделай файл SKILL.md: 1) name — коротко; 2) description —\n"
    "«когда прошу …» с синонимами запроса; 3) инструкция шагами:\n"
    "что делать, формат ответа, ограничения, пример вход → выход.\n"
    "Ниша: [ТВОЯ]. Цель — одинаковый результат каждый раз.\n" + VOICE,
    "получишь готовый файл. Дальше — на отладку (стр. 9).")
))

# 09 Отладка
P.append(page("Отладка",9,
  head("Если срабатывает не так","Почини скилл за минуту",
    "Скилл дал не тот результат? Не переписывай всё — точечно уточни. Вот промпт-редактор.")
  + prompt("Промпт · отладка скилла",
    "Вот мой скилл: [ВСТАВЬ SKILL.md]. На запрос «[ЗАПРОС]»\n"
    "он сделал не то: [ЧТО НЕ ТАК]. Найди, какой части не хватает\n"
    "(триггер / шаги / формат / пример), и предложи точечную правку —\n"
    "минимально, не переписывая весь скилл.\n" + VOICE,
    "чаще всего проблема в триггере (срабатывает не там) или в отсутствии примера вход→выход.")
))

# 10-16 · 7 готовых скиллов
P.append(skillpage("Скилл · карусель",10,1,"Карусель AlovLab",
  "собирает премиум-карусель 6–8 слайдов по правилу «кинокадр + знание».",
  "---\n"
  "name: alovlab-carousel\n"
  "description: Когда прошу собрать карусель, слайды или визуальный\n"
  "  пост из нескольких слайдов.\n"
  "---\n"
  "# Карусель AlovLab\n"
  "Собери 6–8 слайдов. Правило «кинокадр + знание»: дай метод/формулу,\n"
  "технику, save-слайд и рабочий промпт.\n"
  "Порядок: 1 обложка-хук - 2 проблема - 3 метод - 4-5 разбор -\n"
  "6 save-слайд - 7 пример - 8 CTA «в комментариях под постом».\n"
  "Голос: живой, короткие фразы, без штампов. Тёмный графит + янтарь.\n"
  "По каждому слайду: SLIDE / HEADLINE / что в кадре / подпись.\n"
  "Честность: без выдуманных цифр и кейсов.\n"))

P.append(skillpage("Скилл · reels",11,2,"Reels / видео AlovLab",
  "собирает сценарий короткого видео 9:16 по секундам, с разметкой сцен.",
  "---\n"
  "name: alovlab-reels\n"
  "description: Когда прошу сценарий рилс, короткого видео, reels,\n"
  "  shorts или видео для охвата.\n"
  "---\n"
  "# Reels AlovLab (по секундам)\n"
  "Сценарий 9:16, ~30-35 сек. Скелет: 0-2 хук - 2-8 проблема -\n"
  "8-25 один приём (показать, не рассказать) - 25-35 результат - CTA.\n"
  "Две колонки: что говорим / что в кадре.\n"
  "Раздели сцены на avatar_scene и non_avatar_scene; не-аватарные —\n"
  "motion-сцены (Seedance), не статик/скриншот/overlay.\n"
  "Дай: таблицу сцен, чистый текст озвучки, 3 заголовка обложки, описание.\n"
  "Голос спокойный, польза плотно. CTA: «в комментариях под постом».\n"))

P.append(skillpage("Скилл · пост",12,3,"Пост живым голосом",
  "пишет пост/подпись в твоём голосе — без штампов, с сильным началом.",
  "---\n"
  "name: alovlab-post\n"
  "description: Когда прошу написать пост, текст, подпись или описание\n"
  "  в моём голосе.\n"
  "---\n"
  "# Пост AlovLab\n"
  "Пиши живым языком. Первое слово уже работает — убери разгон.\n"
  "Короткие предложения, простые слова, одна мысль.\n"
  "Запрещены штампы: «в современном мире», «важно понимать»,\n"
  "«инновационное решение», «выведем на новый уровень» и подобные.\n"
  "Структура: хук - ситуация - одна сильная мысль - пример -\n"
  "шаг сегодня. Не заканчивай дежурным вопросом.\n"
  "Длина: пост 800-1500 знаков; подпись — до 500.\n"))

P.append(skillpage("Скилл · контент-план",13,4,"Контент-план недели",
  "собирает план на неделю по опорам и здоровой пропорции.",
  "---\n"
  "name: alovlab-plan\n"
  "description: Когда прошу контент-план, идеи на неделю, темы,\n"
  "  рубрики или расписание постов.\n"
  "---\n"
  "# Контент-план AlovLab\n"
  "План на неделю. Опоры и пропорция 2:1:1:1: Польза x2,\n"
  "Смысл/позиция x1, Практика/кейс x1, Приглашение x1.\n"
  "Приглашение — раз в неделю, без давления.\n"
  "Каждый день: тема, рубрика, формат, черновик хука, выход воронки.\n"
  "Формат ответа: таблица День · Опора · Рубрика · Формат · Хук.\n"))

P.append(skillpage("Скилл · разбор конкурента",14,5,"Разбор конкурента",
  "раскладывает чужой контент/воронку по ссылке или тексту.",
  "---\n"
  "name: alovlab-competitor\n"
  "description: Когда даю ссылку или текст конкурента и прошу\n"
  "  разобрать, проанализировать его контент или воронку.\n"
  "---\n"
  "# Разбор конкурента\n"
  "Разложи по схеме: оффер - аудитория - хуки (типы) - форматы -\n"
  "воронка (куда ведёт, чем закрывает) - лид-магнит - гэпы.\n"
  "Отдельно: что взять как ПРИЁМ (не текст) и чем мы отличаемся.\n"
  "Только по тому, что реально видно. Нет данных — пиши UNKNOWN,\n"
  "не выдумывай метрики и факты.\n"))

P.append(skillpage("Скилл · возражения",15,6,"Ответы на возражения",
  "обрабатывает возражение клиента через 3 вопроса — в страх, а не в цену.",
  "---\n"
  "name: alovlab-objections\n"
  "description: Когда прошу ответить на возражение клиента или\n"
  "  обработать «дорого», «я подумаю», «нет времени».\n"
  "---\n"
  "# Возражения AlovLab\n"
  "Любое возражение разложи на 3 вопроса: 1) что за словами;\n"
  "2) чего боится; 3) что нужно, чтобы сказать «да».\n"
  "Отвечай на страх, а не на цену. Формула ответа:\n"
  "признай - переведи на страх - дай результат/доказательство -\n"
  "один спокойный шаг. Без давления, «успей» и скидки по умолчанию.\n"))

P.append(skillpage("Скилл · лид-магнит",16,7,"Лид-магнит",
  "собирает короткий полезный материал (чек-лист/шаблон) под тему.",
  "---\n"
  "name: alovlab-leadmagnet\n"
  "description: Когда прошу собрать лид-магнит, чек-лист, гайд\n"
  "  или шаблон под тему.\n"
  "---\n"
  "# Лид-магнит AlovLab\n"
  "Собери короткий полезный материал: чек-лист / шаблон / список.\n"
  "Одна конкретная польза, применимая сегодня.\n"
  "Структура: обещание - 5-10 пунктов/шагов - готовый промпт/шаблон -\n"
  "CTA «в комментариях под постом» - выход на курс.\n"
  "Честно: без выдуманных цифр; отдаём реальную пользу.\n"))

# 17 Установка
P.append(page("Куда положить",17,
  head("Установка","Как подключить скилл",
    "Скилл — это папка с файлом SKILL.md. Claude подхватывает его, когда задача подходит под описание.")
  + act("Шаги",[
      "Создай папку с именем скилла (напр. <b>alovlab-carousel</b>).",
      "Внутри — файл <b>SKILL.md</b> (текст из этой тетради).",
      "Положи папку туда, откуда Claude читает скиллы (в Claude Code — каталог skills проекта).",
      "Проверь: попроси задачу словами из триггера — скилл включится сам."])
  + '<p class="note">Точное место для твоей версии Claude — в официальной доке: <b>code.claude.com/docs</b> (раздел про Skills). Не уверен — попроси Claude показать, куда класть.</p>'
))

# 18 Чек-лист
P.append(page("Чек-лист скилла",18,
  head("Перед сохранением","Скилл готов?")
  + '<div class="callout check"><div class="h">Чек-лист SKILL.md</div>'
    '<div class="row">Имя короткое и по задаче (латиницей, через дефис)</div>'
    '<div class="row">Описание начинается с «Когда прошу…» + синонимы запроса</div>'
    '<div class="row">Инструкция шагами, а не сплошным абзацем</div>'
    '<div class="row">Указан формат ответа</div>'
    '<div class="row">Есть пример вход → выход</div>'
    '<div class="row">Зашиты тон и запреты (штампы, без выдуманных цифр)</div>'
    '<div class="row">Один скилл — одна задача</div>'
    '<div class="row">Проверил на реальном запросе, поправил после теста</div>'
    '</div>'
))

# 19 CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:25pt;line-height:1.12;margin:18px 0 8px">Один раз собрал —<br><span style="color:var(--o2)">работает всегда.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">7 готовых скиллов и весь метод — вся тетрадь дня. Как собрать из скиллов свой контент-конвейер, учим на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Шаблон + скиллы — в комментариях под постом</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Собери свой Claude Skill · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
