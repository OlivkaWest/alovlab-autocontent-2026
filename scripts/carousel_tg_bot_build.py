# -*- coding: utf-8 -*-
"""AlovLab · карусель «Собрал Telegram-бота, а кодить не умею» (DARK, 6 слайдов, 4:5).
Серия «без кода». Единая нумерация N/6, настоящий знак, финал ведёт в Telegram (TELEGRAM-FUNNEL-CTA).
Manrope (cyr/lat раздельно, стрелки DejaVu; вес только 400/500/700/800). Запуск: python3 scripts/carousel_tg_bot_build.py"""
import pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "exports" / "carousels" / "tg-bot"; OUT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1350
BG0, BG1 = (13, 11, 7), (26, 19, 11)
INK, MUT = (245, 240, 232), (176, 165, 150)
O, O2 = (232, 103, 42), (255, 138, 61)
MARK = Image.open(ROOT / "assets/img/logo-mark.png").convert("RGBA")

def mf(sub, wt, px): return ImageFont.truetype(f"/tmp/manrope-{sub}-{wt}.ttf", px)
DJ = lambda px: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", px)
def is_cyr(ch): return 0x0400 <= ord(ch) <= 0x04FF
ARROWS = set("→←↑↓✓•—👆")
def font_for(ch, wt, px):
    if ch in ARROWS: return DJ(px)
    return mf("cyrillic" if is_cyr(ch) else "latin", wt, px)
def measure(s, wt, px): return sum(font_for(c, wt, px).getlength(c) for c in s)
def draw_run(d, xy, s, wt, px, fill):
    x, y = xy
    for ch in s:
        f = font_for(ch, wt, px); d.text((x, y), ch, font=f, fill=fill); x += f.getlength(ch)
    return x
def wrap(s, wt, px, maxw):
    out, cur = [], ""
    for w in s.split(" "):
        t = (cur + " " + w).strip()
        if measure(t, wt, px) <= maxw: cur = t
        else:
            if cur: out.append(cur)
            cur = w
    if cur: out.append(cur)
    return out
def draw_wrapped(d, x, y, s, wt, px, fill, maxw, lh=1.16):
    for ln in wrap(s, wt, px, maxw):
        draw_run(d, (x, y), ln, wt, px, fill); y += int(px * lh)
    return y

def base():
    im = Image.new("RGB", (W, H), BG0); px = im.load()
    for yy in range(H):
        t = yy / H; col = tuple(int(BG0[i] + (BG1[i]-BG0[i]) * t) for i in range(3))
        for xx in range(W): px[xx, yy] = col
    glow = Image.new("L", (W, H), 0); ImageDraw.Draw(glow).ellipse([W-620, -360, W+260, 520], fill=90)
    glow = glow.filter(ImageFilter.GaussianBlur(150))
    im = Image.composite(Image.new("RGB", (W, H), O2), im, glow.point(lambda v: int(v*0.5)))
    return im

