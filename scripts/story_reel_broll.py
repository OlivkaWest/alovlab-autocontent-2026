# -*- coding: utf-8 -*-
"""AlovLab · B-roll под рил Дня 11 «Канцелярия vs Живой текст» (замена пустых кадров агента).
3 сцены 9:16 (1080×1920): (1) редактор «канцелярия → промпт → живой» (реальные оба текста,
БЕЗ фейкового интерфейса), (2) сплит было/стало с обоими абзацами, (3) CTA с логотипом и Telegram.
Рендер — story_shoot.js. Запуск: python3 scripts/story_reel_broll.py"""
from carousel_showcase_render import CSS as BASECSS, LOGO, ROOT, sparks

OUTDIR = ROOT / "exports" / "heygen-broll" / "reel-text"; OUTDIR.mkdir(parents=True, exist_ok=True)

KANC = ('<span class="lab">Канцелярия</span>'
        '«<s>В современном мире</s> нейросети <s>являются важным инструментом</s> '
        'для <s>повышения эффективности</s> создания контента.»')
LIVE = ('<span class="lab live">Живой</span>'
        '«Нейросеть накидает черновик. Ты правишь — и постишь. Без возни с чистого листа.»')
PROMPT_TXT = 'перепиши живой речью: сильное начало, короткие фразы, без штампов'

SHELL = r"""
.stagewrap{display:flex;justify-content:center;padding:40px;background:#050403}
.story{position:relative;width:540px;height:960px;background:radial-gradient(125% 75% at 82% 2%,#20140a,#0a0806 58%);
 border-radius:30px;overflow:hidden;padding:36px 30px 26px;display:flex;flex-direction:column;box-shadow:0 40px 90px -30px #000}
.story .eb{position:relative;z-index:3;font-weight:800;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--o2)}
.story h2{position:relative;z-index:3;margin-top:9px;font-weight:800;font-size:42px;line-height:1.02;letter-spacing:-.02em;color:#fff}
.story h2 b{color:var(--o2);font-weight:800}
.story .sub{position:relative;z-index:3;margin-top:8px;font-size:15px;color:#c2b6a4;font-weight:600}
.body{position:relative;z-index:3;flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px;margin-top:16px}
.doc{background:#131009;border:1px solid rgba(255,255,255,.1);border-radius:15px;padding:15px 17px;font-size:15px;line-height:1.5;color:#9a8f7f}
.doc .lab{display:inline-block;font-weight:800;font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:#8a8177;margin-bottom:8px;
 background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);padding:3px 9px;border-radius:6px}
.doc .lab.live{color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border:none}
.doc s{color:#c56b43;text-decoration-color:#c56b43;text-decoration-thickness:2px}
.doc.live{background:#170e07;border:1px solid rgba(255,150,80,.4);color:#ffe4c8;font-weight:600;box-shadow:0 12px 34px -16px rgba(232,103,42,.5)}
.pbar{display:flex;align-items:flex-start;gap:11px;background:linear-gradient(180deg,rgba(232,103,42,.15),rgba(255,255,255,.02));
 border:1px solid rgba(232,103,42,.42);border-radius:13px;padding:12px 15px}
.pbar .k{flex:0 0 auto;font-weight:800;font-size:9px;letter-spacing:.06em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));border-radius:6px;padding:4px 9px;margin-top:1px}
.pbar .p{font-size:13.5px;line-height:1.4;color:#ffd9b8;font-weight:600}
.arrow{position:relative;z-index:3;text-align:center;color:var(--o2);font-size:18px;font-weight:800;line-height:.3}
.tag2{position:relative;z-index:3;align-self:center;margin-top:2px;font-weight:800;font-size:13px;color:#c2b6a4}
.tag2 b{color:var(--o2)}
.foot{position:relative;z-index:3;margin-top:14px;display:flex;align-items:center;justify-content:space-between}
.foot .lg{display:flex;align-items:center;gap:9px}.foot .lg img{width:30px;height:30px;border-radius:8px}
.foot .lg b{font-weight:800;font-size:17px;color:#fff}.foot .lg b i{color:var(--o2);font-style:normal}
.foot .rt{font-size:11px;font-weight:700;color:#8a8177}
.pre{opacity:0}
/* CTA */
.cta{justify-content:center;text-align:center}
.cta .lgbig{width:60px;height:60px;border-radius:15px;margin:0 auto 18px}
.cta h2{font-size:40px}
.cta .list{position:relative;z-index:3;margin:20px 0;display:flex;flex-direction:column;gap:10px;text-align:left}
.cta .list .li{display:flex;align-items:center;gap:11px;font-size:16px;color:#e2d8c9;font-weight:600}
.cta .list .li i{width:9px;height:9px;border-radius:50%;background:var(--o2);flex:0 0 auto;box-shadow:0 0 8px 1px rgba(255,140,60,.7)}
.cta .btn{position:relative;z-index:3;margin:6px auto 0;font-weight:800;font-size:16px;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));border-radius:14px;padding:15px 24px;box-shadow:0 16px 34px -12px rgba(232,103,42,.8)}
"""
CSS = BASECSS + SHELL

