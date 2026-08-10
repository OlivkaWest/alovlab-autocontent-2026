# -*- coding: utf-8 -*-
"""AlovLab · рабочая тетрадь «Связка недели» (День 7).
Одна идея → семь ролей на неделю + лист самооценки недели 1. Пример — ниша ИИ/контент.
Премиум фикс-A4, светлая основа, тёмные плашки под промпты. База CSS — v2.
Запуск: python3 scripts/guide_svyazka_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "svyazka-nedeli"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-svyazka-nedeli.html"

EXTRA = r"""
.lede2{font-size:12pt;line-height:1.6;color:var(--muted);margin:6px 0 14px;max-width:62ch}
.roles{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:12px 0}
.role{background:#fff;border:1px solid var(--line);border-radius:12px;padding:13px 15px}
.role .rt{display:flex;align-items:baseline;gap:8px;margin-bottom:4px}
.role .rt b{font-weight:800;font-size:12pt;color:var(--ink)}
.role .rt .x{font-weight:800;font-size:8pt;color:var(--o);background:var(--o-tint);padding:3px 8px;border-radius:20px}
.role p{font-size:9.6pt;line-height:1.45;color:var(--muted);margin:0;max-width:none}
.fields{margin:10px 0}
.fld{display:flex;align-items:baseline;gap:8px;padding:8px 0;border-bottom:1px solid var(--line2)}
.fld .k{font-weight:700;font-size:10pt;color:var(--ink);white-space:nowrap}
.fld .ln{flex:1;border-bottom:1px dotted var(--faint);height:1px;margin-bottom:3px}
.selfrow{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 13px;margin:7px 0;font-size:10pt;line-height:1.4;color:var(--ink)}
.selfrow .q{font-weight:700}
.selfrow .ln{display:block;border-bottom:1px dotted var(--faint);height:12px;margin-top:6px}
.emptytbl td{height:26px}
"""
CSS = V2CSS + EXTRA

FOOTLABEL = "AlovLab · День 7 · связка недели"
def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>{FOOTLABEL}</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code):
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code></div>')

P = []

# P1 · Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 72% at 84% 10%,#2c2114,#170f08 54%,#0c0a07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · рабочая тетрадь · День 7</div>
    <h1 style="font-weight:800;font-size:34pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Связка недели: одна идея — <span style="color:var(--o2)">семь дней.</span></h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:40ch">Берёшь одну сильную идею и задаёшь ей семь ролей на неделю. Ноль паники по утрам «о чём сегодня».</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Шаблон недели</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Готовый пример</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Лист самооценки недели&nbsp;1</span>
    </div>
  </div>
</section>""")

# P2 · Что соберёшь
P.append(page("Результат дня", 2, """
  <span class="kick">Результат дня</span>
  <h2>Что ты соберёшь</h2>
  <p class="lede2">Одну связку на неделю: одну сильную идею, разложенную на семь дней контента. Плюс лист самооценки — где ты по итогам первой недели и что забрать во вторую.</p>
  <div class="flow">
    <div class="node"><b>Идея</b><span>одна мысль</span></div><div class="arr">→</div>
    <div class="node"><b>7 ролей</b><span>под неделю</span></div><div class="arr">→</div>
    <div class="node"><b>Неделя</b><span>таблица дней</span></div><div class="arr">→</div>
    <div class="node"><b>Самооценка</b><span>итог недели 1</span></div>
  </div>
  <div class="term"><b>Связка</b> — <span>одна идея, раскрытая с семи сторон за семь дней. Повторяемый процесс, а не семь случайных тем.</span></div>
  <div class="term"><b>Идея</b> — <span>мысль с конфликтом («что не так»), а не тема («о чём»). В ней сталкиваются две вещи.</span></div>
  <div class="term"><b>Роль</b> — <span>каким боком идея повёрнута сегодня: польза, позиция, кейс или приглашение.</span></div>
  <div class="callout result"><div class="h">Обещание</div><p>К концу — заполненная таблица недели «День · Опора · Формат · Роль · Хук» и честный лист самооценки первой недели.</p></div>
"""))

