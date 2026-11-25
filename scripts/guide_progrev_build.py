# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 21 «Прогрев: от подписки до заявки» — премиум-PDF (фикс-A4).
Почему подписчик не покупает, что такое прогрев, лестница доверия, 4 шага прогрева
(знакомство → польза → доказательство → предложение) с примерами постов, стоп-лист,
3 промпта Claude (серия → пост шага → мягкий оффер), до/после, бланк плана прогрева, чек-лист.
Ядро — греешь доверие, а не продаёшь в лоб. Честность: без выдуманных цифр конверсии.
База CSS — из v2. Запуск: python3 scripts/guide_progrev_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "progrev"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-progrev.html"

EXTRA = r"""
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.prompt code{font-size:9.1pt}
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
.opora{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:10px 0}
.opora .o4{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:12px;padding:11px 13px}
.opora .o4 .t{font-weight:800;font-size:11pt;color:var(--ink);display:flex;align-items:center;justify-content:space-between;line-height:1}
.opora .o4 .t i{font-style:normal;color:#fff;font-size:8.5pt;font-weight:800;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:6px;padding:3px 8px}
.opora .o4 p{margin-top:6px;font-size:9.3pt;line-height:1.4;color:var(--body)}
.act{margin:10px 0 4px}
.act .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:7px 0;align-items:start}
.act .s .k{width:20px;height:20px;border-radius:6px;background:#ece0cc;color:#8a6127;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;line-height:1;margin-top:1px}
.act .s p{font-size:9.6pt;line-height:1.44;color:var(--body)}
.act .s p b{color:var(--ink);font-weight:800}.act .s p em{font-style:normal;color:var(--o);font-weight:700}
.actlbl{display:block;font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin:6px 0 2px}
/* пример поста */
.ex{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o2);border-radius:11px;padding:12px 15px;margin:9px 0}
.ex .h{font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px}
.ex p{font-size:9.7pt;line-height:1.5;color:var(--ink)}.ex p+p{margin-top:6px}
/* лестница доверия */
.lad{display:flex;flex-direction:column;gap:7px;margin:11px 0}
.lad .r{display:grid;grid-template-columns:26px 1fr;gap:11px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 13px}
.lad .r .n{width:26px;height:26px;border-radius:8px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center}
.lad .r b{font-weight:800;font-size:10pt;color:var(--ink)}
.lad .r span{font-size:9.2pt;color:var(--body);line-height:1.4}
.lad .r i{font-style:normal;color:var(--o);font-weight:700}
/* бланк */
.blank{display:flex;flex-direction:column;gap:8px;margin:11px 0}
.blank .f{display:grid;grid-template-columns:150px 1fr;gap:12px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 13px}
.blank .f b{font-weight:800;font-size:9.4pt;color:var(--ink)}
.blank .f .ln{height:1px;border-bottom:1.5px dashed var(--line2);min-height:14px}
.blank .f span{font-size:8.7pt;color:var(--faint)}
"""
CSS = V2CSS + EXTRA

VOICE = "[ГОЛОС] живо, короткие фразы, конкретика, без штампов и эмодзи-мусора."

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · прогрев</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>Разбор:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def biz(txt, lbl="Пример"):
    return f'<div class="biz"><b>{lbl}</b>{txt}</div>'

def rec(n, title, body):
    return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{title}</b><p>{body}</p></div></div>'

def pair(bad, good, bl="В лоб", gl="Прогрев"):
    return (f'<div class="pair"><div class="c bad"><span class="l">✕ {bl}</span>{bad}</div>'
            f'<div class="c good"><span class="l">✓ {gl}</span>{good}</div></div>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def act(lbl, steps):
    body = "".join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i, t in enumerate(steps, 1))
    return f'<span class="actlbl">{lbl}</span><div class="act">{body}</div>'

def ex(label, paras):
    body = "".join(f'<p>{p}</p>' for p in paras)
    return f'<div class="ex"><div class="h">{label}</div>{body}</div>'

def opora(cards):
    body = "".join(f'<div class="o4"><div class="t">{t}<i>{tag}</i></div><p>{p}</p></div>' for t, tag, p in cards)
    return f'<div class="opora">{body}</div>'

