# -*- coding: utf-8 -*-
"""AlovLab · День 8 «Один запрос — два ответа» (бриф для ИИ) — SHOWCASE + СВОИ ИЛЛЮСТРАЦИИ.
На слайдах-концептах — bespoke SVG-сцены под каждую мысль (сплит, стена штампов, голова→слово, развилка).
Нумерация N/8. RU кроме AlovLab. Запуск: python3 scripts/carousel_showcase_day8.py"""
import pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-08-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-08-showcase.html"

EXTRA = r"""
.hsm .head h2{font-size:37px}
.cover .head h2{font-size:50px}
.cover .sub{margin-top:14px;max-width:26ch;font-size:17px}
/* область иллюстрации */
.viz{flex:1;position:relative;z-index:2;display:grid;place-items:center;min-height:0;margin-top:14px}
.viz svg{width:min(92%,480px);height:100%;max-height:360px}
.viz::before{content:"";position:absolute;left:50%;top:55%;width:74%;height:64%;transform:translate(-50%,-50%);
 background:radial-gradient(closest-side,rgba(255,120,40,.16),transparent 72%);z-index:-1;pointer-events:none}
.body.tight{margin-top:16px}
/* пу + промпт-плашка */
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
/* список брифа */
.mlist{position:relative;z-index:4;margin-top:18px;display:flex;flex-direction:column;gap:11px}
.mrow{display:flex;align-items:center;gap:14px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:14px;padding:14px 16px}
.mrow .n{flex:0 0 auto;width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:14px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o))}
.mrow .t b{font-weight:700;font-size:17px;color:#fff;line-height:1.15;display:block}
.mrow .t span{font-weight:500;font-size:13px;color:#8a8177;line-height:1.25}
/* до/после сплит */
.split{position:relative;z-index:4;margin-top:16px;display:flex;flex-direction:column;gap:12px}
.sfact{font-weight:600;font-size:14px;color:#b9ad9b;line-height:1.35}.sfact b{color:#fff}
.scard{border-radius:14px;padding:14px 16px}
.scard .lab{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.09em;text-transform:uppercase;padding:4px 9px;border-radius:6px;margin-bottom:8px}
.scard .q{font-weight:700;font-size:15.5px;line-height:1.3}.scard .r{margin-top:6px;font-weight:500;font-size:12px;line-height:1.3}
.scard.cold{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1)}
.scard.cold .lab{background:rgba(255,255,255,.1);color:#9a9084}.scard.cold .q{color:#8f867b}.scard.cold .r{color:#6f675d}
.scard.hot{background:#130c06;border:1px solid rgba(255,150,80,.32);border-left:3px solid var(--o)}
.scard.hot .lab{background:linear-gradient(150deg,var(--o2),var(--o));color:#160e07}.scard.hot .q{color:#fff}.scard.hot .r{color:#c7a184}
"""
CSS = CSS0 + EXTRA

# ---------------- BESPOKE-СЦЕНЫ ----------------
SC_COVER = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="196" y="4" width="88" height="24" rx="12" stroke="url(#ig)" stroke-width="3"/>
 <text x="240" y="21" fill="#ffcaa0" font-size="12" font-weight="800" text-anchor="middle">запрос</text>
 <path d="M240 28 V48 M130 48 H350 M130 48 V66 M350 48 V66" stroke="#6a6157" stroke-width="2.5"/>
 <rect x="40" y="72" width="176" height="166" rx="16" fill="#ffffff08" stroke="#ffffff1f" stroke-width="2"/>
 <rect x="62" y="98" width="132" height="11" rx="5.5" fill="#574e44"/>
 <rect x="62" y="122" width="132" height="11" rx="5.5" fill="#4d463d"/>
 <rect x="62" y="146" width="100" height="11" rx="5.5" fill="#4d463d"/>
 <rect x="62" y="170" width="132" height="11" rx="5.5" fill="#443e36"/>
 <rect x="62" y="194" width="84" height="11" rx="5.5" fill="#443e36"/>
 <text x="128" y="228" fill="#8a8177" font-size="12.5" font-weight="800" text-anchor="middle" letter-spacing="1.5">КАРТОН</text>
 <rect x="264" y="72" width="176" height="166" rx="16" fill="#1a1108" stroke="url(#ig)" stroke-width="2.5"/>
 <rect x="286" y="98" width="132" height="12" rx="6" fill="url(#ig)"/>
 <rect x="286" y="123" width="90" height="12" rx="6" fill="url(#ig)" opacity="0.85"/>
 <rect x="286" y="148" width="120" height="12" rx="6" fill="url(#ig)" opacity="0.7"/>
 <rect x="286" y="173" width="72" height="12" rx="6" fill="url(#ig)" opacity="0.55"/>
 <path d="M410 190 l4.5 11 11 4.5 -11 4.5 -4.5 11 -4.5 -11 -11 -4.5 11 -4.5 z" fill="url(#ig)"/>
 <text x="352" y="228" fill="#ff9a4d" font-size="12.5" font-weight="800" text-anchor="middle" letter-spacing="1.5">ЖИВОЙ</text>
</svg>'''

SC_PROBLEM = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="78" y="8" width="324" height="234" rx="18" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <rect x="100" y="30" width="156" height="28" rx="14" stroke="url(#ig)" stroke-width="2.5"/>
 <text x="112" y="48" fill="#ffcaa0" font-size="12.5" font-weight="700">напиши пост</text>
 <rect x="344" y="30" width="28" height="28" rx="9" fill="url(#ig)"/>
 <path d="M352 44 h11 M358 39 l5 5 -5 5" stroke="#160e07" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="100" y="82" width="272" height="12" rx="6" fill="#574e44"/>
 <rect x="100" y="104" width="272" height="12" rx="6" fill="#4f473e"/>
 <rect x="100" y="126" width="240" height="12" rx="6" fill="#4f473e"/>
 <rect x="100" y="148" width="272" height="12" rx="6" fill="#463f37"/>
 <rect x="100" y="170" width="208" height="12" rx="6" fill="#463f37"/>
 <rect x="100" y="192" width="272" height="12" rx="6" fill="#3f3931"/>
 <rect x="100" y="214" width="176" height="12" rx="6" fill="#3f3931"/>
</svg>'''