def foot(rt):
    return (f'<div class="foot"><div class="lg"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div>'
            f'<div class="rt">{rt}</div></div>')

def scene_claude(reveal=3):
    p = ' pre' if reveal < 2 else ''
    l = ' pre' if reveal < 3 else ''
    return f"""<section class="story">
  <div class="sparks">{sparks()}</div>
  <div class="eb">AlovLab · промпт-редактор</div>
  <h2>Канцелярия <b>→ живой</b></h2>
  <div class="body">
    <div class="doc">{KANC}</div>
    <div class="pbar{p}"><span class="k">промпт</span><span class="p">{PROMPT_TXT}</span></div>
    <div class="arrow{l}">↓</div>
    <div class="doc live{l}">{LIVE}</div>
  </div>
  {foot("смысл тот же — но дочитывают")}
</section>"""

SPLIT = f"""<section class="story">
  <div class="sparks">{sparks()}</div>
  <div class="eb">AlovLab · одна мысль, две подачи</div>
  <h2>Было <b>/ стало</b></h2>
  <div class="body">
    <div class="doc">{KANC}</div>
    <div class="tag2">та же мысль <b>↓</b></div>
    <div class="doc live">{LIVE}</div>
  </div>
  {foot("канцелярия ≠ живой текст")}
</section>"""

CTA = f"""<section class="story cta">
  <div class="sparks">{sparks()}</div>
  <div style="position:relative;z-index:3;margin:auto 0">
    <img class="lgbig" src="data:image/png;base64,{LOGO}">
    <h2>Пиши так,<br><b>чтобы дочитывали.</b></h2>
    <div class="list">
      <div class="li"><i></i>промпт-редактор для Claude</div>
      <div class="li"><i></i>структура поста и продающего</div>
      <div class="li"><i></i>стоп-лист фраз + разборы до/после</div>
    </div>
    <div class="btn">Тетрадь дня → t.me/AlovLab</div>
    <div style="margin-top:14px;font-size:12px;color:#8a8177;font-weight:700">ссылка в профиле</div>
  </div>
</section>"""

def html(inner):
    return f'<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>{CSS}</style><div class="stagewrap">{inner}</div>'

pages = {"scene-claude": scene_claude(3), "scene-split": SPLIT, "scene-cta": CTA}
pages["claude-step-1"] = scene_claude(1)
pages["claude-step-2"] = scene_claude(2)
pages["claude-step-3"] = scene_claude(3)
for name, inner in pages.items():
    (OUTDIR / f"{name}.html").write_text(html(inner), encoding="utf-8")
print("HTML:", ", ".join(pages))
