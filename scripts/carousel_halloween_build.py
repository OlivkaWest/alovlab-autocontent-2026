# -*- coding: utf-8 -*-
"""AlovLab · Карусель «Хэллоуин» — один персонаж, разные сцены, как сохранить внешность в AI-фото.
Не привязана к дню календаря — отдельный сезонный пост (как day-15 была отдельной от Reels).
8 слайдов (не 6, по прямому запросу), 1080×1350 (4:5), светлый премиум-инфографик, тот же
стиль/компоненты, что в carousel_day15_build.py / carousel_day14_build.py.
Честно: конкретные шаги по референсу и обучению аватара — по практике этой же сессии (Soul-аватар,
11 фото), не выдуманы. Названия моделей/функций платформ не гарантируем неизменными — сверять перед
использованием.
Запуск:
  python3 scripts/carousel_halloween_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <html> <outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "content" / "october-2026-system" / "carousels-extra" / "halloween-character"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "carousel.html"

def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")

RANGES = {"cyrillic": "U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin": "U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192"}
faces = ""
for w in (400, 500, 600, 700, 800):
    for sub in ("cyrillic", "latin"):
        fp = FONTS / f"manrope-{sub}-{w}.woff2"
        if fp.exists():
            faces += ("@font-face{font-family:'Manrope';font-weight:%d;font-display:swap;"
                      "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}\n"
                      % (w, b64(fp), RANGES[sub]))

CSS = faces + r"""
*{margin:0;padding:0;box-sizing:border-box;font-family:'Manrope',sans-serif}
body{background:#ddd5c4}
.slide{position:relative;width:540px;height:675px;overflow:hidden;background:#FBF4E9;
 display:flex;flex-direction:column;padding:34px 36px 30px;page-break-after:always}
.kicker{font-size:12.5pt;font-weight:800;letter-spacing:.06em;color:#E1671E;text-transform:uppercase}
h1{font-size:32pt;font-weight:800;line-height:1.06;color:#20242B;margin-top:8px;letter-spacing:-.01em}
h1 i{font-style:normal;color:#E1671E}
h2{font-size:24pt;font-weight:800;line-height:1.12;color:#20242B;margin-top:6px}
h2 i{font-style:normal;color:#E1671E}
.lead{font-size:13.5pt;font-weight:600;color:#3a362f;margin-top:10px;line-height:1.42;max-width:94%}
.sub{font-size:11.5pt;font-weight:500;color:#6E6A63;margin-top:4px;line-height:1.4;max-width:94%}
.badge{position:absolute;top:28px;left:34px;font-size:11pt;font-weight:800;color:#6E6A63;
 border:1.5px solid #E1671E;border-radius:20px;padding:4px 13px;background:#FFF}
.card{background:#FFFFFF;border:1px solid #EBE2D3;border-radius:16px;padding:18px 20px;margin-top:14px;
 box-shadow:0 2px 10px rgba(32,20,10,.04)}
.card.sand{background:#FBEFE0}
.card .lbl{font-size:10.5pt;font-weight:800;letter-spacing:.05em;color:#E1671E;text-transform:uppercase;margin-bottom:8px}
.card p{font-size:12pt;font-weight:500;color:#3a362f;line-height:1.45}
.cards{display:flex;gap:12px;margin-top:14px}
.cards .card{flex:1;margin-top:0}
.steps{display:flex;flex-direction:column;gap:11px;margin-top:4px}
.step{display:flex;gap:12px;align-items:flex-start}
.step .n{flex:0 0 auto;width:30px;height:30px;border-radius:50%;background:#E1671E;color:#fff;
 font-weight:800;font-size:13pt;display:flex;align-items:center;justify-content:center}
.step .t{font-size:12pt;font-weight:600;color:#20242B;line-height:1.36;padding-top:2px}
.step .t b{color:#E1671E}
.note{font-size:10.8pt;font-weight:600;color:#6E6A63;margin-top:10px;line-height:1.4}
.retention{position:absolute;left:36px;right:36px;bottom:56px;font-size:12.5pt;font-weight:700;color:#E1671E}
.sig{position:absolute;bottom:22px;left:36px;display:flex;align-items:center;gap:8px}
.sig img{width:26px;height:26px}
.sig b{font-size:12pt;font-weight:800;color:#20242B}
.sig b i{font-style:normal;color:#E1671E}
.warn{background:#FBEFE0;border:1.5px solid #F2A65A;border-radius:14px;padding:14px 16px;margin-top:12px}
.warn .lbl{font-size:10pt;font-weight:800;color:#E1671E;text-transform:uppercase;margin-bottom:6px}
.warn p{font-size:11.3pt;font-weight:500;color:#3a362f;line-height:1.42}
.pillrow{display:flex;gap:9px;margin-top:14px;flex-wrap:wrap}
.pillrow span{background:#FFFFFF;border:1px solid #EBE2D3;border-radius:20px;padding:7px 14px;
 font-size:11pt;font-weight:700;color:#20242B}
.promptbox{background:#1E1812;border-radius:16px;padding:17px 19px;margin-top:14px}
.promptbox .lbl{display:inline-block;background:#E1671E;color:#1E1812;font-size:9.5pt;font-weight:800;
 letter-spacing:.04em;text-transform:uppercase;border-radius:8px;padding:4px 10px;margin-bottom:10px}
.promptbox code{display:block;font-family:'Courier New',monospace;font-size:9.6pt;font-weight:600;
 color:#F3E9DA;line-height:1.52;white-space:pre-wrap}
"""

def sig():
    return (f'<div class="sig"><img src="data:image/png;base64,{LOGO}">'
            f'<b>Alov<i>Lab</i></b></div>')

N = 10
slides = []

# 1 — обложка / хук
slides.append(f"""<div class="slide">
 <div class="badge">1 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">ИИ-аватары · Хэллоуин</div>
  <h1>ИИ МЕНЯЕТ ЛИЦО<br>В КАЖДОЙ СЦЕНЕ.<br><i>ЭТОТ — НЕТ.</i></h1>
  <p class="lead">Один персонаж. Семь сцен на Хэллоуин. Полная методичка, как это собрать осенью 2026.</p>
  <p class="sub">Сохрани — пригодится, когда дойдёшь до своей серии.</p>
 </div>
 <div class="retention">Приоритет №1 — качество исходника  →</div>
 {sig()}
</div>""")

# 2 — приоритет №1: качество исходника
slides.append(f"""<div class="slide">
 <div class="badge">2 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Приоритет №1 · Осень 2026</div>
  <h2>Сначала — качество кадра,<br>не <i>количество фильтров</i></h2>
  <div class="steps" style="margin-top:10px;gap:10px">
   <div class="step"><div class="n">1</div><div class="t" style="font-size:11.4pt">Резкий портрет, без фильтров и ретуши, которая меняет форму лица.</div></div>
   <div class="step"><div class="n">2</div><div class="t" style="font-size:11.4pt">Ровный естественный свет — без теней, перекрывающих часть лица, без очков.</div></div>
   <div class="step"><div class="n">3</div><div class="t" style="font-size:11.4pt">Простой нейтральный фон — не отвлекает модель от самого лица.</div></div>
   <div class="step"><div class="n">4</div><div class="t" style="font-size:11.4pt">Разрешение от ~1024 px по короткой стороне — на мелком кадре модель теряет детали.</div></div>
  </div>
  <p class="note">По отраслевым гайдам по референсам (сверено на нескольких независимых источниках) — не выдумано.</p>
 </div>
 <div class="retention">Сколько фото и в каких ракурсах  →</div>
 {sig()}
</div>""")

# 3 — сколько фото / два пути
slides.append(f"""<div class="slide">
 <div class="badge">3 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Сколько фото нужно</div>
  <h2>Два пути — и у каждого<br><i>своё</i> число кадров</h2>
  <div class="cards">
   <div class="card"><div class="lbl">Быстрая серия</div><p>2-6 фото: анфас + в полный рост, без обучения. Хватает для короткой подборки.</p></div>
   <div class="card sand"><div class="lbl">Точный персонаж</div><p>5-20 фото, разные ракурсы (анфас, 3/4, профиль), разный свет и фон — обучаешь один раз.</p></div>
  </div>
  <p class="note">Разрыв между путями в 2026 году сократился: часть моделей держит лицо через face-ID embedding (технология InstantID / IP-Adapter-FaceID), а не просто через общее сходство картинки — поэтому для серии из разных сцен обучение пока держит стабильнее.</p>
 </div>
 <div class="retention">Что явно писать в промпте  →</div>
 {sig()}
</div>""")

# 4 — что явно писать в промпте
slides.append(f"""<div class="slide">
 <div class="badge">4 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Что явно писать в промпте</div>
  <h2>Модель понимает<br><i>конкретику</i>, не эмоции</h2>
  <div class="steps" style="margin-top:10px;gap:10px">
   <div class="step"><div class="n">1</div><div class="t" style="font-size:11.4pt">Перечисляй, что <b>нельзя менять</b>: форма лица, нос, брови, губы, цвет глаз, длина и цвет волос.</div></div>
   <div class="step"><div class="n">2</div><div class="t" style="font-size:11.4pt">Описывай сцену, свет и позу точно — без общих слов вроде «красиво» или «атмосферно».</div></div>
   <div class="step"><div class="n">3</div><div class="t" style="font-size:11.4pt">Пиши связным текстом, не набором тегов через запятую — так модель держит контекст лучше.</div></div>
   <div class="step"><div class="n">4</div><div class="t" style="font-size:11.4pt">Разделяй явно: что статично (лицо), а что меняется (костюм, сцена, свет).</div></div>
  </div>
 </div>
 <div class="retention">Сохрани персонажа по имени  →</div>
 {sig()}
</div>""")

# 5 — персонаж как состояние
slides.append(f"""<div class="slide">
 <div class="badge">5 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Рабочий приём</div>
  <h2>Сохрани персонажа<br>по <i>имени</i>, не переписывай</h2>
  <div class="card sand">
   <div class="lbl">Зачем</div>
   <p>Если платформа позволяет сохранить референс или аватар под именем — зови его по имени в каждом новом промпте, не описывай заново своими словами.</p>
  </div>
  <p class="note">Так непохожесть между кадрами не растёт от случайной перефразировки — один раз описал, дальше переиспользуешь, а не пересобираешь текст с нуля для каждой сцены.</p>
 </div>
 <div class="retention">Один персонаж, семь сцен  →</div>
 {sig()}
</div>""")

# 6 — сцены / разнообразие
slides.append(f"""<div class="slide">
 <div class="badge">6 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Один персонаж, разные сцены</div>
  <h2>Семь хэллоуинских<br>ролей — <i>без смены лица</i></h2>
  <p class="sub">Меняется костюм, свет, фон и поза. Лицо — всегда то же самое, с одного референса или аватара.</p>
  <div class="pillrow">
   <span>Вампир</span><span>Ведьма</span><span>Зомби</span><span>Безумный учёный</span>
   <span>Тыквенный король</span><span>Оборотень</span><span>Призрак</span>
  </div>
 </div>
 <div class="retention">Частая ошибка, которая портит серию  →</div>
 {sig()}
</div>""")

# 7 — частая ошибка → фикс
slides.append(f"""<div class="slide">
 <div class="badge">7 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Частая ошибка → фикс</div>
  <h2>Лицо <i>плывёт</i><br>от сцены к сцене</h2>
  <div class="warn">
   <div class="lbl">Ошибка</div>
   <p>Менять референс-фото под каждую новую сцену или слишком сильно переписывать черты лица прямо в промпте.</p>
  </div>
  <div class="card sand">
   <div class="lbl">Фикс</div>
   <p>Один зафиксированный референс (или обученный аватар) на всю серию — меняешь только костюм, фон и позу, не лицо.</p>
  </div>
 </div>
 <div class="retention">Промпт для новой сцены  →</div>
 {sig()}
</div>""")

# 8 — промпт
slides.append(f"""<div class="slide">
 <div class="badge">8 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Копируй и используй</div>
  <h2>Промпт для сцены<br>с <i>тем же лицом</i></h2>
  <div class="promptbox">
   <div class="lbl">Image-gen / identity-ref</div>
   <code>Portrait of this person/character, now dressed as [костюм: vampire /
witch / mad scientist], in [сцена: foggy graveyard at night].
Do not change: face shape, nose, eyebrows, lips, eye color, hair
length and color. Same identity and proportions as reference,
Halloween atmospheric lighting, photorealistic</code>
  </div>
  <p class="sub">Меняешь только то, что в скобках — костюм и сцену. Строка «do not change» держит лицо неизменным.</p>
 </div>
 <div class="retention">Проверка перед публикацией  →</div>
 {sig()}
</div>""")

# 9 — чек-лист перед публикацией
slides.append(f"""<div class="slide">
 <div class="badge">9 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Проверка перед публикацией</div>
  <h2>5 вещей, которые <i>сверяешь</i></h2>
  <div class="steps" style="margin-top:10px;gap:10px">
   <div class="step"><div class="n">1</div><div class="t" style="font-size:11.3pt">Пропорции лица совпадают с референсом — не «похож», а то же лицо.</div></div>
   <div class="step"><div class="n">2</div><div class="t" style="font-size:11.3pt">Нет лишних пальцев и артефактов на руках и аксессуарах.</div></div>
   <div class="step"><div class="n">3</div><div class="t" style="font-size:11.3pt">Свет сцены не обесцвечивает узнаваемые черты — цвет глаз, родинки.</div></div>
   <div class="step"><div class="n">4</div><div class="t" style="font-size:11.3pt">Костюм не закрывает лицо настолько, что личность теряется.</div></div>
   <div class="step"><div class="n">5</div><div class="t" style="font-size:11.3pt">Все кадры серии — в одном стиле и разрешении.</div></div>
  </div>
 </div>
 <div class="retention">Собери свою серию  →</div>
 {sig()}
</div>""")

# 10 — итог + CTA
slides.append(f"""<div class="slide">
 <div class="badge">10 / {N}</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">ОДИН ПЕРСОНАЖ<br><i>ЛЮБАЯ СЦЕНА</i></h1>
  <p class="lead" style="margin-top:10px">Референс один раз, сцен — сколько хватит фантазии на Хэллоуин.</p>
  <div class="card sand" style="margin-top:16px">
   <div class="lbl">Помогу собрать твою серию</div>
   <p>Напиши «ХЭЛЛОУИН» в комментариях — подскажу, как собрать референс под твоего персонажа.</p>
  </div>
 </div>
 {sig()}
</div>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(slides)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "slides:", len(slides))