# P3 · Почему работает
P.append(page("Почему это работает", 3, """
  <span class="kick">Механика</span>
  <h2>Удача не масштабируется. Система — да</h2>
  <p class="lede2">Один пост выстрелил — и ты не смог повторить, потому что не понял, что именно сработало. Хит был случайностью. Система бьёт случайность одним — повторяемостью.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Семь случайных тем</div>Пн — про одну нейросеть, Вт — про другую, Ср — лайфхак. Между собой не связаны. Зритель не запоминает ничего, приглашение в пятницу — как реклама из ниоткуда.</div>
    <div class="box good"><div class="lbl">✓ Одна идея — семь ролей</div>Всю неделю одна мысль с разных сторон. Идея врезается, а пятничный шаг завершает то, что человек уже принял за неделю.</div>
  </div>
  <div class="callout result"><div class="h">Вывод</div><p>Связка недели — это процесс. На следующей неделе берёшь новую идею и запускаешь тот же процесс. Случайность превращается в систему.</p></div>
"""))

# P4 · Идея, а не тема
P.append(page("Идея, а не тема", 4, """
  <span class="kick">Основа</span>
  <h2>Сначала проверь: это идея или тема</h2>
  <p class="lede2">Тема отвечает на «о чём». Идея отвечает на «что не так». Если в формулировке не сталкиваются две вещи — это тема, и неделя выйдет ровной и пресной.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Тема — «о чём»</div>«Нейросети для контента». Ровно, знакомо, никого не цепляет. По ней ходят тысячи.</div>
    <div class="box good"><div class="lbl">✓ Идея — «что не так»</div>«Дело не в модели, а в связке». Есть конфликт: человек винит нейросеть, а решает система.</div>
  </div>
  <h3>Переформулируй тему в идею (ниша ИИ / контент)</h3>
  <ul>
    <li>«Как делать картинки нейросетью» → <strong>«Красиво генерит, а в серию не складывается».</strong></li>
    <li>«ИИ ускоряет контент» → <strong>«Нейросеть быстрая, а контент выходит вразнобой».</strong></li>
    <li>«Промпты для новичков» → <strong>«Пишешь длинный промпт — получаешь дёшево».</strong></li>
  </ul>
  <div class="callout result"><div class="h">Правило</div><p>В идее должно сталкиваться две вещи: усилие и отсутствие результата, ожидание и реальность, «все делают так» и «а работает иначе».</p></div>
"""))

# P5 · Семь ролей
P.append(page("Семь ролей идеи", 5, """
  <span class="kick">Система</span>
  <h2>Одна идея — семь ролей</h2>
  <p class="lede2">Одна мысль поворачивается к зрителю разными боками. Четыре опоры держат неделю; пропорция — пользы больше всего, приглашение ровно один раз.</p>
  <div class="roles">
    <div class="role"><div class="rt"><b>Польза</b><span class="x">×2 · чаще всего</span></div><p>Конкретный приём или разбор, который зритель применит сразу. Ядро недели.</p></div>
    <div class="role"><div class="rt"><b>Позиция</b><span class="x">×1</span></div><p>Взгляд эксперта: как надо и как нет. Доверие и отстройка.</p></div>
    <div class="role"><div class="rt"><b>Кейс</b><span class="x">×1</span></div><p>Что реально вышло в работе — с деталью, без выдуманных цифр. Доказательство.</p></div>
    <div class="role"><div class="rt"><b>Приглашение</b><span class="x">×1 · один раз</span></div><p>Мягкий шаг к продукту. Завершает мысль, а не давит.</p></div>
  </div>
  <div class="callout check"><div class="h">Пропорция здоровой недели · 2 : 1 : 1 : 1</div>
    <div class="row">Пользы — больше всего (минимум два дня с конкретным приёмом)</div>
    <div class="row">Позиция и кейс — по одному дню</div>
    <div class="row">Приглашение — ровно один раз за неделю, не чаще</div>
  </div>
"""))

