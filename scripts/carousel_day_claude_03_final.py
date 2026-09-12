# -*- coding: utf-8 -*-
"""AlovLab · День 3 карусель «Собери свой Claude Skill» — ФИНАЛ (5 слайдов).
Обложка = Higgsfield-печать (src-1) в грейде + хук. Контент = графированные текстовые слайды A,C,D,E.
Единый тёплый грейд, нумерация N/5, логотип на обложке. Запуск: python3 scripts/carousel_day_claude_03_final.py"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, glob, os

ROOT="/home/user/alovlab-autocontent-2026"
SRC=ROOT+"/content/carousel-assets/day-claude-03"
OUT=ROOT+"/exports/carousels/day-claude-03"; os.makedirs(OUT,exist_ok=True)
W,H=1080,1350; N=5
MARK=Image.open(ROOT+"/assets/img/logo-mark.png").convert("RGBA")

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
    dr.rounded_rectangle([x,y,x+pw,y+ph],radius=ph//2,fill=(10,8,6,140),outline=(232,103,42,210),width=2)
    dr.text((x+pad-tb[0],y+pad-tb[1]),t,font=num_font,fill=(255,176,102,255))
def sig(c):
    dr=ImageDraw.Draw(c,"RGBA"); mh=50; mk=MARK.resize((mh,mh),Image.LANCZOS)
    w1=mlen(dr,"Alov",38,"800"); w2=mlen(dr,"Lab",38,"800"); gap=15; tot=mh+gap+w1+w2
    x0=(W-tot)/2; cy=H-70; c.paste(mk,(int(x0),int(cy-mh/2)),mk); tx=x0+mh+gap
    mtext(dr,(tx,cy-27),"Alov",38,"800",(244,239,233,255)); mtext(dr,(tx+w1,cy-27),"Lab",38,"800",(255,138,61,255))

def grade(im):
    a=np.asarray(im.convert("RGB").resize((W,H),Image.LANCZOS),dtype=np.float32)/255.0
    floor=np.array([0.085,0.066,0.050]); a=floor+a*(1.0-floor); a=np.clip(a,0,1)
    a=a+(a-0.5)*0.14*(1-np.abs(a-0.5)*2)
    lum=(0.299*a[...,0]+0.587*a[...,1]+0.114*a[...,2])[...,None]
    a=a*np.array([1.05,1.005,0.93])
    hi=np.clip((lum-0.62)/0.38,0,1); a[...,0]+=hi[...,0]*0.05; a[...,2]-=hi[...,0]*0.03; a=np.clip(a,0,1)
    g=(0.299*a[...,0]+0.587*a[...,1]+0.114*a[...,2])[...,None]; a=g+(a-g)*1.08; a=np.clip(a,0,1)
    out=np.asarray(Image.fromarray((a*255).astype(np.uint8),"RGB"),dtype=np.float32)
    out=out+np.random.normal(0,3.0,(H,W,1)).astype(np.float32)
    return Image.fromarray(np.clip(out,0,255).astype(np.uint8),"RGB").convert("RGBA")

def topscrim(c,h0=520,strength=195):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(1-yy/h0)**1.35))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(5,4,3)),(0,0),blk)

def designed(letter):  # already graded PNG in exports
    return Image.open(f"{OUT}/graded-{letter}.png").convert("RGBA")

# ---- SLIDE 1 · cover (src-1 graded + hook) ----
cov=grade(Image.open(f"{SRC}/src-1.png"))
# extra warm pass so the photoreal cover matches the warm designed slides
_a=np.asarray(cov.convert("RGB"),dtype=np.float32)/255.0
_a=_a*np.array([1.07,1.0,0.82]); _a=np.clip(_a,0,1)
_l=(0.299*_a[...,0]+0.587*_a[...,1]+0.114*_a[...,2])[...,None]
_a=_a+ (np.array([0.045,0.02,-0.02]))*(1-_l)   # warm the shadows
cov=Image.fromarray((np.clip(_a,0,1)*255).astype(np.uint8),"RGB").convert("RGBA")
topscrim(cov)
dr=ImageDraw.Draw(cov,"RGBA")
mtext(dr,(70,96),"CLAUDE SKILLS · ЗА 10 МИНУТ",26,"800",(255,176,102,240))
mtext(dr,(70,140),"Научи ИИ делать",62,"800",(245,241,235,255))
mtext(dr,(70,214),"твою работу.",62,"800",(245,241,235,255))
mtext(dr,(70,300),"Одинаково. Каждый раз.",46,"800",(255,138,61,255))
sig(cov); number(cov,1)
cov.convert("RGB").save(f"{OUT}/slide-01.png"); print("slide-01 cover ok")

# ---- SLIDES 2-5 · A, C, D, E ----
order=["A","C","D","E"]
for idx,letter in enumerate(order,2):
    c=designed(letter); number(c,idx)
    c.convert("RGB").save(f"{OUT}/slide-{idx:02d}.png"); print(f"slide-{idx:02d} ({letter}) ok")

# PDF + light jpg + contact
ims=[Image.open(f"{OUT}/slide-{i:02d}.png").convert("RGB") for i in range(1,6)]
ims[0].save(f"{OUT}/day-claude-03-carousel.pdf","PDF",save_all=True,append_images=ims[1:],resolution=150)
print("done ->",OUT)
