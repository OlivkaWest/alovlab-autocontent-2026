# -*- coding: utf-8 -*-
"""AlovLab · День 17 (20.08) «Рубрики вместо случайностей» — НОВАЯ визуальная система.
Фотореал-кадр на весь слайд + сильная типографика сверху (скрим) + нумерация N/8.
Кадры кладёшь в content/carousel-assets/day-17/<s1..s8>.<ext>; нет файла — тёмный плейсхолдер
с меткой сцены. Заголовки — вектором поверх фото (текст в дизайне, не в фото).
Сборка: python3 scripts/carousel_day17_build.py → node scripts/carousel_shoot.js <html> <outdir>"""
import base64, pathlib
from carousel_showcase_render import CSS as CSS0, LOGO, ROOT

OUTDIR = ROOT / "exports" / "carousels" / "day-17"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-17.html"
ASSET = ROOT / "content" / "carousel-assets" / "day-17"
_EXTS = (".png", ".jpg", ".jpeg", ".webp")

def img_src(name):
    for e in _EXTS:
        p = ASSET / (name + e)
        if p.exists():
            mt = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}[e]
            return f"data:{mt};base64," + base64.b64encode(p.read_bytes()).decode()
    return None

EXTRA = r"""
.d17{position:relative;width:540px;height:675px;overflow:hidden;border-radius:0;background:#0a0806}
.d17 .bg{position:absolute;inset:0;background-size:cover;background-position:center}
.d17 .ph{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;
 background:radial-gradient(120% 90% at 50% 42%,#20140a,#0a0806 72%);color:#6a6157;font-size:12px;font-weight:700;
 letter-spacing:.04em;padding:0 60px;line-height:1.5}
.d17 .scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,5,4,.92) 4%,rgba(6,5,4,.6) 26%,rgba(6,5,4,0) 46%)}
.d17 .top{position:absolute;left:34px;right:30px;top:26px;display:flex;justify-content:space-between;align-items:flex-start}
.d17 .eb{font-weight:800;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--o2)}
.d17 .pg{display:flex;align-items:center;gap:2px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.18);
 border-radius:20px;padding:6px 12px;font-weight:800;font-size:14px;color:#fff}
.d17 .pg b{color:var(--o2)}
.d17 .hd{position:absolute;left:34px;right:34px;top:58px}
.d17 .hd h2{font-weight:800;font-size:41px;line-height:.99;letter-spacing:-.02em;color:#fff;text-shadow:0 2px 18px rgba(0,0,0,.6)}
.d17 .hd h2 .o{color:var(--o2);display:block}
.d17 .hd .sub{margin-top:11px;font-size:15px;line-height:1.35;color:#e6dccb;font-weight:600;max-width:20ch;text-shadow:0 1px 10px rgba(0,0,0,.7)}
.d17 .prm{position:absolute;left:34px;right:34px;bottom:30px;background:rgba(10,8,6,.82);border:1px solid rgba(255,150,80,.4);
 border-left:3px solid var(--o);border-radius:12px;padding:12px 14px;-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
.d17 .prm .tag{display:inline-block;font-weight:800;font-size:8px;letter-spacing:.08em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:3px 8px;border-radius:5px;margin-bottom:8px}
.d17 .prm code{display:block;font-family:'SF Mono',ui-monospace,Menlo,monospace;font-size:10px;line-height:1.45;color:#ffd9b8;white-space:pre-wrap}
.d17 .btn{position:absolute;left:34px;bottom:34px;font-weight:800;font-size:15px;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));border-radius:12px;padding:13px 18px;box-shadow:0 14px 30px -10px rgba(232,103,42,.8)}
.d17 .lg{position:absolute;right:30px;bottom:32px;display:flex;align-items:center;gap:8px}
.d17 .lg img{width:26px;height:26px;border-radius:7px}
.d17 .lg b{font-weight:800;font-size:15px;color:#fff}.d17 .lg b i{color:var(--o2);font-style:normal}
"""
CSS = CSS0 + EXTRA

SL = [
 dict(n=1, img="s1", w="Выгораешь не", o="от работы. От «что постить».", sub="Каждый пост придумываешь заново — и это выматывает.", meta="СЦЕНА 1 · автор ночью, пустой экран, скомканные листы (выгорание)"),
 dict(n=2, img="s2", w="Каждый пост —", o="с нуля.", sub="Стена случайных идей. Ни системы, ни повторяемости.", meta="СЦЕНА 2 · тёмная стена в рваных записках, хаос"),
 dict(n=3, img="s3", w="Нет системы —", o="есть хаос.", sub="Изобретаешь тему каждый день. Как катить камень в гору.", meta="СЦЕНА 3 · Сизиф катит ком из записок вверх"),
 dict(n=4, img="s4", w="Ищешь тему.", o="А надо — рубрику.", sub="Гоняешься за искрой, вместо того чтобы крутить маховик.", meta="СЦЕНА 4 · ловит светлячка сачком vs крутится маховик"),
 dict(n=5, img="s5", w="Четыре опоры.", o="2 : 1 : 1 : 1.", sub="Польза · Смысл · Практика · Приглашение. Первая — вдвойне.", meta="СЦЕНА 5 · четыре колонны держат платформу, первая толще"),
 dict(n=6, img="s6", w="Рубрики,", o="не случайности.", sub="Повторяемые форматы — это конвейер, а не вдохновение.", meta="СЦЕНА 6 · конвейер штампует брендовые плитки со знаком A"),
 dict(n=7, img="s7", w="Claude соберёт", o="твои рубрики.", sub=None,
      meta="СЦЕНА 7 · макро экрана: собирается сетка 4 рубрик",
      prompt="Собери 4 повторяемые рубрики под опоры 2:1:1:1\n(польза·смысл·практика·приглашение) для ниши [ТВОЯ].\nПо каждой: название, формат, о чём. Живо, без штампов."),
 dict(n=8, img="s8", w="Собери", o="сетку рубрик.", sub=None, cta=True, btn="Тетрадь дня → t.me/AlovLab",
      meta="СЦЕНА 8 · тетрадь AlovLab с сеткой рубрик + телефон Telegram"),
]

def slide(d):
    src = img_src(d["img"])
    bg = f'<div class="bg" style="background-image:url({src})"></div>' if src else f'<div class="ph">{d["meta"]}</div>'
    sub = f'<div class="sub">{d["sub"]}</div>' if d.get("sub") else ''
    prm = (f'<div class="prm"><span class="tag">Claude · скопировать</span><code>{d["prompt"]}</code></div>'
           if d.get("prompt") else '')
    btn = f'<div class="btn">{d["btn"]}</div>' if d.get("cta") else ''
    lg = (f'<div class="lg"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div>' if d.get("cta") else '')
    return (f'<div class="slide d17">{bg}<div class="scrim"></div>'
            f'<div class="top"><span class="eb">AlovLab · рубрики вместо случайностей</span>'
            f'<span class="pg">{d["n"]}&nbsp;<b>/ 8</b></span></div>'
            f'<div class="hd"><h2>{d["w"]} <span class="o">{d["o"]}</span></h2>{sub}</div>'
            f'{prm}{btn}{lg}</div>')

HTML = (f'<meta charset="utf-8"><style>{CSS}\n.grid{{display:flex;flex-wrap:wrap;gap:0}}</style>'
        f'<div class="grid">{"".join(slide(d) for d in SL)}</div>')
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SL),
      "| фото:", sum(1 for d in SL if img_src(d["img"])), "/ 8")
