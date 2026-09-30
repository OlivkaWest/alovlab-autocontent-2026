# -*- coding: utf-8 -*-
"""AlovLab · Октябрь 2026 · Методичка G01 «Промпт-помощник для работы» (дни 1-3 календаря).
По GLOBAL-METHODOLOGY-RULE: 3 главы (голосовое->сценарий, структура промпта, проверка ответа),
каждая с паспортом/методом/шагами/промптами/примером/ошибками/самопроверкой.
Запуск: python3 scripts/guide_oct_g01_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "guides" / "G01-prompt-pomoshnik"
OUT = OUTDIR / "workbook.html"

EXTRA = r"""
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.3pt;line-height:1.4;color:var(--ink);margin-top:3px;max-width:none}
.fix{display:grid;gap:8px;margin:10px 0}
.fix .r{background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 13px;font-size:9.8pt;line-height:1.45;color:var(--body)}
.fix .r b{color:var(--ink)}
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:16px 19px;margin:10px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12.5pt;color:#fff;margin-bottom:6px}.team p{font-size:9.8pt;line-height:1.5;color:#cdbfa8;max-width:none}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · Промпт-помощник для работы</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None):
    r = f'<div class="ru">{ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{r}</div>')

P = []

# 01 Cover
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">Октябрь 2026 · Неделя 1, дни 1–3 · G01</div>
    <h1 style="font-weight:800;font-size:28pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:17ch">Промпт-помощник для работы</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Голосовое в сценарий. Промпт, который бьёт точно в адресата. Ответ, который проверили, а не приняли на слово.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 главы</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Копируемые шаблоны</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Честная проверка ответа</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("Г1","Голосовое → сценарий","03"),("Г1","Промпт-шаблон и пример","04"),
 ("Г2","Структура промпта: роль-контекст-ограничения-формат","05"),("Г2","Разбор до/после","06"),
 ("Г3","Как проверить ответ ИИ","07"),("Г3","Три проверки на практике","08"),
 ("—","Частые ошибки всех трёх глав","09"),("—","Сделай сейчас + самопроверка","10"),
 ("—","Источники и статус проверки","11"),("—","Дальше — на курсе","12"),
 ("—","Путь в команду AlovLab","13"),("—","Контакты","14"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:10px;padding:6px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:9.5pt;width:26px">{a}</span>'
               f'<span style="font-weight:600;font-size:10.3pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:9.5pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Три главы, один настроенный чат</h1>'
    '<p class="lead">Дни 1–3 календаря AlovLab на октябрь: то, что превращается к концу недели в личного чат-помощника (день 7).</p>'
    f'<div style="margin-top:4px">{rows}</div>'))

