import base64, pathlib
ROOT=pathlib.Path('.')
A=ROOT/'content/carousel-assets/day-17'
LOGO=base64.b64encode((ROOT/'assets/img/logo-mark.png').read_bytes()).decode()
order=['image','image1','image2','image3','image4','image5','image6','image7']  # -> слайды 1..8
def b64(p): return base64.b64encode(p.read_bytes()).decode()
CSS='''
*{margin:0;box-sizing:border-box}
@font-face{font-family:'Manrope';src:local('Manrope')}
.grid{display:flex;flex-wrap:wrap}
.slide{position:relative;width:540px;height:675px;overflow:hidden;background-size:cover;background-position:50% 15%;
 font-family:'Manrope',system-ui,sans-serif}
.pg{position:absolute;top:20px;right:22px;display:flex;align-items:center;gap:2px;
 background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:7px 13px;
 font-weight:800;font-size:15px;color:#fff;backdrop-filter:blur(3px)}
.pg b{color:#ff8a3d}
.lg{position:absolute;left:24px;bottom:22px;display:flex;align-items:center;gap:8px;
 filter:drop-shadow(0 2px 6px rgba(0,0,0,.8))}
.lg img{width:26px;height:26px;border-radius:7px}
.lg b{font-weight:800;font-size:16px;color:#fff}.lg b i{color:#ff8a3d;font-style:normal}
'''
slides=''
for i,key in enumerate(order, start=1):
    f=A/f'{key}.png'
    src=f'data:image/png;base64,{b64(f)}'
    slides+=(f'<div class="slide" style="background-image:url({src})">'
             f'<div class="pg">{i}&nbsp;<b>/ 8</b></div>'
             f'<div class="lg"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div></div>')
html=f'<meta charset="utf-8"><style>{CSS}</style><div class="grid">{slides}</div>'
(ROOT/'exports/carousels/day-17/day-17-final.html').write_text(html,encoding='utf-8')
print('html ok, slides:', len(order))
