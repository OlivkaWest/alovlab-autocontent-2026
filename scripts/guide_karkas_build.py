# -*- coding: utf-8 -*-
"""AlovLab · методичка «Каркас 2–5–15–30» (День 10) — премиум-PDF, фикс A4-страницы.
Система эталона v2. Тема: сценарий Reels проваливается не когда сложно снять, а когда
написан потоком. Метод — 5 зон, у каждой одна задача. Инструмент: Claude.
Честность (§0): результат в примере — формой, без выдуманных цифр.
Запуск: python3 scripts/guide_karkas_build.py"""
import base64, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "exports" / "guides" / "karkas-2-5-15-30"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "karkas-guide.html"

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")

RANGES = {"cyrillic":"U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin":"U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192"}
faces=""
for w in (400,500,600,700,800):
    for sub in ("cyrillic","latin"):
        fp = FONTS/f'manrope-{sub}-{w}.woff2'
        if fp.exists():
            faces+=("@font-face{font-family:'Manrope';font-weight:%d;font-display:swap;"
                    "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}\n"
                    % (w, b64(fp), RANGES[sub]))

CSS = faces + r"""
*{margin:0;padding:0;box-sizing:border-box}
:root{
 --paper:#FAF6EF; --ink:#1b1712; --body:#3a342c; --muted:#736858; --faint:#a99e8d;
 --o:#DA5F1E; --o2:#ff7a33; --o-tint:#fbeadf; --line:#e9e0d2; --line2:#efe8dc;
 --dark:#13100A; --dark2:#1c160d;
}
@page{ size:A4; margin:0; }
html,body{background:#d9d2c6}
body{font-family:'Manrope',system-ui,sans-serif;-webkit-font-smoothing:antialiased;color:var(--body)}
.page{position:relative;width:210mm;height:297mm;background:var(--paper);overflow:hidden;
 display:flex;flex-direction:column;padding:19mm 22mm 15mm;page-break-after:always}
.page:last-child{page-break-after:auto}
.page--dark{background:var(--dark);color:#f4efe6}
.ph{display:flex;justify-content:space-between;align-items:center;font-size:8.2pt;font-weight:700;
 letter-spacing:.08em;text-transform:uppercase;color:var(--faint);padding-bottom:7mm;margin-bottom:6mm;
 border-bottom:1px solid var(--line)}
.ph .brand{display:inline-flex;align-items:center;gap:6px;color:var(--muted)}
.ph .brand img{width:15px;height:15px;border-radius:4px}
.ph .brand b{color:var(--ink);font-weight:800}.ph .brand b i{color:var(--o);font-style:normal}
.pf{display:flex;justify-content:space-between;align-items:center;margin-top:auto;padding-top:6mm;
 border-top:1px solid var(--line);font-size:8.2pt;font-weight:700;letter-spacing:.06em;color:var(--faint)}
.pf .pnum b{color:var(--o)}
.main{flex:1;min-height:0}
.kick{font-weight:800;font-size:9pt;letter-spacing:.15em;text-transform:uppercase;color:var(--o);margin-bottom:9px}
h1.title{font-weight:800;font-size:27pt;line-height:1.08;letter-spacing:-.02em;color:var(--ink);margin-bottom:12px}
h2{font-weight:800;font-size:19pt;line-height:1.12;letter-spacing:-.015em;color:var(--ink);margin:0 0 6px}
h3{font-weight:800;font-size:13pt;color:var(--ink);margin:16px 0 7px}
p{font-size:11pt;line-height:1.62;color:var(--body);margin:8px 0;max-width:64ch}
.lead{font-size:12pt;line-height:1.6;color:var(--muted);margin:6px 0 14px;max-width:60ch}
strong{color:var(--ink);font-weight:700}
.o{color:var(--o);font-weight:700}
ul{margin:8px 0 8px 2px;list-style:none}
ul li{position:relative;padding-left:20px;font-size:11pt;line-height:1.55;color:var(--body);margin:6px 0;max-width:62ch}
ul li::before{content:"";position:absolute;left:2px;top:8px;width:6px;height:6px;border-radius:50%;background:var(--o)}
.flow{display:flex;align-items:stretch;gap:0;margin:14px 0;flex-wrap:wrap}
.flow .node{flex:1;min-width:0;background:#fff;border:1px solid var(--line);border-radius:11px;padding:12px 8px;text-align:center;
 display:flex;flex-direction:column;justify-content:center;gap:3px}
.flow .node b{font-weight:800;font-size:9.5pt;color:var(--ink);display:block;line-height:1.2}
.flow .node span{font-size:7.5pt;color:var(--muted);letter-spacing:.03em}
.flow .arr{display:flex;align-items:center;color:var(--o);font-weight:800;font-size:13pt;padding:0 5px}
.cards{display:grid;gap:11px;margin:12px 0}
.cards.c2{grid-template-columns:1fr 1fr}
.cards.c3{grid-template-columns:1fr 1fr 1fr}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:13px 15px}
.card .ct{font-weight:800;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;color:var(--o);margin-bottom:5px}
.card .ch{font-weight:800;font-size:11.5pt;color:var(--ink);line-height:1.2;margin-bottom:4px}
.card p{font-size:9.5pt;line-height:1.45;color:var(--muted);margin:2px 0;max-width:none}
.steps{counter-reset:st;display:grid;gap:9px;margin:12px 0}
.step{display:grid;grid-template-columns:30px 1fr;gap:12px;align-items:start}
.step::before{counter-increment:st;content:counter(st);width:30px;height:30px;border-radius:9px;background:var(--ink);
 color:#fff;font-weight:800;font-size:11pt;display:grid;place-items:center}
.step .sx{font-size:10.5pt;line-height:1.45;color:var(--body);padding-top:4px}
.step .sx b{color:var(--ink)}
.gb{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:12px 0}
.gb .box{border-radius:12px;padding:13px 15px;font-size:10pt;line-height:1.5}
.gb .good{background:#f0f6ee;border:1px solid #cfe3c6}
.gb .bad{background:#fbeeea;border:1px solid #f0cabb}
.gb .lbl{font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px;display:flex;align-items:center;gap:6px}
.gb .good .lbl{color:#3f7d34}.gb .bad .lbl{color:#c0492a}
.gb .box b{color:var(--ink)}
.prompt{background:var(--dark);border-radius:14px;padding:16px 18px;margin:12px 0;color:#f2eadf}
.prompt .plbl{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.prompt .plbl .tag{font-weight:800;font-size:8pt;letter-spacing:.12em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px}
.prompt code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:9.3pt;line-height:1.6;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.prompt .ru{font-size:9pt;line-height:1.45;color:#b9ad9b;margin-top:11px;padding-top:10px;border-top:1px solid rgba(255,255,255,.1)}
.prompt .ru b{color:#fff}
.mns{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:12px 0}
.mns .m{border:1px solid var(--line);border-radius:11px;padding:12px 14px;background:#fff}
.mns .m .h{font-weight:800;font-size:8.5pt;letter-spacing:.06em;text-transform:uppercase;margin-bottom:6px}
.mns .move .h{color:var(--o)} .mns .stay .h{color:var(--muted)}
.mns .m p{font-size:10pt;color:var(--body);line-height:1.4;margin:0;max-width:none}
.callout{border-radius:12px;padding:14px 16px;margin:12px 0}
.result{background:var(--o-tint);border:1px solid #f2d3bf}
.result .h{font-weight:800;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px}
.result p{font-size:10.5pt;color:var(--ink);margin:0;line-height:1.5;max-width:none}
.check{background:#fff;border:1px solid var(--line)}
.check .h{font-weight:800;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);margin-bottom:8px}
.check .row{display:flex;align-items:flex-start;gap:9px;font-size:10pt;line-height:1.4;color:var(--body);margin:6px 0}
.check .row::before{content:"";flex:0 0 auto;width:14px;height:14px;border-radius:4px;border:1.5px solid var(--o);
 background:var(--o-tint);margin-top:1px}
.fix{display:grid;grid-template-columns:1fr;gap:7px;margin:10px 0}
.fix .r{background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 12px;font-size:9.5pt;line-height:1.4}
.fix .r b{color:var(--o)}.fix .r code{font-family:ui-monospace,Menlo,monospace;font-size:8.5pt;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a}
table{width:100%;border-collapse:separate;border-spacing:0;margin:12px 0;font-size:9.8pt;background:#fff;
 border:1px solid var(--line);border-radius:12px;overflow:hidden}
th{background:var(--ink);color:#fff;font-weight:800;text-transform:uppercase;letter-spacing:.05em;font-size:7.8pt;
 text-align:left;padding:10px 12px}
td{padding:10px 12px;border-top:1px solid var(--line2);color:var(--body);vertical-align:top;line-height:1.35}
td b,td strong{color:var(--ink)}
tr:nth-child(even) td{background:#fbf7f0}
.note{font-size:9.5pt;color:var(--muted);line-height:1.5;font-style:italic;margin:8px 0;max-width:60ch}
.term{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:0 10px 10px 0;
 padding:10px 14px;margin:8px 0}
.term b{color:var(--ink)} .term span{color:var(--body);font-size:10pt;line-height:1.45}
/* мини-сценарий 2 колонки */
.scr{display:flex;flex-direction:column;gap:7px;margin:12px 0}
.scr .r{display:grid;grid-template-columns:64px 1fr;gap:12px;align-items:center;background:#fff;
 border:1px solid var(--line);border-radius:11px;padding:10px 14px}
.scr .r .z{font-weight:800;font-size:9.5pt;color:var(--o);font-variant-numeric:tabular-nums}
.scr .r .x{font-size:10pt;line-height:1.35;color:var(--body)}.scr .r .x b{color:var(--ink)}
/* бланк полей */
.fields{display:flex;flex-direction:column;gap:9px;margin:12px 0}
.fld{background:#fff;border:1px solid var(--line);border-radius:10px;padding:11px 14px}
.fld .l{font-weight:800;font-size:8.5pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o);margin-bottom:9px}
.fld .u{border-bottom:1px dashed var(--faint);height:13px;margin:7px 0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:9px}
/* таймлайн на обложке */
.tl{position:relative;margin-top:26px;height:2px;background:rgba(255,255,255,.18);border-radius:2px}
.tl .dot{position:absolute;top:50%;transform:translate(-50%,-50%);width:12px;height:12px;border-radius:50%;
 background:var(--o2);box-shadow:0 0 12px 2px rgba(255,138,51,.6)}
.tl .lab{position:absolute;top:16px;transform:translateX(-50%);font-weight:800;font-size:8.5pt;color:#e8dccb;font-variant-numeric:tabular-nums}
.tl .zon{position:absolute;top:-30px;transform:translateX(-50%);font-weight:800;font-size:8pt;letter-spacing:.06em;
 text-transform:uppercase;color:var(--o2)}
"""

