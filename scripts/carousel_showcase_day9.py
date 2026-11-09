# -*- coding: utf-8 -*-
"""AlovLab · День 9 (12.08) «Факты, а не вода» — SHOWCASE + иллюстрации.
Текст звучит пусто, потому что под ним нет фактуры. Метод — собрать проверенные факты
с источниками через Perplexity. Честность: НЕ выдумываем цифры — показываем ФОРМУ факта
(цифра + источник + дата). Ниша примеров — ИИ/контент/бизнес. Нумерация N/8.
RU кроме AlovLab и промптов. Запуск: python3 scripts/carousel_showcase_day9.py"""
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-09-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-09-showcase.html"

EXTRA = r"""
.hsm .head h2{font-size:37px}
.cover .head h2{font-size:50px}
.cover .sub{margin-top:14px;max-width:26ch;font-size:17px}
.mch .head h2{font-size:35px}
.viz{flex:1;position:relative;z-index:2;display:grid;place-items:center;min-height:0;margin-top:14px}
.viz svg{width:min(92%,480px);height:100%;max-height:360px}
.viz::before{content:"";position:absolute;left:50%;top:55%;width:74%;height:64%;transform:translate(-50%,-50%);
 background:radial-gradient(closest-side,rgba(255,120,40,.16),transparent 72%);z-index:-1;pointer-events:none}
.body.tight{margin-top:16px}
.pu{position:relative;z-index:4;margin-top:14px;display:inline-block;font-weight:800;font-size:11px;text-transform:uppercase;
 letter-spacing:.03em;color:var(--o2);background:rgba(232,103,42,.13);border:1px solid rgba(232,103,42,.3);border-radius:20px;padding:8px 14px}
.pbox{position:relative;z-index:4;margin-top:15px;background:#120c06;border:1px solid rgba(255,150,80,.28);
 border-left:3px solid var(--o);border-radius:14px;padding:16px 18px}
.pbox .tag{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px;margin-bottom:11px}
.pbox code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:12px;line-height:1.5;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pbox .ru{margin-top:11px;padding-top:10px;border-top:1px solid rgba(255,255,255,.1);font-size:11.5px;line-height:1.4;color:#b9ad9b}
.pbox .ru b{color:#fff}
.sfact{position:relative;z-index:4;font-weight:600;font-size:14px;color:#b9ad9b;line-height:1.4}.sfact b{color:#fff}
.mlist{position:relative;z-index:4;margin-top:16px;margin-bottom:4px;display:flex;flex-direction:column;gap:8px}
.mrow{display:flex;align-items:center;gap:13px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:13px;padding:10px 15px}
.mrow .n{flex:0 0 auto;width:27px;height:27px;border-radius:8px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:13px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o))}
.mrow .t b{font-weight:700;font-size:15.5px;color:#fff;line-height:1.15;display:block}
.mrow .t span{font-weight:500;font-size:12.5px;color:#8a8177;line-height:1.2}
/* биз-применимость на промпт-слайде */
.bizmap{position:relative;z-index:4;margin-top:13px;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.bizmap .r{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));border:1px solid rgba(255,140,60,.14);
 border-radius:11px;padding:9px 12px;font-size:12.5px;line-height:1.3;color:#c9bdac}
.bizmap .r b{color:#ff9a4d;font-weight:800;display:block;font-size:11px;text-transform:uppercase;letter-spacing:.03em;margin-bottom:2px}
"""
CSS = CSS0 + EXTRA

