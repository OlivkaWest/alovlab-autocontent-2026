# -*- coding: utf-8 -*-
"""AlovLab · Карусель «Чат-бот отвечает. Агент делает. Но только там, куда ты дал доступ.» — 25.11.2026.
Тема предложена 24.11 и утверждена пользователем («да»): рилс 22.10 «Агент — не чат-бот»
(content/october-2026-system/reels-extra/day-22/), карусели по нему не было. Доказательство —
реальный кейс этой недели: агент сам собрал и отрендерил ролик и карусель, а HeyGen, Grok и Edits
подключить не смог.
Светлый премиум-инфографик (GLOBAL-CAROUSEL-RULE §13-Б), компоненты из carousel_claude_video_build.py.
7 слайдов 1080×1350 (4:5). Наборы: ru (Instagram), ru-vk (ВКонтакте, отличается только CTA
на 7-м слайде), en.
Запуск:
  python3 scripts/carousel_agent_access_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <html> <outdir>   # для ru, ru-vk, en
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
BASE_OUT = ROOT / "content" / "carousels" / "agent-access-2026-11-25"

def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
FRAME = b64(BASE_OUT / "assets" / "frame-video.jpg")

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
.note{font-size:10.8pt;font-weight:600;color:#6E6A63;margin-top:10px;line-height:1.4}
.retention{position:absolute;left:36px;right:36px;bottom:56px;font-size:12.5pt;font-weight:700;color:#E1671E}
.sig{position:absolute;bottom:22px;left:36px;display:flex;align-items:center;gap:8px}
.sig img{width:26px;height:26px}
.sig b{font-size:12pt;font-weight:800;color:#20242B}
.sig b i{font-style:normal;color:#E1671E}
.prompt{background:#1b1510;border-radius:16px;padding:16px 18px;margin-top:12px;color:#f2eadf}
.prompt .plbl{display:flex;align-items:center;justify-content:space-between;margin-bottom:9px}
.prompt .plbl .tag{font-weight:800;font-size:9.5pt;letter-spacing:.1em;text-transform:uppercase;color:#1b1510;
 background:#FFB066;border-radius:8px;padding:4px 10px}
.prompt .plbl .copy{font-weight:700;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;color:#cbb39d}
.prompt code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:10.2pt;
 line-height:1.52;white-space:pre-wrap;color:#f2eadf}
.vs{display:flex;gap:12px;margin-top:16px;align-items:stretch}
.vs .col{flex:1;border-radius:14px;padding:12px 13px;display:flex;flex-direction:column}
.vs .bot{background:#fff;border:1px solid #EBE2D3}
.vs .agent{background:#20242B;color:#fff}
.vs .who{font-size:10pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px}
.vs .bot .who{color:#6E6A63}
.vs .agent .who{color:#FFB066}
.vs .bubble{background:#F3EDE3;border-radius:12px 12px 12px 3px;padding:9px 11px;font-size:10.8pt;font-weight:600;
 color:#3a362f;line-height:1.38}
.vs .agent img{display:block;width:100%;border-radius:8px}
.vs .file{font-size:10.5pt;font-weight:800;margin-top:7px;color:#fff}
.vs .file span{color:#7FD08F}
.cmp .row{display:flex;gap:10px;margin-top:8px}
.cmp .row > div{flex:1;border-radius:12px;padding:9px 12px;font-size:11.2pt;font-weight:600;line-height:1.36}
.cmp .l{background:#fff;border:1px solid #EBE2D3;color:#3a362f}
.cmp .r{background:#FBEFE0;border:1.5px solid #F2A65A;color:#20242B}
.cmp .h{font-size:9.5pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;margin-bottom:4px}
.cmp .l .h{color:#6E6A63}.cmp .r .h{color:#E1671E}
.req{background:#fff;border:1px dashed #E1671E;border-radius:12px;padding:10px 13px;margin-top:12px;
 font-size:11.5pt;font-weight:700;color:#20242B}
.req span{color:#E1671E}
.loop{display:flex;flex-direction:column;gap:7px;margin-top:14px}
.loop .s{display:flex;gap:12px;align-items:center;background:#fff;border:1px solid #EBE2D3;border-radius:12px;padding:9px 13px}
.loop .s .n{flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:#E1671E;color:#fff;font-weight:800;
 font-size:11.5pt;display:flex;align-items:center;justify-content:center}
.loop .s p{font-size:11.5pt;font-weight:600;color:#20242B;line-height:1.35}
.loop .s p b{color:#E1671E}
.ok,.no{display:flex;flex-direction:column;gap:5px;margin-top:6px}
.ok div,.no div{background:#fff;border:1px solid #EBE2D3;border-radius:11px;padding:6px 12px;font-size:10.6pt;
 font-weight:600;color:#20242B;line-height:1.35}
.ok div::before{content:"✓  ";color:#2E9E5B;font-weight:800}
.no div::before{content:"✕  ";color:#C23B2B;font-weight:800}
.sec{font-size:10pt;font-weight:800;letter-spacing:.06em;text-transform:uppercase;margin-top:9px;color:#6E6A63}
.tiers{display:flex;flex-direction:column;gap:9px;margin-top:12px}
.tier{border-radius:13px;padding:11px 14px;border:1px solid #EBE2D3;background:#fff}
.tier .t{font-size:11.8pt;font-weight:800;color:#20242B}
.tier .t span{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:8px;vertical-align:1px}
.tier p{font-size:10.9pt;font-weight:500;color:#3a362f;line-height:1.4;margin-top:3px}
.checklist{display:flex;flex-direction:column;gap:8px;margin-top:8px}
.checklist .c{display:flex;gap:11px;align-items:center;background:#fff;border:1px solid #EBE2D3;
 border-radius:12px;padding:10px 14px}
.checklist .c .box{flex:0 0 auto;width:20px;height:20px;border-radius:6px;border:2px solid #E1671E}
.checklist .c p{font-size:11.3pt;font-weight:600;color:#20242B;line-height:1.35}
"""

