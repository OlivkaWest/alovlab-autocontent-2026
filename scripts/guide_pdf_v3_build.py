# -*- coding: utf-8 -*-
"""AlovLab · методичка Higgsfield v3 — редакторская пересборка в кейс-драму.
Один реальный проект (ресторанный Reels из 4 кадров) ведётся от исходника к готовому ролику.
База вёрстки — из v2 (фикс-A4, светлые страницы, тёмные плашки). Добавлены визуальные доказательства."""
import base64, pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, page, LOGO, HERO, TRUFFLE, HANDS, INTERIOR, b64, ROOT

AVATAR = b64(ROOT / "content/carousel-assets/restaurant" / "hf_20260805_140559_e09977d3-1fba-4645-8d01-95522ce3eee8.png")
OUTDIR = ROOT / "exports" / "higgsfield-guide" / "v3-redesign"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "higgsfield-restaurant-reels-guide-v3.html"

EXTRA = r"""
/* кадр */
.frame{border-radius:12px;overflow:hidden;border:1px solid var(--line);background:#fff;position:relative}
.frame img{width:100%;display:block;object-fit:cover}
.frame .flabel{position:absolute;top:8px;left:8px;font-weight:800;font-size:7.5pt;letter-spacing:.08em;text-transform:uppercase;
 color:#fff;background:rgba(19,16,10,.72);padding:4px 8px;border-radius:6px}
.fcap{font-size:8.5pt;color:var(--muted);margin-top:6px;line-height:1.35}.fcap b{color:var(--ink)}

/* карта ролика */
.scenemap{display:grid;grid-template-columns:repeat(5,1fr);gap:9px;margin:14px 0}
.sm{background:#fff;border:1px solid var(--line);border-radius:11px;overflow:hidden}
.sm .t{position:relative}.sm img{width:100%;height:96px;object-fit:cover;display:block}
.sm .n{position:absolute;top:6px;left:6px;width:20px;height:20px;border-radius:6px;background:var(--o);color:#fff;font-weight:800;font-size:9pt;display:grid;place-items:center}
.sm .b{padding:9px 10px}.sm .b .h{font-weight:800;font-size:8.5pt;color:var(--ink);line-height:1.18}
.sm .b .d{font-size:7pt;color:var(--muted);margin-top:4px;line-height:1.35}

/* анатомия промпта */
.anatomy{display:grid;gap:7px;margin:12px 0}
.anatomy .a{display:grid;grid-template-columns:104px 1fr;gap:11px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:9px;padding:8px 12px}
.anatomy .a .k{font-weight:800;font-size:7pt;letter-spacing:.05em;text-transform:uppercase;color:#fff;background:var(--o);border-radius:5px;padding:6px 6px;text-align:center;line-height:1.1}
.anatomy .a .v{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:9pt;color:var(--ink)}
.anatomy .a.neg .k{background:#8a5a2a}

/* карточки инструментов вход→выход */
.tc{background:#fff;border:1px solid var(--line);border-radius:13px;padding:15px 16px;margin:11px 0}
.tc .th{display:flex;align-items:baseline;gap:10px;margin-bottom:10px}
.tc .th .nm{font-weight:800;font-size:14pt;color:var(--ink)}
.tc .th .fn{font-size:9pt;color:var(--muted)}
.tc .io{display:grid;grid-template-columns:1fr 26px 1fr;gap:9px;align-items:stretch}
.tc .io .cell{background:#faf6ef;border:1px solid var(--line);border-radius:9px;padding:10px 12px;font-size:9.3pt;line-height:1.4;color:var(--body)}
.tc .io .cell .cl{font-weight:800;font-size:7pt;letter-spacing:.08em;text-transform:uppercase;color:var(--o);display:block;margin-bottom:4px}
.tc .io .arr{display:grid;place-items:center;color:var(--o);font-weight:800;font-size:15pt}

/* монтажный таймлайн */
.tl-track{display:flex;gap:3px;height:38px;margin:12px 0 6px}
.tl-seg{display:flex;align-items:center;justify-content:center;font-weight:800;font-size:7pt;color:#fff;text-transform:uppercase;letter-spacing:.03em;border-radius:7px;text-align:center;line-height:1.05;padding:0 3px}
.tl-row{display:grid;grid-template-columns:74px 1fr;gap:10px;align-items:center;margin:8px 0;font-size:9pt}
.tl-row .lab{font-weight:800;color:var(--ink);font-size:8pt;text-transform:uppercase;letter-spacing:.05em}
.tl-row .bar{height:10px;border-radius:5px}

/* слот под реальный скрин */
.shot{border:1.5px dashed #cbbfa9;border-radius:11px;padding:15px 16px;background:#f4edE0;background:#f4ede0;margin:10px 0;display:flex;gap:12px;align-items:center}
.shot .ic{width:34px;height:34px;border-radius:9px;background:var(--o-tint);color:var(--o);display:grid;place-items:center;font-weight:800;font-size:13pt;flex:0 0 auto}
.shot .sh{font-weight:800;font-size:8.5pt;letter-spacing:.05em;text-transform:uppercase;color:var(--o)}
.shot .sd{font-size:9pt;color:var(--muted);line-height:1.4;margin-top:2px}

/* визуальный чек-лист по блокам */
.vcheck{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin:12px 0}
.vg{background:#fff;border:1px solid var(--line);border-radius:11px;padding:12px 14px}
.vg .gh{font-weight:800;font-size:8.5pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:8px}
.vg .row{display:flex;gap:8px;font-size:9pt;line-height:1.35;color:var(--body);margin:6px 0}
.vg .row::before{content:"";flex:0 0 auto;width:12px;height:12px;border-radius:4px;border:1.5px solid var(--o);background:var(--o-tint);margin-top:1px}
"""
CSS = V2CSS + EXTRA

