# -*- coding: utf-8 -*-
"""AlovLab · B-roll для HeyGen-сторис: сцена 3 «путь новичка» + сцена 4 «тарифы».
9:16 (1080×1920), тот же стиль, что сцена 2. Реальный смысл в каждом элементе, без фейкового UI.
Тарифы/включённое — реальные из закрепа. Без зачёркнутых цен, таймеров, «осталось мест».
Запуск: python3 scripts/story_broll_build.py  (рендер — story_shoot.js)"""
import base64, math
from carousel_showcase_render import CSS as BASECSS, LOGO, ROOT, sparks

OUTDIR = ROOT / "exports" / "heygen-broll" / "stories-course"; OUTDIR.mkdir(parents=True, exist_ok=True)
ASSET = ROOT / "content" / "carousel-assets" / "commercial"
def b64(name): return base64.b64encode((ASSET / name).read_bytes()).decode()

SHELL = r"""
.stagewrap{display:flex;justify-content:center;padding:40px;background:#050403}
.story{position:relative;width:540px;height:960px;background:radial-gradient(125% 75% at 82% 2%,#20140a,#0a0806 58%);
 border-radius:30px;overflow:hidden;padding:36px 30px 24px;display:flex;flex-direction:column;box-shadow:0 40px 90px -30px #000}
.story .eb{position:relative;z-index:3;font-weight:800;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--o2)}
.story h2{position:relative;z-index:3;margin-top:9px;font-weight:800;font-size:44px;line-height:1.0;letter-spacing:-.02em;color:#fff}
.story h2 b{color:var(--o2);font-weight:800}
.story .sub{position:relative;z-index:3;margin-top:9px;font-size:15px;color:#c2b6a4;font-weight:600}
.foot{position:relative;z-index:3;margin-top:16px;display:flex;align-items:center;justify-content:space-between}
.foot .lg{display:flex;align-items:center;gap:9px}.foot .lg img{width:30px;height:30px;border-radius:8px}
.foot .lg b{font-weight:800;font-size:17px;color:#fff}.foot .lg b i{color:var(--o2);font-style:normal}
.foot .rt{font-size:11px;font-weight:700;color:#8a8177}
.pre{opacity:0}
.thumb{border-radius:9px;overflow:hidden;border:1px solid rgba(255,255,255,.13);line-height:0}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
/* ---- сцена 3 · путь новичка ---- */
.steps{position:relative;z-index:3;flex:1;display:flex;flex-direction:column;justify-content:space-evenly;gap:4px;margin-top:12px}
.step{display:flex;align-items:center;gap:16px;background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.16);border-radius:16px;padding:15px 17px}
.step.res{border-color:rgba(255,150,80,.4);box-shadow:0 14px 34px -16px rgba(232,103,42,.5)}
.step .vis{width:132px;height:96px;flex:0 0 auto;border-radius:11px;background:#100a06;border:1px solid rgba(255,255,255,.1);
 display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative}
.step .tx b{display:block;font-weight:800;font-size:17px;color:#fff;line-height:1.1}
.step .tx span{display:block;margin-top:4px;font-size:12.5px;color:#8a8177;line-height:1.25}
.step .tx .tag{display:inline-block;margin-top:7px;font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:.04em;
 color:var(--o2);background:rgba(232,103,42,.13);border:1px solid rgba(232,103,42,.3);border-radius:20px;padding:3px 9px}
.arrowdown{position:relative;z-index:3;text-align:center;color:var(--o2);font-size:17px;font-weight:800;line-height:.4;margin:1px 0}
.resmini{display:flex;gap:5px;width:100%;height:100%;padding:8px}
.resmini .col{display:flex;flex-direction:column;gap:4px;justify-content:center;flex:1}
.resmini .ln{height:5px;border-radius:3px;background:linear-gradient(90deg,rgba(255,150,80,.7),rgba(255,150,80,.2))}
.bigtitle{position:relative;z-index:3;margin-top:12px;font-weight:800;font-size:22px;line-height:1.06;color:#fff;letter-spacing:-.01em}
.bigtitle b{color:var(--o2)}
.smallnote{position:relative;z-index:3;margin-top:6px;font-size:12.5px;color:#8a8177;font-weight:600}
/* laptop glyph */
.lap{width:88px}
/* ---- сцена 4 · тарифы ---- */
.tcards{position:relative;z-index:3;flex:1;display:flex;flex-direction:column;gap:13px;margin-top:16px;justify-content:space-evenly}
.tc{position:relative;background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.16);border-radius:18px;padding:15px 18px}
.tc.pro{border:2px solid var(--o);box-shadow:0 20px 48px -16px rgba(232,103,42,.6);
 background:linear-gradient(180deg,rgba(232,103,42,.15),rgba(255,255,255,.02))}
.tc .hd{display:flex;align-items:baseline;justify-content:space-between;gap:10px}
.tc .nm{font-weight:800;font-size:21px;color:#fff;letter-spacing:.02em}
.tc .nm small{display:block;font-weight:700;font-size:11px;color:#8a8177;letter-spacing:.02em;margin-top:2px}
.tc .pr{font-weight:800;font-size:23px;color:var(--o2);white-space:nowrap}
.tc .hit{position:absolute;top:-10px;right:18px;font-size:10px;font-weight:800;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:4px 11px;border-radius:20px;letter-spacing:.06em}
.tc .inside{margin-top:11px;display:flex;flex-wrap:wrap;gap:6px}
.tc .ic{font-size:11px;font-weight:600;color:#d0c4b4;background:rgba(255,255,255,.05);border:1px solid rgba(255,140,60,.14);border-radius:8px;padding:4px 9px}
.tc.pro .ic{color:#ffe4c8;border-color:rgba(255,150,80,.32)}
.tfoot{position:relative;z-index:3;margin-top:14px;text-align:center;font-weight:800;font-size:16px;color:#c2b6a4}
.tfoot b{color:#fff}
"""
CSS = BASECSS + SHELL

