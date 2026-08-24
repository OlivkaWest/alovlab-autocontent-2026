# -*- coding: utf-8 -*-
"""AlovLab · День 21 (24.08) «Прогрев: от подписки до заявки» — сборка карусели.
Кадры пользователя (scene-only, ChatGPT) в content/carousel-assets/day-21/s1..s8.
Кроп cover в 4:5 + впечатанный заголовок (белый+оранжевый) + нумерация N/8 + подпись-логотип AlovLab.
Слайд 7 уже честно поправлен в PIL (плашка вместо выдуманного «+76 заявок»).
Сборка: python3 scripts/carousel_day21_build.py → node scripts/carousel_shoot.js <html> <outdir>"""
import base64, pathlib
from carousel_showcase_render import CSS as CSS0, LOGO, ROOT

OUTDIR = ROOT / "exports" / "carousels" / "day-21"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-21.html"
ASSET = ROOT / "content" / "carousel-assets" / "day-21"

def img_src(name):
    p = ASSET / (name + ".png")
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()

EXTRA = r"""
.d21{position:relative;width:540px;height:675px;overflow:hidden;background:#0a0806;border-radius:0}
.d21 .bg{position:absolute;inset:0;background-size:cover}
.d21 .scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,5,4,.94) 3%,rgba(6,5,4,.66) 26%,rgba(6,5,4,0) 48%,rgba(6,5,4,0) 78%,rgba(6,5,4,.55) 100%)}
.d21 .top{position:absolute;left:30px;right:26px;top:24px;display:flex;justify-content:space-between;align-items:flex-start}
.d21 .eb{font-weight:800;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--o2);max-width:60%;line-height:1.3}
.d21 .pg{display:flex;align-items:center;gap:2px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.2);
 border-radius:20px;padding:6px 12px;font-weight:800;font-size:14px;color:#fff}
.d21 .pg b{color:var(--o2)}
.d21 .hd{position:absolute;left:32px;right:32px;top:54px}
.d21 .hd h2{font-weight:800;font-size:40px;line-height:1.0;letter-spacing:-.02em;color:#fff;text-shadow:0 2px 20px rgba(0,0,0,.7)}
.d21 .hd h2 .o{color:var(--o2);display:block}
.d21 .hd .sub{margin-top:12px;font-size:15px;line-height:1.35;color:#e6dccb;font-weight:600;max-width:22ch;text-shadow:0 1px 12px rgba(0,0,0,.85)}
.d21 .steps{margin-top:13px;display:flex;flex-wrap:wrap;gap:6px}
.d21 .steps span{font-weight:700;font-size:11px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));border-radius:7px;padding:4px 9px}
.d21 .btn{position:absolute;left:32px;bottom:78px;font-weight:800;font-size:15px;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));border-radius:12px;padding:13px 18px;box-shadow:0 14px 30px -10px rgba(232,103,42,.85)}
.d21 .lg{position:absolute;left:32px;bottom:30px;display:flex;align-items:center;gap:8px}
.d21 .lg img{width:26px;height:26px;border-radius:7px}
.d21 .lg b{font-weight:800;font-size:15px;color:#fff}.d21 .lg b i{color:var(--o2);font-style:normal}
"""
CSS = CSS0 + EXTRA

SL = [
 dict(n=1, img="s1", pos="50% 56%", w="Подписался —", o="не значит купит.",
      sub="Холодный подписчик остывает без внимания."),
 dict(n=2, img="s2", pos="50% 52%", w="Залил магнит —", o="и замолчал.",
      sub="Одно сообщение и тишина. Он остыл."),
 dict(n=3, img="s3", pos="50% 50%", w="Подписка —", o="не финиш. Старт.",
      sub="Путь к «да» только начинается."),
 dict(n=4, img="s4", pos="50% 55%", w="Грей доверие.", o="Постепенно.",
      sub="Не продавай в лоб — прогревай."),
 dict(n=5, img="s5", pos="50% 58%", w="Четыре шага", o="до «да».",
      steps=["Знакомство", "Польза", "Доказательство", "Предложение"]),
 dict(n=6, img="s6", pos="50% 54%", w="Тишина и спам —", o="убивают.",
      sub="Ровное тепло греет. Вспышка — отпугивает."),
 dict(n=7, img="s7", pos="50% 44%", w="Claude соберёт", o="прогрев до заявки.",
      sub="Серия постов — от подписки до «да»."),
 dict(n=8, img="s8", pos="50% 50%", w="Забери", o="план прогрева.",
      sub="Готовая серия из 4 шагов — в тетради дня."),
]

def slide(d):
    src = img_src(d["img"])
    bg = f'<div class="bg" style="background-image:url({src});background-position:{d["pos"]}"></div>'
    sub = f'<div class="sub">{d["sub"]}</div>' if d.get("sub") else ''
    steps = ('<div class="steps">' + "".join(f'<span>{s}</span>' for s in d["steps"]) + '</div>') if d.get("steps") else ''
    lg = f'<div class="lg"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div>'
    return (f'<div class="slide d21">{bg}<div class="scrim"></div>'
            f'<div class="top"><span class="eb">AlovLab · прогрев</span>'
            f'<span class="pg">{d["n"]}&nbsp;<b>/ 8</b></span></div>'
            f'<div class="hd"><h2>{d["w"]} <span class="o">{d["o"]}</span></h2>{sub}{steps}</div>'
            f'{lg}</div>')

HTML = (f'<meta charset="utf-8"><style>{CSS}\n.grid{{display:flex;flex-wrap:wrap;gap:0}}</style>'
        f'<div class="grid">{"".join(slide(d) for d in SL)}</div>')
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SL))
