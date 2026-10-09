# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 2 (29.08) «Пиши так, чтобы не звучало как нейросеть» — премиум-PDF (фикс-A4).
Рубрика «Дело не в модели». Стоп-лист из 10 фраз (каждая: почему палит → как сказать живо),
правило «первое слово уже работает», 5 приёмов живого письма, 3 промпта (переписать / детектор штампов /
свой стоп-лист под нишу), до/после, чек-лист. Честность: штампы реальные из стоп-листа, без выдуманных цифр.
База CSS — v2. Запуск: python3 scripts/guide_claude_text_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "claude-text"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-claude-text.html"

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
.stop{background:#fff;border:1px solid var(--line);border-radius:12px;padding:11px 13px;margin:8px 0}
.stop .ph{display:flex;align-items:center;gap:10px;margin-bottom:6px}
.stop .ph .n{width:22px;height:22px;border-radius:7px;background:#13100a;color:var(--o2);font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center;flex:none}
.stop .ph s{color:#b23b16;font-weight:800;font-size:11pt;text-decoration:line-through;text-decoration-color:#e0a58c}
.stop .why{font-size:9.4pt;line-height:1.42;color:var(--body);margin:2px 0}
.stop .why b{color:#c56b43;font-weight:800}
.stop .live{font-size:9.6pt;line-height:1.42;color:var(--ink);background:var(--o-tint);border-radius:8px;padding:6px 10px;margin-top:5px}
.stop .live b{color:var(--o);font-weight:800}
.killer{columns:2;column-gap:20px;margin:9px 0}
.killer .k{break-inside:avoid;display:flex;gap:8px;align-items:baseline;padding:6px 0;border-bottom:1px solid var(--line)}
.killer .k .i{color:var(--o);font-weight:800;font-size:9.5pt;flex:none}
.killer .k s{color:#8a5a48;font-weight:700;font-size:9.7pt;text-decoration:line-through;text-decoration-color:#d9b3a2}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:9px 0}
.pair .c{border-radius:12px;padding:11px 13px;font-size:9.4pt;line-height:1.48}
.pair .bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.pair .good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.pair .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:5px}
.pair .bad .l{color:#c56b43}.pair .good .l{color:var(--o)}
"""
CSS = V2CSS + EXTRA
VOICE = "[ГОЛОС] живо, короткие фразы, без штампов."

def page(section, num, inner):
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main">{inner}</div>'
            f'<div class="pf"><span>AlovLab · пиши как человек</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')
def head(kick,h2,lead=None):
    l=f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def rec(n,t,b): return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{t}</b><p>{b}</p></div></div>'
def act(lbl,steps): return f'<span class="actlbl">{lbl}</span><div class="act">'+''.join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i,t in enumerate(steps,1))+'</div>'
def prompt(tag,code,ru=None):
    ru_html=f'<div class="ru"><b>Подсказка:</b> {ru}</div>' if ru else ''
    return f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span><span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>'
def stop(n,phrase,why,live):
    return (f'<div class="stop"><div class="ph"><span class="n">{n}</span><s>«{phrase}»</s></div>'
            f'<p class="why"><b>Палит:</b> {why}</p>'
            f'<p class="live"><b>Живо:</b> {live}</p></div>')
def pair(bad,good,bl="Как пишет нейросеть",gl="Как пишет человек"):
    return (f'<div class="pair"><div class="c bad"><span class="l">✕ {bl}</span>{bad}</div>'
            f'<div class="c good"><span class="l">✓ {gl}</span>{good}</div></div>')

PHRASES = [
 ("В современном мире","пустой разгон, ноль смысла — все так начинают ИИ-тексты.","начни с сути: «Сегодня клиент выбирает за 3 секунды.»"),
 ("Важно понимать","подводка вместо мысли; читатель уже заскучал.","сразу скажи, что важно: «Заголовок решает, откроют пост или нет.»"),
 ("Как известно","если известно — зачем пишешь; звучит снисходительно.","дай факт или убери: «Люди не читают — сканируют.»"),
 ("Стоит отметить","канцелярит-связка, крадёт первую строку.","просто отметь: «Первое слово уже работает.»"),
 ("Давайте разберёмся","школьный тон, ставит читателя ниже.","веди действием: «Разложу на три шага.»"),
 ("Нейросети стремительно развиваются","штамп-новость ни о чём, выдаёт генерацию.","говори про пользу, не про прогресс: «ИИ уже пишет черновик за тебя.»"),
 ("Будущее уже здесь","пафос без содержания, миллион раз слышали.","покажи конкретику: «Сегодня это делает один промпт.»"),
 ("Откройте для себя","рекламная пустота, будто из буклета.","обратись прямо: «Забери приём и попробуй сегодня.»"),
 ("Выведите бизнес на новый уровень","самая заезженная фраза продажников.","назови результат: «Собирай посты за час, а не за день.»"),
 ("Инновационное решение","маркетинговый шум, ничего не значит.","скажи, что это делает: «Инструмент, который снимает рутину.»"),
]

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 2</div>
    <h1 style="font-weight:800;font-size:32pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:17ch">Пиши так, чтобы не звучало <span style="color:var(--o2)">как нейросеть.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:46ch">Текст, написанный ИИ, видно с первой строки — по штампам. Дело не в модели, а в стоп-листе и одном правиле. Внутри: 10 фраз, которые выдают нейросеть, приёмы живого письма и промпты для Claude.</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Стоп-лист 10 фраз</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">5 приёмов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 промпта</span>
    </div>
  </div>
</section>""")

# 02 Что внутри
P.append(page("Что внутри",2,
  head("Тетрадь под рил «5 фраз»","Дело не в модели",
    "«Звучит как ChatGPT» — не потому что модель плохая. Любая нейросеть пишет штампами, пока ты не запретил их и не задал одно правило. Тогда текст оживает — на любой модели.")
  + '<div class="callout result"><div class="h">Что на выходе</div><p>Стоп-лист из 10 фраз, которые выдают нейросеть (с заменами), 5 приёмов живого письма и 3 промпта: переписать текст, проверить на штампы и собрать свой стоп-лист под нишу.</p></div>'
  + '<p class="note">Работает и с Claude, и с любой другой моделью. Дело не в инструменте — в том, что ты просишь.</p>'
))

# 03 Правило
P.append(page("Главное правило",3,
  head("Один сдвиг","Первое слово уже работает",
    "Почти все штампы — это разгон: вступление перед мыслью. Убери разгон — и штамп не нужен. Начинай там, где начинается смысл.")
  + pair('«В современном мире всё больше компаний задумываются о том, как важно понимать своего клиента…»',
         '«Клиент выбирает за 3 секунды. Не угадал — закрыл.»',
         "Разгон (штамп)","Сразу суть")
  + '<span class="kick" style="display:block;margin-top:14px">Проверка на разгон</span>'
  + rec(1,"Вычеркни первое предложение","Если смысл не потерялся — оно было разгоном. Так почти всегда.")
  + rec(2,"Спроси: первое слово цепляет?","Если это «в», «как», «сегодня многие» — переписывай. Первое слово должно работать.")
))

# 04 Стоп-лист (скриншот-страница)
P.append(page("Стоп-лист",4,
  head("Выпиши и не используй","10 фраз, которые выдают нейросеть",
    "Это скриншот-страница. Сверяйся с ней перед публикацией: нашёл фразу из списка — переписывай.")
  + '<div class="killer">'
    + ''.join(f'<div class="k"><span class="i">{i}</span><s>{p}</s></div>' for i,(p,_,_) in enumerate(PHRASES,1))
    + '</div>'
  + '<p class="note">Разбор каждой — со сменой на живой вариант — на следующих страницах.</p>'
))

# 05-07 разбор фраз
P.append(page("Разбор · 1–4",5,
  head("Почему палит → как живо","Фразы 1–4")
  + ''.join(stop(i,p,w,l) for i,(p,w,l) in enumerate(PHRASES[:4],1))
))
P.append(page("Разбор · 5–7",6,
  head("Почему палит → как живо","Фразы 5–7")
  + ''.join(stop(i,p,w,l) for i,(p,w,l) in enumerate(PHRASES[4:7],5))
))
P.append(page("Разбор · 8–10",7,
  head("Почему палит → как живо","Фразы 8–10")
  + ''.join(stop(i,p,w,l) for i,(p,w,l) in enumerate(PHRASES[7:],8))
))

# 08 5 приёмов
P.append(page("Приёмы живого письма",8,
  head("Не только стоп-лист","5 приёмов, чтобы звучать как человек",
    "Убрать штампы — половина дела. Вот что делает текст живым.")
  + rec(1,"Короткие предложения","Одна мысль — одно предложение. Длинное разбей. Читается на выдохе.")
  + rec(2,"Простые слова","«Использовать» → «взять». «Осуществлять» → «делать». Пиши, как говоришь.")
  + rec(3,"Конкретика вместо общего","Не «эффективно», а «собираешь пост за час вместо дня».")
  + rec(4,"Абзацы разной длины","Один в строку, следующий в три. Ровные блоки усыпляют.")
  + rec(5,"Не заканчивай вопросом","«А что думаете вы?» — штамп. Заверши мыслью, а не дежурным вопросом.")
))

# 09 Промпт 1
P.append(page("Промпт 1 · переписать",9,
  head("Этап · оживить текст","Claude переписывает сухое в живое",
    "Готовый текст звучит как робот? Прогони через этот промпт — вернётся живым, и видно, что убрано.")
  + act("Что делаешь",[
      "Вставляешь свой текст в промпт.",
      "Получаешь живой вариант + список убранного.",
      "<em>Читаешь вслух</em>: звучит как ты или как буклет?",
      "Правишь под свой голос."])
  + prompt("Промпт · Claude",
    "Перепиши живым человеческим языком: [ВСТАВЬ ТЕКСТ].\n"
    "Правила: первое слово уже работает (убери разгон);\n"
    "короткие предложения; простые слова; одна мысль.\n"
    "Запрещены штампы: «в современном мире», «важно понимать»,\n"
    "«инновационное решение» и подобные.\n"
    "Покажи готовый вариант и что именно убрал.\n" + VOICE,
    "если Claude оставил штамп — укажи прямо: «убери „важно понимать“ и перепиши строку».")
))

# 10 Промпт 2
P.append(page("Промпт 2 · детектор",10,
  head("Этап · проверить","Claude ищет штампы в твоём тексте",
    "Не уверен, что чисто? Пусть Claude выступит редактором и подсветит каждый штамп с заменой.")
  + act("Что делаешь",[
      "Вставляешь текст.",
      "Получаешь список: где штамп → чем заменить.",
      "Правишь по списку.",
      "<em>Прогоняешь ещё раз</em> — до нуля штампов."])
  + prompt("Промпт · Claude",
    "Проверь мой текст на штампы и канцелярит: [ВСТАВЬ ТЕКСТ].\n"
    "Найди каждую фразу-штамп, объясни коротко, чем она палит,\n"
    "и предложи живую замену. Отдельно отметь разгон в начале\n"
    "(вступление перед мыслью).\n" + VOICE,
    "это твой редактор без оплаты. Прогоняй каждый важный текст перед публикацией.")
))

# 11 Промпт 3
P.append(page("Промпт 3 · свой стоп-лист",11,
  head("Этап · под свою нишу","Claude соберёт стоп-лист под тебя",
    "У каждой ниши свои заезженные фразы. Собери персональный стоп-лист — и держи под рукой.")
  + act("Что делаешь",[
      "Назови свою нишу и пару своих текстов.",
      "Claude выпишет штампы именно твоей темы.",
      "Дополни список этой тетрадью (10 общих фраз).",
      "<em>Держишь рядом</em> — сверяешься перед каждым постом."])
  + prompt("Промпт · Claude",
    "Я работаю в нише [ТВОЯ]. Вот пара моих текстов: [ВСТАВЬ].\n"
    "Собери стоп-лист из 10–15 заезженных фраз именно для этой ниши\n"
    "(которые все пишут и которые звучат шаблонно). По каждой —\n"
    "живая замена. Оформи списком, чтобы держать под рукой.\n" + VOICE,
    "добавляй в список новые штампы, как только заметишь их у себя или у конкурентов.")
))

# 12 До/после
P.append(page("До / после",12,
  head("Разбор","Один абзац — два голоса")
  + pair('«В современном мире важно понимать, что нейросети стремительно развиваются и открывают перед бизнесом инновационные решения, которые выводят его на новый уровень.»',
         '«Нейросеть уже пишет тебе черновик, собирает пост и наводит порядок в файлах. Не «будущее» — сегодня. Вопрос один: ты умеешь ставить задачу?»')
  + '<p class="note">Одна и та же тема. Сверху — четыре штампа из стоп-листа. Снизу — конкретика и живой ритм.</p>'
))

# 13 Чек-лист
P.append(page("Чек-лист · звучит как человек",13,
  head("Контроль","Перед публикацией")
  + '<div class="callout check"><div class="h">Чек-лист живого текста</div>'
    '<div class="row">Ни одной фразы из стоп-листа (10 штук)</div>'
    '<div class="row">Первое слово уже работает — нет разгона</div>'
    '<div class="row">Первое предложение можно было бы удалить? Удалил</div>'
    '<div class="row">Короткие предложения, простые слова</div>'
    '<div class="row">Есть конкретика, а не общие «эффективно/качественно»</div>'
    '<div class="row">Абзацы разной длины</div>'
    '<div class="row">Не заканчивается дежурным вопросом</div>'
    '<div class="row">Прочитал вслух — звучит как я, а не как буклет</div>'
    '</div>'
  + '<p class="note">Честно: цель — не «обмануть детектор ИИ», а чтобы тебя было приятно читать. Живой текст держит внимание, штампованный — нет.</p>'
))

# 14 CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:25pt;line-height:1.12;margin:18px 0 8px">Дело не в модели —<br><span style="color:var(--o2)">в том, что ты просишь.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Стоп-лист, приёмы и промпты — вся тетрадь дня. Писать так, чтобы читали и покупали, и всей системе контента учим на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Стоп-лист + промпт — в комментариях под постом</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Пиши как человек · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