def sig():
    return (f'<div class="sig"><img src="data:image/png;base64,{LOGO}">'
            f'<b>Alov<i>Lab</i></b></div>')

N = 7

RU = dict(
 s1=dict(k="Агенты без мифов",
         h="ЧАТ-БОТ<br>ОТВЕЧАЕТ.<br><i>АГЕНТ<br>ДЕЛАЕТ.</i>",
         lead="Но только там, куда ты дал ему доступ.",
         bot="Чат-бот", bubble="«Вот 7 шагов, как смонтировать ролик…»",
         agent="Агент", file="collage.mp4 · 37,6 с · <span>готово</span>",
         ret="Разница на одном запросе  →"),
 s2=dict(k="Один запрос",
         h="Два разных<br><i>результата</i>",
         req="Запрос: <span>«Сделай ролик на 37 секунд про вайб кодинг»</span>",
         rows=[("Чат-бот", "Пишет сценарий и советы.", "Агент", "Ставит Remotion и пишет сцены."),
               ("Чат-бот", "Монтируешь ты.", "Агент", "Рендерит и проверяет кадры."),
               ("Чат-бот", "На выходе текст.", "Агент", "На выходе файл.")],
         note="Модель может быть та же самая. Разница в том, есть ли у неё руки.",
         ret="Как работает агент  →"),
 s3=dict(k="Под капотом",
         h="Цикл агента<br><i>в пять шагов</i>",
         loop=["<b>Цель.</b> Что должно получиться и как понять, что готово.",
               "<b>План.</b> Разбивает задачу на шаги.",
               "<b>Инструменты.</b> Файлы, терминал, браузер, коннекторы.",
               "<b>Проверка.</b> Смотрит на результат, а не на свой код.",
               "<b>Сдача.</b> Отдаёт файл, ссылку или отчёт."],
         note="Без третьего шага это снова чат-бот, только с планом.",
         ret="Наш кейс этой недели  →"),
 s4=dict(k="Реальный кейс, не теория",
         h="Что агент сделал сам<br><i>и где упёрся</i>",
         ok_t="Сделал сам",
         ok=["Поставил Remotion, написал 5 сцен, отрендерил MP4 на 37,6 с",
             "Проверил факты через веб-поиск",
             "Сверстал карусель и проверил все 14 слайдов",
             "Закоммитил и отправил всё в GitHub"],
         no_t="Упёрся",
         no=["HeyGen: коннектора нет", "Grok: коннектора нет", "Edits: мобильное приложение, подключить нечем"],
         ret="Карта доступа  →"),
 s5=dict(k="Сохрани карту",
         h="Где у агента<br><i>есть руки</i>",
         tiers=[("#2E9E5B", "Сразу", "Файлы, терминал, код, веб-поиск в его рабочей среде."),
                ("#F2A65A", "Через коннектор", "Сервисы, которые ты подключил: Google Drive, Gmail, Canva, Figma и другие (коннекторы на протоколе MCP)."),
                ("#C23B2B", "Только через тебя", "Нет коннектора или API: мобильные приложения, закрытые кабинеты. Агент готовит промпт и файлы, кнопку жмёшь ты.")],
         note="Платное и необратимое хороший агент без спроса не делает. Наш попросил разрешения на платную генерацию. Я отказал, и он её не запускал.",
         ret="Как ставить задачу  →"),
 s6=dict(k="Сохрани промпт",
         h="Задача<br><i>для агента</i>",
         code="Цель: [ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ: файл,\n"
              "страница, отчёт].\n"
              "Где работать: [ПАПКА / СЕРВИСЫ, к которым\n"
              "у тебя есть доступ].\n"
              "Готово, когда: [КРИТЕРИЙ ПРОВЕРКИ].\n"
              "Перед платными и необратимыми действиями\n"
              "спроси меня.\n"
              "Если до сервиса нет доступа, не обходи:\n"
              "скажи и подготовь то, что я сделаю руками.",
         ret="Перед запуском  →"),
 s7=dict(h="СОХРАНИ<i>.</i>",
         lead="Прежде чем менять модель, проверь доступы.",
         cl="Перед запуском агента",
         items=["Цель и критерий «готово»", "Доступы: папка, коннекторы", "Что нельзя делать без спроса"],
         lbl="Карта доступов + промпт",
         cta="В Telegram, ссылка в шапке профиля.",
         course="Как ставить нейросети задачу, чтобы она делала работу, разбираем на курсе «Нейросети и ChatGPT для каждого»."),
)