# 03 Chapter 1 part 1
P.append(page("Глава 1 · Паспорт", 3,
    head("Глава 1", "Голосовое → сценарий",
         "Для кого: авторы и фрилансеры, которые объясняют голосом легче, чем пишут. Результат: черновик поста из голосового сообщения за 5 минут.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Время</div><div class="ch">5–10 минут</div><p>Одно голосовое + одна расшифровка.</p></div>'
      '<div class="card"><div class="ct">Инструменты</div><div class="ch">ChatGPT + голосовое</div><p>Расшифровка голосом или вручную, дальше — в чат.</p></div>'
      '<div class="card"><div class="ct">Уровень</div><div class="ch">Базовый</div><p>Специальной подготовки не требуется.</p></div></div>'
    + '<div class="term"><b>Метод.</b> <span>Расшифровка голосового — это сырьё, не готовый текст. Задача промпта — не переписать её красиво, а собрать в структуру поста, сохранив узнаваемые формулировки автора.</span></div>'))

# 04 Chapter 1 part 2 - prompt + example
P.append(page("Глава 1 · Промпт", 4,
    prompt("ШАБЛОН · СКОПИРОВАТЬ",
           "Вот расшифровка моего голосового сообщения: [вставить текст расшифровки].\nСобери из неё сценарий поста: хук в первой строке, основная мысль, один пример, один призыв.\nСохрани мои формулировки и порядок мыслей, где это возможно. Не заменяй мою речь на гладкий обобщённый текст.\nЕсли где-то мысль оборвана — оставь пометку [уточнить], не додумывай за меня.")
    + '<div class="io"><div class="c"><b>Что вставить</b><p>Сырая расшифровка голосового, без правок.</p></div>'
      '<div class="c out"><b>Что получить</b><p>Структурированный черновик поста, узнаваемый по формулировкам как твой.</p></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div><p>Черновик, который не стыдно узнать своим — не отредактированная нейросетью версия, а твоя мысль в порядке.</p></div>'))

# 05 Chapter 2 part 1
P.append(page("Глава 2 · Структура", 5,
    head("Глава 2", "Структура промпта: роль, контекст, ограничения, формат",
         "Для кого: те, кто пишет клиентам/партнёрам через ИИ. Результат: свой промпт-каркас для повторяющейся переписки.")
    + '<table class="ref"><tr><th>Часть</th><th>Вопрос, на который отвечает</th><th>Пример</th></tr>'
      '<tr><td><b>Роль</b></td><td>Кто ты в этой задаче?</td><td>«Я фрилансер-дизайнер, пишу владельцу кофейни»</td></tr>'
      '<tr><td><b>Контекст</b></td><td>Что адресат уже знает, а что нет?</td><td>«Видел работы в Instagram, не знает цен»</td></tr>'
      '<tr><td><b>Ограничения</b></td><td>Что нельзя?</td><td>«Не длиннее 150 слов, без канцелярита»</td></tr>'
      '<tr><td><b>Формат</b></td><td>Как должен выглядеть результат?</td><td>«3 абзаца + один следующий шаг»</td></tr></table>'
    + '<p class="note">Убери любую из четырёх частей — и ответ снова станет обобщённым, годным всем и никому.</p>'))

# 06 Chapter 2 do/before-after
P.append(page("Глава 2 · До/После", 6,
    prompt("ШАБЛОН · СКОПИРОВАТЬ",
           "Я [роль], пишу [кому и зачем].\n[Что адресат уже знает / не знает].\n[Ограничения по длине/тону/что не упоминать].\nФормат: [структура результата].")
    + '<div class="gb"><div class="box bad"><div class="lbl">Без структуры</div>«Напиши предложение клиенту» — обобщённый текст, годится любому бизнесу.</div>'
      '<div class="box good"><div class="lbl">Со структурой</div>Роль+контекст+ограничения+формат — текст с деталями именно этого клиента, готовый к отправке.</div></div>'
    + '<p class="note">Заполни шаблон под свою самую частую рабочую переписку — используешь его не один раз, а как каркас.</p>'))

# 07 Chapter 3 part 1
P.append(page("Глава 3 · Проверка", 7,
    head("Глава 3", "Как проверить ответ ИИ",
         "Для кого: любой, кто использует ответы ИИ в реальной работе. Результат: привычка проверять перед использованием.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Проверка 1</div><div class="ch">Первоисточник</div><p>Если он есть — открой сам, не верь пересказу.</p></div>'
      '<div class="card"><div class="ct">Проверка 2</div><div class="ch">Одно утверждение</div><p>Возьми конкретную фразу, проверь именно её.</p></div>'
      '<div class="card"><div class="ct">Проверка 3</div><div class="ch">Цифры отдельно</div><p>Независимо от текста, по другому источнику.</p></div></div>'
    + '<div class="warn"><div class="h">Так нельзя</div><ul><li>Переспросить ту же модель тем же или другими словами — это тот же источник, не проверка.</li><li>Требовать от модели показать «скрытые рассуждения» как доказательство — для проверки достаточно проверяемых шагов и источника, не внутреннего хода модели.</li></ul></div>'))

# 08 Chapter 3 practice
P.append(page("Глава 3 · На практике", 8,
    prompt("ЧЕК-ЛИСТ ПРОВЕРКИ · СКОПИРОВАТЬ",
           "Перед тем как использовать этот ответ:\n1) Есть ли первоисточник? Открыл его сам?\n2) Какое одно утверждение здесь ключевое? Проверил его отдельно?\n3) Есть ли цифры? Сверил их с независимым источником?\nЕсли хотя бы один пункт не выполнен — не использую ответ как факт, использую как черновик.")
    + '<div class="io"><div class="c"><b>Пример без проверки</b><p>Ответ с цифрой звучит уверенно — отправлен клиенту как факт.</p></div>'
      '<div class="c out"><b>Пример с проверкой</b><p>Та же цифра сверена с источником — либо подтверждена, либо скорректирована до отправки.</p></div></div>'))

# 09 errors combined
P.append(page("Ошибки · Все 3 главы", 9,
    head("Ошибки", "Частые ошибки трёх глав",
         "По одной характерной ошибке на главу.")
    + '<div class="fix">'
      '<div class="r"><b>Глава 1.</b> Просишь «сделай красиво» вместо «сохрани мою речь» — получаешь гладкий обобщённый текст вместо своего голоса.</div>'
      '<div class="r"><b>Глава 2.</b> Указываешь только роль без контекста и ограничений — ответ всё ещё обобщённый, просто с претензией на экспертность.</div>'
      '<div class="r"><b>Глава 3.</b> Переспрашиваешь ту же модель вместо независимой проверки — получаешь ту же уверенность, не больше фактической точности.</div></div>'))

# 10 action + selfcheck
P.append(page("Сделай сейчас", 10,
    head("Действие", "Сделай сейчас",
         "Один вечер — три готовых элемента личного помощника.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Возьми реальное голосовое</b> себе клиенту/партнёру, преврати в черновик по шаблону главы 1.</div></div>'
      '<div class="step"><div class="sx"><b>Собери свой промпт-каркас</b> по формуле главы 2 под самую частую переписку.</div></div>'
      '<div class="step"><div class="sx"><b>Прогони любой рабочий ответ ИИ</b> через три проверки главы 3.</div></div></div>'
    + '<div class="callout check"><div class="h">Самопроверка</div>'
      '<div class="row">Черновик из голосового звучит как я, не как нейросеть.</div>'
      '<div class="row">Промпт-каркас заполнен под конкретную свою переписку, не абстрактно.</div>'
      '<div class="row">Хотя бы один ответ прошёл все три проверки перед использованием.</div></div>'))

# 11 sources
P.append(page("Источники", 11,
    head("Источники", "Статус проверки",
         "Честно про то, что проверено, а что нет.")
    + '<div class="warn"><div class="h">Статус</div><ul>'
      '<li>Методология глав — общий принцип промпт-инжиниринга, не привязан к версии продукта.</li>'
      '<li>Конкретные названия пунктов интерфейса для расшифровки голосовых — не проверялись напрямую, использовать любой доступный способ расшифровки.</li>'
      '<li>Оба примера (главы 1 и 2) — учебные, не результат реального клиентского проекта.</li></ul></div>'))

# 12 course
P.append(page("Дальше", 12,
    head("Дальше", "Модуль «Земля Слов» на курсе",
         "Эти три главы — ровно то, с чего начинается модуль «Земля Слов» курса «Нейросети и ChatGPT для каждого».")
    + '<p>6 видеоуроков, 6 направлений (Слова, Изображения, Видео, Звук, Аватары, Знания). Специальных технических предпосылок для старта сайт не заявляет.</p>'
    + '<div class="warn"><div class="h">Честно про цену</div><ul><li>Тарифы на октябрь не переподтверждены вживую (сетевой доступ к сайту заблокирован в этой сессии) — цену здесь не называем, проверь на alovlab.ru перед публикацией любого материала с ценой.</li></ul></div>'))

# 13 team
P.append(page("Команда", 13,
    head("Путь дальше", "Путь в команду AlovLab",
         "Если промпт-помощники — то, что тебе реально нравится собирать, есть куда расти.")
    + '<div class="team"><div class="h">Уверенно собираешь промпт-системы?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты под задачи брендов, набивают портфолио на живых кейсах.</p>'
      '<div class="dirs"><span>Промпт-системы</span><span>Контент-ассистенты</span><span>Автоматизация переписки</span></div>'
      '<p style="margin-top:8px">Это практика, не обещание трудоустройства.</p></div>'))

# 14 contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Октябрь 2026</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Три главы — один настроенный чат-помощник</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Дальше — методичка G02 (дни 4-7): что нельзя вставлять в чат, формат ответа, и сборка всего в помощника.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))
