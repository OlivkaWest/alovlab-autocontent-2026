# -*- coding: utf-8 -*-
"""AlovLab · карусель «За вечер собрал сайт, а кодить не умею» (DARK, 6 слайдов, 4:5).
Единая нумерация N/6, настоящий знак logo-mark.png снизу, фирменный оранжевый акцент.
Manrope (cyrillic/latin сабсеты раздельно, стрелки через DejaVu). Запуск: python3 scripts/carousel_site_vecher_build.py"""
import pathlib, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "exports" / "carousels" / "site-vecher"; OUT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1350
BG0, BG1 = (13, 11, 7), (26, 19, 11)
INK = (245, 240, 232)
MUT = (176, 165, 150)
O   = (232, 103, 42)
O2  = (255, 138, 61)
MARK = Image.open(ROOT / "assets/img/logo-mark.png").convert("RGBA")

def mf(sub, wt, px):
    return ImageFont.truetype(str(pathlib.Path(f"/tmp/manrope-{sub}-{wt}.ttf")), px)
DJ = lambda px: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", px)

def is_cyr(ch): return 0x0400 <= ord(ch) <= 0x04FF
ARROWS = set("→←↑↓✓•—")

def font_for(ch, wt, px):
    if ch in ARROWS: return DJ(px)
    return mf("cyrillic" if is_cyr(ch) else "latin", wt, px)

def measure(s, wt, px):
    w = 0
    for ch in s:
        f = font_for(ch, wt, px)
        w += f.getlength(ch)
    return w

def draw_run(d, xy, s, wt, px, fill):
    x, y = xy
    for ch in s:
        f = font_for(ch, wt, px)
        d.text((x, y), ch, font=f, fill=fill)
        x += f.getlength(ch)
    return x

def wrap(s, wt, px, maxw):
    words = s.split(" "); lines=[]; cur=""
    for w in words:
        t = (cur+" "+w).strip()
        if measure(t, wt, px) <= maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def draw_wrapped(d, x, y, s, wt, px, fill, maxw, lh=1.16, spans=None):
    for ln in wrap(s, wt, px, maxw):
        draw_run(d, (x, y), ln, wt, px, fill)
        y += int(px*lh)
    return y

def base():
    im = Image.new("RGB", (W, H), BG0); px = im.load()
    for yy in range(H):
        t = yy/H
        px_col = tuple(int(BG0[i]+(BG1[i]-BG0[i])*t) for i in range(3))
        for xx in range(W): px[xx, yy] = px_col
    # orange radial glow top-right
    glow = Image.new("L", (W, H), 0); gd = ImageDraw.Draw(glow)
    gd.ellipse([W-620, -360, W+260, 520], fill=90)
    glow = glow.filter(ImageFilter.GaussianBlur(150))
    ov = Image.new("RGB", (W, H), O2)
    im = Image.composite(ov, im, glow.point(lambda v: int(v*0.5)))
    return im