# P6 · Пошагово
P.append(page("Пошагово", 6, """
  <span class="kick">Инструкция</span>
  <h2>Как собрать связку за один вечер</h2>
  <div class="steps">
    <div class="step"><div class="sx"><b>Выбери одну идею недели</b> — с конфликтом, которая цепляет тебя самого. Запиши одной строкой.</div></div>
    <div class="step"><div class="sx"><b>Проверь, что это идея, а не тема</b> — есть ли в ней столкновение двух вещей (стр. 4).</div></div>
    <div class="step"><div class="sx"><b>Открой Claude</b> и вставь основной промпт (стр. 7), подставив нишу, аудиторию, идею и продукт.</div></div>
    <div class="step"><div class="sx"><b>Получи семь ролей идеи</b> — неделю с опорой, форматом и хуком под каждый день. Проверь пропорцию.</div></div>
    <div class="step"><div class="sx"><b>Вычеркни лишнее</b> — если под днём две мысли, оставь одну; если два дня дублируются, поменяй роль.</div></div>
    <div class="step"><div class="sx"><b>Прогони промпт улучшения</b> (стр. 8) — заостри хуки, убери дни, которые не двигают вперёд.</div></div>
    <div class="step"><div class="sx"><b>Проверь жёстким промптом</b> — где неделя разваливается на случайные посты. Исправь.</div></div>
    <div class="step"><div class="sx"><b>Заполни таблицу и лист самооценки</b> (стр. 11–12). Результат дня готов.</div></div>
  </div>
"""))

# P7 · Основной промпт
P.append(page("Промпт · Claude", 7, prompt(
  "Основной промпт · разложить идею на неделю",
  """Ты — контент-стратег. Помоги разложить одну идею на неделю контента.
Ниша: [НИША]. Аудитория: [АУДИТОРИЯ]. Продукт, к которому ведём: [ПРОДУКТ].
Идея недели (одна мысль с конфликтом): [ИДЕЯ_НЕДЕЛИ].

Собери связку на 5 рабочих дней (Пн–Пт). Все дни раскрывают ОДНУ эту идею
с разных сторон, не повторяя друг друга дословно. Роли:
- Польза — конкретный приём или разбор, который зритель применит.
- Позиция — взгляд эксперта: как надо и как нет.
- Кейс — что реально выходит в работе (без выдуманных цифр).
- Приглашение — мягкий шаг к продукту, РОВНО ОДИН раз за неделю.

Пропорция: пользы больше всего (2 дня), позиция 1, кейс 1, приглашение 1.
Для каждого дня: опора, формат (Reels / карусель / пост), роль идеи, хук до 9 слов.
Живой русский, короткие фразы, одна идея во всех днях, каждый день ведёт в Telegram.
Верни таблицей: День | Опора | Формат | Роль идеи | Хук.""") + """
  <span class="kick" style="margin-top:16px;display:block">Что подставить</span>
  <div class="cards c2">
    <div class="card"><div class="ct">[НИША] · [ПРОДУКТ]</div><p>чем занимаешься и к чему ведёшь</p></div>
    <div class="card"><div class="ct">[ИДЕЯ_НЕДЕЛИ]</div><p>одна мысль с конфликтом, не тема</p></div>
  </div>
  <p class="note">Claude держит всю неделю разом и не теряет исходную идею на седьмом дне. Тот же промпт работает в ChatGPT.</p>
"""))

# P8 · Промпты доводки
_p8a = prompt("Улучшение · заострить",
  "Вот моя связка на неделю: [ВСТАВИТЬ]. Усиль её: заостри хук каждого дня (до 9 слов, без разгона); найди день, который не двигает зрителя вперёд, и дай ему настоящую роль или замени; проверь пропорцию — пользы больше всего, приглашение один раз. Покажи, что изменил и почему.")
