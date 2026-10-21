# -*- coding: utf-8 -*-
"""AlovLab · День 6 карусель «ChatGPT против Claude: выбирай под задачу» — сборка из кадров пользователя.
v2 по GLOBAL-CAROUSEL-RULE: усилен информационный слой (принципы, техника+промпт, формула выбора, retention),
3 уровня иерархии, слайд 7 без большого логотипа (payoff «собери стек»). Готовая таблица (5) не тронута.
Все → 4:5 (1080x1350). Нумерация N/7, маленький знак AlovLab снизу.
Запуск: python3 scripts/carousel_day_claude_06_build.py"""
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import glob, os

ROOT="/home/user/alovlab-autocontent-2026"
SRC=ROOT+"/content/carousel-assets/day-claude-06"
OUT=ROOT+"/exports/carousels/day-claude-06"; os.makedirs(OUT,exist_ok=True)
W,H=1080,1350; N=7
MARK=Image.open(ROOT+"/assets/img/logo-mark.png").convert("RGBA")
FS=sorted(glob.glob(f"{SRC}/ChatGPT*.png"))   # порядок по таймстампу = порядок слайдов

_fc={}
def _f(px,wt,scr):
    k=(px,wt,scr)
    if k not in _fc: _fc[k]=ImageFont.truetype(f"/tmp/manrope-{scr}-{wt}.ttf",px)
    return _fc[k]
_dv={}
def _d(px):
    if px not in _dv: _dv[px]=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",px)
    return _dv[px]
def is_cyr(ch): return 0x0400<=ord(ch)<=0x04FF
def pick(ch,px,wt):
    if ch in "→←↑↓✓•▸": return _d(px)
    return _f(px,wt,"cyrillic" if is_cyr(ch) else "latin")
def mtext(dr,xy,t,px,wt,fill):
    x,y=xy
    for ch in t:
        f=pick(ch,px,wt); dr.text((x,y),ch,font=f,fill=fill); x+=dr.textlength(ch,font=f)
    return x
def mlen(dr,t,px,wt): return sum(dr.textlength(ch,font=pick(ch,px,wt)) for ch in t)

num_font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",30)
def number(c,i):
    dr=ImageDraw.Draw(c,"RGBA"); t=f"{i}/{N}"; tb=dr.textbbox((0,0),t,font=num_font)
    tw,th=tb[2]-tb[0],tb[3]-tb[1]; pad=15; pw,ph=tw+pad*2,th+pad*2; x,y=W-pw-32,32
    dr.rounded_rectangle([x,y,x+pw,y+ph],radius=ph//2,fill=(10,8,6,150),outline=(232,103,42,210),width=2)
    dr.text((x+pad-tb[0],y+pad-tb[1]),t,font=num_font,fill=(255,176,102,255))
def sig(c):
    dr=ImageDraw.Draw(c,"RGBA"); mh=44; mk=MARK.resize((mh,mh),Image.LANCZOS)
    w1=mlen(dr,"Alov",32,"800"); w2=mlen(dr,"Lab",32,"800"); gap=12; tot=mh+gap+w1+w2
    x0=(W-tot)/2; cy=H-58; c.paste(mk,(int(x0),int(cy-mh/2)),mk); tx=x0+mh+gap
    mtext(dr,(tx,cy-22),"Alov",32,"800",(244,239,233,255)); mtext(dr,(tx+w1,cy-22),"Lab",32,"800",(255,138,61,255))
def topscrim(c,h0=470,strength=200):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(1-yy/h0)**1.4))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(4,3,2)),(0,0),blk)
def botscrim(c,h0=250,strength=210):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(yy/h0)**1.5))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(4,3,2)),(0,H-h0),blk)
def card(c,x,y,w,lines,fs=25,pad=20,lh=None):
    """тёмная плашка с промптом; lines: список строк. Возвращает нижний y."""
    dr=ImageDraw.Draw(c,"RGBA"); lh=lh or int(fs*1.32)
    hgt=pad*2+lh*len(lines)
    dr.rounded_rectangle([x,y,x+w,y+hgt],radius=18,fill=(9,7,5,232),outline=(232,103,42,180),width=2)
    yy=y+pad
    for t in lines: mtext(dr,(x+pad,yy),t,fs,"500",(238,232,224,255)); yy+=lh
    return y+hgt

