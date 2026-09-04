# -*- coding: utf-8 -*-
"""AlovLab · День 21 (24.08) «Прогрев / МОСТ 4 КАСАНИЙ» — карусель v2 (кинокадр + знание).
Кадры пользователя (scene-only) в content/carousel-assets/day-21/s1..s8 + впечатанный МЕТОД:
авторский термин «Мост 4 касаний», save-слайд «что писать», реальный промпт Claude.
Стиль не меняем: cinematic premium, графит + огонь + оранжевый. Данные интегрированы в сцену
полупрозрачными стеклянными панелями (не PowerPoint). Слайд 7 честно поправлен (без «+76 заявок»).
Сборка: python3 scripts/carousel_day21_build.py → node scripts/carousel_shoot.js <html> <outdir>"""
import base64, pathlib
from carousel_showcase_render import CSS as CSS0, LOGO, ROOT

OUTDIR = ROOT / "exports" / "carousels" / "day-21"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-21.html"
ASSET = ROOT / "content" / "carousel-assets" / "day-21"

def _prep():
    """Из присланных ChatGPT-кадров готовит s1..s8 и честно закрывает выдуманный
    «+76 заявок» на s7 (Rule 0)."""
    import glob, shutil
    from PIL import Image, ImageDraw, ImageFont
    files = sorted(glob.glob(str(ASSET / "ChatGPT Image*.png")))
    for i, f in enumerate(files, 1):
        shutil.copy(f, ASSET / f"s{i}.png")
    im = Image.open(ASSET / "s7.png").convert("RGB"); d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = 546, 546, 736, 700
    d.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=(19, 16, 12), outline=(150, 90, 45), width=1)
    FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    fo, fh, fs = ImageFont.truetype(FB, 13), ImageFont.truetype(FB, 17), ImageFont.truetype(FR, 11)
    cx = (x0 + x1) // 2
    def ct(y, t, f, fill):
        w = d.textlength(t, font=f); d.text((cx - w / 2, y), t, font=f, fill=fill)
    ct(y0 + 16, "ПОСТ 3 · ДОКАЗАТЕЛЬСТВО", fo, (232, 138, 61))
    ct(y0 + 42, "Твой реальный кейс", fh, (240, 236, 230))
    ct(y0 + 74, "что вышло в работе —", fs, (150, 142, 130))
    ct(y0 + 90, "без выдуманных цифр", fs, (150, 142, 130))
    im.save(ASSET / "s7.png")

def img_src(name):
    p = ASSET / (name + ".png")
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()

