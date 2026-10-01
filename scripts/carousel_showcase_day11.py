# -*- coding: utf-8 -*-
"""AlovLab · День 11 (14.08) «Текст, который читают» — SHOWCASE + иллюстрации.
Живой текст против канцелярии: одно и то же, две подачи. Инструмент — Claude (промпт-редактор).
Честность: без выдуманных цифр; запрещённые фразы показываем как АНТИ-пример. Ниша — ИИ/контент.
Нумерация N/8. RU кроме AlovLab и промптов. Запуск: python3 scripts/carousel_showcase_day11.py"""
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-11-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-11-showcase.html"

EXTRA = r"""
.hsm .head h2{font-size:37px}
.cover .head h2{font-size:47px}
.cover .sub{margin-top:14px;max-width:27ch;font-size:16.5px}
.mch .head h2{font-size:35px}
.viz{flex:1;position:relative;z-index:2;display:grid;place-items:center;min-height:0;margin-top:14px}
.viz svg{width:min(92%,480px);height:100%;max-height:360px}
.viz::before{content:"";position:absolute;left:50%;top:55%;width:74%;height:64%;transform:translate(-50%,-50%);
 background:radial-gradient(closest-side,rgba(255,120,40,.16),transparent 72%);z-index:-1;pointer-events:none}
.body.tight{margin-top:16px}
.pbox{position:relative;z-index:4;margin-top:15px;background:#120c06;border:1px solid rgba(255,150,80,.28);
 border-left:3px solid var(--o);border-radius:14px;padding:16px 18px}
.pbox .tag{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px;margin-bottom:11px}
.pbox code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:12px;line-height:1.5;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pbox .ru{margin-top:11px;padding-top:10px;border-top:1px solid rgba(255,255,255,.1);font-size:11.5px;line-height:1.4;color:#b9ad9b}
.pbox .ru b{color:#fff}
.sfact{position:relative;z-index:4;font-weight:600;font-size:14px;color:#b9ad9b;line-height:1.4}.sfact b{color:#fff}
.gv{position:relative;z-index:4;margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:11px}
.gv .b{border-radius:13px;padding:13px 15px;font-size:13.5px;line-height:1.4}
.gv .bad{background:#1a120c;border:1px solid #4a2f22;color:#c8a998}
.gv .good{background:#12100a;border:1px solid rgba(255,150,80,.32);color:#ffe4c8}
.gv .lbl{display:block;font-weight:800;font-size:10px;letter-spacing:.05em;text-transform:uppercase;margin-bottom:7px}
.gv .bad .lbl{color:#c56b4e}.gv .good .lbl{color:var(--o2)}
.mlist{position:relative;z-index:4;margin-top:16px;margin-bottom:4px;display:flex;flex-direction:column;gap:8px}
.mrow{display:flex;align-items:center;gap:13px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:13px;padding:10px 15px}
.mrow .n{flex:0 0 auto;width:27px;height:27px;border-radius:8px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:13px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o))}
.mrow .t b{font-weight:700;font-size:15.5px;color:#fff;line-height:1.15;display:block}
.mrow .t span{font-weight:500;font-size:12.5px;color:#8a8177;line-height:1.2}
.bizmap{position:relative;z-index:4;margin-top:13px;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.bizmap .r{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));border:1px solid rgba(255,140,60,.14);
 border-radius:11px;padding:9px 12px;font-size:12.5px;line-height:1.3;color:#c9bdac}
.bizmap .r b{color:#ff9a4d;font-weight:800;display:block;font-size:11px;text-transform:uppercase;letter-spacing:.03em;margin-bottom:2px}
"""
CSS = CSS0 + EXTRA

