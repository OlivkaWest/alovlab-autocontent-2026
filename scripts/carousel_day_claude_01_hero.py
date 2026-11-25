from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, os, glob

SRC = "/home/user/alovlab-autocontent-2026/content/carousel-assets/day-claude-01"
OUT = "/home/user/alovlab-autocontent-2026/exports/carousels/day-claude-01"
W, H = 1080, 1350
N = 8
COVER = sorted(glob.glob(os.path.join(SRC, "*.png")))[0]
MARK = Image.open("/home/user/alovlab-autocontent-2026/assets/img/logo-mark.png").convert("RGBA")

def MN(px, wt="500"):  # Manrope mixed
    return px, wt
_fc={}
def _f(px,wt,scr):
    k=(px,wt,scr)
    if k not in _fc: _fc[k]=ImageFont.truetype(f"/tmp/manrope-{scr}-{wt}.ttf",px)
    return _fc[k]
def is_cyr(ch): return 0x0400<=ord(ch)<=0x04FF
_dvcache={}
def _dv(px):
    if px not in _dvcache: _dvcache[px]=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",px)
    return _dvcache[px]
def _pick(ch,px,wt):
    if ch in "→←↑↓✓•▸": return _dv(px)          # glyphs Manrope subset lacks
    return _f(px,wt,"cyrillic" if is_cyr(ch) else "latin")
def mtext(d,xy,t,px,wt,fill):
    x,y=xy
    for ch in t:
        f=_pick(ch,px,wt)
        d.text((x,y),ch,font=f,fill=fill); x+=d.textlength(ch,font=f)
    return x
def mlen(d,t,px,wt):
    return sum(d.textlength(ch,font=_pick(ch,px,wt)) for ch in t)

MONO = lambda px: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", px)

# screen quad in cover-source coords (1122x1402), then scaled to 1080x1350
SX, SY = 1080/1122, 1350/1402
QUAD = [(120,290),(654,258),(686,758),(150,800)]   # TL,TR,BR,BL (source px)
QUAD = [(x*SX, y*SY) for x,y in QUAD]

def find_coeffs(target, source):
    m=[]
    for (tx,ty),(sx,sy) in zip(target,source):
        m.append([tx,ty,1,0,0,0,-sx*tx,-sx*ty])
        m.append([0,0,0,tx,ty,1,-sy*tx,-sy*ty])
    A=np.array(m,dtype=float); B=np.array(source).reshape(8)
    return np.linalg.solve(A,B)

def warp_onto(base, panel):
    pw,ph=panel.size
    coeffs=find_coeffs(QUAD,[(0,0),(pw,0),(pw,ph),(0,ph)])
    warped=panel.transform((W,H),Image.PERSPECTIVE,coeffs,Image.BICUBIC)
    # soft screen bloom from bright content
    glow=warped.split()[3].point(lambda a:a).filter(ImageFilter.GaussianBlur(9))
    bloom=Image.new("RGBA",(W,H),(255,175,110,0)); bloom.putalpha(glow.point(lambda a:int(a*0.28)))
    base=Image.alpha_composite(base, bloom)
    return Image.alpha_composite(base, warped)

def panel_terminal(title_cmd, lines, big=True):
    pw,ph=820,780
    p=Image.new("RGBA",(pw,ph),(0,0,0,0))
    d=ImageDraw.Draw(p)
    # screen body (emissive near-black with faint cool tint)
    d.rounded_rectangle([0,0,pw,ph],radius=6,fill=(9,10,10,255))
    # title bar
    d.rectangle([0,0,pw,70],fill=(26,24,22,255))
    for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
        d.ellipse([34+i*34,26,54+i*34,46],fill=c)
    tf=MONO(24); d.text((pw/2-90,24),"claude-code — zsh",font=tf,fill=(150,146,140))
    d.line([0,70,pw,70],fill=(40,38,35),width=2)
    # command line
    y=104; pad=44
    cf=MONO(30)
    d.text((pad,y),"$",font=cf,fill=(120,220,140))
    mtext(d,(pad+34,y-2),title_cmd,31,"700",(238,232,224,255))
    y+=78
    lf_px=34 if big else 30
    for i,ln in enumerate(lines,1):
        mtext(d,(pad,y),str(i),lf_px,"800",(255,150,60,255))
        mtext(d,(pad+44,y),ln,lf_px,"500",(232,226,219,255))
        y+=lf_px+34
    # cursor
    d.rectangle([pad,y+6,pad+20,y+lf_px+2],fill=(255,150,60,255))
    return p

