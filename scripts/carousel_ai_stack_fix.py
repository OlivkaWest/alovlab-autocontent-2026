from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
SRC="exports/carousels/ai-stack"
MARK=Image.open("assets/img/logo-mark.png").convert("RGBA")
W,H=1080,1350
def F(px,wt): return ImageFont.truetype(f"/tmp/manrope-latin-{wt}.ttf",px)
numf=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",30)

def local_dark(arr, x0,y0,x1,y1):
    return tuple(int(v) for v in arr[y0:y1,x0:x1].reshape(-1,3).mean(0))

def kill_num6(c, arr):
    # flat fill over baked "6 / 8" ghost, matched local dark
    col = local_dark(arr, 585,90,665,104)  # flat dark just below the ghost line
    d=ImageDraw.Draw(c,"RGBA")
    d.rectangle([575,44,670,88], fill=col+(255,))  # hard fill, surroundings uniform

def replace_logo(c, arr):
    # sample local dark near logo
    bg = local_dark(arr, 395,1250,420,1300)
    bg2= local_dark(arr, 695,1250,720,1300)
    col= tuple(int((a+b)/2) for a,b in zip(bg,bg2))
    # feathered patch over baked logo region x402..700 y1236..1312
    mask=Image.new("L",(W,H),0); md=ImageDraw.Draw(mask)
    md.rounded_rectangle([400,1224,702,1318],radius=22,fill=255)
    mask=mask.filter(ImageFilter.GaussianBlur(10))
    layer=Image.new("RGBA",(W,H),col+(255,))
    c.paste(layer, (0,0), mask)
    # stamp real mark + wordmark centered
    dr=ImageDraw.Draw(c,"RGBA"); mh=46; mk=MARK.resize((mh,mh),Image.LANCZOS)
    wm=F(31,"800"); w1=dr.textlength("Alov",font=wm); w2=dr.textlength("Lab",font=wm); gap=11
    tot=mh+gap+w1+w2; x0=(W-tot)/2; cy=1274
    c.paste(mk,(int(x0),int(cy-mh/2)),mk); tx=x0+mh+gap
    dr.text((tx,cy-20),"Alov",font=wm,fill=(244,239,233,255))
    dr.text((tx+w1,cy-20),"Lab",font=wm,fill=(255,138,61,255))

def numchip(c,i):
    dr=ImageDraw.Draw(c,"RGBA"); t=f"{i}/8"; tb=dr.textbbox((0,0),t,font=numf)
    tw,th=tb[2]-tb[0],tb[3]-tb[1]; pad=15; pw,ph=tw+pad*2,th+pad*2; x,y=W-pw-34,34
    dr.rounded_rectangle([x,y,x+pw,y+ph],radius=ph//2,fill=(10,8,6,210),outline=(232,103,42,240),width=3)
    dr.text((x+pad-tb[0],y+pad-tb[1]),t,font=numf,fill=(255,176,102,255))

TEST=[1,3,6]
import sys
targets = range(1,9) if "--all" in sys.argv else TEST
for i in targets:
    c=Image.open(f"{SRC}/slide-{i:02d}.png").convert("RGBA")
    arr=np.asarray(c.convert("RGB")).astype(int)
    if i==6: kill_num6(c,arr)
    replace_logo(c,arr); numchip(c,i)
    out = f"{SRC}/slide-{i:02d}.png" if "--all" in sys.argv else f"/tmp/t-{i:02d}.png"
    c.convert("RGB").save(out); print("ok",i,out)
