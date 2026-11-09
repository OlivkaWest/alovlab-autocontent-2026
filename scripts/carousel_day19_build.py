# -*- coding: utf-8 -*-
"""AlovLab · Карусель дня 19 (19.10.2026) — параллельный формат к ведущему Reels того же дня.
Запись календаря: content/october-2026-system/calendar/calendar.csv, OCT-19. Ведущий формат дня —
Reels (format_lead=Reels), карусель — добавленный формат по запросу пользователя («и карусель»),
та же CORE IDEA, что в reels-extra/day-19 (пайплайн: сценарий-диалог → два голоса → монтаж).
Методичка G07 (реестр «Видео и звук для клиента», дни 18-21) ещё не написана — CTA не обещает файл,
только личный разбор в комментариях, как и в самом Reels этого дня.
Светлый премиум-инфографик, тот же стиль/компоненты, что в carousel_day14_build.py.
6 слайдов 1080×1350 (4:5). Запуск:
  python3 scripts/carousel_day19_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <html> <outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "content" / "october-2026-system" / "carousels-extra" / "day-19"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "carousel.html"

def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")

RANGES = {"cyrillic": "U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin": "U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192"}
faces = ""
for w in (400, 500, 600, 700, 800):
    for sub in ("cyrillic", "latin"):
        fp = FONTS / f"manrope-{sub}-{w}.woff2"
        if fp.exists():
            faces += ("@font-face{font-family:'Manrope';font-weight:%d;font-display:swap;"
                      "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}\n"
                      % (w, b64(fp), RANGES[sub]))

CSS = faces + r"""
*{margin:0;padding:0;box-sizing:border-box;font-family:'Manrope',sans-serif}
body{background:#ddd5c4}
.slide{position:relative;width:540px;height:675px;overflow:hidden;background:#FBF4E9;
 display:flex;flex-direction:column;padding:34px 36px 30px;page-break-after:always}
.kicker{font-size:12.5pt;font-weight:800;letter-spacing:.06em;color:#E1671E;text-transform:uppercase}
h1{font-size:34pt;font-weight:800;line-height:1.04;color:#20242B;margin-top:8px;letter-spacing:-.01em}
h1 i{font-style:normal;color:#E1671E}
h2{font-size:25pt;font-weight:800;line-height:1.1;color:#20242B;margin-top:6px}
h2 i{font-style:normal;color:#E1671E}
.lead{font-size:13.5pt;font-weight:600;color:#3a362f;margin-top:10px;line-height:1.42;max-width:94%}
.sub{font-size:11.5pt;font-weight:500;color:#6E6A63;margin-top:4px;line-height:1.4;max-width:94%}
.badge{position:absolute;top:28px;left:34px;font-size:11pt;font-weight:800;color:#6E6A63;
 border:1.5px solid #E1671E;border-radius:20px;padding:4px 13px;background:#FFF}
.card{background:#FFFFFF;border:1px solid #EBE2D3;border-radius:16px;padding:18px 20px;margin-top:14px;
 box-shadow:0 2px 10px rgba(32,20,10,.04)}
.card.sand{background:#FBEFE0}
.card .lbl{font-size:10.5pt;font-weight:800;letter-spacing:.05em;color:#E1671E;text-transform:uppercase;margin-bottom:8px}
.card p{font-size:12pt;font-weight:500;color:#3a362f;line-height:1.45}
.steps{display:flex;flex-direction:column;gap:12px;margin-top:4px}
.step{display:flex;gap:12px;align-items:flex-start}
.step .n{flex:0 0 auto;width:30px;height:30px;border-radius:50%;background:#E1671E;color:#fff;
 font-weight:800;font-size:13pt;display:flex;align-items:center;justify-content:center}
.step .t{font-size:12.3pt;font-weight:600;color:#20242B;line-height:1.38;padding-top:2px}
.step .t b{color:#E1671E}
.note{font-size:10.8pt;font-weight:600;color:#6E6A63;margin-top:10px;line-height:1.4}
.retention{position:absolute;left:36px;right:36px;bottom:56px;font-size:12.5pt;font-weight:700;color:#E1671E}
.sig{position:absolute;bottom:22px;left:36px;display:flex;align-items:center;gap:8px}
.sig img{width:26px;height:26px}
.sig b{font-size:12pt;font-weight:800;color:#20242B}
.sig b i{font-style:normal;color:#E1671E}
.warn{background:#FBEFE0;border:1.5px solid #F2A65A;border-radius:14px;padding:14px 16px;margin-top:12px}
.warn .lbl{font-size:10pt;font-weight:800;color:#E1671E;text-transform:uppercase;margin-bottom:6px}
.warn p{font-size:11.3pt;font-weight:500;color:#3a362f;line-height:1.42}
.chain{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-top:14px;background:#FFFFFF;
 border:1px solid #EBE2D3;border-radius:14px;padding:14px 16px}
.chain b{font-size:11pt;font-weight:800;color:#20242B;background:#FBEFE0;border-radius:9px;padding:6px 11px}
.chain .a{color:#E1671E;font-weight:800;font-size:13pt}
.pillrow{display:flex;gap:9px;margin-top:14px;flex-wrap:wrap}
.pillrow span{background:#FFFFFF;border:1px solid #EBE2D3;border-radius:20px;padding:7px 14px;
 font-size:11pt;font-weight:700;color:#20242B}
.gb{display:flex;gap:12px;margin-top:4px}
.gb .box{flex:1;border-radius:14px;padding:14px 16px}
.gb .box.bad{background:#FCEEEA;border:1px solid #EFC7BB}
.gb .box.good{background:#EAF3EC;border:1px solid #BFDCC6}
.gb .lbl{font-size:10pt;font-weight:800;text-transform:uppercase;margin-bottom:6px}
.gb .bad .lbl{color:#C0492E}
.gb .good .lbl{color:#3E8E55}
.gb p{font-size:11pt;font-weight:500;color:#3a362f;line-height:1.4}
"""

def sig():
    return (f'<div class="sig"><img src="data:image/png;base64,{LOGO}">'
            f'<b>Alov<i>Lab</i></b></div>')

slides = []

# 1 — обложка / хук (hookA из calendar.csv)
slides.append(f"""<div class="slide">
 <div class="badge">1 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">AI-подкаст</div>
  <h1>ЭТОТ ПОДКАСТ<br>ВЕДУТ <i>ДВА<br>ЧЕЛОВЕКА.</i></h1>
  <p class="lead">Ни один из них не существует.</p>
  <div class="pillrow"><span>Сценарий</span><span>Два голоса</span><span>Монтаж</span></div>
 </div>
 <div class="retention">Как это устроено на самом деле  →</div>
 {sig()}
</div>""")

# 2 — как устроено: цепочка
slides.append(f"""<div class="slide">
 <div class="badge">2 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Разрушаем миф</div>
  <h2>Нет студии.<br>Нет <i>двух дикторов</i></h2>
  <p class="lead" style="font-size:12pt">Есть один текст-диалог и два разных синтезированных голоса, наложенных по очереди.</p>
  <div class="chain">
   <b>сценарий-диалог</b><span class="a">→</span><b>голос 1</b><span class="a">→</span><b>голос 2</b><span class="a">→</span><b>монтаж</b>
  </div>
  <p class="note">Голоса — два клона или два голоса из библиотеки, нарочно разные по тембру и темпу, чтобы не путались на слух.</p>
 </div>
 <div class="retention">5 шагов, чтобы собрать свой  →</div>
 {sig()}
</div>""")

# 3 — чек-лист сборки
slides.append(f"""<div class="slide">
 <div class="badge">3 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Чек-лист сборки</div>
  <h2>5 шагов до <i>готового</i></h2>
  <div class="steps" style="margin-top:10px;gap:10px">
   <div class="step"><div class="n">1</div><div class="t" style="font-size:11.6pt">Пиши диалог как пьесу — реплика за репликой, с именем говорящего перед каждой строкой.</div></div>
   <div class="step"><div class="n">2</div><div class="t" style="font-size:11.6pt">Выбери два контрастных голоса — разный тембр, разный темп речи, не близнецы.</div></div>
   <div class="step"><div class="n">3</div><div class="t" style="font-size:11.6pt">Озвучь реплики каждого голоса отдельно, по ролям, не одним проходом.</div></div>
   <div class="step"><div class="n">4</div><div class="t" style="font-size:11.6pt">Смонтируй с короткими живыми паузами между репликами — без них звучит как два робота по очереди.</div></div>
   <div class="step"><div class="n">5</div><div class="t" style="font-size:11.6pt">Прослушай в наушниках целиком — не путаются ли голоса в середине разговора.</div></div>
  </div>
 </div>
 <div class="retention">Частая ошибка новичка  →</div>
 {sig()}
</div>""")

# 4 — частая ошибка → фикс
slides.append(f"""<div class="slide">
 <div class="badge">4 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Частая ошибка → фикс</div>
  <h2>Оба голоса<br>звучат <i>одинаково</i></h2>
  <div class="warn">
   <div class="lbl">Ошибка</div>
   <p>Взяли два похожих голоса из библиотеки — через минуту слушатель уже не понимает, кто сейчас говорит.</p>
  </div>
  <div class="card sand">
   <div class="lbl">Фикс</div>
   <p>Бери контраст нарочно: один голос ниже и медленнее, второй выше и живее. Разница должна быть слышна с первой фразы.</p>
  </div>
  <p class="note">Проверка: закрой глаза и слушай только первые 10 секунд каждого — если путаешь, голоса слишком похожи.</p>
 </div>
 <div class="retention">Честно про эту тему  →</div>
 {sig()}
</div>""")

# 5 — честный пример / ограничение (без выдуманного кейса)
slides.append(f"""<div class="slide">
 <div class="badge">5 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Честно, без прикрас</div>
  <h2>Самое сложное —<br>не <i>голоса</i></h2>
  <div class="gb">
   <div class="box bad"><div class="lbl">Кажется сложным</div><p>Найти два разных голоса и записать текст.</p></div>
   <div class="box good"><div class="lbl">Реально сложное</div><p>Живые паузы, перебивки и темп — то, что отличает разговор от двух монологов подряд.</p></div>
  </div>
  <p class="note">В портфеле AlovLab пока готов сольный AI-подкаст на голосовом клонировании (ElevenLabs) — диалоговый формат с двумя голосами строится на той же базе, следующим шагом конвейера.</p>
 </div>
 <div class="retention">Собери свой  →</div>
 {sig()}
</div>""")

# 6 — итог + один CTA
slides.append(f"""<div class="slide">
 <div class="badge">6 / 6</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">СОБЕРИ<br><i>СВОЙ</i></h1>
  <p class="lead" style="margin-top:10px">Сценарий, два голоса, монтаж — конвейер, а не студия на два человека.</p>
  <div class="card sand" style="margin-top:16px">
   <div class="lbl">Разбор под твою тему</div>
   <p>Напиши «ПОДКАСТ» в комментариях — разберу, как собрать такой диалог под твою тему.</p>
  </div>
 </div>
 {sig()}
</div>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(slides)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "slides:", len(slides))