EXTRA = r"""
.d21{position:relative;width:540px;height:675px;overflow:hidden;background:#0a0806;border-radius:0}
.d21 .bg{position:absolute;inset:0;background-size:cover}
.d21 .scrim{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,5,4,.94) 3%,rgba(6,5,4,.72) 24%,rgba(6,5,4,.28) 46%,rgba(6,5,4,.5) 70%,rgba(6,5,4,.82) 100%)}
.d21 .top{position:absolute;left:30px;right:26px;top:22px;display:flex;justify-content:space-between;align-items:flex-start;z-index:3}
.d21 .eb{font-weight:800;font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--o2);max-width:66%;line-height:1.3}
.d21 .pg{display:flex;align-items:center;gap:2px;background:rgba(0,0,0,.5);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:6px 12px;font-weight:800;font-size:14px;color:#fff}
.d21 .pg b{color:var(--o2)}
.d21 .hd{position:absolute;left:32px;right:32px;top:52px;z-index:3}
.d21 .hd h2{font-weight:800;font-size:35px;line-height:1.02;letter-spacing:-.02em;color:#fff;text-shadow:0 2px 20px rgba(0,0,0,.8)}
.d21 .hd h2 .o{color:var(--o2);display:block}
.d21 .hd h2.sm{font-size:31px}
.d21 .hd .sub{margin-top:11px;font-size:14px;line-height:1.35;color:#e9dfce;font-weight:600;max-width:24ch;text-shadow:0 1px 12px rgba(0,0,0,.9)}
.d21 .lg{position:absolute;left:32px;bottom:26px;display:flex;align-items:center;gap:8px;z-index:4}
.d21 .lg img{width:24px;height:24px;border-radius:7px}
.d21 .lg b{font-weight:800;font-size:14px;color:#fff}.d21 .lg b i{color:var(--o2);font-style:normal}
/* стеклянная панель под метод */
.d21 .panel{position:absolute;left:30px;right:30px;z-index:3;background:rgba(9,7,5,.62);
 -webkit-backdrop-filter:blur(7px);backdrop-filter:blur(7px);border:1px solid rgba(255,160,90,.2);
 border-left:3px solid var(--o);border-radius:15px;padding:15px 17px}
.d21 .sysrow{display:grid;grid-template-columns:30px 1fr;gap:11px;align-items:baseline;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.09)}
.d21 .sysrow:last-child{border-bottom:0}.d21 .sysrow:first-child{padding-top:0}
.d21 .sysrow .nm{font-weight:800;font-size:16px;color:var(--o2);line-height:1}
.d21 .sysrow .lb{font-weight:800;font-size:14px;color:#fff;letter-spacing:.01em}
.d21 .sysrow .ds{display:block;margin-top:2px;font-weight:500;font-size:11.5px;line-height:1.32;color:#c9bda9}
/* пары «касание → мысль» */
.d21 .qrow{display:flex;align-items:center;gap:9px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.09)}
.d21 .qrow:last-child{border-bottom:0}.d21 .qrow:first-child{padding-top:0}
.d21 .qrow .a{font-weight:800;font-size:12.5px;color:#fff;min-width:118px;text-transform:uppercase;letter-spacing:.02em}
.d21 .qrow .ar{color:var(--o2);font-weight:800}
.d21 .qrow .b{font-size:13px;color:var(--o3);font-weight:700;font-style:italic}
/* горизонтальная цепочка */
.d21 .chain{display:flex;align-items:center;gap:7px;flex-wrap:wrap}
.d21 .chain .c{font-weight:800;font-size:14px;color:#fff;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);border-radius:9px;padding:8px 11px}
.d21 .chain .c.f{color:#8a8073;background:rgba(255,255,255,.03);border-color:rgba(255,255,255,.08)}
.d21 .chain .ar{color:var(--o2);font-weight:800;font-size:15px}
/* вертикальный мост */
.d21 .bridge{display:flex;flex-direction:column;gap:0}
.d21 .bridge .nd{display:grid;grid-template-columns:30px 1fr;gap:11px;align-items:center;padding:8px 0}
.d21 .bridge .nd .nm{font-weight:800;font-size:15px;color:var(--o2)}
.d21 .bridge .nd .lb{font-weight:800;font-size:15px;color:#fff;letter-spacing:.01em}
.d21 .bridge .ln{grid-column:1;width:2px;height:9px;background:linear-gradient(var(--o),transparent);margin-left:14px}
/* формула */
.d21 .formula{display:inline-flex;align-items:center;gap:10px;background:rgba(9,7,5,.6);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);border:1px solid rgba(255,160,90,.28);border-radius:13px;padding:13px 18px}
.d21 .formula b{font-weight:800;font-size:17px;color:#fff}.d21 .formula .ar{color:var(--o2);font-size:18px;font-weight:800}
/* промпт-плашка */
.d21 .prm{position:absolute;left:30px;right:30px;z-index:3;background:rgba(6,5,4,.82);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);border:1px solid rgba(255,150,80,.4);border-left:3px solid var(--o);border-radius:13px;padding:13px 15px}
.d21 .prm .tag{display:inline-block;font-weight:800;font-size:8.5px;letter-spacing:.08em;text-transform:uppercase;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:3px 8px;border-radius:5px;margin-bottom:9px}
.d21 .prm code{display:block;font-family:'SF Mono',ui-monospace,Menlo,monospace;font-size:10px;line-height:1.5;color:#ffe0c4;white-space:pre-wrap}
.d21 .cap{position:absolute;left:32px;right:32px;bottom:58px;z-index:3;font-size:12px;font-weight:700;color:#e9dfce;font-style:italic;text-shadow:0 1px 10px rgba(0,0,0,.9)}
"""
CSS = CSS0 + EXTRA
EB = "AlovLab · МОСТ 4 КАСАНИЙ"

_prep()

def frame(n, img, pos, inner):
    return (f'<div class="slide d21"><div class="bg" style="background-image:url({img_src(img)});background-position:{pos}"></div>'
            f'<div class="scrim"></div>'
            f'<div class="top"><span class="eb">{EB}</span><span class="pg">{n}&nbsp;<b>/ 8</b></span></div>'
            f'{inner}'
            f'<div class="lg"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div></div>')

def hd(w, o, sub=None, sm=False):
    s = f'<div class="sub">{sub}</div>' if sub else ''
    cls = 'sm' if sm else ''
    return f'<div class="hd"><h2 class="{cls}">{w} <span class="o">{o}</span></h2>{s}</div>'

def panel(bottom, rows_html):
    return f'<div class="panel" style="bottom:{bottom}px">{rows_html}</div>'

SLIDES = []

# 1 — конфликт (без изменений)
SLIDES.append(frame(1, "s1", "50% 56%",
  hd("Подписался —", "не значит купит.", "Холодный подписчик остывает без внимания.")))

# 2 — потеря человека ПОСЛЕ магнита
chain2 = ('<div class="chain">'
          '<span class="c">ПОЛУЧИЛ</span><span class="ar">→</span>'
          '<span class="c">ПРОЧИТАЛ</span><span class="ar">→</span>'
          '<span class="c f">ТИШИНА</span><span class="ar">→</span>'
          '<span class="c f">ЗАБЫЛ</span></div>')
