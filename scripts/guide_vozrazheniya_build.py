# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 24 (27.08) «Возражения: услышь не слово» — премиум-PDF (фикс-A4).
Метод «отвечай на страх, а не на слова»: любое возражение = 3 вопроса. Разбор 5 частых возражений
(дорого/подумаю/гарантии/нет времени/напишу позже) с готовым ответом, формула ответа, 3 промпта
Claude (разложить → ответить → банк ответов), до/после, бланк, чек-лист.
Честность: примеры учебные, без выдуманных цифр. CTA — в комментариях под постом (TG+ВК).
База CSS — v2. Запуск: python3 scripts/guide_vozrazheniya_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "vozrazheniya"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-vozrazheniya.html"

EXTRA = r"""
.rec{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:8px 0;align-items:start}
.rec .n{width:22px;height:22px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.prompt code{font-size:8.9pt;line-height:1.5}
.act{margin:9px 0 2px}
.act .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:6px 0;align-items:start}
.act .s .k{width:20px;height:20px;border-radius:6px;background:#ece0cc;color:#8a6127;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;line-height:1;margin-top:1px}
.act .s p{font-size:9.5pt;line-height:1.42;color:var(--body)}.act .s p b{color:var(--ink);font-weight:800}.act .s p em{font-style:normal;color:var(--o);font-weight:700}
.actlbl{display:block;font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin:6px 0 2px}
.phrase{display:inline-block;background:#13100a;color:#fff;font-weight:800;font-size:14pt;border-radius:9px;padding:7px 15px;margin:2px 0 8px}
.phrase i{color:var(--o2);font-style:normal}
.tri{margin:7px 0}
.tri .r{display:grid;grid-template-columns:132px 1fr;gap:12px;align-items:baseline;padding:8px 0;border-bottom:1px solid var(--line)}
.tri .r:last-child{border-bottom:0}
.tri .r b{font-weight:800;font-size:8.3pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.tri .r p{font-size:9.6pt;line-height:1.4;color:var(--ink)}
.tri .r.hi{background:var(--o-tint);border-radius:9px;padding:8px 11px;border:0;margin-top:3px}.tri .r.hi b{color:var(--o)}.tri .r.hi p{font-weight:700}
.reply{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o2);border-radius:11px;padding:11px 14px;margin:9px 0}
.reply .h{font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o);margin-bottom:5px}
.reply p{font-size:9.7pt;line-height:1.5;color:var(--ink);font-style:italic}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:9px 0}
.pair .c{border-radius:12px;padding:11px 13px;font-size:9.5pt;line-height:1.48}
.pair .bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.pair .good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.pair .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:5px}
.pair .bad .l{color:#c56b43}.pair .good .l{color:var(--o)}
.formula{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin:10px 0}
.formula span{font-weight:800;font-size:10pt;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:9px;padding:8px 12px}
.formula i{color:var(--o2);font-style:normal;font-weight:800;font-size:12pt}
.blank{display:flex;flex-direction:column;gap:8px;margin:9px 0}
.blank .row{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:9px;padding:9px 12px}
.blank .row .h{font-weight:800;font-size:9pt;color:var(--ink);margin-bottom:5px}
.blank .ln{height:1px;border-bottom:1.4px dashed var(--line2);min-height:12px;margin:5px 0}
"""
CSS = V2CSS + EXTRA
VOICE = "[ГОЛОС] живо, короткие фразы, без штампов и давления."

def page(section, num, inner):
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main">{inner}</div>'
            f'<div class="pf"><span>AlovLab · возражения</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')
def head(kick,h2,lead=None):
    l=f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def rec(n,t,b): return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{t}</b><p>{b}</p></div></div>'
def act(lbl,steps): return f'<span class="actlbl">{lbl}</span><div class="act">'+''.join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i,t in enumerate(steps,1))+'</div>'
def prompt(tag,code,ru=None):
    ru_html=f'<div class="ru"><b>Разбор:</b> {ru}</div>' if ru else ''
    return f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span><span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>'
def tri(za,boit,nuzhno):
    return ('<div class="tri">'
            f'<div class="r"><b>Что за словами</b><p>{za}</p></div>'
            f'<div class="r"><b>Чего боится</b><p>{boit}</p></div>'
            f'<div class="r hi"><b>Что нужно</b><p>{nuzhno}</p></div></div>')
def reply(txt): return f'<div class="reply"><div class="h">Как ответить (пример)</div><p>{txt}</p></div>'
def pair(bad,good,bl="Ответ на слова",gl="Ответ на страх"):
    return (f'<div class="pair"><div class="c bad"><span class="l">✕ {bl}</span>{bad}</div>'
            f'<div class="c good"><span class="l">✓ {gl}</span>{good}</div></div>')