def frame(img, label, height=150):
    return f'<div class="frame"><span class="flabel">{label}</span><img src="data:image/png;base64,{img}" style="height:{height}px"></div>'

PAGES = []

# P1 · Обложка (как в v2)
PAGES.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:url(data:image/png;base64,{HERO}) center/cover;opacity:.62"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(19,16,10,.35),rgba(19,16,10,.15) 38%,rgba(19,16,10,.97) 86%)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · разбор продакшна</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:15ch">Ресторанный Reels в Higgsfield — от четырёх кадров до готового ролика</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:38ch">Разбираем один реальный проект по сценам: исходник → оживление → результат → монтаж.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">9:16 · 25–35 сек</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Image-to-Video</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">аватар Нейромонах</span>
    </div>
  </div>
</section>""")

# P2 · Вот ролик, который собираем — КАРТА РОЛИКА
PAGES.append(page("Проект · карта ролика", 2, f"""
  <span class="kick">Проект</span>
  <h2>Вот ролик, который мы соберём</h2>
  <p class="lead">Пять сцен, 25–35 секунд. Аватар открывает и закрывает, между ними — ресторанный B-roll под голос. Каждый кадр внизу — реальный исходник этого проекта.</p>
  <div class="scenemap">
    <div class="sm"><div class="t"><span class="n">1</span><img src="data:image/png;base64,{AVATAR}"></div><div class="b"><div class="h">Аватар · хук</div><div class="d">2–4 сек · говорит · останавливает</div></div></div>
    <div class="sm"><div class="t"><span class="n">2</span><img src="data:image/png;base64,{HERO}"></div><div class="b"><div class="h">Гребешок</div><div class="d">3–4 сек · push-in · аппетит</div></div></div>
    <div class="sm"><div class="t"><span class="n">3</span><img src="data:image/png;base64,{HANDS}"></div><div class="b"><div class="h">Руки шефа</div><div class="d">2–3 сек · min · забота</div></div></div>
    <div class="sm"><div class="t"><span class="n">4</span><img src="data:image/png;base64,{INTERIOR}"></div><div class="b"><div class="h">Интерьер</div><div class="d">3–4 сек · dolly · вечер</div></div></div>
    <div class="sm"><div class="t"><span class="n">5</span><img src="data:image/png;base64,{TRUFFLE}"></div><div class="b"><div class="h">Трюфель + финал</div><div class="d">3–5 сек · push-in · зовём</div></div></div>
  </div>
  <div class="cards c3">
    <div class="card"><div class="ct">Формат</div><div class="ch">9:16 · 1080×1920</div><p>Reels, VK Клипы, Shorts.</p></div>
    <div class="card"><div class="ct">Инструменты</div><div class="ch">Higgsfield + HeyGen</div><p>Оживление кадров + говорящий аватар.</p></div>
    <div class="card"><div class="ct">Что получишь</div><div class="ch">Готовый MP4</div><p>Вертикальный ролик под публикацию.</p></div>
  </div>
  <div class="callout result"><div class="h">Как читать методичку</div><p>Идём по сценам этого проекта. На каждой: исходник, задача, промпт, что двигается, где ломается и как чинить.</p></div>
