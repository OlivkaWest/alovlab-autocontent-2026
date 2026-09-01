# -*- coding: utf-8 -*-
"""AlovLab · День 6 карусель «ChatGPT против Claude: выбирай под задачу» — сборка из кадров пользователя.
7 слайдов. Чистые сцены (1,2,3,4,6) — впечатываю заголовки; готовые с текстом (5 таблица, 7 лого) — не трогаю (только номер).
Все → 4:5 (1080x1350). Нумерация N/7, знак AlovLab.
Запуск: python3 scripts/carousel_day_claude_06_build.py"""
from PIL import Image, ImageDraw, ImageFont
import glob, os

ROOT="/home/user/alovlab-autocontent-2026"
SRC=ROOT+"/content/carousel-assets/day-claude-06"
OUT=ROOT+"/exports/carousels/day-claude-06"; os.makedirs(OUT,exist_ok=True)
W,H=1080,1350; N=7
MARK=Image.open(ROOT+"/assets/img/logo-mark.png").convert("RGBA")
FS=sorted(glob.glob(f"{SRC}/ChatGPT*.png"))   # order by embedded timestamp = slide order

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
    dr=ImageDraw.Draw(c,"RGBA"); mh=48; mk=MARK.resize((mh,mh),Image.LANCZOS)
    w1=mlen(dr,"Alov",36,"800"); w2=mlen(dr,"Lab",36,"800"); gap=14; tot=mh+gap+w1+w2
    x0=(W-tot)/2; cy=H-66; c.paste(mk,(int(x0),int(cy-mh/2)),mk); tx=x0+mh+gap
    mtext(dr,(tx,cy-25),"Alov",36,"800",(244,239,233,255)); mtext(dr,(tx+w1,cy-25),"Lab",36,"800",(255,138,61,255))
def topscrim(c,h0=470,strength=195):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(1-yy/h0)**1.4))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(4,3,2)),(0,0),blk)
def botscrim(c,h0=210,strength=205):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(yy/h0)**1.5))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(4,3,2)),(0,H-h0),blk)

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

W_=(245,241,235,255); O=(255,138,61,255); EY=(255,176,102,240); FX=(210,202,193,255)

# 1 · обложка — ChatGPT против Claude
c=fit(0); topscrim(c,540); botscrim(c,190)
dr,y=head(c,[("ДЕНЬ 6 · ВЫБОР ПОД ЗАДАЧУ",26,"800",EY),
             ("ChatGPT",64,"800",W_),
             ("против Claude",64,"800",O)],96)
dr2=ImageDraw.Draw(c,"RGBA")
mtext(dr2,(70,H-150),"Спорить бессмысленно.",34,"800",W_)
mtext(dr2,(70,H-108),"Вопрос не в этом.",34,"800",O)
number(c,1); c.convert("RGB").save(f"{OUT}/slide-01.png"); print("1 ok")

# 2 · провокация — два инструмента
c=fit(1); topscrim(c,500)
dr,y=head(c,[("СУТЬ",24,"800",EY),
             ("Это два разных",50,"800",W_),
             ("инструмента.",50,"800",O)],96)
mtext(dr,(70,y+6),"→ вопрос: что ты делаешь сейчас",30,"500",FX)
sig(c); number(c,2); c.convert("RGB").save(f"{OUT}/slide-02.png"); print("2 ok")

# 3 · Claude — текст и код
c=fit(2); topscrim(c,470)
dr,y=head(c,[("КОГДА ВАЖЕН ТЕКСТ И КОД",24,"800",EY),
             ("Это берёт",50,"800",W_),
             ("Claude.",50,"800",O)],96)
mtext(dr,(70,y+6),"→ живой текст, документы, агенты",30,"500",FX)
sig(c); number(c,3); c.convert("RGB").save(f"{OUT}/slide-03.png"); print("3 ok")

# 4 · ChatGPT — весь набор
c=fit(3); topscrim(c,470)
dr,y=head(c,[("КОГДА НУЖЕН ВЕСЬ НАБОР",24,"800",EY),
             ("Это берёт",50,"800",W_),
             ("ChatGPT.",50,"800",O)],96)
mtext(dr,(70,y+6),"→ картинки, голос, свежий поиск",30,"500",FX)
sig(c); number(c,4); c.convert("RGB").save(f"{OUT}/slide-04.png"); print("4 ok")

# 5 · таблица (готовая) — только номер
c=fit(4); number(c,5); c.convert("RGB").save(f"{OUT}/slide-05.png"); print("5 ok")

# 6 · правило задачи
c=fit(5); topscrim(c,470)
dr,y=head(c,[("МЕТОД",24,"800",EY),
             ("Правило",50,"800",W_),
             ("задачи.",50,"800",O)],96)
mtext(dr,(70,y+6),"→ выбирай под тип, а не по привычке",30,"500",FX)
sig(c); number(c,6); c.convert("RGB").save(f"{OUT}/slide-06.png"); print("6 ok")

# 7 · финал (лого вшит) — CTA сверху + номер
c=fit(6)
tp=Image.new("L",(1,320),0)
for yy in range(320): tp.putpixel((0,yy),int(180*(1-yy/320)**1.4))
blk=Image.new("RGBA",(W,320),(0,0,0,0)); blk.putalpha(tp.resize((W,320)))
c.paste(Image.new("RGB",(W,320),(4,3,2)),(0,0),blk)
dr=ImageDraw.Draw(c,"RGBA")
mtext(dr,(70,92),"Сохрани карту.",40,"800",W_)
mtext(dr,(70,142),"Промпты и шпаргалка — в комментах ↓",30,"700",O)
number(c,7); c.convert("RGB").save(f"{OUT}/slide-07.png"); print("7 ok")

# PDF + превью-грид
ims=[Image.open(f"{OUT}/slide-{i:02d}.png").convert("RGB") for i in range(1,8)]
ims[0].save(f"{OUT}/day-claude-06-carousel.pdf","PDF",save_all=True,append_images=ims[1:],resolution=150)
cols=4; rows=2; tw,th=320,400; gap=14; bg=(245,240,232)
grid=Image.new("RGB",(cols*tw+(cols+1)*gap, rows*th+(rows+1)*gap),bg)
for i,im in enumerate(ims):
    r,cc=divmod(i,cols); grid.paste(im.resize((tw,th),Image.LANCZOS),(gap+cc*(tw+gap),gap+r*(th+gap)))
grid.save(f"{OUT}/preview.jpg","JPEG",quality=88)
print("done")