def fit(i):  # -> RGBA 1080x1350, cover-crop (кадры близки к 4:5)
    im=Image.open(FS[i]).convert("RGB")
    r=max(W/im.width,H/im.height); nw,nh=int(round(im.width*r)),int(round(im.height*r))
    im2=im.resize((nw,nh),Image.LANCZOS); x=(nw-W)//2; y=(nh-H)//2
    return im2.crop((x,y,x+W,y+H)).convert("RGBA")

def head(c,lines,y=96):
    dr=ImageDraw.Draw(c,"RGBA")
    for (t,px,wt,col) in lines:
        mtext(dr,(70,y),t,px,wt,col); y+=int(px*1.05)+6
    return dr,y

W_=(245,241,235,255); O=(255,138,61,255); EY=(255,176,102,240); FX=(212,204,195,255); GY=(178,170,162,255)

# 1 · ХУК / конфликт
c=fit(0); topscrim(c,560); botscrim(c,230)
dr,y=head(c,[("ДЕНЬ 6 · ВЫБОР ПОД ЗАДАЧУ",26,"800",EY),
             ("ChatGPT",64,"800",W_),
             ("против Claude",64,"800",O)],96)
dr2=ImageDraw.Draw(c,"RGBA")
mtext(dr2,(70,H-168),"Спорить, кто лучше,",34,"800",W_)
mtext(dr2,(70,H-126),"бессмысленно. Разница в другом",34,"800",O)
mtext(dr2,(70,H-80),"листай  →",28,"700",EY)
number(c,1); c.convert("RGB").save(f"{OUT}/slide-01.png"); print("1 ok")

# 2 · ломаем мнение + принцип
c=fit(1); topscrim(c,540)
dr,y=head(c,[("ГЛАВНЫЙ ПРИНЦИП",24,"800",EY),
             ("Модель выбирают",50,"800",W_),
             ("не по рейтингу.",50,"800",O)],96)
mtext(dr,(70,y+8),"Сначала смотри на ТИП задачи,",31,"700",W_)
mtext(dr,(70,y+48),"а не на то, что «сейчас в топе».",31,"500",FX)
mtext(dr,(70,y+104),"А типов работы всего пять  →",29,"700",EY)
sig(c); number(c,2); c.convert("RGB").save(f"{OUT}/slide-02.png"); print("2 ok")

# 3 · Claude + техника + короткий промпт
c=fit(2); topscrim(c,430); botscrim(c,470,205)
dr,y=head(c,[("ТЕКСТ · ДОКУМЕНТЫ · КОД",24,"800",EY),
             ("Это берёт Claude",48,"800",W_)],96)
mtext(dr,(70,y+4),"Приём: перед большим файлом сначала",28,"700",W_)
mtext(dr,(70,y+40),"попроси карту, потом вопросы по разделам.",28,"500",FX)
card(c,70,H-360,W-140,[
  "Промпт:",
  "Сначала построй карту документа:",
  "раздел → мысль → цифры → риск.",
  "Пока ничего не анализируй.",
],fs=25)
dr3=ImageDraw.Draw(c,"RGBA"); mtext(dr3,(70,H-150),"Так он не поплывёт на 40 страницах  →",28,"700",EY)
sig(c); number(c,3); c.convert("RGB").save(f"{OUT}/slide-03.png"); print("3 ok")

# 4 · ChatGPT + принцип-маршрут
c=fit(3); topscrim(c,470)
dr,y=head(c,[("КАРТИНКИ · ГОЛОС · ПОИСК",24,"800",EY),
             ("Это берёт",48,"800",W_),
             ("ChatGPT",48,"800",O)],96)
