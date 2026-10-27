# -*- coding: utf-8 -*-
"""AlovLab · Карусель «Реклама красивая. Товар — другой.» — та же CORE IDEA, что в Reels дня 6
серии «Нейромонах. Доводим до дела» (content/dovodim-do-dela/plan/plan-30-dney.csv, День 6,
27.10.2026, тема «Красивый, но другой товар»). Карусель — отдельный параллельный формат по
прямому запросу пользователя («карусель дня» → «собери»), на активном плане carousel-слота нет
(content/strategy/CONTENT-PLAN.md не ведётся с сентября), поэтому используется та же CORE IDEA.
Светлый премиум-инфографик (GLOBAL-CAROUSEL-RULE §13-Б), тот же стиль/компоненты, что в
carousel_day19_build.py. 6 слайдов 1080×1350 (4:5), RU + EN.
Честно: демонстрация на нейтральном предмете (керамическая кружка), реального клиентского кейса
нет — метод и промпт рабочие, не привязаны к выдуманному заказу.
Запуск:
  python3 scripts/carousel_dovodim_day06_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <ru_html> <ru_outdir>
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <en_html> <en_outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
BASE_OUT = ROOT / "content" / "dovodim-do-dela" / "carousels" / "day-06"

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
h1{font-size:34pt;font-weight:800;line-height:1.04;color:#20242B;margin-top:8px;letter-spacing:-.01em}
h1 i{font-style:normal;color:#E1671E}
h2{font-size:25pt;font-weight:800;line-height:1.1;color:#20242B;margin-top:6px}
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
.steps{display:flex;flex-direction:column;gap:12px;margin-top:4px}
.step{display:flex;gap:12px;align-items:flex-start}
.step .n{flex:0 0 auto;width:30px;height:30px;border-radius:50%;background:#E1671E;color:#fff;
 font-weight:800;font-size:13pt;display:flex;align-items:center;justify-content:center}
.step .t{font-size:12.3pt;font-weight:600;color:#20242B;line-height:1.38;padding-top:2px}
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
.gb{display:flex;gap:12px;margin-top:4px}
.gb .box{flex:1;border-radius:14px;padding:14px 16px}
.gb .box.bad{background:#FCEEEA;border:1px solid #EFC7BB}
.gb .box.good{background:#EAF3EC;border:1px solid #BFDCC6}
.gb .lbl{font-size:10pt;font-weight:800;text-transform:uppercase;margin-bottom:6px}
.gb .bad .lbl{color:#C0492E}
.gb .good .lbl{color:#3E8E55}
.gb p{font-size:11pt;font-weight:500;color:#3a362f;line-height:1.4}
.prompt{background:#1b1510;border-radius:16px;padding:18px 20px;margin-top:14px;color:#f2eadf}
.prompt .plbl{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.prompt .plbl .tag{font-weight:800;font-size:9.5pt;letter-spacing:.1em;text-transform:uppercase;color:#1b1510;
 background:#FFB066;border-radius:8px;padding:4px 10px}
.prompt .plbl .copy{font-weight:700;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;color:#cbb39d}
.prompt code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:10.3pt;
 line-height:1.56;white-space:pre-wrap;color:#f2eadf}
"""

def sig():
    return (f'<div class="sig"><img src="data:image/png;base64,{LOGO}">'
            f'<b>Alov<i>Lab</i></b></div>')

