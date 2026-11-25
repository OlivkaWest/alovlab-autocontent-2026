# -*- coding: utf-8 -*-
"""AlovLab · Карусель «Видео без монтажа. Одна задача в чате.» — 23.11.2026.
CORE IDEA последнего Reels (content/reels/claude-code-remotion-demo/): объясняющий ролик собран
кодом в Remotion через Claude Code. Плана на 23.11 нет (dovodim-do-dela закончился 20.11,
CONTENT-PLAN.md не ведётся с сентября) — по согласованному правилу берём CORE IDEA последнего Reels.
Карусель показывает механику, доказательство — реальные кадры нашего рендера (assets/frame-0N.jpg,
вырезаны из remotion/render/collage.mp4, заглушка персонажа в кадр не попадает).
Светлый премиум-инфографик (GLOBAL-CAROUSEL-RULE §13-Б), компоненты из carousel_dovodim_day19_build.py.
7 слайдов 1080×1350 (4:5), RU + EN.
Запуск:
  python3 scripts/carousel_claude_video_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <ru_html> <ru_outdir>
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <en_html> <en_outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
BASE_OUT = ROOT / "content" / "carousels" / "claude-code-video-2026-11-23"

def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
FRAMES = [b64(BASE_OUT / "assets" / f"frame-0{i}.jpg") for i in (1, 2, 3)]

RANGES = {"cyrillic": "U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin": "U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192,U+00D7"}
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
.badge{position:absolute;top:28px;left:34px;font-size:11pt;font-weight:800;color:#6E6A63;
 border:1.5px solid #E1671E;border-radius:20px;padding:4px 13px;background:#FFF}
.card{background:#FFFFFF;border:1px solid #EBE2D3;border-radius:16px;padding:16px 18px;margin-top:14px;
 box-shadow:0 2px 10px rgba(32,20,10,.04)}
.card.sand{background:#FBEFE0}
.card .lbl{font-size:10.5pt;font-weight:800;letter-spacing:.05em;color:#E1671E;text-transform:uppercase;margin-bottom:7px}
.card p{font-size:12pt;font-weight:500;color:#3a362f;line-height:1.45}
.card p b{color:#20242B}
.steps{display:flex;flex-direction:column;gap:12px;margin-top:12px}
.step{display:flex;gap:12px;align-items:flex-start}
.step .n{flex:0 0 auto;width:30px;height:30px;border-radius:50%;background:#E1671E;color:#fff;
 font-weight:800;font-size:13pt;display:flex;align-items:center;justify-content:center}
.step .t{font-size:12.2pt;font-weight:600;color:#20242B;line-height:1.38;padding-top:2px}
.step .t b{color:#E1671E}
.note{font-size:10.8pt;font-weight:600;color:#6E6A63;margin-top:10px;line-height:1.4}
.retention{position:absolute;left:36px;right:36px;bottom:56px;font-size:12.5pt;font-weight:700;color:#E1671E}
.sig{position:absolute;bottom:22px;left:36px;display:flex;align-items:center;gap:8px}
.sig img{width:26px;height:26px}
.sig b{font-size:12pt;font-weight:800;color:#20242B}
.sig b i{font-style:normal;color:#E1671E}
.warn{background:#FBEFE0;border:1.5px solid #F2A65A;border-radius:14px;padding:13px 16px;margin-top:12px}
.warn .lbl{font-size:10pt;font-weight:800;color:#E1671E;text-transform:uppercase;margin-bottom:5px}
.warn p{font-size:11.3pt;font-weight:500;color:#3a362f;line-height:1.42}
.prompt{background:#1b1510;border-radius:16px;padding:16px 18px;margin-top:12px;color:#f2eadf}
.prompt .plbl{display:flex;align-items:center;justify-content:space-between;margin-bottom:9px}
.prompt .plbl .tag{font-weight:800;font-size:9.5pt;letter-spacing:.1em;text-transform:uppercase;color:#1b1510;
 background:#FFB066;border-radius:8px;padding:4px 10px}
.prompt .plbl .copy{font-weight:700;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;color:#cbb39d}
.prompt code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:10.3pt;
 line-height:1.52;white-space:pre-wrap;color:#f2eadf}
.frames{display:flex;gap:10px;margin-top:14px}
.frames figure{flex:1;background:#fff;border:1px solid #EBE2D3;border-radius:12px;padding:6px;
 box-shadow:0 2px 10px rgba(32,20,10,.05)}
.frames img{display:block;width:100%;border-radius:8px}
.frames figcaption{font-size:9.5pt;font-weight:700;color:#6E6A63;margin-top:5px;text-align:center}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px}
.chips span{font-size:10.5pt;font-weight:800;color:#20242B;background:#fff;border:1.5px solid #F2A65A;
 border-radius:20px;padding:4px 11px}
.pits{display:flex;flex-direction:column;gap:10px;margin-top:12px}
.pit{background:#fff;border:1px solid #EBE2D3;border-radius:12px;padding:11px 14px}
.pit .x{font-size:11.5pt;font-weight:800;color:#20242B;line-height:1.35}
.pit .x::before{content:"✕ ";color:#C23B2B}
.pit .f{font-size:11pt;font-weight:600;color:#3a362f;line-height:1.4;margin-top:4px}
.pit .f::before{content:"→ ";color:#E1671E;font-weight:800}
.hero{position:absolute;left:58px;right:58px;bottom:90px;background:#fff;border:1px solid #EBE2D3;
 border-radius:14px;padding:8px;transform:rotate(-2deg);box-shadow:0 14px 30px rgba(32,20,10,.14)}
.hero img{display:block;width:100%;border-radius:9px}
.hero .lbl{position:absolute;top:-10px;right:18px;background:#20242B;color:#fff;font-size:9.5pt;
 font-weight:800;letter-spacing:.06em;border-radius:8px;padding:4px 10px}
.checklist{display:flex;flex-direction:column;gap:8px;margin-top:14px}
.checklist .c{display:flex;gap:11px;align-items:center;background:#fff;border:1px solid #EBE2D3;
 border-radius:12px;padding:10px 14px}
.checklist .c .box{flex:0 0 auto;width:20px;height:20px;border-radius:6px;border:2px solid #E1671E}
.checklist .c p{font-size:11.3pt;font-weight:600;color:#20242B;line-height:1.35}
"""

