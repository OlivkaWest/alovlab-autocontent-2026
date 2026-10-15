# -*- coding: utf-8 -*-
"""AlovLab · Карусель дня 15 (15.10.2026) — «Этот диктор не человек. И говорит на языке, которого не знает».
Дополнительная карусель к плановому Reels-дню (лид-формат дня 15 в календаре — Reels, не меняется,
текст рилса ещё не написан — отдельная задача). Тема: пайплайн AI-аватара, дублирующего контент
на незнакомом ему языке (calendar.csv, OCT-15).
Честность по числам (flex_what_to_check календаря): точный список языков и реальное качество
синхронизации у сторонних платформ не проверены из этой среды (сеть к ним заблокирована) — конкретное
число не называем. Единственное число в карусели — «90+ языков» для AlovLab Studio, это подтверждённый
факт из CLAUDE.md (раздел 1, Studio), не стороннее утверждение.
Светлый премиум-инфографик, тот же стиль/компоненты, что в carousel_day09_build.py.
6 слайдов 1080×1350 (4:5). Запуск:
  python3 scripts/carousel_day15_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <html> <outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "content" / "october-2026-system" / "carousels-extra" / "day-15"
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
.note{font-size:10.8pt;font-weight:600;color:#6E6A63;margin-top:10px;line-height:1.4}
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
.chain{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin-top:14px;background:#FFFFFF;
 border:1px solid #EBE2D3;border-radius:14px;padding:14px 16px}
.chain b{font-size:11pt;font-weight:800;color:#20242B;background:#FBEFE0;border-radius:9px;padding:6px 11px}
.chain .a{color:#E1671E;font-weight:800;font-size:13pt}
.langrow{display:flex;gap:9px;margin-top:14px}
.langrow .lc{flex:1;background:#FFFFFF;border:1px solid #EBE2D3;border-radius:12px;padding:11px 12px;
 box-shadow:0 2px 10px rgba(32,20,10,.04)}
.langrow .lc .code{font-size:9.5pt;font-weight:800;color:#E1671E;letter-spacing:.06em}
.langrow .lc .txt{font-size:11.5pt;font-weight:700;color:#20242B;margin-top:3px;line-height:1.3}
.promptbox{background:#1E1812;border-radius:16px;padding:17px 19px;margin-top:14px}
.promptbox .lbl{display:inline-block;background:#E1671E;color:#1E1812;font-size:9.5pt;font-weight:800;
 letter-spacing:.04em;text-transform:uppercase;border-radius:8px;padding:4px 10px;margin-bottom:10px}
.promptbox code{display:block;font-family:'Courier New',monospace;font-size:9.6pt;font-weight:600;
 color:#F3E9DA;line-height:1.52;white-space:pre-wrap}
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
    chips = [(ICON_TARGET, "КОНКРЕТНО"), (ICON_BOLT, "ПО ШАГАМ"), (ICON_PROMPT, "ПАЙПЛАЙН"),
             (ICON_BOOKMARK, "СОХРАНИ"), (ICON_STAR, "УРОВЕНЬ ЭКСПЕРТА")]
    return '<div class="footer">' + "".join(
        f'<div class="chip">{svg}<span>{label}</span></div>' for svg, label in chips) + '</div>'

def langrow(ru, en, es):
    return (f'<div class="langrow">'
            f'<div class="lc"><div class="code">RU</div><div class="txt">{ru}</div></div>'
            f'<div class="lc"><div class="code">EN</div><div class="txt">{en}</div></div>'
            f'<div class="lc"><div class="code">ES</div><div class="txt">{es}</div></div></div>')

LOC_PROMPT = ("Ты редактор-локализатор сценариев для видео с аватаром.\n"
"Сценарий на русском: [вставь текст].\n"
"Адаптируй под [целевой язык] — сохрани смысл и тон, не переводи дословно.\n"
"Не трогай: [название бренда, имена, цифры].\n"
"Не длиннее оригинала больше чем на 15% — иначе собьётся синхронизация губ.\n"
"Выдай: адаптированный текст + список мест, где пришлось перефразировать, и почему.")

slides = []

# 1 — обложка / хук
slides.append(f"""<div class="slide has-footer">
 <div class="badge">1 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">ИИ-аватары</div>
  <h1>ЭТОТ ДИКТОР<br><i>НЕ ЧЕЛОВЕК</i></h1>
  <p class="lead">И говорит на языке, которого не знает.</p>
  {langrow("Попробуй бесплатно", "Try it for free", "Pruébalo gratis")}
  <p class="illustrative">Иллюстративный пример перевода одной фразы, не результат реального проекта.</p>
 </div>
 <div class="retention">Разбираем пайплайн по шагам  →</div>
 {footer()}{sig()}
