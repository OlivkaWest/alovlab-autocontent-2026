# -*- coding: utf-8 -*-
"""День 18 сборка финала из полных слайдов пользователя (ChatGPT).
7 портретных = ровно 4:5 → ресайз в 1080×1350. Слайд 5 (ландшафт) → паддинг тёмным до 4:5.
Слайды уже с впечённой нумерацией 01–08 и AlovLab-брендингом → второй чип не добавляем."""
from PIL import Image
import pathlib, glob

ROOT = pathlib.Path("/home/user/alovlab-autocontent-2026")
SRC = ROOT / "content/carousel-assets/day-18"
OUT = ROOT / "exports/carousels/day-18"
OUT.mkdir(parents=True, exist_ok=True)

files = sorted(glob.glob(str(SRC / "ChatGPT Image*.png")))  # timestamp sort = порядок 1..8
assert len(files) == 8, f"ожидал 8, нашёл {len(files)}"

TW, TH = 1080, 1350  # 4:5

def fit_4x5(im):
    im = im.convert("RGB")
    r = im.width / im.height
    target = TW / TH  # 0.8
    if abs(r - target) < 0.01:
        return im.resize((TW, TH), Image.LANCZOS)
    # ландшафт/иное → паддинг тёмным фоном картинки до 4:5
    # масштабируем по ширине, центрируем чуть выше середины (заголовок вверху)
    scaled_h = int(TW / r)
    s = im.resize((TW, scaled_h), Image.LANCZOS)
    bg = im.getpixel((4, 4))  # тёмный угол
    canvas = Image.new("RGB", (TW, TH), bg)
    y = int((TH - scaled_h) * 0.42)  # сдвиг вверх: чуть больше воздуха снизу (пол уходит в чёрное)
    canvas.paste(s, (0, y))
    return canvas

for i, f in enumerate(files, 1):
    im = Image.open(f)
    out = fit_4x5(im)
    out.save(OUT / f"slide-{i:02d}.png")
    print(f"slide-{i:02d}  <- {pathlib.Path(f).name}  ({im.size} -> {out.size})")

print("done ->", OUT)
