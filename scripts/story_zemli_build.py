# -*- coding: utf-8 -*-
"""AlovLab · B-roll для HeyGen-сторис (сцена 2): сетка «6 Земель ИИ» — 9:16 (1080×1920).
Реальные примеры, не пустые карточки: ИЗОБРАЖЕНИЯ/ВИДЕО — настоящие AI-кадры проекта,
ЗВУК — waveform, СЛОВА/ЗНАНИЯ — типографика запрос→результат, АВАТАРЫ — портрет→субтитры.
Без фейкового окна приложения. Запуск: python3 scripts/story_zemli_build.py"""
import base64, math
from carousel_showcase_render import CSS as BASECSS, LOGO, ROOT, sparks

OUTDIR = ROOT / "exports" / "heygen-broll" / "stories-course"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "scene2-6-zemel.html"
ASSET = ROOT / "content" / "carousel-assets" / "commercial"

def b64(name):
    return base64.b64encode((ASSET / name).read_bytes()).decode()

def wave(n=30, w=150, h=40):
    bars = []
    for i in range(n):
        v = abs(math.sin(i * 1.6 + 1) * 0.6 + math.sin(i * 0.5) * 0.4)
        bh = 5 + v * (h - 8); x = i * (w / n)
        bars.append(f'<rect x="{x:.1f}" y="{(h-bh)/2:.1f}" width="2.4" height="{bh:.1f}" rx="1.2" fill="#ff9a4d"/>')
    return f'<svg viewBox="0 0 {w} {h}" preserveAspectRatio="none" style="width:100%;height:100%">{"".join(bars)}</svg>'

EXTRA = r"""
.stagewrap{display:flex;justify-content:center;padding:40px;background:#050403}
.story{position:relative;width:540px;height:960px;background:radial-gradient(125% 75% at 82% 2%,#20140a,#0a0806 58%);
 border-radius:30px;overflow:hidden;padding:36px 30px 24px;display:flex;flex-direction:column;box-shadow:0 40px 90px -30px #000}
.story .eb{position:relative;z-index:3;font-weight:800;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--o2)}
.story h2{position:relative;z-index:3;margin-top:9px;font-weight:800;font-size:46px;line-height:.98;letter-spacing:-.02em;color:#fff}
.story h2 b{color:var(--o2);font-weight:800}
.story .sub{position:relative;z-index:3;margin-top:9px;font-size:15px;color:#c2b6a4;font-weight:600}
.zgrid{position:relative;z-index:3;margin-top:18px;flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:13px}
.z{position:relative;background:linear-gradient(180deg,rgba(255,255,255,.05),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.16);border-radius:16px;padding:12px 13px 11px;display:flex;flex-direction:column;overflow:hidden}
.z .lab{display:flex;align-items:center;gap:8px;font-weight:800;font-size:13px;letter-spacing:.03em;color:#fff}
.z .lab .n{width:20px;height:20px;border-radius:6px;background:linear-gradient(150deg,var(--o2),var(--o));color:#160e07;
 font-size:11px;display:flex;align-items:center;justify-content:center;font-weight:800;flex:0 0 auto}
.z .mid{flex:1;display:flex;align-items:center;justify-content:center;gap:8px;margin-top:10px;min-height:0}
.z .mc{font-size:10.5px;color:#8a8177;margin-top:8px;font-weight:600;line-height:1.2}
.z .mc b{color:var(--o2)}
.thumb{height:100%;border-radius:9px;overflow:hidden;border:1px solid rgba(255,255,255,.13);line-height:0;flex:1}
.thumb img{width:100%;height:100%;object-fit:cover;display:block}
.arrow{color:var(--o2);font-weight:800;font-size:16px;flex:0 0 auto}
.playdot{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:30px;height:30px;border-radius:50%;
 background:rgba(0,0,0,.45);border:1.5px solid #fff;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px}
/* СЛОВА / ЗНАНИЯ типографика */
.txt{width:100%;display:flex;flex-direction:column;gap:5px}
.pill{align-self:flex-start;font-size:10px;font-weight:800;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:20px;padding:3px 9px;letter-spacing:.02em}
.ln{height:6px;border-radius:3px;background:linear-gradient(90deg,rgba(255,150,80,.75),rgba(255,150,80,.2))}
.ln.g{background:#3a342c}
.srcs{display:flex;gap:5px;flex-wrap:wrap}
.chip{font-size:9px;font-weight:700;color:#c9bdac;border:1px solid #4a433a;border-radius:8px;padding:2px 7px}
/* АВАТАР */
.av{display:flex;align-items:center;gap:10px;width:100%;justify-content:center}
.avhead{width:44px;height:44px;border-radius:50%;background:radial-gradient(circle at 50% 38%,#2a2018,#161009);
 border:1.5px solid rgba(255,150,80,.4);position:relative;flex:0 0 auto;overflow:hidden}
.avhead::before{content:"";position:absolute;left:50%;top:24%;width:15px;height:15px;border-radius:50%;transform:translateX(-50%);background:#6a6157}
.avhead::after{content:"";position:absolute;left:50%;bottom:-3px;width:30px;height:22px;border-radius:50% 50% 0 0;transform:translateX(-50%);background:#6a6157}
.subs{display:flex;flex-direction:column;gap:4px;flex:1;max-width:96px}
.subs .s{height:6px;border-radius:3px;background:linear-gradient(90deg,var(--o2),rgba(255,150,80,.15))}
.motion{position:absolute;right:9px;top:34px;display:flex;flex-direction:column;gap:3px}
.motion i{display:block;width:16px;height:2.5px;border-radius:2px;background:var(--o2);opacity:.85}
.motion i:nth-child(2){width:11px;opacity:.6}.motion i:nth-child(3){width:7px;opacity:.4}
.foot{position:relative;z-index:3;margin-top:16px;display:flex;align-items:center;justify-content:space-between}
.foot .lg{display:flex;align-items:center;gap:9px}
.foot .lg img{width:30px;height:30px;border-radius:8px}
.foot .lg b{font-weight:800;font-size:17px;color:#fff}.foot .lg b i{color:var(--o2);font-style:normal}
.foot .rt{font-size:11px;font-weight:700;color:#8a8177}
"""
CSS = BASECSS + EXTRA

