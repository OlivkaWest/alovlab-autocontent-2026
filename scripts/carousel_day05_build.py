# -*- coding: utf-8 -*-
"""AlovLab · Карусель дня 5 (05.10.2026) — «Один вопрос — два разных ответа. Не баг».
Дополнительная карусель к плановому Reels-дню (лид-формат дня 5 в календаре — Reels, уже написан,
не меняется). Та же CORE IDEA, что в reels/ru/day-05.md и G02 глава 2.
Светлый премиум-инфографик, эталон стиля — exports/carousels/day-claude-06-v2 (GLOBAL-CAROUSEL-RULE §13-Б).
6 слайдов 1080×1350 (4:5). Запуск:
  python3 scripts/carousel_day05_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <html> <outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "content" / "october-2026-system" / "carousels-extra" / "day-05"
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
.topright{position:absolute;top:26px;right:32px;display:flex;align-items:center;gap:7px}
.topright img{width:26px;height:26px}
.topright b{font-size:13pt;font-weight:800;color:#20242B}
.topright b i{font-style:normal;color:#E1671E}
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
.promptbox{background:#1c1712;border-radius:16px;padding:20px 22px;margin-top:14px}
.promptbox .lbl{font-size:10pt;font-weight:800;letter-spacing:.07em;color:#F2A65A;text-transform:uppercase;margin-bottom:10px}
.promptbox code{display:block;font-family:'Manrope',sans-serif;font-size:11.3pt;font-weight:500;line-height:1.56;color:#EFE8DD;white-space:pre-wrap}
.promptbox.sm{padding:15px 18px}
.promptbox.sm code{font-size:10.5pt}
.ans{display:flex;gap:10px;align-items:flex-start;background:#FFFFFF;border:1px solid #EBE2D3;border-radius:12px;padding:10px 14px;margin-top:9px}
.ans .n{flex:0 0 auto;width:22px;height:22px;border-radius:50%;background:#F2A65A;color:#fff;font-weight:800;font-size:10.5pt;display:flex;align-items:center;justify-content:center;margin-top:1px}
.ans p{font-size:10.6pt;font-weight:500;color:#3a362f;line-height:1.4;font-style:italic}
.oneans{background:#FFFFFF;border:1px solid #EBE2D3;border-radius:12px;padding:12px 16px;margin-top:10px}
.oneans p{font-size:11pt;font-weight:500;color:#3a362f;line-height:1.42;font-style:italic}
.note{font-size:10.8pt;font-weight:600;color:#6E6A63;margin-top:10px;line-height:1.4}
.split{display:flex;gap:12px;margin-top:14px}
.split .half{flex:1;background:#FFFFFF;border:1px solid #EBE2D3;border-radius:14px;padding:14px 16px}
.split .half.after{border-color:#E1671E}
.split .lbl{font-size:10pt;font-weight:800;letter-spacing:.05em;text-transform:uppercase;margin-bottom:8px}
.split .before .lbl{color:#9a9183}
.split .after .lbl{color:#E1671E}
.split li{font-size:10.8pt;font-weight:500;color:#3a362f;line-height:1.5;list-style:none;margin-bottom:3px}
.split li:before{content:"— "}
.retention{position:absolute;left:36px;right:36px;bottom:56px;font-size:12.5pt;font-weight:700;color:#E1671E}
.slide.has-footer .retention{bottom:130px}
.footer{position:absolute;bottom:62px;left:0;right:0;display:flex;justify-content:center;gap:22px}
.footer .chip{display:flex;flex-direction:column;align-items:center;gap:4px}
.footer .chip svg{width:20px;height:20px}
.footer .chip span{font-size:7.6pt;font-weight:700;color:#6E6A63;text-align:center;max-width:62px}
.sig{position:absolute;bottom:22px;left:36px;display:flex;align-items:center;gap:8px}
.sig img{width:26px;height:26px}
.sig b{font-size:12pt;font-weight:800;color:#20242B}
.sig b i{font-style:normal;color:#E1671E}
.warn{background:#FBEFE0;border:1.5px solid #F2A65A;border-radius:14px;padding:14px 16px;margin-top:12px}
.warn .lbl{font-size:10pt;font-weight:800;color:#E1671E;text-transform:uppercase;margin-bottom:6px}
.warn p{font-size:11.3pt;font-weight:500;color:#3a362f;line-height:1.42}
.illustrative{font-size:9.3pt;font-weight:600;color:#9a9183;margin-top:8px;font-style:italic}
"""

