# -*- coding: utf-8 -*-
"""AlovLab · Карусель «Сменил нейросеть. Забыл исправить задание.» — та же CORE IDEA, что в Reels
дня 19 серии «Нейромонах. Доводим до дела» (content/dovodim-do-dela/plan/plan-30-dney.csv, День 19,
09.11.2026, формат А «Узнал себя», тема «Смена инструмента вместо исправления»). Carousel-слота в
действующем плане нет (content/strategy/CONTENT-PLAN.md не ведётся с сентября, dovodim-do-dela
зарезервирован за «Рилс дня») — используется та же CORE IDEA, тот же подход, что уже был согласован
пользователем для дня 06 (carousel_dovodim_day06_build.py).
Светлый премиум-инфографик (GLOBAL-CAROUSEL-RULE §13-Б), тот же стиль/компоненты, что в
carousel_dovodim_day06_build.py / carousel_day19_build.py (архивный). 6 слайдов 1080×1350 (4:5), RU + EN.
Честно: демонстрации на реальном кейсе нет (план просит её для Reels, не для карусели) — метод и
промпт рабочие, общий принцип, не привязаны к выдуманному заказу.
Запуск:
  python3 scripts/carousel_dovodim_day19_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <ru_html> <ru_outdir>
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <en_html> <en_outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
BASE_OUT = ROOT / "content" / "dovodim-do-dela" / "carousels" / "day-19"

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
h1{font-size:33pt;font-weight:800;line-height:1.06;color:#20242B;margin-top:8px;letter-spacing:-.01em}
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
.prompt{background:#1b1510;border-radius:16px;padding:18px 20px;margin-top:14px;color:#f2eadf}
.prompt .plbl{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.prompt .plbl .tag{font-weight:800;font-size:9.5pt;letter-spacing:.1em;text-transform:uppercase;color:#1b1510;
 background:#FFB066;border-radius:8px;padding:4px 10px}
.prompt .plbl .copy{font-weight:700;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;color:#cbb39d}
.prompt code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:10.8pt;
 line-height:1.56;white-space:pre-wrap;color:#f2eadf}
.checklist{display:flex;flex-direction:column;gap:10px;margin-top:4px}
.checklist .c{display:flex;gap:11px;align-items:flex-start;background:#fff;border:1px solid #EBE2D3;
 border-radius:12px;padding:11px 14px}
.checklist .c .box{flex:0 0 auto;width:22px;height:22px;border-radius:6px;border:2px solid #E1671E}
.checklist .c p{font-size:11.3pt;font-weight:600;color:#20242B;line-height:1.4}
"""

def sig():
    return (f'<div class="sig"><img src="data:image/png;base64,{LOGO}">'
            f'<b>Alov<i>Lab</i></b></div>')

