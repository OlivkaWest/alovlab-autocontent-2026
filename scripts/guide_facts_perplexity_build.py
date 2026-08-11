# -*- coding: utf-8 -*-
"""AlovLab · методичка «Факты, а не вода» (Perplexity) — премиум-PDF, фикс A4-страницы.
Система эталона higgsfield-restaurant-reel v2: светлая основа для чтения, тёмные плашки
только под обложку/промпты, полный контроль пагинации, один экран — одна мысль.
Честность (§0): метод, а не факты. Нигде не вписываем выдуманные цифры — только ФОРМУ факта.
Запуск: python3 scripts/guide_facts_perplexity_build.py"""
import base64, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "exports" / "guides" / "facts-perplexity"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "facts-perplexity-guide.html"

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
IMGDIR = ROOT / "content/carousel-assets/day-09-perplexity/_res"
def IMG(n): return b64(IMGDIR / f"s{n}.jpg")
HERO   = IMG(1)  # рабочий стол: факты + источники
STEPS5 = IMG(7)  # 5 шагов на экране
DESK   = IMG(2)  # facts first not fluff — дисциплина фактов (чистая, без вшитых цифр)
EMPTY  = IMG(5)  # пустой Evidence
FLUFF  = IMG(4)  # буллшит-слова

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
h3 .n{color:var(--o)}
p{font-size:11pt;line-height:1.62;color:var(--body);margin:8px 0;max-width:64ch}
.lead{font-size:12pt;line-height:1.6;color:var(--muted);margin:6px 0 14px;max-width:60ch}
strong{color:var(--ink);font-weight:700}
.o{color:var(--o);font-weight:700}
ul{margin:8px 0 8px 2px;list-style:none}
ul li{position:relative;padding-left:20px;font-size:11pt;line-height:1.55;color:var(--body);margin:6px 0;max-width:62ch}
ul li::before{content:"";position:absolute;left:2px;top:8px;width:6px;height:6px;border-radius:50%;background:var(--o)}
.hr{height:1px;background:var(--line);margin:14px 0}
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
.scene{display:grid;grid-template-columns:52px 1fr auto;gap:14px;align-items:center;background:#fff;
 border:1px solid var(--line);border-radius:12px;padding:12px 15px;margin:9px 0}
.scene .sn{width:52px;height:52px;border-radius:12px;background:var(--o-tint);color:var(--o);display:grid;place-items:center;
 font-weight:800;font-size:16pt}