def chip_label(d, text):
    px = 22; pad = 16; tw = measure(text, 800, px); x, y = 70, 70; wb = tw+pad*2; hb = 44
    d.rounded_rectangle([x, y, x+wb, y+hb], radius=hb//2, outline=O2, width=2)
    draw_run(d, (x+pad, y+hb/2-px/2-2), text, 800, px, O2)
def chip_num(d, i):
    t = f"{i}/6"; px = 26; f = DJ(px); tw = f.getlength(t); pad = 15; pw = tw+pad*2; ph = 48
    x = W-pw-70; y = 70
    d.rounded_rectangle([x, y, x+pw, y+ph], radius=ph//2, fill=(12,9,6), outline=O, width=2)
    d.text((x+pad, y+ph/2-px/2-4), t, font=f, fill=O2)
def footer(im, d):
    mh = 44; mk = MARK.resize((mh, mh), Image.LANCZOS); px = 30
    w1 = measure("Alov", 800, px); w2 = measure("Lab", 800, px); gap = 11
    tot = mh+gap+w1+w2; x0 = (W-tot)/2; cy = H-70
    d.line([(150, cy), (x0-26, cy)], fill=(70,60,48), width=2)
    d.line([(x0+tot+26, cy), (W-150, cy)], fill=(70,60,48), width=2)
    im.paste(mk, (int(x0), int(cy-mh/2)), mk); tx = x0+mh+gap
    draw_run(d, (tx, cy-px/2-3), "Alov", 800, px, INK); draw_run(d, (tx+w1, cy-px/2-3), "Lab", 800, px, O2)

def phone_chat(im, d, x, y, w, h):
    d.rounded_rectangle([x, y, x+w, y+h], radius=34, fill=(20,16,10), outline=(60,48,34), width=2)
    # header
    d.rounded_rectangle([x+16, y+16, x+w-16, y+70], radius=14, fill=(28,22,14))
    d.ellipse([x+30, y+28, x+62, y+60], fill=O)
    draw_run(d, (x+74, y+32), "AlovLab bot", 800, 22, INK)
    # user bubble (right)
    d.rounded_rectangle([x+w-260, y+96, x+w-24, y+150], radius=16, fill=(52,42,30))
    draw_run(d, (x+w-238, y+110), "/start", 700, 24, INK)
    # bot bubble (left)
    d.rounded_rectangle([x+24, y+166, x+w-120, y+240], radius=16, fill=(30,24,16))
    draw_run(d, (x+44, y+182), "Привет! Забери гайд", 500, 22, INK)
    draw_run(d, (x+44, y+210), "или оставь заявку.", 500, 22, INK)
    # buttons
    d.rounded_rectangle([x+24, y+258, x+(w//2)-6, y+312], radius=14, fill=O)
    draw_run(d, (x+52, y+272), "Забрать гайд", 800, 21, (22,14,7))
    d.rounded_rectangle([x+(w//2)+6, y+258, x+w-24, y+312], radius=14, outline=O2, width=2)
    draw_run(d, (x+(w//2)+34, y+272), "Оставить заявку", 800, 19, O2)

def save(im, i): im.convert("RGB").save(OUT / f"slide-{i:02d}.png"); print("ok", i)

# 1 COVER
im = base(); d = ImageDraw.Draw(im, "RGBA")
chip_label(d, "ОБЛОЖКА"); chip_num(d, 1)
phone_chat(im, d, 300, 300, 480, 470)
y = 830
draw_run(d, (70, y), "СОБРАЛ", 800, 96, INK); y += 100
draw_run(d, (70, y), "TELEGRAM-БОТА.", 800, 76, INK); y += 100
draw_run(d, (70, y), "КОДИТЬ НЕ УМЕЮ.", 800, 86, O2); y += 112
draw_run(d, (70, y), "Claude написал. Я запустил за вечер.", 500, 33, MUT)
footer(im, d); save(im, 1)

# 2 ПРОВОКАЦИЯ
im = base(); d = ImageDraw.Draw(im, "RGBA")
chip_label(d, "ПРОВОКАЦИЯ"); chip_num(d, 2)
y = 190
draw_run(d, (70, y), "БОТ — ЭТО НЕ", 800, 74, INK); y += 80
draw_run(d, (70, y), "ПРОГРАММИРОВАНИЕ.", 800, 58, O2); y += 118
y = draw_wrapped(d, 70, y, "Это про то, какую рутину он с тебя снимает. Раньше: искать разработчика, ждать, платить. Сегодня: описал словами, Claude написал код.", 500, 37, INK, 940, 1.32)
y += 26
cw = (940-30)//2
for idx, (lbl, txt, col) in enumerate([("РАНЬШЕ", "разработчик · ожидание · счёт", (150,120,95)), ("СЕЙЧАС", "описал → готовый код бота", O2)]):
    cx = 70+idx*(cw+30)
    d.rounded_rectangle([cx, y, cx+cw, y+150], radius=16, fill=(22,17,11), outline=(60,48,34), width=2)
    draw_run(d, (cx+22, y+22), lbl, 800, 20, col)
    draw_wrapped(d, cx+22, y+58, txt, 700, 27, INK, cw-44, 1.2)
y += 190
draw_run(d, (70, y), "Твоя работа — придумать, что бот должен делать.", 500, 31, MUT)
footer(im, d); save(im, 2)

# 3 МЕТОД
im = base(); d = ImageDraw.Draw(im, "RGBA")
chip_label(d, "МЕТОД"); chip_num(d, 3)
y = 190
draw_run(d, (70, y), "4 ШАГА ДО", 800, 84, INK); y += 90
draw_run(d, (70, y), "ЖИВОГО БОТА", 800, 84, O2); y += 130
steps = [("1", "Опиши", "что бот делает: отвечает, выдаёт гайд, собирает заявки"),
         ("2", "Получи код", "Claude пишет готового бота на Python"),
         ("3", "Возьми токен", "у @BotFather в Telegram, минута, бесплатно"),
         ("4", "Запусти", "вставил токен, включил — бот отвечает")]
for n, t, sd in steps:
    d.rounded_rectangle([70, y, 1010, y+150], radius=16, fill=(20,16,10), outline=(58,46,32), width=2)
    d.rounded_rectangle([92, y+42, 158, y+108], radius=14, fill=O)
    d.text((112, y+50), n, font=DJ(40), fill=(22,14,7))
    draw_run(d, (190, y+34), t, 800, 36, INK)
    draw_wrapped(d, 190, y+82, sd, 500, 28, MUT, 790, 1.2)
    y += 168
draw_run(d, (70, y+4), "Кода не пишешь. Пишешь, что бот должен уметь.", 500, 31, MUT)
footer(im, d); save(im, 3)

# 4 ПРОМПТ
im = base(); d = ImageDraw.Draw(im, "RGBA")
chip_label(d, "ПРОМПТ"); chip_num(d, 4)
y = 190
draw_run(d, (70, y), "ПРОМПТ, КОТОРЫЙ", 800, 72, INK); y += 80
draw_run(d, (70, y), "СОБИРАЕТ БОТА", 800, 72, O2); y += 118
px0, py0, px1, py1 = 70, y, 1010, y+560
d.rounded_rectangle([px0, py0, px1, py1], radius=20, fill=(9,7,4), outline=(70,45,26), width=2)
d.rounded_rectangle([px0+26, py0+26, px0+250, py0+70], radius=8, fill=O)
draw_run(d, (px0+44, py0+34), "СКОПИРОВАТЬ", 800, 20, (22,14,7))
ptxt = ("Напиши Telegram-бота на Python (python-telegram-bot). По /start приветствие и кнопки "
        "[КНОПКА 1], [КНОПКА 2]. [КНОПКА 1] присылает [ГАЙД/ССЫЛКУ]. [КНОПКА 2] принимает сообщение и отвечает. "
        "Добавь обработку ошибок, токен в отдельную переменную. Дай готовый код одним файлом и инструкцию для новичка.")
draw_wrapped(d, px0+30, py0+96, ptxt, 500, 27, (255,214,178), px1-px0-60, 1.42)
y = py1+26
draw_run(d, (70, y), "Меняешь только слова в [СКОБКАХ]. Полный — в Telegram.", 500, 30, MUT)
footer(im, d); save(im, 4)

# 5 ПРИМЕНЕНИЕ
im = base(); d = ImageDraw.Draw(im, "RGBA")
chip_label(d, "ПРИМЕНЕНИЕ"); chip_num(d, 5)
y = 190
draw_run(d, (70, y), "ЧТО ПОРУЧИТЬ", 800, 80, INK); y += 86
draw_run(d, (70, y), "БОТУ", 800, 80, O2); y += 128
rows = [("Лид-магнит", "сам выдаёт гайд и промпт новым подписчикам"),
        ("Приём заявок", "собирает имя и контакт, шлёт тебе в личку"),
        ("Автоответ", "отвечает на частые вопросы, разгружает тебя")]
for t, sd in rows:
    d.rounded_rectangle([70, y, 1010, y+118], radius=14, fill=(20,16,10), outline=(58,46,32), width=2)
    d.rounded_rectangle([70, y, 76, y+118], radius=0, fill=O)
    draw_run(d, (104, y+22), t, 800, 32, INK)
    draw_wrapped(d, 104, y+64, sd, 500, 28, MUT, 860, 1.2)
    y += 136
y += 6
d.rounded_rectangle([70, y, 1010, y+150], radius=16, fill=(30,21,12), outline=(80,54,30), width=2)
draw_run(d, (96, y+22), "ЧЕСТНО", 800, 22, O2)
draw_wrapped(d, 96, y+58, "Чтобы бот работал всегда — размести его на хостинге (бесплатный способ в гайде). Токен не показывай, чужие данные без спроса не собирай.", 500, 27, INK, 860, 1.3)
footer(im, d); save(im, 5)

# 6 ФИНАЛ
im = base(); d = ImageDraw.Draw(im, "RGBA")
chip_label(d, "ФИНАЛ"); chip_num(d, 6)
y = 235
draw_run(d, (70, y), "НЕ ЗАКАЗЫВАЙ", 800, 82, INK); y += 90
draw_run(d, (70, y), "БОТА.", 800, 82, INK); y += 104
draw_run(d, (70, y), "СОБЕРИ САМ", 800, 90, O2); y += 98
draw_run(d, (70, y), "ЗА ВЕЧЕР.", 800, 90, O2); y += 126
y = draw_wrapped(d, 70, y, "Сохрани. Описал задачу, Claude написал код, подключил токен, запустил. Первый бот — сегодня.", 500, 35, INK, 940, 1.32)
y += 24
d.rounded_rectangle([70, y, 1010, y+104], radius=16, fill=O)
draw_run(d, (100, y+22), "ГАЙД + ПРОМПТ БЕСПЛАТНО → В TELEGRAM", 800, 28, (22,14,7))
draw_run(d, (100, y+62), "@AlovLab · ссылка в шапке профиля", 700, 24, (60,30,10))
y += 126
draw_run(d, (70, y), "Бот и автоматизация под бизнес → бриф @alovlab", 500, 28, MUT)
footer(im, d); save(im, 6)
print("done ->", OUT)
