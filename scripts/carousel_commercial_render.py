# -*- coding: utf-8 -*-
"""AlovLab · «Одна модель. Два ценника.» — продакшн-карусель про дорогую AI-рекламу.
Сквозной кейс: премиум-кроссовки. Нарисованные кадры сток/commercial, реальные промпты
(Seedance 2.5, Gemini Omni Flash, Veo 3.1, Runway Gen-4.5), pipeline, deliverables, монетизация.
Модели сверены на 11.08.2026. Запуск: python3 scripts/carousel_commercial_render.py"""
import base64, pathlib
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, LOGO, ROOT)
from carousel_commercial_frames import frame, viz_svg, DEFS_FRAME

OUTDIR = ROOT / "exports" / "commercial-ai-carousel" / "v2"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "commercial-ai.html"
ASSET = ROOT / "content" / "carousel-assets" / "commercial"

EXTRA = r"""
.hsm .head h2{font-size:36px}
.cover .head h2{font-size:47px}
.cover .sub{margin-top:12px;max-width:30ch;font-size:15.5px}
.split2{position:relative;z-index:4;margin-top:auto;padding-top:16px;display:grid;grid-template-columns:1fr 48px 1fr;gap:8px;align-items:center}
.pf{position:relative;aspect-ratio:3/4;border-radius:14px;overflow:hidden;border:1px solid rgba(255,255,255,.14)}
.pf.good{border:2px solid var(--o);box-shadow:0 16px 44px -16px rgba(232,103,42,.65)}
.pf .ph{position:absolute;inset:0}
.pf .hint{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;
 font-size:12px;font-weight:800;color:#9a8f7f;text-align:center;padding:0 12px;line-height:1.3}
.pf .hint span{font-size:10px;font-weight:600;color:#6a6157}
.pf .lb{position:absolute;left:0;right:0;bottom:0;padding:26px 12px 11px;background:linear-gradient(0deg,rgba(0,0,0,.9),rgba(0,0,0,.5) 55%,transparent)}
.pf .lb b{font-weight:800;font-size:14px;color:#fff;display:block;letter-spacing:.04em}
.pf.good .lb b{color:var(--o2)}
.pf .lb span{font-size:9.5px;color:#c9bdac;letter-spacing:.02em}
.neq{display:flex;flex-direction:column;align-items:center;gap:3px}
.neq b{font-size:24px;font-weight:800;color:var(--o2);line-height:1}
.neq span{font-size:7px;font-weight:800;letter-spacing:.05em;color:#8a8177;text-align:center;line-height:1.25}
.mch .head h2{font-size:33px}
.body.tight{margin-top:14px;font-size:15.5px}
.viz{flex:1;position:relative;z-index:2;display:flex;align-items:center;justify-content:center;min-height:0;margin-top:12px}
.viz svg{width:min(97%,500px);height:auto}
.pw{position:relative;z-index:4;margin-top:13px;background:#0e0a06;border:1px solid rgba(255,150,80,.3);border-radius:14px;overflow:hidden}
.pw .bar{display:flex;align-items:center;gap:7px;padding:9px 14px;background:#160f08;border-bottom:1px solid rgba(255,255,255,.07)}
.pw .bar b{font-weight:800;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--o2)}
.pw .dot{width:8px;height:8px;border-radius:50%}
.pw code{display:block;padding:13px 15px;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:11.5px;
 line-height:1.5;color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pw code b{color:#fff}.pw code i{color:#8a8177;font-style:normal}
.cap{position:relative;z-index:4;margin-top:11px;font-size:13px;line-height:1.4;color:#b9ad9b}.cap b{color:#fff}
.spec{position:relative;z-index:4;margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:7px}
.spec .s{display:flex;gap:9px;align-items:baseline;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:10px;padding:8px 11px}
.spec .s b{font-weight:800;font-size:8.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--o2);min-width:52px}
.spec .s span{font-size:12px;color:#e9e2d8;line-height:1.25}
.pipe{position:relative;z-index:4;margin-top:14px;display:flex;flex-direction:column;gap:8px}
.pipe .r{display:grid;grid-template-columns:154px 1fr;gap:12px;align-items:center;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:12px;padding:10px 14px}
.pipe .r .m{font-weight:800;font-size:13.5px;color:#fff;line-height:1.1}
.pipe .r .m i{display:block;font-style:normal;font-weight:700;font-size:8.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--o2);margin-top:3px}
.pipe .r .d{font-size:12px;color:#b9ad9b;line-height:1.3}
.deliv{position:relative;z-index:4;margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.deliv .d{background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.02));border:1px solid rgba(255,140,60,.16);border-radius:11px;padding:11px 13px}
.deliv .d b{display:block;font-weight:800;font-size:16px;color:var(--o2)}
.deliv .d span{font-size:11.5px;color:#b9ad9b}
.ladder{position:relative;z-index:4;margin-top:13px;display:flex;flex-direction:column;gap:6px}
.ladder .l .bar{height:32px;border-radius:9px;background:linear-gradient(90deg,rgba(232,103,42,.5),rgba(232,103,42,.13));
 border:1px solid rgba(255,150,80,.3);display:flex;align-items:center;padding:0 14px;font-weight:800;font-size:13px;color:#fff}
.ladder .l:last-child .bar{background:linear-gradient(90deg,var(--o),var(--o2));color:#160e07}
.pack{position:relative;z-index:4;margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:7px 16px}
.pack .p{display:flex;gap:9px;align-items:baseline;font-size:13.5px;color:#e9e2d8;line-height:1.3}
.pack .p i{color:var(--o2);font-style:normal;font-weight:800}
"""
CSS = CSS0 + EXTRA

