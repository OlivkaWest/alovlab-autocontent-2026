# -*- coding: utf-8 -*-
"""AlovLab · тетрадь «КАРТА СОСТОЯНИЙ» — премиум-PDF (фикс-A4).
Экспертная техника прогрева: перед генерацией постов Claude строит карту читателя
СОСТОЯНИЕ → ТРЕНИЕ → СДВИГ по 4 касаниям «Моста 4 касаний», и только потом пишет текст.
Диагноз, ядро «пиши переходы, не посты», карта по каждому касанию с примером, как строить,
2 промпта Claude (построить карту → написать посты), до/после, бланк карты, чек-лист.
Честность: примеры учебные, без выдуманных цифр. База CSS — v2. Запуск: python3 scripts/guide_karta_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "karta-sostoyaniy"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-karta-sostoyaniy.html"

EXTRA = r"""
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.prompt code{font-size:8.9pt}
.rec{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:8px 0;align-items:start}
.rec .n{width:22px;height:22px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}
.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:9px 0}
.pair .c{border-radius:12px;padding:11px 13px;font-size:9.6pt;line-height:1.48}
.pair .bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.pair .good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.pair .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:5px}
.pair .bad .l{color:#c56b43}.pair .good .l{color:var(--o)}
.act{margin:10px 0 4px}
.act .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:7px 0;align-items:start}
.act .s .k{width:20px;height:20px;border-radius:6px;background:#ece0cc;color:#8a6127;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;line-height:1;margin-top:1px}
.act .s p{font-size:9.6pt;line-height:1.44;color:var(--body)}
.act .s p b{color:var(--ink);font-weight:800}.act .s p em{font-style:normal;color:var(--o);font-weight:700}
.actlbl{display:block;font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin:6px 0 2px}
.ex{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o2);border-radius:11px;padding:12px 15px;margin:10px 0}
.ex .h{font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px}
.ex p{font-size:9.6pt;line-height:1.48;color:var(--ink)}.ex p+p{margin-top:6px}
/* переход состояния — плашка */
.shift{display:inline-flex;align-items:center;gap:9px;background:var(--o-tint);border:1px solid #f2d3bf;border-radius:9px;padding:6px 13px;font-weight:800;font-size:10pt;color:var(--ink);margin:2px 0 10px}
.shift i{color:var(--o);font-style:normal;font-size:12pt}
/* карта: три строки СОСТОЯНИЕ/ТРЕНИЕ/СДВИГ */
.tri{margin:8px 0}
.tri .r{display:grid;grid-template-columns:108px 1fr;gap:12px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--line)}
.tri .r:last-child{border-bottom:0}
.tri .r b{font-weight:800;font-size:8.5pt;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.tri .r p{font-size:9.8pt;line-height:1.42;color:var(--ink)}
.tri .r.sh{background:var(--o-tint);border-radius:9px;padding:9px 11px;border:0;margin-top:4px}
.tri .r.sh b{color:var(--o)}.tri .r.sh p{font-weight:700}
/* recap-таблица касаний */
.four{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.four .r{display:grid;grid-template-columns:26px 1fr auto;gap:12px;align-items:center;background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:10px;padding:10px 13px}
.four .r .n{font-weight:800;font-size:12pt;color:var(--o2)}
.four .r .lb{font-weight:800;font-size:10pt;color:var(--ink)}
.four .r .sh{font-size:9pt;color:var(--o);font-weight:700;white-space:nowrap}
/* бланк карты 4×3 */
.blank{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.blank .row{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:10px;padding:9px 12px}
.blank .row .h{font-weight:800;font-size:9pt;color:var(--ink);margin-bottom:6px}
.blank .row .h i{font-style:normal;color:var(--o)}
.blank .ln{height:1px;border-bottom:1.5px dashed var(--line2);min-height:13px;margin:6px 0}
.blank .ln.s{border-color:#e7b48f}
"""
CSS = V2CSS + EXTRA
VOICE = "[ГОЛОС] живо, короткие фразы, конкретика, без штампов и эмодзи-мусора."

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · карта состояний</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>Разбор:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def biz(txt, lbl="Пример"): return f'<div class="biz"><b>{lbl}</b>{txt}</div>'
def rec(n, t, b): return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{t}</b><p>{b}</p></div></div>'
def pair(bad, good, bl="Без карты", gl="По карте"):
    return (f'<div class="pair"><div class="c bad"><span class="l">✕ {bl}</span>{bad}</div>'
            f'<div class="c good"><span class="l">✓ {gl}</span>{good}</div></div>')
def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def act(lbl, steps):
    body = "".join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i, t in enumerate(steps, 1))
    return f'<span class="actlbl">{lbl}</span><div class="act">{body}</div>'
def ex(label, paras): return f'<div class="ex"><div class="h">{label}</div>' + "".join(f'<p>{p}</p>' for p in paras) + '</div>'
def shift(a, b): return f'<div class="shift">{a}<i>→</i>{b}</div>'
def tri(sost, tren, sdvig):
    return ('<div class="tri">'
            f'<div class="r"><b>Состояние</b><p>{sost}</p></div>'
            f'<div class="r"><b>Трение</b><p>{tren}</p></div>'
            f'<div class="r sh"><b>Сдвиг</b><p>{sdvig}</p></div></div>')

P = []

# P1 · Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · метод · прогрев</div>
    <h1 style="font-weight:800;font-size:34pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:14ch">Карта <span style="color:var(--o2)">состояний.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Почему прогрев не работает и как это чинит одна техника: сначала описываешь состояние читателя на каждом шаге, и только потом пишешь посты. С примерами и промптами для Claude.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Состояние → Трение → Сдвиг</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Герой-промпт</span>
    </div>
  </div>
</section>""")

# P2 · Что внутри
P.append(page("Что внутри", 2,
  head("Тетрадь · метод прогрева", "Пиши не посты — переходы",
    "Прогрев — это не серия постов. Это цепочка смен состояний читателя. Прежде чем писать, опиши, где человек и что ему мешает. Тогда текст попадает, а не льётся в пустоту.")
  + '<div class="flow">'
    '<div class="node"><b>Магнит</b><span>поднял руку</span></div><div class="arr">→</div>'
    '<div class="node"><b>Карта</b><span>состояний</span></div><div class="arr">→</div>'
    '<div class="node"><b>Посты</b><span>переходы</span></div><div class="arr">→</div>'
    '<div class="node"><b>Заявка</b><span>курс / бриф</span></div>'
    '</div>'
  + '<div class="term"><b>Состояние</b> — <span>что человек думает и чувствует в конкретной точке пути.</span></div>'
  + '<div class="term"><b>Трение</b> — <span>что мешает ему сделать следующий шаг прямо сейчас.</span></div>'
  + '<div class="term"><b>Сдвиг</b> — <span>что он должен понять, чтобы шагнуть дальше. Задача поста — сделать один сдвиг.</span></div>'
  + '<div class="callout result"><div class="h">Что на выходе</div><p>Заполненная карта состояний на 4 касания и два промпта: построить карту и написать по ней посты, которые двигают человека к заявке.</p></div>'
))

# P3 · Диагноз
P.append(page("Диагноз", 3,
  head("Почему мимо", "Пишешь текст без карты", "Пост получается гладким, а конверсии нет. Причина не в словах — ты не знаешь, в каком состоянии читатель и что ему мешает.")
  + rec(1, "Просишь «напиши прогрев»", "Claude выдаёт красивый текст ни для кого. Нет адресата — нет попадания.")
  + rec(2, "Пишешь о себе, не о нём", "Пост про твой продукт, а не про то, что человек сейчас думает и боится.")
  + rec(3, "Прыгаешь через состояние", "Предлагаешь купить тому, кто ещё сомневается. Сдвиг пропущен — шаг не случился.")
  + rec(4, "Одинаковые посты подряд", "Каждый пост толчёт одно. Читатель не двигается по пути, он стоит.")
  + '<p class="note">Лечится одним: перед текстом строим карту — состояние, трение, сдвиг. Тогда каждый пост знает, кого и куда двигает.</p>'
))

# P4 · Ядро
P.append(page("Ядро метода", 4,
  head("Сдвиг мышления", "Пост делает один сдвиг", "Не «дать пользы побольше», а перевести человека из одного состояния в следующее. Один пост — один сдвиг.")
  + rec(1, "Сначала диагностика", "Опиши состояние и трение. Это важнее, чем формулировки в посте.")
  + rec(2, "Потом текст", "Пост пишется под конкретный сдвиг: закрыть это трение, дать это понимание.")
  + rec(3, "Порядок нельзя тасовать", "Доказательство до микро-результата — не поверят. Предложение первым — отпугнёт.")
  + '<div class="callout check"><div class="h">Правило</div>'
    '<div class="row">У каждого поста есть адресат в конкретном состоянии</div>'
    '<div class="row">У каждого поста ровно один сдвиг</div>'
    '<div class="row">Следующий пост начинается там, где кончился предыдущий</div>'
    '</div>'
))

# P5 · Мост 4 касаний = 4 сдвига
P.append(page("Мост 4 касаний", 5,
  head("Карта пути", "Четыре касания — четыре сдвига", "Лид-магнит не продаёт. Он открывает мост из 4 касаний. Каждое касание — один сдвиг состояния читателя.")
  + '<div class="four">'
    '<div class="r"><span class="n">01</span><span class="lb">Знакомство</span><span class="sh">чужой → свой</span></div>'
    '<div class="r"><span class="n">02</span><span class="lb">Микро-результат</span><span class="sh">скептик → «получилось»</span></div>'
    '<div class="r"><span class="n">03</span><span class="lb">Доказательство</span><span class="sh">сомнение → доверие</span></div>'
    '<div class="r"><span class="n">04</span><span class="lb">Предложение</span><span class="sh">интерес → действие</span></div>'
    '</div>'
  + '<p class="note">Дальше — карта каждого касания: состояние, трение, сдвиг и пример поста, который этот сдвиг делает.</p>'
))

# P6 · Анатомия карты
P.append(page("Анатомия карты", 6,
  head("Три поля", "Состояние · Трение · Сдвиг", "Любое касание описывается одной тройкой. Заполнил — знаешь, о чём и зачем пост.")
  + rec(1, "Состояние", "Что человек думает и чувствует ЗДЕСЬ. От первого лица: «у меня всё равно не выйдет».")
  + rec(2, "Трение", "Что конкретно мешает шагнуть: страх, сомнение, непонимание, отсутствие шага.")
  + rec(3, "Сдвиг", "Что он должен понять, чтобы двинуться. Это и есть цель поста — одна на текст.")
  + biz("трение — не «мало мотивации», а конкретный барьер: «боюсь, что сложно», «не верю, что у меня выйдет», «непонятно, что делать дальше».", "Как формулировать")
))

# P7-P10 · Карта по касаниям
P.append(page("Касание 1 · Знакомство", 7,
  head("Чужой → свой", "Карта: знакомство") + shift("Чужой", "Свой")
  + tri("«Скачал гайд, но кто этот автор? Ещё один продавец курсов?»",
        "Не доверяет, не понимает, зачем оставаться в канале.",
        "«Он говорит про мою боль своими словами — он свой».")
  + ex("Пример поста",
     ["Меня зовут Илья. Учу собирать контент на нейросетях — без агентств и монтажёров.",
      "Знаю это чувство: скачал очередной гайд и закрыл. Здесь по-другому — показываю метод на своих руках. Завтра разберём, с чего начать, если ты вообще не трогал ИИ."])
))
P.append(page("Касание 2 · Микро-результат", 8,
  head("Скептик → «получилось»", "Карта: микро-результат") + shift("Скептик", "«Получилось»")
  + tri("«Интересно, но у меня всё равно не выйдет — я не технарь».",
        "Боится сложности, нет первой маленькой победы своими руками.",
        "«Я сам это сделал — и получилось!»")
  + ex("Пример поста",
     ["Частая ошибка новичка — просить у нейросети «сделай красиво». Она не читает мыслей.",
      "Дай ей рамку: кто ты, для кого, что нужно на выходе. Попробуй прямо сейчас на своём запросе — увидишь разницу с первого раза. Это и есть твоя первая маленькая победа."])
))
P.append(page("Касание 3 · Доказательство", 9,
  head("Сомнение → доверие", "Карта: доказательство") + shift("Сомнение", "Доверие")
  + tri("«У автора-то выходит. А в реальной работе так же?»",
        "Сомневается, что метод повторяем и работает не только у эксперта.",
        "«Это система, а не разовая удача — повторю и я».")
  + ex("Пример поста",
     ["На днях собрал рекламный ролик для кофейни за вечер — на одном промпте и бесплатных инструментах.",
      "Не «вау-генерация», а рабочий конвейер: сценарий → кадры → сборка. Метод повторяемый — на выходных покажу по шагам, чтобы ты собрал свой."])
))
P.append(page("Касание 4 · Предложение", 10,
  head("Интерес → действие", "Карта: предложение") + shift("Интерес", "Действие")
  + tri("«Хочу так же. Но что конкретно делать дальше?»",
        "Не видит понятного следующего шага; боится давления и «впаривания».",
        "«Вижу шаг — он логичный, и меня не толкают».")
  + ex("Пример поста · мягкий оффер",
     ["Если хочешь собрать такой конвейер под себя — на курсе разбираем всю систему по шагам: от первого промпта до готового контента. Без воды.",
      "Ссылка в профиле — посмотри программу и реши сам. Не тороплю: это работает, когда ты готов."])
))

# P11 · Как строить карту
P.append(page("Как строить карту", 11,
  head("Порядок", "Снизу вверх — от заявки", "Строй карту не от начала, а от цели: куда ведёшь. Так каждый предыдущий сдвиг готовит следующий.")
  + act("Порядок работы", [
      "Начни с касания 4: какое <b>действие</b> нужно и что мешает его сделать.",
      "Поднимись к 3, 2, 1: какое состояние должно быть ПЕРЕД этим шагом.",
      "Проверь цепочку сверху вниз: каждый сдвиг <em>логично готовит</em> следующий.",
      "Только теперь пиши посты — по одному на касание.",
    ])
  + '<div class="callout check"><div class="h">Частые ошибки</div>'
    '<div class="row">Трение расплывчатое («мало доверия») вместо конкретного барьера</div>'
    '<div class="row">Два сдвига в одном посте — читатель не успевает</div>'
    '<div class="row">Состояние описано про продукт, а не про человека</div>'
    '</div>'
))

# P12 · Промпт 1 (HERO)
P.append(page("Промпт 1 · карта", 12,
  head("Этап · построить карту", "Claude строит карту состояний", "Главный промпт метода. Сначала заставляем Claude описать читателя — и только потом писать. Обрати внимание на остановку «жди ок».")
  + act("Что делаешь", [
      "Заполняешь [магнит], [аудиторию], [продукт] и вставляешь промпт.",
      "Claude выдаёт <b>карту</b> (состояние/трение/сдвиг по 4 касаниям) и останавливается.",
      "Правишь карту под свою реальность — <em>это важнее текста</em>.",
      "Пишешь «ок» — переходишь к промпту 2.",
    ])
  + prompt("Промпт · Claude · Карта состояний",
    "Ты — редактор Telegram-воронки.\n"
    "Лид-магнит: [ЧТО ПОЛУЧИЛ ЧЕЛОВЕК]\n"
    "Аудитория: [КТО] · Продукт: [ЧТО ПРОДАЮ]\n\n"
    "ШАГ 1 — КАРТА СОСТОЯНИЙ. Не пиши посты.\n"
    "Для каждого из 4 касаний опиши читателя тройкой:\n"
    "— СОСТОЯНИЕ: что он думает и чувствует сейчас\n"
    "— ТРЕНИЕ: что мешает сделать следующий шаг\n"
    "— СДВИГ: что должен понять, чтобы шагнуть дальше\n"
    "Касания и целевой сдвиг: 1) знакомство чужой→свой;\n"
    "2) микро-результат скептик→получилось; 3) доказательство\n"
    "сомнение→доверие; 4) предложение интерес→действие.\n"
    "Покажи карту таблицей. Остановись и жди моё «ок».\n" + VOICE,
    "сила промпта не в длине, а в диагностике до генерации + остановке. Правь карту — тогда посты попадут.")
))

# P13 · Промпт 2
P.append(page("Промпт 2 · посты", 13,
  head("Этап · написать по карте", "Claude пишет посты-переходы", "Карта готова и выверена. Теперь Claude пишет 4 поста — каждый закрывает трение и делает сдвиг.")
  + act("Что делаешь", [
      "После «ок» отправляешь второй промпт.",
      "Claude пишет 4 поста — <b>по одному на касание</b>.",
      "Проверяешь: пост закрывает именно <em>трение своего касания</em>.",
      "Добавляешь свои факты и публикуешь по одному в день.",
    ])
  + prompt("Промпт · Claude",
    "Теперь по карте напиши 4 поста, по одному на касание.\n"
    "Каждый пост закрывает ТРЕНИЕ своего касания и делает СДВИГ.\n"
    "Для каждого: хук первой строки, одна мысль, структура, один CTA.\n"
    "Без инфостиля, клише, «успей» и давления.\n"
    "Каждый пост логично продолжает предыдущий. Мои факты: [ВСТАВЬ].\n" + VOICE,
    "посты растут из карты, а не наоборот. Если пост не двигает состояние — он лишний.")
))

# P14 · До/после
P.append(page("До / после", 14,
  head("Разбор", "Без карты против по карте")
  + pair('«Купи мой курс по нейросетям — научу зарабатывать!» Кому, в каком состоянии — неизвестно. Мимо.',
         'Касание 2, состояние «у меня не выйдет» → пост про первую маленькую победу своими руками. Точно в цель.',
         "Без карты", "По карте")
  + '<p class="note">Один и тот же продукт. Разница — в том, знаешь ли ты, <b>кого и куда</b> двигаешь этим постом.</p>'
))

# P15 · Бланк
P.append(page("Бланк · карта состояний", 15,
  head("Заполни под себя", "Твоя карта на 4 касания")
  + '<div class="blank">'
    + "".join(
      f'<div class="row"><div class="h"><i>{nm}</i> · {lb} ({sh})</div>'
      '<div class="ln"></div><div class="ln"></div><div class="ln s"></div></div>'
      for nm, lb, sh in [("01", "Знакомство", "чужой→свой"), ("02", "Микро-результат", "скептик→получилось"),
                         ("03", "Доказательство", "сомнение→доверие"), ("04", "Предложение", "интерес→действие")])
    + '</div>'
  + '<p class="note">Три строки в каждом блоке: состояние · трение · <span style="color:var(--o);font-weight:700">сдвиг</span>. Заполнил — отдавай в промпт 2.</p>'
))

# P16 · Чек-лист
P.append(page("Чек-лист · честность", 16,
  head("Контроль", "Карта или гладкий текст")
  + '<div class="callout check"><div class="h">Чек-лист карты</div>'
    '<div class="row">У каждого касания заполнены состояние, трение, сдвиг</div>'
    '<div class="row">Состояние — про человека, от первого лица; трение — конкретный барьер</div>'
    '<div class="row">У каждого поста ровно один сдвиг</div>'
    '<div class="row">Порядок касаний не нарушен: доказательство и польза до предложения</div>'
    '<div class="row">Карту построили ДО текста, а не наоборот</div>'
    '<div class="row">Примеры и кейсы реальные, без выдуманных цифр</div>'
    '</div>'
  + '<p class="note">Честно: карта состояний — это уважение к читателю, а не манипуляция. Ты ведёшь его по пути, а не толкаешь. Примеры в тетради — учебные, без выдуманных результатов.</p>'
))

# P17 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Пиши не посты —<br><span style="color:var(--o2)">переходы.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:47ch;margin:0 auto 20px">Карта состояний, мост 4 касаний и два промпта для Claude — вся тетрадь дня. Всей системе — от упаковки до прогрева — учим на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Карта состояний · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