""", ))

# P3 · Что подготовить
PAGES.append(page("Подготовка", 3, f"""
  <span class="kick">Подготовка</span>
  <h2>Что собрать до старта</h2>
  <p class="lead">Всё под рукой — не будешь метаться между вкладками посреди работы.</p>
  <div class="cards c3">
    <div class="card"><div class="ct">Визуал</div><div class="ch">4 кадра</div><p>Гребешок, руки, интерьер, трюфель.</p></div>
    <div class="card"><div class="ct">Герой</div><div class="ch">Аватар</div><p>Образ для вступления и финала.</p></div>
    <div class="card"><div class="ct">Смысл</div><div class="ch">Сценарий</div><p>Готовый — на стр. 13.</p></div>
    <div class="card"><div class="ct">Звук</div><div class="ch">Голос</div><p>Закадр, спокойная подача.</p></div>
    <div class="card"><div class="ct">Атмосфера</div><div class="ch">Музыка</div><p>Кинематографичная, ниже голоса.</p></div>
    <div class="card"><div class="ct">Финал</div><div class="ch">Логотип PNG</div><p>Прозрачный фон, только в конце.</p></div>
  </div>
  <div class="prompt" style="padding:14px 16px">
    <div class="plbl"><span class="tag">Папка проекта</span></div>
    <code>restaurant_video/
  01_references/   02_higgsfield/   03_avatar/   04_voice/
  05_music/        06_logo/         07_edit/     08_export/</code>
  </div>
  <p>Имена по-человечески: <span class="o">01_scallop_source.png</span>, не <span class="o">final2.png</span>. На монтаже сэкономит полчаса поиска удачного дубля.</p>
""", ))

# P4 · Как читать кадр под видео
PAGES.append(page("Кадр · требования", 4, f"""
  <span class="kick">Кадр</span>
  <h2>Какой исходник оживёт, а какой сломается</h2>
  <p class="lead">Кадр должен выглядеть как хороший первый кадр видео. Плохой исходник не спасёт ни один промпт.</p>
  <div class="imgpair">
    <figure><img src="data:image/png;base64,{HERO}"><figcaption><b>Подходит.</b> Объект целиком, тёплый боковой свет, воздух сверху под пар и наезд.</figcaption></figure>
    <figure><img src="data:image/png;base64,{INTERIOR}"><figcaption><b>Подходит.</b> Глубина и коридор, по которому камера проедет вперёд.</figcaption></figure>
  </div>
  <div class="gb">
    <div class="box good"><div class="lbl">✓ Хороший</div>Вертикаль 9:16, объект в центре, единый тёплый свет, тёмный фон, высокое разрешение.</div>
    <div class="box bad"><div class="lbl">✕ Плохой</div>Объект обрезан краем, каша по свету, текст на кадре, лишние пальцы, битая посуда, сильное размытие.</div>
  </div>