def photo_frame(name, lbl, micro, good):
    """Слот кадра на обложке. Если в content/carousel-assets/commercial/ лежит реальный
    фотореал (Nano Banana Pro) — вшиваем его. Иначе рисуем концепт-кадр тем же SVG, что и
    слайды 2–3: сток = плоский серый кроссовок, commercial = свет/rim/атмосфера."""
    p = ASSET / name
    if p.exists():
        b = base64.b64encode(p.read_bytes()).decode()
        media = f'style="background-image:url(data:image/png;base64,{b});background-size:cover;background-position:center"'
        ph = f'<div class="ph" {media}></div>'
    else:
        svg = (f'<svg viewBox="0 0 240 320" preserveAspectRatio="xMidYMid meet" '
               f'style="width:100%;height:100%;display:block">{DEFS_FRAME}{frame(0,0,240,320,good,"")}</svg>')
        ph = f'<div class="ph">{svg}</div>'
    cls = "pf good" if good else "pf"
    return f'<div class="{cls}">{ph}<div class="lb"><b>{lbl}</b><span>{micro}</span></div></div>'

def cover():
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">AlovLab · AI-реклама для брендов</span><span class="pg">1<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Одна нейросеть.</span><span class="o">Два ценника.</span></h2></div>
  <div class="sub">Слева — AI-сток. Справа — реклама, которую покупает бренд. Разница не в нейросети.</div>
  <div class="split2">
    {photo_frame("stock.png","AI-СТОК","ровный свет · центр · нет истории",False)}
    <div class="neq"><b>≠</b><span>SAME AI</span><span>DIFFERENT DIRECTION</span></div>
    {photo_frame("commercial.png","AI-COMMERCIAL","режиссура · свет · камера · атмосфера",True)}
  </div>
  {FOOT}
</article>"""

def slide2():
    fr = frame(0,0,240,176,False,"AI-СТОК")
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Главная ошибка</span><span class="pg">2<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Ты просишь</span><span class="o">«сделать рекламу».</span></h2></div>
  <div class="pw"><div class="bar"><span class="dot" style="background:#e0533a"></span><span class="dot" style="background:#e0a23a"></span><span class="dot" style="background:#4a433a"></span><b>плохой промпт</b></div>
    <code>Сделай дорогую рекламу белых кроссовок.
Кинематографично. Премиально. Как Nike.</code></div>
  {viz_svg(240,176, fr, mh=190)}
  <div class="cap"><b>Плоский свет, случайная камера, нет истории.</b> Модель получила «сделай хорошо» — и сделала среднее. Вина в брифе, не в нейросети.</div>
  {FOOT}
</article>"""

