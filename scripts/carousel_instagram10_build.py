# -*- coding: utf-8 -*-
"""AlovLab · Карусель «Отдай свой Instagram ChatGPT» · master task 10/10.
Отдельная флагманская карусель (не привязана к одному дню календаря). 7 слайдов 1080x1350 (4:5).
Светлый премиум-инфографик (эталон day-claude-06-v2). Фото Ильи на слайдах 1 и 7 (identity lock,
реальный файл assets/img/ilya-alov.jpg, не AI-генерация — см. обоснование в carousel.md).
Без тире в текстах карусели — везде точка/двоеточие/скобка/стрелка.
Запуск:
  python3 scripts/carousel_instagram10_build.py
  NODE_PATH=/opt/node22/lib/node_modules node scripts/carousel_shoot.js <html> <outdir>
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "content" / "october-2026-system" / "carousels-extra" / "instagram-chatgpt-10"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "carousel.html"

def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
PORTRAIT = b64(ROOT / "assets" / "img" / "ilya-alov.jpg")

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
.portrait{width:112px;height:112px;border-radius:50%;object-fit:cover;object-position:50% 20%;border:3px solid #FFFFFF;box-shadow:0 4px 18px rgba(32,20,10,.14)}
.portrait.lg{width:168px;height:168px}
.badreq{font-size:9.8pt;font-weight:600;color:#9a9183;margin-top:10px;font-style:italic}
.badreq b{color:#b0564a;font-style:normal;font-weight:700}
h2.compact{font-size:21pt;margin-top:4px}
.promptbox.xs{padding:12px 15px;margin-top:8px}
.promptbox.xs .lbl{font-size:8.6pt;margin-bottom:6px}
.promptbox.xs code{font-size:9.3pt;line-height:1.42}
.rows{margin-top:9px;display:flex;flex-direction:column;gap:6px}
.rows .row{background:#FFFFFF;border:1px solid #EBE2D3;border-radius:10px;padding:8px 11px}
.rows .row b{display:block;font-size:8.3pt;font-weight:800;letter-spacing:.04em;color:#E1671E;text-transform:uppercase;margin-bottom:2px}
.rows .row span{font-size:9.6pt;font-weight:500;color:#3a362f;line-height:1.32;font-style:italic}
.rows.grid2{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.rows.grid2 .row{padding:9px 10px}
.rows.grid2 .row span{font-size:9pt;line-height:1.28}
.payoff{background:#1c1712;border-radius:12px;padding:10px 14px;margin-top:9px}
.payoff p{font-size:10pt;font-weight:600;color:#F2A65A;line-height:1.35}
.comment-note{font-size:8.8pt;font-weight:600;color:#9a9183;margin-top:6px}
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

N = 7
slides = []

# 1 — обложка / хук
slides.append(f"""<div class="slide">
 <div class="badge">1 / {N}</div>{brand_top()}
 <div style="margin-top:64px;display:flex;align-items:center;gap:14px">
  <img class="portrait" style="width:88px;height:88px" src="data:image/jpeg;base64,{PORTRAIT}">
  <div class="kicker">Нейромонах. Личный опыт.</div>
 </div>
 <h1 style="margin-top:14px;font-size:29pt;line-height:1.08">Я ПЕРЕСТАЛ ПРОСИТЬ CHATGPT<br><i>ПРИДУМАТЬ КОНТЕНТ.</i></h1>
 <p class="lead" style="margin-top:12px">Теперь он ведёт систему.</p>
 <p class="sub">Аудитория → контент → лид магнит → заявка.</p>
 <div class="retention" style="position:static;margin-top:28px">Смотри, как это работает по шагам  →</div>
 {sig()}
</div>""")

# 2 — проблема + честность про макросы
slides.append(f"""<div class="slide">
 <div class="badge">2 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Частая ошибка</div>
  <h2 class="compact">НЕ ПРОСИ ДАТЬ ИДЕИ.<br><i>ДАЙ СИСТЕМУ.</i></h2>
  <div class="card">
   <div class="lbl">Плохой запрос</div>
   <p>«Дай 30 идей для Reels.» «Составь контент план.» Ни контекста, ни аудитории, ни цели, ни пути до продажи.</p>
  </div>
  <div class="warn">
   <div class="lbl">Честно про команды</div>
   <p>/contentmix, /audiencemap, /leadidea, /funnelmap. Это не функции ChatGPT. Это макросы AlovLab: один раз настраиваешь ChatGPT, дальше команда запускает готовый сценарий.</p>
  </div>
  <div class="promptbox xs">
   <div class="lbl">Настройка (один раз)</div>
   <code>Дальше я буду писать короткие команды.
Каждая означает полный сценарий из этого чата. Выполняй по памяти, не переспрашивай заново.</code>
  </div>
  <p class="comment-note">Полный текст настройки и все 4 промпта одним файлом: в комментариях.</p>
 </div>
 <div class="retention">Первый макрос в деле  →</div>
 {sig()}
</div>""")

# 3 — /contentmix
slides.append(f"""<div class="slide">
 <div class="badge">3 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Макрос 1 · /contentmix</div>
  <h2 class="compact">ОДНА МЫСЛЬ.<br><i>ЧЕТЫРЕ ФОРМАТА.</i></h2>
  <p class="badreq">Плохой запрос: <b>«Дай идеи, что постить.»</b></p>
  <div class="promptbox xs">
   <div class="lbl">Промпт (сокращённо)</div>
   <code>Ты контент стратег. Мысль: [...] Ниша: [...] Аудитория: [...] Цель: [...]