""", ))

# P5 · Как оживляем в Higgsfield (шаги + слоты под скрины)
PAGES.append(page("Higgsfield · процесс", 5, f"""
  <span class="kick">Higgsfield</span>
  <h2>Как оживить кадр</h2>
  <p class="lead">Названия кнопок иногда меняются — держись логики. Сначала один тест, потом объём.</p>
  <div class="steps">
    <div class="step"><div class="sx"><b>Image-to-Video</b> → загрузи исходный кадр, поставь <b>9:16</b>.</div></div>
    <div class="step"><div class="sx"><b>Короткая длительность</b> (3–4 сек) + движение камеры.</div></div>
    <div class="step"><div class="sx"><b>Впиши промпт</b> и запусти <b>один</b> тестовый дубль.</div></div>
    <div class="step"><div class="sx"><b>Досмотри до конца</b>, скачай только удачный. Повтори для сцен.</div></div>
  </div>
  <div class="shot"><div class="ic">▣</div><div><div class="sh">Сюда — реальный скрин</div><div class="sd">Кадрируй область: выбор режима Image-to-Video и загрузку кадра. Стрелка + подпись, без всего интерфейса.</div></div></div>
  <div class="shot"><div class="ic">▣</div><div><div class="sh">Сюда — реальный скрин</div><div class="sd">Поле промпта и выбор движения камеры. Выдели нужную кнопку.</div></div></div>
  <div class="callout result"><div class="h">Один кадр — одно движение</div><p>Чем меньше просишь, тем меньше модель фантазирует. Быстрый наезд + облёт + смена света в одном промпте = каша.</p></div>
""", ))

# P6 · Анатомия промпта
PAGES.append(page("Промпт · анатомия", 6, f"""
  <span class="kick">Промпт</span>
  <h2>Из чего собран рабочий промпт</h2>
  <p class="lead">Каждый промпт — это шесть частей. Собери их по порядку, и модель поймёт, что двигать, а что держать.</p>
  <div class="anatomy">
    <div class="a"><div class="k">Объект</div><div class="v">premium scallop dish</div></div>
    <div class="a"><div class="k">Стабильность</div><div class="v">stays completely stable</div></div>
    <div class="a"><div class="k">Камера</div><div class="v">slow cinematic push-in</div></div>
    <div class="a"><div class="k">Среда</div><div class="v">delicate steam rises and curls</div></div>
    <div class="a"><div class="k">Свет</div><div class="v">warm amber side light</div></div>
    <div class="a neg"><div class="k">Ограничения</div><div class="v">no deformation, no new ingredients</div></div>
  </div>
  <div class="callout result"><div class="h">Правило</div><p>Двигается фон и камера — не сам объект. Стабильность и ограничения прописываем всегда, иначе еда «поплывёт».</p></div>
""", ))

# ---- сцена-страницы ----
def scene_page(kick, num, section, title, img, task, code, ru, move, stay, err, ok):
    return page(section, num, f"""
  <span class="kick">{kick}</span>
  <h2>{title}</h2>
  <div style="display:grid;grid-template-columns:150px 1fr;gap:15px;align-items:center;margin:10px 0 4px">
    {frame(img,'Исходник',150)}
    <div><div style="font-weight:800;font-size:8.5pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px">Задача сцены</div>
      <p style="font-size:10.5pt;line-height:1.5;margin:0">{task}</p></div>
  </div>
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
    <div class="box bad"><div class="lbl">✕ Где ломается</div>{err}</div>
    <div class="box good"><div class="lbl">✓ Что получаем</div>{ok}</div>
  </div>