def slide3():
    callouts = (
     '<line x1="30" y1="60" x2="96" y2="92" stroke="#ff9a4d" stroke-width="1.6"/><circle cx="30" cy="60" r="3" fill="#ff9a4d"/><text x="14" y="52" fill="#ff9a4d" font-size="11" font-weight="800" font-family="Manrope">LIGHT · amber rim</text>'
     '<line x1="270" y1="60" x2="196" y2="92" stroke="#ff9a4d" stroke-width="1.6"/><circle cx="270" cy="60" r="3" fill="#ff9a4d"/><text x="176" y="52" fill="#ff9a4d" font-size="11" font-weight="800" font-family="Manrope">CAMERA · low dolly</text>'
     '<line x1="34" y1="150" x2="96" y2="130" stroke="#ff9a4d" stroke-width="1.6"/><circle cx="34" cy="150" r="3" fill="#ff9a4d"/><text x="14" y="170" fill="#ff9a4d" font-size="11" font-weight="800" font-family="Manrope">FOREGROUND · reflection</text>'
     '<line x1="266" y1="150" x2="200" y2="126" stroke="#ff9a4d" stroke-width="1.6"/><circle cx="266" cy="150" r="3" fill="#ff9a4d"/><text x="176" y="170" fill="#ff9a4d" font-size="11" font-weight="800" font-family="Manrope">ACTION · laces tighten</text>'
    )
    fr = frame(0,0,300,236,True,"COMMERCIAL FRAME",callouts=callouts)
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Как мыслит режиссёр</span><span class="pg">3<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Модель — кадр.</span><span class="o">Режиссёр — смысл.</span></h2></div>
  {viz_svg(300,236, fr, mh=300)}
  <div class="cap"><b>Ты видишь режиссуру:</b> свет, камера, действие, звук — заданы, а не случайны.</div>
  {FOOT}
</article>"""

def slide4():
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Seedance 2.5 · референсы</span><span class="pg">4<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Дорогой кадр —</span><span class="o">это референсы.</span></h2></div>
  <div class="spec">
    <div class="s"><b>Ref 1</b><span>продукт — геометрия, лого 1:1</span></div>
    <div class="s"><b>Ref 2</b><span>свет — тёмная студия, rim</span></div>
    <div class="s"><b>Ref 3</b><span>движение камеры</span></div>
    <div class="s"><b>Ref 4</b><span>среда — мокрый бетон</span></div>
    <div class="s"><b>Ref 5</b><span>ритм и звук</span></div>
    <div class="s"><b>Модель</b><span>до 50 референсов · 4K · звук</span></div>
  </div>
  <div class="pw"><div class="bar"><span class="dot" style="background:var(--o)"></span><b>Seedance 2.5 · prompt</b></div>
    <code><i>@ref1</i> product — keep geometry, sole, logo, white 1:1.
<i>@ref2</i> lighting: dark studio, narrow warm rim, deep blacks.
Extreme low-angle macro on wet concrete; laces slowly self-tighten;
controlled lateral dolly; rim light travels the material; hard cut
to a first step, asphalt ripples. Native SFX: lace tension, wet step.</code></div>
  {FOOT}
</article>"""

def slide5():
    fr = frame(4,4,150,150,True,"V1 · чисто") + frame(346,4,150,150,True,"V2 · напряжение")
    fr += ('<path d="M188 78 h120 M296 69 l13 9 -13 9" stroke="url(#ig)" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
           '<text x="248" y="62" fill="#ff9a4d" font-size="12" font-weight="800" font-family="Manrope" text-anchor="middle">EDIT</text>'
           '<text x="248" y="96" fill="#8a8177" font-size="10.5" font-family="Manrope" text-anchor="middle">разговором</text>')
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Gemini Omni Flash · правка</span><span class="pg">5<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Не регенерация —</span><span class="o">режиссёрская правка.</span></h2></div>
  {viz_svg(496,158, fr, mh=150)}
  <div class="pw"><div class="bar"><span class="dot" style="background:var(--o)"></span><b>conversational edit</b></div>
    <code><b>Keep</b> the shoe, framing and camera path unchanged.
