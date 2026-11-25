# -*- coding: utf-8 -*-
"""AlovLab · доводка редизайна «Bot Field Notes» до публикации.
Добавляет на все 9 слайдов (RU+EN): 1) чип нумерации N/9 (в стиле этого дизайна: тонкая рамка, моно-шрифт,
top-right, зеркально шапке); 2) подпись снизу с настоящим знаком logo-mark.png + AlovLab (моно, светло-серый).
Источники не трогаем — пишем в exports/carousels/tg-bot-fieldnotes/{RU,EN}/NN.png.
Запуск: python3 scripts/carousel_tgbot_fieldnotes_finish.py
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC_RU = ROOT / "content/carousel-assets/tg-bot-fieldnotes/RU-src"
SRC_EN = ROOT / "content/carousel-assets/tg-bot-fieldnotes/EN-src"
OUT = ROOT / "exports/carousels/tg-bot-fieldnotes"
MARK = Image.open(ROOT / "assets/img/logo-mark.png").convert("RGBA")

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
GREY = (154, 156, 150, 255)
LINE = (60, 62, 60, 255)
W, H = 1080, 1350
N = 9

def font(px): return ImageFont.truetype(MONO, px)

def add_chip(draw, i, n=N):
    txt = f"{i:02d} / {n:02d}"
    f = font(15)
    tw = draw.textlength(txt, font=f)
    padx, padх_r = 14, 14
    pad_y = 9
    x1 = 1007  # right content margin (matches cards' right edge)
    th = 15
    x0 = x1 - (tw + padx + padх_r)
    y0, y1 = 50, 50 + th + pad_y*2
    draw.rectangle([x0, y0, x1, y1], outline=LINE, width=1)
    draw.text((x0 + padx, y0 + pad_y - 1), txt, font=f, fill=GREY)

def add_footer(im, draw):
    mh = 20
    mk = MARK.resize((mh, mh), Image.LANCZOS)
    x0 = 64
    cy = 1310
    im.paste(mk, (x0, int(cy - mh/2)), mk)
    f = font(15)
    tx = x0 + mh + 10
    draw.text((tx, int(cy - 15/2) - 1), "AlovLab", font=f, fill=GREY)
    # thin divider above footer for separation from body (only if space allows, purely decorative, skip to avoid clutter)

def process(src_dir, out_dir, lang):
    out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(1, N+1):
        p = src_dir / f"{i:02d}.png"
        im = Image.open(p).convert("RGBA")
        d = ImageDraw.Draw(im, "RGBA")
        add_chip(d, i)
        add_footer(im, d)
        im.convert("RGB").save(out_dir / f"slide-{i:02d}.png")
    print(f"{lang}: {N} slides -> {out_dir}")

process(SRC_RU, OUT / "RU", "RU")
process(SRC_EN, OUT / "EN", "EN")
print("done")
