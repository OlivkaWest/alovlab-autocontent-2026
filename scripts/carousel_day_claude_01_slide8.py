from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, glob, os

SRC="/home/user/alovlab-autocontent-2026/content/carousel-assets/day-claude-01"
OUT="/home/user/alovlab-autocontent-2026/exports/carousels/day-claude-01"
W,H=1080,1350; N=8
COVER=sorted(glob.glob(os.path.join(SRC,"*.png")))[0]
MARK=Image.open("/home/user/alovlab-autocontent-2026/assets/img/logo-mark.png").convert("RGBA")
SX,SY=1080/1122,1350/1402
QUAD=[(120,290),(654,258),(686,758),(150,800)]
QUAD=[(x*SX,y*SY) for x,y in QUAD]

def _f(px,wt,scr): return ImageFont.truetype(f"/tmp/manrope-{scr}-{wt}.ttf",px)
def is_cyr(ch): return 0x0400<=ord(ch)<=0x04FF
def mtext(d,xy,t,px,wt,fill):
    x,y=xy
    for ch in t:
        f=_f(px,wt,"cyrillic" if is_cyr(ch) else "latin")
        d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)
    return x
def mlen(d,t,px,wt): return sum(d.textlength(ch,font=_f(px,wt,"cyrillic" if is_cyr(ch) else "latin")) for ch in t)

def find_coeffs(target,source):
    m=[]
    for (tx,ty),(sx,sy) in zip(target,source):
        m.append([tx,ty,1,0,0,0,-sx*tx,-sx*ty]); m.append([0,0,0,tx,ty,1,-sy*tx,-sy*ty])
    return np.linalg.solve(np.array(m,float),np.array(source).reshape(8))

def warp(panel):
    pw,ph=panel.size
    # map panel top-portion to the screen; align top edge, keep aspect by width
    coeffs=find_coeffs(QUAD,[(0,0),(pw,0),(pw,ph),(0,ph)])
    return panel.transform((W,H),Image.PERSPECTIVE,coeffs,Image.BICUBIC)

MARK=MARK
def signature(c):
    d=ImageDraw.Draw(c,"RGBA"); mh=52; mk=MARK.resize((mh,mh),Image.LANCZOS)
    w1=mlen(d,"Alov",40,"800"); w2=mlen(d,"Lab",40,"800"); gap=16; tot=mh+gap+w1+w2
    x0=(W-tot)/2; cy=H-74; c.paste(mk,(int(x0),int(cy-mh/2)),mk); tx=x0+mh+gap
    mtext(d,(tx,cy-28),"Alov",40,"800",(244,239,233,255)); mtext(d,(tx+w1,cy-28),"Lab",40,"800",(255,138,61,255))
nf=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",30)
def number(c,i):
    d=ImageDraw.Draw(c,"RGBA"); t=f"{i}/{N}"; tb=d.textbbox((0,0),t,font=nf)
    tw,th=tb[2]-tb[0],tb[3]-tb[1]; pad=16; pw,ph=tw+pad*2,th+pad*2; x,y=W-pw-34,34
    d.rounded_rectangle([x,y,x+pw,y+ph],radius=ph//2,fill=(10,8,6,150),outline=(232,103,42,220),width=2)
    d.text((x+pad-tb[0],y+pad-tb[1]),t,font=nf,fill=(255,176,102,255))

base=Image.open(COVER).convert("RGB").resize((W,H),Image.LANCZOS).convert("RGBA")
term=Image.open("/tmp/term8.png").convert("RGBA")

# flat screen buffer at screen aspect; terminal scaled to full width, pasted at top (no distortion)
SW,SH=1030,984
ts=term.resize((SW,int(term.height*SW/term.width)),Image.LANCZOS)
flat=Image.new("RGBA",(SW,SH),(9,10,11,255))          # the monitor surface (covers baked prompt)
# faint top-down screen sheen so it reads as a lit display
sh=Image.new("L",(1,SH),0)
for yy in range(SH): sh.putpixel((0,yy),int(26*(1-yy/SH)))
sheen=Image.new("RGBA",(SW,SH),(60,54,48,0)); sheen.putalpha(sh.resize((SW,SH)))
flat=Image.alpha_composite(flat,sheen)
flat.paste(ts,(0,0),ts)
coeffs=find_coeffs(QUAD,[(0,0),(SW,0),(SW,SH),(0,SH)])
warped=flat.transform((W,H),Image.PERSPECTIVE,coeffs,Image.BICUBIC)
# emissive bloom from text alpha
a=warped.split()[3].filter(ImageFilter.GaussianBlur(10))
bloom=Image.new("RGBA",(W,H),(255,170,105,0)); bloom.putalpha(a.point(lambda v:int(v*0.30)))
s8=Image.alpha_composite(base.copy(),bloom)
s8=Image.alpha_composite(s8,warped)
signature(s8); number(s8,8)
s8.convert("RGB").save(os.path.join(OUT,"slide-08.png")); print("slide-08 ok", term.size)