def sig():
    return (f'<div class="sig"><img src="data:image/png;base64,{LOGO}">'
            f'<b>Alov<i>Lab</i></b></div>')

def frames(caps):
    return ('<div class="frames">' + "".join(
        f'<figure><img src="data:image/jpeg;base64,{FRAMES[i + 1]}"><figcaption>{c}</figcaption></figure>'
        for i, c in enumerate(caps)) + '</div>')

N = 7

T = {
 "ru": dict(
  s1=("Claude Code + Remotion",
      "ВИДЕО<br>БЕЗ МОНТАЖА.<br><i>ОДНА ЗАДАЧА<br>В ЧАТЕ.</i>",
      "37 секунд видео. Ни одного кадра руками.",
      "Как это устроено  →",
      "кадр из готового MP4"),
  s2=("Почему это вообще работает",
      "В Remotion<br>видео — <i>это код</i>",
      "Сцена = компонент. Время = номер кадра. Анимация = формула. А код пишет Claude Code.",
      "30 кадров = 1 секунда",
      "Сказал «сцена на 5 секунд» — это 150 кадров. Посчитать и разложить по таймлайну модель может сама.",
      "«Вайб кодинг» — слово года 2025 по версии Collins: задачу описываешь словами, код пишет ИИ. Видео — тот же вайб кодинг.",
      "4 шага до файла  →"),
  s3=("Схема",
      "От пустой папки<br><i>до MP4</i>",
      ["<b>Пустая папка</b> и Claude Code. Проверь, что стоит Node.js.",
       "<b>Задача:</b> тема, стиль, формат 1080×1920, сцены по секундам.",
       "<b>Claude</b> ставит Remotion, пишет сцены, запускает рендер.",
       "<b>Правки словами:</b> «акцент сделай синим», «сцену 3 на секунду короче»."],
      "Пока Claude работает, держи открытым превью Remotion Studio: каждую правку видно сразу, без нового рендера.",
      "Что вышло на деле  →"),
  s4=("Не скриншот из рекламы",
      "Реальный рендер<br><i>из нашего проекта</i>",
      ["сцена 2 · газетная карточка", "сцена 4 · задача в терминале"],
      ["1080×1920", "30 к/с", "1128 кадров", "37,6 с", "5 сцен"],
      "Персонаж в кадре пока заглушка. Лицо кодом не рисуется: его вставляют готовым клипом аватара.",
      "Задача целиком  →"),
  s5=("Сохрани задачу",
      "Промпт<br><i>для Claude Code</i>",
      "Тема ролика: [ТЕМА].\n"
      "Ты моушн-дизайнер и разработчик Remotion.\n"
      "Сделай объясняющее видео в стиле бумажного\n"
      "коллажа: вырезки, газетные заголовки,\n"
      "красный маркер.\n"
      "Формат: 1080×1920, 30 к/с, [N] сцен,\n"
      "длительность каждой сцены в секундах.\n"
      "Всё кодом в Remotion в этой папке: сам\n"
      "поставь зависимости и отрендери MP4.\n"
      "Перед сдачей проверь кадры, а не только код.",
      "Где споткнёшься  →"),
  s6=("Три подвоха",
      "Где споткнёшься<br><i>и как обойти</i>",
      [("Тайминг «на глаз»", "Задай каждой сцене секунды. Модель сама переведёт в кадры."),
       ("Лицо или персонаж", "Кодом не рисуется. Вставь готовый клип аватара или PNG."),
       ("Команда от 4 человек", "Remotion бесплатен для частных лиц и команд до 3 человек. Компаниям крупнее нужна платная лицензия.")],
      "Сделай свой  →"),
  s7=("СОХРАНИ<i>.</i>",
      "Возьми свою тему и прогони задачу: одна папка, один промпт, один рендер.",
      "Перед запуском",
      ["Node.js установлен", "Claude Code открыт в пустой папке", "Тема и длительность сцен в секундах"],
      "Полный промпт + чек-лист запуска",
      "В Telegram, ссылка в шапке профиля.",
      "Как ставить нейросети задачу так, чтобы она делала работу, разбираем на курсе «Нейросети и ChatGPT для каждого»."),
 ),
 "en": dict(
  s1=("Claude Code + Remotion",
      "VIDEO<br>WITHOUT EDITING.<br><i>ONE TASK<br>IN A CHAT.</i>",
      "37 seconds of video. Not one frame by hand.",
      "How it works  →",
      "a frame from the finished MP4"),
  s2=("Why this works at all",
      "In Remotion<br>video <i>is code</i>",
      "Scene = component. Time = frame number. Animation = formula. And Claude Code writes the code.",
      "30 frames = 1 second",
      "Say “a 5-second scene” and that's 150 frames. The model can do the math and lay out the timeline itself.",
      "“Vibe coding” is Collins' 2025 Word of the Year: you describe the task in words, AI writes the code. Video is vibe coding too.",
      "4 steps to a file  →"),
  s3=("The flow",
      "From an empty folder<br><i>to an MP4</i>",
      ["<b>An empty folder</b> and Claude Code. Make sure Node.js is installed.",
       "<b>The task:</b> topic, style, 1080×1920 format, scenes in seconds.",
       "<b>Claude</b> installs Remotion, writes the scenes, runs the render.",
       "<b>Edits in words:</b> “make the accent blue”, “cut scene 3 by a second”."],
      "While Claude works, keep the Remotion Studio preview open: every edit shows up instantly, no new render.",
      "What it actually made  →"),
  s4=("Not an ad screenshot",
      "A real render<br><i>from our project</i>",
      ["scene 2 · newspaper card", "scene 4 · task in the terminal"],
      ["1080×1920", "30 fps", "1,128 frames", "37.6 s", "5 scenes"],
      "The character is still a placeholder. A face can't be drawn in code: you drop in a ready avatar clip.",
      "The full task  →"),
  s5=("Save the task",
      "Prompt<br><i>for Claude Code</i>",
      "Video topic: [TOPIC].\n"
      "You're a motion designer and Remotion developer.\n"
      "Make an explainer video in a paper-collage\n"
      "style: cutouts, newspaper headlines,\n"
      "red marker.\n"
      "Format: 1080×1920, 30 fps, [N] scenes,\n"
      "each scene's length in seconds.\n"
      "Everything in Remotion code in this folder:\n"
      "install dependencies and render an MP4.\n"
      "Before you hand it over, check the frames,\n"
      "not just the code.",
      "Where you'll trip  →"),
  s6=("Three catches",
      "Where you'll trip<br><i>and how to avoid it</i>",
      [("Timing by eye", "Give every scene its seconds. The model converts them to frames."),
       ("A face or character", "Can't be drawn in code. Drop in a ready avatar clip or PNG."),
       ("A team of 4+", "Remotion is free for individuals and teams of up to 3. Bigger companies need a paid license.")],
      "Make your own  →"),
  s7=("SAVE<i>.</i>",
      "Take your own topic and run the task: one folder, one prompt, one render.",
      "Before you start",
      ["Node.js is installed", "Claude Code is open in an empty folder", "Topic and scene lengths in seconds"],
      "Full prompt + launch checklist",
      "On Telegram, link in bio.",
      "How to give AI a task so it actually does the work: we cover it in the course “AI and ChatGPT for Everyone”."),
 ),
}