""")

PAGES.append(scene_page("Сцена 2 · Гребешок", 7, "Сцена · Гребешок", "Оживляем гребешок", HERO,
  "Разжечь аппетит за 3–4 секунды. Камера медленно входит, пар поднимается — блюдо остаётся собой.",
  "A gourmet scallop dish stays completely stable while the camera makes a slow cinematic push-in. Delicate steam rises and gently curls upward. Soft warm amber side light glides across the glossy sauce. Dark elegant restaurant background, no deformation, no new ingredients.",
  "блюдо стабильно, медленный наезд, пар вьётся, тёплый свет по соусу.",
  "камера (push-in), пар, блик света.", "блюдо, тарелка, состав.",
  "быстрый наезд — гребешок «дышит» и плывёт.", "живой пар, плавный наезд, соус блестит — кадр дорогой."))

PAGES.append(scene_page("Сцена 3 · Руки шефа", 8, "Сцена · Руки шефа", "Оживляем руки шефа", HANDS,
  "Показать заботу. Самая хрупкая сцена: движение минимальное, иначе ломаются пальцы.",
  "A chef's hands slowly and gently place a finished plate onto the table. The hand movement is small and natural, fingers keep correct anatomy. The plate keeps its shape. A very soft push-in. No extra fingers, no additional hands, no changing dish.",
  "руки аккуратно ставят тарелку, мелкое движение, пальцы анатомичны, лёгкий наезд.",
  "кисти (чуть), лёгкий push-in.", "тарелка, блюдо, вторая рука.",
  "большое движение рук — лишние пальцы и «резиновые» кисти.", "руки нормальные, тарелка встала мягко, блюдо не изменилось."))

PAGES.append(scene_page("Сцена 4 · Интерьер", 9, "Сцена · Интерьер", "Оживляем интерьер", INTERIOR,
  "Обещать вечер. Здесь работает проезд камеры — геометрия зала должна остаться на месте.",
  "An upscale restaurant interior at dusk. The camera performs a slow cinematic dolly forward. Candle flames flicker gently, warm bokeh shimmers. The room keeps its geometry, tables and chairs stay in place. No people appearing, no morphing walls.",
  "медленный проезд вперёд, пламя дрожит, боке мерцает, геометрия сохраняется.",
  "камера (dolly), пламя, боке.", "стены, столы, стулья, перспектива.",
  "быстрый проезд — интерьер «перестраивается».", "плавный проезд, зал стабилен, атмосфера дорогая."))

# P10 · Трюфель + ограничения
PAGES.append(page("Сцена 5 · Трюфель", 10, "Сцена · Трюфель", f"""
  <span class="kick">Сцена 5 · Трюфель</span>
  <h2>Оживляем финальное блюдо</h2>
  <div style="display:grid;grid-template-columns:150px 1fr;gap:15px;align-items:center;margin:10px 0 4px">
    {frame(TRUFFLE,'Исходник',150)}
    <div><div style="font-weight:800;font-size:8.5pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px">Задача сцены</div>
      <p style="font-size:10.5pt;line-height:1.5;margin:0">Финальный герой. Золотой блик легко превращается в огонь — держим его мягким.</p></div>
  </div>
  <div class="prompt">
    <div class="plbl"><span class="tag">Готовый промпт · скопировать</span></div>
    <code>A luxury truffle dish stays perfectly stable while the camera makes a slow push-in. Steam softly curls upward. A warm golden highlight slowly travels along the rim of the plate. The truffle keeps its exact shape. No new ingredients, no deformation, no fire, no text.</code>
    <div class="ru"><b>По-русски:</b> трюфель стабилен, наезд, пар вьётся, золотой блик едет по краю тарелки.</div>
  </div>
  <div class="prompt" style="padding:13px 16px">
    <div class="plbl"><span class="tag">Negative — держи коротким</span></div>
    <code>no deformation, no morphing, no extra fingers, no changing ingredients, no floating objects, no sudden camera movement, no flickering, no text</code>
  </div>
  <p class="note">Длинный negative-список путает модель не хуже плохого фото.</p>
""", ))

# P11 · Камера + длительность
PAGES.append(page("Камера · длительность", 11, f"""
  <span class="kick">Камера</span>
  <h2>Движение и длительность</h2>
  <p class="lead">Правило, которое спасает кредиты: чем сложнее кадр, тем спокойнее движение.</p>
  <table>
    <tr><th>Движение</th><th>Где</th><th>Риск</th></tr>
    <tr><td><b>Push-in</b> — наезд</td><td>еда, финал</td><td>еда «дышит», если быстро</td></tr>
    <tr><td><b>Dolly</b> — проезд</td><td>интерьер</td><td>геометрия плывёт</td></tr>
    <tr><td><b>Static</b> — почти стоит</td><td>сложные кадры</td><td>безопасно, но вяло</td></tr>
  </table>
  <div class="cards c3">
    <div class="card"><div class="ct">Аватар</div><div class="ch">2–4 сек</div></div>
    <div class="card"><div class="ct">Гребешок</div><div class="ch">3–4 сек</div></div>
    <div class="card"><div class="ct">Руки</div><div class="ch">2–3 сек</div></div>
    <div class="card"><div class="ct">Интерьер</div><div class="ch">3–4 сек</div></div>
    <div class="card"><div class="ct">Трюфель</div><div class="ch">3–4 сек</div></div>
    <div class="card"><div class="ct">Финал+лого</div><div class="ch">3–5 сек</div></div>
  </div>
