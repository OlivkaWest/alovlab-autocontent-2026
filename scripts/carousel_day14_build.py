# -*- coding: utf-8 -*-
"""AlovLab · Карусель дня 14 (14.10.2026) — капстоун недели 2: «Собери свою первую карусель-визитку».
Запись календаря: content/october-2026-system/calendar/calendar.csv, OCT-14. Статус до этой сборки —
запланирован_текст_не_написан. Методичка G05 (дни 12-13-14) ещё не написана — в этой карусели это
не скрывается, CTA не обещает файл методички, только разбор в комментариях (как и прописано в
calendar.csv, cta_tg/cta_vk).
Светлый премиум-инфографик, тот же стиль/компоненты, что в carousel_day15_build.py.
6 слайдов 1080×1350 (4:5). Запуск:
  python3 scripts/carousel_day14_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <html> <outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "content" / "october-2026-system" / "carousels-extra" / "day-14"
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
.illustrative{font-size:9.3pt;font-weight:600;color:#9a9183;margin-top:8px;font-style:italic}
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

# 1 — обложка / хук
slides.append(f"""<div class="slide">
 <div class="badge">1 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Капстоун · Неделя 2</div>
  <h1>ТВОЯ ПЕРВАЯ<br><i>КАРУСЕЛЬ-ВИЗИТКА</i></h1>
  <p class="lead">Неделя визуала закончилась. Осталось собрать.</p>
  <div class="pillrow"><span>Кадры</span><span>Стиль</span><span>Структура</span></div>
  <p class="sub" style="margin-top:12px">У тебя уже есть всё три — ниже чек-лист, как это соединить в один пост.</p>
 </div>
 <div class="retention">Анатомия карусели, которую долистывают  →</div>
 {sig()}
</div>""")

# 2 — анатомия (recap дня 12)
slides.append(f"""<div class="slide">
 <div class="badge">2 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Анатомия · Повтор дня 12</div>
  <h2>Конфликт → усиление<br>→ связка → <i>CTA</i></h2>
  <div class="steps" style="margin-top:12px">
   <div class="step"><div class="n">1</div><div class="t"><b>Конфликт.</b> Первый слайд ломает ожидание — без «привет» и без плана поста.</div></div>
   <div class="step"><div class="n">2</div><div class="t"><b>Усиление.</b> 2-4 слайда дожимают мысль конкретикой: пример, цифра, приём.</div></div>
   <div class="step"><div class="n">3</div><div class="t"><b>Связка.</b> Один слайд соединяет тему с тем, что ты предлагаешь дальше.</div></div>
   <div class="step"><div class="n">4</div><div class="t"><b>CTA.</b> Последний слайд — один понятный шаг, не два конкурирующих.</div></div>
  </div>
  <div class="chain">
   <b>конфликт</b><span class="a">→</span><b>усиление</b><span class="a">→</span><b>связка</b><span class="a">→</span><b>CTA</b>
  </div>
 </div>
 <div class="retention">Чек-лист перед сборкой  →</div>
 {sig()}
</div>""")

# 3 — чек-лист сборки
slides.append(f"""<div class="slide">
 <div class="badge">3 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Чек-лист перед сборкой</div>
  <h2>5 вещей, которые должны <i>быть</i></h2>
  <div class="steps" style="margin-top:10px;gap:11px">
   <div class="step"><div class="n">1</div><div class="t" style="font-size:11.6pt">Одна главная мысль на весь пост — не отдельная тема на каждый слайд.</div></div>
   <div class="step"><div class="n">2</div><div class="t" style="font-size:11.6pt">Минимум 3 из 6: промпт, приём, алгоритм, до/после, чек-лист, ошибка+фикс.</div></div>
   <div class="step"><div class="n">3</div><div class="t" style="font-size:11.6pt">Первый слайд — хук жёстче всех остальных, без плана поста и приветствия.</div></div>
   <div class="step"><div class="n">4</div><div class="t" style="font-size:11.6pt">Один логотип на слайд — не задваивай бренд-знак сверху и снизу.</div></div>
   <div class="step"><div class="n">5</div><div class="t" style="font-size:11.6pt">Финал — один понятный CTA, не рекламный слайд вместо пользы.</div></div>
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
  <h2>Слайдов много.<br>Мысли — <i>ни одной</i></h2>
  <div class="warn">
   <div class="lbl">Ошибка</div>
   <p>Пытаться впихнуть всю экспертизу в 6 слайдов — получается каша, которую никто не долистывает до конца.</p>
  </div>
  <div class="card sand">
   <div class="lbl">Фикс</div>
   <p>Выбери одну мысль, которую человек унесёт с собой. Всё остальное — вычёркивай, даже если жалко.</p>
  </div>
  <p class="note">Проверка: убери все картинки — если текст без них всё ещё держит мысль, слайд готов.</p>
 </div>
 <div class="retention">Реальный пример — не чужой, наш  →</div>
 {sig()}
</div>""")

# 5 — реальный пример (до/после, честно — наша же карусель дня 15)
slides.append(f"""<div class="slide">
 <div class="badge">5 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Реальный пример · Не чужой, наш</div>
  <h2>Было 6.5/10.<br>Пересобрали за <i>вечер</i></h2>
  <div class="gb">
   <div class="box bad"><div class="lbl">Было</div><p>Абстрактные слайды без конкретики, слайд-реклама вместо пользы, два CTA на финале.</p></div>
   <div class="box good"><div class="lbl">Стало</div><p>Конкретный пайплайн на 4 шага, готовый промпт для копирования, один CTA.</p></div>
  </div>
  <p class="note">Та же карусель, тот же день — просто прогнали по чек-листу со слайда 3 ещё раз.</p>
 </div>
 <div class="retention">Собери свою сегодня  →</div>
 {sig()}
</div>""")

# 6 — итог + один CTA
slides.append(f"""<div class="slide">
 <div class="badge">6 / 6</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">СОБЕРИ<br><i>СВОЮ</i></h1>
  <p class="lead" style="margin-top:10px">Все инструменты уже на руках — осталось нажать «опубликовать».</p>
  <div class="card sand" style="margin-top:16px">
   <div class="lbl">Разбор твоей карусели</div>
   <p>Напиши «ВИЗИТКА» в комментариях — разберу твою первую карусель лично.</p>
  </div>
 </div>
 {sig()}
</div>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(slides)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "slides:", len(slides))