BRAND = f'<span class="brand"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></span>'
def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>Каркас 2–5–15–30 · Reels</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt_page(step, num, section, title, lead, code, ru, ask, ban, err, ok):
    return page(section, num, f"""
  <span class="kick">{step}</span>
  <h2>{title}</h2>
  <p class="lead">{lead}</p>
  <div class="prompt">
    <div class="plbl"><span class="tag">Готовый промпт · скопировать в Claude</span></div>
    <code>{code}</code>
    <div class="ru"><b>По-русски:</b> {ru}</div>
  </div>
  <div class="mns">
    <div class="m move"><div class="h">▲ Что требуем</div><p>{ask}</p></div>
    <div class="m stay"><div class="h">■ Что запрещаем</div><p>{ban}</p></div>
  </div>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Главная ошибка</div>{err}</div>
    <div class="box good"><div class="lbl">✓ Удачно, если</div>{ok}</div>
  </div>
""")

PAGES = []

# ---------- P1 · Обложка ----------
tl_marks = [(0,"0",""),(14,"2",""),(24,"5",""),(66,"15",""),(100,"30","")]
tl_zones = [(7,"удар"),(19,"боль"),(45,"приём"),(83,"результат")]
dots="".join(f'<div class="dot" style="left:{x}%"></div><div class="lab" style="left:{x}%">{t}</div>' for x,t,_ in tl_marks)
zons="".join(f'<div class="zon" style="left:{x}%">{z}</div>' for x,z in tl_zones)
PAGES.append(f"""<section class="page page--dark" style="justify-content:space-between;padding:20mm 22mm">
  <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  <div>
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.06;letter-spacing:-.02em;color:#fff;max-width:17ch">Каркас 2–5–15–30: сценарий Reels, где ни одна секунда не провисает</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:38ch">За один заход в Claude — таблица по секундам: удар, боль, один приём, результат, шаг. Каркас, по которому можно встать и снять.</p>
    <div style="margin-top:30px;padding:0 6px 20px"><div class="tl">{dots}{zons}</div></div>
    <div style="margin-top:14px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">инструмент · Claude</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">метод · 5 зон</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">бланк · 2 колонки</span>
    </div>
  </div>
  <div></div>
</section>""")