""", ))

# P12 · Оценка + ошибки
PAGES.append(page("Оценка · ошибки", 12, f"""
  <span class="kick">Контроль</span>
  <h2>Как отбраковать клип</h2>
  <p class="lead">Красивый кадр с деформацией — это брак. На большом экране косяк вылезет.</p>
  <div class="callout check"><div class="h">Клип годный, если</div>
    <div class="row">Объект сохранил форму, посуда не деформируется</div>
    <div class="row">Камера плавно, без скачков и мерцания</div>
    <div class="row">Пар выглядит паром, руки анатомичны</div>
    <div class="row">Фон не перестраивается, клип встаёт в монтаж</div>
  </div>
  <h3>Проблема → решение (вписать в промпт)</h3>
  <div class="fix">
    <div class="r"><b>Блюдо плавится.</b> → <code>slow push-in, food stays stable</code></div>
    <div class="r"><b>Лишние пальцы.</b> → <code>small hand motion, no extra fingers</code></div>
    <div class="r"><b>Интерьер плывёт.</b> → <code>room keeps geometry</code></div>
    <div class="r"><b>Блик как огонь.</b> → <code>soft warm highlight, no fire</code></div>
  </div>
""", ))

# P13 · Аватар + сценарий
PAGES.append(page("Аватар · сценарий", 13, f"""
  <span class="kick">Аватар</span>
  <h2>Кто говорит и что</h2>
  <div style="display:grid;grid-template-columns:130px 1fr;gap:15px;align-items:center;margin:10px 0">
    {frame(AVATAR,'Аватар',150)}
    <div><p style="font-size:10.5pt;line-height:1.55;margin:0">Генерь аватара <strong>отдельно</strong> от ресторана: тёмный фон, крупный план, янтарный контровой свет, взгляд в камеру. Сложный фон + живая речь = сломанное лицо.</p></div>
  </div>
  <h3>Готовый сценарий · 25–35 секунд</h3>
  <div class="cards" style="gap:9px">
    <div class="card"><div class="ct">Аватар · хук</div><p style="font-size:10.5pt;color:var(--ink);line-height:1.5">«В слабом ресторане тебе подают блюдо. В сильном — сначала меняют твой вечер».</p></div>
    <div class="card"><div class="ct">Закадр · поверх B-roll</div><p style="font-size:10.5pt;color:var(--ink);line-height:1.5">«Пар над тарелкой — это обещание. Свет, тишина, подача — вечер собирается до первого кусочка. Ты не заказываешь ужин. Ты бронируешь память».</p></div>
    <div class="card"><div class="ct">Аватар · финал</div><p style="font-size:10.5pt;color:var(--ink);line-height:1.5">«Хочешь такой вечер — стол уже ждёт. Бронь под роликом».</p></div>
  </div>