</div>""")

# 2 — проблема / было-стало
slides.append(f"""<div class="slide">
 <div class="badge">2 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Было vs стало</div>
  <h2>Три рынка —<br><i>три студии?</i></h2>
  <p class="sub">Вот что меняется, если локализуешь одну запись вместо новой на каждый рынок.</p>
  <div class="card">
   <div class="lbl">Было</div>
   <p>3 новых рынка → 3 студии, 3 диктора, 3 отдельных монтажа. Каждый — с нуля, заново от сценария до финального рендера.</p>
  </div>
  <div class="card sand">
   <div class="lbl">Стало</div>
   <p>3 новых рынка → 1 запись + пайплайн локализации. Один проект, три языка на выходе, без повторной студии.</p>
  </div>
 </div>
 <div class="retention">Как устроен этот пайплайн  →</div>
 {sig()}
</div>""")

# 3 — пайплайн / 4 шага
slides.append(f"""<div class="slide">
 <div class="badge">3 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Пайплайн · 4 шага</div>
  <h2>Один сценарий.<br><i>Любой язык</i> на выходе.</h2>
  <div class="steps" style="margin-top:12px">
   <div class="step"><div class="n">1</div><div class="t"><b>Исходник.</b> Записываешь сценарий один раз, на своём языке, обычным голосом.</div></div>
   <div class="step"><div class="n">2</div><div class="t"><b>Адаптация текста.</b> Перевод под рынок не дословный — сохраняет смысл, тон и термины бренда.</div></div>
   <div class="step"><div class="n">3</div><div class="t"><b>Дубляж и синхронизация.</b> Голос озвучивает новый текст, губы подстраиваются под него.</div></div>
   <div class="step"><div class="n">4</div><div class="t"><b>Проверка.</b> Смотришь короткий тестовый фрагмент на целевом языке перед полным рендером.</div></div>
  </div>
  <div class="chain">
   <b>исходник</b><span class="a">→</span><b>адаптация</b><span class="a">→</span><b>дубляж+синхро</b><span class="a">→</span><b>проверка</b>
  </div>
 </div>
 <div class="retention">Но это не значит «нажал кнопку и готово»  →</div>
 {sig()}
</div>""")

# 4 — 5 конкретных проверок
slides.append(f"""<div class="slide">
 <div class="badge">4 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Проверка перед публикацией</div>
  <h2>5 вещей, которые <i>проверяешь</i> перед показом</h2>
  <div class="steps" style="margin-top:10px;gap:9px">
   <div class="step"><div class="n">1</div><div class="t" style="font-size:11.3pt">Синхронизация губ выглядит естественно на крупном плане лица.</div></div>
   <div class="step"><div class="n">2</div><div class="t" style="font-size:11.3pt">Перевод не исказил смысл и не тронул название бренда.</div></div>
   <div class="step"><div class="n">3</div><div class="t" style="font-size:11.3pt">Паузы и интонация соответствуют смыслу — не слишком быстро и не слишком медленно.</div></div>
   <div class="step"><div class="n">4</div><div class="t" style="font-size:11.3pt">Тестовый фрагмент (10-15 сек) проверен человеком, который знает целевой язык.</div></div>
   <div class="step"><div class="n">5</div><div class="t" style="font-size:11.3pt">Полный ролик пересмотрен в нескольких случайных местах, не только с начала.</div></div>
  </div>
 </div>
 <div class="retention">Готовый промпт для шага «адаптация»  →</div>
 {sig()}
</div>""")

# 5 — промпт AlovLab (копипаст, заменяет бизнес-слайд)
slides.append(f"""<div class="slide">
 <div class="badge">5 / 6</div>
 <div style="margin-top:72px">
  <div class="kicker">Копируй и используй</div>
  <h2>Промпт AlovLab<br><i>Локализация сценария</i></h2>
  <div class="promptbox">
   <div class="lbl">ChatGPT / Claude</div>
   <code>{LOC_PROMPT}</code>
  </div>
  <p class="sub">Используешь до того, как текст уйдёт в HeyGen или ElevenLabs — на шаге «адаптация текста» из пайплайна.</p>
 </div>
 <div class="retention">Что получаешь на выходе  →</div>
 {sig()}
</div>""")

# 6 — итог + один CTA
slides.append(f"""<div class="slide has-footer">
 <div class="badge">6 / 6</div>
 <div style="margin-top:72px">
  <h1 style="font-size:29pt">ОДИН СЦЕНАРИЙ<br><i>ЛЮБОЙ ЯЗЫК</i></h1>
  <p class="lead" style="margin-top:10px">Сценарий, записанный один раз, может звучать на рынке, где ты физически не был.</p>
  {langrow("Попробуй бесплатно", "Try it for free", "Pruébalo gratis")}
  <p class="illustrative">Иллюстративный пример, не результат реального проекта.</p>
  <div class="card sand" style="margin-top:12px">
   <div class="lbl">Забери промпт</div>
   <p>«Локализация сценария» — в Telegram, t.me/AlovLab, в закрепе.</p>
  </div>
 </div>
 {footer()}{sig()}
</div>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(slides)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "slides:", len(slides))
