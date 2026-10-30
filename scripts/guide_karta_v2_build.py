# -*- coding: utf-8 -*-
"""AlovLab · тетрадь «КАРТА СОСТОЯНИЙ» v2 — premium mini-course (пересборка с нуля).
Не справочник, а урок: framework (5 полей) → диагностика → Prompt Stack (9) с обучающей обёрткой
(зачем/вход/выход/хороший ответ/красные флаги/дожать) → Prompt Debugging → 3 before/after цепочки →
сквозное практическое задание с артефактом → бланк → чек-лист → master workflow.
Честность: без выдуманных цифр, чужой текст не вставляется. База CSS — v2. Запуск: python3 scripts/guide_karta_v2_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "karta-sostoyaniy-v2"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-karta-v2.html"

EXTRA = r"""
.rec{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:8px 0;align-items:start}
.rec .n{width:22px;height:22px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.prompt code{font-size:8.7pt;line-height:1.5}
.act{margin:9px 0 2px}
.act .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:6px 0;align-items:start}
.act .s .k{width:20px;height:20px;border-radius:6px;background:#ece0cc;color:#8a6127;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;line-height:1;margin-top:1px}
.act .s p{font-size:9.5pt;line-height:1.42;color:var(--body)}.act .s p b{color:var(--ink);font-weight:800}.act .s p em{font-style:normal;color:var(--o);font-weight:700}
/* переход-плашка + карта 5 полей */
.shift{display:inline-flex;align-items:center;gap:9px;background:var(--o-tint);border:1px solid #f2d3bf;border-radius:9px;padding:5px 12px;font-weight:800;font-size:9.5pt;color:var(--ink);margin:2px 0 8px}
.shift i{color:var(--o);font-style:normal;font-size:11pt}
.tri{margin:7px 0}
.tri .r{display:grid;grid-template-columns:118px 1fr;gap:12px;align-items:baseline;padding:8px 0;border-bottom:1px solid var(--line)}
.tri .r:last-child{border-bottom:0}
.tri .r b{font-weight:800;font-size:8.3pt;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.tri .r p{font-size:9.6pt;line-height:1.4;color:var(--ink)}
.tri .r.hi{background:var(--o-tint);border-radius:9px;padding:8px 11px;border:0;margin-top:3px}.tri .r.hi b{color:var(--o)}.tri .r.hi p{font-weight:700}
/* обучающая обёртка промпта */
.brief{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:7px 0}
.brief .b{background:#fff;border:1px solid var(--line);border-radius:9px;padding:8px 11px}
.brief .b b{display:block;font-size:7.3pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o);font-weight:800;margin-bottom:3px}
.brief .b p{font-size:9.2pt;line-height:1.32;color:var(--ink)}
.pchk{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:9px 0 0}
.pchk .c{border-radius:9px;padding:9px 11px;font-size:8.9pt;line-height:1.38}
.pchk .g{background:#f0f6ec;border:1px solid #cfe3c6;color:#40603a}
.pchk .r{background:#faf0ea;border:1px solid #eccdb9;color:#8a5a44}
.pchk .f{grid-column:1 / -1;background:#13100a;border:1px solid rgba(255,150,80,.3);color:#ffd9b8}
.pchk .c b{display:block;font-size:7.3pt;letter-spacing:.05em;text-transform:uppercase;font-weight:800;margin-bottom:4px}
.pchk .g b{color:#3f7d34}.pchk .r b{color:#c56b43}.pchk .f b{color:var(--o2)}
.pchk .f code{font-family:'SF Mono',ui-monospace,Menlo,monospace;font-size:8.6pt;color:#ffe0c4}
/* stack-карта 9 промптов */
.stack{display:flex;flex-direction:column;gap:6px;margin:9px 0}
.stack .r{display:grid;grid-template-columns:30px 1fr auto;gap:11px;align-items:center;background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:9px;padding:8px 12px}
.stack .r .n{font-weight:800;font-size:11pt;color:var(--o2)}
.stack .r .lb{font-weight:800;font-size:9.6pt;color:var(--ink)}
.stack .r .io{font-size:7.8pt;color:var(--muted);white-space:nowrap}
.stack .r.gen{border-left-color:#c99;background:#fbf3f0}
/* debugging таблица */
.dbg{width:100%;border-collapse:collapse;margin:8px 0;font-size:9pt}
.dbg th{text-align:left;font-size:7.3pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o);padding:6px 7px;border-bottom:2px solid var(--line2)}
.dbg td{padding:8px 7px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.32;color:var(--ink)}
.dbg td.s{font-weight:700}.dbg td.f{font-family:'SF Mono',ui-monospace,monospace;font-size:8pt;color:var(--body)}
/* before/after */
.ba .lbl{font-weight:800;font-size:7.6pt;letter-spacing:.05em;text-transform:uppercase;margin:9px 0 3px}
.ba .lbl.bad{color:#c56b43}.ba .lbl.good{color:var(--o)}.ba .lbl.n{color:var(--muted)}
.ba .box{border-radius:9px;padding:9px 12px;font-size:9.2pt;line-height:1.42}
.ba .box.bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.ba .box.good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.ba .box.mono{background:#13100a;color:#ffd9b8;font-family:'SF Mono',ui-monospace,monospace;font-size:8.5pt}
.ba .box.diag{background:var(--o-tint);border:1px solid #f2d3bf;color:var(--ink)}
/* workflow одной колонкой */
.wf{display:flex;flex-direction:column;gap:0;margin:8px 0}
.wf .st{display:grid;grid-template-columns:26px 1fr;gap:12px;align-items:start;padding:7px 0}
.wf .st .n{width:26px;height:26px;border-radius:8px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center}
.wf .st b{font-weight:800;font-size:10pt;color:var(--ink)}.wf .st p{margin-top:1px;font-size:9pt;line-height:1.34;color:var(--body)}
.wf .ln{grid-column:1;width:2px;height:8px;background:linear-gradient(var(--o),transparent);margin-left:12px}
/* бланк */
.blank{display:flex;flex-direction:column;gap:8px;margin:9px 0}
.blank .row{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:9px;padding:9px 12px}
.blank .row .h{font-weight:800;font-size:8.8pt;color:var(--ink);margin-bottom:5px}.blank .row .h i{font-style:normal;color:var(--o)}
.blank .ln{height:1px;border-bottom:1.4px dashed var(--line2);min-height:12px;margin:5px 0}
.result{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:11px;padding:11px 14px;margin:9px 0}
.result .h{font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o);margin-bottom:4px}
.result p{font-size:9.6pt;line-height:1.45;color:var(--ink)}
"""
CSS = V2CSS + EXTRA
VOICE = "[ГОЛОС] живо, короткие фразы, конкретика, без штампов и эмодзи-мусора."

def page(section, num, inner):
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main">{inner}</div>'
            f'<div class="pf"><span>AlovLab · карта состояний</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def rec(n, t, b): return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{t}</b><p>{b}</p></div></div>'
def act(lbl, steps):
    body = "".join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i, t in enumerate(steps, 1))
    return f'<span class="kick" style="display:block;margin-bottom:2px">{lbl}</span><div class="act">{body}</div>'
def promptpage(section, num, name, sub, inp, out, why, tag, code, good, flags, follow):
    brief = ('<div class="brief">'
             f'<div class="b"><b>Вход</b><p>{inp}</p></div>'
             f'<div class="b"><b>Выход</b><p>{out}</p></div></div>'
             f'<p class="note" style="margin-top:6px"><b>Почему работает:</b> {why}</p>')
    plaque = (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
              f'<span class="copy">скопировать</span></div><code>{code}</code></div>')
    checks = ('<div class="pchk">'
              f'<div class="c g"><b>Хороший ответ</b>{good}</div>'
              f'<div class="c r"><b>Красные флаги</b>{flags}</div>'
              f'<div class="c f"><b>Как дожать · follow-up</b><code>{follow}</code></div></div>')
    return page(section, num, head(name, sub) + brief + plaque + checks)

P = []

# 01 · Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · mini-course · прогрев</div>
    <h1 style="font-weight:800;font-size:34pt;line-height:1.04;letter-spacing:-.02em;color:#fff;max-width:14ch">Карта <span style="color:var(--o2)">состояний.</span></h1>
    <p style="margin-top:15px;font-size:12pt;line-height:1.5;color:#d8cdbd;max-width:46ch">Урок, а не справочник. Ты не «узнаешь про прогрев» — ты построишь его: карту читателя, стек из 9 промптов и готовую серию из 4 постов, которая ведёт к заявке. С отладкой и разборами «плохо → хорошо».</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Framework 5 полей</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Prompt Stack · 9</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Debugging</span>
    </div>
  </div>
</section>""")

# 02 · Что ты соберёшь (result-first)
P.append(page("Результат", 2,
  head("Обещание урока", "Что у тебя будет в конце",
    "Не конспект, а три готовых артефакта. Дойдёшь до конца — они собраны под твою нишу, не абстрактно.")
  + rec(1, "Карта состояний", "Заполненная таблица читателя на 4 касания: где он, что мешает, что должно измениться, чем доказать, что сделать.")
  + rec(2, "Свой промпт-стек", "9 промптов, которые ты запускаешь по очереди — от диагностики до оценки. Один раз настроил — крутишь под любой продукт.")
  + rec(3, "Серия из 4 постов", "Готовый прогрев, где каждый пост двигает человека на шаг ближе к заявке — без впаривания.")
  + '<div class="result"><div class="h">Как пользоваться</div><p>Читай подряд. После разделов с промптами — сразу запускай их в Claude на своём материале. К стр. 23 (практика) у тебя на руках будет готовая серия, а не конспект.</p></div>'
))

# 03 · Проблема
P.append(page("Проблема", 3,
  head("Дорогая тишина", "Прогрев не продаёт — и ты не понимаешь почему",
    "Собрал базу через лид-магнит. Постишь. А заявок нет. Дело не в частоте и не в цене продукта.")
  + rec(1, "Пик готовности — и мимо", "Сразу после скачивания человек максимально тёплый. Через три дня молчания он холодный. Ты упустил самый дорогой момент.")
  + rec(2, "Посты гладкие, но пустые", "Текст читается, а внутри — ничего, что двигает к решению. Лайк есть, шага нет.")
  + rec(3, "Продаёшь холодному", "Даёшь оффер тому, кто ещё сомневается. Он закрывает и не возвращается.")
  + '<p class="note">Общий совет «надо прогревать» тут бесполезен. Нужна механика: кого, из какого состояния и в какое ты двигаешь каждым постом. Этим и займёмся.</p>'
))

# 04 · Почему обычный подход — мусор
P.append(page("Почему не работает", 4,
  head("Мусор на входе", "«Напиши прогрев» — и получаешь пустоту",
    "Claude не телепат. Просишь «напиши 4 прогревающих поста» — он пишет для никого. Проблема не в модели, а в том, что ты дал ей нулевой вход.")
  + '<div class="pchk" style="grid-template-columns:1fr 1fr">'
    '<div class="c r"><b>Так делают все</b>«Ты эксперт по маркетингу. Напиши серию прогревающих постов для моей аудитории.» → гладкий текст ни для кого.</div>'
    '<div class="c g"><b>Так управляют моделью</b>Сначала описываешь состояние человека, трение, во что он не верит, чем это снять — и только потом просишь текст.</div>'
    '</div>'
  + '<p class="note">Разница не в длине промпта. В том, что во втором случае ты <b>думаешь за стратега, а не за копирайтера</b>. Claude лишь дописывает то, что ты уже разложил. Инструмент для этого — карта состояний.</p>'
))

# 05 · FRAMEWORK (SAVE)
P.append(page("Framework · SAVE", 5,
  head("Карта состояний", "Пять вопросов, которые решают всё",
    "Любое касание описывается пятью полями. Заполнил — знаешь, о чём пост, зачем он и чем закрывается. Это ядро метода. Сохрани страницу.")
  + '<div class="tri">'
    '<div class="r"><b>1 · Состояние</b><p>Что человек думает и чувствует ЗДЕСЬ. От первого лица.</p></div>'
    '<div class="r"><b>2 · Трение</b><p>Что конкретно мешает сделать следующий шаг.</p></div>'
    '<div class="r"><b>3 · Сдвиг</b><p>Что он должен понять, чтобы двинуться дальше.</p></div>'
    '<div class="r"><b>4 · Доказательство</b><p>Чем ты подтвердишь сдвиг: демонстрация, кейс, до–после.</p></div>'
    '<div class="r hi"><b>5 · Действие</b><p>Один конкретный шаг, который человек делает после поста.</p></div>'
    '</div>'
  + '<p class="note">Три поля (состояние-трение-сдвиг) отвечают «о чём пост». Ещё два (доказательство-действие) — «чем закрыть и куда вести». Без последних двух касание не срабатывает.</p>'
))

# 06 · Диагностика по полям
P.append(page("Диагностика", 6,
  head("Как заполнять", "Один вопрос — одна ошибка предотвращена",
    "Каждое поле карты — это вопрос к себе. И каждое поле страхует от конкретной ошибки прогрева.")
  + '<table class="dbg"><tr><th>Поле</th><th>Вопрос</th><th>Что предотвращает</th></tr>'
    '<tr><td class="s">Состояние</td><td>Что он думает прямо сейчас?</td><td>Пост «в никуда», без адресата</td></tr>'
    '<tr><td class="s">Трение</td><td>Что мешает шагнуть?</td><td>Пользу дал, а барьер не снял</td></tr>'
    '<tr><td class="s">Сдвиг</td><td>Что должно измениться в голове?</td><td>Пост без цели, «просто контент»</td></tr>'
    '<tr><td class="s">Доказательство</td><td>Чем докажу?</td><td>Голословность, «поверьте мне»</td></tr>'
    '<tr><td class="s">Действие</td><td>Что он сделает?</td><td>Прочитал — и ничего не сделал</td></tr>'
    '</table>'
  + '<p class="note"><b>Правило формулировки:</b> состояние и трение пиши от первого лица, как человек думает про себя («у меня всё равно не выйдет»), а не ярлыками («низкая мотивация»). Ярлык не подскажет, что писать. Живая фраза — подскажет.</p>'
))

# 07 · Мост 4 касаний (recap)
P.append(page("Мост 4 касаний", 7,
  head("Куда ведёт карта", "Четыре касания — четыре сдвига",
    "Лид-магнит не продаёт. Он открывает мост из 4 касаний. На каждом заполняешь свою карту состояний; цель касания — сделать один сдвиг.")
  + '<div class="stack">'
    '<div class="r"><span class="n">01</span><span class="lb">Знакомство</span><span class="io">чужой → свой</span></div>'
    '<div class="r"><span class="n">02</span><span class="lb">Микро-результат</span><span class="io">скептик → «получилось»</span></div>'
    '<div class="r"><span class="n">03</span><span class="lb">Доказательство</span><span class="io">сомнение → доверие</span></div>'
    '<div class="r"><span class="n">04</span><span class="lb">Предложение</span><span class="io">интерес → действие</span></div>'
    '</div>'
  + '<p class="note">Порядок не тасуется: доказательство и микро-результат идут ДО предложения. Иначе просишь купить того, кто ещё не поверил. Дальше — стек промптов, который собирает всё это за тебя.</p>'
))

# 08 · PROMPT STACK карта (SAVE)
P.append(page("Prompt Stack · SAVE", 8,
  head("Не один мега-промпт", "Стек из 9 шагов",
    "Одна простыня текста не научит управлять моделью. Стек учит: каждый промпт делает одну работу, а его выход — вход следующего. Сохрани карту.")
  + '<div class="stack">'
    '<div class="r"><span class="n">1</span><span class="lb">Диагноз состояния</span><span class="io">→ состояние</span></div>'
    '<div class="r"><span class="n">2</span><span class="lb">Трение</span><span class="io">состояние → барьеры</span></div>'
    '<div class="r"><span class="n">3</span><span class="lb">Убеждения / возражения</span><span class="io">трение → что мешает верить</span></div>'
    '<div class="r"><span class="n">4</span><span class="lb">Доказательство</span><span class="io">убеждения → чем снять</span></div>'
    '<div class="r"><span class="n">5</span><span class="lb">Последовательность</span><span class="io">карта → 4 касания</span></div>'
    '<div class="r gen"><span class="n">6</span><span class="lb">Генерация постов</span><span class="io">карта → 4 поста</span></div>'
    '<div class="r"><span class="n">7</span><span class="lb">Red team (разнести)</span><span class="io">посты → претензии</span></div>'
    '<div class="r"><span class="n">8</span><span class="lb">Humanize (живой язык)</span><span class="io">посты → без AI-языка</span></div>'
    '<div class="r"><span class="n">9</span><span class="lb">Score (оценка)</span><span class="io">серия → баллы + правки</span></div>'
    '</div>'
  + '<p class="note">Шаги 1–5 — диагностика (думаешь ты, Claude помогает). Шаг 6 — генерация. Шаги 7–9 — контроль качества. Большинство пропускает 1–5 и 7–9. Там и теряется результат.</p>'
))

# 09 · Легенда промпт-страниц
P.append(page("Как читать дальше", 9,
  head("Легенда", "Каждый промпт — маленький урок",
    "Дальше девять страниц устроены одинаково. Не просто «вот команда» — а как её применять и как чинить.")
  + rec(1, "Вход / Выход", "Что подать в промпт и что должно получиться. Выход одного шага — вход следующего.")
  + rec(2, "Почему работает", "Механизм: за счёт чего этот промпт сильнее обычной просьбы.")
  + rec(3, "Хороший ответ / Красные флаги", "Как отличить сильный результат от слабого прямо на месте.")
  + rec(4, "Как дожать · follow-up", "Готовая до-команда, если Claude ответил слабо. Копируешь и отправляешь следом.")
  + '<p class="note">Запускай промпты подряд в одном чате Claude — он помнит контекст, и каждый шаг опирается на предыдущий.</p>'
))

# 10–18 · PROMPT STACK (9)
P.append(promptpage("Промпт 1 · Диагноз", 10, "Шаг 1", "Состояние аудитории",
  "Магнит, аудитория, продукт.", "3–5 фраз от первого лица: что человек думает после скачивания.",
  "модель не угадывает читателя — ты заставляешь её сначала описать его, а не сразу продавать.",
  "Промпт · Claude",
  "Ты — стратег контент-воронки, не копирайтер.\n"
  "Контекст: лид-магнит — [ЧТО]. Аудитория — [КТО]. Продукт — [ЧТО ПРОДАЮ].\n"
  "Опиши состояние человека СРАЗУ после скачивания магнита.\n"
  "От первого лица, 3–5 фраз: что думает, чего ждёт, чего боится.\n"
  "Не пиши посты и не давай советов — только состояние.\n"
  "Если данных мало — сначала задай мне уточняющие вопросы.",
  "Живые фразы с сомнением: «ну скачал, а дальше-то что».",
  "Ярлыки «хочет расти», «нуждается в контенте» — это не состояние.",
  "Убери всё, что звучит как из презентации. Оставь то, что человек реально думает про себя."))

P.append(promptpage("Промпт 2 · Трение", 11, "Шаг 2", "Настоящий барьер",
  "Состояние из шага 1.", "3 главных трения, отсортированы по силе.",
  "«мало мотивации» — не барьер, а отговорка. Промпт требует назвать конкретную преграду, которую можно снять постом.",
  "Промпт · Claude",
  "Возьми состояние из прошлого ответа.\n"
  "Найди ТРЕНИЕ — что конкретно мешает сделать следующий шаг.\n"
  "Не «мало мотивации», а точный барьер: страх, недоверие,\n"
  "непонимание, прошлый неудачный опыт, цена, «не для меня».\n"
  "Дай 3 главных трения, отсортируй по силе. По каждому —\n"
  "одна фраза, как оно звучит в голове человека.",
  "Барьеры разные и конкретные, каждый можно закрыть отдельным постом.",
  "Все три про одно и то же, или общие слова без «как звучит в голове».",
  "Первое трение слишком общее. Разбей его на 2 конкретных и покажи, как каждое звучит от первого лица."))

P.append(promptpage("Промпт 3 · Убеждения", 12, "Шаг 3", "Что мешает поверить",
  "Трения из шага 2.", "Список: возражение → что за ним → новое убеждение.",
  "за возражением «дорого» почти всегда стоит другое — «не верю, что сработает у меня». Промпт вскрывает настоящую причину.",
  "Промпт · Claude",
  "На основе трений выпиши убеждения, мешающие купить [ПРОДУКТ].\n"
  "Для каждого дай: (1) как звучит возражение вслух;\n"
  "(2) что на самом деле стоит за ним; (3) какое НОВОЕ убеждение\n"
  "должно прийти на замену.\n"
  "Отдели реальные возражения от отговорок.",
  "Видна разница между «что говорят» и «что думают»; новое убеждение конкретное.",
  "Возражения переписаны как рекламные тезисы; «отговорки» не отделены.",
  "По каждому возражению честно ответь: это настоящая причина или прикрытие? Оставь только настоящие."))

P.append(promptpage("Промпт 4 · Доказательство", 13, "Шаг 4", "Чем снять сомнение",
  "Новые убеждения из шага 3.", "Под каждое убеждение — тип доказательства, что у тебя есть.",
  "убеждение без доказательства — пустой лозунг. Промпт привязывает каждый сдвиг к конкретному пруфу и честно метит, где пруфа нет.",
  "Промпт · Claude",
  "Для каждого нового убеждения подбери, ЧЕМ его доказать:\n"
  "демонстрация на глазах / кейс / до–после / разбор / скрин\n"
  "процесса. Только те доказательства, что у меня реально есть\n"
  "или могу собрать. Если доказательства нет — так и напиши,\n"
  "тогда убеждение слабое. Без выдуманных цифр и кейсов.",
  "Каждое убеждение подкреплено реальным, доступным тебе пруфом.",
  "Придуманные цифры/кейсы, «клиент заработал X» — стоп, это ложь.",
  "Убери всё, чего у меня нет. Где доказательства не хватает — предложи, что я могу быстро снять/показать."))

P.append(promptpage("Промпт 5 · Последовательность", 14, "Шаг 5", "Порядок 4 касаний",
  "Вся карта (шаги 1–4).", "Таблица: касание → трение → сдвиг → доказательство. Остановка.",
  "порядок решает: доказательство до микро-результата — не поверят, оффер первым — отпугнёт. Остановка «жди ок» даёт тебе выверить карту до генерации.",
  "Промпт · Claude",
  "Собери мост из 4 касаний под мою карту:\n"
  "1 знакомство (чужой→свой) · 2 микро-результат (скептик→получилось)\n"
  "· 3 доказательство (сомнение→доверие) · 4 предложение (интерес→действие).\n"
  "Для каждого касания: какое трение закрывает, какой сдвиг\n"
  "делает, какое доказательство несёт. Проверь порядок.\n"
  "Покажи таблицей. Остановись и жди моё «ок».",
  "Каждое касание закрывает своё трение; порядок логичен; Claude ждёт.",
  "Два касания про одно; предложение стоит раньше доказательства.",
  "Касания 2 и 3 дублируют друг друга. Разведи: во 2 — своя маленькая победа, в 3 — чужой результат."))

P.append(promptpage("Промпт 6 · Генерация", 15, "Шаг 6", "Посты по карте",
  "Выверенная карта + твои факты.", "4 поста, по одному на касание.",
  "теперь у модели есть всё: адресат, барьер, сдвиг, пруф. Она не сочиняет — она собирает по твоей карте.",
  "Промпт · Claude",
  "После «ок» напиши 4 поста, по одному на касание.\n"
  "Каждый: хук первой строки → одна мысль → пример/доказательство\n"
  "→ один мягкий CTA. Пост закрывает ТРЕНИЕ своего касания и\n"
  "делает СДВИГ. Каждый следующий продолжает предыдущий.\n"
  "800–1200 знаков. Мои факты: [ВСТАВЬ]. " + VOICE,
  "Каждый пост узнаётся по своему сдвигу; факты — твои.",
  "Посты можно поменять местами и ничего не изменится — значит, сдвигов нет.",
  "Пост 4 продаёт слишком рано. Оставь предложение только в нём, а из 1–3 убери любой намёк на продажу."))

P.append(promptpage("Промпт 7 · Red team", 16, "Шаг 7", "Разнести свой результат",
  "4 поста из шага 6.", "По каждому посту — 2–3 претензии и что вырезать.",
  "автор себя не критикует. Промпт заставляет Claude сменить роль на скептика и найти слабые места до того, как их увидит аудитория.",
  "Промпт · Claude",
  "Стань скептиком, который НЕ верит автору.\n"
  "Разнеси каждый из 4 постов: где звучит как реклама, где\n"
  "голословно, где банально, где давление, где человек не поймёт\n"
  "следующий шаг. По каждому — 2–3 конкретные претензии и что\n"
  "вырезать. Не будь вежливым.",
  "Претензии предметные, с указанием строк; есть что вырезать.",
  "«В целом хорошо, но можно лучше» — это не red team.",
  "Ты слишком мягок. Представь, что тебе платят за то, чтобы порвать этот текст. Ещё раз, жёстче."))

P.append(promptpage("Промпт 8 · Humanize", 17, "Шаг 8", "Убрать AI-язык",
  "Посты после правок red team.", "Те же посты живой человеческой речью.",
  "модель по умолчанию пишет ровно и мёртво. Промпт с тестом «сказал бы вслух?» вычищает канцелярит, не трогая смысл.",
  "Промпт · Claude",
  "Перепиши посты живой речью. Убери канцелярит и AI-язык:\n"
  "«важно понимать», «данный подход», «эффективно», «в современном\n"
  "мире», «таким образом», «позволяет». Короткие фразы, разная\n"
  "длина, сильное начало. Проверка каждой фразы: автор сказал бы\n"
  "так вслух? Нет — переписать. Смысл не упрощай, упрощай объяснение.",
  "Читается как речь живого человека; ни одной штампованной связки.",
  "Стало проще по смыслу или потерялась конкретика — перебор.",
  "Абзац 2 всё ещё звучит как статья. Перепиши так, будто объясняешь другу за столом."))

P.append(promptpage("Промпт 9 · Score", 18, "Шаг 9", "Оценить и дожать",
  "Финальная серия.", "Баллы по критериям + что чинить, где < 8.",
  "без внешней оценки правишь вслепую. Промпт даёт чек-лист и указывает слабые посты по именам — ты чинишь точечно.",
  "Промпт · Claude",
  "Оцени серию 0–10 по каждому: хук; одна мысль на пост; закрывает\n"
  "трение; делает сдвиг; есть доказательство; CTA не давит; живой\n"
  "язык; посты связаны между собой.\n"
  "Где < 8 — назови пост и что чинить. Ничего не хвали без причины.",
  "Честные баллы, конкретные правки по слабым постам.",
  "Все девятки без замечаний — Claude льстит, попроси строже.",
  "Ты завысил. Оцени как редактор, которому не понравилось. Где реально < 8?"))

# 19 · DEBUGGING (SAVE)
P.append(page("Prompt Debugging · SAVE", 19,
  head("Когда вышла ерунда", "Симптом → причина → что изменить",
    "Промпт дал слабый ответ — это не тупик, а сигнал. Найди симптом и дожми. Сохрани страницу — пригодится каждый раз.")
  + '<table class="dbg"><tr><th>Симптом</th><th>Почему так</th><th>Что изменить · follow-up</th></tr>'
    '<tr><td class="s">Слишком общо</td><td>Нет данных о человеке</td><td class="f">Дай состояние и трение из шагов 1–2, попроси переписать под них</td></tr>'
    '<tr><td class="s">Слишком рекламно</td><td>Просил «продающий» без карты</td><td class="f">«Убери продажу из постов 1–3, предложение только в 4-м»</td></tr>'
    '<tr><td class="s">Повторяет очевидное</td><td>Нет доказательства/механизма</td><td class="f">«Добавь конкретику: что именно, как, с деталью»</td></tr>'
    '<tr><td class="s">Не чувствует аудиторию</td><td>ЦА слишком широкая</td><td class="f">«Пиши для одного человека: [имя, ситуация]»</td></tr>'
    '<tr><td class="s">Придумывает факты</td><td>Не задал ограничение</td><td class="f">«Без выдуманных цифр. Где данных нет — так и напиши»</td></tr>'
    '<tr><td class="s">Канцелярит</td><td>Не задал голос</td><td class="f">Запусти шаг 8 · Humanize</td></tr>'
    '<tr><td class="s">Все посты одинаковые</td><td>Нет разных сдвигов</td><td class="f">«Каждый пост — свой сдвиг из карты, не повторяй мысль»</td></tr>'
    '<tr><td class="s">CTA давит</td><td>Давление по умолчанию</td><td class="f">«Замени на один спокойный шаг, без "успей" и дефицита»</td></tr>'
    '</table>'
))

# 20–22 · BEFORE/AFTER
def ba_page(section, num, title, lead, inp, badp, bado, diag, betterp, bettero, why):
    return page(section, num, head("Разбор", title, lead)
      + f'<div class="ba"><div class="lbl n">Вход</div><div class="box good">{inp}</div>'
      + f'<div class="lbl bad">Плохой промпт</div><div class="box mono">{badp}</div>'
      + f'<div class="lbl bad">Что выдал</div><div class="box bad">{bado}</div>'
      + f'<div class="lbl n">Диагноз</div><div class="box diag">{diag}</div>'
      + f'<div class="lbl good">Промпт по карте</div><div class="box mono">{betterp}</div>'
      + f'<div class="lbl good">Что выдал</div><div class="box good">{bettero}</div>'
      + f'<p class="note"><b>Почему сработало:</b> {why}</p></div>')

P.append(ba_page("Before / After · 1", 20, "«Напиши прогрев» против карты",
  "Классика: команда без входных данных.",
  "Магнит «7 промптов для reels», аудитория — новички без опыта в ИИ.",
  "Ты эксперт по маркетингу. Напиши 4 прогревающих поста для моей аудитории.",
  "«Друзья! Сегодня поговорим о важности контента. Нейросети открывают безграничные возможности. Важно понимать, что каждый может…» — гладко, ни для кого, сразу общие слова.",
  "Нет адресата и трения. Модель заполнила пустоту штампами. Продажа идей началась с первой строки.",
  "Шаг 1: опиши состояние новичка после скачивания «7 промптов». Затем шаги 2→5, потом посты.",
  "«Скачал 7 промптов — и завис на первом. Знакомо? Первый промпт вообще не про сложные настройки…» — пост 2 бьёт в «у меня не выйдет» и даёт маленькую победу.",
  "текст вырос из состояния «боюсь, что сложно», а не из пустоты. Он узнаётся и двигает."))

P.append(ba_page("Before / After · 2", 21, "Возражение «дорого» — не про деньги",
  "Прямая продажа поверх сомнения.",
  "Тёплая аудитория, продукт — курс. Многие «think about it».",
  "Напиши пост, который закроет возражение «дорого» и продаст курс.",
  "«Наш курс стоит своих денег! Инвестиция в себя окупается. Не откладывай — начни зарабатывать на нейросетях уже сегодня!» — давление и лозунги.",
  "«Дорого» здесь — прикрытие. Настоящее трение: «не верю, что у меня выйдет». Промпт бил не в ту причину.",
  "Шаг 3: раздели возражение «дорого» на настоящее и отговорку. Шаг 4: подбери доказательство под настоящее.",
  "«Дело почти никогда не в цене. Дело в мысли „у меня не получится, как у него“. Поэтому покажу процесс целиком — собери ролик по шагам вместе со мной, бесплатно…» — снимает настоящий барьер.",
  "закрыли реальное убеждение доказательством (демонстрация), а не давили на кошелёк."))

P.append(ba_page("Before / After · 3", 22, "Один пост — четыре действия",
  "CTA, который просит всё сразу.",
  "Финальный пост серии, продукт — курс.",
  "Заверши серию сильным призывом к действию.",
  "«Подписывайся, ставь лайк, сохраняй, переходи по ссылке и покупай курс со скидкой, пока не поздно!» — пять действий, паника.",
  "Пять CTA = ноль CTA. Человек не выбирает — он закрывает. И дефицит выглядит фальшиво.",
  "Debugging: «CTA давит» → один спокойный шаг. Плюс шаг 8 · Humanize.",
  "«Если хочешь собрать такой конвейер под себя — вся система на курсе, по шагам. Ссылка в профиле, посмотри программу и реши сам.» — один шаг, без давления.",
  "одно действие снимает выбор-паралич; спокойный тон конвертирует тёплых лучше срочности."))

# 23 · Практическое задание
P.append(page("Практика", 23,
  head("Собери свою серию", "8 шагов до готового артефакта",
    "Не «подумай об аудитории», а сделай. Открой Claude, держи под рукой карту (стр. 5) и стек (стр. 8). На выходе — 4 поста, а не идея.")
  + act("Делай по порядку", [
      "Впиши в шаг 1 свой магнит, аудиторию, продукт — запусти. Получи состояние.",
      "Запусти шаги 2, 3, 4 подряд — в одном чате. Собери трение, убеждения, доказательства.",
      "Шаг 5 — получи таблицу-карту. <b>Останови Claude</b> и выверь её руками (стр. 24).",
      "Напиши «ок» и запусти шаг 6 — 4 поста.",
      "Шаг 7 — red team. Внеси правки, которые согласен принять.",
      "Шаг 8 — humanize. Прочитай вслух: звучит как ты?",
      "Шаг 9 — score. Почини посты с оценкой ниже 8.",
      "Поставь в план: 4 поста, по одному в день. <em>Серия готова.</em>",
    ])
  + '<div class="result"><div class="h">Твой артефакт</div><p>Заполненная карта + 4 поста, выверенные red team, humanize и score. Это не конспект урока — это контент, который завтра идёт в канал.</p></div>'
))

# 24 · Бланк
P.append(page("Бланк · карта", 24,
  head("Заполни под себя", "Карта состояний на 4 касания",
    "Пять полей на каждое касание. Заполнил после шага 5 — отдавай в шаг 6.")
  + '<div class="blank">'
    + "".join(
      f'<div class="row"><div class="h"><i>{nm}</i> · {lb} <span style="color:var(--muted);font-weight:600">({sh})</span></div>'
      '<div class="ln"></div><div class="ln"></div></div>'
      for nm, lb, sh in [("01","Знакомство","чужой→свой"),("02","Микро-результат","скептик→получилось"),
                         ("03","Доказательство","сомнение→доверие"),("04","Предложение","интерес→действие")])
    + '</div>'
  + '<p class="note">В каждом блоке держи все пять полей: состояние · трение · сдвиг · доказательство · <span style="color:var(--o);font-weight:700">действие</span>.</p>'
))

# 25 · Checklist (SAVE)
P.append(page("Чек-лист · SAVE", 25,
  head("Контроль качества", "Перед публикацией серии")
  + '<div class="callout check"><div class="h">Карта и серия</div>'
    '<div class="row">По каждому касанию заполнены все 5 полей карты</div>'
    '<div class="row">Состояние и трение — от первого лица, а не ярлыками</div>'
    '<div class="row">Каждый пост закрывает своё трение и делает один сдвиг</div>'
    '<div class="row">Под каждый сдвиг есть реальное доказательство (без выдумок)</div>'
    '<div class="row">Порядок: микро-результат и доказательство ДО предложения</div>'
    '<div class="row">Прогнал red team, humanize и score — правки внесены</div>'
    '<div class="row">У каждого поста один спокойный CTA, без «успей»</div>'
    '</div>'
  + '<p class="note">Если хоть один пункт пустой — серия не готова. Это и есть разница между «попросил нейросеть» и «управляю нейросетью».</p>'
))

# 26 · MASTER WORKFLOW (SAVE)
P.append(page("Master Workflow · SAVE", 26,
  head("Весь процесс", "Одна страница — от магнита до серии",
    "Сфотографируй и держи рядом. Это карта всего урока: запускаешь сверху вниз, каждый шаг кормит следующий.")
  + '<div class="wf">'
    '<div class="st"><span class="n">1</span><div><b>Диагноз</b><p>Состояние человека после магнита.</p></div></div><div class="ln"></div>'
    '<div class="st"><span class="n">2</span><div><b>Трение → Убеждения → Доказательство</b><p>Барьеры, что мешает верить, чем снять.</p></div></div><div class="ln"></div>'
    '<div class="st"><span class="n">3</span><div><b>Карта + последовательность</b><p>4 касания, выверить руками, «ок».</p></div></div><div class="ln"></div>'
    '<div class="st"><span class="n">4</span><div><b>Генерация</b><p>4 поста по карте.</p></div></div><div class="ln"></div>'
    '<div class="st"><span class="n">5</span><div><b>Red team → Humanize → Score</b><p>Разнести, оживить, оценить, починить.</p></div></div><div class="ln"></div>'
    '<div class="st"><span class="n">6</span><div><b>План</b><p>4 поста по дням → заявки.</p></div></div>'
    '</div>'
))

# 27 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:25pt;line-height:1.12;margin:18px 0 8px">Ты не прочитал урок.<br>Ты <span style="color:var(--o2)">собрал систему.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Карта состояний, стек из 9 промптов и готовая серия — теперь это твой рабочий процесс. Всей системе — от упаковки до прогрева и продаж — учим на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Карта состояний · mini-course · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