_p8b = prompt("Жёсткая оценка · отбраковать",
  "Оцени мою неделю строго, как редактор, который её отклонит. Найди: где это семь случайных тем, а не одна идея; где день повторяет другой дословно; где приглашений больше одного; где нет пользы, только рассуждения. Скажи прямо, держится ли неделя на одной идее. Оценка 1–10 по целостности и по конкретности пользы. Неделя: [ВСТАВИТЬ].")
_p8c = prompt("Финальная проверка · да/нет",
  "Проверь связку по чек-листу, ответь да/нет: все дни раскрывают одну идею без дословных повторов; пользы больше всего, приглашение один раз; в кейсе нет выдуманных цифр; у каждого дня хук до 9 слов, который цепляет; каждый день ведёт в Telegram. Где «нет» — перепиши день. Неделя: [ВСТАВИТЬ].")
P.append(page("Промпты · доводка", 8,
  '<span class="kick">Доводка</span><h2>Заострить, отбраковать, проверить</h2>' + _p8a + _p8b + _p8c))

# P9 · Готовый пример (ниша ИИ)
P.append(page("Готовый пример", 9, """
  <span class="kick">Готовый пример · ниша ИИ / контент</span>
  <h2>Одна идея — вся неделя</h2>
  <p class="lede2">Идея недели: <span class="o">«Дело не в модели, а в связке»</span>. Ниша — наставник по нейросетям для контента, продукт — разбор рабочих связок. Аудитория — новички, у кого генерит красиво, а в серию не складывается.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Слабо · семь случайных тем</div>Пн — «5 нейросетей», Вт — «польза ИИ», Ср — «мой стек», Чт — «мифы о промптах», Пт — «купи курс». Не связаны, зритель не запоминает, приглашение из воздуха.</div>
    <div class="box good"><div class="lbl">✓ Сильно · одна идея — пять ролей</div>Всю неделю мысль «дело не в модели, а в связке» — с пяти сторон. Пятничный шаг завершает то, что человек принял за неделю.</div>
  </div>
  <table>
    <tr><th>День</th><th>Опора</th><th>Формат</th><th>Роль идеи</th><th>Хук</th></tr>
    <tr><td><b>Пн</b></td><td>Польза</td><td>Reels</td><td>связка, что даёт «дорогой» кадр</td><td>«Дело не в модели. Дело в связке.»</td></tr>
    <tr><td><b>Вт</b></td><td>Позиция</td><td>пост</td><td>винят модель, а решает система</td><td>«Не нейросеть слабая. Связка слабая.»</td></tr>
    <tr><td><b>Ср</b></td><td>Польза</td><td>карусель</td><td>разбор: Midjourney → Nano Banana</td><td>«Один рисует. Второй удерживает.»</td></tr>
    <tr><td><b>Чт</b></td><td>Кейс</td><td>Reels</td><td>обычное фото → премиум-кадр</td><td>«Тот же кадр. Другая связка.»</td></tr>
    <tr><td><b>Пт</b></td><td>Приглашение</td><td>пост</td><td>шаг на разбор связок</td><td>«Собираешь дёшево? Разберём связку.»</td></tr>
  </table>
  <p class="note">Одна мысль — пять ролей, без дословных повторов. Приглашение одно, в пятницу. В кейсе — только то, что реально было, без выдуманных цифр.</p>
"""))

