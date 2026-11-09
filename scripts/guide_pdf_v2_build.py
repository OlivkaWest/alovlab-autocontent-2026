# -*- coding: utf-8 -*-
"""AlovLab · методичка Higgsfield v2 — премиальная вёрстка с фиксированными A4-страницами.
Светлая основа для чтения, тёмные плашки только под обложку и промпты. Полный контроль пагинации."""
import base64, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OUTDIR = ROOT / "exports" / "higgsfield-guide" / "v2-redesign"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "higgsfield-restaurant-reels-guide-v2.html"

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")
IMG = lambda n: b64(ROOT / "content/carousel-assets/restaurant" / n)
HERO      = IMG("hf_20260805_131843_164fe080-d862-4b73-a1b7-dbe6f4662e9f.png")  # гребешок+атмосфера
TRUFFLE   = IMG("hf_20260805_131843_27649360-b457-42af-a557-5abcdd8446fa.png")  # трюфель
HANDS     = IMG("hf_20260805_135919_ad8f388b-6f4b-4be6-b721-79a4cadc2983.png")  # руки шефа
INTERIOR  = IMG("hf_20260805_135919_7bbef46e-854d-4b41-b135-d37982262e6a.png")  # интерьер

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

/* колонтитулы */
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

/* типографика */
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

/* поток / схема */
.flow{display:flex;align-items:stretch;gap:0;margin:14px 0;flex-wrap:wrap}
.flow .node{flex:1;min-width:0;background:#fff;border:1px solid var(--line);border-radius:11px;padding:12px 8px;text-align:center;
 display:flex;flex-direction:column;justify-content:center;gap:3px}
.flow .node b{font-weight:800;font-size:9.5pt;color:var(--ink);display:block;line-height:1.2}
.flow .node span{font-size:7.5pt;color:var(--muted);letter-spacing:.03em}
.flow .arr{display:flex;align-items:center;color:var(--o);font-weight:800;font-size:13pt;padding:0 5px}

/* карточки */
.cards{display:grid;gap:11px;margin:12px 0}
.cards.c2{grid-template-columns:1fr 1fr}
.cards.c3{grid-template-columns:1fr 1fr 1fr}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:13px 15px}
.card .ct{font-weight:800;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;color:var(--o);margin-bottom:5px}
.card .ch{font-weight:800;font-size:11.5pt;color:var(--ink);line-height:1.2;margin-bottom:4px}
.card p{font-size:9.5pt;line-height:1.45;color:var(--muted);margin:2px 0;max-width:none}

/* сцена-карточка */
.scene{display:grid;grid-template-columns:52px 1fr auto;gap:14px;align-items:center;background:#fff;
 border:1px solid var(--line);border-radius:12px;padding:12px 15px;margin:9px 0}
.scene .sn{width:52px;height:52px;border-radius:12px;background:var(--o-tint);color:var(--o);display:grid;place-items:center;
 font-weight:800;font-size:16pt}
.scene .sh{font-weight:800;font-size:12pt;color:var(--ink);margin-bottom:2px}
.scene .sd{font-size:9.5pt;color:var(--muted);line-height:1.4}
.scene .sd b{color:var(--body)}
.scene .stag{font-weight:800;font-size:8pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);
 background:var(--o-tint);border-radius:20px;padding:5px 11px;white-space:nowrap}