RU_VK = {**RU, "s7": {**RU["s7"], "cta": "В Telegram, ссылка в закрепе и в первом комментарии."}}

EN = dict(
 s1=dict(k="Agents, no myths",
         h="A CHATBOT<br>ANSWERS.<br><i>AN AGENT<br>DOES.</i>",
         lead="But only where you've given it access.",
         bot="Chatbot", bubble="“Here are 7 steps to edit your video…”",
         agent="Agent", file="collage.mp4 · 37.6 s · <span>done</span>",
         ret="Same request, two results  →"),
 s2=dict(k="One request",
         h="Two different<br><i>results</i>",
         req="Request: <span>“Make a 37-second video about vibe coding”</span>",
         rows=[("Chatbot", "Writes a script and tips.", "Agent", "Installs Remotion, writes the scenes."),
               ("Chatbot", "You do the editing.", "Agent", "Renders and checks the frames."),
               ("Chatbot", "You get text.", "Agent", "You get a file.")],
         note="It can be the very same model. The difference is whether it has hands.",
         ret="How an agent works  →"),
 s3=dict(k="Under the hood",
         h="The agent loop<br><i>in five steps</i>",
         loop=["<b>Goal.</b> What should come out and how to tell it's done.",
               "<b>Plan.</b> Breaks the task into steps.",
               "<b>Tools.</b> Files, terminal, browser, connectors.",
               "<b>Check.</b> Looks at the result, not at its own code.",
               "<b>Deliver.</b> Hands over a file, a link or a report."],
         note="Without step three it's a chatbot again, just with a plan.",
         ret="Our case this week  →"),
 s4=dict(k="A real case, not theory",
         h="What the agent did<br><i>and where it got stuck</i>",
         ok_t="Did on its own",
         ok=["Installed Remotion, wrote 5 scenes, rendered a 37.6 s MP4",
             "Checked the facts with web search",
             "Built the carousel and checked all 14 slides",
             "Committed and pushed everything to GitHub"],
         no_t="Got stuck",
         no=["HeyGen: no connector", "Grok: no connector", "Edits: a mobile app, nothing to connect"],
         ret="The access map  →"),
 s5=dict(k="Save the map",
         h="Where an agent<br><i>has hands</i>",
         tiers=[("#2E9E5B", "Right away", "Files, terminal, code, web search in its workspace."),
                ("#F2A65A", "Through a connector", "Services you've connected: Google Drive, Gmail, Canva, Figma and more (MCP connectors)."),
                ("#C23B2B", "Only through you", "No connector or API: mobile apps, closed dashboards. The agent preps the prompt and files, you press the button.")],
         note="A good agent doesn't do paid or irreversible things without asking. Ours asked to run a paid generation. I said no, and it didn't run it.",
         ret="How to set the task  →"),
 s6=dict(k="Save the prompt",
         h="A task<br><i>for an agent</i>",
         code="Goal: [WHAT SHOULD COME OUT: a file,\n"
              "a page, a report].\n"
              "Where to work: [FOLDER / SERVICES you\n"
              "have access to].\n"
              "Done when: [HOW TO CHECK IT].\n"
              "Ask me before anything paid or\n"
              "irreversible.\n"
              "If you can't reach a service, don't work\n"
              "around it: tell me and prep what I'll do\n"
              "by hand.",
         ret="Before you start  →"),
 s7=dict(h="SAVE<i>.</i>",
         lead="Before you switch models, check the access.",
         cl="Before you run an agent",
         items=["The goal and what “done” means", "Access: folder, connectors", "What it must not do without asking"],
         lbl="Access map + prompt",
         cta="On Telegram, link in bio.",
         course="How to give AI a task so it actually does the work: we cover it in the course “AI and ChatGPT for Everyone”."),
)