def brand_top():
    return f'<div class="topright"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></div>'

def sig():
    return (f'<div class="sig"><img src="data:image/png;base64,{LOGO}">'
            f'<b>Alov<i>Lab</i></b></div>')

ICON_TARGET = '<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="#E1671E" stroke-width="2"/><circle cx="12" cy="12" r="4.5" stroke="#E1671E" stroke-width="2"/><circle cx="12" cy="12" r="1.3" fill="#E1671E"/></svg>'
ICON_BOLT = '<svg viewBox="0 0 24 24" fill="none"><path d="M13 2 4 14h6l-1 8 9-12h-6l1-8z" fill="#4A8E7E"/></svg>'
ICON_PROMPT = '<svg viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2" stroke="#F2A65A" stroke-width="2"/><path d="M7 10h10M7 14h6" stroke="#F2A65A" stroke-width="2" stroke-linecap="round"/></svg>'
ICON_BOOKMARK = '<svg viewBox="0 0 24 24" fill="none"><path d="M6 3h12v18l-6-4-6 4V3z" stroke="#9D7FD6" stroke-width="2" stroke-linejoin="round"/></svg>'
ICON_STAR = '<svg viewBox="0 0 24 24" fill="none"><path d="M12 2l2.9 6.6 7.1.6-5.4 4.7 1.7 7-6.3-3.9-6.3 3.9 1.7-7-5.4-4.7 7.1-.6z" stroke="#E1671E" stroke-width="1.8" stroke-linejoin="round"/></svg>'

def footer():
    chips = [(ICON_TARGET, "КОНКРЕТНО"), (ICON_BOLT, "ПО ШАГАМ"), (ICON_PROMPT, "ПРОМПТ"),
             (ICON_BOOKMARK, "СОХРАНИ"), (ICON_STAR, "УРОВЕНЬ ЭКСПЕРТА")]
    return '<div class="footer">' + "".join(
        f'<div class="chip">{svg}<span>{label}</span></div>' for svg, label in chips) + '</div>'

N = 8
slides = []

# 1 — обложка / хук
slides.append(f"""<div class="slide has-footer">
 <div class="badge">1 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Как работает ответ нейронки</div>
  <h1>ОДИН ВОПРОС<br><i>ДВА РАЗНЫХ ОТВЕТА</i></h1>
  <p class="lead">И это не баг — модель отвечает по-разному каждый раз.</p>
  <p class="sub">Разбираем на конкретном примере одного вопроса.</p>
 </div>
 <div class="retention">Смотри, как это выглядит на практике  →</div>
 {footer()}{sig()}
</div>""")

# 2 — проблема / наблюдение
slides.append(f"""<div class="slide">
 <div class="badge">2 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Знакомая ситуация</div>
  <h2>Задал тот же вопрос.<br>Получил <i>другой</i> ответ.</h2>
  <p class="sub">Кажется, что нейронка ошиблась. На самом деле — нет.</p>
  <div class="card">
   <div class="lbl">Что происходит на самом деле</div>
   <p>Модель не хранит готовый ответ и не вспоминает его из базы. Она собирает ответ заново при каждом запуске, и немного по-разному.</p>
  </div>
  <div class="card sand">
   <div class="lbl">Почему это не ошибка</div>
   <p>Оба ответа могут быть одинаково правильными. Это просто разные пути к одному результату, а не один верный и один сломанный.</p>
  </div>
 </div>
 <div class="retention">Вот как это выглядит на одном и том же вопросе  →</div>
 {sig()}
</div>""")

# 3 — пример: спросили неправильно
slides.append(f"""<div class="slide">
 <div class="badge">3 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Пример · как спросили не так</div>
  <h2>Один вопрос.<br>Один ответ <i>без выбора</i>.</h2>
  <div class="promptbox sm">
   <div class="lbl">Вопрос нейронке</div>
   <code>Напиши короткий пост в Instagram про скидку 20% на кофе в выходные.</code>
  </div>
  <div class="oneans">
   <p>«Друзья, в эти выходные дарим скидку 20% на все напитки! Ждём вас в гости!»</p>
  </div>
  <div class="warn">
   <div class="lbl">В чём проблема</div>
   <p>Ответ один — и его сразу приняли как готовый. Не с чем сравнить, не видно, мог ли выйти текст точнее.</p>
  </div>
  <p class="illustrative">Учебный пример, не переписка реального клиента AlovLab.</p>
 </div>
 <div class="retention">Тот же вопрос, но на один шаг длиннее  →</div>
 {sig()}
</div>""")