# ---------- P2 · Содержание ----------
toc = [
 ("01","Что ты соберёшь","03"),("02","Почему поток проваливается","04"),("03","Каркас 2–5–15–30","05"),
 ("04","Две колонки","06"),("05","Собираем в Claude","07"),("06","Промпт 1 · основной","08"),
 ("07","Промпт 2 · улучшение","09"),("08","Промпт 3 · жёсткая оценка","10"),
 ("09","Промпт 4 · финальная проверка","11"),("10","Пример: риелтор","12"),
 ("11","Типовые ошибки","13"),("12","Бланк тетради","14"),
 ("13","Чек-лист готовности","15"),("14","Все промпты и маршрут","16"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:12px;padding:9px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:10pt;width:26px">{a}</span>'
               f'<span style="font-weight:600;font-size:11.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:10pt">{c}</span></div>' for a,b,c in toc)
PAGES.append(page("Содержание", 2, f"""
  <span class="kick">Содержание</span>
  <h1 class="title">Маршрут гайда</h1>
  <p class="lead">Четырнадцать шагов от угла до готового сценария по секундам. Иди по порядку — каждый шаг опирается на предыдущий.</p>
  <div style="margin-top:6px">{rows}</div>
"""))

# ---------- P3 ----------
PAGES.append(page("Шаг 01 · Что ты соберёшь", 3, f"""
  <span class="kick">Шаг 01</span>
  <h2>Что ты соберёшь</h2>
  <p class="lead">Сценарий Reels на 30 секунд — не абзац потоком, а таблица: слева что говоришь, справа что в кадре. У каждой секунды своя задача, и провисать нечему.</p>
  <div class="flow">
    <div class="node"><b>Угол</b><span>+ один приём</span></div><div class="arr">→</div>
    <div class="node"><b>5 зон</b><span>2–5–15–30</span></div><div class="arr">→</div>
    <div class="node"><b>Таблица</b><span>2 колонки</span></div><div class="arr">→</div>
    <div class="node"><b>Ролик</b><span>30 сек</span></div>
  </div>
  <div class="cards c3">
    <div class="card"><div class="ct">Формат</div><div class="ch">9:16, 30 сек</div><p>Вертикаль под Reels, VK Клипы, Shorts.</p></div>
    <div class="card"><div class="ct">Инструмент</div><div class="ch">Claude</div><p>Держит длинную инструкцию и отдаёт результат таблицей.</p></div>
    <div class="card"><div class="ct">Результат</div><div class="ch">Каркас-таблица</div><p>Сценарий, по которому можно встать и снять.</p></div>
  </div>
  <h3>Три слова, которые нужны сегодня</h3>
  <div class="term"><b>Каркас</b> — <span>жёсткая раскладка 30 секунд на зоны 2–5–15–30, у каждой одна задача. Противоположность «потоку».</span></div>
  <div class="term"><b>Зона</b> — <span>отрезок ленты с одной работой: удар, боль, приём, результат, шаг. Секунда без работы — вылетает.</span></div>
  <div class="term"><b>Удержание</b> — <span>сколько зрителей досматривают. Растёт, когда каждая секунда обещает больше прошлой.</span></div>
"""))

# ---------- P4 ----------
PAGES.append(page("Шаг 02 · Почему поток проваливается", 4, f"""
  <span class="kick">Шаг 02</span>
  <h2>Почему поток проваливается</h2>
  <p class="lead">Сценарий выматывает не когда сложно снять, а когда написан потоком. Ты пишешь, как говоришь: подряд. Начало бодрое, а к восьмой секунде — «ну и вот», «в общем».</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Поток</div>Решает одну задачу — донести твою мысль до конца. Зрителю всё равно, дошла ли она. Он уходит на середине.</div>
    <div class="box good"><div class="lbl">✓ Каркас</div>Даёт каждой секунде одну работу. Зритель остаётся, пока следующая секунда обещает больше прошлой.</div>
  </div>
  <p>Донести мысль и удержать зрителя — <strong>две разные задачи</strong>. Поток решает первую и проваливает вторую. Каркас решает именно вторую: у каждой секунды есть работа → нет пустых мест → зрителю всё время обещают следующее → он досматривает.</p>
  <div class="callout result"><div class="h">Коротко</div><p>Поток даёт складный текст. Каркас даёт досмотренный ролик. Нам нужен второй.</p></div>
"""))

# ---------- P5 ----------
PAGES.append(page("Шаг 03 · Каркас 2–5–15–30", 5, f"""
  <span class="kick">Шаг 03</span>
  <h2>Каркас 2–5–15–30</h2>
  <p class="lead">Одна тридцатисекундная лента, пять зон. У каждой ровно одна работа. Держи их перед глазами, когда раскладываешь свой угол.</p>
  <table>
    <tr><th style="width:78px">Зона</th><th>Задача — что должна сделать</th></tr>
    <tr><td><b>0–2 · удар</b></td><td>Одна фраза или кадр, после которого нельзя пролистнуть. Без «привет, друзья». Первое слово уже работает. <b>Остановить палец.</b></td></tr>
    <tr><td><b>2–5 · боль</b></td><td>Назови проблему зрителя конкретно, его словами. Он должен подумать «это про меня». <b>Удержать после удара.</b></td></tr>
    <tr><td><b>5–15 · приём</b></td><td>Ровно один. Не рассказать, а показать: действие в кадре плюс короткая реплика. <b>Дать пользу здесь и сейчас.</b></td></tr>
    <tr><td><b>15–30 · итог</b></td><td>Что меняется, если применить приём: во времени, в деньгах, в результате. <b>Показать, ради чего досматривать.</b></td></tr>
    <tr><td><b>финал · CTA</b></td><td>Одна строка, спокойно. В Telegram за конкретным — тетрадь, промпт, чек-лист. <b>Перевести внимание в шаг.</b></td></tr>
  </table>
  <div class="callout result"><div class="h">Правило</div><p>У каждой зоны — ровно одна работа. Делает две — раздели на две секунды. Не делает ни одной — вычеркни.</p></div>
"""))

# ---------- P6 ----------
PAGES.append(page("Шаг 04 · Две колонки", 6, f"""
  <span class="kick">Шаг 04</span>
  <h2>Две колонки, а не строчка</h2>
  <p class="lead">Сценарий пишется не потоком, а в две колонки. Это и есть защита от провисания.</p>
  <div class="cards c2">
    <div class="card"><div class="ct">Колонка 1</div><div class="ch">Что говорю</div><p>Закадровый голос или реплика в кадр. Коротко, как в жизни.</p></div>
    <div class="card"><div class="ct">Колонка 2</div><div class="ch">Что в кадре</div><p>Действие и текст на экране: что зритель видит в эту секунду.</p></div>
  </div>
  <p>Поток забывает про картинку и превращается в говорящую голову — а её листают. Как только рядом с каждой репликой стоит «что в кадре», ты вынужден показывать, а не пересказывать.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Пустая правая колонка</div>«Говорит на камеру» — сигнал, что секунда провиснет: глазу нечего дать.</div>
    <div class="box good"><div class="lbl">✓ Заполненная</div>Конкретное действие или текст на экране. Нет кадра — режь секунду.</div>
  </div>
"""))

# ---------- P7 ----------
PAGES.append(page("Шаг 05 · Собираем в Claude", 7, f"""
  <span class="kick">Шаг 05</span>
  <h2>Собираем сценарий в Claude</h2>
  <p class="lead">Везде — что открыть, что вставить, что проверить. Ни одного «настрой инструмент».</p>
  <div class="steps">
    <div class="step"><div class="sx"><b>Возьми угол и приём.</b> Впиши угол, который выбрал раньше, и один приём, который покажешь.</div></div>
    <div class="step"><div class="sx"><b>Открой Claude</b> (claude.ai) или ChatGPT, новый чат.</div></div>
    <div class="step"><div class="sx"><b>Вставь основной промпт</b> (шаг 06), подставь нишу, аудиторию, угол, приём, продукт.</div></div>
    <div class="step"><div class="sx"><b>Проверь границы зон.</b> Удар в 0–2? В 5–15 ровно один приём? Второй — вычеркни.</div></div>
    <div class="step"><div class="sx"><b>Заполни правую колонку до конца.</b> Ни одной пустой клетки «что в кадре».</div></div>
    <div class="step"><div class="sx"><b>Прогони через оценку и проверку</b> (шаги 08–09) — исправь ту секунду, где зритель уходит.</div></div>
  </div>
  <div class="callout result"><div class="h">Что забрать</div><p>Сценарий-таблицу 0–2 / 2–5 / 5–15 / 15–30 / финал + понимание, где он провисал и как ты это починил.</p></div>
"""))

# ---------- P8–P11 · Промпты ----------
PAGES.append(prompt_page("Шаг 06 · Промпт 1", 8, "Шаг 06 · Промпт «Основной»", "Промпт 1 — собрать по секундам",
  "Базовый запрос. Раскладывает твой угол и приём на сценарий по каркасу — таблицей в две колонки.",
  "Ты — сценарист коротких видео. Собери сценарий Reels\nна 30 сек по каркасу. Ниша: [X]. Аудитория: [Y].\nПродукт: [P]. Угол: [Z]. Приём: [один].\nЗоны: 0–2 удар · 2–5 боль · 5–15 один приём ·\n15–30 результат (без выдуманных цифр) · финал CTA\nв Telegram. Отдай таблицей: таймкод | что говорю |\nчто в кадре. Один приём, ни одной пустой правой клетки.",
  "собери сценарий на 30 сек по зонам 2–5–15–30, ровно один приём, результат без выдуманных цифр — таблицей в две колонки.",
  "жёсткие зоны, один приём, таблицу в две колонки, живой русский, результат без выдуманных цифр.",
  "приветствие и разгон в 0–2, больше одного приёма, пустую колонку «что в кадре».",
  "просишь «просто сценарий» без зон — Claude отдаёт поток, и середина провисает.",
  "на выходе таблица: удар в 0–2, ровно один приём в 5–15, правая колонка заполнена везде."))

PAGES.append(prompt_page("Шаг 07 · Промпт 2", 9, "Шаг 07 · Промпт «Улучшение»", "Промпт 2 — заострить и уплотнить",
  "Когда черновик готов — прогони его через усиление: острее удар, один приём, плотнее середина.",
  "Вот мой сценарий: [ВСТАВИТЬ]. Усиль его:\n— в 0–2 сделай удар острее, убери разгон и приветствие;\n— в 5–15 оставь ровно один приём, лишнее вычеркни;\n— найди секунду, где начинается провисание, уплотни;\n— заполни пустые клетки «что в кадре».\nПокажи таблицей: было / стало и что именно изменил.",
  "усиль черновик: острее удар, один приём, плотнее середина, заполни пустые кадры — и покажи было/стало.",
  "сравнение было/стало, острый удар, один приём, заполненную правую колонку.",
  "переписывать весь текст целиком вместо точечных правок.",
  "правишь на глаз и теряешь, что именно стало лучше.",
  "видишь было/стало по зонам и понимаешь, где стало плотнее."))

PAGES.append(prompt_page("Шаг 08 · Промпт 3", 10, "Шаг 08 · Промпт «Жёсткая оценка»", "Промпт 3 — где уходит зритель",
  "Пусть Claude сыграет редактора, который твой сценарий отклонит. Он назовёт секунду ухода — её и чинишь.",
  "Оцени мой сценарий строго, как редактор, который его\nотклонит. Назови конкретную секунду, на которой\nзритель уйдёт, и почему. Найди: где разгон вместо\nудара, где приёмов больше одного, где правая колонка\nпустая, где результат абстрактный. Дай оценку 1–10\nза удар и за удержание. Не хвали из вежливости.\nСценарий: [ВСТАВИТЬ].",
  "оцени строго как редактор: назови секунду ухода и причину, дай оценку 1–10, без вежливой похвалы.",
  "конкретную секунду ухода, причину, оценку 1–10, список слабых зон.",
  "вежливую похвалу и общие советы «в целом хорошо».",
  "правишь весь сценарий, хотя проседает одна секунда.",
  "точечно чинишь именно ту зону, которую назвал редактор."))

PAGES.append(prompt_page("Шаг 09 · Промпт 4", 11, "Шаг 09 · Промпт «Финальная проверка»", "Промпт 4 — да / нет по каркасу",
  "Последний прогон перед съёмкой. Ответы «да/нет» по каждому пункту каркаса — где «нет», ту зону переписываешь.",
  "Проверь сценарий по каркасу, ответь да/нет по каждому:\n— в 0–2 удар, а не приветствие, первое слово работает;\n— в 2–5 боль названа конкретно;\n— в 5–15 ровно один приём, показан в кадре;\n— в 15–30 результат конкретный, без выдуманных цифр;\n— финал — одна строка CTA в Telegram;\n— в каждой строке заполнена «что в кадре».\nГде «нет» — перепиши зону. Сценарий: [ВСТАВИТЬ].",
  "пройди сценарий по каркасу и ответь да/нет по каждому пункту; где «нет» — перепиши зону.",
  "чёткие да/нет по каждому пункту и переписанную зону там, где «нет».",
  "размытые ответы «скорее да» — нужен бинарный вердикт.",
  "считаешь сценарий готовым без построчной проверки.",
  "по всем пунктам «да», а спорные зоны переписаны и проверены снова."))

# ---------- P12 · Пример ----------
demo_rows = [
 ("0–2","<b>Квартиру показывают в солнце. Смотри в дождь.</b> — солнечное окно → серое мокрое стекло"),
 ("2–5","В сухую ты не увидишь ни один протёкший шов — палец по сухому углу, текст «сухо ≠ цело»"),
 ("5–15","Приди после дождя, проверь 3 места — крупно каждое, счётчик 1-2-3"),
 ("15–30","Пять минут в дождь — минус ремонт от сырости потом — кадр «до/после» состояния"),
 ("финал","Чек-лист «что смотреть» → тетрадь дня — логотип A, кнопка «Забрать»"),
]
scr="".join(f'<div class="r"><span class="z">{z}</span><span class="x">{x}</span></div>' for z,x in demo_rows)
PAGES.append(page("Шаг 10 · Пример: риелтор", 12, f"""
  <span class="kick">Шаг 10</span>
  <h2>Пример: риелтор, вторичка</h2>
  <p class="lead"><b>Угол:</b> «квартиру показывают в лучшем свете — правда вылезает потом». <b>Приём:</b> «повторный просмотр после дождя, проверь три места».</p>
  <div class="gb" style="grid-template-columns:1fr">
    <div class="box bad"><div class="lbl">✕ Поток</div>«Всем привет! Сегодня про то, как выбрать квартиру и не переплатить, это очень важная тема, давайте разберёмся…» — удар отсутствует, боль размазана, к пятой секунде зритель ушёл.</div>
  </div>
  <h3>Сильный вариант — каркас 2–5–15–30</h3>
  <div class="scr">{scr}</div>
  <p class="note">Результат в 15–30 — формой, без выдуманной суммы: в реальном ролике подставь свою цифру из практики, не придуманную.</p>
"""))

# ---------- P13 · Ошибки ----------
PAGES.append(page("Шаг 11 · Типовые ошибки", 13, f"""
  <span class="kick">Шаг 11</span>
  <h2>Типовые ошибки</h2>
  <p class="lead">Шесть ошибок топят удержание. Проверь свой сценарий по каждой.</p>
  <div class="fix">
    <div class="r"><b>Пишут потоком, а не по зонам.</b> → Сразу разложи на 2–5–15–30, каждой — одну задачу.</div>
    <div class="r"><b>Разгон вместо удара в 0–2.</b> → Вынеси острую фразу в первое слово, приветствие вырежи.</div>
    <div class="r"><b>Несколько приёмов в 5–15.</b> → Оставь один, показать в кадре; остальное — в другой ролик.</div>
    <div class="r"><b>Пустая правая колонка.</b> → К каждой реплике конкретный кадр; нет кадра — режь секунду.</div>
    <div class="r"><b>Результат в 15–30 абстрактный.</b> → Покажи конкретно: время, деньги, цифра из своей практики.</div>
    <div class="r"><b>CTA размазан.</b> → Одна строка, один шаг — в Telegram за тетрадью дня.</div>
  </div>
"""))

# ---------- P14 · Бланк ----------
def fld(l): return f'<div class="fld"><div class="l">{l}</div><div class="u"></div></div>'
def fld2(l): return f'<div class="fld"><div class="l">{l}</div><div class="u"></div><div class="u"></div></div>'
PAGES.append(page("Шаг 12 · Бланк тетради", 14, f"""
  <span class="kick">Шаг 12</span>
  <h2>Бланк: заполни свой</h2>
  <p class="lead">Впиши свой угол и разложи его по зонам в две колонки. Правая клетка не должна остаться пустой.</p>
  <div class="two">{fld("Моя ниша")}{fld("Аудитория")}</div>
  <div class="fields" style="margin-top:9px">
    {fld("Мой угол")}
    {fld("Мой приём (один)")}
  </div>
  <h3>Сценарий по зонам · что говорю / что в кадре</h3>
  <div class="fields">
    {fld2("0–2 · удар")}
    {fld2("2–5 · боль")}
    {fld2("5–15 · один приём")}
    {fld2("15–30 · результат")}
    {fld("финал · CTA в Telegram")}
  </div>
"""))

# ---------- P15 · Чек-лист ----------
PAGES.append(page("Шаг 13 · Чек-лист", 15, f"""
  <span class="kick">Шаг 13</span>
  <h2>Чек-лист готовности</h2>
  <p class="lead">Прогони финал по списку. Где «нет» — вернись к нужному шагу и перепиши зону.</p>
  <div class="callout check"><div class="h">Сценарий готов, если</div>
    <div class="row">Разложен на пять зон 2–5–15–30, не потоком</div>
    <div class="row">В 0–2 — удар, а не приветствие; первое слово работает</div>
    <div class="row">В 5–15 — ровно один приём, показан в кадре</div>
    <div class="row">Правая колонка «что в кадре» заполнена везде</div>
    <div class="row">Результат в 15–30 конкретный, без выдуманных цифр</div>
    <div class="row">CTA — одна строка, ведёт в Telegram за тетрадью</div>
    <div class="row">Ни одной пустой секунды: у каждой есть задача</div>
  </div>
  <div class="callout result"><div class="h">Итог дня</div><p>Ты больше не пишешь сценарий потоком. У тебя есть таблица по каркасу 2–5–15–30, по которой можно встать и снять.</p></div>
"""))

# ---------- P16 · Финал ----------
PAGES.append(f"""<section class="page page--dark" style="justify-content:space-between">
  <div>
    <div style="font-weight:800;font-size:9pt;letter-spacing:.15em;text-transform:uppercase;color:var(--o2);margin-bottom:10px">Шпаргалка</div>
    <h2 style="color:#fff;font-size:19pt;margin-bottom:4px">Четыре промпта — рядом</h2>
    <p style="color:#b9ad9b;font-size:10.5pt;line-height:1.5;margin-bottom:14px;max-width:60ch">Собрать → усилить → отклонить → проверить. Прогоняй сценарий по кругу, пока все «да».</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">1 · Собрать</div><code style="font-family:ui-monospace,monospace;font-size:8pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">Сценарий Reels на 30 сек по каркасу. Зоны 0–2/2–5/5–15/15–30/финал, один приём. Таблица: таймкод / что говорю / что в кадре.</code></div>
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">2 · Усилить</div><code style="font-family:ui-monospace,monospace;font-size:8pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">Острее удар в 0–2, один приём в 5–15, уплотни провисание, заполни пустые «что в кадре». Покажи было/стало.</code></div>
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">3 · Отклонить</div><code style="font-family:ui-monospace,monospace;font-size:8pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">Как редактор: назови секунду, где зритель уйдёт, и почему. Оценка 1–10 за удар и удержание. Без вежливости.</code></div>
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">4 · Проверить</div><code style="font-family:ui-monospace,monospace;font-size:8pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">Да/нет по каркасу: удар, боль, один приём, конкретный результат, CTA, заполнена «что в кадре». Где нет — перепиши.</code></div>
    </div>
  </div>
  <div style="text-align:center;border-top:1px solid rgba(255,255,255,.12);padding-top:18px">
    <img src="data:image/png;base64,{LOGO}" style="width:44px;height:44px;border-radius:11px">
    <div style="font-weight:800;font-size:14pt;color:#fff;margin:11px 0 5px">Собрал сценарий — сними. Застрял — приходи.</div>
    <div style="color:#b9ad9b;font-size:10pt;margin-bottom:14px">Бланк тетради дня, промпт дня и разборы — в Telegram.</div>
    <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
      <span style="font-weight:800;font-size:10pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:9px 15px;border-radius:9px">Telegram · t.me/AlovLab</span>
      <span style="font-weight:800;font-size:10pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:9px 15px;border-radius:9px">VK · vk.com/alovlab</span>
      <span style="font-weight:800;font-size:10pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:9px 15px;border-radius:9px">alovlab.ru</span>
    </div>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Каркас 2–5–15–30 · Reels · AlovLab</title><style>{CSS}</style>' + "\n".join(PAGES)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(PAGES))