def build(lang):
    t = T[lang]
    s = []
    k, h, lead, ret, hl = t["s1"]
    s.append(f"""<div class="slide">
 <div class="badge">1 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{k}</div>
  <h1>{h}</h1>
  <p class="lead">{lead}</p>
 </div>
 <div class="hero"><span class="lbl">{hl}</span><img src="data:image/jpeg;base64,{FRAMES[0]}"></div>
 <div class="retention">{ret}</div>
 {sig()}
</div>""")
    k, h, lead, lbl, p, fact, ret = t["s2"]
    s.append(f"""<div class="slide">
 <div class="badge">2 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{k}</div>
  <h2>{h}</h2>
  <p class="lead" style="font-size:12.3pt">{lead}</p>
  <div class="card"><div class="lbl">{lbl}</div><p>{p}</p></div>
  <div class="warn"><p>{fact}</p></div>
 </div>
 <div class="retention">{ret}</div>
 {sig()}
</div>""")
    k, h, steps, tip, ret = t["s3"]
    st = "".join(f'<div class="step"><div class="n">{i+1}</div><div class="t">{x}</div></div>'
                 for i, x in enumerate(steps))
    s.append(f"""<div class="slide">
 <div class="badge">3 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{k}</div>
  <h2>{h}</h2>
  <div class="steps">{st}</div>
  <div class="card sand" style="margin-top:16px"><p>{tip}</p></div>
 </div>
 <div class="retention">{ret}</div>
 {sig()}
</div>""")
    k, h, caps, chips, note, ret = t["s4"]
    ch = "".join(f"<span>{c}</span>" for c in chips)
    s.append(f"""<div class="slide">
 <div class="badge">4 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{k}</div>
  <h2>{h}</h2>
  {frames(caps)}
  <div class="chips">{ch}</div>
  <div class="note">{note}</div>
 </div>
 <div class="retention">{ret}</div>
 {sig()}
</div>""")
    k, h, code, ret = t["s5"]
    tag, copy = ("Промпт", "скопировать") if lang == "ru" else ("Prompt", "copy")
    s.append(f"""<div class="slide">
 <div class="badge">5 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{k}</div>
  <h2>{h}</h2>
  <div class="prompt">
   <div class="plbl"><span class="tag">{tag}</span><span class="copy">{copy}</span></div>
   <code>{code}</code>
  </div>
 </div>
 <div class="retention">{ret}</div>
 {sig()}
</div>""")
    k, h, pits, ret = t["s6"]
    pt = "".join(f'<div class="pit"><div class="x">{x}</div><div class="f">{f}</div></div>' for x, f in pits)
    s.append(f"""<div class="slide">
 <div class="badge">6 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{k}</div>
  <h2>{h}</h2>
  <div class="pits">{pt}</div>
 </div>
 <div class="retention">{ret}</div>
 {sig()}
</div>""")
    h, lead, cl, items, lbl, p, course = t["s7"]
    ci = "".join(f'<div class="c"><div class="box"></div><p>{x}</p></div>' for x in items)
    s.append(f"""<div class="slide">
 <div class="badge">7 / {N}</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">{h}</h1>
  <p class="lead" style="margin-top:10px">{lead}</p>
  <div class="kicker" style="margin-top:16px;font-size:10.5pt">{cl}</div>
  <div class="checklist" style="margin-top:8px">{ci}</div>
  <div class="card sand" style="margin-top:14px">
   <div class="lbl">{lbl}</div>
   <p>{p}</p>
  </div>
  <div class="note" style="margin-top:14px">{course}</div>
 </div>
 {sig()}
</div>""")

    outdir = BASE_OUT / lang
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / "carousel.html"
    out.write_text("<!doctype html><html lang=%s><head><meta charset=utf-8><style>%s</style></head>"
                   "<body>%s</body></html>" % (lang, CSS, "".join(s)), encoding="utf-8")
    print("HTML:", out, "slides:", len(s))

build("ru")
build("en")
