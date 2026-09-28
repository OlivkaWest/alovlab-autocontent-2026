import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path("/home/user/alovlab-autocontent-2026")
OUT = ROOT / "exports/carousels/tg-bot-fieldnotes"
MARK = Image.open(ROOT / "assets/img/logo-mark.png").convert("RGBA")
DVS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DVS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def sans(px, bold=False): return ImageFont.truetype(DVS_B if bold else DVS, px)
def mono(px, bold=False): return ImageFont.truetype(MONO_B if bold else MONO, px)

W, H = 1080, 1350
BG = (18, 20, 20); GREY = (154, 156, 150); WHITE = (240, 236, 228)
ORANGE = (255, 106, 61); LIME = (214, 234, 122); LINE = (60, 62, 60); INK = (18, 16, 14)

def wrap(d, s, f, maxw):
    words = s.split(" "); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t, font=f) <= maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def draw_wrap(d,x,y,s,f,fill,maxw,lh=1.14):
    for ln in wrap(d,s,f,maxw):
        d.text((x,y),ln,font=f,fill=fill); y+=int(f.size*lh)
    return y

def header(d, i, n=10):
    d.text((64,57), "ALOVLAB  /  FIELD NOTES", font=mono(15), fill=GREY)
    txt=f"{i:02d} / {n:02d}"; f=mono(15)
    tw=d.textlength(txt,font=f); x1=1007; padx=14; pad_y=9; th=15
    x0=x1-(tw+padx*2)
    d.rectangle([x0,50,x1,50+th+pad_y*2], outline=LINE, width=1)
    d.text((x0+padx,50+pad_y-1), txt, font=f, fill=GREY)

def footer(im,d):
    mh=20; mk=MARK.resize((mh,mh), Image.LANCZOS)
    im.paste(mk,(64,int(1310-mh/2)),mk)
    d.text((64+mh+10,1310-8), "AlovLab", font=mono(15), fill=GREY)

im = Image.new("RGB",(W,H),BG)
d = ImageDraw.Draw(im,"RGBA")
header(d,10)
d.text((64,128), "ИТОГ / ДЕЙСТВИЕ", font=sans(16,True), fill=ORANGE)

y=163
d.text((64,y), "ОДНОГО БОТА", font=sans(58,True), fill=WHITE); y+=64
d.text((64,y), "МАЛО.", font=sans(58,True), fill=WHITE); y+=64
d.text((64,y), "НУЖНА СИСТЕМА.", font=sans(58,True), fill=ORANGE); y+=80

y = draw_wrap(d,64,y,"Бот — один инструмент. На курсе собираешь весь конвейер: тексты, визуал, видео, боты и автоматизация — одной системой.", sans(24), GREY, 940, 1.32)
y += 26

card_x0, card_y0, card_x1 = 64, y, 1016
pad = 26
d.rounded_rectangle([card_x0,card_y0,card_x1,card_y0+430], radius=22, fill=LIME)
cy = card_y0+pad
d.text((card_x0+pad,cy), "КУРС", font=sans(14,True), fill=INK); cy+=30
d.text((card_x0+pad,cy), "«Нейросети и ChatGPT", font=sans(30,True), fill=INK); cy+=38
d.text((card_x0+pad,cy), "для каждого»", font=sans(30,True), fill=INK); cy+=50
cy = draw_wrap(d,card_x0+pad,cy,"6 видеоуроков · 6 «Земель»: Слова, Изображения, Видео, Звук, Аватары, Знания. Плюс то, что ты только что прошёл — боты и автоматизация конвейера.", sans(19), (60,54,40), card_x1-card_x0-pad*2, 1.32)
cy += 20
d.line([(card_x0+pad,cy),(card_x1-pad,cy)], fill=(20,18,16,140), width=1); cy+=20
d.text((card_x0+pad,cy), "ТАРИФ ПРО", font=sans(14,True), fill=INK); cy+=28
old_txt="99 990 ₽"; f_old=sans(20)
d.text((card_x0+pad,cy+6), old_txt, font=f_old, fill=(90,86,70))
ow=d.textlength(old_txt,font=f_old)
d.line([(card_x0+pad,cy+16),(card_x0+pad+ow,cy+16)], fill=(90,86,70), width=2)
d.text((card_x0+pad+ow+16,cy), "49 990 ₽", font=sans(28,True), fill=INK)
cy += 42
cy = draw_wrap(d,card_x0+pad,cy,"Всё из Базового + доступ навсегда + сертификат + проверка заданий + личное менторство + приватный клуб.", sans(16), (60,54,40), card_x1-card_x0-pad*2, 1.32)
cy += 14
chip_txt="СКИДКА 50% · ДО 30 СЕНТЯБРЯ"; f_chip=mono(15,True)
cw=d.textlength(chip_txt,font=f_chip)+26
d.rounded_rectangle([card_x0+pad,cy,card_x0+pad+cw,cy+38], radius=19, fill=ORANGE)
d.text((card_x0+pad+13,cy+9), chip_txt, font=f_chip, fill=(20,12,8))

y = card_y0+430+28
btn_h=72
d.rounded_rectangle([64,y,1016,y+btn_h], radius=16, fill=ORANGE)
d.text((96,y+21), "НАЧАТЬ КУРС", font=sans(24,True), fill=INK)
d.text((1016-58,y+16), "→", font=sans(30,True), fill=INK)
y += btn_h+20
d.text((64,y), "Все тарифы и вход — alovlab.ru", font=sans(18), fill=GREY); y+=28
d.text((64,y), "Гарантия возврата 14 дней, если не зайдёт.", font=sans(16), fill=(110,108,102))

d.line([(64,1178),(1016,1178)], fill=LINE, width=1)
d.text((64,1197), "НАВЫК: СИСТЕМА, НЕ ИНСТРУМЕНТ", font=mono(15), fill=GREY)
footer(im,d)
im.convert("RGB").save(OUT/"RU"/"slide-10.png")
print("saved RU 10")
