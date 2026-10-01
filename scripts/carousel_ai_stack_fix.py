from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
SRC="content/carousel-assets/ai-stack"; OUT="exports/carousels/ai-stack"
names=['s01-cover','s02-provocation','s03-map','s04-combo1','s05-combo2','s06-combo3','s07-prompt','s08-final']
W,H=1080,1350
MARK=Image.open("assets/img/logo-mark.png").convert("RGBA")
def F(px,wt): return ImageFont.truetype(f"/tmp/manrope-latin-{wt}.ttf",px)
def dark(arr,x0,y0,x1,y1): return tuple(int(v) for v in arr[y0:y1,x0:x1].reshape(-1,3).mean(0))

def kill6(c,arr):
    col=dark(arr,585,90,665,104)
    ImageDraw.Draw(c,"RGBA").rectangle([575,44,670,88],fill=col+(255,))

def logo(c,arr):
    col=tuple(int((a+b)/2) for a,b in zip(dark(arr,395,1250,420,1300),dark(arr,695,1250,720,1300)))
    mask=Image.new("L",(W,H),0); md=ImageDraw.Draw(mask)
    md.rounded_rectangle([400,1224,702,1318],radius=22,fill=255)
    mask=mask.filter(ImageFilter.GaussianBlur(10))
    c.paste(Image.new("RGBA",(W,H),col+(255,)),(0,0),mask)
    dr=ImageDraw.Draw(c,"RGBA"); mh=46; mk=MARK.resize((mh,mh),Image.LANCZOS)
    wm=F(31,"800"); w1=dr.textlength("Alov",font=wm); w2=dr.textlength("Lab",font=wm); gap=11
    tot=mh+gap+w1+w2; x0=(W-tot)/2; cy=1274
    c.paste(mk,(int(x0),int(cy-mh/2)),mk); tx=x0+mh+gap
    dr.text((tx,cy-20),"Alov",font=wm,fill=(244,239,233,255))
    dr.text((tx+w1,cy-20),"Lab",font=wm,fill=(255,138,61,255))

for i,n in enumerate(names,1):
    im=Image.open(f"{SRC}/{n}.png").convert("RGBA").resize((W,H),Image.LANCZOS)
    arr=np.asarray(im.convert("RGB")).astype(int)
    if i==6: kill6(im,arr)
    logo(im,arr)
    im.convert("RGB").save(f"{OUT}/slide-{i:02d}.png"); print("ok",i)
