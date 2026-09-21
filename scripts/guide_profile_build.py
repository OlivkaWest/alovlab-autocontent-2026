# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 16 «Профиль как мост» — премиум-PDF (фикс-A4).
Профиль, который переводит с Reels в Telegram. Диагноз, мост в 3 узла, формула шапки,
закреп, 5 хайлайтов под путь новичка, бланк профиля, промпты (Claude) и разборы витрина/мост.
Честность: без выдуманных цифр конверсии (клик IG→TG не отслеживается). Ниша — ИИ/контент.
База CSS — из v2. Запуск: python3 scripts/guide_profile_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "profile-most"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-profile-most.html"

EXTRA = r"""
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.prompt code{font-size:9.1pt}
.rec{display:grid;grid-template-columns:22px 1fr;gap:11px;margin:8px 0;align-items:start}
.rec .n{width:22px;height:22px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}
.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.42;color:var(--body)}
.rec .t i{font-style:normal;color:var(--muted)}.rec .t em{font-style:normal;color:var(--o);font-weight:700}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:9px 0}
.pair .c{border-radius:12px;padding:11px 13px;font-size:9.6pt;line-height:1.48}
.pair .bad{background:#faf0ea;border:1px solid #eccdb9;color:#7d6a5c}
.pair .good{background:#fff;border:1px solid var(--line);color:var(--ink)}
.pair .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:5px}
.pair .bad .l{color:#c56b43}.pair .good .l{color:var(--o)}
.form{background:#13100a;border:1px solid rgba(255,150,80,.28);border-left:3px solid var(--o);border-radius:12px;padding:14px 16px;margin:11px 0}
.form .r{display:flex;flex-wrap:wrap;gap:9px;align-items:center;font-size:11pt;color:#ffd9b8;font-weight:700}
.form .r span{background:rgba(255,255,255,.06);border:1px solid rgba(255,150,80,.3);border-radius:8px;padding:5px 11px}
.form .r i{color:var(--o2);font-style:normal;font-weight:800}
.form .cap{margin-top:9px;font-size:9.3pt;color:#b9ad9b;line-height:1.4}
.blank{display:flex;flex-direction:column;gap:9px;margin:11px 0}
.blank .f{display:grid;grid-template-columns:120px 1fr;gap:12px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 13px}
.blank .f b{font-weight:800;font-size:9.5pt;color:var(--ink)}
.blank .f .ln{height:1px;border-bottom:1.5px dashed var(--line2);min-height:14px}
.blank .f span{font-size:8.7pt;color:var(--faint)}
"""
CSS = V2CSS + EXTRA

VOICE = "[ГОЛОС] живо, короткие фразы, конкретика, без штампов и эмодзи-мусора."

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · профиль как мост</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>Разбор:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def biz(txt, lbl="Пример"):
    return f'<div class="biz"><b>{lbl}</b>{txt}</div>'

def rec(n, title, body):
    return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{title}</b><p>{body}</p></div></div>'