mtext(dr,(70,y+8),"Бери его, когда задача прыгает",29,"700",W_)
mtext(dr,(70,y+46),"между форматами:",29,"500",FX)
mtext(dr,(70,y+92),"нашёл → проверил → показал",27,"700",EY)
mtext(dr,(70,y+126),"картинкой → обсудил голосом.",27,"700",EY)
sig(c); number(c,4); c.convert("RGB").save(f"{OUT}/slide-04.png"); print("4 ok")

# 5 · SAVE-таблица (готовая) — метка «сохрани» + номер
c=fit(4)
tp=Image.new("L",(1,150),0)
for yy in range(150): tp.putpixel((0,yy),int(150*(1-yy/150)**1.5))
blk=Image.new("RGBA",(W,150),(0,0,0,0)); blk.putalpha(tp.resize((W,150)))
c.paste(Image.new("RGB",(W,150),(4,3,2)),(0,0),blk)
dr=ImageDraw.Draw(c,"RGBA"); mtext(dr,(70,44),"↓  СОХРАНИ ЭТУ КАРТУ",26,"800",EY)
number(c,5); c.convert("RGB").save(f"{OUT}/slide-05.png"); print("5 ok")

# 6 · правило задачи + формула + указатель на полный промпт
c=fit(5); topscrim(c,470); botscrim(c,300,205)
dr,y=head(c,[("МЕТОД ВЫБОРА",24,"800",EY),
             ("Правило задачи",50,"800",W_)],96)
mtext(dr,(70,y+8),"Гоняй любую задачу по формуле:",29,"500",FX)
# формула карточкой
card(c,70,y+58,W-140,[
  "ЗАДАЧА  →  ТИП РАБОТЫ",
  "→  НУЖНЫЕ ВОЗМОЖНОСТИ  →  МОДЕЛЬ",
],fs=27)
dr6=ImageDraw.Draw(c,"RGBA")
mtext(dr6,(70,H-172),"Полный промпт, который сам разложит",29,"700",W_)
mtext(dr6,(70,H-134),"задачу на стек — в комментах  ↓",29,"700",O)
sig(c); number(c,6); c.convert("RGB").save(f"{OUT}/slide-06.png"); print("6 ok")

# 7 · payoff (БЕЗ большого логотипа) — затемняем вшитый лого, отдаём место пользе
c=fit(6)
c=ImageEnhance.Brightness(c.convert("RGB")).enhance(0.40).convert("RGBA")
# радиальное затемнение центра (где вшитый лого)
vg=Image.new("L",(W,H),0); vgd=ImageDraw.Draw(vg)
vgd.ellipse([W*0.12,H*0.10,W*0.88,H*0.62],fill=150)
vg=vg.resize((W//4,H//4)).resize((W,H))  # мягкое размытие
ov=Image.new("RGBA",(W,H),(0,0,0,0)); ov.putalpha(vg); c.paste(Image.new("RGB",(W,H),(4,3,2)),(0,0),ov)
dr=ImageDraw.Draw(c,"RGBA")
mtext(dr,(70,430),"Не выбирай",58,"800",W_)
mtext(dr,(70,500),"одну нейросеть.",58,"800",W_)
mtext(dr,(70,588),"Собери стек.",58,"800",O)
mtext(dr,(70,700),"Карта + промпт выбора —",32,"700",FX)
mtext(dr,(70,742),"в комментариях  ↓",32,"800",EY)
sig(c); number(c,7); c.convert("RGB").save(f"{OUT}/slide-07.png"); print("7 ok")

# PDF + превью-грид
ims=[Image.open(f"{OUT}/slide-{i:02d}.png").convert("RGB") for i in range(1,8)]
ims[0].save(f"{OUT}/day-claude-06-carousel.pdf","PDF",save_all=True,append_images=ims[1:],resolution=150)
cols=4; rows=2; tw,th=320,400; gap=14; bg=(245,240,232)
grid=Image.new("RGB",(cols*tw+(cols+1)*gap, rows*th+(rows+1)*gap),bg)
for i,im in enumerate(ims):
    r,cc=divmod(i,cols); grid.paste(im.resize((tw,th),Image.LANCZOS),(gap+cc*(tw+gap),gap+r*(th+gap)))
grid.save(f"{OUT}/preview.jpg","JPEG",quality=88)
print("done")