.scene .sh{font-weight:800;font-size:12pt;color:var(--ink);margin-bottom:2px}
.scene .sd{font-size:9.5pt;color:var(--muted);line-height:1.4}
.scene .sd b{color:var(--body)}
.scene .stag{font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);
 background:var(--o-tint);border-radius:20px;padding:5px 11px;white-space:nowrap}
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
.prompt .plbl .copy{font-weight:700;font-size:7.5pt;letter-spacing:.1em;text-transform:uppercase;color:#cbb39d}
.prompt code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:9.5pt;line-height:1.62;
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
.fix .r{background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 12px;font-size:9.3pt;line-height:1.4}
.fix .r b{color:var(--o)}.fix .r code{font-family:ui-monospace,Menlo,monospace;font-size:8.5pt;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a}
table{width:100%;border-collapse:separate;border-spacing:0;margin:12px 0;font-size:9.6pt;background:#fff;
 border:1px solid var(--line);border-radius:12px;overflow:hidden}
th{background:var(--ink);color:#fff;font-weight:800;text-transform:uppercase;letter-spacing:.05em;font-size:7.8pt;
 text-align:left;padding:10px 12px}
td{padding:10px 12px;border-top:1px solid var(--line2);color:var(--body);vertical-align:top;line-height:1.35}
td b,td strong{color:var(--ink)}
tr:nth-child(even) td{background:#fbf7f0}
.imgpair{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:12px 0}
.imgpair figure{border-radius:12px;overflow:hidden;border:1px solid var(--line);background:#fff}
.imgpair img{width:100%;height:150px;object-fit:cover;display:block}
.imgpair figcaption{font-size:8.5pt;color:var(--muted);padding:8px 11px;line-height:1.35}
.imgpair figcaption b{color:var(--ink)}
.note{font-size:9.5pt;color:var(--muted);line-height:1.5;font-style:italic;margin:8px 0;max-width:60ch}
.term{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:0 10px 10px 0;
 padding:10px 14px;margin:8px 0}
.term b{color:var(--ink)} .term span{color:var(--body);font-size:10pt;line-height:1.45}
"""

BRAND = f'<span class="brand"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></span>'
def page(section, num, inner, dark=False):
    if dark:
        return f'<section class="page page--dark">{inner}</section>'
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>Факты, а не вода · Perplexity</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

PAGES = []

# ---------- P1 · Обложка ----------
PAGES.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:url(data:image/jpeg;base64,{HERO}) center/cover;opacity:.6"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(19,16,10,.4),rgba(19,16,10,.2) 36%,rgba(19,16,10,.97) 84%)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд</div>
    <h1 style="font-weight:800;font-size:32pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:16ch">Факты, а не вода: как собрать проверенную фактуру через Perplexity</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:38ch">За 15 минут — лист из 7 фактов с источниками. Чтобы текст держался на цифрах и датах, а не на красивых словах.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">инструмент · Perplexity</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">метод · 5 шагов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">3 готовых промпта</span>
    </div>
  </div>
</section>""")

# ---------- P2 · Содержание ----------
toc = [
 ("01","Что мы соберём","03"),("02","Почему текст звучит пусто","04"),("03","Что считать фактом","05"),
 ("04","Что подготовить","06"),("05","Метод за 15 минут — 5 шагов","07"),("06","Формула запроса","08"),
 ("07","Промпт 1 · собрать факты","09"),("08","Промпт 2 · проверить и углубить","10"),
 ("09","Промпт 3 · под свой бизнес","11"),("10","Как проверить источник","12"),
 ("11","Отсев мусора","13"),("12","Из листа фактов — в текст","14"),
 ("13","Частые ошибки и чек-лист","15"),("14","Все промпты и маршрут","16"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:12px;padding:9px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:10pt;width:26px">{a}</span>'
               f'<span style="font-weight:600;font-size:11.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:10pt">{c}</span></div>' for a,b,c in toc)
PAGES.append(page("Содержание", 2, f"""
  <span class="kick">Содержание</span>
  <h1 class="title">Маршрут гайда</h1>
  <p class="lead">Четырнадцать шагов от пустого текста до листа проверенных фактов. Иди по порядку — каждый шаг опирается на предыдущий.</p>
  <div style="margin-top:6px">{rows}</div>
"""))

# ---------- P3 · Что мы соберём ----------
PAGES.append(page("Шаг 01 · Что мы соберём", 3, f"""
  <span class="kick">Шаг 01</span>
  <h2>Что мы соберём</h2>
  <p class="lead">Один рабочий лист: семь проверенных фактов по твоей теме. Каждый — в жёсткой форме: факт → цифра → источник → год. Из такого листа текст пишется сам.</p>
  <div class="flow">
    <div class="node"><b>Тема</b><span>узкая</span></div><div class="arr">→</div>
    <div class="node"><b>Запрос</b><span>Perplexity</span></div><div class="arr">→</div>
    <div class="node"><b>Проверка</b><span>источник</span></div><div class="arr">→</div>
    <div class="node"><b>Отсев</b><span>мусор</span></div><div class="arr">→</div>
    <div class="node"><b>Лист</b><span>7 фактов</span></div><div class="arr">→</div>
    <div class="node"><b>Текст</b><span>на фактуре</span></div>
  </div>
  <div class="cards c3">
    <div class="card"><div class="ct">Инструмент</div><div class="ch">Perplexity</div><p>Поисковик-ассистент: отвечает и сразу даёт ссылки на источники.</p></div>
    <div class="card"><div class="ct">Время</div><div class="ch">15 минут</div><p>Один заход: запрос, проверка, чистка, лист.</p></div>
    <div class="card"><div class="ct">Результат</div><div class="ch">Лист фактуры</div><p>7 фактов с источником и датой — под пост, рилс, продающий текст.</p></div>
  </div>
  <h3>Три слова, которые нужны сегодня</h3>
  <div class="term"><b>Факт</b> — <span>проверяемое утверждение с цифрой, источником и датой. Не мнение, не прогноз, не оценка.</span></div>
  <div class="term"><b>Источник</b> — <span>откуда взята цифра: исследование, отчёт, официальная статистика. У факта всегда есть адрес.</span></div>
  <div class="term"><b>Первоисточник</b> — <span>тот, кто получил данные первым. Не пересказ в блоге, а сам отчёт или исследование.</span></div>
"""))

# ---------- P4 · Почему текст звучит пусто ----------
PAGES.append(page("Шаг 02 · Почему текст пуст", 4, f"""
  <span class="kick">Шаг 02</span>
  <h2>Почему текст звучит пусто</h2>
  <p class="lead">«Полезно», «эффективно», «качественно» — слова, которые подходят чему угодно. Дело не в слоге. Под текстом просто нет фактуры, и словам не на чём стоять.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Вода</div>«Нейросети сильно экономят время и заметно повышают эффективность бизнеса». Красиво — и ни о чём. Проверить нечего.</div>
    <div class="box good"><div class="lbl">✓ Фактура</div>«[Инструмент] сокращает [задачу] с [было] до [стало] — [источник], [год]». Конкретно и проверяемо.</div>
  </div>
  <div class="imgpair">
    <figure><img src="data:image/jpeg;base64,{FLUFF}"><figcaption><b>Общие слова.</b> «Инновационный», «синергия», «трансформация» — подходят любому.</figcaption></figure>
    <figure><img src="data:image/jpeg;base64,{EMPTY}"><figcaption><b>Пустой раздел «доказательства».</b> Резюме есть — источников нет.</figcaption></figure>
  </div>
  <p>Проверка на воду простая: попробуй <strong>удалить предложение</strong>. Если смысл не изменился — это была вода. Факт удалить нельзя: он несёт цифру, без которой мысль рушится.</p>
"""))

# ---------- P5 · Что считать фактом ----------
PAGES.append(page("Шаг 03 · Что считать фактом", 5, f"""
  <span class="kick">Шаг 03</span>
  <h2>Что считать фактом</h2>
  <p class="lead">Факт всегда конкретен и проверяем. Если у утверждения нет источника — это не факт, а мнение. Пустое место честнее выдуманной цифры.</p>
  <div class="prompt">
    <div class="plbl"><span class="tag">Форма факта · шаблон</span></div>
    <code>[что] изменилось на [цифра]
за [срок] — [источник], [год].</code>
    <div class="ru"><b>Правило:</b> нет цифры или источника — факт не готов. Не выдумывай число, чтобы «закрыть» строку. Лучше оставить пусто и добрать позже.</div>
  </div>
  <div class="mns">
    <div class="m move"><div class="h">✓ Это факт</div><p>Цифра из отчёта, официальная статистика, результат исследования с датой и автором.</p></div>
    <div class="m stay"><div class="h">✕ Это не факт</div><p>Мнение эксперта, прогноз «к 2030 будет», «многие считают», рекламное обещание бренда.</p></div>
  </div>
  <div class="callout result"><div class="h">Зачем так строго</div><p>Один проверяемый факт весит больше десяти эпитетов. Он останавливает пролистывание и даёт словам опору. На нём строится доверие.</p></div>
"""))

# ---------- P6 · Что подготовить ----------
PAGES.append(page("Шаг 04 · Что подготовить", 6, f"""
  <span class="kick">Шаг 04</span>
  <h2>Что подготовить заранее</h2>
  <p class="lead">Перед тем как открыть Perplexity, реши три вещи. Иначе получишь общий пересказ вместо фактуры под свою задачу.</p>
  <div class="cards c3">
    <div class="card"><div class="ct">Тема</div><div class="ch">Узкая</div><p>«ИИ в поддержке клиентов», а не «ИИ вообще». Узкая тема даёт точные цифры.</p></div>
    <div class="card"><div class="ct">Задача</div><div class="ch">Под что факты</div><p>Пост, рилс, продающий текст — от этого зависит, какие цифры искать.</p></div>
    <div class="card"><div class="ct">Формат</div><div class="ch">Лист фактуры</div><p>Куда складываешь: факт, цифра, источник, год — в столбик.</p></div>
  </div>
  <h3>Бланк листа фактуры</h3>
  <div class="prompt" style="padding:14px 16px">
    <div class="plbl"><span class="tag">Скопируй в тетрадь дня</span></div>
    <code>Тема: ______________________________

1. факт → цифра → источник → год
2. факт → цифра → источник → год
3. …  (до 7)</code>
  </div>
  <p class="note">Бланк на 7 фактов уже готов в тетради дня — ссылка в конце гайда. Заполняешь по ходу проверки, а не в конце по памяти.</p>
"""))

# ---------- P7 · Метод 5 шагов ----------
PAGES.append(page("Шаг 05 · Метод за 15 минут", 7, f"""
  <span class="kick">Шаг 05</span>
  <h2>Метод за 15 минут — 5 шагов</h2>
  <p class="lead">Один заход в Perplexity. Не пытайся собрать всё одним вопросом — идёшь по шагам, и на выходе лист, а не каша.</p>
  <div class="steps">
    <div class="step"><div class="sx"><b>Сузь тему.</b> «X для Y», а не «про X вообще». Чем уже — тем конкретнее цифры.</div></div>
    <div class="step"><div class="sx"><b>Проси факты и цифры</b> — и сразу со ссылкой на источник в ответе.</div></div>
    <div class="step"><div class="sx"><b>Проверь источник.</b> Кто, когда, официальный ли, не реклама ли. Открой первоисточник.</div></div>
    <div class="step"><div class="sx"><b>Отсей мусор.</b> Старьё, «одна статья», мнения без данных, рекламные цифры — вон.</div></div>
    <div class="step"><div class="sx"><b>Вынеси в лист.</b> Факт → цифра → источник → год. До семи строк — хватит на любой текст.</div></div>
  </div>
  <div class="callout result"><div class="h">Что должно получиться</div><p>Лист из 5–7 фактов, каждый с адресом. Открываешь его — и пишешь пост за десять минут, потому что спорить не с чем: под каждой мыслью цифра.</p></div>
"""))

# ---------- P8 · Формула запроса ----------
PAGES.append(page("Шаг 06 · Формула запроса", 8, f"""
  <span class="kick">Шаг 06</span>
  <h2>Формула запроса</h2>
  <p class="lead">Собирай запрос по частям — так Perplexity понимает, что искать, в каком виде отдать и что выкинуть.</p>
  <div class="prompt">
    <div class="plbl"><span class="tag">Формула</span></div>
    <code>[сколько фактов] + [узкая тема] + [требование источника] + [жёсткий формат] + [что исключить]</code>
  </div>
  <div class="cards c2">
    <div class="card"><div class="ct">Сколько</div><div class="ch">Собери 7 фактов</div><p>Число задаёт объём и не даёт растечься.</p></div>
    <div class="card"><div class="ct">Тема</div><div class="ch">по теме: [X для Y]</div><p>Узко — чтобы цифры были предметными.</p></div>
    <div class="card"><div class="ct">Источник</div><div class="ch">только со ссылкой + дата</div><p>Без адреса факт не принимаем.</p></div>
    <div class="card"><div class="ct">Формат</div><div class="ch">факт → цифра → источник → год</div><p>Готовая строка листа, не абзац.</p></div>
    <div class="card"><div class="ct">Приоритет</div><div class="ch">официальные данные</div><p>Отчёты и исследования выше блогов.</p></div>
    <div class="card"><div class="ct">Исключить</div><div class="ch">рекламу и мнения</div><p>Страховка от пустых обещаний.</p></div>
  </div>
  <p class="note">Дальше — три готовых промпта: собрать, проверить, адаптировать под бизнес. Копируй целиком и меняй только тему.</p>
"""))

# ---------- Промпт-страницы ----------
def prompt_page(step, num, section, title, lead, code, ru, ask, ban, err, ok):
    return page(section, num, f"""
  <span class="kick">{step}</span>
  <h2>{title}</h2>
  <p class="lead">{lead}</p>
  <div class="prompt">
    <div class="plbl"><span class="tag">Готовый промпт · скопировать в Perplexity</span></div>
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

PAGES.append(prompt_page("Шаг 07 · Промпт 1", 9, "Шаг 07 · Промпт «Собрать факты»", "Промпт 1 — собрать факты",
  "Базовый запрос. Даёт готовый лист фактуры по узкой теме — с источником и датой у каждого пункта.",
  "Собери 7 проверенных фактов по теме: [ТВОЯ ТЕМА].\nТолько с источниками (ссылка + дата). Приоритет —\nофициальные данные и исследования. Формат каждого:\nфакт → цифра → источник → год. Исключи рекламу и мнения.",
  "семь фактов по узкой теме, каждый со ссылкой и датой, приоритет официальным данным, жёсткий формат строки, без рекламы и мнений.",
  "цифру, ссылку, дату, официальный приоритет, формат строки.",
  "рекламу, прогнозы, оценочные слова, факты без источника.",
  "тема слишком широкая («про ИИ») — в ответе общие фразы вместо цифр.",
  "каждый пункт — с числом и рабочей ссылкой, тему видно с первой строки."))

PAGES.append(prompt_page("Шаг 08 · Промпт 2", 10, "Шаг 08 · Промпт «Проверить»", "Промпт 2 — проверить и углубить",
  "Когда факт понравился — прогони его через проверку. Промпт ищет первоисточник и показывает, где цифру могли исказить.",
  "Проверь факт: «[ВСТАВЬ ФАКТ С ЦИФРОЙ]».\nНайди первоисточник (кто и когда опубликовал).\nУточни: актуальна ли цифра, как считали, нет ли\nпротиворечащих данных. Если источник — реклама\nили пересказ, предупреди об этом.",
  "найди, кто первым опубликовал цифру и когда; проверь методику и свежесть; предупреди, если это реклама или пересказ.",
  "первоисточник, дату, методику, контр-данные.",
  "принимать блог-пересказ за первоисточник.",
  "берёшь цифру из первого же блога, не проверив, кто её посчитал.",
  "дошёл до отчёта-первоисточника и понял, за какой период цифра."))

PAGES.append(prompt_page("Шаг 09 · Промпт 3", 11, "Шаг 09 · Промпт «Под бизнес»", "Промпт 3 — под свой бизнес",
  "Тот же метод, но факты — под конкретную нишу. Подставь свою и получишь фактуру, которая работает на твою аудиторию.",
  "Собери 7 фактов, полезных для [НИША: эксперт /\nмагазин / услуга / локальный бизнес] по теме [ТЕМА].\nТолько с источником и датой. Формат:\nфакт → цифра → источник → год. Сначала — те,\nчто усиливают доверие клиента и снимают возражение.",
  "семь фактов под конкретную нишу и тему, с источником и датой, в приоритете — снимающие возражение клиента.",
  "привязку к нише, снятие возражений, источник, дату.",
  "общие факты «ни для кого», без пользы клиенту.",
  "берёшь факты, интересные тебе, а не полезные твоему клиенту.",
  "каждый факт закрывает конкретное «а докажите» от клиента."))

# ---------- P12 · Как проверить источник ----------
PAGES.append(page("Шаг 10 · Проверка источника", 12, f"""
  <span class="kick">Шаг 10</span>
  <h2>Как проверить источник</h2>
  <p class="lead">Perplexity даёт ссылки, но отвечаешь за факт ты. Тридцать секунд на источник — и ты не подставишься под «а где вы это взяли».</p>
  <div class="callout check"><div class="h">Четыре вопроса к любому источнику</div>
    <div class="row"><b>Кто?</b>&nbsp; Автор данных — исследование, ведомство, компания. Не аноним.</div>
    <div class="row"><b>Когда?</b>&nbsp; Есть дата. Свежесть важна: рынок ИИ устаревает за год.</div>
    <div class="row"><b>Официальный?</b>&nbsp; Первоисточник, а не пересказ пересказа в блоге.</div>
    <div class="row"><b>Не реклама?</b>&nbsp; Цифра не продаёт продукт того, кто её опубликовал.</div>
  </div>
  <h3>Проблема → что делать</h3>
  <div class="fix">
    <div class="r"><b>Ссылка на блог, а не отчёт.</b> Попроси первоисточник → <code>найди, кто опубликовал первым</code></div>
    <div class="r"><b>Нет даты.</b> Уточни период → <code>за какой год эта цифра</code></div>
    <div class="r"><b>Цифра от продавца решения.</b> Ищи независимую → <code>есть ли данные не от вендора</code></div>
    <div class="r"><b>Одна статья на весь интернет.</b> Проверь, повторяют ли → <code>кто ещё это подтверждает</code></div>
  </div>
"""))

# ---------- P13 · Отсев мусора ----------
PAGES.append(page("Шаг 11 · Отсев мусора", 13, f"""
  <span class="kick">Шаг 11</span>
  <h2>Отсев мусора</h2>
  <p class="lead">Половина «фактов» из выдачи — не факты. Убираешь их сразу, чтобы в лист попадало только то, за что не стыдно.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ В мусор</div>Прогнозы «к 2030 году», круглые цифры без источника, «эксперты считают», рекламные обещания, статья пятилетней давности про быстрый рынок.</div>
    <div class="box good"><div class="lbl">✓ В лист</div>Цифра из свежего отчёта, официальная статистика с датой, результат исследования с понятной методикой и автором.</div>
  </div>
  <div class="imgpair">
    <figure><img src="data:image/jpeg;base64,{DESK}"><figcaption><b>Дисциплина фактов.</b> Источники, даты, чек-лист проверки — «facts first, not fluff».</figcaption></figure>
    <figure><img src="data:image/jpeg;base64,{STEPS5}"><figcaption><b>Фильтры запроса.</b> Без мнений и прогнозов, только данные, свежий период.</figcaption></figure>
  </div>
  <p class="note">Пустой лист лучше листа с выдуманными цифрами. Если по теме честной фактуры мало — это тоже вывод: значит, тему берут на ощущениях, и твой честный текст будет сильнее.</p>
"""))

# ---------- P14 · Из листа в текст ----------
PAGES.append(page("Шаг 12 · Из фактов — в текст", 14, f"""
  <span class="kick">Шаг 12</span>
  <h2>Из листа фактов — в текст</h2>
  <p class="lead">Лист готов — текст пишется быстро. Один факт становится крючком, остальные держат мысль. Эпитеты больше не нужны: работает цифра.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Было (вода)</div>«Нейросети — это мощный инструмент, который открывает бизнесу огромные возможности и выводит работу на новый уровень».</div>
    <div class="box good"><div class="lbl">✓ Стало (на фактуре)</div>«[Факт с цифрой из листа]. Вот что это значит для твоей задачи — и что сделать уже сегодня».</div>
  </div>
  <h3>Как разложить лист по тексту</h3>
  <ul>
    <li><strong>Крючок</strong> — самый неожиданный факт. Цифра в первой строке останавливает пролистывание.</li>
    <li><strong>Тело</strong> — 2–3 факта, которые ведут мысль. Каждый снимает одно «а докажи».</li>
    <li><strong>Вывод</strong> — что читателю сделать. Без цифр здесь можно: их вес уже отработал выше.</li>
  </ul>
  <div class="callout result"><div class="h">Правило</div><p>Один текст — один-два сильных факта, не весь лист сразу. Остальное — в следующие посты. Лист из семи фактов кормит неделю контента.</p></div>
"""))

# ---------- P15 · Ошибки + чек-лист ----------
PAGES.append(page("Шаг 13 · Ошибки и чек-лист", 15, f"""
  <span class="kick">Шаг 13</span>
  <h2>Частые ошибки и чек-лист</h2>
  <p class="lead">Три ошибки убивают фактуру. Проверь лист по чек-листу перед тем, как писать текст.</p>
  <div class="fix">
    <div class="r"><b>Выдумал цифру,</b> чтобы «закрыть» строку. → Нет источника — нет факта. Оставь пусто.</div>
    <div class="r"><b>Взял пересказ за факт.</b> → Дойди до первоисточника, проверь дату и методику.</div>
    <div class="r"><b>Тема слишком широкая.</b> → Сузь до «X для Y» и переспроси — цифры станут предметными.</div>
  </div>
  <div class="callout check"><div class="h">Чек-лист листа фактуры</div>
    <div class="row">У каждого факта есть цифра, источник и год</div>
    <div class="row">Источники — первоисточники, а не пересказы</div>
    <div class="row">Нет прогнозов, мнений и рекламных обещаний</div>
    <div class="row">Цифры свежие, период указан</div>
    <div class="row">Ни одной выдуманной или «примерно такой» цифры</div>
    <div class="row">Факты полезны читателю, а не только интересны тебе</div>
  </div>
"""))

# ---------- P16 · Все промпты + контакты ----------
PAGES.append(f"""<section class="page page--dark" style="justify-content:space-between">
  <div>
    <div style="font-weight:800;font-size:9pt;letter-spacing:.15em;text-transform:uppercase;color:var(--o2);margin-bottom:10px">Шпаргалка</div>
    <h2 style="color:#fff;font-size:19pt;margin-bottom:4px">Три промпта — рядом</h2>
    <p style="color:#b9ad9b;font-size:10.5pt;line-height:1.5;margin-bottom:14px;max-width:60ch">Скопируй нужный, подставь свою тему, держи формат строки.</p>
    <div style="display:grid;gap:10px">
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">1 · Собрать факты</div><code style="font-family:ui-monospace,monospace;font-size:8.2pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">Собери 7 проверенных фактов по теме: [ТЕМА]. Только со ссылкой и датой. Приоритет — официальные данные. Формат: факт → цифра → источник → год. Без рекламы и мнений.</code></div>
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">2 · Проверить</div><code style="font-family:ui-monospace,monospace;font-size:8.2pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">Проверь факт: «[ФАКТ]». Найди первоисточник (кто и когда). Актуальна ли цифра, как считали, есть ли контр-данные. Если реклама или пересказ — предупреди.</code></div>
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">3 · Под бизнес</div><code style="font-family:ui-monospace,monospace;font-size:8.2pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">Собери 7 фактов для [НИША] по теме [ТЕМА]. Только с источником и датой. Формат: факт → цифра → источник → год. Сначала — снимающие возражение клиента.</code></div>
    </div>
  </div>
  <div style="text-align:center;border-top:1px solid rgba(255,255,255,.12);padding-top:18px">
    <img src="data:image/png;base64,{LOGO}" style="width:44px;height:44px;border-radius:11px">
    <div style="font-weight:800;font-size:14pt;color:#fff;margin:11px 0 5px">Собрал лист фактов — покажи. Застрял — приходи.</div>
    <div style="color:#b9ad9b;font-size:10pt;margin-bottom:14px">Бланк тетради дня, промпт дня и разборы — в Telegram.</div>
    <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
      <span style="font-weight:800;font-size:10pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:9px 15px;border-radius:9px">Telegram · t.me/AlovLab</span>
      <span style="font-weight:800;font-size:10pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:9px 15px;border-radius:9px">VK · vk.com/alovlab</span>
      <span style="font-weight:800;font-size:10pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:9px 15px;border-radius:9px">alovlab.ru</span>
    </div>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Факты, а не вода · Perplexity · AlovLab</title><style>{CSS}</style>' + "\n".join(PAGES)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(PAGES))