# ---------------- SVG-сцены ----------------
SC_COVER = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="40" y="34" width="160" height="112" rx="14" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <path d="M60 64 h120 M60 86 h120 M60 108 h78" stroke="#463f37" stroke-width="6" stroke-linecap="round"/>
 <path d="M40 168 q20 -11 40 0 t40 0 t40 0 t40 0" stroke="#5a5148" stroke-width="2.5" fill="none"/>
 <path d="M40 183 q20 -11 40 0 t40 0 t40 0 t40 0" stroke="#3f3931" stroke-width="2" fill="none"/>
 <text x="120" y="214" fill="#8a8177" font-size="13" font-weight="800" text-anchor="middle" letter-spacing="1.5">ВОДА</text>
 <path d="M228 92 h24 M244 84 l9 8 -9 8" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="280" y="34" width="160" height="112" rx="14" fill="#1a1108" stroke="url(#ig)" stroke-width="2.5"/>
 <path d="M300 64 h120 M300 86 h120 M300 108 h78" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/>
 <g font-size="9.5" font-weight="800" text-anchor="middle">
  <rect x="282" y="158" width="46" height="22" rx="6" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="305" y="173" fill="#ffcaa0">цифра</text>
  <rect x="332" y="158" width="58" height="22" rx="6" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="361" y="173" fill="#ffcaa0">источник</text>
  <rect x="394" y="158" width="44" height="22" rx="6" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="416" y="173" fill="#ffcaa0">дата</text>
 </g>
 <text x="360" y="214" fill="#ff9a4d" font-size="13" font-weight="800" text-anchor="middle" letter-spacing="1.5">ФАКТ</text>
 <path d="M250 42 l3.5 9 9 3.5 -9 3.5 -3.5 9 -3.5 -9 -9 -3.5 9 -3.5 z" fill="url(#ig)"/>
</svg>'''

SC_PROBLEM = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="70" y="26" width="340" height="164" rx="16" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <g font-size="13" font-weight="700" text-anchor="middle">
  <rect x="96" y="52" width="98" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="145" y="72" fill="#8a8177">полезно</text>
  <rect x="206" y="52" width="128" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="270" y="72" fill="#8a8177">качественно</text>
  <rect x="110" y="92" width="120" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="170" y="112" fill="#8a8177">эффективно</text>
  <rect x="242" y="92" width="112" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="298" y="112" fill="#8a8177">уникально</text>
  <rect x="150" y="132" width="86" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="193" y="152" fill="#8a8177">быстро</text>
  <rect x="248" y="132" width="82" height="30" rx="15" fill="#ffffff09" stroke="#4a433a" stroke-width="1.5"/><text x="289" y="152" fill="#8a8177">удобно</text>
 </g>
 <text x="240" y="220" fill="#8a8177" font-size="13" font-weight="800" text-anchor="middle">звучит — но ничего не сказал</text>
</svg>'''

SC_CAUSE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="120" y="26" width="240" height="82" rx="14" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <path d="M144 52 h192 M144 72 h192 M144 90 h120" stroke="#463f37" stroke-width="6" stroke-linecap="round"/>
 <text x="240" y="100" fill="#6a6157" font-size="0" text-anchor="middle"> </text>
 <rect x="120" y="128" width="240" height="86" rx="14" fill="none" stroke="#4a433a" stroke-width="2.5" stroke-dasharray="8 7"/>
 <text x="240" y="168" fill="#8a8177" font-size="14" font-weight="800" text-anchor="middle">фактуры нет</text>
 <text x="240" y="190" fill="#6a6157" font-size="12" text-anchor="middle">ни цифр · ни источников · ни конкретики</text>
 <path d="M240 108 v20 M232 120 l8 8 8 -8" stroke="url(#ig)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SC_MISTAKE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="46" y="70" width="150" height="110" rx="13" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <path d="M66 96 h110 M66 116 h110 M66 136 h70" stroke="#463f37" stroke-width="5" stroke-linecap="round"/>
 <path d="M150 176 a30 30 0 1 0 -20 -26" stroke="#6a6157" stroke-width="3" fill="none" stroke-linecap="round"/>
 <path d="M128 118 l4 14 -14 3" stroke="#6a6157" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
 <text x="121" y="210" fill="#8a8177" font-size="12.5" font-weight="800" text-anchor="middle">шлифуешь слова</text>
 <text x="121" y="228" fill="#6a6157" font-size="11" text-anchor="middle">— вода остаётся</text>
 <path d="M214 128 h44 M246 119 l12 9 -12 9" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="330" cy="118" r="34" stroke="url(#ig)" stroke-width="3.5" fill="#1a1108"/>
 <path d="M330 100 v36 M312 118 h36" stroke="url(#ig)" stroke-width="3.5" stroke-linecap="round"/>
 <path d="M356 144 l30 30" stroke="url(#ig)" stroke-width="6" stroke-linecap="round"/>
 <text x="342" y="216" fill="#ff9a4d" font-size="12.5" font-weight="800" text-anchor="middle">собираешь факты</text>
 <text x="342" y="234" fill="#b9ad9b" font-size="11" text-anchor="middle">— текст держит</text>
