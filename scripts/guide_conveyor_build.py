# -*- coding: utf-8 -*-
"""AlovLab · методичка-тетрадь «Контент-конвейер на нейросетях» (под карусель-конвейер, День 4).
Экспертные промпты по этапам: картинка (Midjourney·Nano Banana·Ideogram) → видео (Higgsfield·Kling)
→ голос (ElevenLabs) → аватар (HeyGen). Премиум фикс-A4, светлые страницы, тёмные плашки под промпты.
База CSS — из v2. Запуск: python3 scripts/guide_conveyor_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "conveyor-prompts"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-conveyor-prompts.html"

EXTRA = r"""
.stage{display:flex;align-items:center;gap:12px;margin:2px 0 4px}
.stage .b{font-weight:800;font-size:9pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));
 padding:5px 11px;border-radius:20px;letter-spacing:.04em;white-space:nowrap}
.stage .t{font-weight:800;font-size:9pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.tool{display:grid;grid-template-columns:118px 1fr;gap:12px;background:#fff;border:1px solid var(--line);
 border-radius:11px;padding:11px 14px;margin:8px 0}
.tool .nm{font-weight:800;font-size:11pt;color:var(--ink);line-height:1.2}
.tool .nm i{display:block;font-style:normal;font-weight:700;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o);margin-top:3px}
.tool .ds{font-size:9.7pt;line-height:1.45;color:var(--body)}
.tool .ds b{color:var(--ink)}
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.param{display:grid;grid-template-columns:130px 1fr;gap:8px;font-size:9.6pt;line-height:1.4;padding:7px 0;border-top:1px solid var(--line2)}
.param:first-child{border-top:none}
.param code{font-family:ui-monospace,Menlo,monospace;font-size:9pt;background:#f1e9db;padding:2px 7px;border-radius:5px;color:#8a5a2a;font-weight:600;height:fit-content}
.param span{color:var(--body)}.param span b{color:var(--ink)}
.paramwrap{background:#fff;border:1px solid var(--line);border-radius:11px;padding:6px 14px;margin:10px 0}
.prompt code{font-size:9pt}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · конвейер нейросетей</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>По-русски:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def stage(b, t):
    return f'<div class="stage"><span class="b">{b}</span><span class="t">{t}</span></div>'

def biz(txt):
    return f'<div class="biz"><b>Бизнес</b>{txt}</div>'

P = []

# ---------- P1 · Обложка ----------
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 72% at 84% 10%,#2c2114,#170f08 54%,#0c0a07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд · набор промптов</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.06;letter-spacing:-.02em;color:#fff;max-width:16ch">Контент-конвейер на нейросетях: от картинки до <span style="color:var(--o2)">говорящего аватара.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Один герой проходит четыре этапа. На каждом — какой инструмент, почему он, и готовый промпт с синтаксисом.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Картинка</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Видео</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Голос</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Аватар</span>
    </div>
  </div>
</section>""")

# ---------- P2 · Карта конвейера ----------
P.append(page("Карта конвейера", 2, """
  <span class="kick">Что ты соберёшь</span>
  <h2>Не одна генерация, а конвейер</h2>
  <p class="lead">Ценность не в красивой картинке. Ценность в системе, которая из одного героя выдаёт картинку, видео, голос и аватар — стабильно, а не один раз повезло.</p>
  <div class="flow">
    <div class="node"><b>Картинка</b><span>MJ · Nano Banana</span></div><div class="arr">→</div>
    <div class="node"><b>Видео</b><span>Higgsfield · Kling</span></div><div class="arr">→</div>
    <div class="node"><b>Голос</b><span>ElevenLabs</span></div><div class="arr">→</div>
    <div class="node"><b>Аватар</b><span>HeyGen</span></div><div class="arr">→</div>
    <div class="node"><b>Ролик</b><span>монтаж</span></div>
  </div>
  <div class="term"><b>Промпт</b> — <span>точное задание модели: что показать, что двигать, что оставить неизменным. Чем конкретнее — тем стабильнее результат.</span></div>
  <div class="term"><b>Консистентность</b> — <span>один и тот же герой (лицо, товар, стиль) на всех кадрах серии. Главное, что отличает конвейер от случайных генераций.</span></div>
  <div class="callout result"><div class="h">Обещание</div><p>К концу гайда у тебя набор готовых промптов на все четыре этапа и один сквозной пример, собранный от картинки до аватара.</p></div>
"""))

# ---------- P3 · Что чем делать ----------
P.append(page("Что чем делать", 3, """
  <span class="kick">Карта инструментов</span>
  <h2>Какой инструмент на каком этапе</h2>
  <p class="lead">Ошибка новичка — тянуть всё в один инструмент. Профи знает: у каждого этапа свой герой.</p>
  <table>
    <tr><th>Этап</th><th>Инструмент</th><th>Зачем именно он</th></tr>
    <tr><td><b>Картинка с нуля</b></td><td>Midjourney</td><td>премиум-эстетика из текста, но не редактирует твоё фото</td></tr>
    <tr><td><b>Правки и один герой</b></td><td>Nano Banana</td><td>правит загруженное фото, держит лицо и объект неизменными</td></tr>
    <tr><td><b>Текст на картинке</b></td><td>Ideogram · Nano Banana</td><td>рендерят читаемые буквы — Midjourney текст ломает</td></tr>
    <tr><td><b>Оживить кадр в видео</b></td><td>Higgsfield · Kling</td><td>image-to-video: камера едет, среда живёт, объект стабилен</td></tr>
    <tr><td><b>Голос за кадром</b></td><td>ElevenLabs</td><td>живая интонация и паузы, а не робот</td></tr>
    <tr><td><b>Говорящий аватар</b></td><td>HeyGen</td><td>двойник в кадре ведёт ролики без съёмок</td></tr>
  </table>
  <p class="note">Nano Banana — image-модель Google: редактура, консистентность, текст. Midjourney — премиум с нуля. Одно не заменяет другое — они работают в паре.</p>
"""))

# ---------- P4 · Этап 1 · Картинка с нуля (Midjourney) ----------
P.append(page("Этап 1 · Картинка · Midjourney", 4,
  stage("Этап 1", "Картинка · с нуля") +
  "<h2>Midjourney — премиум из текста</h2>"
  "<p class=\"lead\">Когда своего фото нет и нужен «дорогой» кадр под бренд. Собирай промпт слоями: объект → свет → атмосфера → камера → параметры.</p>" +
  prompt("Готовый промпт · Midjourney",
    "editorial food photograph of a seared scallop on dark slate, warm amber side light, "
    "delicate rising steam, glossy reduction sauce, shallow depth of field, moody near-black "
    "background, hyper-detailed, commercial food styling --ar 4:5 --style raw --stylize 250 --v 6",
    "премиальное фото гребешка на тёмном сланце, тёплый боковой свет, лёгкий пар, глянцевый соус, малая глубина резкости, кинематографичный тёмный фон.") +
  """<span class="kick" style="display:block;margin-top:14px">Параметры, которые отличают профи</span>
  <div class="paramwrap">
    <div class="param"><code>--ar 4:5 / 9:16</code><span><b>Формат.</b> 4:5 под ленту, 9:16 под Reels и первый кадр видео.</span></div>
    <div class="param"><code>--style raw</code><span><b>Убирает «миджорнишность».</b> Ближе к реальному фото, меньше отсебятины.</span></div>
    <div class="param"><code>--stylize 250</code><span><b>Баланс.</b> Ниже — точнее по промпту, выше — красивее и вольнее.</span></div>
    <div class="param"><code>--sref [ссылка]</code><span><b>Единый стиль.</b> Один референс на всю ленту — кадры выглядят серией.</span></div>
    <div class="param"><code>--cref [ссылка] --cw 100</code><span><b>Один герой.</b> Держит лицо/персонажа между кадрами.</span></div>
    <div class="param"><code>--seed [число]</code><span><b>Повтор.</b> Тот же seed — доснять кадр в том же свете.</span></div>
  </div>""" +
  biz("ресторан и e-com — карточки товара; личный бренд — обложки; упаковка и баннеры под единый стиль ленты.")
))

# ---------- P5 · Этап 1 · Правки и консистентность (Nano Banana) ----------
P.append(page("Этап 1 · Правки · Nano Banana", 5,
  stage("Этап 1", "Картинка · правки и один герой") +
  "<h2>Nano Banana — правит твоё фото</h2>"
  "<p class=\"lead\">Когда фото уже есть: заменить фон, собрать серию с одним лицом, добавить читаемый текст. Объект остаётся собой — Midjourney так не умеет.</p>" +
  prompt("Промпт A · замена фона, товар неизменен",
    "[загрузи фото товара] Replace the cluttered background with a clean warm-lit premium studio "
    "backdrop. Keep the product, its label, shape and reflections exactly the same. Match the lighting "
    "and shadows to the new scene. Photorealistic.",
    "замени фон на чистую премиум-студию, товар, этикетку, форму и блики сохрани точно; свет подгони под сцену.") +
  prompt("Промпт B · один герой в серии кадров",
    "[загрузи портрет] Place the same person in a dark upscale studio with warm rim light. Keep the "
    "exact face, hairstyle and outfit unchanged. Editorial magazine look, 85mm lens, natural skin texture.",
    "тот же человек в тёмной студии с тёплым контровым светом; лицо, причёску и одежду не менять.") +
  """<div class="biz"><b>Приём</b>Текст на картинке (обложка, упаковка) — бери <b>Ideogram</b> или Nano Banana: «Add headline "ALOVLAB", clean bold type, perfectly legible, no distortion». Midjourney буквы ломает.</div>""" +
  biz("любой товар — карточки без съёмки; эксперт — линейка постов с одним лицом; упаковка и обложки с текстом.")
))

# ---------- P6 · Этап 2 · Видео (Higgsfield / Kling) ----------
P.append(page("Этап 2 · Видео · Higgsfield · Kling", 6,
  stage("Этап 2", "Видео · оживить кадр") +
  "<h2>Higgsfield и Kling — кадр оживает</h2>"
  "<p class=\"lead\">Готовую картинку превращаем в видео. Режим Image-to-Video: загруженный кадр — первый кадр клипа. Правило: одно фото — одно движение.</p>" +
  prompt("Формула промпта видео",
    "[объект + стабильность] + [одно движение камеры] + [движение среды] + [свет] + [ограничения]") +
  prompt("Готовый промпт · Higgsfield / Kling",
    "[загрузи кадр] The product stays completely stable while the camera makes a slow cinematic "
    "push-in. Delicate steam rises and gently curls upward. Warm amber light glides across the surface. "
    "Shallow depth of field. No deformation, no morphing, no sudden camera movement, no new objects.",
    "объект стабилен, камера медленно наезжает, пар вьётся вверх, тёплый свет скользит по поверхности; без деформаций.") +
  """<div class="mns">
    <div class="m move"><div class="h">▲ Двигается</div><p>камера (push-in / dolly), пар, блик света, пламя свечей.</p></div>
    <div class="m stay"><div class="h">■ Стоит на месте</div><p>сам объект, его форма, состав, геометрия сцены.</p></div>
  </div>
  <div class="biz"><b>Инструменты</b>Higgsfield — пресеты движения камеры и высокая стабильность. Kling — сильная физика и более длинные динамичные сцены. Выбор — под кадр.</div>""" +
  biz("реклама и промо-Reels; оживить карточку товара; атмосферный B-roll под закадровый голос.")
))

# ---------- P7 · Этап 3 · Голос (ElevenLabs) ----------
P.append(page("Этап 3 · Голос · ElevenLabs", 7,
  stage("Этап 3", "Голос · закадр") +
  "<h2>ElevenLabs — живой голос за кадром</h2>"
  "<p class=\"lead\">Здесь «промпт» — это сам текст и то, как он размечен. Модель читает ровно так, как ты записал: короткие фразы и точки дают паузы и дыхание.</p>" +
  prompt("Текст под озвучку · разметка паузами",
    "Пар над тарелкой — это не еда. Это обещание.\n"
    "Свет. Тишина. Подача. Вечер собирается до первого кусочка.\n"
    "Ты не заказываешь ужин. Ты бронируешь память.") +
  """<span class="kick" style="display:block;margin-top:12px">Настройки под спокойную подачу</span>
  <div class="paramwrap">
    <div class="param"><code>Stability 45–55</code><span><b>Живо, но не рвано.</b> Ниже — больше эмоции и разброса, выше — ровнее и монотоннее.</span></div>
    <div class="param"><code>Similarity 75</code><span><b>Ближе к тембру голоса.</b> Держит характер выбранного голоса.</span></div>
    <div class="param"><code>Style — низкий</code><span><b>Без переигровки.</b> Для наставнической спокойной интонации.</span></div>
    <div class="param"><code>Speed — чуть медленнее</code><span><b>Вес словам.</b> Премиум звучит неторопливо.</span></div>
  </div>
  <div class="biz"><b>Приёмы</b>Точка вместо запятой = пауза. Отдельная строка = вдох. Многоточие… = задержка перед сильной фразой. Пиши, как говоришь вслух.</div>""" +
  biz("озвучка Reels и Shorts без диктора; аудио для подкаста; дубляж роликов на другой язык.")
))

# ---------- P8 · Этап 4 · Аватар (HeyGen) ----------
P.append(page("Этап 4 · Аватар · HeyGen", 8,
  stage("Этап 4", "Аватар · говорящий двойник") +
  "<h2>HeyGen — двойник ведёт ролик</h2>"
  "<p class=\"lead\">Аватар держит внимание в начале и в конце, B-roll с озвучкой — в середине. Не вешай всё на аватар: он для лица и слова, а не для атмосферы.</p>" +
  prompt("Сценарий аватара · хук и финал",
    "[Хук · аватар в кадре]\n"
    "В слабом ресторане тебе подают блюдо. В сильном — сначала меняют твой вечер.\n\n"
    "[Финал · аватар в кадре]\n"
    "Хочешь такой вечер — стол уже ждёт. Бронь под роликом.") +
  """<div class="cards c2">
    <div class="card"><div class="ct">Кадр аватара</div><div class="ch">Тёмный фон, крупный план</div><p>Тёплый контровой свет, взгляд в камеру, минимум жестов — лицо стабильнее.</p></div>
    <div class="card"><div class="ct">Голос</div><div class="ch">Свяжи с ElevenLabs</div><p>Загрузи озвучку с этапа 3 или выбери голос — единая подача во всём ролике.</p></div>
  </div>
  <div class="biz"><b>Сборка</b>Аватар (хук) → B-roll с этапа 2 под голос с этапа 3 → аватар (финал) + логотип. Один герой прошёл весь конвейер.</div>""" +
  biz("эксперт и блогер — ролики каждый день без съёмок; отдел продаж — персональные видео; обучение и онбординг.")
))

# ---------- P9 · Сквозной прогон ----------
P.append(page("Сквозной прогон", 9, """
  <span class="kick">Один герой — весь конвейер</span>
  <h2>Как это собирается вместе</h2>
  <p class="lead">Возьмём одно блюдо ресторана и проведём его через все четыре этапа. Тот же принцип — для товара, эксперта, бренда.</p>
  <div class="scene"><div class="sn">1</div><div><div class="sh">Картинка</div><div class="sd"><b>Midjourney</b> рисует премиум-кадр гребешка. Есть своё фото — <b>Nano Banana</b> меняет фон, товар неизменен.</div></div><span class="stag">кадр 4:5 / 9:16</span></div>
  <div class="scene"><div class="sn">2</div><div><div class="sh">Видео</div><div class="sd"><b>Higgsfield / Kling</b> оживляют кадр: медленный наезд, пар вьётся, объект стабилен.</div></div><span class="stag">клип 3–4 сек</span></div>
  <div class="scene"><div class="sn">3</div><div><div class="sh">Голос</div><div class="sd"><b>ElevenLabs</b> читает закадр спокойно, с паузами. Точки и строки задают дыхание.</div></div><span class="stag">закадр</span></div>
  <div class="scene"><div class="sn">4</div><div><div class="sh">Аватар</div><div class="sd"><b>HeyGen</b> открывает хуком и закрывает призывом. Между ними — B-roll под голос.</div></div><span class="stag">хук + финал</span></div>
  <div class="callout result"><div class="h">Что на выходе</div><p>Вертикальный ролик, собранный из четырёх нейросетей за вечер — то, за что раньше платили смену, команду и студию. Это и есть конвейер, а не одна генерация.</p></div>
"""))

# ---------- P10 · Чек-лист ----------
P.append(page("Чек-лист · честность", 10, """
  <span class="kick">Контроль</span>
  <h2>Проверь конвейер перед выдачей</h2>
  <div class="callout check"><div class="h">Чек-лист по этапам</div>
    <div class="row">Картинка: один стиль/свет на всю серию (--sref или референс)</div>
    <div class="row">Правки: товар и лицо остались неизменными, текст читается</div>
    <div class="row">Видео: объект стабилен, движется только камера и среда</div>
    <div class="row">Голос: слышен, громче музыки, паузы на месте</div>
    <div class="row">Аватар: лицо стабильно, кадр простой, взгляд в камеру</div>
    <div class="row">Формат под площадку: 9:16 вертикаль для Reels/Shorts</div>
  </div>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Ошибка новичка</div>Один инструмент на всё и десять правок в одном промпте. Модель фантазирует, герой «плывёт».</div>
    <div class="box good"><div class="lbl">✓ Как у профи</div>Каждый этап — свой инструмент, один кадр — одно действие, один герой держится через всю серию.</div>
  </div>
  <p class="note">Честно: кадры — концепт под бренд, а не «результат клиента». Никаких выдуманных цифр. Названия и возможности инструментов меняются — держись логики этапов, а не кнопок.</p>
"""))

# ---------- P11 · CTA ----------
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Забери весь набор промптов<br>для <span style="color:var(--o2)">конвейера.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:46ch;margin:0 auto 20px">Шпаргалка «что чем делать», готовые промпты на все четыре этапа и приёмы: --sref, --cref, редактура, консистентность, разметка голоса. Собери свой ролик за вечер.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Промпты → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">VK · vk.com/alovlab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Гайд · Контент-конвейер на нейросетях · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