# 4 — пример: спросили правильно
slides.append(f"""<div class="slide">
 <div class="badge">4 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Пример · как спросить правильно</div>
  <h2>Та же задача.<br>Три ответа <i>на выбор</i>.</h2>
  <div class="promptbox sm">
   <div class="lbl">Тот же вопрос + одна строка</div>
   <code>Напиши короткий пост в Instagram про скидку 20% на кофе в выходные.
Дай два-три разных варианта, не один. Пронумеруй их.</code>
  </div>
  <div class="ans"><div class="n">1</div><p>«В эти выходные кофе с нами на 20% дешевле. Заходи.»</p></div>
  <div class="ans"><div class="n">2</div><p>«Суббота и воскресенье — скидка 20% на весь кофе. Без предзаказа.»</p></div>
  <div class="ans"><div class="n">3</div><p>«Хочешь кофе чуть дешевле в выходные? У нас минус 20%.»</p></div>
 </div>
 <div class="retention">Выбрали — не угадали с первого раза  →</div>
 {sig()}
</div>""")

# 5 — что это даёт
slides.append(f"""<div class="slide">
 <div class="badge">5 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Что изменилось</div>
  <h2>Из трёх видно,<br>какой <i>точнее</i>.</h2>
  <div class="steps" style="margin-top:16px">
   <div class="step"><div class="n">1</div><div class="t">Вариант 1 — короче всего, годится для сторис.</div></div>
   <div class="step"><div class="n">2</div><div class="t">Вариант 2 — с деталью «без предзаказа», снимает лишний вопрос у клиента.</div></div>
   <div class="step"><div class="n">3</div><div class="t">Вариант 3 — вопросом, подходит, если в блоге обычно живой тон.</div></div>
  </div>
  <div class="warn">
   <div class="lbl">Почему это важно</div>
   <p>Один вариант — это одна попытка, не факт. Особенно если текст пойдёт клиенту или в публикацию.</p>
  </div>
 </div>
 <div class="retention">Готовый шаблон для своих вопросов  →</div>
 {sig()}
</div>""")

# 6 — готовый промпт (тот же, что в G02 глава 2)
slides.append(f"""<div class="slide">
 <div class="badge">6 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Промпт · копируй</div>
  <h2>Шаблон на <i>несколько</i> вариантов</h2>
  <div class="promptbox">
   <div class="lbl">Копируемый промпт</div>
   <code>[твой обычный рабочий запрос]
Дай два-три разных варианта ответа, не один. Пронумеруй их.</code>
  </div>
  <p class="note">Добавляешь одну строку к любому своему вопросу. Тот же шаблон — в методичке G02, глава 2.</p>
 </div>
 <div class="retention">Частая ошибка, которую это чинит  →</div>
 {sig()}
</div>""")

# 7 — до/после + ошибка
slides.append(f"""<div class="slide">
 <div class="badge">7 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">До / после</div>
  <h2>Одна попытка <i>или выбор</i></h2>
  <div class="split">
   <div class="half before"><div class="lbl">Один ответ</div>
    <li>Берёшь первый результат</li><li>Не с чем сравнить</li><li>Не подошёл — переделываешь с нуля</li>
   </div>
   <div class="half after"><div class="lbl">Три варианта</div>
    <li>Сравниваешь между собой</li><li>Видно, где точнее</li><li>Выбираешь, а не угадываешь</li>
   </div>
  </div>
  <div class="warn">
   <div class="lbl">Частая ошибка → фикс</div>
   <p>Берёшь первый ответ, потому что он пришёл быстро. Фикс: добавь в промпт «дай два-три варианта» — это одна строка, не лишняя работа.</p>
  </div>
 </div>
 <div class="retention">Попробуй на следующем запросе  →</div>
 {sig()}
</div>""")

# 8 — итог + CTA
slides.append(f"""<div class="slide has-footer">
 <div class="badge">8 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <h1 style="font-size:30pt">Два ответа —<br><i>не ошибка, а выбор</i>.</h1>
  <p class="lead" style="margin-top:14px">Попробуй на следующем запросе: попроси не один ответ, а три. Особенно если текст уйдёт клиенту.</p>
  <div class="card sand" style="margin-top:20px">
   <div class="lbl">Забирай шаблон</div>
   <p>Готовый промпт на несколько вариантов — в комментариях под постом.</p>
  </div>
 </div>
 {footer()}{sig()}
</div>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(slides)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "slides:", len(slides))
