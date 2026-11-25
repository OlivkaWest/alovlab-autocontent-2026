# -*- coding: utf-8 -*-
"""AlovLab · карусель Дня 3 «Что такое Claude Skill» — сборка из кадров Higgsfield (src-1..8).
Путь A: эстетика печати + смысл несут заголовки. Заголовки/панель SKILL.md/CTA впечатываются.
Кадры 1856x2304 (4:5) -> 1080x1350. Manrope (mixed cyr/lat), стрелки/кавычки — DejaVu fallback.
Запуск: python3 scripts/carousel_day_claude_03_build.py"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import glob, os

ROOT="/home/user/alovlab-autocontent-2026"
SRC=ROOT+"/content/carousel-assets/day-claude-03"
OUT=ROOT+"/exports/carousels/day-claude-03"; os.makedirs(OUT,exist_ok=True)
W,H=1080,1350; N=8
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
    tw,th=tb[2]-tb[0],tb[3]-tb[1]; pad=16; pw,ph=tw+pad*2,th+pad*2; x,y=W-pw-34,34
    dr.rounded_rectangle([x,y,x+pw,y+ph],radius=ph//2,fill=(10,8,6,150),outline=(232,103,42,220),width=2)
    dr.text((x+pad-tb[0],y+pad-tb[1]),t,font=num_font,fill=(255,176,102,255))
def sig(c):
    dr=ImageDraw.Draw(c,"RGBA"); mh=52; mk=MARK.resize((mh,mh),Image.LANCZOS)
    w1=mlen(dr,"Alov",40,"800"); w2=mlen(dr,"Lab",40,"800"); gap=16; tot=mh+gap+w1+w2
    x0=(W-tot)/2; cy=H-72; c.paste(mk,(int(x0),int(cy-mh/2)),mk); tx=x0+mh+gap
    mtext(dr,(tx,cy-28),"Alov",40,"800",(244,239,233,255)); mtext(dr,(tx+w1,cy-28),"Lab",40,"800",(255,138,61,255))
def scrim(c,h0=180,strength=205):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(yy/h0)**1.6))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(6,5,4)),(0,H-h0),blk)
def topscrim(c,h0=430,strength=175):
    g=Image.new("L",(1,h0),0)
    for yy in range(h0): g.putpixel((0,yy),int(strength*(1-yy/h0)**1.4))
    g=g.resize((W,h0)); blk=Image.new("RGBA",(W,h0),(0,0,0,0)); blk.putalpha(g)
    c.paste(Image.new("RGB",(W,h0),(5,4,3)),(0,0),blk)

def base(i):
    return Image.open(f"{SRC}/src-{i}.png").convert("RGB").resize((W,H),Image.LANCZOS).convert("RGBA")

def headline(c, lines, y=100):
    dr=ImageDraw.Draw(c,"RGBA")
    for (t,px,wt,col) in lines:
        mtext(dr,(70,y),t,px,wt,col); y+=int(px*1.02)+6
    return y

# ---- slides ----
def s1():
    c=base(1); topscrim(c)
    headline(c,[("Научи ИИ делать",58,"800",(245,241,235,255)),
                ("одинаково.",58,"800",(245,241,235,255)),
                ("Каждый раз.",72,"800",(255,138,61,255))])
    scrim(c); sig(c); number(c,1); return c
def s2():
    c=base(2); topscrim(c)
    headline(c,[("Объясняешь заново —",52,"800",(245,241,235,255)),
                ("получаешь разное.",52,"800",(255,138,61,255))])
    scrim(c); sig(c); number(c,2); return c
def s3():
    c=base(3); topscrim(c)
    headline(c,[("Скилл — это",56,"800",(245,241,235,255)),
                ("форма для результата.",52,"700",(245,241,235,255))])
    scrim(c); sig(c); number(c,3); return c
def s4():
    c=base(4); topscrim(c,h0=360)
    headline(c,[("Что внутри Skill:",50,"800",(245,241,235,255)),
                ("три части.",50,"800",(255,138,61,255))])
    dr=ImageDraw.Draw(c,"RGBA")
    cx0,cy0,cx1,cy1=70,470,W-70,1120
    dr.rounded_rectangle([cx0,cy0,cx1,cy1],radius=26,fill=(14,11,9,205),outline=(232,103,42,170),width=2)
    dr.rounded_rectangle([cx0+30,cy0+26,cx0+30+mlen(dr,'SKILL.md',26,'800')+26,cy0+70],radius=10,fill=(232,103,42,255))
    mtext(dr,(cx0+43,cy0+34),"SKILL.md",26,"800",(12,9,7,255))
    rows=[("1 · Имя","как называется скилл"),
          ("2 · Когда включать","по каким запросам применять"),
          ("3 · Что делать","пошаговая инструкция")]
    yy=cy0+108
    for a,b in rows:
        mtext(dr,(cx0+40,yy),a,34,"800",(255,176,102,255))
        mtext(dr,(cx0+40,yy+44),b,28,"500",(226,220,213,255)); yy+=150
    scrim(c); sig(c); number(c,4); return c
def s5():
    c=base(5); topscrim(c)
    headline(c,[("Собрал один раз —",54,"800",(245,241,235,255)),
                ("дальше одно слово.",54,"800",(255,138,61,255))])
    scrim(c); sig(c); number(c,5); return c
def s6():
    c=base(6); topscrim(c)
    headline(c,[("Конвейер,",64,"800",(245,241,235,255)),
                ("а не генерация.",56,"800",(255,138,61,255))])
    scrim(c); sig(c); number(c,6); return c
def s7():
    c=base(7); topscrim(c)
    headline(c,[("Claude соберёт",54,"800",(245,241,235,255)),
                ("форму сам.",54,"800",(255,138,61,255))])
    scrim(c); sig(c); number(c,7); return c
def s8():
    c=base(8); topscrim(c)
    headline(c,[("Собери",64,"800",(245,241,235,255)),
                ("свой скилл.",64,"800",(255,138,61,255))])
    dr=ImageDraw.Draw(c,"RGBA")
    scrim(c,h0=250,strength=215)
    mtext(dr,(70,H-176),"Шаблон SKILL.md + промпт",34,"700",(245,241,235,255))
    mtext(dr,(70,H-132),"— в комментариях под постом ↓",30,"700",(255,138,61,255))
    sig(c); number(c,8); return c

builders=[s1,s2,s3,s4,s5,s6,s7,s8]
for i,b in enumerate(builders,1):
    b().convert("RGB").save(f"{OUT}/slide-{i:02d}.png"); print(f"slide-{i:02d} ok")
# PDF
ims=[Image.open(f"{OUT}/slide-{i:02d}.png").convert("RGB") for i in range(1,9)]
ims[0].save(f"{OUT}/day-claude-03-carousel.pdf","PDF",save_all=True,append_images=ims[1:],resolution=150)
print("done ->",OUT)