def build(lang):
    slides = []
    N = 6
    if lang == "ru":
        slides.append(f"""<div class="slide">
 <div class="badge">1 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Промпты, не подписки</div>
  <h1>СМЕНИЛ<br>НЕЙРОСЕТЬ.<br><i>ЗАБЫЛ<br>ИСПРАВИТЬ<br>ЗАДАНИЕ.</i></h1>
  <p class="lead">Почему новая подписка не чинит старый промпт.</p>
 </div>
 <div class="retention">Дело не в модели  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">2 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Разрушаем миф</div>
  <h2>Ты меняешь<br>инструмент. <i>Задание<br>остаётся тем же.</i></h2>
  <p class="lead" style="font-size:12pt">Большинство плохих ответов — не слабая модель, а неполная постановка: нет исходных данных, нет критерия «что считать готовым».</p>
  <div class="warn"><p>Новая модель отвечает на тот же неполный вопрос — и выдаёт тот же результат, только с другим акцентом.</p></div>
 </div>
 <div class="retention">Что именно чинить  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">3 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Авторский метод</div>
  <h2>Правило <i>двух<br>вещей</i></h2>
  <div class="steps" style="margin-top:10px">
   <div class="step"><div class="n">1</div><div class="t"><b>Исходные данные.</b> Что именно у тебя уже есть — цифры, текст, пример, ссылка. Без них модель додумывает за тебя.</div></div>
   <div class="step"><div class="n">2</div><div class="t"><b>Критерий результата.</b> Как выглядит готовый ответ и по какому признаку ты его примешь. Без критерия модель не знает, когда остановиться.</div></div>
  </div>
 </div>
 <div class="retention">Рабочий промпт  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">4 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Сохрани этот промпт</div>
  <h2>Добавь это<br>в любой <i>незакрытый<br>запрос</i></h2>
  <div class="prompt">
   <div class="plbl"><span class="tag">Промпт</span><span class="copy">скопировать</span></div>
   <code>Вот исходные данные: [ЧТО У ТЕБЯ ЕСТЬ].
Нужен результат: [ЧТО ИМЕННО СЧИТАТЬ ГОТОВЫМ].
Если данных не хватает для точного ответа,
сначала задай мне уточняющие вопросы,
не угадывай.</code>
  </div>
 </div>
 <div class="retention">Чек-лист перед сменой сервиса  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">5 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Прежде чем платить за новую подписку</div>
  <h2>Проверь<br><i>три вещи</i></h2>
  <div class="checklist">
   <div class="c"><div class="box"></div><p>Я дал исходные данные, не только идею в двух словах?</p></div>
   <div class="c"><div class="box"></div><p>Я назвал критерий готового результата?</p></div>
   <div class="c"><div class="box"></div><p>Я уже пробовал добавить недостающее сам, в том же сервисе?</p></div>
  </div>
  <div class="note">Один и тот же сервис — платить за тест новой подписки не нужно.</div>
 </div>
 <div class="retention">Сохрани и сделай сейчас  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">6 / {N}</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">СОХРАНИ<i>.</i></h1>
  <p class="lead" style="margin-top:10px">Добавь в свой следующий запрос исходные данные и критерий результата — прежде чем искать другую нейросеть.</p>
  <div class="card sand" style="margin-top:16px">
   <div class="lbl">Разбор под твою задачу</div>
   <p>Шаблон запроса — в закрепе в Telegram.</p>
  </div>
 </div>
 {sig()}
</div>""")
    else:
        slides.append(f"""<div class="slide">
 <div class="badge">1 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Prompts, not subscriptions</div>
  <h1>SWITCHED<br>THE MODEL.<br><i>FORGOT TO<br>FIX THE<br>REQUEST.</i></h1>
  <p class="lead">Why a new subscription doesn't fix an old prompt.</p>
 </div>
 <div class="retention">It's not the model  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">2 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Breaking the myth</div>
  <h2>You switch<br>the tool. <i>The request<br>stays the same.</i></h2>
  <p class="lead" style="font-size:12pt">Most bad answers aren't a weak model — they're an incomplete ask: no source data, no criteria for what counts as done.</p>
  <div class="warn"><p>The new model answers the same incomplete question — and gives you the same result, with a different accent.</p></div>
 </div>
 <div class="retention">What to actually fix  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">3 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">The method</div>
  <h2>The two-thing<br><i>rule</i></h2>
  <div class="steps" style="margin-top:10px">
   <div class="step"><div class="n">1</div><div class="t"><b>Source data.</b> What you already have — numbers, text, an example, a link. Without it the model guesses for you.</div></div>
   <div class="step"><div class="n">2</div><div class="t"><b>Success criteria.</b> What the finished answer looks like and how you'll judge it. Without it the model doesn't know when to stop.</div></div>
  </div>
 </div>
 <div class="retention">The working prompt  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">4 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Save this prompt</div>
  <h2>Add this to<br>any <i>unfinished<br>request</i></h2>
  <div class="prompt">
   <div class="plbl"><span class="tag">Prompt</span><span class="copy">copy</span></div>
   <code>Here's my source data: [WHAT YOU HAVE].
I need this result: [WHAT COUNTS AS DONE].
If there isn't enough data for an exact
answer, ask me clarifying questions first.
Don't guess.</code>
  </div>
 </div>
 <div class="retention">Check before you switch  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">5 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">Before you pay for a new subscription</div>
  <h2>Check<br><i>three things</i></h2>
  <div class="checklist">
   <div class="c"><div class="box"></div><p>Did I give source data, not just an idea in two words?</p></div>
   <div class="c"><div class="box"></div><p>Did I name the success criteria?</p></div>
   <div class="c"><div class="box"></div><p>Did I already try adding what's missing, in the same service?</p></div>
  </div>
  <div class="note">Same service — no need to pay to test a new one.</div>
 </div>
 <div class="retention">Save and do it now  →</div>
 {sig()}
</div>""")
        slides.append(f"""<div class="slide">
 <div class="badge">6 / {N}</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">SAVE<i>.</i></h1>
  <p class="lead" style="margin-top:10px">Add source data and success criteria to your next request — before you go looking for a different model.</p>
  <div class="card sand" style="margin-top:16px">
   <div class="lbl">Breakdown for your case</div>
   <p>Request template — pinned on Telegram.</p>
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