# P10 · Типовые ошибки
P.append(page("Типовые ошибки", 10, """
  <span class="kick">Грабли</span>
  <h2>Шесть ошибок, которые ломают неделю</h2>
  <div class="fix">
    <div class="r"><b>Семь тем вместо одной идеи.</b> Пн про одно, Вт про другое → неделя рассыпается. Одна идея, семь ролей.</div>
    <div class="r"><b>Приглашение каждый день.</b> «Купи» в каждом посте → выглядит как реклама, отписки. Один раз за неделю.</div>
    <div class="r"><b>Только позиция, ноль пользы.</b> Всю неделю «я так считаю» → нечего применить. Минимум два дня с приёмом.</div>
    <div class="r"><b>Дни дословно повторяются.</b> Пн и Ср — одна мысль теми же словами → спам. Меняй роль, не только слова.</div>
    <div class="r"><b>Идея — это тема без конфликта.</b> «Нейросети» вместо «дело не в модели» → пресно. Столкни две вещи.</div>
    <div class="r"><b>Кейс с выдуманными цифрами.</b> «+300% охвата» → недоверие и претензии. Только то, что реально было.</div>
  </div>
"""))

# P11 · Поля тетради + таблица недели
def fld(k):
    return f'<div class="fld"><span class="k">{k}</span><span class="ln"></span></div>'
P.append(page("Рабочая тетрадь · поля", 11,
  '<span class="kick">Заполни по себе</span><h2>Поля рабочей тетради</h2>'
  '<div class="fields">' +
  fld("Моя ниша") + fld("Моя аудитория") + fld("Главная проблема аудитории") +
  fld("Идея недели (мысль с конфликтом)") + fld("Что с чем не сходится в идее") +
  fld("Что подставил в промпт") + fld("Вывод дня") +
  '</div>'
  '<span class="kick" style="display:block;margin-top:10px">Таблица недели · заполни</span>'
  '<table class="emptytbl"><tr><th>День</th><th>Опора</th><th>Формат</th><th>Роль идеи</th><th>Черновик хука</th></tr>'
  '<tr><td><b>Пн</b></td><td>Польза</td><td></td><td></td><td></td></tr>'
  '<tr><td><b>Вт</b></td><td>Позиция</td><td></td><td></td><td></td></tr>'
  '<tr><td><b>Ср</b></td><td>Польза</td><td></td><td></td><td></td></tr>'
  '<tr><td><b>Чт</b></td><td>Кейс</td><td></td><td></td><td></td></tr>'
  '<tr><td><b>Пт</b></td><td>Приглашение</td><td></td><td></td><td></td></tr></table>'))

# P12 · Лист самооценки + чек-лист
P.append(page("Самооценка недели 1", 12, """
  <span class="kick">Итог недели 1</span>
  <h2>Лист самооценки — честно, по себе</h2>
  <div class="selfrow"><span class="q">Что из недели 1 я реально усвоил<span class="ln"></span></span></div>
  <div class="selfrow"><span class="q">Где провис (день / тема)<span class="ln"></span></span></div>
  <div class="selfrow"><span class="q">Самый сильный материал недели и почему<span class="ln"></span></span></div>
  <div class="selfrow"><span class="q">Самый слабый и что с ним не так<span class="ln"></span></span></div>
  <div class="selfrow"><span class="q">Что забираю во вторую неделю<span class="ln"></span></span></div>
  <div class="callout check"><div class="h">Чек-лист готовности связки</div>
    <div class="row">Идея недели одна, и в ней есть конфликт</div>
    <div class="row">Семь ролей одной идеи, а не семь тем</div>
    <div class="row">Пропорция: пользы больше всего, приглашение один раз</div>
    <div class="row">Ни один день не повторяет другой дословно</div>
    <div class="row">В кейсе нет выдуманных цифр</div>
    <div class="row">Каждый день ведёт в Telegram за конкретным</div>
  </div>
"""))

# P13 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Случайность стала<br><span style="color:var(--o2)">системой.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:46ch;margin:0 auto 20px">Одна идея — вся неделя, без паники по утрам. Забирай шаблон связки, готовый пример и разборы рабочих связок инструментов в Telegram.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь и связки → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">VK · vk.com/alovlab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Связка недели · рабочая тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