def build(lang):
    slides = []
    if lang == "ru":
        # 1 — обложка / конфликт
        slides.append(f"""<div class="slide">
 <div class="badge">1 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Товарные генерации</div>
  <h1>РЕКЛАМА<br>КРАСИВАЯ.<br><i>ТОВАР —<br>ДРУГОЙ.</i></h1>
  <p class="lead">Как проверить генерацию, прежде чем сдать клиенту.</p>
 </div>
 <div class="retention">Почему так выходит  →</div>
 {sig()}
</div>""")
        # 2 — причина
        slides.append(f"""<div class="slide">
 <div class="badge">2 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Разрушаем миф</div>
  <h2>Нейросеть<br>дорисовывает <i>то,<br>на что не смотрят.</i></h2>
  <p class="lead" style="font-size:12pt">Чаще всего плывёт то, что не в фокусе промпта: форма ручки, застёжка, носик, пропорции.</p>
  <div class="note">Текст в кадре выглядит правильно. Форма — уже нет.</div>
 </div>
 <div class="retention">Метод проверки  →</div>
 {sig()}
</div>""")
        # 3 — техника / авторский метод
        slides.append(f"""<div class="slide">
 <div class="badge">3 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Авторский метод</div>
  <h2>Правило <i>трёх<br>точек</i></h2>
  <div class="steps" style="margin-top:10px">
   <div class="step"><div class="n">1</div><div class="t"><b>Силуэт.</b> Наложи исходник и генерацию друг на друга — контур должен совпасть.</div></div>
   <div class="step"><div class="n">2</div><div class="t"><b>Функциональные детали.</b> Ручка, крышка, застёжка, кнопка — пересчитать поштучно.</div></div>
   <div class="step"><div class="n">3</div><div class="t"><b>Пропорции.</b> Ширина к высоте — сверяй с исходником, не на глаз.</div></div>
  </div>
 </div>
 <div class="retention">Рабочий промпт  →</div>
 {sig()}
</div>""")
        # 4 — промпт
        slides.append(f"""<div class="slide">
 <div class="badge">4 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Сохрани этот промпт</div>
  <h2>Добавь в конец<br>любого <i>промпта<br>товара</i></h2>
  <div class="prompt">
   <div class="plbl"><span class="tag">Промпт</span><span class="copy">скопировать</span></div>
   <code>Сохрани точную форму, пропорции и материал товара
с референсного фото: [ОПИСАНИЕ ТОВАРА].
Не меняй форму ручки, крышки, носика и других
функциональных деталей.
Меняй только: фон, свет, ракурс камеры, композицию.
Никаких отклонений от геометрии оригинала.</code>
  </div>
 </div>
 <div class="retention">Если несовпадение найдено  →</div>
 {sig()}
</div>""")
        # 5 — ошибка + фикс
        slides.append(f"""<div class="slide">
 <div class="badge">5 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Ошибка → фикс</div>
  <h2>Нашёл<br>несовпадение —<br><i>что делать</i></h2>
  <div class="warn">
   <div class="lbl">Не так</div>
   <p>Перегенерировать с нуля в надежде, что в этот раз повезёт.</p>
  </div>
  <div class="card sand">
   <div class="lbl">Так</div>
   <p>Зафиксировать форму, менять только фон и свет. Если деталь всё равно плывёт — назвать её прямо словами в промпте.</p>
  </div>
 </div>
 <div class="retention">Сохрани чек-лист  →</div>
 {sig()}
</div>""")
        # 6 — финал + CTA
        slides.append(f"""<div class="slide">
 <div class="badge">6 / 6</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">СОХРАНИ<i>.</i></h1>
  <p class="lead" style="margin-top:10px">Проверяй форму товара по правилу трёх точек до того, как отправишь клиенту.</p>
  <div class="card sand" style="margin-top:16px">
   <div class="lbl">Шаблон проверки</div>
   <p>Чек-лист и промпт целиком — в закрепе в Telegram.</p>
  </div>
 </div>
 {sig()}
</div>""")
    else:
        # EN
        slides.append(f"""<div class="slide">
 <div class="badge">1 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Product generations</div>
  <h1>THE AD<br>LOOKS GREAT.<br><i>THE PRODUCT<br>DOESN'T MATCH.</i></h1>
  <p class="lead">How to check a generation before you ship it.</p>
 </div>
 <div class="retention">Why it happens  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">2 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Breaking the myth</div>
  <h2>The model<br>redraws <i>what<br>nobody's watching.</i></h2>
  <p class="lead" style="font-size:12pt">It's usually the stuff outside the prompt's focus: handle shape, clasp, spout, proportions.</p>
  <div class="note">The copy in frame reads fine. The shape already doesn't.</div>
 </div>
 <div class="retention">The check method  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">3 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">The method</div>
  <h2>The three-point<br><i>rule</i></h2>
  <div class="steps" style="margin-top:10px">
   <div class="step"><div class="n">1</div><div class="t"><b>Silhouette.</b> Overlay the source and the generation — the outline has to match.</div></div>
   <div class="step"><div class="n">2</div><div class="t"><b>Functional details.</b> Handle, lid, clasp, button — count them one by one.</div></div>
   <div class="step"><div class="n">3</div><div class="t"><b>Proportions.</b> Width to height against the source, not by eye.</div></div>
  </div>
 </div>
 <div class="retention">The working prompt  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">4 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Save this prompt</div>
  <h2>Append this to<br>any <i>product<br>prompt</i></h2>
  <div class="prompt">
   <div class="plbl"><span class="tag">Prompt</span><span class="copy">copy</span></div>
   <code>Preserve the exact shape, proportions and material
of the product from the reference photo:
[PRODUCT DESCRIPTION].
Do not alter the shape of the handle, lid, spout
or other functional details.
Change only: background, lighting, camera angle,
composition. No deviation from the original geometry.</code>
  </div>
 </div>
 <div class="retention">If you find a mismatch  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">5 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Mistake → fix</div>
  <h2>Found a<br>mismatch —<br><i>what to do</i></h2>
  <div class="warn">
   <div class="lbl">Not this</div>
   <p>Regenerate from scratch and hope it works this time.</p>
  </div>
  <div class="card sand">
   <div class="lbl">This</div>
   <p>Lock the shape, change only background and light. If a detail still drifts, name it explicitly in the prompt.</p>
  </div>
 </div>
 <div class="retention">Save the checklist  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">6 / 6</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">SAVE<i>.</i></h1>
  <p class="lead" style="margin-top:10px">Check the product shape with the three-point rule before you send it to the client.</p>
  <div class="card sand" style="margin-top:16px">
   <div class="lbl">Check template</div>
   <p>The full checklist and prompt — pinned on Telegram.</p>
  </div>
 </div>
 {sig()}
</div>""")

    outdir = BASE_OUT / lang
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / "carousel.html"
    html = ("<!doctype html><html lang=%s><head><meta charset=utf-8>"
            "<style>%s</style></head><body>%s</body></html>"
            % (lang, CSS, "".join(slides)))
    out.write_text(html, encoding="utf-8")
    print("HTML:", out, "slides:", len(slides))

build("ru")
build("en")