# ---------------- SVG-сцены ----------------
SC_COVER = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="40" y="30" width="160" height="140" rx="14" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <g stroke="#463f37" stroke-width="4.5" stroke-linecap="round">
  <path d="M58 56 h124"/><path d="M58 72 h124"/><path d="M58 88 h124"/><path d="M58 104 h124"/><path d="M58 120 h116"/><path d="M58 136 h124"/><path d="M58 152 h92"/>
 </g>
 <text x="120" y="192" fill="#8a8177" font-size="12.5" font-weight="800" text-anchor="middle" letter-spacing="1.2">КАНЦЕЛЯРИЯ</text>
 <path d="M228 92 h24 M244 84 l9 8 -9 8" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="280" y="30" width="160" height="140" rx="14" fill="#1a1108" stroke="url(#ig)" stroke-width="2.5"/>
 <g stroke="#ff9a4d" stroke-linecap="round">
  <path d="M300 60 h78" stroke-width="9"/><path d="M300 88 h116" stroke-width="6.5"/><path d="M300 110 h64" stroke-width="6.5"/><path d="M300 132 h100" stroke-width="6.5" opacity="0.85"/>
 </g>
 <text x="360" y="192" fill="#ff9a4d" font-size="12.5" font-weight="800" text-anchor="middle" letter-spacing="1.2">ЖИВОЙ</text>
 <path d="M250 40 l3.5 9 9 3.5 -9 3.5 -3.5 9 -3.5 -9 -9 -3.5 9 -3.5 z" fill="url(#ig)"/>
</svg>'''

SC_PROBLEM = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="70" y="24" width="250" height="168" rx="14" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <g stroke-linecap="round">
  <path d="M92 52 h206" stroke="#8a8177" stroke-width="6"/>
  <path d="M92 78 h206" stroke="#7a7167" stroke-width="6"/>
  <path d="M92 104 h170" stroke="#463f37" stroke-width="6"/>
  <path d="M92 130 h150" stroke="#332e28" stroke-width="6"/>
  <path d="M92 156 h120" stroke="#2a2620" stroke-width="6"/>
 </g>
 <path d="M330 104 h44 M362 95 l12 9 -12 9" stroke="#ff9a4d" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="400" cy="80" r="11" stroke="#ff9a4d" stroke-width="2.6" fill="none"/>
 <path d="M389 120 c0 -14 22 -14 22 0" stroke="#ff9a4d" stroke-width="2.6" fill="none" stroke-linecap="round"/>
 <text x="200" y="222" fill="#8a8177" font-size="13.5" font-weight="800" text-anchor="middle">бросают на третьей строке</text>
</svg>'''

SC_CAUSE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="46" y="24" width="388" height="166" rx="16" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <g font-size="12.5" font-weight="700" text-anchor="middle">
  <rect x="66" y="48" width="176" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="154" y="68" fill="#8a8177">в современном мире</text>
  <rect x="256" y="48" width="164" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="338" y="68" fill="#8a8177">важно понимать</text>
  <rect x="66" y="90" width="160" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="146" y="110" fill="#8a8177">стоит отметить</text>
  <rect x="240" y="90" width="180" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="330" y="110" fill="#8a8177">давайте разберёмся</text>
  <rect x="120" y="132" width="240" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="240" y="152" fill="#8a8177">как известно, не секрет, что…</text>
 </g>
 <text x="240" y="182" fill="#8a8177" font-size="0"> </text>
</svg>'''

SC_MISTAKE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="42" y="52" width="150" height="150" rx="13" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <g stroke="#463f37" stroke-width="4.5" stroke-linecap="round"><path d="M60 74 h114"/><path d="M60 90 h114"/><path d="M60 106 h114"/><path d="M60 122 h100"/><path d="M60 138 h114"/><path d="M60 154 h84"/></g>
 <path d="M117 200 a30 30 0 1 0 -20 -26" stroke="#6a6157" stroke-width="3" fill="none" stroke-linecap="round"/>
 <path d="M96 152 l3 15 -15 2" stroke="#6a6157" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
 <text x="117" y="228" fill="#8a8177" font-size="12" font-weight="800" text-anchor="middle">дописываешь ещё</text>
 <path d="M214 128 h44 M246 119 l12 9 -12 9" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="300" y="70" width="130" height="86" rx="12" fill="#1a1108" stroke="url(#ig)" stroke-width="2.5"/>
 <g stroke="#ff9a4d" stroke-linecap="round"><path d="M318 96 h70" stroke-width="8"/><path d="M318 118 h94" stroke-width="6"/><path d="M318 136 h56" stroke-width="6"/></g>
 <text x="365" y="182" fill="#ff9a4d" font-size="12" font-weight="800" text-anchor="middle">меняешь подачу</text>
 <text x="365" y="200" fill="#b9ad9b" font-size="10.5" text-anchor="middle">— то же, но живо</text>
</svg>'''