cap2 = '<div style="margin-top:12px;font-size:12.5px;line-height:1.35;color:#c9bda9;font-weight:600">Магнит скачали — и контакт затух. Тут и теряют человека.</div>'
SLIDES.append(frame(2, "s2", "50% 50%",
  hd("Главная ошибка —", "ПОСЛЕ магнита.", sm=True)
  + panel(140, chain2 + cap2)))

# 3 — раскрытие метода: мост из 4 касаний
bridge3 = ('<div class="bridge">'
  '<div class="nd"><span class="nm">01</span><span class="lb">ЗНАКОМСТВО</span></div><div class="ln"></div>'
  '<div class="nd"><span class="nm">02</span><span class="lb">МИКРО-РЕЗУЛЬТАТ</span></div><div class="ln"></div>'
  '<div class="nd"><span class="nm">03</span><span class="lb">ДОКАЗАТЕЛЬСТВО</span></div><div class="ln"></div>'
  '<div class="nd"><span class="nm">04</span><span class="lb">ПРЕДЛОЖЕНИЕ</span></div></div>')
SLIDES.append(frame(3, "s3", "50% 50%",
  hd("Построй мост", "из 4 касаний.", "Лид-магнит не продаёт. Он открывает мост до предложения.")
  + panel(70, bridge3)))

# 4 — механизм: каждое касание делает одну работу
q4 = ''.join(
  f'<div class="qrow"><span class="a">{a}</span><span class="ar">→</span><span class="b">{b}</span></div>'
  for a, b in [("Знакомство", "«Я тебя понимаю»"), ("Микро-результат", "«У меня получилось»"),
               ("Доказательство", "«Работает не только у автора»"), ("Предложение", "«Вижу следующий шаг»")])
SLIDES.append(frame(4, "s4", "50% 52%",
  hd("Каждое касание —", "одна работа.", sm=True)
  + panel(70, q4)))

# 5 — SAVE-слайд: что писать
sys5 = ''.join(
  f'<div class="sysrow"><span class="nm">{nm}</span><span><span class="lb">{lb}</span><span class="ds">{ds}</span></span></div>'
  for nm, lb, ds in [
    ("01", "ЗНАКОМСТВО", "История, ошибка, узнаваемая ситуация"),
    ("02", "МИКРО-РЕЗУЛЬТАТ", "Один приём, который применишь сразу"),
    ("03", "ДОКАЗАТЕЛЬСТВО", "Кейс, до–после, разбор — факт вместо слов"),
    ("04", "ПРЕДЛОЖЕНИЕ", "Один логичный следующий шаг")])
SLIDES.append(frame(5, "s5", "50% 40%",
  hd("Вот что писать", "в 4 постах.", sm=True)
  + panel(66, sys5)))

# 6 — правило одного следующего шага
SLIDES.append(frame(6, "s6", "50% 46%",
  hd("Один пост —", "один следующий шаг.", "Не «подпишись + скачай + купи» разом. Один CTA на пост.")
  + '<div class="panel" style="bottom:120px;text-align:center;border-left:0">'
    '<div class="formula"><b>ОДНА МЫСЛЬ</b><span class="ar">→</span><b>ОДНО ДЕЙСТВИЕ</b></div></div>'))

# 7 — реальный промпт «Мост 4 касаний»
PROMPT = (
  "Ты — редактор Telegram-воронки.\n"
  "Лид-магнит: [ЧТО ПОЛУЧИЛ ЧЕЛОВЕК]\n"
  "Аудитория: [КТО] · Продукт: [ЧТО ПРОДАЮ]\n\n"
  "Собери мост из 4 постов:\n"
  "1. Знакомство — продолжи мысль магнита\n"
  "2. Микро-результат — дай маленькую победу\n"
  "3. Доказательство — покажи кейс / разбор\n"
  "4. Предложение — один логичный шаг\n\n"
  "Для каждого: хук, мысль, структура, CTA.\n"
  "Без инфостиля, клише и давления.")
SLIDES.append(frame(7, "s7", "50% 30%",
  hd("Дай Claude", "архитектуру.", sm=True)
  + '<div class="prm" style="bottom:84px"><span class="tag">Промпт · Мост 4 касаний</span>'
    f'<code>{PROMPT}</code></div>'
  + '<div class="cap">Не проси «напиши прогрев» — дай конструкцию.</div>'))

# 8 — CTA (сцена без изменений)
SLIDES.append(frame(8, "s8", "50% 50%",
  hd("Забери", "план прогрева.", "Промпт + бланк «Мост 4 касаний» — в тетради дня.")))

HTML = (f'<meta charset="utf-8"><style>{CSS}\n.grid{{display:flex;flex-wrap:wrap;gap:0}}</style>'
        f'<div class="grid">{"".join(SLIDES)}</div>')
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
