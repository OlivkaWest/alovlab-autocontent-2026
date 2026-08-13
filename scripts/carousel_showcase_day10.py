# -*- coding: utf-8 -*-
"""AlovLab · День 10 (13.08) «Каркас 2–5–15–30» — SHOWCASE + иллюстрации.
Сценарий Reels проваливается не когда сложно снять, а когда написан потоком.
Метод — разрезать 30 сек на 5 зон, у каждой одна задача. Инструмент: Claude.
Честность: результат — формой, без выдуманных цифр. Ниша примера — риелтор.
Нумерация N/8. RU кроме AlovLab. Запуск: python3 scripts/carousel_showcase_day10.py"""
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-10-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-10-showcase.html"

EXTRA = r"""
.hsm .head h2{font-size:36px}
.cover .head h2{font-size:48px}
.cover .sub{margin-top:14px;max-width:27ch;font-size:17px}
.mch .head h2{font-size:35px}
.viz{flex:1;position:relative;z-index:2;display:grid;place-items:center;min-height:0;margin-top:14px}
.viz svg{width:min(94%,490px);height:100%;max-height:360px}
.viz::before{content:"";position:absolute;left:50%;top:55%;width:74%;height:64%;transform:translate(-50%,-50%);
 background:radial-gradient(closest-side,rgba(255,120,40,.16),transparent 72%);z-index:-1;pointer-events:none}
.body.tight{margin-top:16px}
.pbox{position:relative;z-index:4;margin-top:15px;background:#120c06;border:1px solid rgba(255,150,80,.28);
 border-left:3px solid var(--o);border-radius:14px;padding:16px 18px}
.pbox .tag{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px;margin-bottom:11px}
.pbox code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:11.5px;line-height:1.5;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pbox .ru{margin-top:11px;padding-top:10px;border-top:1px solid rgba(255,255,255,.1);font-size:11.5px;line-height:1.4;color:#b9ad9b}
.pbox .ru b{color:#fff}
.sfact{position:relative;z-index:4;font-weight:600;font-size:14px;color:#b9ad9b;line-height:1.4}.sfact b{color:#fff}
/* зоны каркаса */
.mlist{position:relative;z-index:4;margin-top:16px;margin-bottom:4px;display:flex;flex-direction:column;gap:8px}
.mrow{display:flex;align-items:center;gap:13px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:13px;padding:10px 15px}
.mrow .n{flex:0 0 auto;min-width:52px;height:27px;padding:0 8px;border-radius:8px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:12px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));font-variant-numeric:tabular-nums}
.mrow .t b{font-weight:700;font-size:15px;color:#fff;line-height:1.15;display:block}
.mrow .t span{font-weight:500;font-size:12px;color:#8a8177;line-height:1.2}
/* мини-сценарий в две колонки (демо) */
.scr{position:relative;z-index:4;margin-top:13px;display:flex;flex-direction:column;gap:6px}
.scr .r{display:grid;grid-template-columns:52px 1fr;gap:11px;align-items:center;background:linear-gradient(180deg,rgba(255,255,255,.04),rgba(255,255,255,.018));
 border:1px solid rgba(255,140,60,.13);border-radius:11px;padding:8px 12px}
.scr .r .z{font-weight:800;font-size:11px;color:var(--o2);font-variant-numeric:tabular-nums}
.scr .r .x{font-size:12px;line-height:1.3;color:#d8cdbd}.scr .r .x b{color:#fff}
/* биз-применимость */
.bizmap{position:relative;z-index:4;margin-top:13px;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.bizmap .r{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));border:1px solid rgba(255,140,60,.14);
 border-radius:11px;padding:9px 12px;font-size:12.5px;line-height:1.3;color:#c9bdac}
.bizmap .r b{color:#ff9a4d;font-weight:800;display:block;font-size:11px;text-transform:uppercase;letter-spacing:.03em;margin-bottom:2px}
"""
CSS = CSS0 + EXTRA