""", ))

# P14 · Инструменты + монтажный таймлайн
PAGES.append(page("Инструменты · монтаж", 14, f"""
  <span class="kick">Сборка</span>
  <h2>Инструменты и монтаж</h2>
  <div class="tc">
    <div class="th"><span class="nm">Higgsfield</span><span class="fn">оживление кадров</span></div>
    <div class="io"><div class="cell"><span class="cl">Вход</span>Статичный кадр блюда 9:16</div><div class="arr">→</div><div class="cell"><span class="cl">Выход</span>Клип 3–4 сек с движением камеры</div></div>
  </div>
  <div class="tc">
    <div class="th"><span class="nm">HeyGen</span><span class="fn">говорящий аватар</span></div>
    <div class="io"><div class="cell"><span class="cl">Вход</span>Фраза + образ аватара</div><div class="arr">→</div><div class="cell"><span class="cl">Выход</span>Клип с синхронной речью</div></div>
  </div>
  <h3>Монтажный таймлайн</h3>
  <div class="tl-track">
    <div class="tl-seg" style="flex:3;background:#c0492a">Аватар</div>
    <div class="tl-seg" style="flex:4;background:#DA5F1E">Гребешок</div>
    <div class="tl-seg" style="flex:3;background:#e07a2a">Руки</div>
    <div class="tl-seg" style="flex:4;background:#DA5F1E">Интерьер</div>
    <div class="tl-seg" style="flex:4;background:#e07a2a">Трюфель</div>
    <div class="tl-seg" style="flex:4;background:#c0492a">Финал+лого</div>
  </div>
  <div class="tl-row"><span class="lab">Голос</span><span class="bar" style="background:linear-gradient(90deg,#1b1712,#1b1712)"></span></div>
  <div class="tl-row"><span class="lab">Музыка</span><span class="bar" style="background:#d9cdba"></span></div>
  <div class="tl-row"><span class="lab">Субтитры</span><span class="bar" style="background:#f2d3bf"></span></div>
  <p class="note">Голос всегда громче музыки. Склейки встык, dissolve — только между кадрами еды. Логотип — только в финале.</p>
""", ))

# P15 · Субтитры + экспорт
PAGES.append(page("Субтитры · экспорт", 15, f"""
  <span class="kick">Финиш</span>
  <h2>Субтитры и экспорт</h2>
  <div class="cards c2">
    <div class="card"><div class="ct">Субтитры</div><div class="ch">Крупно, снизу, 2 строки</div><p>Белый текст, мягкая тень, ключевое слово оранжевым. Не перекрывают лицо и блюдо.</p></div>
    <div class="card"><div class="ct">Пример</div><div class="ch">«Ты бронируешь память»</div><p>Блок 1: «Ты не заказываешь ужин». Блок 2: «Ты бронируешь <span class="o">ПАМЯТЬ</span>».</p></div>
  </div>
  <div class="cards c3">
    <div class="card"><div class="ct">Формат</div><div class="ch">9:16 · 1080×1920</div></div>
    <div class="card"><div class="ct">Файл</div><div class="ch">MP4 · H.264</div></div>
    <div class="card"><div class="ct">Проверка</div><div class="ch">на телефоне</div></div>
  </div>
  <div class="callout result"><div class="h">Перед экспортом</div><p>Посмотри без звука (читается ли картинка) и со звуком (не давит ли музыка голос). Потом — на телефоне.</p></div>
""", ))

# P16 · Визуальный чек-лист
PAGES.append(page("Чек-лист", 16, f"""
  <span class="kick">Контроль</span>
  <h2>Финальный чек-лист по блокам</h2>
  <p class="lead">Пройди перед публикацией. Один блок — одна зона ответственности.</p>
  <div class="vcheck">
    <div class="vg"><div class="gh">Кадр</div><div class="row">объект не деформируется</div><div class="row">стиль и свет совпадают</div></div>
    <div class="vg"><div class="gh">Движение</div><div class="row">камера плавная</div><div class="row">нет мерцания и скачков</div></div>
    <div class="vg"><div class="gh">Голос</div><div class="row">слышен и громче музыки</div><div class="row">лицо аватара стабильно</div></div>
    <div class="vg"><div class="gh">Монтаж</div><div class="row">ритм держит внимание</div><div class="row">логотип только в финале</div></div>
    <div class="vg"><div class="gh">Экспорт</div><div class="row">9:16, MP4, H.264</div><div class="row">нет случайного текста</div></div>
    <div class="vg"><div class="gh">Публикация</div><div class="row">первые 2 сек цепляют</div><div class="row">проверено на телефоне</div></div>
  </div>
  <div class="callout result"><div class="h">Задание</div><p>Сдать: 4 исходника, 4 промпта, 4 клипа, финальный ролик и разбор — какие артефакты вылезли и как ты их починил.</p></div>
""", ))

# P17 · Все промпты + маршрут + контакты (тёмная, как в v2)
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

HTML = f'<meta charset="utf-8"><title>Higgsfield · ресторанный Reels · AlovLab · v3</title><style>{CSS}</style>' + "\n".join(PAGES)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(PAGES))