/* step chips */
.steps{counter-reset:st;display:grid;gap:9px;margin:12px 0}
.step{display:grid;grid-template-columns:30px 1fr;gap:12px;align-items:start}
.step::before{counter-increment:st;content:counter(st);width:30px;height:30px;border-radius:9px;background:var(--ink);
 color:#fff;font-weight:800;font-size:11pt;display:grid;place-items:center}
.step .sx{font-size:10.5pt;line-height:1.45;color:var(--body);padding-top:4px}
.step .sx b{color:var(--ink)}

/* good / bad */
.gb{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:12px 0}
.gb .box{border-radius:12px;padding:13px 15px;font-size:10pt;line-height:1.5}
.gb .good{background:#f0f6ee;border:1px solid #cfe3c6}
.gb .bad{background:#fbeeea;border:1px solid #f0cabb}
.gb .lbl{font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px;display:flex;align-items:center;gap:6px}
.gb .good .lbl{color:#3f7d34}.gb .bad .lbl{color:#c0492a}
.gb .box b{color:var(--ink)}

/* тёмная плашка промпта */
.prompt{background:var(--dark);border-radius:14px;padding:16px 18px;margin:12px 0;color:#f2ead f;color:#f2eadf}
.prompt .plbl{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.prompt .plbl .tag{font-weight:800;font-size:8pt;letter-spacing:.12em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px}
.prompt .plbl .copy{font-weight:700;font-size:7.5pt;letter-spacing:.1em;text-transform:uppercase;color:#c9a; color:#cbb39d}
.prompt code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:9.5pt;line-height:1.62;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.prompt .ru{font-size:9pt;line-height:1.45;color:#b9ad9b;margin-top:11px;padding-top:10px;border-top:1px solid rgba(255,255,255,.1)}
.prompt .ru b{color:#fff}

/* мини-таблица разбора движется/стоит */
.mns{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:12px 0}
.mns .m{border:1px solid var(--line);border-radius:11px;padding:12px 14px;background:#fff}
.mns .m .h{font-weight:800;font-size:8.5pt;letter-spacing:.06em;text-transform:uppercase;margin-bottom:6px}
.mns .move .h{color:var(--o)} .mns .stay .h{color:var(--muted)}
.mns .m p{font-size:10pt;color:var(--body);line-height:1.4;margin:0;max-width:none}

/* врезки результата и проверки */
.callout{border-radius:12px;padding:14px 16px;margin:12px 0}
.result{background:var(--o-tint);border:1px solid #f2d3bf}
.result .h{font-weight:800;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px}
.result p{font-size:10.5pt;color:var(--ink);margin:0;line-height:1.5;max-width:none}
.check{background:#fff;border:1px solid var(--line)}
.check .h{font-weight:800;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);margin-bottom:8px}
.check .row{display:flex;align-items:flex-start;gap:9px;font-size:10pt;line-height:1.4;color:var(--body);margin:6px 0}
.check .row::before{content:"";flex:0 0 auto;width:14px;height:14px;border-radius:4px;border:1.5px solid var(--o);
 background:var(--o-tint);margin-top:1px}

/* «проблема→причина→решение» строки */
.fix{display:grid;grid-template-columns:1fr;gap:7px;margin:10px 0}
.fix .r{background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 12px;font-size:9.3pt;line-height:1.4}
.fix .r b{color:var(--o)}.fix .r code{font-family:ui-monospace,Menlo,monospace;font-size:8.5pt;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a}

/* таблица (компактно, но с воздухом) */
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

/* term */
.term{background:#fff;border:1px solid var(--line);border-left:3px solid var(--o);border-radius:0 10px 10px 0;
 padding:10px 14px;margin:8px 0}
.term b{color:var(--ink)} .term span{color:var(--body);font-size:10pt;line-height:1.45}
"""

BRAND = f'<span class="brand"><img src="data:image/png;base64,{LOGO}"><b>Alov<i>Lab</i></b></span>'
def page(section, num, inner, dark=False):
    cls = "page page--dark" if dark else "page"
    if dark:
        return f'<section class="{cls}">{inner}</section>'
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>Higgsfield · ресторанный Reels</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="{cls}">{header}<div class="main">{inner}</div>{footer}</section>'

PAGES = []

# ---------- P1 · Обложка ----------
PAGES.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:url(data:image/png;base64,{HERO}) center/cover;opacity:.62"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(19,16,10,.35),rgba(19,16,10,.15) 38%,rgba(19,16,10,.97) 86%)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд</div>
    <h1 style="font-weight:800;font-size:32pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Как собрать кинематографичный Reels ресторана в Higgsfield AI</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:36ch">Четыре кадра, AI-аватар и закадровый голос — от исходников до готового вертикального ролика.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">9:16 · вертикальный</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Image-to-Video</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">аватар Нейромонах</span>
    </div>
  </div>
</section>""")

# ---------- P2 · Содержание ----------
toc = [
 ("01","Что мы соберём","03"),("02","Что подготовить","04"),("03","Сценарная схема","05"),
 ("04","Готовим исходные кадры","06"),("05","Собираем первый клип","07"),("06","Формула промпта","08"),
 ("07","Промпт: гребешок","09"),("08","Промпт: руки шефа","10"),("09","Промпт: интерьер","11"),
 ("10","Промпт: трюфель + ограничения","12"),("11","Движение камеры и длительность","13"),
 ("12","Оценка клипа и частые ошибки","14"),("13","Аватар и сценарий","15"),
 ("14","Монтаж и субтитры","16"),("15","Экспорт и чек-лист","17"),("16","Все промпты и маршрут","18"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:12px;padding:9px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:10pt;width:26px">{a}</span>'
               f'<span style="font-weight:600;font-size:11.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:10pt">{c}</span></div>' for a,b,c in toc)
PAGES.append(page("Содержание", 2, f"""
  <span class="kick">Содержание</span>
  <h1 class="title">Маршрут гайда</h1>
  <p class="lead">Шестнадцать шагов от четырёх фотографий до готового ролика. Иди по порядку — каждый шаг опирается на предыдущий.</p>
  <div style="margin-top:6px">{rows}</div>
"""))

# ---------- P3 · Что мы соберём ----------
PAGES.append(page("Шаг 01 · Что мы соберём", 3, f"""
  <span class="kick">Шаг 01</span>
  <h2>Что мы соберём</h2>
  <p class="lead">Вертикальный рекламный ролик ресторана на 20–30 секунд. Пять сцен: аватар открывает и закрывает, между ними — ресторанный B-roll под голос.</p>
  <div class="flow">
    <div class="node"><b>4 фото</b><span>исходники</span></div><div class="arr">→</div>
    <div class="node"><b>4 клипа</b><span>Higgsfield</span></div><div class="arr">→</div>
    <div class="node"><b>Аватар</b><span>Нейромонах</span></div><div class="arr">→</div>
    <div class="node"><b>Голос</b><span>закадр</span></div><div class="arr">→</div>
    <div class="node"><b>Монтаж</b><span>+субтитры</span></div><div class="arr">→</div>
    <div class="node"><b>Reels</b><span>9:16</span></div>
  </div>
  <div class="cards c3">
    <div class="card"><div class="ct">Формат</div><div class="ch">9:16, 1080×1920</div><p>Вертикаль под Reels, VK Клипы, Shorts.</p></div>
    <div class="card"><div class="ct">Длительность</div><div class="ch">20–30 секунд</div><p>Короткие сцены по 2–4 сек.</p></div>
    <div class="card"><div class="ct">Роль Higgsfield</div><div class="ch">Оживить фото</div><p>Камера едет, пар вьётся — фото остаётся собой.</p></div>
  </div>
  <h3>Три слова, которые нужны сегодня</h3>
  <div class="term"><b>Image-to-Video</b> — <span>видео из одного фото. Загруженный кадр становится первым кадром клипа. Это наш режим.</span></div>
  <div class="term"><b>Camera Motion</b> — <span>движение камеры: приближение (push-in), проезд (dolly), поворот (pan).</span></div>
  <div class="term"><b>Исходный кадр</b> — <span>фото, которое ты загружаешь. От его качества зависит весь результат.</span></div>
"""))

# ---------- P4 · Что подготовить ----------
PAGES.append(page("Шаг 02 · Что подготовить", 4, f"""
  <span class="kick">Шаг 02</span>
  <h2>Что подготовить заранее</h2>
  <p class="lead">Собери всё до того, как откроешь Higgsfield. Тогда не будешь метаться между вкладками посреди работы.</p>
  <div class="cards c3">
    <div class="card"><div class="ct">Визуал</div><div class="ch">4 фотографии</div><p>Гребешок, руки шефа, интерьер, блюдо с трюфелем.</p></div>
    <div class="card"><div class="ct">Герой</div><div class="ch">Аватар</div><p>Образ Нейромонаха для вступления и финала.</p></div>
    <div class="card"><div class="ct">Смысл</div><div class="ch">Сценарий</div><p>Готовый текст — дам на шаге 13.</p></div>
    <div class="card"><div class="ct">Звук</div><div class="ch">Голос</div><p>Озвучка закадра, спокойная подача.</p></div>
    <div class="card"><div class="ct">Атмосфера</div><div class="ch">Музыка</div><p>Спокойная, кинематографичная, ниже голоса.</p></div>
    <div class="card"><div class="ct">Финал</div><div class="ch">Логотип PNG</div><p>Прозрачный фон, ставится только в конце.</p></div>
  </div>
  <h3>Папка проекта и имена файлов</h3>
  <div class="prompt" style="padding:14px 16px">
    <div class="plbl"><span class="tag">Структура папок</span></div>
    <code>restaurant_video/
  01_references/     02_higgsfield_generations/
  03_avatar/         04_voice/
  05_music/          06_logo/
  07_edit/           08_export/</code>
  </div>
  <p>Имена — по-человечески: <code style="font-family:ui-monospace,monospace;font-size:9.5pt;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">01_scallop_source.png</code>, не <span class="o">final2.png</span> или <span class="o">последний_точно.png</span>. Через час сам не вспомнишь, где что — а на монтаже будешь искать удачный дубль среди десяти безымянных файлов.</p>
"""))

# ---------- P5 · Сценарная схема ----------
def scene(n, tag, h, dur, who, emo):
    return (f'<div class="scene"><div class="sn">{n}</div><div><div class="sh">{h}</div>'
            f'<div class="sd"><b>{dur}</b> · {who} · <span style="color:var(--o)">{emo}</span></div></div>'
            f'<span class="stag">{tag}</span></div>')
PAGES.append(page("Шаг 03 · Сценарная схема", 5, f"""
  <span class="kick">Шаг 03</span>
  <h2>Пять сцен ролика</h2>
  <p class="lead">Каждая сцена — одна задача. Аватар держит внимание в начале и в конце, B-roll продаёт атмосферу в середине.</p>
  {scene('1','Аватар','Хук в кадре','2–4 сек','аватар говорит','остановить палец')}
  {scene('2','B-roll','Гребешок с паром','3–4 сек','закадр','разжечь аппетит')}
  {scene('3','B-roll','Руки шефа, подача','2–3 сек','закадр','показать заботу')}
  {scene('4','B-roll','Интерьер зала','3–4 сек','закадр','обещать вечер')}
  {scene('5','Финал','Трюфель + аватар + логотип','3–5 сек','аватар говорит','позвать за столик')}
  <div class="callout result" style="margin-top:14px"><div class="h">Что должно получиться</div><p>Ровный ритм: сильное лицо → вкусный B-roll → сильное лицо. Зритель досматривает и понимает, куда идти.</p></div>
"""))

# ---------- P6 · Готовим кадры ----------
PAGES.append(page("Шаг 04 · Исходные кадры", 6, f"""
  <span class="kick">Шаг 04</span>
  <h2>Готовим исходные кадры</h2>
  <p class="lead">Фото должно выглядеть как хороший первый кадр видео, а не как картинка для меню. Плохой исходник не спасёт ни один промпт.</p>
  <div class="gb">
    <div class="box good"><div class="lbl">✓ Хороший исходник</div>Вертикаль 9:16, объект целиком и в центре, тёплый боковой свет, тёмный фон, есть воздух сверху для пара и наезда камеры.</div>
    <div class="box bad"><div class="lbl">✕ Плохой исходник</div>Объект обрезан краем, каша по свету, текст на кадре, лишние пальцы, битая посуда, сильное размытие.</div>
  </div>
  <div class="imgpair">
    <figure><img src="data:image/png;base64,{HERO}"><figcaption><b>Гребешок.</b> Есть пар, соус блестит, сверху воздух под движение.</figcaption></figure>
    <figure><img src="data:image/png;base64,{INTERIOR}"><figcaption><b>Интерьер.</b> Глубина, свечи, боке — коридор для проезда камеры.</figcaption></figure>
  </div>
  <h3>Коротко по каждой сцене</h3>
  <ul>
    <li><strong>Гребешок:</strong> крупный план, виден соус, источник пара, место сверху под наезд.</li>
    <li><strong>Руки шефа:</strong> нормальные пальцы, тарелка почти на столе, движения будет мало.</li>
    <li><strong>Интерьер:</strong> свечи, столы, глубокая перспектива, тёплые лампы, боке.</li>
    <li><strong>Трюфель:</strong> крупный план, видна текстура, тёплый золотой блик.</li>
  </ul>
"""))

# ---------- P7 · Собираем клип ----------
PAGES.append(page("Шаг 05 · Первый клип", 7, f"""
  <span class="kick">Шаг 05</span>
  <h2>Собираем первый клип</h2>
  <p class="lead">Названия кнопок иногда меняются — держись логики. Сначала один тест, потом объём.</p>
  <div class="steps">
    <div class="step"><div class="sx"><b>Открой</b> раздел создания видео и выбери режим <b>Image-to-Video</b>.</div></div>
    <div class="step"><div class="sx"><b>Загрузи</b> исходный кадр и поставь вертикальный формат <b>9:16</b>.</div></div>
    <div class="step"><div class="sx"><b>Задай</b> короткую длительность (3–4 сек) и движение камеры.</div></div>
    <div class="step"><div class="sx"><b>Впиши</b> текстовый промпт (готовые — дальше).</div></div>
    <div class="step"><div class="sx"><b>Запусти</b> одну тестовую генерацию и досмотри её до конца.</div></div>
    <div class="step"><div class="sx"><b>Скачай</b> только удачный дубль. Повтори для остальных сцен.</div></div>
  </div>
  <div class="callout result"><div class="h">Главный принцип · один кадр — одно движение</div><p>Чем меньше просишь, тем меньше модель фантазирует.</p></div>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Так не надо</div>«Камера наезжает, облетает блюдо, шеф берёт тарелку, появляется огонь, меняется зал».</div>
    <div class="box good"><div class="lbl">✓ Так надо</div>«Медленный наезд. Пар плавно поднимается. Свет чуть меняется на соусе».</div>
  </div>
"""))

# ---------- P8 · Формула промпта ----------
PAGES.append(page("Шаг 06 · Формула промпта", 8, f"""
  <span class="kick">Шаг 06</span>
  <h2>Формула промпта</h2>
  <p class="lead">Собирай промпт по частям — так модель понимает, что двигать, а что держать на месте.</p>
  <div class="prompt">
    <div class="plbl"><span class="tag">Формула</span></div>
    <code>[объект] + [одно действие] + [движение камеры] + [движение среды] + [свет] + [стиль] + [ограничения]</code>
  </div>
  <div class="cards c2">
    <div class="card"><div class="ct">Объект</div><div class="ch">premium scallop dish</div><p>Прямо называем, что в кадре.</p></div>
    <div class="card"><div class="ct">Стабильность</div><div class="ch">remains intact</div><p>Приказ не менять еду.</p></div>
    <div class="card"><div class="ct">Камера</div><div class="ch">slow push-in</div><p>Одно спокойное движение.</p></div>
    <div class="card"><div class="ct">Среда</div><div class="ch">steam rises</div><p>Живёт фон, не сам объект.</p></div>
    <div class="card"><div class="ct">Свет</div><div class="ch">warm amber light</div><p>Задаёт ощущение «дорого».</p></div>
    <div class="card"><div class="ct">Ограничения</div><div class="ch">no deformation</div><p>Страховка от фантазий модели.</p></div>
  </div>
  <p class="note">Дальше — четыре готовых промпта. Каждый можно копировать целиком: объект, движение и ограничения уже собраны.</p>
"""))

# ---------- Промпт-страницы ----------
def prompt_page(step, num, section, title, lead, code, ru, move, stay, err, ok, img):
    return page(section, num, f"""
  <span class="kick">{step}</span>
  <h2>{title}</h2>
  <p class="lead">{lead}</p>
  <div class="prompt">
    <div class="plbl"><span class="tag">Готовый промпт · скопировать в Higgsfield</span></div>
    <code>{code}</code>
    <div class="ru"><b>По-русски:</b> {ru}</div>
  </div>
  <div class="mns">
    <div class="m move"><div class="h">▲ Двигается</div><p>{move}</p></div>
    <div class="m stay"><div class="h">■ Стоит на месте</div><p>{stay}</p></div>
  </div>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Главная ошибка</div>{err}</div>
    <div class="box good"><div class="lbl">✓ Удачно, если</div>{ok}</div>
  </div>
""")

PAGES.append(prompt_page("Шаг 07 · Промпт 1", 9, "Шаг 07 · Промпт «Гребешок»", "Промпт 1 — Гребешок",
  "Медленный наезд, живой пар, блики на соусе. Еда остаётся собой.",
  "A gourmet scallop dish stays completely stable while the camera makes a slow cinematic push-in. Delicate steam rises and gently curls upward. Soft warm amber side light glides across the glossy sauce. Dark elegant restaurant background, shallow depth of field, no deformation, no new ingredients.",
  "блюдо стабильно, камера медленно наезжает, пар вьётся вверх, тёплый свет скользит по соусу, тёмный премиум-фон.",
  "камера (push-in), пар, блик света.", "блюдо, тарелка, состав.",
  "просишь слишком быстрый наезд — гребешок «дышит» и плывёт.",
  "еда та же, пар живой, наезд плавный, соус блестит.", HERO))

PAGES.append(prompt_page("Шаг 08 · Промпт 2", 10, "Шаг 08 · Промпт «Руки шефа»", "Промпт 2 — Руки шефа",
  "Самая хрупкая сцена. Движение минимальное, иначе ломаются пальцы.",
  "A chef's hands slowly and gently place a finished plate onto the table. The hand movement is small and natural, fingers keep correct anatomy. The plate keeps its shape. The camera performs a very soft push-in. Warm light, realistic, no extra fingers, no additional hands, no changing dish.",
  "руки медленно и аккуратно ставят тарелку, движение мелкое, пальцы анатомичны, тарелка держит форму, лёгкий наезд.",
  "кисти (чуть), лёгкий push-in.", "тарелка, блюдо, вторая рука.",
  "большое движение руками — лишние пальцы и «резиновые» кисти.",
  "руки нормальные, тарелка встала мягко, блюдо не изменилось.", HANDS))

PAGES.append(prompt_page("Шаг 09 · Промпт 3", 11, "Шаг 09 · Промпт «Интерьер»", "Промпт 3 — Интерьер",
  "Здесь работает проезд камеры. Геометрия зала должна остаться на месте.",
  "An upscale restaurant interior at dusk. The camera performs a slow cinematic dolly forward. Candle flames flicker gently, warm bokeh lights shimmer softly. The room keeps its geometry, tables and chairs stay in place. Realistic, no people appearing, no morphing walls.",
  "зал на закате, камера медленно едет вперёд, пламя свечей дрожит, боке мерцает, геометрия сохраняется, мебель не двигается.",
  "камера (dolly), пламя, боке.", "стены, столы, стулья, перспектива.",
  "быстрый проезд — интерьер начинает «перестраиваться».",
  "едем плавно, зал стабилен, атмосфера тёплая и дорогая.", INTERIOR))

# ---------- P12 · Промпт 4 + ограничения ----------
PAGES.append(page("Шаг 10 · Промпт «Трюфель»", 12, f"""
  <span class="kick">Шаг 10 · Промпт 4</span>
  <h2>Промпт 4 — Трюфель + ограничения</h2>
  <p class="lead">Финальный герой. Золотой блик легко превращается в огонь — держим его мягким.</p>
  <div class="prompt">
    <div class="plbl"><span class="tag">Готовый промпт · скопировать в Higgsfield</span></div>
    <code>A luxury truffle dish stays perfectly stable while the camera makes a slow push-in. Steam softly curls upward. A warm golden highlight slowly travels along the rim of the plate. The truffle keeps its exact shape. Premium food commercial, no new ingredients, no deformation, no fire, no text.</code>
    <div class="ru"><b>По-русски:</b> трюфель стабилен, камера наезжает, пар вьётся, золотой блик едет по краю тарелки, форма сохраняется.</div>
  </div>
  <h3>Базовый блок ограничений (negative prompt)</h3>
  <div class="prompt" style="padding:14px 16px">
    <div class="plbl"><span class="tag">Negative — держи коротким</span></div>
    <code>no deformation, no morphing, no extra fingers, no additional hands, no changing ingredients, no floating objects, no sudden camera movement, no flickering, no text, no logo</code>
  </div>
  <p class="note">Длинный negative-список путает модель не хуже плохого фото. И помни: ограничения не чинят плохой исходник — сначала нормальный кадр, потом промпт.</p>
"""))

# ---------- P13 · Движение камеры + длительность ----------
PAGES.append(page("Шаг 11 · Камера и длительность", 13, f"""
  <span class="kick">Шаг 11</span>
  <h2>Движение камеры и длительность</h2>
  <p class="lead">Правило, которое спасает кредиты: чем сложнее кадр, тем спокойнее движение.</p>
  <table>
    <tr><th>Движение</th><th>Где использовать</th><th>Риск</th></tr>
    <tr><td><b>Push-in</b> — наезд</td><td>еда, финал</td><td>еда «дышит», если быстро</td></tr>
    <tr><td><b>Dolly</b> — проезд</td><td>интерьер</td><td>геометрия плывёт</td></tr>
    <tr><td><b>Pan</b> — поворот</td><td>панорама зала</td><td>смаз по краям</td></tr>
    <tr><td><b>Static</b> — почти стоит</td><td>сложные кадры</td><td>безопасно, но вяло</td></tr>
  </table>
  <h3>Длительность сцен</h3>
  <div class="cards c3">
    <div class="card"><div class="ct">Аватар · вступление</div><div class="ch">2–4 сек</div></div>
    <div class="card"><div class="ct">Гребешок</div><div class="ch">3–4 сек</div></div>
    <div class="card"><div class="ct">Руки шефа</div><div class="ch">2–3 сек</div></div>
    <div class="card"><div class="ct">Интерьер</div><div class="ch">3–4 сек</div></div>
    <div class="card"><div class="ct">Трюфель</div><div class="ch">3–4 сек</div></div>
    <div class="card"><div class="ct">Финал + логотип</div><div class="ch">3–5 сек</div></div>
  </div>
  <div class="callout result"><div class="h">Принцип настройки</div><p>Формат 9:16, короткая сцена, высокая стабильность, минимальное изменение исходника. Движение камеры важнее движения самого блюда.</p></div>
"""))

# ---------- P14 · Оценка + ошибки ----------
PAGES.append(page("Шаг 12 · Оценка и ошибки", 14, f"""
  <span class="kick">Шаг 12</span>
  <h2>Оценка клипа и частые ошибки</h2>
  <p class="lead">Красивый кадр с деформацией — это брак. На большом экране косяк вылезет.</p>
  <div class="callout check"><div class="h">Проверь себя перед тем, как оставить дубль</div>
    <div class="row">Объект сохранил форму, посуда не деформируется</div>
    <div class="row">Камера едет плавно, без скачков и мерцания</div>
    <div class="row">Пар выглядит паром, не дымом; свет не мигает</div>
    <div class="row">Руки анатомичны, фон не перестраивается</div>
    <div class="row">Клип реально встаёт в монтаж</div>
  </div>
  <h3>Проблема → решение (вписать в промпт)</h3>
  <div class="fix">
    <div class="r"><b>Блюдо плавится.</b> Убери сложное движение → <code>slow push-in, food stays stable</code></div>
    <div class="r"><b>Лишние пальцы.</b> Меньше движения рук → <code>small hand motion, no extra fingers</code></div>
    <div class="r"><b>Интерьер перестраивается.</b> Замедли проезд → <code>room keeps geometry</code></div>
    <div class="r"><b>Блик как огонь.</b> Смягчи свет → <code>soft warm highlight, no fire</code></div>
    <div class="r"><b>Появился текст.</b> Запрети явно → <code>no text, no captions</code></div>
  </div>
"""))

# ---------- P15 · Аватар + сценарий ----------
PAGES.append(page("Шаг 13 · Аватар и сценарий", 15, f"""
  <span class="kick">Шаг 13</span>
  <h2>Аватар и сценарий</h2>
  <p class="lead">Аватара генерь отдельно от ресторана. Сложный фон плюс живая речь — и модель ломает лицо.</p>
  <div class="cards c2">
    <div class="card"><div class="ct">Кадр аватара</div><div class="ch">Тёмный фон, крупный план</div><p>Янтарный контровой свет, взгляд в камеру, минимум жестов.</p></div>
    <div class="card"><div class="ct">Правило</div><div class="ch">Одна задача за раз</div><p>Простой кадр = стабильное лицо. Не вешай всё на одну генерацию.</p></div>
  </div>
  <h3>Готовый сценарий · 20–30 секунд</h3>
  <div class="cards" style="gap:9px">
    <div class="card"><div class="ct">Аватар · хук</div><p style="font-size:11pt;color:var(--ink);line-height:1.5">«В слабом ресторане тебе подают блюдо. В сильном — сначала меняют твой вечер».</p></div>
    <div class="card"><div class="ct">Закадр · поверх B-roll</div><p style="font-size:11pt;color:var(--ink);line-height:1.5">«Пар над тарелкой — это не еда. Это обещание. Свет, тишина, подача — вечер собирается до первого кусочка. Ты не заказываешь ужин. Ты бронируешь память».</p></div>
    <div class="card"><div class="ct">Аватар · финал</div><p style="font-size:11pt;color:var(--ink);line-height:1.5">«Хочешь такой вечер — стол уже ждёт. Бронь под роликом».</p></div>
  </div>
"""))

# ---------- P16 · Монтаж + субтитры ----------
PAGES.append(page("Шаг 14 · Монтаж и субтитры", 16, f"""
  <span class="kick">Шаг 14</span>
  <h2>Монтаж и субтитры</h2>
  <p class="lead">Движение уже внутри клипов. Задача монтажа — ритм и звук, а не эффекты.</p>
  <div class="flow" style="margin:10px 0">
    <div class="node"><b>Аватар</b><span>хук</span></div><div class="arr">→</div>
    <div class="node"><b>Гребешок</b></div><div class="arr">→</div>
    <div class="node"><b>Руки</b></div><div class="arr">→</div>
    <div class="node"><b>Интерьер</b></div><div class="arr">→</div>
    <div class="node"><b>Трюфель</b></div><div class="arr">→</div>
    <div class="node"><b>Аватар</b><span>+лого</span></div>
  </div>
  <ul>
    <li>Склейки — встык. <strong>Dissolve</strong> (плавное перетекание) только между двумя кадрами еды, чуть-чуть.</li>
    <li>Голос всегда громче музыки. Музыка спокойная, ниже речи.</li>
    <li>Звук слоями: шум зала, звон посуды, звук поставленной тарелки, тихий room tone.</li>
    <li>Пауза в полсекунды перед финальной фразой — пауза продаёт.</li>
  </ul>
  <h3>Субтитры</h3>
  <div class="cards c2">
    <div class="card"><div class="ct">Как</div><div class="ch">Крупно, снизу, 2 строки</div><p>Белый текст, мягкая тень, ключевое слово — оранжевым. Не перекрывают лицо и блюдо.</p></div>
    <div class="card"><div class="ct">Пример разбивки</div><div class="ch">«Ты бронируешь память»</div><p>Блок 1: «Ты не заказываешь ужин». Блок 2: «Ты бронируешь <span class="o">ПАМЯТЬ</span>».</p></div>
  </div>
"""))

# ---------- P17 · Экспорт + чек-лист ----------
PAGES.append(page("Шаг 15 · Экспорт и проверка", 17, f"""
  <span class="kick">Шаг 15</span>
  <h2>Экспорт и финальная проверка</h2>
  <div class="cards c3">
    <div class="card"><div class="ct">Формат</div><div class="ch">9:16 · 1080×1920</div></div>
    <div class="card"><div class="ct">Файл</div><div class="ch">MP4 · H.264</div></div>
    <div class="card"><div class="ct">Логотип</div><div class="ch">только финал, fade-in</div></div>
  </div>
  <div class="callout check"><div class="h">Чек-лист перед публикацией</div>
    <div class="row">Все сцены вертикальные, стиль и свет совпадают</div>
    <div class="row">Блюда не деформируются, руки естественные</div>
    <div class="row">Камера не дёргается, нет мерцания</div>
    <div class="row">Субтитры читаются, не перекрывают лицо и блюдо</div>
    <div class="row">Логотип только в финале</div>
    <div class="row">Голос слышен и громче музыки</div>
    <div class="row">Нет случайного текста и водяных знаков</div>
    <div class="row">Первые 2 секунды цепляют, финал завершён</div>
    <div class="row">Проверено на телефоне и в наушниках</div>
  </div>
  <div class="callout result"><div class="h">Практическое задание</div><p>Сдать: 4 исходника, 4 промпта, 4 клипа, финальный ролик и короткий разбор — какие артефакты вылезли и как ты их починил. Последнее важнее всего.</p></div>
"""))

# ---------- P18 · Все промпты + маршрут + контакты ----------
PAGES.append(f"""<section class="page page--dark" style="justify-content:space-between">
  <div>
    <div style="font-weight:800;font-size:9pt;letter-spacing:.15em;text-transform:uppercase;color:var(--o2);margin-bottom:10px">Шпаргалка</div>
    <h2 style="color:#fff;font-size:19pt;margin-bottom:4px">Все четыре промпта — рядом</h2>
    <p style="color:#b9ad9b;font-size:10.5pt;line-height:1.5;margin-bottom:14px;max-width:60ch">Скопируй нужный, подставь свой кадр, оставь одно движение.</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">1 · Гребешок</div><code style="font-family:ui-monospace,monospace;font-size:8pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">scallop stays stable, slow push-in, steam rises, warm amber light, no deformation</code></div>
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">2 · Руки шефа</div><code style="font-family:ui-monospace,monospace;font-size:8pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">hands gently place a plate, small natural motion, correct fingers, soft push-in, no extra hands</code></div>
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">3 · Интерьер</div><code style="font-family:ui-monospace,monospace;font-size:8pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">restaurant interior, slow dolly forward, candle flicker, warm bokeh, geometry stays, no morphing</code></div>
      <div style="background:#1c160d;border-radius:11px;padding:12px 14px"><div style="color:var(--o2);font-weight:800;font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px">4 · Трюфель</div><code style="font-family:ui-monospace,monospace;font-size:8pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap">truffle dish stable, slow push-in, steam curls, golden highlight, no fire, no text</code></div>
    </div>
  </div>
  <div style="text-align:center;border-top:1px solid rgba(255,255,255,.12);padding-top:18px">
    <img src="data:image/png;base64,{LOGO}" style="width:44px;height:44px;border-radius:11px">
    <div style="font-weight:800;font-size:14pt;color:#fff;margin:11px 0 5px">Сделал ролик — покажи. Застрял — приходи.</div>
    <div style="color:#b9ad9b;font-size:10pt;margin-bottom:14px">Гайды, промпт дня и разборы — в Telegram.</div>
    <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
      <span style="font-weight:800;font-size:10pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:9px 15px;border-radius:9px">Telegram · t.me/AlovLab</span>
      <span style="font-weight:800;font-size:10pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:9px 15px;border-radius:9px">VK · vk.com/alovlab</span>
      <span style="font-weight:800;font-size:10pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:9px 15px;border-radius:9px">alovlab.ru</span>
    </div>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Higgsfield · ресторанный Reels · AlovLab · v2</title><style>{CSS}</style>' + "\n".join(PAGES)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(PAGES))