def pair(bad, good, bl="Витрина", gl="Мост"):
    return (f'<div class="pair"><div class="c bad"><span class="l">✕ {bl}</span>{bad}</div>'
            f'<div class="c good"><span class="l">✓ {gl}</span>{good}</div></div>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

P = []

# P1 · Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 16</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Профиль как <span style="color:var(--o2)">мост.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Как превратить профиль из витрины в мост, который переводит гостя с Reels в Telegram. Формула шапки, закреп, 5 хайлайтов, бланк профиля и промпты.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Шапка</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Закреп</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Хайлайты</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Бланк</span>
    </div>
  </div>
</section>""")

# P2 · Что внутри
P.append(page("Что внутри", 2,
  head("Тетрадь под карусель «Профиль как мост»", "Reels приводят. Профиль решает",
    "Reels дают охват — но заявка рождается в профиле. Если он не ведёт дальше, трафик утекает. Эта тетрадь — как построить мост от гостя до Telegram.")
  + '<div class="flow">'
    '<div class="node"><b>Reels</b><span>охват</span></div><div class="arr">→</div>'
    '<div class="node"><b>Профиль</b><span>мост</span></div><div class="arr">→</div>'
    '<div class="node"><b>Telegram</b><span>оффер</span></div><div class="arr">→</div>'
    '<div class="node"><b>Заявка</b><span>курс / бриф</span></div>'
    '</div>'
  + '<div class="term"><b>Витрина</b> — <span>красивый профиль, который любуется собой. Гостю неясно, зачем оставаться и куда идти.</span></div>'
  + '<div class="term"><b>Мост</b> — <span>профиль, где каждый элемент ведёт дальше: шапка → закреп → хайлайты → Telegram.</span></div>'
  + '<div class="callout result"><div class="h">Что на выходе</div><p>Готовая шапка, тема закрепа, 5 хайлайтов под путь новичка и заполненный бланк профиля — мост, по которому гость доходит до заявки.</p></div>'
))

# P3 · Диагноз
P.append(page("Диагноз", 3,
  head("Почему уходят", "Профиль-витрина", "Гость решает за секунды. Если профиль не сказал, зачем остаться и куда шагнуть — он закрывает вкладку.")
  + rec(1, "Шапка «о себе»", "«Эксперт, помогаю, DM открыт» — гость не понял, что он получит и зачем.")
  + rec(2, "Некуда идти", "Нет одного понятного шага. Ссылка есть, но непонятно, что за ней и зачем нажимать.")
  + rec(3, "Хайлайты-витрина", "«Обо мне», «Отзывы», «Работа» — красиво, но не ведут по пути, а просто украшают.")
  + rec(4, "Reels не стыкуются", "В Reels обещал одно, в профиле — тишина. Мост оборвался на входе.")
  + '<p class="note">Хорошая новость: это не про красоту, а про маршрут. Маршрут собирается из трёх узлов — дальше.</p>'
))

# P4 · Мост в 3 узла
P.append(page("Мост · 3 узла", 4,
  head("Карта", "Три узла, которые ведут дальше", "Каждый узел решает свою задачу и передаёт гостя следующему. Ни один — не «для красоты».")
  + '<div class="scene"><div class="sn">1</div><div><div class="sh">Шапка</div><div class="sd">За 3 секунды говорит: кто ты, для кого, что дашь и куда идти. Последняя строка ведёт в Telegram.</div></div><span class="stag">кто → куда</span></div>'
  + '<div class="scene"><div class="sn">2</div><div><div class="sh">Закреп</div><div class="sd">Отвечает на один вопрос: зачем идти в твой Telegram именно сейчас. Отдаёт обещанное из Reels.</div></div><span class="stag">зачем в TG</span></div>'
  + '<div class="scene"><div class="sn">3</div><div><div class="sh">Хайлайты</div><div class="sd">Ведут по пути новичка: старт → польза → доказательство → оффер → ответы. Не витрина, а маршрут.</div></div><span class="stag">путь</span></div>'
  + biz("аватар и имя — мелкие, но важные узлы: имя ловит в поиске, аватар считывается за долю секунды. Про них — на стр. 11.", "Ещё")
))

# P5 · Формула шапки
P.append(page("Формула шапки", 5,
  head("Шапка = указатель", "Четыре строки, которые ведут", "Шапка — не «о себе». Это указатель: за чем ты здесь и куда идти. Собирается из четырёх строк.")
  + '<div class="form"><div class="r"><span>кто ты</span><i>→</i><span>для кого</span><i>→</i><span>что дашь</span><i>→</i><span>куда идти</span></div>'
  '<div class="cap">Последняя строка всегда ведёт в Telegram за конкретным: гайд, промпт, чек-лист.</div></div>'
  + rec(1, "Кто ты", "Одной фразой: чем занимаешься. «Учу собирать контент на ИИ».")
  + rec(2, "Для кого", "Кому это. «Экспертам и малому бизнесу» — гость узнаёт себя.")
  + rec(3, "Что человек получит", "Результат, а не процесс. «Контент без подрядчиков».")
  + rec(4, "Куда идти", "Один шаг с конкретикой. «Гайд “Промпт дня” → t.me/AlovLab».")
))

# P6 · Шапка до/после
P.append(page("Шапка · до / после", 6,
  head("Разбор", "Указатель, а не витрина")
  + pair('«Эксперт по нейросетям 🚀 Помогаю выйти на новый уровень. Успех. Мотивация. DM открыт.»',
         '«Учу собирать контент на ИИ — с нуля. Гайд «Промпт дня» и разборы → в Telegram, ссылка ниже.»')
  + '<span class="kick" style="display:block;margin-top:14px">Под свою нишу</span>'
  + '<div class="pair"><div class="c good"><span class="l">Эксперт</span>кто учу → что получишь → гайд/чек-лист в Telegram</div>'
    '<div class="c good"><span class="l">Магазин</span>что продаём → кому → подборка/скидка в канале</div></div>'
  + '<div class="pair"><div class="c good"><span class="l">Услуга</span>что делаем → для кого → разбор/бриф в личке</div>'
    '<div class="c good"><span class="l">Локальный</span>что и где → для кого рядом → меню/запись в боте</div></div>'
))

# P7 · Промпт шапки
P.append(page("Промпт · шапка", 7,
  head("Этап · собрать шапку", "Claude пишет шапку по формуле", "Заполняешь нишу и оффер — получаешь 3 варианта. Дальше правишь под свой голос.")
  + prompt("Промпт · Claude",
    "Напиши шапку профиля (bio) по формуле: кто ты → для кого →\n"
    "что человек получит → куда идти (Telegram за конкретным).\n"
    "4 строки, живо, без штампов и эмодзи-мусора. Дай 3 варианта.\n"
    "Ниша: [ТВОЯ]. Что даю в Telegram: [ГАЙД / ПРОМПТ / ЧЕК-ЛИСТ].\n" + VOICE,
    "3 варианта — чтобы выбрать тон. Последняя строка всегда ведёт в Telegram за конкретным.")
  + biz("для любого профиля: эксперт, магазин, услуга, локальный бизнес, личный бренд.")
))

# P8 · Закреп
P.append(page("Закреп", 8,
  head("Второй узел", "Закреп отвечает: зачем в Telegram", "Гость кликнул шапку и попал на закреп. Здесь один вопрос: зачем идти дальше именно сейчас.")
  + rec(1, "Что человек уже увидел", "Свяжи с Reels: «ты видел, как ИИ делает контент».")
  + rec(2, "Что получит в Telegram", "Конкретика: гайд, промпты, разборы — не «полезный контент».")
  + rec(3, "Как попасть", "Один шаг: «жми ссылку в шапке → забирай гайд».")
  + '<div class="callout check"><div class="h">Проверь закреп</div>'
    '<div class="row">Отвечает на «зачем мне туда идти», а не «какой я молодец»</div>'
    '<div class="row">Есть конкретное обещание (что именно в Telegram)</div>'
    '<div class="row">Один шаг, без выбора из пяти кнопок</div>'
    '</div>'
))

# P9 · Промпт закрепа
P.append(page("Промпт · закреп", 9,
  head("Этап · собрать закреп", "Claude пишет закреп", "Пост, который переводит гостя из профиля в Telegram за один шаг.")
  + prompt("Промпт · Claude",
    "Напиши закреплённый пост, который отвечает на один вопрос:\n"
    "зачем гостю идти в мой Telegram. Структура: что человек уже\n"
    "увидел (Reels) → что получит в Telegram (конкретно) → как\n"
    "попасть (1 шаг). Коротко, без воды и давления. Ниша: [ТВОЯ].\n"
    "Оффер в Telegram: [ЧТО ДАЮ].\n" + VOICE,
    "закреп — мост, а не пейдж. Одно обещание, один шаг. Всё лишнее убери.")
))

# P10 · Хайлайты
P.append(page("Хайлайты", 10,
  head("Третий узел", "Пять хайлайтов под путь новичка", "Хайлайты — не витрина «обо мне». Это маршрут: с чего начать → до заявки. Достаточно пяти.")
  + '<div class="scene"><div class="sn">1</div><div><div class="sh">Старт</div><div class="sd">«Начни отсюда»: кто ты, что даёшь, куда идти. Первый хайлайт — навигатор.</div></div><span class="stag">навигатор</span></div>'
  + '<div class="scene"><div class="sn">2</div><div><div class="sh">Польза</div><div class="sd">Приёмы и разборы — короткая ценность, ради которой остаются.</div></div><span class="stag">ценность</span></div>'
  + '<div class="scene"><div class="sn">3</div><div><div class="sh">Кейсы</div><div class="sd">Что реально вышло. Доказательство вместо обещаний.</div></div><span class="stag">пруф</span></div>'
  + '<div class="scene"><div class="sn">4</div><div><div class="sh">Оффер</div><div class="sd">Что можно забрать/купить и как. Тарифы, гайд, бриф.</div></div><span class="stag">шаг</span></div>'
  + '<div class="scene"><div class="sn">5</div><div><div class="sh">Ответы</div><div class="sd">Отзывы и частые вопросы — снимают сомнения перед шагом.</div></div><span class="stag">доверие</span></div>'
))

# P11 · Аватар, имя, ссылка
P.append(page("Аватар · имя · ссылка", 11,
  head("Мелкие узлы моста", "Их видят первыми", "Имя ловит в поиске, аватар считывается за долю секунды, ссылка — единственная дверь. Мелочи, которые ломают мост.")
  + rec(1, "Имя (не ник)", "В поле «Имя» — ниша + имя: «Илья · Нейросети для контента». По этому ищут.")
  + rec(2, "Аватар", "Читается в кружке: лицо или знак, без мелкого текста. Контраст, чтобы видно на тёмном и светлом.")
  + rec(3, "Ссылка", "Одна, рабочая, ведёт в Telegram за конкретным. Не «сайт вообще», а прямо к обещанию.")
  + biz("имя «alovlab» + «Нейросети & Контент» — гость и найдёт в поиске, и сразу поймёт, о чём профиль.")
))

# P12 · Маршрут гостя
P.append(page("Маршрут гостя", 12,
  head("7 секунд", "Что гость видит по порядку", "Собери всё вместе — и пройди профиль глазами новичка. За 7 секунд он должен понять путь.")
  + '<div class="scene"><div class="sn">1</div><div><div class="sh">Аватар + имя</div><div class="sd">«Кто это и про что» — за долю секунды.</div></div><span class="stag">0–1 сек</span></div>'
  + '<div class="scene"><div class="sn">2</div><div><div class="sh">Шапка</div><div class="sd">«Что я получу и куда идти» — за 3 секунды.</div></div><span class="stag">1–4 сек</span></div>'
  + '<div class="scene"><div class="sn">3</div><div><div class="sh">Закреп / хайлайт «Старт»</div><div class="sd">«Зачем идти в Telegram» — подтверждение.</div></div><span class="stag">4–6 сек</span></div>'
  + '<div class="scene"><div class="sn">4</div><div><div class="sh">Ссылка</div><div class="sd">Один клик — и он в Telegram за обещанным.</div></div><span class="stag">7 сек</span></div>'
  + '<p class="note">Если на любом шаге непонятно «куда дальше» — мост рвётся здесь. Чини именно этот узел.</p>'
))

# P13 · Бланк профиля
P.append(page("Бланк профиля", 13,
  head("Шаблон · заполни под себя", "Собери свой мост")
  + '<div class="blank">'
    '<div class="f"><b>Имя</b><div class="ln"></div></div>'
    '<div class="f"><b>Аватар</b><span>лицо / знак, контрастный, без мелкого текста</span></div>'
    '<div class="f"><b>Шапка · 1</b><div class="ln"></div></div>'
    '<div class="f"><b>Шапка · 2</b><div class="ln"></div></div>'
    '<div class="f"><b>Шапка · 3</b><div class="ln"></div></div>'
    '<div class="f"><b>Шапка · 4 → TG</b><div class="ln"></div></div>'
    '<div class="f"><b>Ссылка</b><div class="ln"></div></div>'
    '<div class="f"><b>Закреп</b><div class="ln"></div></div>'
    '<div class="f"><b>Хайлайты</b><span>Старт · Польза · Кейсы · Оффер · Ответы</span></div>'
    '</div>'
  + '<p class="note">Заполнил все поля — у тебя мост, а не витрина. Проверь по чек-листу на следующей странице.</p>'
))

# P14 · Чек-лист
P.append(page("Чек-лист · честность", 14,
  head("Контроль", "Мост или витрина")
  + '<div class="callout check"><div class="h">Чек-лист профиля</div>'
    '<div class="row">Имя ловит в поиске: ниша + имя</div>'
    '<div class="row">Шапка говорит, что получу и куда идти; последняя строка → Telegram</div>'
    '<div class="row">Ссылка одна, рабочая, ведёт за конкретным</div>'
    '<div class="row">Закреп отвечает «зачем в Telegram», а не «какой я»</div>'
    '<div class="row">5 хайлайтов ведут по пути: старт → польза → кейсы → оффер → ответы</div>'
    '<div class="row">Reels и профиль стыкуются: обещание не обрывается</div>'
    '</div>'
  + '<p class="note">Честно: клик из профиля в Telegram обычно не отслеживается — не гонись за «процентом конверсии», а собери понятный маршрут. Примеры — учебные, в нише ИИ/контента, без выдуманных цифр.</p>'
))

# P15 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Собери мост —<br>не <span style="color:var(--o2)">витрину.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:47ch;margin:0 auto 20px">Формула шапки, закреп, 5 хайлайтов, бланк профиля и промпты для Claude — вся тетрадь дня. Переведи гостя с Reels в Telegram за 7 секунд.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Профиль как мост · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