# ---------------- СЦЕНЫ ----------------
SC_COVER = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <text x="40" y="40" fill="#8a8177" font-size="12" font-weight="800" letter-spacing="1">ПОТОК</text>
 <path d="M40 58 C110 54 150 92 240 96 S360 118 442 116" stroke="#5a5148" stroke-width="3" fill="none"/>
 <circle cx="240" cy="96" r="4" fill="#6a6157"/>
 <text x="240" y="82" fill="#6a6157" font-size="10.5" text-anchor="middle">провисает</text>
 <text x="40" y="158" fill="#ff9a4d" font-size="12" font-weight="800" letter-spacing="1">КАРКАС · 2–5–15–30</text>
 <g font-weight="800" text-anchor="middle">
  <rect x="40" y="172" width="66" height="46" rx="11" fill="#1a1108" stroke="url(#ig)" stroke-width="2.2"/>
  <text x="73" y="192" fill="#ffcaa0" font-size="12">0–2</text><text x="73" y="208" fill="#8a8177" font-size="9" font-weight="700">удар</text>
  <rect x="112" y="172" width="66" height="46" rx="11" fill="#1a1108" stroke="url(#ig)" stroke-width="2.2"/>
  <text x="145" y="192" fill="#ffcaa0" font-size="12">2–5</text><text x="145" y="208" fill="#8a8177" font-size="9" font-weight="700">боль</text>
  <rect x="184" y="172" width="98" height="46" rx="11" fill="#1a1108" stroke="url(#ig)" stroke-width="2.6"/>
  <text x="233" y="192" fill="#ffcaa0" font-size="12">5–15</text><text x="233" y="208" fill="#8a8177" font-size="9" font-weight="700">один приём</text>
  <rect x="288" y="172" width="90" height="46" rx="11" fill="#1a1108" stroke="url(#ig)" stroke-width="2.2"/>
  <text x="333" y="192" fill="#ffcaa0" font-size="12">15–30</text><text x="333" y="208" fill="#8a8177" font-size="9" font-weight="700">результат</text>
  <rect x="384" y="172" width="58" height="46" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="2.2"/>
  <text x="413" y="192" fill="#ffcaa0" font-size="11">CTA</text><text x="413" y="208" fill="#8a8177" font-size="9" font-weight="700">шаг</text>
 </g>
</svg>'''

SC_PROBLEM = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="150" y="14" width="180" height="150" rx="18" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <circle cx="240" cy="78" r="28" stroke="#5a5148" stroke-width="3"/>
 <path d="M231 63 l21 15 -21 15 z" fill="#5a5148"/>
 <path d="M180 132 h120" stroke="#463f37" stroke-width="3" stroke-linecap="round"/>
 <text x="240" y="152" fill="#6a6157" font-size="10.5" text-anchor="middle">говорящая голова</text>
 <path d="M40 200 C120 200 150 206 200 218 S330 240 440 244" stroke="#5a5148" stroke-width="3" fill="none"/>
 <circle cx="200" cy="218" r="4" fill="url(#ig)"/>
 <text x="205" y="210" fill="#ff9a4d" font-size="11" font-weight="800">8-я сек — ушли</text>
 <text x="40" y="194" fill="#8a8177" font-size="10.5" font-weight="700">удержание</text>
</svg>'''

SC_CAUSE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <circle cx="135" cy="118" r="58" fill="#ffffff06" stroke="#5a5148" stroke-width="3"/>
 <path d="M112 118 l14 14 26 -30" stroke="#6a6157" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
 <text x="135" y="200" fill="#8a8177" font-size="12" font-weight="800" text-anchor="middle">донести мысль</text>
 <text x="135" y="218" fill="#6a6157" font-size="10.5" text-anchor="middle">задача потока</text>
 <path d="M206 118 h46 M242 109 l12 9 -12 9" stroke="#6a6157" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="345" cy="118" r="60" fill="#1a1108" stroke="url(#ig)" stroke-width="3"/>
 <circle cx="345" cy="118" r="34" stroke="url(#ig)" stroke-width="2.4"/>
 <circle cx="345" cy="118" r="11" fill="url(#ig)"/>
 <text x="345" y="202" fill="#ff9a4d" font-size="12" font-weight="800" text-anchor="middle">удержать зрителя</text>
 <text x="345" y="220" fill="#8a8177" font-size="10.5" text-anchor="middle">другая задача</text>
</svg>'''

SC_MISTAKE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="40" y="30" width="150" height="190" rx="14" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <g stroke="#463f37" stroke-width="6" stroke-linecap="round">
  <path d="M60 62 h110"/><path d="M60 86 h110"/><path d="M60 110 h110"/><path d="M60 134 h110"/><path d="M60 158 h90"/><path d="M60 182 h110"/></g>
 <path d="M52 42 L182 208 M182 42 L52 208" stroke="#8a5a4a" stroke-width="3" opacity=".8"/>
 <text x="115" y="238" fill="#8a8177" font-size="11.5" font-weight="800" text-anchor="middle">переписать весь</text>
 <path d="M210 124 h44 M244 115 l12 9 -12 9" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="286" y="30" width="150" height="190" rx="14" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <g stroke="#463f37" stroke-width="6" stroke-linecap="round">
  <path d="M306 62 h110"/><path d="M306 86 h110"/></g>
 <rect x="298" y="102" width="126" height="30" rx="8" fill="#e8672a2e" stroke="url(#ig)" stroke-width="2.2"/>
 <path d="M312 117 h84" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/>
 <g stroke="#463f37" stroke-width="6" stroke-linecap="round">
  <path d="M306 158 h110"/><path d="M306 182 h90"/></g>
 <text x="361" y="238" fill="#ff9a4d" font-size="11.5" font-weight="800" text-anchor="middle">чинить одну</text>
</svg>'''

def viz(scene): return f'<div class="viz">{scene}</div>'

def cover(hw, ho, sub, scene):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">AlovLab · каркас 2–5–15–30</span><span class="pg">1<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
  {viz(scene)}
  {FOOT}
