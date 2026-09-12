# -*- coding: utf-8 -*-
"""AlovLab · День 4 карусель «5 ошибок, из-за которых ИИ отвечает водой» — сборка из кадров пользователя.
7 слайдов. Чистые сцены (1,2,3,4,6) — впечатываю заголовки/фиксы; готовые с текстом (5,7) — не трогаю.
Все → 4:5 (1080x1350): обложка resize, 2:3 — edge-паддинг (текст не режем). Нумерация N/7, логотип.
Запуск: python3 scripts/carousel_day_claude_04_build.py"""
from PIL import Image, ImageDraw, ImageFont
import glob, os

ROOT="/home/user/alovlab-autocontent-2026"
SRC=ROOT+"/content/carousel-assets/day-claude-04"
OUT=ROOT+"/exports/carousels/day-claude-04"; os.makedirs(OUT,exist_ok=True)
W,H=1080,1350; N=7
MARK=Image.open(ROOT+"/assets/img/logo-mark.png").convert("RGBA")
FS=sorted(glob.glob(f"{SRC}/ChatGPT*.png"))   # order by timestamp = slide order

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
def topscrim(c,h0=470,strength=190):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(1-yy/h0)**1.4))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(4,3,2)),(0,0),blk)
def botscrim(c,h0=200,strength=200):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(yy/h0)**1.5))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(4,3,2)),(0,H-h0),blk)

def fit(i):  # -> RGBA 1080x1350, edge-pad if not 4:5
    im=Image.open(FS[i]).convert("RGB")
    if abs(im.width/im.height-0.8)<0.02:
        return im.resize((W,H),Image.LANCZOS).convert("RGBA")
    r=min(W/im.width,H/im.height); nw,nh=int(round(im.width*r)),int(round(im.height*r))
    im2=im.resize((nw,nh),Image.LANCZOS); canvas=Image.new("RGB",(W,H),(8,7,6))
    x=(W-nw)//2; y=(H-nh)//2
    if nw<W:
        left=im2.crop((0,0,1,nh)).resize((max(x,1),nh)); right=im2.crop((nw-1,0,nw,nh)).resize((max(W-x-nw,1),nh))
        canvas.paste(left,(0,y)); canvas.paste(right,(x+nw,y))
    if nh<H:
        top=im2.crop((0,0,nw,1)).resize((nw,max(y,1))); bot=im2.crop((0,nh-1,nw,nh)).resize((nw,max(H-y-nh,1)))
        canvas.paste(top,(x,0)); canvas.paste(bot,(x,y+nh))
    canvas.paste(im2,(x,y)); return canvas.convert("RGBA")

def head(c,lines,y=100):
    dr=ImageDraw.Draw(c,"RGBA")
    for (t,px,wt,col) in lines:
        mtext(dr,(70,y),t,px,wt,col); y+=int(px*1.04)+6
    return dr,y

W_=(245,241,235,255); O=(255,138,61,255); EY=(255,176,102,240); FX=(206,198,190,255)

# 1 · обложка
c=fit(0); topscrim(c,520)
dr,y=head(c,[("CLAUDE · КАК СПРАШИВАТЬ",26,"800",EY),
             ("ИИ отвечает водой?",58,"800",W_),
             ("Дело не в нём.",58,"800",O)],96)
sig(c); number(c,1); c.convert("RGB").save(f"{OUT}/slide-01.png"); print("1 ok")

# 2 · ошибка размытая задача
c=fit(1); topscrim(c)
dr,y=head(c,[("ОШИБКА 1",24,"800",EY),
             ("Размытая задача —",50,"800",W_),
             ("размытый ответ.",50,"800",O)],96)
mtext(dr,(70,y+6),"→ дай роль, цель и формат",30,"500",FX)
sig(c); number(c,2); c.convert("RGB").save(f"{OUT}/slide-02.png"); print("2 ok")

# 3 · ошибка ноль контекста
c=fit(2); topscrim(c)
dr,y=head(c,[("ОШИБКА 2",24,"800",EY),
             ("Ноль контекста —",50,"800",W_),
             ("ИИ додумывает.",50,"800",O)],96)
mtext(dr,(70,y+6),"→ дай факты, примеры, аудиторию",30,"500",FX)
sig(c); number(c,3); c.convert("RGB").save(f"{OUT}/slide-03.png"); print("3 ok")

# 4 · ошибка пять задач (в кадре записки — заголовок сверху)
c=fit(3); topscrim(c,430)
dr,y=head(c,[("ОШИБКА 3",24,"800",EY),
             ("Пять задач —",50,"800",W_),
             ("в один запрос.",50,"800",O)],90)
mtext(dr,(70,y+6),"→ по одной за раз",30,"500",FX)
number(c,4); c.convert("RGB").save(f"{OUT}/slide-04.png"); print("4 ok")

# 5 · 5 ошибок -> 5 фиксов (готовый) — только номер
c=fit(4); number(c,5); c.convert("RGB").save(f"{OUT}/slide-05.png"); print("5 ok")

# 6 · как надо (Claude)
c=fit(5); topscrim(c)
dr,y=head(c,[("КАК НАДО",24,"800",EY),
             ("Спроси точно —",50,"800",W_),
             ("получи чисто.",50,"800",O)],96)
sig(c); number(c,6); c.convert("RGB").save(f"{OUT}/slide-06.png"); print("6 ok")

# 7 · CTA (готовый) — номер + строка воронки сверху
c=fit(6);
tp=Image.new("L",(1,300),0)
for yy in range(300): tp.putpixel((0,yy),int(170*(1-yy/300)**1.4))
blk=Image.new("RGBA",(W,300),(0,0,0,0)); blk.putalpha(tp.resize((W,300)))
c.paste(Image.new("RGB",(W,300),(4,3,2)),(0,0),blk)
dr=ImageDraw.Draw(c,"RGBA")
mtext(dr,(70,96),"Чек-лист «5 ошибок» + промпт",34,"800",W_)
mtext(dr,(70,140),"— в комментариях под постом ↓",30,"700",O)
number(c,7); c.convert("RGB").save(f"{OUT}/slide-07.png"); print("7 ok")

# PDF
ims=[Image.open(f"{OUT}/slide-{i:02d}.png").convert("RGB") for i in range(1,8)]
ims[0].save(f"{OUT}/day-claude-04-carousel.pdf","PDF",save_all=True,append_images=ims[1:],resolution=150)
print("done")