def build(name, t):
    lang = "en" if name == "en" else "ru"
    s = []
    a = t["s1"]
    s.append(f"""<div class="slide">
 <div class="badge">1 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{a['k']}</div>
  <h1>{a['h']}</h1>
  <p class="lead">{a['lead']}</p>
  <div class="vs">
   <div class="col bot"><div class="who">{a['bot']}</div><div class="bubble">{a['bubble']}</div></div>
   <div class="col agent"><div class="who">{a['agent']}</div>
    <img src="data:image/jpeg;base64,{FRAME}"><div class="file">{a['file']}</div></div>
  </div>
 </div>
 <div class="retention">{a['ret']}</div>
 {sig()}
</div>""")
    a = t["s2"]
    rows = "".join(f'<div class="row"><div class="l"><div class="h">{l1}</div>{l2}</div>'
                   f'<div class="r"><div class="h">{r1}</div>{r2}</div></div>' for l1, l2, r1, r2 in a["rows"])
    s.append(f"""<div class="slide">
 <div class="badge">2 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{a['k']}</div>
  <h2>{a['h']}</h2>
  <div class="req">{a['req']}</div>
  <div class="cmp">{rows}</div>
  <div class="note">{a['note']}</div>
 </div>
 <div class="retention">{a['ret']}</div>
 {sig()}
</div>""")
    a = t["s3"]
    lp = "".join(f'<div class="s"><div class="n">{i+1}</div><p>{x}</p></div>' for i, x in enumerate(a["loop"]))
    s.append(f"""<div class="slide">
 <div class="badge">3 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{a['k']}</div>
  <h2>{a['h']}</h2>
  <div class="loop">{lp}</div>
  <div class="note">{a['note']}</div>
 </div>
 <div class="retention">{a['ret']}</div>
 {sig()}
</div>""")
    a = t["s4"]
    ok = "".join(f"<div>{x}</div>" for x in a["ok"])
    no = "".join(f"<div>{x}</div>" for x in a["no"])
    s.append(f"""<div class="slide">
 <div class="badge">4 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{a['k']}</div>
  <h2 style="font-size:23pt">{a['h']}</h2>
  <div class="sec">{a['ok_t']}</div>
  <div class="ok">{ok}</div>
  <div class="sec">{a['no_t']}</div>
  <div class="no">{no}</div>
 </div>
 <div class="retention">{a['ret']}</div>
 {sig()}
</div>""")
    a = t["s5"]
    tr = "".join(f'<div class="tier"><div class="t"><span style="background:{c}"></span>{h}</div><p>{p}</p></div>'
                 for c, h, p in a["tiers"])
    s.append(f"""<div class="slide">
 <div class="badge">5 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{a['k']}</div>
  <h2>{a['h']}</h2>
  <div class="tiers">{tr}</div>
  <div class="note">{a['note']}</div>
 </div>
 <div class="retention">{a['ret']}</div>
 {sig()}
</div>""")
    a = t["s6"]
    tag, copy = ("Промпт", "скопировать") if lang == "ru" else ("Prompt", "copy")
    s.append(f"""<div class="slide">
 <div class="badge">6 / {N}</div>
 <div style="margin-top:72px">
  <div class="kicker">{a['k']}</div>
  <h2>{a['h']}</h2>
  <div class="prompt">
   <div class="plbl"><span class="tag">{tag}</span><span class="copy">{copy}</span></div>
   <code>{a['code']}</code>
  </div>
 </div>
 <div class="retention">{a['ret']}</div>
 {sig()}
</div>""")
    a = t["s7"]
    ci = "".join(f'<div class="c"><div class="box"></div><p>{x}</p></div>' for x in a["items"])
    s.append(f"""<div class="slide">
 <div class="badge">7 / {N}</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">{a['h']}</h1>
  <p class="lead" style="margin-top:10px">{a['lead']}</p>
  <div class="kicker" style="margin-top:16px;font-size:10.5pt">{a['cl']}</div>
  <div class="checklist">{ci}</div>
  <div class="card sand" style="margin-top:14px">
   <div class="lbl">{a['lbl']}</div>
   <p>{a['cta']}</p>
  </div>
  <div class="note" style="margin-top:14px">{a['course']}</div>
 </div>
 {sig()}
</div>""")

    outdir = BASE_OUT / name
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / "carousel.html"
    out.write_text("<!doctype html><html lang=%s><head><meta charset=utf-8><style>%s</style></head>"
                   "<body>%s</body></html>" % (lang, CSS, "".join(s)), encoding="utf-8")
    print("HTML:", out, "slides:", len(s))

build("ru", RU)
build("ru-vk", RU_VK)
build("en", EN)