SC_CAUSE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <path d="M64 244 v-70 a66 66 0 0 1 132 0 v70 z" fill="#1a1108" stroke="url(#ig)" stroke-width="3"/>
 <g font-size="11.5" font-weight="700" text-anchor="middle">
  <rect x="78" y="140" width="54" height="22" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="105" y="155" fill="#ffcaa0">ниша</text>
  <rect x="138" y="140" width="58" height="22" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="167" y="155" fill="#ffcaa0">гость</text>
  <rect x="78" y="168" width="46" height="22" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="101" y="183" fill="#ffcaa0">тон</text>
  <rect x="130" y="168" width="66" height="22" rx="11" fill="#e8672a2e" stroke="url(#ig)" stroke-width="1.4"/><text x="163" y="183" fill="#ffcaa0">продукт</text>
 </g>
 <path d="M210 150 h58 M256 141 l12 9 -12 9" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 <rect x="292" y="92" width="150" height="116" rx="15" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <rect x="316" y="140" width="48" height="12" rx="6" fill="#574e44"/>
 <text x="367" y="150" fill="#6a6157" font-size="11" font-weight="700">одно слово</text>
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
 <rect x="324" y="142" width="46" height="8" rx="4" fill="url(#ig)"/>
 <rect x="324" y="158" width="46" height="8" rx="4" fill="url(#ig)" opacity="0.8"/>
 <rect x="324" y="174" width="30" height="8" rx="4" fill="url(#ig)" opacity="0.6"/>
 <text x="346" y="234" fill="#ff9a4d" font-size="12.5" font-weight="800" text-anchor="middle">бриф</text>
</svg>'''

def viz(scene): return f'<div class="viz">{scene}</div>'

def cover(hw, ho, sub, scene):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">AlovLab · как ставить задачу ИИ</span><span class="pg">1<b> / 8</b></span></div>
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

BRIEF = [
 ("1","Контекст","кто ты, для кого, что за продукт"),
 ("2","Роль","кем должен быть ИИ: редактор, стратег"),
 ("3","Критерий","что считать хорошим и что запрещено"),
]
def brief_slide():
    rows="".join(f'<div class="mrow"><div class="n">{n}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>' for n,t,s in BRIEF)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Решение</span><span class="pg">5<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Бриф — это</span><span class="o">три вещи.</span></h2></div>
  <div class="mlist">{rows}</div>
  {FOOT}
</article>"""

def demo_slide():
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">До / после</span><span class="pg">6<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Тот же запрос —</span><span class="o">другой ответ.</span></h2></div>
  <div class="split">
    <div class="sfact"><b>Задача:</b> «Напиши пост про новое меню».</div>
    <div class="scard cold"><span class="lab">Голый запрос</span><div class="q">«Мы рады представить наше новое меню»</div><div class="r">Модель заткнула пустоту самым средним. Картон.</div></div>
    <div class="scard hot"><span class="lab">Запрос + бриф</span><div class="q">Пасту крутят в круге пекорино при госте → бронь столика</div><div class="r">Тот же ИИ. Появились контекст, роль и критерий.</div></div>
  </div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт</span><span class="pg">7<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Шаблон</span><span class="o">брифа.</span></h2></div>
  <div class="pu">Польза · блогер · эксперт · SMM · бизнес</div>
  <div class="pbox"><span class="tag">Claude / ChatGPT</span><code>Контекст: ты [РОЛЬ] для [БИЗНЕС]. Аудитория: [КТО].
Продукт: [ЧТО], деталь: [ФИШКА].
Задача: [ЧТО НАПИСАТЬ].
Критерий: один хук, одна деталь, живой язык.
Запрещено: «мы рады», штампы, вода. Финал — [ДЕЙСТВИЕ].</code>
    <div class="ru"><b>Разбор:</b> три строки сверху над задачей — контекст, роль, критерий. Меняют не модель, а качество ответа.</div></div>
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
 cover("Один запрос —", "два ответа.", "Слева картон, справа живой текст. Модель — одна и та же.", SC_COVER),
 sc("Проблема","Просишь","«напиши пост».","А получаешь картон: «мы рады представить","наше новое меню» — так ИИ отвечает на голую строку.", SC_PROBLEM, 2),
 sc("Причина","ИИ не читает","мысли.","Нишу, гостя, тон, продукт ты держишь в голове.","ИИ их не видит — и затыкает пустоту средним.", SC_CAUSE, 3),
 sc("Ошибка","Ты меняешь","модель.","А менять надо бриф. Слабый ответ —","это слабо поставленная задача, а не слабый ИИ.", SC_MISTAKE, 4),
 brief_slide(),
 demo_slide(),
 prompt_slide(),
 cta("Добавь","три строки.",
     ["<b>не переписывай</b> задачу — допиши сверху 3 строки",
      "контекст · роль · критерий — и отправь заново",
      "формула и шаблон под нишу — в тетради"],
     "Тетрадь → t.me/AlovLab"),
]

HTML = f"""<title>Один запрос — два ответа · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 8 · 11 августа · showcase + иллюстрации</span>
    <h1>Одним постом: обложка → проблема → бриф → было/после → промпт → CTA. Instagram и Telegram, 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