</article>"""

def sc(eb, hw, ho, bl, bm, scene, pg):
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">{eb}</span><span class="pg">{pg}<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="body tight"><span class="l">{bl}</span> <span class="m">{bm}</span></div>
  {viz(scene)}
  {FOOT}
</article>"""

ZONES = [
 ("0–2","Удар","одна фраза — остановить палец"),
 ("2–5","Боль","конкретно, его словами — «это про меня»"),
 ("5–15","Один приём","показать, а не рассказать — ровно один"),
 ("15–30","Результат","что меняется — ради чего досматривать"),
 ("финал","CTA","одна строка — в Telegram за конкретным"),
]
def method_slide():
    rows="".join(f'<div class="mrow"><div class="n">{n}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>' for n,t,s in ZONES)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Механика · 30 секунд</span><span class="pg">5<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">30 секунд —</span><span class="o">5 зон.</span></h2></div>
  <div class="mlist">{rows}</div>
  {FOOT}
</article>"""

def demo_slide():
    rows = [
     ("0–2","Квартиру показывают в солнце. Смотри в дождь."),
     ("2–5","В сухую ты не увидишь ни один протёкший шов."),
     ("5–15","Повторный просмотр после дождя — проверь 3 места."),
     ("15–30","Пять минут в дождь — минус ремонт от сырости потом."),
     ("финал","Чек-лист «что смотреть» → тетрадь дня."),
    ]
    scr="".join(f'<div class="r"><span class="z">{z}</span><span class="x">{x}</span></div>' for z,x in rows)
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">До / после · пример: риелтор</span><span class="pg">6<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Тот же угол —</span><span class="o">другой ролик.</span></h2></div>
  <div class="sfact" style="margin-top:14px"><b>Поток:</b> «Всем привет! Сегодня про то, как выбрать квартиру и не переплатить…» — разгон, ушли к 5-й секунде.</div>
  <div class="scr">{scr}</div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт · Claude</span><span class="pg">7<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Разложи угол</span><span class="o">по секундам.</span></h2></div>
  <div class="pbox"><span class="tag">Claude / ChatGPT · скопировать</span><code>Разложи мой угол в сценарий Reels на 30 сек
по каркасу 2–5–15–30. Ниша: [X]. Аудитория: [Y].
Угол: [Z]. Приём: [один]. Отдай таблицей:
таймкод | что говорю | что в кадре.
0–2 — удар, 5–15 — ровно один приём, финал — CTA.</code>
    <div class="ru"><b>Разбор:</b> жёсткие зоны + один приём + две колонки = ролик, по которому можно встать и снять.</div></div>
  <div class="bizmap">
    <div class="r"><b>Эксперт</b>разбор-приём: одна ошибка клиента за ролик</div>
    <div class="r"><b>Услуга</b>«до/после» процесса, результат в цифре</div>
    <div class="r"><b>Магазин</b>один товар — одно применение в кадре</div>
    <div class="r"><b>Локальный</b>приём «проверь на месте» под нишу</div>
  </div>
  {FOOT}
</article>"""

def cta(hw, ho, items, btn):
    lis="".join(f'<div class="li"><i></i><span>{t}</span></div>' for t in items)
    return f"""<article class="slide cta">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings" style="top:120%">{rings()}</div></div>
  <div class="top"><span class="eb">Дальше</span><span class="pg">8<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="clist">{lis}</div>
  <div class="btn">{btn}</div>
  {FOOT}
</article>"""

SLIDES = [
 cover("Поток — складно.", "Каркас — досмотрено.",
       "Сценарий проваливается не когда сложно снять. А когда написан потоком — без задачи на каждую секунду.", SC_COVER),
 sc("Проблема","Пишешь сценарий","потоком.","Начало бодрое, а к 8-й секунде — «ну и вот», «в общем», «как я уже сказал».",
    "Это не стиль. Это провал середины — там зрителя и теряешь.", SC_PROBLEM, 2),
 sc("Причина","Поток решает","не ту задачу.","Донести мысль ≠ удержать зрителя. Ему всё равно, дошла ли она.",
    "Он остаётся, только пока каждая секунда обещает больше прошлой.", SC_CAUSE, 3),
 sc("Ошибка","Переписываешь","весь текст.","А чинить надо одну секунду — ту, где зритель уходит.",
    "Складный текст ≠ досмотренный ролик. Правь зону, а не слог.", SC_MISTAKE, 4),
 method_slide(),
 demo_slide(),
 prompt_slide(),
 cta("Собери свой","сценарий.",
     ["<b>каркас 2–5–15–30</b> + бланк в две колонки — в тетради дня",
      "как заострить удар в 0–2 и убрать провисание середины",
      "инструмент дня — Claude (или ChatGPT)"],
     "Тетрадь дня → t.me/AlovLab"),
]

HTML = f"""<title>Каркас 2–5–15–30 · День 10 · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 10 · 13 августа · showcase + иллюстрации</span>
    <h1>Каркас 2–5–15–30: обложка → проблема → причина → ошибка → 5 зон → до/после → промпт (Claude) → CTA. 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