Разложи на Reels, карусель, пост, Telegram. Для каждого: хук, угол, структура, CTA.</code>
  </div>
  <div class="rows grid2">
   <div class="row"><b>Reels</b><span>«Ты не ищешь новую тему. Ты ищешь свой угол в старой.»</span></div>
   <div class="row"><b>Карусель</b><span>«5 тем, которые ты уже знаешь, просто не считал их контентом»</span></div>
   <div class="row"><b>Пост</b><span>«Почему я месяц думал, что мне нечего сказать»</span></div>
   <div class="row"><b>Telegram</b><span>«Как один вопрос от подписчика стал темой на неделю»</span></div>
  </div>
 </div>
 <div class="retention">Один промпт сильнее тридцати идей  →</div>
 {sig()}
</div>""")

# 4 — /audiencemap
slides.append(f"""<div class="slide">
 <div class="badge">4 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Макрос 2 · /audiencemap</div>
  <h2 class="compact">ПЕРЕСТАНЬ УГАДЫВАТЬ,<br><i>ЧТО НУЖНО ЛЮДЯМ</i></h2>
  <p class="badreq">Плохой запрос: <b>«Какой контент зайдёт моей аудитории?»</b></p>
  <div class="promptbox xs">
   <div class="lbl">Промпт (сокращённо)</div>
   <code>Ты исследователь аудитории. Ниша: [...] Продукт: [...]
Материалы (комментарии, вопросы, отзывы): [...]
Не придумывай факты, которых нет во входных данных. Собери: проблемы, желания, вопросы, возражения.</code>
  </div>
  <div class="rows">
   <div class="row"><b>Проблема словами клиента</b><span>«Не знаю, с чего начать пост.»</span></div>
   <div class="row"><b>Скрытый смысл</b><span>Боится, что его контент никому не будет интересен.</span></div>
   <div class="row"><b>Тема и формат</b><span>«3 признака, что тебе есть что сказать» (карусель + личный пример)</span></div>
  </div>
  <p class="illustrative">Демонстрационный пример логики анализа, не разбор реальных сообщений клиентов AlovLab.</p>
 </div>
 <div class="retention">Дальше: лид магнит, который реально берут  →</div>
 {sig()}
</div>""")

# 5 — /leadidea
slides.append(f"""<div class="slide">
 <div class="badge">5 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Макрос 3 · /leadidea</div>
  <h2 class="compact">НЕ ДЕЛАЙ ЛИД МАГНИТ<br><i>РАДИ ЛИД МАГНИТА</i></h2>
  <p class="badreq">Плохой запрос: <b>«Придумай лид магнит для моей аудитории.»</b></p>
  <div class="promptbox xs">
   <div class="lbl">Промпт (сокращённо)</div>
   <code>Ты продуктовый маркетолог. Аудитория: [...] Проблема: [...] Продукт: [...]
7 лид магнитов с маленьким реальным результатом за 5 до 20 минут. Не абстрактные PDF вроде «10 секретов».</code>
  </div>
  <div class="rows">
   <div class="row"><b>Проблема</b><span>«Не знаю, что публиковать.»</span></div>
   <div class="row"><b>Слабый магнит</b><span>«50 идей для постов.»</span></div>
   <div class="row"><b>Сильный магнит</b><span>«Матрица из 4 рубрик, которая собирает план недели за 10 минут.»</span></div>
  </div>
  <p class="comment-note">Полный промпт: в комментариях.</p>
 </div>
 <div class="retention">Дальше: куда всё это ведёт  →</div>
 {sig()}
</div>""")

# 6 — /funnelmap
slides.append(f"""<div class="slide">
 <div class="badge">6 / {N}</div>{brand_top()}
 <div style="margin-top:72px">
  <div class="kicker">Макрос 4 · /funnelmap</div>
  <h2 class="compact">КОНТЕНТ ДОЛЖЕН<br><i>КУДА ТО ВЕСТИ</i></h2>
  <p class="badreq">Плохой запрос: <b>«Как мне продавать через контент?»</b></p>
  <div class="promptbox xs">
   <div class="lbl">Промпт (сокращённо)</div>
   <code>Ты маркетолог воронок. Продукт: [...] Цена: [...] Площадка: [...] Лид магнит: [...] Целевое действие: [...]
Путь: контент, подписка, лид магнит, прогрев, предложение, заявка. Найди, где человек теряется.</code>
  </div>
  <div class="payoff"><p>Reels → карусель с методом → гайд → 3 полезных сообщения → кейс → приглашение</p></div>
  <p class="note">Тогда контент перестаёт жить отдельно от бизнеса.</p>
 </div>
 <div class="retention">Собираем всё вместе  →</div>
 {sig()}
</div>""")

# 7 — итог + CTA
slides.append(f"""<div class="slide">
 <div class="badge">7 / {N}</div>{brand_top()}
 <div style="margin-top:60px">
  <img class="portrait" style="width:100px;height:100px" src="data:image/jpeg;base64,{PORTRAIT}">
 </div>
 <h1 style="margin-top:14px;font-size:27pt">CHATGPT НЕ ДОЛЖЕН<br>ПИСАТЬ ЗА ТЕБЯ.</h1>
 <p class="lead" style="margin-top:8px"><i style="font-style:normal;color:#E1671E;font-weight:800">Он должен работать по твоей системе.</i></p>
 <p class="sub" style="margin-top:6px">Контент → внимание. Аудитория → темы. Лид магнит → контакт. Воронка → заявка.</p>
 <div class="card sand" style="margin-top:16px">
  <div class="lbl">Забирай всё одним файлом</div>
  <p>4 промпта и настройка макросов. Напиши в комментариях: НЕЙРО.</p>
 </div>
 {sig()}
</div>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(slides)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "slides:", len(slides))