</svg>'''

def viz(scene): return f'<div class="viz">{scene}</div>'

def cover(hw, ho, sub, scene):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">AlovLab · факты, а не вода</span><span class="pg">1<b> / 8</b></span></div>
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
 ("1","Сузь тему","«X для Y», а не «про ИИ вообще»"),
 ("2","Проси факты и цифры","и сразу — со ссылками на источник"),
 ("3","Проверь источник","кто, когда, официальный ли, не реклама"),
 ("4","Отсей мусор","старьё, «одна статья», мнения без данных"),
 ("5","Вынеси в лист","факт → цифра → источник → год"),
]
def method_slide():
    rows="".join(f'<div class="mrow"><div class="n">{n}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>' for n,t,s in STEPS)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Метод · Perplexity · 15 минут</span><span class="pg">5<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Факты за 15 минут —</span><span class="o">5 шагов.</span></h2></div>
  <div class="mlist">{rows}</div>
  {FOOT}
</article>"""

def demo_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Вода / факт · форма</span><span class="pg">6<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Не эпитет —</span><span class="o">а фактура.</span></h2></div>
  <div class="sfact" style="margin-top:15px"><b>Вода:</b> «Нейросети сильно экономят время и повышают эффективность.» — красиво и ни о чём.</div>
  <div class="pbox"><span class="tag">Форма факта · шаблон</span><code>[инструмент] сокращает [задачу]
с [было] до [стало] — [источник], [год].</code>
    <div class="ru"><b>Смысл:</b> факт всегда конкретен и проверяем — цифра и источник. Цифры не выдумывай: если источника нет, факта нет. Пустое место честнее вранья.</div></div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт · Perplexity</span><span class="pg">7<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Собери факты</span><span class="o">под свою тему.</span></h2></div>
  <div class="pbox"><span class="tag">Perplexity · скопировать</span><code>Собери 7 проверенных фактов по теме: [ТВОЯ ТЕМА].
Только с источниками (ссылка + дата). Приоритет —
официальные данные и исследования. Формат каждого:
факт → цифра → источник → год. Исключи рекламу и мнения.</code>
    <div class="ru"><b>Разбор:</b> узкая тема + требование источника + жёсткий формат = лист фактуры, а не пересказ рекламы.</div></div>
  <div class="bizmap">
    <div class="r"><b>Эксперт</b>факты и цифры по своей нише — вес словам</div>
    <div class="r"><b>Магазин</b>характеристики, сравнения, стандарты</div>
    <div class="r"><b>Услуга</b>сроки, гарантии, нормы, кейсы</div>
    <div class="r"><b>Локальный</b>цифры по городу, спросу, сезону</div>
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
 cover("Вода — это не", "стиль. Это лень.", "Текст звучит пусто не потому, что ты плохо пишешь. Под ним просто нет фактуры.", SC_COVER),
 sc("Проблема","Текст звучит","общо.","«Полезно», «качественно», «эффективно» —","слова, которые подходят чему угодно и не говорят ничего.", SC_PROBLEM, 2),
 sc("Причина","Под текстом","пусто.","Нет цифр, источников, конкретики.","Красивые слова не держатся — им не на чём стоять.", SC_CAUSE, 3),
 sc("Ошибка","Ты переписываешь","текст.","А переписывать надо не формулировки.","Пустой текст — это пустой этап фактов, а не слабый слог.", SC_MISTAKE, 4),
 method_slide(),
 demo_slide(),
 prompt_slide(),
 cta("Сначала факты —","потом текст.",
     ["<b>7 фактов с источниками</b> за 15 минут — бланк в тетради",
      "как искать и проверять: что считать источником",
      "инструмент дня — Perplexity"],
     "Тетрадь дня → t.me/AlovLab"),
]

HTML = f"""<title>Факты, а не вода · День 9 · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 9 · 12 августа · showcase + иллюстрации</span>
    <h1>Факты, а не вода: обложка → проблема → причина → ошибка → метод (Perplexity) → форма факта → промпт → CTA. 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