def chip_label(d, text):
    px=22; pad=16; tw=measure(text, 800, px)
    x,y=70,70; wbox=tw+pad*2; hbox=44
    d.rounded_rectangle([x,y,x+wbox,y+hbox], radius=hbox//2, outline=O2, width=2)
    draw_run(d,(x+pad,y+hbox/2-px/2-2),text,800,px,O2)

def chip_num(d, i):
    t=f"{i}/6"; px=26; f=DJ(px); tw=f.getlength(t); pad=15; pw=tw+pad*2; ph=48
    x=W-pw-70; y=70
    d.rounded_rectangle([x,y,x+pw,y+ph], radius=ph//2, fill=(12,9,6), outline=O, width=2)
    d.text((x+pad, y+ph/2-px/2-4), t, font=f, fill=O2)

def footer(im, d):
    # thin flanking lines + real mark + Alov/Lab centered
    mh=44; mk=MARK.resize((mh,mh), Image.LANCZOS)
    wm=800; px=30
    w1=measure("Alov",wm,px); w2=measure("Lab",wm,px); gap=11
    tot=mh+gap+w1+w2; x0=(W-tot)/2; cy=H-70
    # lines
    d.line([(150,cy),(x0-26,cy)], fill=(70,60,48), width=2)
    d.line([(x0+tot+26,cy),(W-150,cy)], fill=(70,60,48), width=2)
    im.paste(mk,(int(x0),int(cy-mh/2)),mk)
    tx=x0+mh+gap
    draw_run(d,(tx,cy-px/2-3),"Alov",wm,px,INK)
    draw_run(d,(tx+w1,cy-px/2-3),"Lab",wm,px,O2)

def headline(d, y, lines):
    # lines: list of (text, color)
    for txt,col in lines:
        draw_run(d,(70,y),txt,800,88,col)
        y+=96
    return y

def browser_card(im, d, x, y, w, h, title, dark=True):
    d.rounded_rectangle([x,y,x+w,y+h], radius=22, fill=(20,16,10), outline=(60,48,34), width=2)
    # top bar dots
    for i,c in enumerate([(232,103,42),(255,180,90),(120,110,90)]):
        d.ellipse([x+22+i*26,y+20,x+38+i*26,y+36], fill=c)
    d.line([(x+18,y+52),(x+w-18,y+52)], fill=(50,40,28), width=2)
    # hero mock
    d.rounded_rectangle([x+30,y+74,x+w-30,y+108], radius=8, fill=(52,42,30))
    d.rounded_rectangle([x+30,y+120,x+w*0.62,y+146], radius=8, fill=(40,32,22))
    d.rounded_rectangle([x+30,y+h-64,x+220,y+h-24], radius=10, fill=O)
    draw_run(d,(x+58,y+h-58),title,800,22,(22,14,7))

def save(im, i):
    im.convert("RGB").save(OUT / f"slide-{i:02d}.png")
    print("ok", i)

# ---------- SLIDE 1 · cover ----------
im=base(); d=ImageDraw.Draw(im,"RGBA")
chip_label(d,"ОБЛОЖКА"); chip_num(d,1)
browser_card(im,d,150,300,780,470,"Оставить заявку")
y=830
draw_run(d,(70,y),"ЗА ВЕЧЕР",800,96,INK); y+=100
draw_run(d,(70,y),"СОБРАЛ САЙТ.",800,96,INK); y+=118
draw_run(d,(70,y),"КОДИТЬ НЕ УМЕЮ.",800,96,O2); y+=120
draw_run(d,(70,y),"Claude собрал. Я объяснил словами.",500,34,MUT)
footer(im,d); save(im,1)

# ---------- SLIDE 2 · провокация ----------
im=base(); d=ImageDraw.Draw(im,"RGBA")
chip_label(d,"ПРОВОКАЦИЯ"); chip_num(d,2)
y=190
draw_run(d,(70,y),"САЙТ — ЭТО",800,84,INK); y+=90
draw_run(d,(70,y),"НЕ ПРО КОД.",800,84,O2); y+=140
y=draw_wrapped(d,70,y,"Это про то, как объяснить задачу. Раньше: студия, месяц, деньги вперёд. Сегодня: вечер и нейросеть, которая пишет код за тебя.",500,38,INK,940,1.32)
y+=30
# two cards было/стало
cw=(940-30)//2
for idx,(lbl,txt,col) in enumerate([("РАНЬШЕ","студия · месяц · деньги вперёд",(150,120,95)),("СЕЙЧАС","описал → готовая страница",O2)]):
    cx=70+idx*(cw+30)
    d.rounded_rectangle([cx,y,cx+cw,y+150], radius=16, fill=(22,17,11), outline=(60,48,34), width=2)
    draw_run(d,(cx+22,y+22),lbl,800,20,col)
    draw_wrapped(d,cx+22,y+58,txt,700,28,INK,cw-44,1.2)
y+=190
draw_run(d,(70,y),"Твоя работа — сказать, что должно получиться.",500,32,MUT)
footer(im,d); save(im,2)

# ---------- SLIDE 3 · метод ----------
im=base(); d=ImageDraw.Draw(im,"RGBA")
chip_label(d,"МЕТОД"); chip_num(d,3)
y=190
draw_run(d,(70,y),"4 ШАГА ДО",800,84,INK); y+=90
draw_run(d,(70,y),"ЖИВОГО САЙТА",800,84,O2); y+=130
steps=[("1","Опиши","кто ты, что продаёшь, какие блоки нужны"),
       ("2","Получи","Claude собирает готовую HTML-страницу"),
       ("3","Правь словами","«кнопку крупнее», «замени фото», «добавь отзывы»"),
       ("4","Опубликуй","один файл на бесплатный хостинг → ссылка")]
for n,t,sd in steps:
    d.rounded_rectangle([70,y,1010,y+150], radius=16, fill=(20,16,10), outline=(58,46,32), width=2)
    d.rounded_rectangle([92,y+42,158,y+108], radius=14, fill=O)
    f=DJ(40); d.text((112,y+50),n,font=f,fill=(22,14,7))
    draw_run(d,(190,y+34),t,800,36,INK)
    draw_wrapped(d,190,y+82,sd,500,29,MUT,780,1.2)
    y+=168
draw_run(d,(70,y+4),"Ни строчки кода. Пишешь фразы.",500,32,MUT)
footer(im,d); save(im,3)

# ---------- SLIDE 4 · промпт ----------
im=base(); d=ImageDraw.Draw(im,"RGBA")
chip_label(d,"ПРОМПТ"); chip_num(d,4)
y=190
draw_run(d,(70,y),"ПРОМПТ, КОТОРЫЙ",800,72,INK); y+=80
draw_run(d,(70,y),"СОБИРАЕТ САЙТ",800,72,O2); y+=118
# dark prompt plate
px0,py0,px1,py1=70,y,1010,y+560
d.rounded_rectangle([px0,py0,px1,py1], radius=20, fill=(9,7,4), outline=(70,45,26), width=2)
d.rounded_rectangle([px0+26,py0+26,px0+250,py0+70], radius=8, fill=O)
draw_run(d,(px0+44,py0+34),"СКОПИРОВАТЬ",800,20,(22,14,7))
ptxt=("Собери одностраничный лендинг на чистом HTML и CSS в одном файле. "
      "Проект: [ЧТО ПРОДАЁШЬ]. Аудитория: [КТО КЛИЕНТ]. Блоки: экран-оффер с кнопкой, "
      "3 выгоды, как работает в 3 шага, отзывы, вопросы, форма заявки, футер с контактами. "
      "Стиль [ТЁМНЫЙ/СВЕТЛЫЙ], акцент [ЦВЕТ], крупная типографика, адаптив под телефон. "
      "Верни готовый файл, который открывается в браузере.")
draw_wrapped(d,px0+30,py0+96,ptxt,500,27,(255,214,178),px1-px0-60,1.42)
y=py1+26
draw_run(d,(70,y),"Меняешь только слова в [СКОБКАХ]. Полный — в комментариях.",500,30,MUT)
footer(im,d); save(im,4)

# ---------- SLIDE 5 · правки ----------
im=base(); d=ImageDraw.Draw(im,"RGBA")
chip_label(d,"ПРАВКИ"); chip_num(d,5)
y=190
draw_run(d,(70,y),"САЙТ ПРАВИТСЯ",800,80,INK); y+=86
draw_run(d,(70,y),"ФРАЗАМИ",800,80,O2); y+=128
edits=["«Сделай первый экран мощнее: оффер в строку, кнопка крупная.»",
       "«Перепиши выгоды под [АУДИТОРИЮ], проще и конкретнее.»",
       "«Проверь, что на телефоне читается и кнопки удобные.»"]
for e in edits:
    d.rounded_rectangle([70,y,1010,y+120], radius=14, fill=(20,16,10), outline=(58,46,32), width=2)
    d.rounded_rectangle([70,y,76,y+120], radius=0, fill=O)
    draw_wrapped(d,104,y+24,e,700,31,INK,860,1.28)
    y+=138
y+=8
d.rounded_rectangle([70,y,1010,y+150], radius=16, fill=(30,21,12), outline=(80,54,30), width=2)
draw_run(d,(96,y+22),"ЧЕСТНЫЙ КОНТЕНТ",800,22,O2)
draw_wrapped(d,96,y+58,"Тексты — от себя. Отзывы — только реальные. Фото — свои или со стоков. Каркас собирает ИИ, правду кладёшь ты.",500,28,INK,860,1.3)
footer(im,d); save(im,5)

# ---------- SLIDE 6 · финал ----------
im=base(); d=ImageDraw.Draw(im,"RGBA")
chip_label(d,"ФИНАЛ"); chip_num(d,6)
y=230
draw_run(d,(70,y),"НЕ ИЩИ",800,90,INK); y+=98
draw_run(d,(70,y),"«СДЕЛАЙТЕ САЙТ».",800,76,INK); y+=104
draw_run(d,(70,y),"СОБЕРИ САМ",800,90,O2); y+=98
draw_run(d,(70,y),"ЗА ВЕЧЕР.",800,90,O2); y+=128
y=draw_wrapped(d,70,y,"Сохрани. Открыл нейросеть, описал, поправил словами, опубликовал. Первый сайт — сегодня.",500,36,INK,940,1.32)
y+=24
d.rounded_rectangle([70,y,1010,y+96], radius=16, fill=O)
draw_run(d,(100,y+30),"Промпт и гайд — в комментариях под постом",800,30,(22,14,7))
y+=118
draw_run(d,(70,y),"Сайт под бизнес под ключ → бриф @alovlab",500,28,MUT)
footer(im,d); save(im,6)

print("done ->", OUT)