def z(n, name, mid, mc):
    return f'<div class="z"><div class="lab"><span class="n">{n}</span>{name}</div><div class="mid">{mid}</div><div class="mc">{mc}</div></div>'

# 1 СЛОВА — запрос → структурированный текст
z_slova = z("1", "СЛОВА",
  '<div class="txt"><span class="pill">запрос</span><div class="ln" style="width:100%"></div><div class="ln" style="width:82%"></div><div class="ln" style="width:64%"></div></div>',
  'запрос → <b>структура</b>')
# 2 ИЗОБРАЖЕНИЯ — реф → AI (реальные кадры)
z_img = z("2", "ИЗОБРАЖЕНИЯ",
  f'<div class="thumb"><img src="data:image/jpeg;base64,{b64("stock.jpg")}"></div><span class="arrow">→</span><div class="thumb"><img src="data:image/jpeg;base64,{b64("commercial.jpg")}"></div>',
  'реф → <b>AI-визуал</b>')
# 3 ВИДЕО — кадр → движение (реальный кадр + play)
z_video = z("3", "ВИДЕО",
  f'<div class="thumb" style="position:relative;width:100%"><img src="data:image/jpeg;base64,{b64("commercial.jpg")}"><div class="playdot">▶</div><div class="motion"><i></i><i></i><i></i></div></div>',
  'кадр → <b>движение</b>')
# 4 ЗВУК — waveform
z_zvuk = z("4", "ЗВУК",
  f'<div style="width:100%;height:100%;display:flex;align-items:center">{wave()}</div>',
  'текст → <b>голос</b>')
# 5 АВАТАРЫ — портрет → говорящий (субтитры)
z_avatar = z("5", "АВАТАРЫ",
  '<div class="av"><div class="avhead"></div><span class="arrow">→</span><div class="subs"><span class="s" style="width:100%"></span><span class="s" style="width:74%"></span><span class="s" style="width:88%"></span></div></div>',
  'фото → <b>говорящий аватар</b>')
# 6 ЗНАНИЯ — источники → конспект
z_know = z("6", "ЗНАНИЯ",
  '<div class="txt"><div class="srcs"><span class="chip">источник</span><span class="chip">данные</span><span class="chip">факт</span></div>'
  '<div class="ln" style="width:100%;margin-top:3px"></div><div class="ln" style="width:88%"></div><div class="ln g" style="width:70%"></div></div>',
  'источники → <b>конспект</b>')

STORY = f"""<section class="story">
  <div class="sparks">{sparks()}</div>
  <div class="eb">AlovLab · курс «Нейросети для каждого»</div>
  <h2><b>6</b> Земель ИИ</h2>
  <div class="sub">6 навыков → одна система</div>
  <div class="zgrid">{z_slova}{z_img}{z_video}{z_zvuk}{z_avatar}{z_know}</div>
  <div class="foot"><div class="lg"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div>
    <div class="rt">от нуля до результата</div></div>
</section>"""

HTML = f"""<title>6 Земель ИИ · story B-roll · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="stagewrap">{STORY}</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB")
