# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 18 «Лид-магнит: приманка, а не подписка» — премиум-PDF (фикс-A4).
Почему «подписывайся» не работает, что такое хороший магнит, 4 формата, куда ставить (3 точки),
анатомия, 3 промпта Claude (идея → собрать сам магнит → упаковка+анонс), до/после,
ШАБЛОН МАГНИТА (заполнить), план запуска, чек-лист. Ядро — приманка, а не призыв.
Честность: без выдуманных цифр. База CSS — из v2. Запуск: python3 scripts/guide_lidmagnit_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "lid-magnit"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-lid-magnit.html"

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
/* 4 формата */
.opora{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:10px 0}
.opora .o4{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:12px;padding:11px 13px}
.opora .o4 .t{font-weight:800;font-size:11pt;color:var(--ink);display:flex;align-items:center;justify-content:space-between;line-height:1}
.opora .o4 .t i{font-style:normal;color:#fff;font-size:8.5pt;font-weight:800;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:6px;padding:3px 8px}
.opora .o4 p{margin-top:6px;font-size:9.3pt;line-height:1.4;color:var(--body)}
/* действия */
.act{margin:10px 0 4px}
.act .s{display:grid;grid-template-columns:20px 1fr;gap:11px;margin:7px 0;align-items:start}
.act .s .k{width:20px;height:20px;border-radius:6px;background:#ece0cc;color:#8a6127;font-weight:800;font-size:9.5pt;display:flex;align-items:center;justify-content:center;line-height:1;margin-top:1px}
.act .s p{font-size:9.6pt;line-height:1.44;color:var(--body)}
.act .s p b{color:var(--ink);font-weight:800}.act .s p em{font-style:normal;color:var(--o);font-weight:700}
.actlbl{display:block;font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin:6px 0 2px}
/* 3 точки-поток */
.dots{display:flex;flex-wrap:wrap;gap:9px;align-items:stretch;margin:11px 0}
.dots .p{flex:1;min-width:120px;background:#fff;border:1px solid var(--line);border-top:3px solid var(--o);border-radius:11px;padding:11px 12px}
.dots .p b{display:block;font-weight:800;font-size:10pt;color:var(--ink);margin-bottom:3px}
.dots .p span{font-size:9pt;line-height:1.38;color:var(--body)}
/* шаблон магнита (тёмная плашка-форма) */
.mag{background:#13100a;border:1px solid rgba(255,150,80,.28);border-left:3px solid var(--o);border-radius:12px;padding:15px 17px;margin:11px 0}
.mag .row{display:grid;grid-template-columns:118px 1fr;gap:12px;align-items:baseline;padding:8px 0;border-bottom:1px solid rgba(255,255,255,.08)}
.mag .row:last-child{border-bottom:0}
.mag .row b{font-weight:800;font-size:9pt;letter-spacing:.03em;text-transform:uppercase;color:var(--o2)}
.mag .row .ln{border-bottom:1.5px dashed rgba(255,180,120,.4);min-height:15px}
.mag .row span{font-size:8.7pt;color:#b9ad9b;line-height:1.35}
/* бланк (светлые линии) */
.blank{display:flex;flex-direction:column;gap:8px;margin:11px 0}
.blank .f{display:grid;grid-template-columns:130px 1fr;gap:12px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 13px}
.blank .f b{font-weight:800;font-size:9.4pt;color:var(--ink)}
.blank .f .ln{height:1px;border-bottom:1.5px dashed var(--line2);min-height:14px}
.blank .f span{font-size:8.7pt;color:var(--faint)}
"""
CSS = V2CSS + EXTRA

VOICE = "[ГОЛОС] живо, короткие фразы, конкретика, без штампов и эмодзи-мусора."

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · лид-магнит</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>Разбор:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def biz(txt, lbl="Пример"):
    return f'<div class="biz"><b>{lbl}</b>{txt}</div>'

def rec(n, title, body):
    return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{title}</b><p>{body}</p></div></div>'

def pair(bad, good, bl="«Подпишись»", gl="Приманка"):
    return (f'<div class="pair"><div class="c bad"><span class="l">✕ {bl}</span>{bad}</div>'
            f'<div class="c good"><span class="l">✓ {gl}</span>{good}</div></div>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def act(lbl, steps):
    body = "".join(f'<div class="s"><div class="k">{i}</div><p>{t}</p></div>' for i, t in enumerate(steps, 1))
    return f'<span class="actlbl">{lbl}</span><div class="act">{body}</div>'

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
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 18</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Лид-магнит: приманка, <span style="color:var(--o2)">не подписка.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Как дать повод перейти с Reels в Telegram. Четыре формата приманки, куда её ставить, шаблон магнита и промпты, которые соберут его за 20 минут.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">4 формата</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Шаблон магнита</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 промпта</span>
    </div>
  </div>
</section>""")

# P2 · Что внутри
P.append(page("Что внутри", 2,
  head("Тетрадь под карусель «Лид-магнит»", "Не проси подписку — дай повод",
    "Профиль ведёт мост в Telegram, рубрики держат ленту — а лид-магнит даёт причину перейти прямо сейчас. Без него мост пустой.")
  + '<div class="flow">'
    '<div class="node"><b>Reels</b><span>охват</span></div><div class="arr">→</div>'
    '<div class="node"><b>Профиль</b><span>мост</span></div><div class="arr">→</div>'
    '<div class="node"><b>Магнит</b><span>повод</span></div><div class="arr">→</div>'
    '<div class="node"><b>Telegram</b><span>заявка</span></div>'
    '</div>'
  + '<div class="term"><b>Лид-магнит</b> — <span>бесплатная польза за переход: гайд, чек-лист, шаблон, разбор. Решает одну боль быстро.</span></div>'
  + '<div class="term"><b>Приманка &gt; призыв</b> — <span>«подпишись» — это про тебя. Приманка — про выгоду человека. Поэтому работает.</span></div>'
  + '<div class="callout result"><div class="h">Что на выходе</div><p>Готовая идея магнита под нишу, собранный с Claude материал, заголовок и анонс, заполненный шаблон магнита и план запуска в 3 точки.</p></div>'
))

# P3 · Диагноз
P.append(page("Диагноз", 3,
  head("Почему не идут", "«Подписывайся» не работает", "Человек пришёл с Reels, глянул профиль — и ушёл. Не потому что скучно. Просто повода перейти ты не дал.")
  + rec(1, "Просишь, а не даёшь", "«Подпишись на мой Telegram» — это про твою выгоду. Человеку — ничего.")
  + rec(2, "Обещание размытое", "«Полезный контент» — не обещание. Непонятно, что именно и зачем.")
  + rec(3, "Нет причины сейчас", "Даже если интересно — «потом». А «потом» не наступает.")
  + rec(4, "Далеко до ценности", "Если за переходом ещё искать пользу — не переходят. Ценность должна быть сразу.")
  + '<p class="note">Решение простое: замени призыв на приманку. Дай конкретную пользу за один шаг — и человек перейдёт сам.</p>'
))

# P4 · Что такое хороший магнит
P.append(page("Хороший магнит", 4,
  head("Четыре признака", "Каким должен быть магнит", "Сильная приманка — это не большой PDF на 50 страниц. Это быстрое решение одной боли.")
  + rec(1, "Одна боль", "Решает один конкретный вопрос, а не «всё обо всём». Узкое бьёт точнее.")
  + rec(2, "Быстрый результат", "Человек применяет и видит пользу за 10-15 минут, а не «когда-нибудь».")
  + rec(3, "Конкретный", "Понятно за секунду, что внутри и что это даст. Название говорит само.")
  + rec(4, "Ведёт дальше", "После магнита — понятный следующий шаг: прогрев, разбор, курс.")
  + '<div class="callout check"><div class="h">Тест приманки</div>'
    '<div class="row">Могу назвать одну боль, которую она снимает</div>'
    '<div class="row">Человек получит результат в тот же день</div>'
    '<div class="row">Заголовок понятен без объяснений</div>'
    '</div>'
))

# P5 · 4 формата
P.append(page("Четыре формата", 5,
  head("Выбор формы", "Четыре формата приманки", "Одна и та же польза работает в разной форме. Выбирай по тому, что быстрее собрать и что ближе аудитории.")
  + opora([
      ("Гайд", "как", "Пошаговое «как сделать» одну вещь. Лучше всего показывает экспертизу."),
      ("Чек-лист", "проверь", "Список пунктов: ничего не забыть. Быстро собрать, легко применить."),
      ("Шаблон / промпт", "бери", "Готовая заготовка: вставил свои данные — готово. Максимум пользы за минуту."),
      ("Разбор", "пример", "Живой пример «до/после» или кейс. Доказательство + метод в одном."),
    ])
  + '<p class="note">Начни с того, что <b>уже есть</b>: твой рабочий чек-лист или промпт — это готовый магнит. Не нужно писать книгу.</p>'
))

# P6 · Как выбрать под нишу
P.append(page("Формат под нишу", 6,
  head("Подгонка", "Что заходит в разных нишах", "Формат подбирают под то, как аудитория привыкла получать пользу. Несколько ориентиров.")
  + '<div class="pair"><div class="c good"><span class="l">Эксперт / услуга</span>Гайд или разбор кейса — показывают глубину и метод.</div>'
    '<div class="c good"><span class="l">Магазин / товар</span>Чек-лист «как выбрать» или подборка — снимают сомнение перед покупкой.</div></div>'
  + '<div class="pair"><div class="c good"><span class="l">Контент / ИИ</span>Шаблон или промпт — сразу дают результат в руки.</div>'
    '<div class="c good"><span class="l">Локальный бизнес</span>Чек-лист или мини-гайд «на месте» — просто и полезно здесь и сейчас.</div></div>'
  + biz("не гадай — спроси у аудитории. Один вопрос в сторис «что нужнее: чек-лист или готовый шаблон?» экономит неделю.", "Приём")
))

# P7 · Анатомия магнита
P.append(page("Анатомия магнита", 7,
  head("Из чего собран", "Пять частей приманки", "Любой магнит — от чек-листа до гайда — собирается из одних и тех же пяти частей. Держи их — и приманка работает.")
  + rec(1, "Боль", "Какую конкретную проблему снимает. С неё начинается всё.")
  + rec(2, "Обещание", "Заголовок-выгода: что человек получит. Это то, что цепляет.")
  + rec(3, "Что внутри", "3-7 пунктов пользы. Не вода, а конкретные шаги/приёмы.")
  + rec(4, "Формат", "Гайд, чек-лист, шаблон или разбор — форма подачи.")
  + rec(5, "Следующий шаг", "Куда ведёт после: прогрев в Telegram → курс или бриф. Магнит — не тупик.")
))

# P8 · Куда ставить
P.append(page("Три точки", 8,
  head("Размещение", "Где стоит приманка", "Магнит не лежит в одном месте — он встречает человека в трёх точках пути. Так его точно увидят.")
  + '<div class="dots">'
    '<div class="p"><b>Шапка</b><span>Последняя строка: «Забери [магнит] → ссылка». Первое, что видит гость.</span></div>'
    '<div class="p"><b>Закреп</b><span>Пост, который объясняет: что за магнит и как забрать за один шаг.</span></div>'
    '<div class="p"><b>Финал Reels</b><span>CTA в конце ролика: «промпт/гайд — в профиле, забирай».</span></div>'
    '</div>'
  + '<p class="note">Одна приманка — три точки контакта. Человек мог пролистать шапку, но зацепиться на финале Reels. Дублируй повод.</p>'
  + biz("магнит ведёт в Telegram за конкретным. Дальше — прогрев к курсу (B2C) или к брифу студии (B2B). Всегда есть выход воронки.", "Куда ведёт")
))

# P9 · Промпт 1 · идея
P.append(page("Промпт 1 · идея", 9,
  head("Этап · придумать магнит", "Claude предложит идеи под нишу", "Первый шаг: получить 5 идей приманки, разложенных по боли, формату и содержанию. Выбираешь одну.")
  + act("Что делаешь", [
      "Открываешь Claude, вставляешь промпт ниже.",
      "Подставляешь <b>[ТВОЯ НИША]</b> — «нейросети для контента», «кофейня» и т.п.",
      "Из 5 идей <em>выбираешь одну</em> — где боль самая горячая.",
      "Переносишь в шаблон магнита на стр. 13.",
    ])
  + prompt("Промпт · Claude",
    "Предложи 5 идей лид-магнита для ниши [ТВОЯ].\n"
    "По каждой: боль аудитории, обещание (заголовок), формат\n"
    "(гайд / чек-лист / шаблон / разбор), что внутри (3-5 пунктов),\n"
    "следующий шаг (куда ведёт). Приманка решает одну боль быстро.\n" + VOICE,
    "выбирай идею по горячей боли, а не по тому, что проще. Приманка ценна ровно настолько, насколько остра боль.")
))

# P10 · Промпт 2 · собрать магнит
P.append(page("Промпт 2 · собрать", 10,
  head("Этап · собрать сам магнит", "Claude напишет гайд или чек-лист", "Идея выбрана. Теперь Claude собирает сам материал — за 20 минут вместо недели.")
  + act("Что делаешь", [
      "Берёшь заголовок и формат из выбранной идеи.",
      "Вставляешь их в промпт, добавляешь свои <b>факты и приёмы</b>.",
      "Claude собирает черновик — ты <em>правишь под свой опыт</em>, убираешь лишнее.",
      "Оформляешь (можно в этой же тетради-стиле) и выкладываешь в Telegram.",
    ])
  + prompt("Промпт · Claude",
    "Собери лид-магнит «[ЗАГОЛОВОК]» в формате [ФОРМАТ] для ниши [ТВОЯ].\n"
    "Структура: короткое вступление (1 абзац) → 5-7 шагов/пунктов\n"
    "с пояснением → мини-итог → следующий шаг в Telegram.\n"
    "Практично, каждый пункт — с конкретикой, без штампов.\n"
    "Мои факты и приёмы: [ВСТАВЬ].\n" + VOICE,
    "Claude даёт каркас, ценность — твои факты. Пустой магнит без конкретики не работает.")
))

# P11 · Промпт 3 · упаковка
P.append(page("Промпт 3 · упаковка", 11,
  head("Этап · заголовок и анонс", "Claude упакует магнит", "Материал готов. Теперь — цепляющее название и тексты, которые заведут людей за магнитом.")
  + act("Что делаешь", [
      "Просишь варианты названия — <b>выбираешь самое конкретное</b>.",
      "Берёшь строку для шапки и текст закрепа.",
      "Ставишь их в три точки (стр. 8): шапка, закреп, финал Reels.",
      "Подпись под Reels — <em>с CTA на магнит</em>.",
    ])
  + prompt("Промпт · Claude",
    "Для лид-магнита «[ЗАГОЛОВОК]» дай: 5 вариантов цепляющего\n"
    "названия, строку для шапки профиля, текст закрепа (зачем идти\n"
    "в Telegram) и подпись под Reels с CTA. Коротко, живо, без\n"
    "давления. Ниша: [ТВОЯ].\n" + VOICE,
    "название — это 80% успеха приманки. Конкретное «7 промптов для reels» бьёт сильнее размытого «полезный гайд».")
))

# P12 · До / после
P.append(page("До / после", 12,
  head("Разбор", "Призыв против приманки")
  + pair('«Подписывайся на мой Telegram — там много полезного про нейросети!» Человек не понял выгоды и пролистал.',
         '«Собрал 7 промптов, которые пишут Reels за тебя. Забирай бесплатно → ссылка в шапке.» Конкретно, за один шаг.')
  + '<span class="kick" style="display:block;margin-top:14px">Формула заголовка</span>'
  + '<div class="pair"><div class="c good"><span class="l">Число + результат</span>«5 шаблонов постов, которые не стыдно опубликовать»</div>'
    '<div class="c good"><span class="l">Боль → решение</span>«Не знаешь, что постить? Готовая сетка рубрик на месяц»</div></div>'
  + '<p class="note">Приманка не обещает «всё». Она обещает <b>одно конкретное</b> — и даёт это сразу.</p>'
))

# P13 · ШАБЛОН МАГНИТА
P.append(page("Шаблон магнита", 13,
  head("Заполни под себя", "Шаблон магнита", "Это ядро тетради. Заполни пять полей — и у тебя готовый каркас приманки под свою нишу.")
  + '<div class="mag">'
    '<div class="row"><b>Боль</b><div class="ln"></div></div>'
    '<div class="row"><b>Обещание</b><div class="ln"></div></div>'
    '<div class="row"><b>Формат</b><span>гайд · чек-лист · шаблон/промпт · разбор</span></div>'
    '<div class="row"><b>Что внутри</b><div class="ln"></div></div>'
    '<div class="row"><b>&nbsp;</b><div class="ln"></div></div>'
    '<div class="row"><b>Следующий шаг</b><div class="ln"></div></div>'
    '</div>'
  + '<p class="note">Заполнил — переноси в Промпт 2 (стр. 10), и Claude соберёт сам материал. Заголовок отшлифуешь Промптом 3.</p>'
))

# P14 · План запуска
P.append(page("План запуска", 14,
  head("Собери и поставь", "План запуска в 3 точки")
  + '<div class="blank">'
    '<div class="f"><b>Название</b><div class="ln"></div></div>'
    '<div class="f"><b>Ссылка / бот</b><div class="ln"></div></div>'
    '<div class="f"><b>Строка в шапку</b><div class="ln"></div></div>'
    '<div class="f"><b>Закреп</b><div class="ln"></div></div>'
    '<div class="f"><b>CTA под Reels</b><div class="ln"></div></div>'
    '</div>'
  + '<div class="callout check"><div class="h">Проверь перед запуском</div>'
    '<div class="row">Магнит лежит в Telegram и открывается за один шаг</div>'
    '<div class="row">Приманка стоит во всех трёх точках: шапка · закреп · финал Reels</div>'
    '<div class="row">Название конкретное, обещает одну выгоду</div>'
    '</div>'
))

# P15 · Чек-лист
P.append(page("Чек-лист · честность", 15,
  head("Контроль", "Приманка или призыв")
  + '<div class="callout check"><div class="h">Чек-лист магнита</div>'
    '<div class="row">Решает одну конкретную боль, а не «всё сразу»</div>'
    '<div class="row">Даёт результат в тот же день</div>'
    '<div class="row">Название понятно за секунду и обещает выгоду</div>'
    '<div class="row">Стоит в трёх точках и ведёт в Telegram за один шаг</div>'
    '<div class="row">После магнита есть следующий шаг: прогрев → курс или бриф</div>'
    '<div class="row">Внутри — реальная польза, без воды и выдуманных обещаний</div>'
    '</div>'
  + '<p class="note">Честно: магнит не «набирает подписчиков любой ценой». Он даёт реальную пользу тем, кому она нужна. Примеры в тетради — учебные, без выдуманных цифр.</p>'
))

# P16 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Дай повод —<br>не проси <span style="color:var(--o2)">подписку.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:47ch;margin:0 auto 20px">Шаблон магнита, четыре формата и промпты для Claude — вся тетрадь дня. Упаковке, рубрикам и лид-магнитам — всей системе — учим на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Лид-магнит: приманка, не подписка · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
