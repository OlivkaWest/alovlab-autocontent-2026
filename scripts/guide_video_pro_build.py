# -*- coding: utf-8 -*-
"""AlovLab · ПОЛНАЯ методичка-урок «Ролик без камеры на нейросети» (премиум-PDF, фикс-A4).
Со всеми промптами, названиями света, движениями камеры, планами, библиотекой сцен,
разбором на живом примере (мини-реклама кофейни) и монтажом. По GLOBAL-METHODOLOGY-RULE.
Запуск: python3 scripts/guide_video_pro_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "video-no-camera"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-video-PRO.html"

EXTRA = r"""
.main.mid{display:flex;flex-direction:column;justify-content:center}
.midwrap{width:100%}
.lvls{margin:8px 0 2px}
.lvls .row{display:grid;grid-template-columns:120px 1fr;gap:10px;align-items:start;margin:6px 0}
.lvls .row .k{font-weight:800;font-size:9pt;color:var(--o);padding-top:2px}
.lvls .row p{margin:0;font-size:9.6pt;line-height:1.4;color:var(--body)}
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:9px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:9px 12px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.1pt;line-height:1.38;color:var(--ink);margin-top:3px;max-width:none}
.sc{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff;margin:7px 0}
.sc .t{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.sc b{font-weight:800;font-size:10pt;color:var(--ink)}
.sc .lt{font-size:7.6pt;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--o);white-space:nowrap}
.sc code{display:block;font-family:ui-monospace,Menlo,monospace;font-size:7.9pt;line-height:1.42;color:#8a5a2a;background:#faf3ea;border-radius:7px;padding:7px 9px;margin-top:5px;white-space:pre-wrap}
.warn{background:#13100a;border-radius:14px;padding:14px 17px;margin:9px 0;color:#f4efe6}
.warn .h{font-weight:800;font-size:10pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o2);margin-bottom:7px}
.warn ul{margin:0;padding-left:0;list-style:none}
.warn li{position:relative;padding:4px 0 4px 20px;font-size:9.4pt;line-height:1.4;color:#eae4da;max-width:none}
.warn li:before{content:"✕";position:absolute;left:0;color:var(--o2);font-weight:800}
.warn li.ok:before{content:"✔"}
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:15px 18px;margin:9px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12.5pt;color:#fff;margin-bottom:6px}.team p{font-size:9.6pt;line-height:1.5;color:#cdbfa8;max-width:none}
.team .dirs{display:flex;flex-wrap:wrap;gap:6px;margin:9px 0 3px}
.team .dirs span{font-size:8.2pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:4px 10px}
table.ref{width:100%;border-collapse:separate;border-spacing:0;margin:9px 0;font-size:9pt;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden}
table.ref th{background:var(--ink);color:#fff;font-weight:800;text-transform:uppercase;letter-spacing:.04em;font-size:7.4pt;text-align:left;padding:8px 10px}
table.ref td{padding:7px 10px;border-top:1px solid var(--line2);color:var(--body);vertical-align:top;line-height:1.3}
table.ref td b{color:var(--ink)}
table.ref td code{font-family:ui-monospace,Menlo,monospace;font-size:8pt;color:#8a5a2a}
table.ref tr:nth-child(even) td{background:#fbf7f0}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · ролик без камеры · полный урок</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None):
    r = f'<div class="ru">{ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{r}</div>')

def sc(title, light, code):
    return (f'<div class="sc"><div class="t"><b>{title}</b><span class="lt">{light}</span></div>'
            f'<code>{code}</code></div>')

P = []

# 01 Cover
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:absolute;right:8%;top:22%;width:48%;height:38%;border-radius:16px;border:1px solid rgba(255,140,60,.28);background:linear-gradient(160deg,rgba(255,140,60,.10),rgba(255,140,60,0))"></div>
  <div style="position:absolute;right:24%;top:37%;width:64px;height:64px;border-radius:50%;border:2px solid var(--o2);display:grid;place-items:center;color:var(--o2);font-size:22pt">▶</div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · полный урок</div>
    <h1 style="font-weight:800;font-size:32pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Ролик без камеры на нейросети</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Полный урок: все промпты, схемы света, движения камеры, планы, разбор на живом примере и монтаж. От пустого экрана до готовой рекламы.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Библиотека сцен</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Схемы света</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Разбор кейса</span>
    </div>
  </div>
</section>""")

# 02 TOC
toc = [
 ("01","Что ты соберёшь","03"),("02","4 слоя кадра","04"),("03","Свет: схемы","05"),
 ("04","Камера: движения","06"),("05","Планы кадра","07"),("06","Анатомия промпта","08"),
 ("07","Мастер-промпт сцены","09"),("08","Библиотека сцен · 1","10"),("09","Библиотека сцен · 2","11"),
 ("10","Негативы и настройки","12"),("11","Лицо и идентичность","13"),
 ("12","Разбор кейса: кофейня","14"),("13","Кейс: сцены 1–3","15"),("14","Кейс: сцены 4–5","16"),
 ("15","Монтаж и грейд","17"),("16","Звук и озвучка","18"),("17","Плохо/хорошо","19"),
 ("18","Честно и по закону","20"),("19","Ошибки и фиксы","21"),
 ("20","Сделай сейчас + проверка","22"),("21","Дальше — на курсе","23"),
 ("22","Путь в команду AlovLab","24"),("23","Контакты","25"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:10px;padding:6px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:9.5pt;width:24px">{a}</span>'
               f'<span style="font-weight:600;font-size:10.5pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:9.5pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Маршрут урока</h1>'
    '<p class="lead">Двадцать три шага: теория кадра, справочники света и камеры, библиотека промптов, разбор кейса и монтаж.</p>'
    f'<div style="margin-top:4px">{rows}</div>'))

# 03 result
P.append(page("Шаг 01 · Результат", 3,
    head("Шаг 01", "Что ты соберёшь", "Короткий кинематографичный ролик 9:16 на 15–30 секунд из сгенерённых сцен: реклама, Reels, заставка бренда.")
    + '<div class="flow"><div class="node"><b>Опиши</b><span>сцену</span></div><div class="arr">→</div>'
      '<div class="node"><b>Сгенерь</b><span>3–6 сек</span></div><div class="arr">→</div>'
      '<div class="node"><b>Собери</b><span>монтаж</span></div><div class="arr">→</div>'
      '<div class="node"><b>Опубликуй</b><span>9:16</span></div></div>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Инструменты</div><div class="ch">Видео-нейросеть</div><p>Higgsfield, Veo, Seedance, Kling и др. Генерят сцену по тексту.</p></div>'
      '<div class="card"><div class="ct">Плюс</div><div class="ch">Монтаж</div><p>Любой редактор: склейка, музыка, подписи, грейд.</p></div>'
      '<div class="card"><div class="ct">Съёмка</div><div class="ch">Ноль</div><p>Ни камеры, ни актёров, ни площадки.</p></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div>'
      '<p>Вертикальный ролик уровня рекламы: смена красивых кадров, единый тёплый грейд, музыка и короткие подписи. Собран за вечер одним человеком.</p></div>'))

# 04 four layers
P.append(page("Шаг 02 · Кадр", 4,
    head("Шаг 02", "Любой кадр это 4 слоя", "Опиши все четыре, и сцена выйдет дорогой, а не случайной.")
    + '<div class="scene"><div class="sn">1</div><div><div class="sh">Объект и план</div><div class="sd">Что в кадре и как близко: общий, средний, крупный, макро.</div></div><span class="stag">Что</span></div>'
    + '<div class="scene"><div class="sn">2</div><div><div class="sh">Камера</div><div class="sd">Движение: наезд, облёт, проезд, статика.</div></div><span class="stag">Как снято</span></div>'
    + '<div class="scene"><div class="sn">3</div><div><div class="sh">Свет</div><div class="sd">Схема и время: золотой час, софтбокс, контровой, неон.</div></div><span class="stag">Настроение</span></div>'
    + '<div class="scene"><div class="sn">4</div><div><div class="sh">Грейд и настроение</div><div class="sd">Цвет и атмосфера: тёплый, холодный, дорогой, кино.</div></div><span class="stag">Стиль</span></div>'
    + '<p>Дальше два справочника: свет и камера. Из них ты собираешь любую сцену как из кубиков.</p>'))

# 05 light
P.append(page("Шаг 03 · Свет", 5,
    head("Шаг 03", "Свет: схемы и названия", "Свет решает, дорогой кадр или дешёвый. Вставляй ключевые слова в промпт.")
    + '<table class="ref"><tr><th>Схема</th><th>Что даёт</th><th>Ключевые слова</th></tr>'
      '<tr><td><b>Золотой час</b></td><td>тёплый, мягкий, дорогой</td><td><code>golden hour, warm sunlight, long shadows</code></td></tr>'
      '<tr><td><b>Синий час</b></td><td>сумерки, киношно</td><td><code>blue hour, cool tones, moody</code></td></tr>'
      '<tr><td><b>Софтбокс</b></td><td>ровный, чистый, студийный</td><td><code>soft studio lighting, softbox, even light</code></td></tr>'
      '<tr><td><b>Рембрандт</b></td><td>драматичный портрет</td><td><code>Rembrandt lighting, dramatic side light</code></td></tr>'
      '<tr><td><b>Контровой (rim)</b></td><td>светящийся контур объекта</td><td><code>rim light, backlight, glowing edge</code></td></tr>'
      '<tr><td><b>Из окна</b></td><td>мягкий, реалистичный</td><td><code>natural window light, soft shadows</code></td></tr>'
      '<tr><td><b>Неон</b></td><td>город, техно, цвет</td><td><code>neon lighting, colorful reflections</code></td></tr>'
      '<tr><td><b>Low-key</b></td><td>тёмный, контрастный</td><td><code>low-key lighting, deep shadows</code></td></tr>'
      '<tr><td><b>High-key</b></td><td>светлый, чистый, воздушный</td><td><code>high-key lighting, bright, airy</code></td></tr>'
      '<tr><td><b>Практический</b></td><td>уют, лампы в кадре</td><td><code>practical lights, warm lamps in frame</code></td></tr></table>'
    + '<p class="note">Держи ОДНУ схему света на весь ролик (например золотой час) — тогда сцены склеятся как один фильм.</p>'))

# 06 camera
P.append(page("Шаг 04 · Камера", 6,
    head("Шаг 04", "Камера: движения", "Движение задаёт энергию кадра. Одно движение на сцену, не мешай пять.")
    + '<table class="ref"><tr><th>Движение</th><th>Эффект</th><th>Ключевые слова</th></tr>'
      '<tr><td><b>Наезд</b></td><td>погружение, акцент</td><td><code>slow push-in, dolly in</code></td></tr>'
      '<tr><td><b>Отъезд</b></td><td>раскрытие, финал</td><td><code>slow pull-out, dolly out</code></td></tr>'
      '<tr><td><b>Облёт</b></td><td>объём, премиум</td><td><code>orbit, arc shot around subject</code></td></tr>'
      '<tr><td><b>Проезд</b></td><td>движение вдоль</td><td><code>tracking shot, dolly along</code></td></tr>'
      '<tr><td><b>Кран</b></td><td>масштаб, размах</td><td><code>crane up, crane down</code></td></tr>'
      '<tr><td><b>Ручная</b></td><td>живость, документальность</td><td><code>handheld, subtle shake</code></td></tr>'
      '<tr><td><b>Статика</b></td><td>спокойствие, чистота</td><td><code>locked static shot</code></td></tr>'
      '<tr><td><b>Наклон/панорама</b></td><td>раскрытие пространства</td><td><code>tilt up, slow pan</code></td></tr>'
      '<tr><td><b>Рэк-фокус</b></td><td>перевод внимания</td><td><code>rack focus, focus shift</code></td></tr>'
      '<tr><td><b>Слоу-мо</b></td><td>дорого, детально</td><td><code>slow motion</code></td></tr></table>'
    + '<p class="note">Оптика: добавь <code>85mm, shallow depth of field</code> для портрета, <code>wide 24mm</code> для простора.</p>'))

# 07 shots
P.append(page("Шаг 05 · Планы", 7,
    head("Шаг 05", "Планы кадра", "Чередуй планы, иначе ролик монотонный. Классика: общий → средний → крупный → деталь.")
    + '<table class="ref"><tr><th>План</th><th>Зачем</th><th>Ключевые слова</th></tr>'
      '<tr><td><b>Общий (establishing)</b></td><td>показать место</td><td><code>establishing wide shot</code></td></tr>'
      '<tr><td><b>Средний</b></td><td>действие, контекст</td><td><code>medium shot</code></td></tr>'
      '<tr><td><b>Крупный (close-up)</b></td><td>эмоция, продукт</td><td><code>close-up</code></td></tr>'
      '<tr><td><b>Макро/деталь</b></td><td>фактура, вкусно</td><td><code>extreme close-up, macro detail</code></td></tr>'
      '<tr><td><b>Портрет</b></td><td>герой</td><td><code>portrait, shallow depth of field</code></td></tr>'
      '<tr><td><b>POV</b></td><td>вовлечение, от первого лица</td><td><code>POV shot, first person</code></td></tr>'
      '<tr><td><b>Через плечо (OTS)</b></td><td>диалог, точка зрения</td><td><code>over-the-shoulder shot</code></td></tr></table>'
    + '<div class="callout check"><div class="h">Мини-раскадровка на 15 секунд</div>'
      '<div class="row">Общий (место) → крупный (деталь) → портрет (герой) → финал (продукт/логотип).</div>'
      '<div class="row">Каждая сцена 1–3 секунды, склейки в темп музыки.</div></div>'))

# 08 anatomy
P.append(page("Шаг 06 · Промпт", 8,
    head("Шаг 06", "Анатомия промпта сцены", "Семь блоков. Заполни каждый, и генератор поймёт тебя однозначно.")
    + '<table class="ref"><tr><th>Блок</th><th>Что писать</th></tr>'
      '<tr><td><b>Формат</b></td><td>vertical 9:16, длительность 5 секунд</td></tr>'
      '<tr><td><b>Объект/план</b></td><td>что в кадре и какой план</td></tr>'
      '<tr><td><b>Камера</b></td><td>движение и оптика</td></tr>'
      '<tr><td><b>Свет</b></td><td>схема из справочника</td></tr>'
      '<tr><td><b>Движение</b></td><td>что двигается в кадре</td></tr>'
      '<tr><td><b>Грейд/настроение</b></td><td>тёплый, кино, дорого, реалистично</td></tr>'
      '<tr><td><b>Негатив</b></td><td>no text, no watermark, no distorted faces</td></tr></table>'
    + '<p>Порядок не строгий, но чем полнее блоки, тем меньше дублей. На следующей странице этот скелет собран в мастер-промпт.</p>'))

# 09 master prompt
master = ("Cinematic vertical 9:16 shot, 5 seconds. План: [ОБЩИЙ / КРУПНЫЙ / МАКРО]. Объект: [ЧТО В КАДРЕ]. "
          "Камера: [slow push-in / orbit / static], [85mm shallow depth of field]. Свет: [golden hour / softbox / rim light]. "
          "Движение: [что двигается]. Грейд: warm cinematic, expensive, photoreal, no distortion. "
          "Negative: no text, no watermark, no logos, no distorted faces, no gibberish.")
P.append(page("Шаг 07 · Мастер", 9,
    head("Шаг 07", "Мастер-промпт сцены", "Скопируй, подставь значения из справочников света, камеры и планов.")
    + prompt("Мастер-промпт · СКОПИРОВАТЬ", master)
    + '<div class="io"><div class="c"><b>Что вставить</b><p>План, объект, движение камеры, схему света, что двигается. Всё берётся из справочников выше.</p></div>'
      '<div class="c out"><b>Что получить</b><p>Готовую кинематографичную сцену 5 секунд, 9:16, под монтаж.</p></div></div>'
    + '<div class="lvls"><div class="row"><span class="k">Быстрый</span><p>Заполни скобки и отправь.</p></div>'
      '<div class="row"><span class="k">Про</span><p>Добавь оптику и зерно: «85mm, subtle film grain, cinematic color».</p></div>'
      '<div class="row"><span class="k">Advanced</span><p>Задай непрерывность: «same warm grade and light as previous scene» для склейки в один фильм.</p></div></div>'))

# 10 library 1
P.append(page("Шаг 08 · Сцены", 10,
    head("Шаг 08", "Библиотека сцен · часть 1", "Готовые промпты. Меняй объект под свою тему, свет держи единым.")
    + sc("Establishing · место", "золотой час",
         "Cinematic vertical 9:16, 5s, establishing wide shot of [МЕСТО], golden hour, warm sunlight, long shadows, slow push-in, photoreal. No text, no watermark.")
    + sc("Интерьер · уют", "практический свет",
         "Cinematic vertical 9:16, 5s, cozy interior of [МЕСТО], practical warm lamps in frame, soft glow, slow dolly, shallow depth of field. No text, no watermark.")
    + sc("Продукт · макро", "софтбокс + контровой",
         "Cinematic vertical 9:16, 5s, extreme close-up of [ПРОДУКТ] on a dark reflective surface, soft studio light and rim light, slow orbit, macro detail. No text, no watermark.")
    + sc("Портрет · герой", "свет из окна / Рембрандт",
         "Cinematic vertical 9:16, 5s, portrait of [ГЕРОЙ], natural window light, shallow depth of field 85mm, subtle push-in, keep face natural. No text, no watermark, no distorted face.")))

# 11 library 2
P.append(page("Шаг 08 · Сцены", 11,
    head("Библиотека сцен · часть 2", "Ещё сцены под финал, атмосферу и результат.")
    + sc("Деталь · фактура", "контровой",
         "Cinematic vertical 9:16, 5s, extreme macro of [ДЕТАЛЬ: пар, капли, ткань], rim light, slow motion, photoreal texture. No text, no watermark.")
    + sc("Атмосфера · переход", "low-key",
         "Cinematic vertical 9:16, 5s, a rich cinematic frame emerges from darkness with warm particles and soft light bloom, low-key lighting, elegant reveal. No text, no watermark.")
    + sc("POV · от первого лица", "естественный",
         "Cinematic vertical 9:16, 5s, POV shot walking into [МЕСТО], natural light, subtle handheld motion, photoreal, immersive. No text, no watermark.")
    + sc("Финал · телефон (i2v)", "контровой",
         "Cinematic vertical 9:16, 5s, a phone on a dark desk, warm rim light, screen plays a vertical ad, slow push-in to the screen, photoreal. No text on room, no watermark.")
    + '<p class="note">Финал лучше делать image-to-video: старт-кадр телефон с чистым экраном, ролик на экран кладёшь на монтаже.</p>'))

# 12 negatives/settings
P.append(page("Шаг 09 · Настройки", 12,
    head("Шаг 09", "Негативы и настройки", "Что выставить и что запретить, чтобы не жечь кредиты и не ловить брак.")
    + '<div class="cards c2">'
      '<div class="card"><div class="ct">Формат</div><div class="ch">9:16 · 5 сек</div><p>Короткие сцены дешевле и легче режутся.</p></div>'
      '<div class="card"><div class="ct">Движение</div><div class="ch">motion средний</div><p>Слишком сильное — артефакты, слишком слабое — статика.</p></div>'
      '<div class="card"><div class="ct">Дубли</div><div class="ch">2–3 на сцену</div><p>Бери лучший. Так работают все, это норма.</p></div>'
      '<div class="card"><div class="ct">Непрерывность</div><div class="ch">один грейд</div><p>Один свет и цвет во всех промптах.</p></div></div>'
    + '<div class="warn"><div class="h">Negative (добавляй ко всем сценам)</div><ul>'
      '<li class="ok">no text, no captions (русский текст добавишь на монтаже)</li>'
      '<li class="ok">no watermark, no logos</li>'
      '<li class="ok">no distorted faces, no extra fingers</li>'
      '<li class="ok">no warping, no flicker</li></ul></div>'))

# 13 identity
P.append(page("Шаг 10 · Лицо", 13,
    head("Шаг 10", "Лицо и идентичность", "Если в кадре конкретный человек, его нужно закрепить, иначе будет чужой.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Загрузи фото-референс</b> лица как основу сцены (image-to-video или reference).</div></div>'
      '<div class="step"><div class="sx"><b>В промпте пиши</b> «keep the face natural and unchanged, same person».</div></div>'
      '<div class="step"><div class="sx"><b>Не проси сильных ракурсов</b> в профиль и резких движений головы — там лицо плывёт чаще.</div></div>'
      '<div class="step"><div class="sx"><b>Проверяй каждый дубль</b> на искажения лица и рук, брак не бери.</div></div></div>'
    + '<div class="callout result"><div class="h">Итог</div><p>Узнаваемый герой в кадре, без пластиковой кожи и чужих черт. Для бренда это критично.</p></div>'))

# 14 case intro
P.append(page("Кейс · кофейня", 14,
    head("Разбор кейса", "Мини-реклама кофейни за вечер", "Соберём вертикальный ролик «Утро в кофейне» из 5 сцен. Единый свет: золотой час и тёплые лампы.")
    + '<div class="flow"><div class="node"><b>1</b><span>улица</span></div><div class="arr">→</div>'
      '<div class="node"><b>2</b><span>интерьер</span></div><div class="arr">→</div>'
      '<div class="node"><b>3</b><span>латте</span></div><div class="arr">→</div>'
      '<div class="node"><b>4</b><span>бариста</span></div><div class="arr">→</div>'
      '<div class="node"><b>5</b><span>финал</span></div></div>'
    + '<p>Идея: тёплое утро, дорогой кофе, живой человек. Задача ролика — вызвать желание зайти. Ниже точные промпты по сценам, все в одном грейде.</p>'
    + '<div class="callout check"><div class="h">Единый стиль кейса</div>'
      '<div class="row">Свет: золотой час снаружи, тёплые практические лампы внутри.</div>'
      '<div class="row">Грейд: тёплый, мягкий контраст. Планы: общий → интерьер → макро → портрет → финал.</div></div>'))

# 15 case 1-3
P.append(page("Кейс · сцены 1–3", 15,
    head("Кейс", "Сцены 1–3")
    + sc("Сцена 1 · Улица, вывеска", "золотой час",
         "Cinematic vertical 9:16, 5s, establishing wide shot of a cozy coffee shop storefront on a city street, golden hour, warm sunlight, long shadows, slow push-in toward the entrance, photoreal. No text, no watermark.")
    + sc("Сцена 2 · Интерьер, пар над чашкой", "практические лампы",
         "Cinematic vertical 9:16, 5s, warm cozy coffee shop interior, practical warm lamps in frame, steam rising from a cup on a wooden table, soft glow, slow dolly in, shallow depth of field. No text, no watermark.")
    + sc("Сцена 3 · Латте-арт макро", "софтбокс + контровой",
         "Cinematic vertical 9:16, 5s, extreme close-up of latte art in a ceramic cup, soft studio light with warm rim light, slow orbit, macro detail, photoreal. No text, no watermark.")))

# 16 case 4-5
P.append(page("Кейс · сцены 4–5", 16,
    head("Кейс", "Сцены 4–5 + сборка")
    + sc("Сцена 4 · Бариста (лицо-референс)", "свет из окна",
         "Cinematic vertical 9:16, 5s, portrait of a friendly barista smiling, natural warm window light, shallow depth of field 85mm, subtle push-in, keep face natural and unchanged. No text, no watermark, no distorted face.")
    + sc("Сцена 5 · Финал, чашка + место под лого", "контровой",
         "Cinematic vertical 9:16, 5s, a coffee cup on a warm wooden table, warm rim light, gentle steam, slow push-in, clean empty space above for a logo, photoreal. No text, no watermark.")
    + '<div class="callout result"><div class="h">Сборка</div>'
      '<p>Склей 5 сцен по 1–2 секунды в темп музыки, положи один тёплый грейд, добавь короткие подписи и лого на сцену 5. На выходе вертикальная реклама кофейни, снятая без камеры.</p></div>'))

# 17 editing
P.append(page("Шаг 11 · Монтаж", 17,
    head("Шаг 11", "Монтаж и грейд", "Здесь набор сцен становится рекламой.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Разложи сцены в темп музыки.</b> Склейки на бит, 1–2 секунды на сцену.</div></div>'
      '<div class="step"><div class="sx"><b>Один грейд поверх всего.</b> Лёгкая цветокоррекция под единый тёплый тон.</div></div>'
      '<div class="step"><div class="sx"><b>Хук в первые 2 секунды.</b> Самая сильная сцена в начало.</div></div>'
      '<div class="step"><div class="sx"><b>Подписи крупно, отдельным слоем.</b> Одна мысль на кадр, русский текст здесь, не в генерации.</div></div>'
      '<div class="step"><div class="sx"><b>Экспорт 9:16.</b> Проверь на телефоне: читается, не дёргается, звук на месте.</div></div></div>'
    + '<p class="note">Переходы держи простыми: рез или короткое затемнение. Модные глитчи чаще удешевляют, чем украшают.</p>'))

# 18 sound
P.append(page("Шаг 12 · Звук", 18,
    head("Шаг 12", "Звук и озвучка", "Звук это половина впечатления. Не публикуй немой ролик.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Музыка</div><div class="ch">Один трек</div><p>Кинематографичная подложка, склейки в бит. Без авторских рисков.</p></div>'
      '<div class="card"><div class="ct">Атмосфера</div><div class="ch">Звуки сцен</div><p>Шум улицы, пар, чашка. Добавляют реализм.</p></div>'
      '<div class="card"><div class="ct">Голос</div><div class="ch">Озвучка</div><p>Закадровый голос или аватар, если нужен текст от бренда.</p></div></div>'
    + '<p>Голос за кадром, дубляж и озвучку своим голосом разбираем отдельно (Земля Звук в курсе и часть 2 в Telegram). Здесь достаточно музыки и атмосферы.</p>'
    + '<div class="term"><b>Правило громкости.</b> <span>Музыка не должна перебивать голос. Если есть закадр, приглуши музыку под ним.</span></div>'))

# 19 good/bad
P.append(page("Шаг 13 · Как просить", 19,
    head("Шаг 13", "Промпт сцены: плохо и хорошо", "Кадр выходит ровно настолько, насколько ты его описал.")
    + '<div class="gb">'
      '<div class="box bad"><div class="lbl">Плохо</div>«Красивое видео кофейни.»<br><br>Нет плана, света, движения. Выходит общо и дёшево.</div>'
      '<div class="box good"><div class="lbl">Хорошо</div>«9:16, общий план витрины кофейни, золотой час, тёплый свет, длинные тени, медленный наезд, 5 секунд.»</div></div>'
    + '<p>Формула из четырёх слоёв (объект + камера + свет + грейд) плюс негатив = предсказуемо дорогой кадр.</p>'
    + '<div class="callout result"><div class="h">Проверка кадра</div><p>Если можешь одним взглядом назвать план, свет и движение — промпт собран правильно.</p></div>'))

# 20 honest
P.append(page("Шаг 14 · Честность", 20,
    head("Шаг 14", "Честно и по закону", "Красивый ролик не должен обманывать и нарушать права.")
    + '<div class="warn"><div class="h">Так нельзя</div><ul>'
      '<li>Выдавать сгенерённый продукт за реальное фото товара, если он отличается.</li>'
      '<li>Чужая музыка без прав.</li>'
      '<li>Лицо реального человека без согласия.</li>'
      '<li>Обещать в рекламе то, чего у продукта нет.</li></ul></div>'
    + '<div class="warn"><div class="h" style="color:#8fd08a">Так правильно</div><ul>'
      '<li class="ok">Своё лицо через reference, чужое только с согласия.</li>'
      '<li class="ok">Музыка без авторских претензий или лицензионная.</li>'
      '<li class="ok">Условный продукт подавай как имидж-ролик, не как фото товара.</li>'
      '<li class="ok">Текст и обещания правдивые.</li></ul></div>'))

# 21 errors
P.append(page("Шаг 15 · Ошибки", 21,
    head("Шаг 15", "Ошибки и фиксы", "Шесть граблей первого ролика.")
    + '<div class="fix">'
      '<div class="r"><b>Сцены вразнобой.</b> Фикс: один свет и грейд во всех промптах.</div>'
      '<div class="r"><b>Лицо чужое или плывёт.</b> Фикс: reference + «keep face natural, no distortion».</div>'
      '<div class="r"><b>Текст в кадре кривой.</b> Фикс: не вшивай текст в генерацию, добавляй на монтаже.</div>'
      '<div class="r"><b>Ролик затянут.</b> Фикс: сцены по 1–2 сек, склейки на бит, сильный кадр в начало.</div>'
      '<div class="r"><b>Сожгли кредиты.</b> Фикс: 5 секунд и 2–3 дубля, не длиннее.</div>'
      '<div class="r"><b>Немой ролик.</b> Фикс: музыка + звуки атмосферы обязательно.</div></div>'))

# 22 action
P.append(page("Шаг 16 · Действие", 22,
    head("Шаг 16", "Сделай сейчас", "Собери первый ролик из 4–5 сцен за один заход.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Выбери тему и 4–5 сцен</b> (общий → деталь → герой → финал).</div></div>'
      '<div class="step"><div class="sx"><b>Собери промпты</b> из библиотеки и справочников, единый свет.</div></div>'
      '<div class="step"><div class="sx"><b>Сгенерь по 2–3 дубля,</b> возьми лучшие.</div></div>'
      '<div class="step"><div class="sx"><b>Смонтируй:</b> темп, грейд, музыка, подписи, экспорт 9:16.</div></div></div>'
    + '<div class="callout check"><div class="h">Проверь перед публикацией</div>'
      '<div class="row">Первые 2 секунды цепляют.</div>'
      '<div class="row">Единый свет и грейд во всех сценах.</div>'
      '<div class="row">Планы чередуются, ролик не монотонный.</div>'
      '<div class="row">Есть музыка и звук, подписи читаются.</div>'
      '<div class="row">Лица и продукт без искажений, ничего не выдаёт за реальную съёмку.</div></div>'))

# 23 course
P.append(page("Дальше", 23,
    head("Дальше", "Ролик — это один результат. А есть система", "Ты собрал клип за вечер. На курсе собираешь метод под любые видео.")
    + '<p>Один ролик — хорошо. Но сила в системе: как ставить кадр, держать стиль, добавлять голос и аватар, собирать конвейер из сцен и монтажа. Это «Земля Видео» и «Земля Звук» в курсе «Нейросети и ChatGPT для каждого».</p>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Голос и дубляж</div><p>Закадр и озвучка своим голосом на 90+ языков.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Аватар</div><p>Цифровой двойник, который говорит в кадре.</p></div>'
      '<div class="card"><div class="ct">На курсе</div><div class="ch">Конвейер</div><p>Сцена → монтаж → публикация как система.</p></div></div>'
    + '<p>Ролик без камеры это вход. Дальше ты перестаёшь заказывать съёмку и собираешь видео сам.</p>'))

# 24 team
P.append(page("Команда", 24,
    head("Путь дальше", "Путь в команду AlovLab", "Начало получаться и хочется делать для брендов — есть куда расти.")
    + '<div class="team"><div class="h">Снимаешь ролики уверенно?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты: собирают AI-рекламу и промо под бренды, набивают портфолио на живых кейсах и растут рядом с командой.</p>'
      '<div class="dirs"><span>AI-реклама</span><span>Промо-ролики</span><span>Аватары и дубляж</span><span>Контент-конвейеры</span></div>'
      '<p style="margin-top:8px">Это работа и практика, а не обещание трудоустройства. Но дорога открыта: покажи, что доводишь ролик до результата.</p></div>'
    + '<p>Бизнесу, которому нужна AI-реклама под ключ — это AlovLab Studio. Отправляешь бриф, продакшн и конвейер берём на себя.</p>'))

# 25 contacts
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Автоконтент</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Не арендуй съёмку. Сними словами.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Все промпты, справочники и разбор — в этой методичке. Забирай в Telegram. Нужна AI-реклама под бренд — отправь бриф в студию.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Бриф студии · @alovlab</span>
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">alovlab.ru</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))