def viz(scene): return f'<div class="viz">{scene}</div>'

def cover(hw, ho, sub, scene):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">AlovLab · текст, который читают</span><span class="pg">1<b> / 8</b></span></div>
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

STEPS = [
 ("1","Сильное начало","первое слово уже цепляет, без разгона"),
 ("2","Короткие фразы","одна мысль — одно предложение"),
 ("3","Конкретика","пример вместо штампа и общих слов"),
 ("4","Убери канцелярию","«важно понимать», «в современном мире» — вон"),
 ("5","Один смысл","один текст — одна идея, остальное режь"),
]
def method_slide():
    rows="".join(f'<div class="mrow"><div class="n">{n}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>' for n,t,s in STEPS)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Метод · как оживить текст</span><span class="pg">5<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Живой текст —</span><span class="o">5 приёмов.</span></h2></div>
  <div class="mlist">{rows}</div>
  {FOOT}
</article>"""

def demo_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Одно и то же · две подачи</span><span class="pg">6<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">То же —</span><span class="o">но читают.</span></h2></div>
  <div class="gv">
    <div class="b bad"><span class="lbl">✕ Канцелярия</span>«В современном мире нейросети являются важным инструментом для повышения эффективности создания контента.»</div>
    <div class="b good"><span class="lbl">✓ Живой</span>«Нейросеть накидает черновик. Ты правишь — и постишь. Никакой возни с чистого листа.»</div>
  </div>
  <div class="sfact" style="margin-top:14px"><b>Смысл один.</b> Слева — разгон и штампы, читатель ушёл. Справа — сильное начало, короткие фразы, конкретика.</div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт · Claude</span><span class="pg">7<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Промпт-редактор</span><span class="o">под свой текст.</span></h2></div>
  <div class="pbox"><span class="tag">Claude · скопировать</span><code>Перепиши абзац живой человеческой речью: сильное
начало, короткие фразы, одна мысль, конкретика вместо
штампов. Убери канцелярию и клише («в современном
мире», «важно понимать», «стоит отметить»).
Смысл сохрани — воду убери. Вот текст: [ВСТАВЬ АБЗАЦ]</code>
    <div class="ru"><b>Разбор:</b> даёшь Клоду свой абзац — получаешь версию, которую дочитывают. Дальше правишь под свой голос.</div></div>
  <div class="bizmap">
    <div class="r"><b>Эксперт</b>посты и сторис без канцелярии</div>
    <div class="r"><b>Магазин</b>описания и карточки, что читают</div>
    <div class="r"><b>Услуга</b>продающий текст без штампов</div>
    <div class="r"><b>SMM</b>лента одним голосом</div>
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
 cover("Тебя не читают", "из-за 3-й строки.", "Не из-за темы. Текст звучит как канцелярия — и читатель уходит раньше, чем дошёл до сути.", SC_COVER),
 sc("Проблема","Пишешь","как в отчёте.","Длинно, гладко, ни о чём —","и читатель отваливается на третьем предложении.", SC_PROBLEM, 2),
 sc("Причина","Виноват не","текст. Разгон.","Штампы и клише крадут первые секунды.","Пока ты «подводишь к мысли», человек уже пролистал.", SC_CAUSE, 3),
 sc("Ошибка","Дописываешь","ещё абзац.","А надо не добавить, а переписать подачу.","Тот же смысл — короче, живее, с сильного начала.", SC_MISTAKE, 4),
 method_slide(),
 demo_slide(),
 prompt_slide(),
 cta("Сначала подача —","потом объём.",
     ["<b>структура поста и продающего</b> — в тетради",
      "список запрещённых фраз + промпт-редактор",
      "инструмент дня — Claude"],
     "Тетрадь дня → t.me/AlovLab"),
]

HTML = f"""<title>Текст, который читают · День 11 · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 11 · 14 августа · showcase + иллюстрации</span>
    <h1>Текст, который читают: обложка → проблема → причина → ошибка → 5 приёмов → до/после → промпт (Claude) → CTA. 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