P = []

# P1 · Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 21</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Прогрев: от подписки <span style="color:var(--o2)">до заявки.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Как превратить холодного подписчика в тёплого покупателя. Лестница доверия, четыре шага прогрева с примерами постов и промпты, которые соберут серию за вечер.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">4 шага</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Примеры постов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 промпта</span>
    </div>
  </div>
</section>""")

# P2 · Что внутри
P.append(page("Что внутри", 2,
  head("Тетрадь под карусель «Прогрев»", "Подписка — не продажа",
    "Лид-магнит привёл человека в Telegram. Но подписка ≠ покупка. Между ними — прогрев: серия контента, которая греет доверие и ведёт к заявке.")
  + '<div class="flow">'
    '<div class="node"><b>Магнит</b><span>привёл</span></div><div class="arr">→</div>'
    '<div class="node"><b>Прогрев</b><span>греет</span></div><div class="arr">→</div>'
    '<div class="node"><b>Оффер</b><span>предлагает</span></div><div class="arr">→</div>'
    '<div class="node"><b>Заявка</b><span>курс / бриф</span></div>'
    '</div>'
  + '<div class="term"><b>Прогрев</b> — <span>последовательность постов, которая переводит человека из «просто подписался» в «готов купить». Не давление — доверие.</span></div>'
  + '<div class="term"><b>Холодный / тёплый</b> — <span>холодный только узнал тебя; тёплый уже доверяет и понимает ценность. Прогрев греет.</span></div>'
  + '<div class="callout result"><div class="h">Что на выходе</div><p>Понимание лестницы доверия, готовая серия прогрева из 4 постов с примерами, промпты под свою нишу и заполненный план запуска.</p></div>'
))

# P3 · Диагноз
P.append(page("Диагноз", 3,
  head("Почему не покупают", "Подписчик есть — заявок нет", "Дело не в цене и не в аудитории. Между подпиской и покупкой пропущен шаг — прогрев.")
  + rec(1, "Молчание после магнита", "Человек забрал гайд — и тишина. Доверие не выросло, он забыл про тебя.")
  + rec(2, "Продажа в лоб", "Сразу «покупай курс». Холодный человек не готов — закрывает и уходит.")
  + rec(3, "Обо всём сразу", "Каждый пост — новая тема без связи. Нет пути, нет нарастания доверия.")
  + rec(4, "Нет предложения", "Греешь-греешь, а прямого шага так и не даёшь. Тёплый человек не знает, что делать.")
  + '<p class="note">Прогрев чинит всё это: даёт путь от знакомства до предложения, где каждый пост готовит к следующему.</p>'
))

# P4 · Что такое прогрев
P.append(page("Что такое прогрев", 4,
  head("Принцип", "Греешь доверие, не давишь", "Прогрев — это не «продавать чаще». Это вести человека по пути, где он сам дозревает до решения.")
  + rec(1, "Постепенно", "Доверие не появляется с одного поста. Нужна серия, где каждый шаг — чуть теплее.")
  + rec(2, "Через пользу", "Сначала дай — потом предложи. Человек должен получить ценность до оффера.")
  + rec(3, "Без давления", "Никаких «успей», фейкового дефицита и «осталось 2 места». Тёплый купит сам.")
  + rec(4, "С понятным шагом", "В конце — прямое, спокойное предложение. Без него прогрев не превращается в заявку.")
  + biz("прогрев работает и в B2C (курс), и в B2B (бриф студии). Меняется оффер в конце — путь тот же.", "Где работает")
))

# P5 · Лестница доверия
P.append(page("Лестница доверия", 5,
  head("Карта", "От чужого до покупателя", "Человек не прыгает из «подписался» в «оплатил». Он поднимается по лестнице. Задача прогрева — провести по всем ступеням.")
  + '<div class="lad">'
    '<div class="r"><div class="n">1</div><div><b>Чужой</b> · <span>только увидел тебя. Не знает, кто ты и зачем.</span></div></div>'
    '<div class="r"><div class="n">2</div><div><b>Знакомый</b> · <span>понял, о чём ты и чем полезен. Начал читать.</span></div></div>'
    '<div class="r"><div class="n">3</div><div><b>Доверяет</b> · <span>получил пользу, увидел результат. Верит, что ты решишь его вопрос.</span></div></div>'
    '<div class="r"><div class="n">4</div><div><b>Покупатель</b> · <span>готов к шагу. Ему нужно только понятное предложение.</span></div></div>'
    '</div>'
  + '<p class="note">Каждый шаг прогрева поднимает на ступень выше. Продажа в лоб — это прыжок с первой на четвёртую. Так не бывает.</p>'
))

# P6 · 4 шага обзор
P.append(page("Четыре шага", 6,
  head("Система", "Четыре шага прогрева", "Серия прогрева собирается из четырёх типов постов. Каждый — своя задача, каждый готовит к следующему.")
  + opora([
      ("1 · Знакомство", "кто", "Кто ты, чем полезен, чего ждать. Человек понимает, зачем остался."),
      ("2 · Польза", "дай", "Конкретный приём или разбор. Даёшь результат до всякой продажи."),
      ("3 · Доказательство", "верю", "Что реально вышло: кейс, до/после. Доверие из обещаний — в факты."),
      ("4 · Предложение", "шаг", "Спокойный прямой оффер: что предлагаешь и как сделать шаг."),
    ])
  + '<p class="note">Это минимальная серия. Можно растянуть: 2 поста пользы, 2 доказательства — но порядок шагов не меняется.</p>'
))

# P7 · Шаг 1 Знакомство
P.append(page("Шаг 1 · знакомство", 7,
  head("Первый шаг", "Знакомство: кто ты и зачем", "Человек только подписался. Первый пост отвечает: кто ты, чем полезен и что его тут ждёт.")
  + rec(1, "Представься по делу", "Не биография. Одна фраза: чем занимаешься и кому помогаешь.")
  + rec(2, "Пообещай путь", "Скажи, что человек будет получать: разборы, приёмы, метод.")
  + ex("Пример поста · ниша ИИ/контент",
      ["Меня зовут Илья. Учу собирать контент на нейросетях — без агентств и монтажёров.",
       "Здесь показываю метод: как ИИ делает работу, а ты повторяешь. Начнём с простого — завтра разберу, с чего вообще начать, если ты никогда не трогал нейросети."])
))

# P8 · Шаг 2 Польза
P.append(page("Шаг 2 · польза", 8,
  head("Второй шаг", "Польза: дай результат", "Теперь дай конкретную пользу. Один приём, который человек применит сегодня. Это разогревает доверие.")
  + rec(1, "Один приём", "Не «10 лайфхаков». Один, но разобранный до применения.")
  + rec(2, "Сразу применимо", "Человек прочитал — и может сделать. Польза здесь и сейчас.")
  + ex("Пример поста · ниша ИИ/контент",
      ["Частая ошибка новичка — просить у нейросети «сделай красиво». Модель не читает мыслей.",
       "Дай ей рамку: кто ты, для кого, что нужно на выходе. Один этот приём меняет результат сильнее, чем смена модели. Попробуй на своём следующем запросе — увидишь разницу."])
))

# P9 · Шаг 3 Доказательство
P.append(page("Шаг 3 · доказательство", 9,
  head("Третий шаг", "Доказательство: покажи результат", "Обещания греют слабо. Факт — сильно. Покажи, что реально вышло: кейс, до/после, процесс.")
  + rec(1, "Конкретный результат", "Что именно получилось и как. Деталь важнее громких слов.")
  + rec(2, "Метод повторяем", "Покажи, что это система, а не разовая удача. Тогда человек верит, что и у него выйдет.")
  + ex("Пример поста · ниша ИИ/контент",
      ["На днях собрал рекламный ролик для кофейни за вечер — на одном промпте и бесплатных инструментах.",
       "Не «вау-генерация», а рабочий конвейер: сценарий → кадры → сборка. Метод повторяемый — на выходных покажу по шагам, чтобы ты собрал свой."])
))

# P10 · Шаг 4 Предложение
P.append(page("Шаг 4 · предложение", 10,
  head("Четвёртый шаг", "Предложение без впаривания", "Человек тёплый. Теперь — прямое, спокойное предложение. Без давления и фальшивого дефицита.")
  + rec(1, "Где человек сейчас", "Назови его ситуацию: чего он хочет и что мешает.")
  + rec(2, "Что решает оффер", "Коротко: что даёт твой курс/услуга. И простой следующий шаг.")
  + ex("Пример поста · мягкий оффер",
      ["Если хочешь собрать такой конвейер под себя — на курсе разбираем всю систему по шагам: от первого промпта до готового контента. Без воды.",
       "Ссылка в профиле — посмотри программу и реши сам. Не тороплю: это работает, когда ты готов."])
))

# P11 · Что убивает прогрев
P.append(page("Стоп-лист", 11,
  head("Ошибки", "Что убивает прогрев")
  + rec(1, "Тишина", "Залил магнит и пропал. Доверие остывает быстрее, чем кажется.")
  + rec(2, "Продажа в лоб", "«Покупай» на холодную. Отпугивает тех, кто ещё не дозрел.")
  + rec(3, "Фейковый дефицит", "«Осталось 2 места», таймеры на нулях. Тёплый человек чувствует манипуляцию.")
  + rec(4, "Обо всём сразу", "Посты без связи и порядка. Нет пути — нет нарастания доверия.")
  + '<div class="callout check"><div class="h">Признак здорового прогрева</div>'
    '<div class="row">Каждый пост готовит к следующему</div>'
    '<div class="row">Сначала польза, потом предложение</div>'
    '<div class="row">Ни одного «успей» и выдуманного дефицита</div>'
    '</div>'
))

# P12 · Промпт 1 серия
P.append(page("Промпт 1 · серия", 12,
  head("Этап · собрать серию", "Claude соберёт прогрев под нишу", "Первый шаг: получить всю серию из 4 постов, разложенную по шагам. Дальше правишь под свой голос.")
  + act("Что делаешь", [
      "Открываешь Claude, вставляешь промпт ниже.",
      "Подставляешь <b>[ТВОЯ НИША]</b> — «нейросети для контента», «мастер-мебельщик» и т.п.",
      "Получаешь 4 поста по шагам — <em>проверяешь порядок</em>: польза до предложения.",
      "Переносишь темы в бланк плана прогрева (стр. 16).",
    ])
  + prompt("Промпт · Claude",
    "Собери серию прогрева для Telegram из 4 постов под нишу [ТВОЯ]:\n"
    "знакомство → польза → доказательство → предложение.\n"
    "По каждому посту: тема, суть (о чём), мягкий переход к следующему.\n"
    "Прогрев греет доверие, не продаёт в лоб. Без давления.\n" + VOICE,
    "серия — это путь. Проверь, что польза и доказательство идут ДО предложения, а не после.")
))

# P13 · Промпт 2 пост
P.append(page("Промпт 2 · пост шага", 13,
  head("Этап · написать пост", "Claude напишет пост под шаг", "Серия намечена. Теперь Claude пишет конкретный пост под нужный шаг — с твоими фактами.")
  + act("Что делаешь", [
      "Выбираешь шаг: знакомство / польза / доказательство / предложение.",
      "Вставляешь в промпт <b>свои факты и примеры</b> из практики.",
      "Claude пишет пост — ты <em>правишь под свой голос</em>, убираешь лишнее.",
      "Публикуешь по плану: один пост — один шаг.",
    ])
  + prompt("Промпт · Claude",
    "Напиши пост прогрева для шага «[ШАГ]» (знакомство / польза /\n"
    "доказательство / предложение) под нишу [ТВОЯ]. Структура: хук →\n"
    "одна мысль → пример из практики → мягкий переход дальше.\n"
    "800–1200 знаков, живо, без штампов и давления.\n"
    "Мои факты: [ВСТАВЬ].\n" + VOICE,
    "ценность поста — твои факты. Claude даёт форму, конкретику вставляешь ты.")
))

# P14 · Промпт 3 оффер
P.append(page("Промпт 3 · оффер", 14,
  head("Этап · мягкое предложение", "Claude напишет оффер без давления", "Финальный пост серии — предложение. Спокойное, честное, с понятным шагом.")
  + act("Что делаешь", [
      "Подставляешь свой оффер: курс, услуга, бриф.",
      "Claude пишет пост-предложение <b>без «успей» и дефицита</b>.",
      "Проверяешь: назван путь человека → что решает оффер → <em>простой шаг</em>.",
      "Публикуешь как финал серии — и ведёшь на заявку.",
    ])
  + prompt("Промпт · Claude",
    "Напиши пост-предложение для тёплой аудитории под нишу [ТВОЯ].\n"
    "Оффер: [ЧТО ПРЕДЛАГАЕШЬ]. Структура: где человек сейчас →\n"
    "что решает оффер → простой следующий шаг. Без давления,\n"
    "без «успей» и искусственного дефицита. Живо и спокойно.\n" + VOICE,
    "мягкий оффер конвертирует тёплых лучше, чем агрессивный — давлением. Дай решить самому.")
))

# P15 · До / после
P.append(page("До / после", 15,
  head("Разбор", "В лоб против прогрева")
  + pair('«Курс по нейросетям — 14 990. Успей купить, осталось 2 места!» Холодный человек не готов и уходит.',
         'Знакомство → приём → кейс → «хочешь собрать под себя — вот программа, реши сам». Тёплый доходит до заявки.')
  + '<span class="kick" style="display:block;margin-top:14px">Порядок решает</span>'
  + '<div class="pair"><div class="c bad"><span class="l">✕ Так рвётся</span>Предложение первым постом — до пользы и доверия.</div>'
    '<div class="c good"><span class="l">✓ Так греет</span>Предложение последним — когда человек уже получил ценность.</div></div>'
  + '<p class="note">Одни и те же слова оффера работают по-разному в зависимости от того, <b>что было до них</b>.</p>'
))

# P16 · Бланк
P.append(page("Бланк · план прогрева", 16,
  head("Заполни под себя", "План прогрева")
  + '<div class="blank">'
    '<div class="f"><b>Пост 1 · Знакомство</b><div class="ln"></div></div>'
    '<div class="f"><b>Пост 2 · Польза</b><div class="ln"></div></div>'
    '<div class="f"><b>Пост 3 · Доказательство</b><div class="ln"></div></div>'
    '<div class="f"><b>Пост 4 · Предложение</b><div class="ln"></div></div>'
    '<div class="f"><b>Оффер / ссылка</b><div class="ln"></div></div>'
    '</div>'
  + '<div class="callout check"><div class="h">Проверь серию</div>'
    '<div class="row">Порядок: знакомство → польза → доказательство → предложение</div>'
    '<div class="row">Польза и кейс идут ДО оффера</div>'
    '<div class="row">В финале — понятный шаг на заявку</div>'
    '</div>'
))

# P17 · Чек-лист
P.append(page("Чек-лист · честность", 17,
  head("Контроль", "Прогрев или впаривание")
  + '<div class="callout check"><div class="h">Чек-лист прогрева</div>'
    '<div class="row">Серия идёт по шагам, каждый готовит к следующему</div>'
    '<div class="row">Сначала польза и доказательство — потом предложение</div>'
    '<div class="row">Есть прямой, но спокойный оффер в финале</div>'
    '<div class="row">Ни «успей», ни фейкового дефицита, ни давления</div>'
    '<div class="row">Каждый пост ведёт к заявке: курс (B2C) или бриф (B2B)</div>'
    '<div class="row">Примеры и кейсы — реальные, без выдуманных цифр</div>'
    '</div>'
  + '<p class="note">Честно: прогрев — это уважение к человеку, а не воронка-манипуляция. Ты даёшь дозреть, а не выжимаешь. Примеры в тетради — учебные, без выдуманных результатов.</p>'
))

# P18 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Грей доверие —<br>не дави на <span style="color:var(--o2)">кнопку.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:47ch;margin:0 auto 20px">Лестница доверия, 4 шага прогрева с примерами и промпты для Claude — вся тетрадь дня. Упаковке, рубрикам, магнитам и прогреву — всей системе — учим на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Прогрев: от подписки до заявки · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