def foot(rt):
    return (f'<div class="foot"><div class="lg"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div>'
            f'<div class="rt">{rt}</div></div>')

# ---------------- СЦЕНА 3 · путь новичка ----------------
LAPTOP = ('<svg class="lap" viewBox="0 0 88 64" fill="none">'
 '<rect x="10" y="6" width="68" height="44" rx="4" fill="#0d0a06" stroke="#4a433a" stroke-width="2"/>'
 '<rect x="18" y="26" width="44" height="9" rx="4.5" fill="none" stroke="#5a5148" stroke-width="1.6"/>'
 '<rect x="21" y="29.5" width="2" height="2" rx="1" fill="#8a8177"/>'
 '<path d="M4 56 h80 l-6 -6 H10 z" fill="#161009" stroke="#4a433a" stroke-width="2"/></svg>')
PROMPT_BUBBLE = ('<div style="width:100%;padding:0 10px"><div style="background:rgba(232,103,42,.16);border:1px solid rgba(232,103,42,.4);'
 'border-radius:12px 12px 12px 3px;padding:9px 11px;font-size:12px;color:#ffd9b8;font-weight:600;line-height:1.3">'
 '«сделай пост про мой продукт»</div></div>')
RESMINI = ('<div class="resmini"><div class="col"><div class="ln" style="width:100%"></div><div class="ln" style="width:78%"></div>'
 '<div class="ln" style="width:90%"></div></div>'
 f'<div class="thumb" style="flex:0 0 34px"><img src="data:image/jpeg;base64,{b64("commercial.jpg")}"></div>'
 f'<div class="thumb" style="flex:0 0 34px;position:relative"><img src="data:image/jpeg;base64,{b64("master.jpg")}">'
 '<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-size:9px">▶</div></div></div>')

def scene3(reveal=3):
    steps = [
      (f'<div class="vis">{LAPTOP}</div>', "Чистый лист", "пустой чат, ни одного запроса", "0 опыта", ""),
      (f'<div class="vis" style="width:132px">{PROMPT_BUBBLE}</div>', "Первый запрос", "простыми словами, без терминов", "по шаблону", ""),
      (f'<div class="vis">{RESMINI}</div>', "Первый результат", "текст · картинка · видео", "готово", "res"),
    ]
    rows = []
    for i, (vis, ttl, sub, tag, cls) in enumerate(steps):
        pre = " pre" if (i + 1) > reveal else ""
        if i > 0:
            rows.append(f'<div class="arrowdown{pre}">↓</div>')
        rows.append(f'<div class="step{(" "+cls) if cls else ""}{pre}">{vis}'
                    f'<div class="tx"><b>{ttl}</b><span>{sub}</span><span class="tag">{tag}</span></div></div>')
    return f"""<section class="story">
  <div class="sparks">{sparks()}</div>
  <div class="eb">AlovLab · курс с нуля</div>
  <h2>Путь новичка</h2>
  <div class="sub">открыл → повторил → получил результат</div>
  <div class="steps">{''.join(rows)}</div>
  <div class="bigtitle">С нуля. <b>Без технического языка.</b></div>
  {foot("даже если ни разу не пробовал")}
</section>"""

# ---------------- СЦЕНА 4 · тарифы ----------------
def tc(nm, sub, pr, inside, pro=False, hit=False, pre=False):
    ics = "".join(f'<span class="ic">{i}</span>' for i in inside)
    hitb = '<span class="hit">ХИТ</span>' if hit else ''
    p = " pre" if pre else ""
    return (f'<div class="tc{" pro" if pro else ""}{p}">{hitb}'
            f'<div class="hd"><div class="nm">{nm}<small>{sub}</small></div><div class="pr">{pr}</div></div>'
            f'<div class="inside">{ics}</div></div>')

def scene4(reveal=3):
    cards = [
      dict(nm="МИНИ", sub="попробовать", pr="2 999 ₽", inside=["Модуль «Земля Слов»", "закрытый ТГ-канал", "ИИ-ассистент"]),
      dict(nm="БАЗОВЫЙ", sub="весь курс", pr="14 990 ₽", inside=["6 уроков · 6 Земель", "канал + ассистент", "обновления"]),
      dict(nm="ПРО", sub="курс + менторство", pr="49 990 ₽", inside=["всё из Базового", "доступ навсегда", "сертификат", "проверка заданий", "менторство", "клуб"], pro=True, hit=True),
    ]
    html_cards = "".join(tc(**c, pre=(i + 1) > reveal) for i, c in enumerate(cards))
    return f"""<section class="story">
  <div class="sparks">{sparks()}</div>
  <div class="eb">AlovLab · три уровня входа</div>
  <h2>Заходишь <b>с любого</b></h2>
  <div class="sub">выбираешь глубину — система одна</div>
  <div class="tcards">{html_cards}</div>
  <div class="tfoot">Гарантия возврата <b>14 дней</b></div>
  {foot("без таймеров и «мест»")}
</section>"""

VARIANTS = [("scene3-path", scene3()), ("scene4-tariffs", scene4())]
VARIANTS += [(f"scene3-step-{i}", scene3(i)) for i in range(1, 4)]
VARIANTS += [(f"scene4-card-{i}", scene4(i)) for i in range(1, 4)]
for name, html in VARIANTS:
    out = OUTDIR / f"{name}.html"
    out.write_text(f'<title>{name} · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>{CSS}</style><div class="stagewrap">{html}</div>', encoding="utf-8")
print("HTML: base + scene3-step-1..3 + scene4-card-1..3")
