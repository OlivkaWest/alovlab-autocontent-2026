# -*- coding: utf-8 -*-
"""AlovLab · День 8 «Как сделать топовый рекламный ролик» (бриф/промпт для ИИ) — SHOWCASE + иллюстрации.
Пример — реклама (кроссовок), НЕ еда. Метод — 6 слотов Seedance 2.5. Блоки с реальным содержимым.
Нумерация N/8. RU кроме AlovLab и промптов. Запуск: python3 scripts/carousel_showcase_day8.py"""
import pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-08-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-08-showcase.html"

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
.sfact{font-weight:600;font-size:14px;color:#b9ad9b;line-height:1.4}.sfact b{color:#fff}
/* список слотов */
.mlist{position:relative;z-index:4;margin-top:16px;margin-bottom:4px;display:flex;flex-direction:column;gap:8px}
.mrow{display:flex;align-items:center;gap:13px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:13px;padding:10px 15px}
.mrow .n{flex:0 0 auto;width:27px;height:27px;border-radius:8px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:13px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o))}
.mrow .t b{font-weight:700;font-size:15.5px;color:#fff;line-height:1.15;display:block}
.mrow .t span{font-weight:500;font-size:12.5px;color:#8a8177;line-height:1.2}
"""
CSS = CSS0 + EXTRA

# ---------------- СЦЕНЫ (превью-кадры ролика, без «пустых» полосок) ----------------
SC_COVER = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="196" y="4" width="88" height="24" rx="12" stroke="url(#ig)" stroke-width="3"/>
 <text x="240" y="21" fill="#ffcaa0" font-size="12" font-weight="800" text-anchor="middle">промпт</text>
 <path d="M240 28 V48 M130 48 H350 M130 48 V64 M350 48 V64" stroke="#6a6157" stroke-width="2.5"/>
 <rect x="44" y="66" width="168" height="150" rx="14" fill="#ffffff08" stroke="#ffffff1f" stroke-width="2"/>
 <circle cx="128" cy="130" r="26" stroke="#5a5148" stroke-width="3"/>
 <path d="M121 118 l19 12 -19 12 z" fill="#5a5148"/>
 <text x="128" y="238" fill="#8a8177" font-size="12.5" font-weight="800" text-anchor="middle" letter-spacing="1.5">СТОК</text>
 <rect x="268" y="66" width="168" height="150" rx="14" fill="#1a1108" stroke="url(#ig)" stroke-width="2.5"/>
 <circle cx="352" cy="130" r="26" stroke="url(#ig)" stroke-width="3"/>
 <path d="M345 118 l19 12 -19 12 z" fill="url(#ig)"/>
 <path d="M300 92 l3.5 9 9 3.5 -9 3.5 -3.5 9 -3.5 -9 -9 -3.5 9 -3.5 z" fill="url(#ig)"/>
 <path d="M414 178 l3 7.5 7.5 3 -7.5 3 -3 7.5 -3 -7.5 -7.5 -3 7.5 -3 z" fill="url(#ig)" opacity="0.85"/>
 <text x="352" y="238" fill="#ff9a4d" font-size="12.5" font-weight="800" text-anchor="middle" letter-spacing="1.5">КИНО</text>
</svg>'''

SC_PROBLEM = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="118" y="20" width="244" height="158" rx="16" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <circle cx="240" cy="88" r="30" stroke="#5a5148" stroke-width="3"/>
 <path d="M231 72 l22 16 -22 16 z" fill="#5a5148"/>
 <path d="M150 150 h180" stroke="#463f37" stroke-width="3" stroke-linecap="round"/>
 <text x="240" y="212" fill="#8a8177" font-size="13" font-weight="800" text-anchor="middle">плоский сток</text>
 <text x="240" y="232" fill="#6a6157" font-size="11.5" text-anchor="middle">ровный свет · ноль динамики</text>
</svg>'''

SC_CAUSE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <path d="M64 244 v-70 a66 66 0 0 1 132 0 v70 z" fill="#1a1108" stroke="url(#ig)" stroke-width="3"/>
 <g font-size="11.5" font-weight="700" text-anchor="middle">
  <rect x="76" y="140" width="52" height="22" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="102" y="155" fill="#ffcaa0">свет</text>
  <rect x="134" y="140" width="62" height="22" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="165" y="155" fill="#ffcaa0">ракурс</text>
  <rect x="76" y="168" width="72" height="22" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="112" y="183" fill="#ffcaa0">движение</text>
  <rect x="154" y="168" width="42" height="22" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="175" y="183" fill="#ffcaa0">звук</text>
 </g>
 <path d="M210 150 h58 M256 141 l12 9 -12 9" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="292" y="98" width="150" height="104" rx="15" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <circle cx="367" cy="140" r="18" stroke="#5a5148" stroke-width="2.6"/>
 <path d="M362 132 l12 8 -12 8 z" fill="#5a5148"/>
 <text x="367" y="182" fill="#6a6157" font-size="11" font-weight="700" text-anchor="middle">одно слово</text>
</svg>'''

SC_MISTAKE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <circle cx="240" cy="34" r="7" fill="url(#ig)"/>
 <path d="M240 41 C240 78 150 82 132 110" stroke="#6a6157" stroke-width="3"/>
 <path d="M240 41 C240 78 330 82 348 110" stroke="url(#ig)" stroke-width="3.5"/>
 <g stroke="#6a6157" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path d="M150 168 a34 34 0 1 0 -18 -30"/>
  <path d="M128 128 l6 16 -16 4"/>
 </g>
 <text x="116" y="222" fill="#8a8177" font-size="12.5" font-weight="800" text-anchor="middle">сменить модель</text>
 <text x="116" y="240" fill="#6a6157" font-size="11" text-anchor="middle">— тупик</text>
 <rect x="306" y="122" width="80" height="90" rx="12" fill="#1a1108" stroke="url(#ig)" stroke-width="2.5"/>
 <path d="M322 146 h48 M322 162 h48 M322 178 h30" stroke="url(#ig)" stroke-width="5" stroke-linecap="round"/>
 <text x="346" y="234" fill="#ff9a4d" font-size="12.5" font-weight="800" text-anchor="middle">промпт</text>
</svg>'''

def viz(scene): return f'<div class="viz">{scene}</div>'

def cover(hw, ho, sub, scene):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">AlovLab · топовый рекламный ролик</span><span class="pg">1<b> / 8</b></span></div>
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

SLOTS = [
 ("1","Субъект + действие","что в кадре и что делает"),
 ("2","Сцена","где, окружение, фон"),
 ("3","Свет и стиль","премиум-реклама, настроение"),
 ("4","Камера","движение и монтаж"),
 ("5","Звук","музыка, эффекты, нативно"),
 ("6","Референсы","до 50: продукт, стиль, лицо"),
]
def method_slide():
    rows="".join(f'<div class="mrow"><div class="n">{n}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>' for n,t,s in SLOTS)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Метод · формула Seedance 2.5</span><span class="pg">5<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Топовый ролик —</span><span class="o">6 слотов.</span></h2></div>
  <div class="mlist">{rows}</div>
  {FOOT}
</article>"""

def demo_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">До / после · Seedance 2.5</span><span class="pg">6<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Тот же продукт —</span><span class="o">другой ролик.</span></h2></div>
  <div class="sfact" style="margin-top:15px"><b>Голый запрос:</b> «сделай рекламу кроссовок» — на выходе плоский сток.</div>
  <div class="pbox"><span class="tag">Seedance 2.5 · живой промпт</span><code>Белый кроссовок на бетонном постаменте, шнурки затягиваются сами, взлетает пыль — тёмная студия, один движущийся луч света — премиальная спортивная реклама, глянцевые блики — быстрый облёт камерой и слоу-мо на пике — глубокий бас и чёткий щелчок.</code>
    <div class="ru"><b>Разбор — 6 слотов:</b> субъект + действие · сцена · свет и стиль · камера · звук. Детали вместо пустоты — модель снимает кино, а не сток.</div></div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт</span><span class="pg">7<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Шаблон под</span><span class="o">свой продукт.</span></h2></div>
  <div class="pu">Польза · бренд · e-com · SMM · продакшен</div>
  <div class="pbox"><span class="tag">Seedance 2.5 · скопировать</span><code>[ПРОДУКТ] + [действие/движение] —
[сцена и свет] — [стиль: премиум-реклама, настроение] —
[движение камеры и монтаж] — [звук: музыка, эффекты].
Референсы: фото продукта, кадр-стиль, лицо (до 50).</code>
    <div class="ru"><b>Разбор:</b> заполни 6 слотов под свой товар — и получишь рекламный кадр, а не сток. Пустых мест не оставляй.</div></div>
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
 cover("Один промпт —", "два ролика.", "Слева сток, справа кино. Модель — одна и та же. Разницу делает промпт.", SC_COVER),
 sc("Проблема","Просишь","«сделай рекламу».","И получаешь плоский сток: ровный свет, ноль динамики.","ИИ снял «что-то про продукт» — потому что так и попросили.", SC_PROBLEM, 2),
 sc("Причина","Нейросеть не","додумает кадр.","Свет, ракурс, движение, звук — это режиссёрское решение.","Не скажешь — получишь среднее, что модель знает про всех.", SC_CAUSE, 3),
 sc("Ошибка","Ты меняешь","модель.","А менять надо промпт. Плоский ролик —","это плоское задание, а не слабая нейросеть.", SC_MISTAKE, 4),
 method_slide(),
 demo_slide(),
 prompt_slide(),
 cta("Собери","свой промпт.",
     ["<b>6 слотов</b> под твой продукт → рекламный кадр, а не сток",
      "формула, разбор и готовые промпты — в тетради",
      "трендовые модели: Seedance 2.5, Kling, Higgsfield"],
     "Промпты → t.me/AlovLab"),
]

HTML = f"""<title>Как сделать топовый рекламный ролик · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 8 · 11 августа · showcase + иллюстрации</span>
    <h1>Как сделать топовый рекламный ролик: обложка → проблема → 6 слотов → до/после → промпт → CTA. 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
