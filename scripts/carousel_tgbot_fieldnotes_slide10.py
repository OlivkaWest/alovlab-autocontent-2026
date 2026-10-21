# -*- coding: utf-8 -*-
"""AlovLab · слайд 10 «Bot Field Notes» — финальный экшен-CTA в курс.
Визуально повторяет редизайн: тёмный фон, тонкие рамки, моно-капшены (DejaVuSansMono),
крупный заголовок Manrope 800, оранжевый акцент. Реальные цифры из CLAUDE.md (ПРО 99990→49990 = 50% ровно).
Обновляет нумерацию всех 10 слайдов RU+EN на N/10.
Запуск: python3 scripts/carousel_tgbot_fieldnotes_slide10.py
"""
import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "exports/carousels/tg-bot-fieldnotes"
MARK = Image.open(ROOT / "assets/img/logo-mark.png").convert("RGBA")
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def manrope(sub, wt, px): return ImageFont.truetype(f"/tmp/manrope-{sub}-{wt}.ttf", px)
def is_cyr(ch): return 0x0400 <= ord(ch) <= 0x04FF
def mfont(ch, wt, px): return manrope("cyrillic" if is_cyr(ch) else "latin", wt, px)
def mono(px, bold=False): return ImageFont.truetype(MONO_B if bold else MONO, px)

W, H = 1080, 1350
BG = (18, 20, 20)
GREY = (154, 156, 150)
WHITE = (240, 236, 228)
ORANGE = (255, 106, 61)
LIME = (214, 234, 122)
LINE = (60, 62, 60)
INK = (18, 16, 14)

def draw_mrun(d, xy, s, wt, px, fill):
    x, y = xy
    for ch in s:
        f = mfont(ch, wt, px)
        d.text((x, y), ch, font=f, fill=fill)
        x += f.getlength(ch)
    return x

def mwidth(d, s, wt, px):
    return sum(mfont(ch, wt, px).getlength(ch) for ch in s)

def wrap_m(d, s, wt, px, maxw):
    words = s.split(" "); lines = []; cur = ""
    for w in words:
        t = (cur + " " + w).strip()
        if mwidth(d, t, wt, px) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def draw_mwrap(d, x, y, s, wt, px, fill, maxw, lh=1.14):
    for ln in wrap_m(d, s, wt, px, maxw):
        draw_mrun(d, (x, y), ln, wt, px, fill); y += int(px*lh)
    return y

def base():
    im = Image.new("RGB", (W, H), BG)
    return im

def header(d, i, n=10):
    draw_mrun(d, (64, 57), "ALOVLAB  /  FIELD NOTES", 500, 15, GREY)
    txt = f"{i:02d} / {n:02d}"
    f = mono(15)
    tw = d.textlength(txt, font=f)
    x1 = 1007; padx = 14; pad_y = 9; th = 15
    x0 = x1 - (tw + padx*2)
    d.rectangle([x0, 50, x1, 50+th+pad_y*2], outline=LINE, width=1)
    d.text((x0+padx, 50+pad_y-1), txt, font=f, fill=GREY)

def footer(im, d):
    mh = 20; mk = MARK.resize((mh, mh), Image.LANCZOS)
    im.paste(mk, (64, int(1310-mh/2)), mk)
    d.text((64+mh+10, 1310-8), "AlovLab", font=mono(15), fill=GREY)

im = base()
d = ImageDraw.Draw(im, "RGBA")
header(d, 10)

# kicker
draw_mrun(d, (64, 128), "ИТОГ / ДЕЙСТВИЕ", 700, 16, ORANGE)

# headline
y = 165
draw_mrun(d, (64, y), "ОДНОГО БОТА", 800, 62, WHITE); y += 68
draw_mrun(d, (64, y), "МАЛО.", 800, 62, WHITE); y += 68
draw_mrun(d, (64, y), "НУЖНА СИСТЕМА.", 800, 62, ORANGE); y += 84