<b>Change only:</b> reduce fill light 30%; deepen wet-asphalt
reflections; add subtle mist; delay the hero light to the last second.
Do not alter shoe geometry, logo, camera path or duration.</code></div>
  {FOOT}
</article>"""

PIPE = [
 ("Nano Banana Pro","image","master-кадр продукта 1:1 + текст"),
 ("Seedance 2.5","сцена","до 50 референсов, кинокадр, звук"),
 ("Gemini Omni Flash","правка","режиссёрский edit разговором"),
 ("Veo 3.1","звук","нативный 3D-звук, image-to-video, 4K"),
 ("Runway Gen-4.5","камера","точная хореография камеры в промпте"),
 ("Higgsfield","workflow","пресеты движения и сборка"),
]
def slide6():
    rows="".join(f'<div class="r"><div class="m">{m}<i>{f}</i></div><div class="d">{d}</div></div>' for m,f,d in PIPE)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Один ролик — разным моделям</span><span class="pg">6<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Не одна модель.</span><span class="o">Продакшн-конвейер.</span></h2></div>
  <div class="pipe">{rows}</div>
  {FOOT}
</article>"""

def slide7():
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">За что платит бренд</span><span class="pg">7<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Клиент покупает</span><span class="o">не генерацию.</span></h2></div>
  <div class="deliv">
    <div class="d"><b>1× Hero</b><span>15 сек, вертикаль</span></div>
    <div class="d"><b>3× Cutdown</b><span>6 сек под рекламу</span></div>
    <div class="d"><b>5× Hook</b><span>соцсети, первые секунды</span></div>
    <div class="d"><b>4× Frame</b><span>продуктовые кадры</span></div>
    <div class="d"><b>1× Storyboard</b><span>раскадровка</span></div>
    <div class="d"><b>1× Sound</b><span>звуковая режиссура</span></div>
  </div>
  <div class="ladder">
    <div class="l"><div class="bar" style="width:40%">Генерация</div></div>
    <div class="l"><div class="bar" style="width:60%">Ролик</div></div>
    <div class="l"><div class="bar" style="width:80%">Концепт + ролик</div></div>
    <div class="l"><div class="bar" style="width:100%">Кампания-система</div></div>
  </div>
  <div class="cap"><b>Ты продаёшь не «умею Seedance».</b> Ты продаёшь собранную рекламную кампанию.</div>
  {FOOT}
</article>"""

def slide8():
    return f"""<article class="slide cta">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings" style="top:120%">{rings()}</div></div>
  <div class="top"><span class="eb">Дальше</span><span class="pg">8<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Собери commercial,</span><span class="o">не стыдно бренду.</span></h2></div>
  <div class="pack">
    <div class="p"><i>✓</i>рекламный бриф</div><div class="p"><i>✓</i>storyboard-шаблон</div>
    <div class="p"><i>✓</i>Seedance 2.5 промпт</div><div class="p"><i>✓</i>Gemini Omni edit</div>
    <div class="p"><i>✓</i>карта моделей</div><div class="p"><i>✓</i>bad→good чек-лист</div>
    <div class="p"><i>✓</i>чек-лист сдачи</div><div class="p"><i>✓</i>референс-борды</div>
  </div>
  <div class="btn">Забрать PRODUCTION PACK → t.me/AlovLab</div>
  {FOOT}
</article>"""

SLIDES = [cover(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8()]

HTML = f"""<title>Одна модель. Два ценника. · AI-реклама · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · AI-реклама для брендов · продакшн-кейс</span>
    <h1>Как делать дорогую AI-рекламу и продавать её бизнесу. Сквозной кейс: премиум-кроссовки. 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
