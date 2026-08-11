# -*- coding: utf-8 -*-
"""AlovLab · методичка «PRODUCTION PACK: дорогая AI-реклама» — под Reels/карусель commercial-ai.
Как из одной нейросети получить не сток, а кадр, который купит бренд. Сквозной кейс — премиум-
кроссовки. Режиссёрский бриф, референс-борд, готовые промпты по конвейеру (Nano Banana Pro →
Seedance 2.5 → Gemini Omni Flash → Veo 3.1 → Runway Gen-4.5 → Higgsfield), deliverables и лестница
ценности. Модели сверены на 11.08.2026. Премиум фикс-A4, светлые страницы, тёмные плашки под промпты.
База CSS — из v2. Запуск: python3 scripts/guide_commercial_ai_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "commercial-ai-pack"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-commercial-ai-pack.html"

EXTRA = r"""
.stage{display:flex;align-items:center;gap:12px;margin:2px 0 6px}
.stage .b{font-weight:800;font-size:9pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));
 padding:5px 11px;border-radius:20px;letter-spacing:.04em;white-space:nowrap}
.stage .t{font-weight:800;font-size:9pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.biz{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:10px;padding:9px 13px;margin:9px 0;font-size:9.7pt;line-height:1.45;color:var(--ink)}
.biz b{color:var(--o);text-transform:uppercase;font-size:8pt;letter-spacing:.06em;font-weight:800;margin-right:6px}
.param{display:grid;grid-template-columns:132px 1fr;gap:8px;font-size:9.6pt;line-height:1.4;padding:8px 0;border-top:1px solid var(--line2)}
.param:first-child{border-top:none}
.param code{font-family:ui-monospace,Menlo,monospace;font-size:9pt;background:#f1e9db;padding:2px 7px;border-radius:5px;color:#8a5a2a;font-weight:600;height:fit-content}
.param span{color:var(--body)}.param span b{color:var(--ink)}
.paramwrap{background:#fff;border:1px solid var(--line);border-radius:11px;padding:6px 14px;margin:10px 0}
.prompt code{font-size:9pt}
.lad{display:flex;flex-direction:column;gap:7px;margin:10px 0}
.lad .l{display:grid;grid-template-columns:132px 1fr 150px;gap:14px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:10px;padding:11px 14px}
.lad .l .nm{font-weight:800;font-size:10.5pt;color:var(--ink);line-height:1.15}
.lad .l .track{height:12px;border-radius:6px;background:#f1e9db;overflow:hidden}
.lad .l .track i{display:block;height:100%;border-radius:6px;background:linear-gradient(90deg,var(--o),var(--o2))}
.lad .l:nth-child(1) .track i{width:25%;opacity:.5}.lad .l:nth-child(2) .track i{width:50%;opacity:.72}
.lad .l:nth-child(3) .track i{width:75%;opacity:.88}.lad .l:nth-child(4) .track i{width:100%}
.lad .l .ds{font-size:9pt;color:var(--body);text-align:right;line-height:1.35}
.deliv{display:grid;grid-template-columns:1fr 1fr 1fr;gap:9px;margin:10px 0}
.deliv .d{background:#fff;border:1px solid var(--line);border-radius:11px;padding:11px 12px}
.deliv .d b{display:block;font-weight:800;font-size:14pt;color:var(--o);line-height:1}
.deliv .d span{display:block;margin-top:4px;font-size:8.8pt;line-height:1.35;color:var(--body)}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>AlovLab · production pack · дорогая AI-реклама</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None):
    ru_html = f'<div class="ru"><b>По-русски:</b> {ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>')

def stage(b, t):
    return f'<div class="stage"><span class="b">{b}</span><span class="t">{t}</span></div>'

def biz(txt, lbl="Бизнес"):
    return f'<div class="biz"><b>{lbl}</b>{txt}</div>'

P = []

# ---------- P1 · Обложка ----------
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · production pack · набор промптов</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.06;letter-spacing:-.02em;color:#fff;max-width:17ch">Одна нейросеть — два ценника. Как собрать рекламу, которую <span style="color:var(--o2)">купит бренд.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Разница не в модели, а в режиссуре. Сквозной кейс — премиум-кроссовки: бриф, референс-борд и готовые промпты на весь конвейер.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Бриф</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Референсы</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Промпты</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Сборка</span>
    </div>
  </div>
</section>""")

# ---------- P2 · Что внутри + карта конвейера ----------
P.append(page("Что внутри", 2, """
  <span class="kick">Пак под ролик «Одна нейросеть. Два ценника.»</span>
  <h2>Не генерация, а собранная реклама</h2>
  <p class="lead">Бренд платит не за «умею нейросеть». Он платит за кадр, который не стыдно поставить рядом с логотипом. Этот пак — как его получить: один режиссёрский бриф проходит через весь конвейер моделей.</p>
  <div class="flow">
    <div class="node"><b>Master</b><span>Nano Banana Pro</span></div><div class="arr">→</div>
    <div class="node"><b>Сцена</b><span>Seedance 2.5</span></div><div class="arr">→</div>
    <div class="node"><b>Правка</b><span>Gemini Omni</span></div><div class="arr">→</div>
    <div class="node"><b>Звук</b><span>Veo 3.1</span></div><div class="arr">→</div>
    <div class="node"><b>Сборка</b><span>Higgsfield</span></div>
  </div>
  <div class="term"><b>Сток-кадр</b> — <span>ровный свет, объект по центру, ноль истории. Модель получила «сделай красиво» и выдала среднее. Такой кадр тонет в ленте.</span></div>
  <div class="term"><b>Commercial-кадр</b> — <span>свет, камера, действие и звук заданы, а не случайны. Та же нейросеть, но у неё есть режиссёр. Такой кадр бренд покупает.</span></div>
  <div class="callout result"><div class="h">Что на выходе</div><p>Готовый режиссёрский бриф, референс-борд на 5 карточек и промпты на каждый этап — переносишь на свой продукт и собираешь ролик, который продаёт кампанию, а не генерацию.</p></div>
"""))

# ---------- P3 · Сток против commercial ----------
P.append(page("Диагноз", 3, """
  <span class="kick">Главная ошибка брифа</span>
  <h2>Почему «сделай дорого» не работает</h2>
  <p class="lead">Модель — не режиссёр. Она исполняет ровно то, что ты задал. Расплывчатый бриф = расплывчатый кадр. Разница между стоком и рекламой рождается в задании, а не в нейросети.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Сток-промпт</div>«Сделай дорогую рекламу белых кроссовок. Кинематографично. Премиально. Как Nike.» — модель угадывает. Свет плоский, камера случайная, истории нет.</div>
    <div class="box good"><div class="lbl">✓ Режиссёрский промпт</div>Заданы свет, ракурс, действие, среда и звук. Модель не угадывает — исполняет. Кадр читается как реклама, а не как сток.</div>
  </div>
  <span class="kick" style="display:block;margin-top:14px">Пять ручек режиссёра — что задаёшь в каждом кадре</span>
  <div class="paramwrap">
    <div class="param"><code>Свет</code><span><b>Характер сцены.</b> Тёмная студия, узкий тёплый контровой (rim), глубокие тени — вместо ровной заливки.</span></div>
    <div class="param"><code>Камера</code><span><b>Взгляд.</b> Низкий макро-ракурс, короткий наезд (dolly) — а не фронтальный «фотоаппарат на штативе».</span></div>
    <div class="param"><code>Действие</code><span><b>Жизнь в кадре.</b> Шнурки затягиваются сами, первый шаг — микро-событие держит внимание.</span></div>
    <div class="param"><code>Среда</code><span><b>Контекст.</b> Мокрый бетон, отражение, лёгкая дымка — атмосфера, а не пустой фон.</span></div>
    <div class="param"><code>Звук</code><span><b>Вес.</b> Натяжение шнурка, шаг по асфальту, саб-бас — нативный звук достраивает премиум.</span></div>
  </div>
"""))

# ---------- P4 · Режиссёрский бриф (шаблон) ----------
P.append(page("Режиссёрский бриф", 4, """
  <span class="kick">Шаблон · заполняешь под свой продукт</span>
  <h2>Бриф, который держит весь ролик</h2>
  <p class="lead">Один лист решает, каким будет каждый кадр. Заполни пять полей до первой генерации — дальше все модели работают на общий замысел, а не вразнобой.</p>
  <div class="scene"><div class="sn">1</div><div><div class="sh">Продукт-lock</div><div class="sd">Что нельзя менять: геометрия, подошва, лого, цвет. Это фиксируется <b>master-кадром</b> и переносится референсом во все сцены.</div></div><span class="stag">@ref продукт</span></div>
  <div class="scene"><div class="sn">2</div><div><div class="sh">Свет и палитра</div><div class="sd">Тёмная студия, узкий тёплый rim, глубокие чёрные. Один язык света на весь ролик — иначе кадры не склеятся в серию.</div></div><span class="stag">@ref свет</span></div>
  <div class="scene"><div class="sn">3</div><div><div class="sh">Камера</div><div class="sd">Низкий наезд → жёсткая склейка на первый шаг. Одно движение на кадр, без хаотичных пролётов.</div></div><span class="stag">@ref камера</span></div>
  <div class="scene"><div class="sn">4</div><div><div class="sh">Среда и действие</div><div class="sd">Мокрый бетон, отражение, шнурки затягиваются сами. Микро-событие, ради которого зритель досматривает.</div></div><span class="stag">@ref среда</span></div>
  <div class="scene"><div class="sn">5</div><div><div class="sh">Звук</div><div class="sd">Нативные SFX: натяжение шнурка, шаг по мокрому асфальту, низкий свелл. Звук пишем в промпт, а не «приклеим потом».</div></div><span class="stag">@ref ритм</span></div>
  <div class="callout check"><div class="h">Проверь бриф</div>
    <div class="row">Все пять полей заполнены конкретикой, а не эпитетами («дорого», «премиально»)</div>
    <div class="row">Продукт-lock описан так, что модель не тронет геометрию и лого</div>
    <div class="row">Один язык света и одна логика камеры на весь ролик</div>
  </div>
"""))

# ---------- P5 · Референс-борд ----------
P.append(page("Референс-борд", 5, """
  <span class="kick">До 50 референсов · собираем 5 ключевых</span>
  <h2>Дорогой кадр — это референсы</h2>
  <p class="lead">Seedance 2.5 берёт до 50 референсов. Тебе хватит пяти: каждый закрывает одно решение из брифа. В промпте они адресуются как <b>@ref1…@ref5</b> — модель знает, откуда брать что.</p>
  <div class="scene"><div class="sn">1</div><div><div class="sh">Продукт — геометрия, лого 1:1</div><div class="sd">Чистый master-кадр с этапа 1. Держит форму, подошву и лого неизменными во всех сценах.</div></div><span class="stag">@ref1</span></div>
  <div class="scene"><div class="sn">2</div><div><div class="sh">Свет — тёмная студия, rim</div><div class="sd">Кадр-эталон света: узкий тёплый контровой, глубокие чёрные. Задаёт настроение.</div></div><span class="stag">@ref2</span></div>
  <div class="scene"><div class="sn">3</div><div><div class="sh">Движение камеры</div><div class="sd">Референс траектории: низкий наезд, боковой dolly. Модель повторяет характер движения.</div></div><span class="stag">@ref3</span></div>
  <div class="scene"><div class="sn">4</div><div><div class="sh">Среда — мокрый бетон</div><div class="sd">Фактура и отражение. Атмосфера, в которой живёт продукт.</div></div><span class="stag">@ref4</span></div>
  <div class="scene"><div class="sn">5</div><div><div class="sh">Ритм и звук</div><div class="sd">Референс темпа и звуковых акцентов: где пауза, где удар, где шаг.</div></div><span class="stag">@ref5</span></div>
  <div class="biz"><b>Приём</b>Референсы — не «вдохновение», а инструкция. Один референс = одно решение. Мешаешь пять идей в одном кадре — модель усредняет и возвращает сток.</div>
"""))

# ---------- P6 · Этап 1 · Nano Banana Pro ----------
P.append(page("Этап 1 · Master · Nano Banana Pro", 6,
  stage("Этап 1", "Master-кадр · product lock") +
  "<h2>Nano Banana Pro — эталон продукта</h2>"
  "<p class=\"lead\">Первый кадр — не реклама, а <b>референс правды о продукте</b>: точная геометрия, лого, подошва. Он станет @ref1 для сцены. Чистый и честный — на нём модель потом строит атмосферу.</p>" +
  prompt("Готовый промпт · Nano Banana Pro",
    "A single white premium sneaker, clean 3/4 hero angle, seamless warm-neutral "
    "studio backdrop, soft even key light, razor-sharp logo, stitching and sole "
    "tread, exact geometry and true proportions, photoreal, 1:1 product master, "
    "no props, no added text. Lock the silhouette — this is the product reference.",
    "чистый master-кадр кроссовка: точная геометрия, лого, подошва, ровный свет, 1:1. Это референс продукта (@ref1), а не финальная реклама.") +
  "<div class=\"biz\"><b>Почему Pro</b>Nano Banana Pro держит лого и мелкий текст без искажений и даёт до 4K — поэтому продукт остаётся собой, когда сцена станет драматичной. Обычная image-модель на этом ломает надпись.</div>" +
  biz("товар с жёсткой геометрией: техника, флаконы, упаковка, украшения — там, где искажение формы = брак.")
))

# ---------- P7 · Этап 2 · Seedance 2.5 ----------
P.append(page("Этап 2 · Сцена · Seedance 2.5", 7,
  stage("Этап 2", "Сцена · кинокадр из референсов") +
  "<h2>Seedance 2.5 — режиссура в промпте</h2>"
  "<p class=\"lead\">Master-кадр + референсы света, камеры и среды собираются в одну сцену. Каждый @ref несёт своё решение — модель не угадывает, а исполняет бриф.</p>" +
  prompt("Готовый промпт · Seedance 2.5",
    "@ref1 product — keep geometry, sole, logo, white 1:1.\n"
    "@ref2 lighting: dark studio, narrow warm rim, deep blacks.\n"
    "Extreme low-angle macro on wet concrete; laces slowly self-tighten;\n"
    "controlled lateral dolly; rim light travels the material; hard cut\n"
    "to a first step, asphalt ripples. Native SFX: lace tension, wet step.",
    "продукт из @ref1 неизменен; свет из @ref2; низкий макро на мокром бетоне, шнурки затягиваются, боковой dolly, rim скользит по материалу, склейка на первый шаг, нативный звук.") +
  "<div class=\"biz\"><b>Логика</b>Сначала фиксируешь неизменное (продукт, свет), потом задаёшь движение (камера, действие) и в конце — звук. Порядок в промпте = приоритет для модели.</div>"
))

# ---------- P8 · Этап 3 · Gemini Omni Flash ----------
P.append(page("Этап 3 · Правка · Gemini Omni Flash", 8,
  stage("Этап 3", "Правка · разговором, не заново") +
  "<h2>Gemini Omni Flash — режиссёрская правка</h2>"
  "<p class=\"lead\">Кадр почти готов, но света много и нет напряжения. Не перегенерируй заново — правь адресно. Говоришь, что оставить, и что именно поменять. Продукт и камера не трогаются.</p>" +
  prompt("Готовый промпт · conversational edit",
    "Keep the shoe, framing and camera path unchanged.\n"
    "Change only: reduce fill light 30%; deepen wet-asphalt reflections;\n"
    "add subtle mist; delay the hero light to the last second.\n"
    "Do not alter shoe geometry, logo, camera path or duration.",
    "оставь кроссовок, кадрирование и траекторию камеры; поменяй только: заполняющий свет −30%, глубже отражения на асфальте, лёгкая дымка, геройский свет — на последнюю секунду. Геометрию, лого и хронометраж не менять.") +
  "<div class=\"gb\">"
  "<div class=\"box bad\"><div class=\"lbl\">✕ Регенерация</div>«Сделай ещё раз, но лучше» — теряешь удачный кадр, продукт плывёт, свет уходит.</div>"
  "<div class=\"box good\"><div class=\"lbl\">✓ Адресная правка</div>Keep… / Change only… — сохраняешь 90% кадра и точечно доводишь атмосферу.</div>"
  "</div>"
))

# ---------- P9 · Этап 4 · Veo 3.1 / Runway ----------
P.append(page("Этап 4 · Звук и камера · Veo 3.1 · Runway", 9,
  stage("Этап 4", "Звук и камера · достраиваем премиум") +
  "<h2>Veo 3.1 — нативный звук в кадре</h2>"
  "<p class=\"lead\">Дорогое ощущение во многом держится на звуке, а не на картинке. Veo 3.1 генерирует аудио прямо со сценой: не подкладываешь музыку потом, а задаёшь SFX в промпте. Runway Gen-4.5 берёт точную хореографию камеры.</p>" +
  prompt("Готовый промпт · Veo 3.1 (image-to-video)",
    "[from the hero frame] Cinematic 15s. Native audio: low sub-bass swell, one\n"
    "lace-tension creak, a single wet-asphalt footstep on the hard cut. Camera:\n"
    "slow low push-in, then hard cut to the first step. Keep product geometry,\n"
    "logo and proportions unchanged. 4K, deep blacks, warm rim light.",
    "из геройского кадра, 15 сек, нативный звук (саб-бас, скрип шнурка, шаг по мокрому асфальту на склейке); камера — медленный низкий наезд, затем жёсткая склейка на шаг; продукт не менять.") +
  "<div class=\"biz\"><b>Runway Gen-4.5</b>Когда нужна точная траектория — прописываешь движение камеры прямо в промпте (скорость, дуга, точка фокуса). Сильная сторона — предсказуемая хореография кадра.</div>" +
  biz("любой продукт в движении: авто, гаджет, напиток, парфюм — звук и камера превращают показ в рекламу.")
))

# ---------- P10 · Карта моделей + сборка ----------
P.append(page("Карта моделей · сборка", 10, """
  <span class="kick">Что чем делать</span>
  <h2>Каждому этапу — свой инструмент</h2>
  <p class="lead">Ошибка — тянуть весь ролик в одну модель. Конвейер сильнее: каждая закрывает то, в чём она лучшая, а Higgsfield собирает результат.</p>
  <table>
    <tr><th>Этап</th><th>Модель</th><th>Зачем именно она</th></tr>
    <tr><td><b>Master продукта</b></td><td>Nano Banana Pro</td><td>точная геометрия, лого и текст без искажений, до 4K</td></tr>
    <tr><td><b>Сцена</b></td><td>Seedance 2.5</td><td>до 50 референсов, кинокадр и звук из одного промпта</td></tr>
    <tr><td><b>Правка</b></td><td>Gemini Omni Flash</td><td>адресный edit разговором, без потери кадра</td></tr>
    <tr><td><b>Звук</b></td><td>Veo 3.1</td><td>нативное аудио image-to-video, 4K</td></tr>
    <tr><td><b>Камера</b></td><td>Runway Gen-4.5</td><td>точная хореография движения в промпте</td></tr>
    <tr><td><b>Сборка</b></td><td>Higgsfield</td><td>пресеты движения и финальная склейка</td></tr>
  </table>
  <p class="note">Модели и их возможности сверены на 11.08.2026. Названия и лимиты меняются — держись логики этапов (что фиксируем, что двигаем, чем правим), а не конкретных кнопок.</p>
"""))

# ---------- P11 · Что продаёшь бренду ----------
P.append(page("Что продаёшь бренду", 11, """
  <span class="kick">Deliverables · один ролик разным моделям</span>
  <h2>Клиент покупает не генерацию</h2>
  <p class="lead">Из одной собранной сцены нарезается пакет под всю кампанию. Это и превращает «умею нейросеть» в услугу, за которую платят.</p>
  <div class="deliv">
    <div class="d"><b>1× Hero</b><span>15 сек, вертикаль — главный ролик</span></div>
    <div class="d"><b>3× Cutdown</b><span>по 6 сек под рекламные плейсменты</span></div>
    <div class="d"><b>5× Hook</b><span>первые секунды под соцсети</span></div>
    <div class="d"><b>4× Frame</b><span>продуктовые кадры для карточек</span></div>
    <div class="d"><b>1× Storyboard</b><span>раскадровка для согласования</span></div>
    <div class="d"><b>1× Sound</b><span>звуковая режиссура сцены</span></div>
  </div>
  <span class="kick" style="display:block;margin-top:12px">Лестница ценности — на чём растёт чек</span>
  <div class="lad">
    <div class="l"><span class="nm">Генерация</span><div class="track"><i></i></div><span class="ds">отдал кадр — дальше сами</span></div>
    <div class="l"><span class="nm">Ролик</span><div class="track"><i></i></div><span class="ds">собранный клип под задачу</span></div>
    <div class="l"><span class="nm">Концепт + ролик</span><div class="track"><i></i></div><span class="ds">идея, бриф и исполнение</span></div>
    <div class="l"><span class="nm">Кампания-система</span><div class="track"><i></i></div><span class="ds">пакет + конвейер под бренд</span></div>
  </div>
"""))

# ---------- P12 · Чек-лист + честность ----------
P.append(page("Чек-лист · честность", 12, """
  <span class="kick">Контроль перед сдачей</span>
  <h2>Сток или commercial — проверь кадр</h2>
  <div class="callout check"><div class="h">Чек-лист режиссуры</div>
    <div class="row">Свет задан (rim, глубокие чёрные), а не ровная заливка</div>
    <div class="row">Камера — одно осмысленное движение, не случайный ракурс</div>
    <div class="row">В кадре есть действие-событие, ради которого досматривают</div>
    <div class="row">Продукт неизменен: геометрия, лого, подошва, цвет</div>
    <div class="row">Звук нативный, задан в промпте, а не подложен потом</div>
    <div class="row">Формат 9:16 под Reels; нарезаны Hook и Cutdown</div>
  </div>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Сток</div>«Сделай красиво», один промпт, ровный свет, объект по центру, тишина. Тонет в ленте.</div>
    <div class="box good"><div class="lbl">✓ Commercial</div>Бриф из пяти решений, референсы, адресная правка, нативный звук. Кадр, который бренд ставит рядом с лого.</div>
  </div>
  <p class="note">Честно: кадры кроссовка — концепт-дизайн под кейс, не «результат клиента». Никаких выдуманных цифр и цен. Показываешь ИИ — реальный интерфейс инструмента.</p>
"""))

# ---------- P13 · CTA ----------
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:26pt;line-height:1.1;margin:18px 0 8px">Собери commercial,<br>не стыдно <span style="color:var(--o2)">бренду.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Весь пак: режиссёрский бриф, референс-борд, готовые промпты (Nano Banana Pro · Seedance 2.5 · Gemini Omni · Veo 3.1 · Runway), карта моделей и чек-лист bad→good. Переноси на свой продукт.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Забрать пак → t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Реклама под бренд → бриф @alovlab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>PRODUCTION PACK · дорогая AI-реклама · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