# lead
y = draw_mwrap(d, 64, y, "Бот — один инструмент. На курсе собираешь весь конвейер: тексты, визуал, видео, боты и автоматизация — одной системой.", 500, 27, GREY, 940, 1.3)
y += 28

# course card (lime, like slide 9/5 accent cards)
card_x0, card_y0, card_x1 = 64, y, 1016
pad = 26
d.rounded_rectangle([card_x0, card_y0, card_x1, card_y0+430], radius=22, fill=LIME)

cy = card_y0 + pad
draw_mrun(d, (card_x0+pad, cy), "КУРС", 800, 15, INK)
cy += 30
draw_mrun(d, (card_x0+pad, cy), "«Нейросети и ChatGPT", 800, 34, INK); cy += 40
draw_mrun(d, (card_x0+pad, cy), "для каждого»", 800, 34, INK); cy += 52

draw_mwrap(d, card_x0+pad, cy, "6 видеоуроков · 6 «Земель»: Слова, Изображения, Видео, Звук, Аватары, Знания. Плюс то, что ты только что прошёл — боты и автоматизация конвейера.", 500, 21, INK, card_x1-card_x0-pad*2, 1.3)
cy += 96

d.line([(card_x0+pad, cy), (card_x1-pad, cy)], fill=(20,18,16,140), width=1)
cy += 22

draw_mrun(d, (card_x0+pad, cy), "ТАРИФ ПРО", 800, 15, INK)
cy += 30
# price row: old struck + new big
old_txt = "99 990 ₽"; f_old = mono(22)
d.text((card_x0+pad, cy+6), old_txt, font=f_old, fill=(90,86,70))
ow = d.textlength(old_txt, font=f_old)
d.line([(card_x0+pad, cy+16), (card_x0+pad+ow, cy+16)], fill=(90,86,70), width=2)
new_x = card_x0+pad+ow+18
draw_mrun(d, (new_x, cy-4), "49 990 ₽", 800, 32, INK)
cy += 46

draw_mwrap(d, card_x0+pad, cy, "Всё из Базового + доступ навсегда + сертификат + проверка заданий + личное менторство + приватный клуб.", 500, 18, (60,54,40), card_x1-card_x0-pad*2, 1.3)
cy += 60

# discount chip
chip_txt = "СКИДКА 50% · ДО 30 СЕНТЯБРЯ"
f_chip = mono(16, bold=True)
cw = d.textlength(chip_txt, font=f_chip) + 28
d.rounded_rectangle([card_x0+pad, cy, card_x0+pad+cw, cy+40], radius=20, fill=ORANGE)
d.text((card_x0+pad+14, cy+11), chip_txt, font=f_chip, fill=(20,12,8))

y = card_y0 + 430 + 30

# CTA button (orange, full width, like slide 9 lime CTA style but orange for action)
btn_h = 74
d.rounded_rectangle([64, y, 1016, y+btn_h], radius=16, fill=ORANGE)
draw_mrun(d, (96, y+22), "НАЧАТЬ КУРС", 800, 26, INK)
arrow_f = mono(24, bold=True)
d.text((1016-70, y+22), "→", font=arrow_f, fill=INK)
y += btn_h + 22

draw_mrun(d, (64, y), "Все тарифы и вход — alovlab.ru", 500, 19, GREY)
y += 30
draw_mrun(d, (64, y), "Гарантия возврата 14 дней, если не зайдёт.", 500, 17, (110,108,102))

# divider + micro caption like other slides
d.line([(64, 1178), (1016, 1178)], fill=LINE, width=1)
d.text((64, 1197), "НАВЫК: СИСТЕМА, НЕ ИНСТРУМЕНТ", font=mono(15), fill=GREY)

footer(im, d)
im.convert("RGB").save(OUT / "RU" / "slide-10.png")
print("RU slide 10 saved")