def signature(canvas):
    d=ImageDraw.Draw(canvas,"RGBA"); mh=52; mark=MARK.resize((mh,mh),Image.LANCZOS)
    w1=mlen(d,"Alov",40,"800"); w2=mlen(d,"Lab",40,"800")
    gap=16; total=mh+gap+w1+w2; x0=(W-total)/2; cy=H-74
    canvas.paste(mark,(int(x0),int(cy-mh/2)),mark); tx=x0+mh+gap
    ty=cy-40*0.72/2- (-6)
    mtext(d,(tx,cy-28),"Alov",40,"800",(244,239,233,255))
    mtext(d,(tx+w1,cy-28),"Lab",40,"800",(255,138,61,255))

num_font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",30)
def number(canvas,i):
    d=ImageDraw.Draw(canvas,"RGBA"); txt=f"{i}/{N}"
    tb=d.textbbox((0,0),txt,font=num_font); tw,th=tb[2]-tb[0],tb[3]-tb[1]
    pad=16; pw,ph=tw+pad*2,th+pad*2; x,y=W-pw-34,34
    d.rounded_rectangle([x,y,x+pw,y+ph],radius=ph//2,fill=(10,8,6,150),outline=(232,103,42,220),width=2)
    d.text((x+pad-tb[0],y+pad-tb[1]),txt,font=num_font,fill=(255,176,102,255))
def scrim(canvas,height=170,strength=200):
    g=Image.new("L",(1,height),0)
    for yy in range(height): g.putpixel((0,yy),int(strength*(yy/height)**1.6))
    g=g.resize((W,height)); blk=Image.new("RGBA",(W,height),(0,0,0,0)); blk.putalpha(g)
    canvas.paste(Image.new("RGB",(W,height),(6,5,4)),(0,H-height),blk)

base=Image.open(COVER).convert("RGB").resize((W,H),Image.LANCZOS).convert("RGBA")

# ---- SLIDE 1 ----
panel1=panel_terminal("что ИИ сделает без кода:",[
    "текст → аккуратный документ",
    "порядок в файлах — сам",
    "страница из твоего текста",
    "данные → таблица и вывод",
    "повторяемое → делает всегда",
])
s1=warp_onto(base.copy(),panel1)
d=ImageDraw.Draw(s1,"RGBA")
scrim(s1)
mtext(d,(70,H-150),"Claude Code · без кода",30,"700",(255,176,102,235))
signature(s1); number(s1,1)
s1.convert("RGB").save(os.path.join(OUT,"slide-01.png")); print("slide-01 ok")

# ---- SLIDE 8 (prompt inside display + CTA outside) ----
def panel_prompt(cmd, lines):
    pw,ph=820,780
    p=Image.new("RGBA",(pw,ph),(0,0,0,0)); d=ImageDraw.Draw(p)
    d.rounded_rectangle([0,0,pw,ph],radius=6,fill=(9,10,10,255))
    d.rectangle([0,0,pw,70],fill=(26,24,22,255))
    for i,c in enumerate([(255,95,86),(255,189,46),(39,201,63)]):
        d.ellipse([34+i*34,26,54+i*34,46],fill=c)
    d.text((pw/2-90,24),"claude-code — zsh",font=MONO(24),fill=(150,146,140))
    d.line([0,70,pw,70],fill=(40,38,35),width=2)
    y=104; pad=44
    d.text((pad,y),"$",font=MONO(30),fill=(120,220,140))
    d.text((pad+34,y),cmd,font=MONO(30),fill=(238,232,224))
    y+=70
    for ln in lines:
        if ln=="":
            y+=22; continue
        d.text((pad,y),"›",font=MONO(30),fill=(255,150,60))
        mtext(d,(pad+34,y-2),ln,30,"500",(226,220,213,255))
        y+=48
    d.rectangle([pad,y+4,pad+18,y+34],fill=(255,150,60,255))
    return p

panel8=panel_prompt("claude-code",[
    "Ты — мой помощник. Я не программист.",
    "Задача словами: [что хочу].",
    "Дай короткий план шагами.",
    "Делай по одному шагу и спрашивай",
    "  подтверждение перед правкой файлов.",
])
s8=warp_onto(base.copy(),panel8)
d=ImageDraw.Draw(s8,"RGBA")
box=Image.new("RGBA",(W,300),(0,0,0,0))
gb=Image.new("L",(1,300),0)
for yy in range(300): gb.putpixel((0,yy),int(210*(yy/300)**1.2))
box.putalpha(gb.resize((W,300)))
s8.paste(Image.new("RGB",(W,300),(6,5,4)),(0,H-300),box)
mtext(d,(70,H-250),"Твой первый запрос — забери целиком",34,"700",(255,176,102,235))
mtext(d,(70,H-200),"Чек-лист «первый запуск»",44,"800",(245,241,235,255))
mtext(d,(70,H-142),"— в комментариях под постом ↓",36,"700",(255,138,61,255))
number(s8,8)
s8.convert("RGB").save(os.path.join(OUT,"slide-08.png")); print("slide-08 ok")