def objpage(section,num,phrase_w,phrase_o,za,boit,nuzhno,rep):
    return page(section,num, f'<span class="kick" style="display:block">Разбор возражения</span>'
        f'<div class="phrase">«{phrase_w}<i>{phrase_o}</i>»</div>'
        + tri(za,boit,nuzhno) + reply(rep))

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 24</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Возражения: <span style="color:var(--o2)">услышь не слово.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">«Дорого» — это не про деньги. За каждой фразой клиента прячется страх. Отвечай на страх — и «нет» превращается в «да». Разбор 5 частых возражений, формула ответа и промпты для Claude.</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">5 возражений</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Формула ответа</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 промпта</span>
    </div>
  </div>
</section>""")

# 02 Что внутри
P.append(page("Что внутри",2,
  head("Тетрадь под карусель «Возражения»","Клиент говорит не то, что думает",
    "Возражение — это не отказ. Это вопрос без ответа. Твоя работа — услышать не слово, а страх под ним, и ответить туда. Тогда «дорого» и «я подумаю» перестают убивать сделку.")
  + '<div class="term"><b>Возражение</b> — <span>то, что клиент говорит вслух. Почти всегда — прикрытие настоящей причины.</span></div>'
  + '<div class="term"><b>Страх</b> — <span>то, что стоит за словами: боится потерять деньги, ошибиться, разочароваться. Отвечать надо сюда.</span></div>'
  + '<div class="callout result"><div class="h">Что на выходе</div><p>Разбор 5 частых возражений по одной схеме, готовые ответы, формула, промпты — и заполненный банк ответов под твою нишу.</p></div>'
))

# 03 Диагноз
P.append(page("Диагноз",3,
  head("Почему теряешь","Отвечаешь на слова — теряешь клиента",
    "Клиент сказал «дорого» — и ты начал оправдывать цену или дал скидку. В этот момент сделка уже проиграна: ты ответил не на то.")
  + rec(1,"Принял слова за чистую монету","«Дорого» ≠ «нет денег». Но ты споришь о цене вместо настоящей причины.")
  + rec(2,"Начал защищаться","Оправдания звучат как слабость. Клиент чувствует давление и уходит.")
  + rec(3,"Дал скидку","Скидка на холодную не убеждает — она обесценивает и не снимает страх.")
  + rec(4,"Задавил","«Успей», «последний шанс» — фейковая срочность отпугивает тёплого человека.")
  + '<p class="note">Лечится одним сдвигом: не отвечай на слова. Услышь страх под ними — и ответь на страх.</p>'
))

# 04 Метод
P.append(page("Метод",4,
  head("Три вопроса","Любое возражение = 3 вопроса",
    "Не важно, что сказал клиент. Разложи любую фразу на три вопроса — и сразу видно, о чём на самом деле речь и что отвечать.")
  + '<div class="tri">'
    '<div class="r"><b>1 · Что за словами</b><p>Настоящая причина. Что клиент имеет в виду на самом деле.</p></div>'
    '<div class="r"><b>2 · Чего боится</b><p>Страх под причиной: потерять деньги, время, лицо; ошибиться.</p></div>'
    '<div class="r hi"><b>3 · Что нужно</b><p>Что он должен получить/понять, чтобы сказать «да».</p></div>'
    '</div>'
  + '<p class="note">Ответ строишь на пункт 3 — «что нужно». На слова (пункт «дорого») не отвечаешь вообще.</p>'
))

# 05 Правило
P.append(page("Правило",5,
  head("Главный сдвиг","Не спорь о цене — верни к результату",
    "Как только разговор ушёл в цену — ты проигрываешь: спорить о числах бесполезно. Верни фокус на то, ради чего клиент вообще пришёл.")
  + '<div class="pair"><div class="c bad"><span class="l">✕ Спор о цене</span>«Это не дорого, у конкурентов дороже, и вообще качество…» — защита, числа против чисел.</div>'
    '<div class="c good"><span class="l">✓ Возврат к результату</span>«Давай зафиксируем результат, который тебе нужен, и покажу, как придём к нему без риска.»</div></div>'
  + '<p class="note">Цена — это число. Результат — это жизнь клиента. Второе всегда перевешивает, если о нём напомнить.</p>'
))

# 06-10 · 5 возражений
P.append(objpage("«Дорого»",6,"Дорого","",
  "Не про деньги. Про «а вдруг не окупится, не поможет».",
  "Потерять деньги зря, купить и разочароваться.",
  "Уверенность, что решение даст результат; понятный план без риска.",
  "«Понимаю, рисковать деньгами не хочется. Давай так: зафиксируем результат, который тебе нужен, и я покажу по шагам, как мы к нему придём. Тогда цена — это не трата, а путь к нему.»"))
P.append(objpage("«Я подумаю»",7,"Я подумаю","",
  "Не готов решать прямо сейчас; что-то одно не закрыто.",
  "Ошибиться, поменять привычный сценарий, поспешить.",
  "Снять последнее конкретное сомнение и лёгкий необязывающий шаг.",
  "«Конечно, подумай. Обычно за «подумаю» прячется один невыясненный вопрос. Что тебя останавливает больше — цена, сроки или сомнение, что подойдёт именно тебе? Разберём — и решишь спокойно.»"))
P.append(objpage("«Нужны гарантии»",8,"Нужны гарантии","",
  "Не доверяет; боится, что обещания не сойдутся с реальностью.",
  "Потерять и деньги, и время; остаться с плохим результатом.",
  "Конкретное доказательство и предсказуемость процесса.",
  "«Понимаю, вслепую заходить не хочется. Вот что гарантирую конкретно: [этапы работы / что если не подойдёт]. И покажу, как это выглядело у других — чтобы ты видел, а не верил на слово.»"))
P.append(objpage("«Нет времени»",9,"Нет времени","",
  "Не видит ценности или перегружен; боится ещё одной нагрузки.",
  "Что это отнимет время и силы, которых и так нет.",
  "Понять, что решение экономит время, а не добавляет задач.",
  "«Как раз чтобы не грузить тебя — я беру [эту часть] на себя. От тебя нужно только [минимум], это займёт [X минут]. Смысл в том, чтобы у тебя времени стало больше, а не меньше.»"))
P.append(objpage("«Напишу позже»",10,"Напишу позже","",
  "Не хочет отказывать впрямую или ещё не дозрел.",
  "Давления и навязчивости; сказать «нет» в лицо.",
  "Лёгкий необязывающий следующий шаг и ощущение, что не торопят.",
  "«Без проблем, не тороплю. Оставлю тебе [материал / место / бронь], а когда будешь готов — напиши одно слово «старт». Так ничего не потеряешь и решишь в своём темпе.»"))

# 11 Формула ответа
P.append(page("Формула ответа",11,
  head("Как построить ответ","Признай → страх → результат → шаг",
    "Любой ответ на возражение собирается из четырёх частей. Держи порядок — и ответ звучит как поддержка, а не как спор.")
  + '<div class="formula"><span>Признай чувство</span><i>→</i><span>Переведи на страх</span><i>→</i><span>Дай результат/доказательство</span><i>→</i><span>Один лёгкий шаг</span></div>'
  + rec(1,"Признай","«Понимаю, рисковать не хочется». Человек должен почувствовать, что его услышали.")
  + rec(2,"Переведи на страх","Назови настоящую причину: «дело ведь не в цене, а в том, сработает ли».")
  + rec(3,"Дай результат/доказательство","Верни к тому, ради чего пришёл; покажи, а не обещай.")
  + rec(4,"Один лёгкий шаг","Маленькое необязывающее действие. Без «успей» и давления.")
))

# 12 Промпт 1
P.append(page("Промпт 1 · разложить",12,
  head("Этап · разобрать возражение","Claude раскладывает на 3 вопроса",
    "Первый шаг — вскрыть, что на самом деле стоит за фразой клиента. Дальше ответ строится сам.")
  + act("Что делаешь",[
      "Открываешь Claude, вставляешь промпт.",
      "Подставляешь <b>возражение и нишу</b>.",
      "Получаешь 3 вопроса — <em>проверяешь</em>: настоящая причина, а не «вода».",
      "Переносишь в бланк (стр. 16)."])
  + prompt("Промпт · Claude",
    "Возьми возражение «[ЧТО ГОВОРЯТ]» под нишу [ТВОЯ].\n"
    "Разложи на 3 вопроса:\n"
    "1) что за словами (настоящая причина);\n"
    "2) чего человек боится;\n"
    "3) что ему нужно, чтобы сказать «да».\n"
    "Без спора о цене. Коротко и конкретно.\n" + VOICE,
    "если «что за словами» подходит под любой бизнес — это вода. Проси конкретнее под твою нишу.")
))

# 13 Промпт 2
P.append(page("Промпт 2 · ответить",13,
  head("Этап · написать ответ","Claude пишет ответ на страх",
    "Разбор есть. Теперь — короткий ответ по формуле: признай → страх → результат → шаг.")
  + act("Что делаешь",[
      "Берёшь разбор из промпта 1.",
      "Вставляешь его и <b>свои факты/доказательства</b>.",
      "Claude пишет ответ — <em>читаешь вслух</em>: звучит как поддержка, не спор?",
      "Правишь под свой голос."])
  + prompt("Промпт · Claude",
    "На основе разбора напиши короткий ответ на возражение\n"
    "«[ЧТО ГОВОРЯТ]» для ниши [ТВОЯ]. Структура: признай чувство →\n"
    "переведи со слов на страх → дай доказательство/результат →\n"
    "один спокойный шаг. Без давления, «успей» и скидки по умолчанию.\n"
    "Мои доказательства: [ВСТАВЬ].\n" + VOICE,
    "ответ бьёт в страх, а не в цену. Скидка — не аргумент; аргумент — результат и предсказуемость.")
))

# 14 Промпт 3
P.append(page("Промпт 3 · банк",14,
  head("Этап · собрать банк","Claude соберёт ответы на все твои возражения",
    "Один раз собираешь банк — и больше не теряешься. На каждое частое возражение готовый разбор и ответ.")
  + act("Что делаешь",[
      "Выпиши 5 своих самых частых возражений.",
      "Вставляешь список в промпт.",
      "Получаешь таблицу: разбор + ответ по каждому.",
      "Держишь под рукой — <em>отвечаешь за секунды</em>, а не выдумываешь на ходу."])
  + prompt("Промпт · Claude",
    "Собери банк ответов на 5 моих частых возражений: [СПИСОК].\n"
    "По каждому дай: как звучит → что за этим → чего боится →\n"
    "что нужно → готовый ответ (признай → страх → доказательство → шаг).\n"
    "Ниша: [ТВОЯ]. Живым языком, без штампов и давления.\n" + VOICE,
    "банк = твой скрипт продаж без впаривания. Обновляй, когда слышишь новое возражение.")
))

# 15 До/после
P.append(page("До / после",15,
  head("Разбор","Слова против страха")
  + pair('Клиент: «Дорого». Ты: «Ну это же качество, и вообще у других дороже, давайте скидку 10%».',
         'Клиент: «Дорого». Ты: «Понимаю. Дело ведь не в цене, а в том, сработает ли. Давай покажу, как придём к результату без риска».')
  + '<span class="kick" style="display:block;margin-top:14px">Ещё пример</span>'
  + pair('«Я подумаю». — «Хорошо, буду ждать!» (и тишина, клиент растворился)',
         '«Я подумаю». — «Конечно. Что останавливает больше — цена, сроки или сомнение, что подойдёт? Разберём — и решишь спокойно».')
  + '<p class="note">Одна и та же фраза клиента. Разница — отвечаешь ты на слово или на страх.</p>'
))

# 16 Бланк
P.append(page("Бланк · твой банк",16,
  head("Заполни под себя","5 твоих возражений — разобраны")
  + '<div class="blank">'
    + ''.join(
      f'<div class="row"><div class="h">Возражение {i}: ______________________</div>'
      '<div class="ln"></div><div class="ln"></div></div>' for i in range(1,6))
    + '</div>'
  + '<p class="note">В каждом блоке: что за словами · чего боится · что нужно · <span style="color:var(--o);font-weight:700">готовый ответ</span>. Собери промптом 3 и впиши.</p>'
))

# 17 Чек-лист
P.append(page("Чек-лист · честность",17,
  head("Контроль","Ответ на страх или спор о цене")
  + '<div class="callout check"><div class="h">Чек-лист ответа</div>'
    '<div class="row">Разложил возражение на 3 вопроса, нашёл настоящую причину</div>'
    '<div class="row">Отвечаешь на страх, а не на слова</div>'
    '<div class="row">Не споришь о цене — вернул к результату</div>'
    '<div class="row">Признал чувство клиента, не защищаешься</div>'
    '<div class="row">Никакой скидки по умолчанию, «успей» и фейкового дефицита</div>'
    '<div class="row">Даёшь один спокойный необязывающий шаг</div>'
    '<div class="row">Доказательства реальные, без выдуманных цифр и кейсов</div>'
    '</div>'
  + '<p class="note">Честно: работа с возражениями — это не «дожать любой ценой», а снять страх и помочь решить. Тому, кому не подходит, честнее сказать «не подходит».</p>'
))

# 18 CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:25pt;line-height:1.12;margin:18px 0 8px">Услышь не слово —<br><span style="color:var(--o2)">услышь страх.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Разбор 5 возражений, формула ответа и промпты — вся тетрадь дня. Продажам без впаривания и всей системе учим на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Гайд + промпт — в комментариях под постом</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Возражения: услышь не слово · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
