# -*- coding: utf-8 -*-
"""AlovLab · методичка «MIDJOURNEY + NANO BANANA — профессиональная система визуалов».
Самостоятельный премиум-гайд (фикс-A4, светлая основа, тёмные плашки под промпты). База CSS — v2.
Параметры выверены по актуальной документации на 08.2026 (MJ V8.2, Nano Banana Pro = Gemini 3 Pro Image).
Собирается партиями. Запуск: python3 scripts/guide_mj_nb_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "mj-nano-banana"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-mj-nano-banana.html"

EXTRA = r"""
.lede2{font-size:12pt;line-height:1.6;color:var(--muted);margin:6px 0 14px;max-width:62ch}
/* ver">was→now, роли */
.wn{display:grid;grid-template-columns:1fr 26px 1fr;gap:10px;align-items:center;margin:9px 0}
.wn .old{background:#fbeeea;border:1px solid #f0cabb;border-radius:11px;padding:11px 13px}
.wn .new{background:#eef6ea;border:1px solid #cfe3c6;border-radius:11px;padding:11px 13px}
.wn .ar{color:var(--o);font-weight:800;font-size:15pt;text-align:center}
.wn .lbl{font-weight:800;font-size:7.5pt;letter-spacing:.08em;text-transform:uppercase;margin-bottom:5px}
.wn .old .lbl{color:#c0492a}.wn .new .lbl{color:#3f7d34}
.wn code{font-family:ui-monospace,Menlo,monospace;font-size:9pt;color:#8a5a2a;background:#f1e9db;padding:1px 5px;border-radius:4px}
.wn .new code{color:#3f7d34;background:#e2efdb}
.wn p{font-size:8.8pt;margin:5px 0 0;color:var(--body);line-height:1.35;max-width:none}
/* факты-плашки */
.facts{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}
.factcard{border:1px solid var(--line);border-radius:13px;padding:15px 16px;background:#fff}
.factcard h4{font-weight:800;font-size:12pt;color:var(--ink);margin:0 0 3px}
.factcard .sub{font-size:8.5pt;color:var(--o);font-weight:700;text-transform:uppercase;letter-spacing:.04em;margin-bottom:9px}
.factcard .f{font-size:9.4pt;line-height:1.4;color:var(--body);padding:5px 0;border-top:1px solid var(--line2);display:grid;grid-template-columns:1fr;gap:2px}
.factcard .f:first-of-type{border-top:none}
.factcard .f b{color:var(--ink)}
.factcard code{font-family:ui-monospace,Menlo,monospace;font-size:8.6pt;color:#8a5a2a;background:#f1e9db;padding:1px 5px;border-radius:4px}
/* prompt stack */
.stack{counter-reset:sk;display:grid;grid-template-columns:1fr 1fr;gap:7px 16px;margin:12px 0}
.sk{display:grid;grid-template-columns:24px 1fr;gap:9px;align-items:start}
.sk::before{counter-increment:sk;content:counter(sk);width:22px;height:22px;border-radius:6px;background:var(--ink);color:#fff;
 font-weight:800;font-size:9pt;display:grid;place-items:center;margin-top:1px}
.sk .n{font-weight:800;font-size:9.5pt;color:var(--ink);line-height:1.25}
.sk .n i{display:block;font-style:normal;font-weight:500;font-size:8.3pt;color:var(--muted);margin-top:1px}
/* уровни */
.lv{border:1px solid var(--line);border-radius:12px;padding:13px 15px;background:#fff;margin:8px 0}
.lv .h{display:flex;align-items:baseline;gap:9px;margin-bottom:5px}
.lv .h b{font-weight:800;font-size:12pt;color:var(--o)}
.lv .h span{font-size:8.5pt;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:.05em}
.lv p{font-size:9.6pt;line-height:1.45;margin:0;color:var(--body);max-width:none}
/* анатомия */
.anat{display:flex;flex-direction:column;gap:5px;margin:12px 0}
.al{display:grid;grid-template-columns:120px 1fr;gap:11px;align-items:center}
.al .tag{font-weight:800;font-size:7.8pt;letter-spacing:.06em;text-transform:uppercase;color:#fff;padding:5px 9px;border-radius:6px;text-align:center}
.al .tx{font-size:9.4pt;line-height:1.35;color:var(--body)}
.al .tx code{font-family:ui-monospace,Menlo,monospace;font-size:8.8pt;color:#8a5a2a;background:#f1e9db;padding:1px 5px;border-radius:4px}
/* lock-шаблон */
.lock{background:var(--dark);border-radius:14px;padding:15px 17px;margin:11px 0}
.lock .plbl{display:flex;justify-content:space-between;align-items:center;margin-bottom:9px}
.lock .tag{font-weight:800;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px}
.lock code{display:block;font-family:'SF Mono',ui-monospace,Menlo,monospace;font-size:9pt;line-height:1.6;color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.lock code b{color:#fff;font-weight:700}
/* поля style bible */
.bible{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:11px 0}
.bf{background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 12px}
.bf .k{font-weight:800;font-size:7.6pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:3px}
.bf .v{font-size:9.5pt;color:var(--body);line-height:1.35}
.chiprow{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.chiprow span{font-size:8.6pt;font-weight:700;color:var(--body);background:#fff;border:1px solid var(--line);border-radius:16px;padding:5px 11px}
"""
CSS = V2CSS + EXTRA

FOOTLABEL = "AlovLab · Midjourney + Nano Banana"
def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>{FOOTLABEL}</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code, ru=None, copy=True):
    ru_html = f'<div class="ru">{ru}</div>' if ru else ''
    copy_html = '<span class="copy">скопировать</span>' if copy else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>{copy_html}</div>'
            f'<code>{code}</code>{ru_html}</div>')

P = []

# ============ P1 · Обложка ============
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(115% 68% at 82% 8%,#2e2214,#180f08 52%,#0b0906)"></div>
  <div style="position:absolute;left:-10%;top:44%;width:60%;height:60%;background:radial-gradient(circle,rgba(255,120,40,.14),transparent 68%)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:16px">Профессиональная система создания визуалов</div>
    <h1 style="font-weight:800;font-size:37pt;line-height:1.02;letter-spacing:-.02em;color:#fff">Midjourney<br><span style="color:var(--o2)">+ Nano&nbsp;Banana</span></h1>
    <p style="margin-top:18px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:44ch">Один создаёт визуальный мир. Второй его фиксирует, редактирует и продолжает. На выходе — серия с одним героем, одним стилем и кадрами под видеогенерацию.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Гайд + рабочая тетрадь</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">65+ промптов</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Актуально · 08.2026</span>
    </div>
  </div>
</section>""")

# ============ P2 · Как устроен документ / логика ============
P.append(page("Как читать эту методичку", 2, """
  <span class="kick">Главный принцип</span>
  <h2>Ты строишь не промпт. Ты строишь визуальную систему</h2>
  <p class="lede2">Цель не «написать красивый запрос», а собрать серию, которая держит одного героя, один продукт и один визуальный язык — в нескольких сценах и форматах, готовую отдать дальше в видео.</p>
  <div class="flow">
    <div class="node"><b>Midjourney</b><span>создаёт мир</span></div><div class="arr">→</div>
    <div class="node"><b>Nano Banana</b><span>фиксирует и правит</span></div><div class="arr">→</div>
    <div class="node"><b>Серия</b><span>один язык</span></div><div class="arr">→</div>
    <div class="node"><b>Video</b><span>Higgsfield · Kling</span></div>
  </div>
  <div class="term"><b>Midjourney</b> — <span>рождает визуальный мир с нуля: свет, стиль, эстетику, master-кадр.</span></div>
  <div class="term"><b>Nano Banana</b> — <span>берёт готовый кадр и намеренно его меняет: фон, одежду, сцену — удерживая лицо и объект.</span></div>
  <div class="term"><b>Серия</b> — <span>несколько кадров, которые читаются как одна кампания: один герой, один продукт, один визуальный паспорт.</span></div>
  <div class="callout result"><div class="h">Эта методичка глубоко раскрывает только этап изображения</div><p>Видео — следующий этап конвейера AlovLab. Здесь мы доводим картинку до состояния «готовый первый кадр под I2V».</p></div>
"""))

# ============ P3 · Актуальность на дату ============
P.append(page("Проверено на дату · 08.2026", 3, """
  <span class="kick">Актуальность</span>
  <h2>Что считается «текущим» на момент этого гайда</h2>
  <p class="lede2">Модели и параметры меняются быстро. Ниже — состояние на август 2026, сверенное с официальной документацией. Если у тебя интерфейс отличается — доверяй документации, а не скриншотам из старых статей.</p>
  <div class="facts">
    <div class="factcard"><div class="sub">Изображение с нуля</div><h4>Midjourney V8.2</h4>
      <div class="f"><span><b>Дефолт с 24.07.2026.</b> До этого: V7 (до 09.06), V8.1 (10.06–23.07).</span></div>
      <div class="f"><span>Нативный <b>2K</b>, чётче типографика, Personalization.</span></div>
      <div class="f"><span>Консистентность — <code>--oref</code> + <code>--ow</code> (Omni Reference).</span></div>
      <div class="f"><span>Живы: <code>--sref</code>, <code>--sw</code>, <code>--stylize</code>, <code>--style raw</code>, <code>--ar</code>.</span></div>
    </div>
    <div class="factcard"><div class="sub">Правки и консистентность</div><h4>Nano Banana Pro</h4>
      <div class="f"><span>Официально — <b>Gemini 3 Pro Image</b> (GA 06.2026). База — Gemini 2.5 Flash Image.</span></div>
      <div class="f"><span>До <b>14 референсов</b> в одну сцену, лица до <b>5 людей</b>.</span></div>
      <div class="f"><span>Текст в кадре <b>94–96%</b>, многоязычный. Вывод <b>1K / 2K / 4K</b>.</span></div>
      <div class="f"><span>Локальные правки, свет, камера, грудинг. Метка <b>SynthID</b>.</span></div>
    </div>
  </div>
  <p class="note">«Nano Banana 2» — народное имя, официально это <b>Nano Banana Pro / Gemini 3 Pro Image</b>. Простые быстрые правки тянет и базовый Nano Banana; премиум-серии, текст и 4K — Pro.</p>
"""))

# ============ P4 · БЫЛО → СТАЛО ============
P.append(page("Не тащи устаревшее", 4, """
  <span class="kick">Было → стало</span>
  <h2>Параметры прошлых поколений, которые больше не основа</h2>
  <p class="lede2">Старые гайды до сих пор учат конструкциям из V6. В V8 путь другой. Показываю замену, чтобы ты не строил работу на том, что уже не работает как раньше.</p>
  <div class="wn">
    <div class="old"><div class="lbl">✕ Было · V6</div><code>--cref [url] --cw 100</code><p>Character Reference — держал лицо персонажа.</p></div>
    <div class="ar">→</div>
    <div class="new"><div class="lbl">✓ Стало · V8</div><code>--oref [url] --ow 100</code><p>Omni Reference: лицо, объект, логотип. <code>--ow</code> 0–1000, лок 400–600.</p></div>
  </div>
  <div class="wn">
    <div class="old"><div class="lbl">✕ Было</div><code>--v 6</code><p>Приходилось явно указывать версию модели.</p></div>
    <div class="ar">→</div>
    <div class="new"><div class="lbl">✓ Стало</div><code>(ничего)</code><p>Дефолт — V8.2. Версию пишем, только если целимся в старую.</p></div>
  </div>
  <div class="wn">
    <div class="old"><div class="lbl">✕ Опасный миф</div><code>--seed = тот же персонаж</code><p>«Один seed — одно лицо». Это неправда.</p></div>
    <div class="ar">→</div>
    <div class="new"><div class="lbl">✓ Правда</div><code>seed = стартовый шум</code><p>Воспроизводит точку старта. Личность держит <code>--oref</code>, не seed.</p></div>
  </div>
  <div class="callout result"><div class="h">Правило</div><p>Основной путь гайда — по актуальному workflow V8.2 и Nano Banana Pro. Старое показываем только там, где это спасает от ошибки, а не как музей параметров.</p></div>
"""))

# ============ P5 · Роли: таблица решений (часть 1) ============
P.append(page("Midjourney или Nano Banana · 1/2", 5, """
  <span class="kick">Роли инструментов</span>
  <h2>Кто что делает лучше</h2>
  <p class="lede2">Не битва инструментов. Один создаёт, второй удерживает и доводит. Граница в 2026 стала мягче: Nano Banana Pro тоже рисует с нуля, но премиум-эстетику «из воздуха» по-прежнему сильнее даёт Midjourney.</p>
  <table>
    <tr><th>Задача</th><th>Чем делать</th><th>Почему</th></tr>
    <tr><td><b>Визуал с нуля</b></td><td>Midjourney</td><td>эстетика и стиль из текста; NB — когда нужен точный контроль и текст</td></tr>
    <tr><td><b>Премиальный key visual</b></td><td>Midjourney → NB</td><td>MJ рождает кадр, NB доводит детали и добавляет текст</td></tr>
    <tr><td><b>Сохранить человека</b></td><td>Nano Banana Pro</td><td>идентичность до 5 лиц; MJ — только через <code>--oref</code></td></tr>
    <tr><td><b>Сохранить товар</b></td><td>Nano Banana Pro</td><td>держит форму, логотип, этикетку 1:1</td></tr>
    <tr><td><b>Поменять фон</b></td><td>Nano Banana</td><td>правит загруженный кадр, объект неизменен</td></tr>
    <tr><td><b>Поменять одежду</b></td><td>Nano Banana</td><td>локальная правка с сохранением лица и позы</td></tr>
    <tr><td><b>Поменять позу</b></td><td>Nano Banana Pro</td><td>переставляет героя, удерживая идентичность</td></tr>
    <tr><td><b>Новая сцена, тот же герой</b></td><td>Nano Banana Pro</td><td>переносит лицо/товар в другую локацию</td></tr>
  </table>
"""))

# ============ P6 · Роли: таблица решений (часть 2) ============
P.append(page("Midjourney или Nano Banana · 2/2", 6, """
  <span class="kick">Роли инструментов</span>
  <h2>Кто что делает лучше — продолжение</h2>
  <table>
    <tr><th>Задача</th><th>Чем делать</th><th>Почему</th></tr>
    <tr><td><b>Серия кадров</b></td><td>MJ (master) → NB</td><td>MJ задаёт язык, NB тиражирует его на сцены</td></tr>
    <tr><td><b>Читаемый текст в кадре</b></td><td>Nano Banana Pro</td><td>94–96%, многоязычный; MJ буквы ломает</td></tr>
    <tr><td><b>Карточка товара</b></td><td>Nano Banana Pro</td><td>чистый фон, товар 1:1, место под текст</td></tr>
    <tr><td><b>Рекламный баннер</b></td><td>Nano Banana Pro</td><td>композиция + встроенный текст в одном проходе</td></tr>
    <tr><td><b>Кадр под Image-to-Video</b></td><td>MJ → NB</td><td>MJ даёт кинокадр, NB чистит и ставит формат 9:16</td></tr>
    <tr><td><b>Объединить референсы</b></td><td>Nano Banana Pro</td><td>до 14 изображений в одну сцену</td></tr>
    <tr><td><b>Локальная правка</b></td><td>Nano Banana</td><td>чинит один участок, не трогая остальное</td></tr>
    <tr><td><b>Предметная фотография</b></td><td>MJ или NB Pro</td><td>MJ — с нуля; NB — если товар уже снят</td></tr>
    <tr><td><b>Editorial / fashion</b></td><td>Midjourney</td><td>сильная художественная эстетика</td></tr>
    <tr><td><b>Food photography</b></td><td>Midjourney → NB</td><td>MJ — аппетитный кадр, NB — серия в одном свете</td></tr>
    <tr><td><b>Личный бренд</b></td><td>MJ → NB Pro</td><td>MJ — образ, NB — одно лицо на всю линейку</td></tr>
  </table>
  <div class="callout result"><div class="h">Одна фраза, которую надо запомнить</div><p>Midjourney создаёт. Nano Banana помогает удержать и довести. Сила не в выборе «или-или», а в связке.</p></div>
"""))

# ============ P7 · PROMPT STACK ============
P.append(page("Архитектура промпта", 7, """
  <span class="kick">Prompt stack</span>
  <h2>Профессиональный промпт — это 15 управляемых слоёв</h2>
  <p class="lede2">Примитив «объект + стиль + свет» слаб. Профи держит в голове систему и включает нужные слои под задачу. Не обязательно все 15 — но знать их надо все.</p>
  <div class="stack">
    <div class="sk"><div class="n">Subject<i>кто или что главное</i></div></div>
    <div class="sk"><div class="n">Action / State<i>что происходит</i></div></div>
    <div class="sk"><div class="n">Environment<i>где это происходит</i></div></div>
    <div class="sk"><div class="n">Composition<i>где объект в кадре</i></div></div>
    <div class="sk"><div class="n">Camera<i>дистанция, ракурс, перспектива</i></div></div>
    <div class="sk"><div class="n">Lens language<i>характер «объектива»</i></div></div>
    <div class="sk"><div class="n">Light<i>источник, направление, жёсткость, температура</i></div></div>
    <div class="sk"><div class="n">Materials / Textures<i>что ощущается физически</i></div></div>
    <div class="sk"><div class="n">Color system<i>доминанта и акцент</i></div></div>
    <div class="sk"><div class="n">Depth<i>передний план / объект / фон</i></div></div>
    <div class="sk"><div class="n">Mood<i>какое ощущение</i></div></div>
    <div class="sk"><div class="n">Commercial intent<i>editorial, campaign, ecommerce, luxury</i></div></div>
    <div class="sk"><div class="n">Continuity<i>что совпадает с прошлыми кадрами</i></div></div>
    <div class="sk"><div class="n">Constraints<i>что запрещено менять</i></div></div>
    <div class="sk"><div class="n">Output<i>формат, разрешение, актуальные параметры</i></div></div>
  </div>
"""))

# ============ P8 · Три уровня ============
P.append(page("Три уровня промпта", 8, """
  <span class="kick">Quick · Pro · Production</span>
  <h2>Не вписывай 15 слоёв всегда</h2>
  <p class="lede2">Глубина промпта — под задачу. Тестируешь идею — хватит пяти слоёв. Гонишь кампанию с continuity — включаешь всю систему.</p>
  <div class="lv"><div class="h"><b>QUICK</b><span>5 элементов · быстрый тест</span></div>
    <p>Subject · Environment · Light · Mood · Output. Проверить идею и композицию, не тратя время.</p></div>
  <div class="lv"><div class="h"><b>PRO</b><span>8–10 элементов · рабочий кадр</span></div>
    <p>+ Composition · Camera · Materials · Color · Commercial intent. Отсюда получаются публикуемые кадры.</p></div>
  <div class="lv"><div class="h"><b>PRODUCTION</b><span>вся система · серия и кампания</span></div>
    <p>+ Lens · Depth · Continuity · Constraints. Когда кадр должен встать в серию и совпасть с остальными.</p></div>
  <div class="callout result"><div class="h">Как расти</div><p>Начинай с QUICK, добавляй слои, когда видишь, чего кадру не хватает. Слой добавляют, чтобы решить проблему, а не «чтобы было длиннее».</p></div>
"""))

# ============ P9 · Анатомия промпта ============
def al(tag, color, tx):
    return f'<div class="al"><span class="tag" style="background:{color}">{tag}</span><span class="tx">{tx}</span></div>'
P.append(page("Анатомия промпта", 9,
  '<span class="kick">Разбор по слоям</span>'
  '<h2>Один профессиональный промпт, разложенный на части</h2>'
  '<p class="lede2">Каждый кусок делает конкретную работу. Убери любой — кадр теряет управляемость.</p>' +
  prompt("Midjourney · production", "editorial portrait of a confident founder, arms crossed, in a dark concrete studio, "
    "subject left-of-center, medium close-up, eye-level, 85mm look, warm amber rim light from camera-right, "
    "matte skin and wool texture, deep brown and ember palette, soft foreground bokeh, quiet-luxury mood, "
    "brand campaign --ar 4:5 --style raw --stylize 150", copy=False) +
  '<div class="anat">' +
  al("Subject", "#b8442a", "confident founder, arms crossed") +
  al("Environment", "#c26a1f", "dark concrete studio") +
  al("Composition", "#a5701f", "left-of-center, medium close-up") +
  al("Camera / lens", "#7d7a25", "eye-level, 85mm look") +
  al("Light", "#3f7d34", "warm amber rim light, camera-right") +
  al("Texture", "#2f7d5a", "matte skin, wool") +
  al("Color", "#2f6d7d", "deep brown + ember") +
  al("Depth / mood", "#3a5a9a", "soft foreground bokeh, quiet luxury") +
  al("Intent", "#6a4a9a", "brand campaign") +
  al("Output", "#8a3a7a", "<code>--ar 4:5 --style raw --stylize 150</code>") +
  '</div>'))

# ============ P10 · Слабый vs профессиональный + анти-porn ============
P.append(page("Слабый против профи", 10, """
  <span class="kick">Почему это работает</span>
  <h2>Разница не в «красивых словах»</h2>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Слабый промпт</div>«beautiful founder portrait, masterpiece, ultra realistic, 8k, insane details, award winning, cinematic, trending on artstation»</div>
    <div class="box good"><div class="lbl">✓ Профессиональный</div>«editorial portrait of a founder, dark concrete studio, warm amber rim light, 85mm look, ember palette, quiet-luxury mood --ar 4:5 --style raw --stylize 150»</div>
  </div>
  <div class="mns">
    <div class="m stay"><div class="h">Почему слабый проваливается</div><p>«8k, masterpiece, award winning» не несут визуальной информации. Модель не знает, куда встать камере, откуда свет, какое настроение. Результат — случайный.</p></div>
    <div class="m move"><div class="h">Почему профи выигрывает</div><p>Каждое слово — управляемый параметр: свет, оптика, палитра, интент. Кадр воспроизводим, редактируем и встаёт в серию.</p></div>
  </div>
  <div class="callout check"><div class="h">Правило против «prompt porn»</div>
    <div class="row">Каждое слово выполняет функцию — или его нет</div>
    <div class="row">Промпт понятен модели, а не только человеку</div>
    <div class="row">Результат воспроизводим и редактируем</div>
    <div class="row">Никаких «8k / masterpiece / trending», если они ничего не задают</div>
  </div>
"""))

# ============ P11 · Midjourney глава ============
P.append(page("Midjourney · как мыслить", 11, """
  <span class="kick">Midjourney · глава 1</span>
  <h2>От идеи до production-ready кадра</h2>
  <p class="lede2">Midjourney силён там, где нужно родить визуальный мир: свет, эстетику, атмосферу, master-кадр серии. Слаб — там, где нужен точный текст, правка твоего фото или гарантия 1:1.</p>
  <div class="cards c2">
    <div class="card"><div class="ct">Силён</div><div class="ch">Создаёт мир с нуля</div><p>Эстетика, свет, стиль, настроение, editorial и fashion, атмосферные сцены.</p></div>
    <div class="card"><div class="ct">Слаб</div><div class="ch">Точность и правки</div><p>Читаемый текст, редактура загруженного фото, гарантия неизменности логотипа.</p></div>
  </div>
  <h3>Четыре установки перед работой</h3>
  <ul>
    <li><strong>Мысли сценой, а не объектом.</strong> Не «гребешок», а «гребешок в тёмном зале, тёплый боковой свет, пар».</li>
    <li><strong>Длиннее ≠ лучше.</strong> Лишние слова размывают. Каждый слой — под задачу.</li>
    <li><strong>Раздели, чем управляешь.</strong> Словами — сцену и свет; параметрами — стиль и формат; референсом — идентичность.</li>
    <li><strong>Сначала master-кадр.</strong> Один сильный кадр задаёт язык всей серии — от него уже тиражируешь.</li>
  </ul>
  <div class="callout result"><div class="h">Что задавать чем</div><p><b>Слова</b> — субъект, сцена, свет, настроение. <b>Параметры</b> — стиль, свобода, формат. <b>Reference</b> — идентичность (<code style="font-family:ui-monospace,monospace;font-size:9pt;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">--oref</code>) и стиль (<code style="font-family:ui-monospace,monospace;font-size:9pt;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">--sref</code>).</p></div>
"""))

# ============ P12 · Midjourney параметры (выверено) ============
P.append(page("Midjourney · параметры V8.2", 12, """
  <span class="kick">Midjourney · глава 2</span>
  <h2>Параметры, выверенные на 08.2026</h2>
  <table>
    <tr><th>Параметр</th><th>Диапазон · дефолт</th><th>Что делает</th></tr>
    <tr><td><code>--ar</code></td><td>напр. 4:5, 9:16, 16:9</td><td>соотношение сторон под площадку и под будущее видео</td></tr>
    <tr><td><code>--style raw</code></td><td>вкл/выкл</td><td>снимает «миджорнишность», делает кадр буквальнее — под фото и рекламу</td></tr>
    <tr><td><code>--stylize</code> / <code>--s</code></td><td>0–1000 · 100</td><td>художественная свобода: 0–50 буквально, 200–400 вольнее</td></tr>
    <tr><td><code>--sref</code> + <code>--sw</code></td><td>sw 0–1000 · 100</td><td>референс стиля; <code>--sw</code> — как сильно стиль давит</td></tr>
    <tr><td><code>--oref</code> + <code>--ow</code></td><td>ow 0–1000 · ~100</td><td>Omni Reference: идентичность лица/объекта; лок 400–600, «намёк» 25–75</td></tr>
    <tr><td><code>--q</code></td><td>по версии</td><td>детализация; V8 умеет нативный 2K</td></tr>
    <tr><td><code>--p</code></td><td>профиль</td><td>Personalization — подмешивает твой вкус</td></tr>
    <tr><td><code>--seed</code></td><td>число</td><td>стартовый шум для воспроизводимости — <b>не</b> замок личности</td></tr>
  </table>
  <div class="callout check"><div class="h">Разделяй четыре вещи — их путают чаще всего</div>
    <div class="row"><b>Стиль</b> → <code>--sref</code>, <code>--style raw</code>, <code>--stylize</code></div>
    <div class="row"><b>Идентичность персонажа/товара</b> → <code>--oref</code> + <code>--ow</code></div>
    <div class="row"><b>Композиция</b> → слова: ракурс, план, где объект в кадре</div>
    <div class="row"><b>Случайность</b> → <code>--seed</code> (только точка старта)</div>
  </div>
"""))

# ============ P13 · Nano Banana глава + семейство ============
P.append(page("Nano Banana · семейство", 13, """
  <span class="kick">Nano Banana · глава 1</span>
  <h2>Не перерисовывай. Редактируй намеренно</h2>
  <p class="lede2">Ключевой сдвиг мышления: Nano Banana не «генерит заново по мотивам», а берёт твой кадр и меняет ровно то, что ты назвал, удерживая остальное. Сначала — что оставить. Потом — что изменить.</p>
  <table>
    <tr><th>Модель</th><th>Для чего</th><th>Качество</th><th>Когда выбирать</th></tr>
    <tr><td><b>Nano Banana</b><br><span style="font-size:8pt;color:var(--muted)">Gemini 2.5 Flash Image</span></td><td>быстрые правки, замена фона, простая консистентность</td><td>высокое, до 2–3 референсов</td><td>черновики, объём, быстрые итерации</td></tr>
    <tr><td><b>Nano Banana Pro</b><br><span style="font-size:8pt;color:var(--muted)">Gemini 3 Pro Image</span></td><td>премиум-серии, текст, композиты, 4K</td><td>до 14 референсов, 5 лиц, текст 94–96%</td><td>кампании, карточки, финальные материалы</td></tr>
  </table>
  <div class="cards c2">
    <div class="card"><div class="ct">Сильные стороны</div><div class="ch">Точность и удержание</div><p>Держит лицо, товар, логотип; читаемый многоязычный текст; композит из многих референсов; 1K–4K.</p></div>
    <div class="card"><div class="ct">Помни</div><div class="ch">Язык — обычный</div><p>Никаких <code>--флагов</code>. Инструкции словами, работает и на русском. На все кадры — метка SynthID.</p></div>
  </div>
"""))

# ============ P14 · EDIT STACK ============
P.append(page("Nano Banana · edit stack", 14,
  '<span class="kick">Nano Banana · глава 2</span>'
  '<h2>Промпт-правка строится иначе: сначала LOCK</h2>'
  '<p class="lede2">Midjourney-промпт описывает мир. Nano Banana-промпт описывает <b>операцию</b> над готовым кадром. Порядок жёсткий: сперва фиксируем неизменное, потом называем правку.</p>' +
  '<div class="stack" style="grid-template-columns:1fr 1fr">'
  '<div class="sk"><div class="n">Input<i>что загружено</i></div></div>'
  '<div class="sk"><div class="n">Lock<i>что нельзя менять</i></div></div>'
  '<div class="sk"><div class="n">Change<i>что изменить</i></div></div>'
  '<div class="sk"><div class="n">Placement<i>где именно</i></div></div>'
  '<div class="sk"><div class="n">Match<i>что подогнать под исходник</i></div></div>'
  '<div class="sk"><div class="n">Light<i>как интегрировать по свету</i></div></div>'
  '<div class="sk"><div class="n">Geometry<i>сохранить перспективу и форму</i></div></div>'
  '<div class="sk"><div class="n">Texture<i>сохранить материалы</i></div></div>'
  '<div class="sk"><div class="n">Continuity<i>совпасть с серией</i></div></div>'
  '<div class="sk"><div class="n">Output<i>формат результата</i></div></div>'
  '</div>' +
  prompt("Nano Banana · структура правки",
    "INPUT: uploaded studio portrait.\n"
    "<b>KEEP</b> exactly: face, skull shape, nose, eyes, beard, hairline, proportions, outfit.\n"
    "<b>CHANGE</b> only: background → deep brown near-black studio with warm amber rim light.\n"
    "MATCH the new light to the face. Keep perspective and skin texture. No reshaping, no age change.",
    '<b style="color:#fff">Правило:</b> «сделай красивее» — это не инструкция. Инструкция — что оставить 1:1 и что именно поменять.') ))

# ============ P15 · Identity Lock ============
P.append(page("Как не потерять человека", 15,
  '<span class="kick">Identity lock</span>'
  '<h2>Что фиксировать, чтобы лицо не «поплыло»</h2>'
  '<p class="lede2">«same person» — слабая защита. Модель нужно вести по конкретным чертам. Перечисляй их явно — тогда серия держит одного героя.</p>'
  '<div class="chiprow">'
  '<span>форма головы</span><span>лицо</span><span>глаза</span><span>нос</span><span>губы</span><span>уши</span>'
  '<span>линия волос</span><span>борода</span><span>возраст</span><span>кожа</span><span>телосложение</span>'
  '<span>шея и плечи</span><span>пропорции</span><span>особые черты</span></div>' +
  prompt("Identity Lock Template · универсальный",
    "KEEP the exact same person, unchanged: head shape, facial structure, eyes, nose, lips, ears,\n"
    "hairline and hair, beard, skin texture and tone, apparent age, body build, neck and shoulders,\n"
    "distinctive features. Do not beautify, do not slim the face, do not change age. Same identity across all frames.") +
  '<div class="cards c3" style="margin-top:6px">'
  '<div class="card"><div class="ct">Мужчина · бизнес</div><p>+ линия челюсти, седина у висков, оправа очков 1:1.</p></div>'
  '<div class="card"><div class="ct">Женщина · fashion</div><p>+ форма бровей, макияж, длина и цвет волос, серьги.</p></div>'
  '<div class="card"><div class="ct">Эксперт · личный бренд</div><p>+ мимический характер, поза, фирменный образ и цвет одежды.</p></div>'
  '</div>'
  '<p class="note">Чем точнее список черт — тем сильнее continuity. Общие слова («красивый», «моложе») ломают идентичность.</p>'))

# ============ P16 · Product Lock ============
P.append(page("Как не потерять товар", 16,
  '<span class="kick">Product lock</span>'
  '<h2>Что фиксировать, чтобы продукт остался собой</h2>'
  '<p class="lede2">Товар обязан читаться как тот же самый: форма, упаковка, логотип, надписи. Одна «улучшенная» этикетка — и это уже другой продукт, юридически и визуально.</p>'
  '<div class="chiprow">'
  '<span>геометрия</span><span>пропорции</span><span>форма</span><span>упаковка</span><span>логотип</span>'
  '<span>надписи</span><span>цвет</span><span>материал</span><span>отражения</span><span>крышка</span>'
  '<span>этикетка</span><span>уникальные элементы</span></div>' +
  prompt("Product Lock Template · универсальный",
    "KEEP the product 1:1, unchanged: exact geometry, proportions and shape, packaging, logo and all text,\n"
    "brand colors, material and finish, reflections, cap and label. Do not redesign, do not restyle the label,\n"
    "do not alter the logo. Only change the environment around it.") +
  '<div class="gb" style="margin-top:8px">'
  '<div class="box good"><div class="lbl">✓ Правильно</div>«Оставь этикетку, логотип и форму 1:1, поменяй только фон и свет».</div>'
  '<div class="box bad"><div class="lbl">✕ Ошибка</div>«Сделай упаковку премиальнее» — модель перерисует логотип и надписи.</div>'
  '</div>'))

# ============ P17 · Style Bible ============
P.append(page("Визуальный паспорт проекта", 17,
  '<span class="kick">Style bible</span>'
  '<h2>Перед серией — собери визуальный паспорт</h2>'
  '<p class="lede2">Style Bible — один экран, который держит всю серию в одном языке. Заполняешь один раз, дальше каждый кадр сверяешь с ним. Пример — ресторанный кейс AlovLab.</p>'
  '<div class="bible">'
  '<div class="bf"><div class="k">Project</div><div class="v">Авторский ресторан · кампания</div></div>'
  '<div class="bf"><div class="k">Subject</div><div class="v">блюда, шеф, интерьер</div></div>'
  '<div class="bf"><div class="k">Primary style</div><div class="v">editorial food, quiet luxury</div></div>'
  '<div class="bf"><div class="k">Light</div><div class="v">warm amber side light</div></div>'
  '<div class="bf"><div class="k">Color palette</div><div class="v">deep brown / near-black + ember</div></div>'
  '<div class="bf"><div class="k">Contrast</div><div class="v">высокий, мягкие тени</div></div>'
  '<div class="bf"><div class="k">Camera</div><div class="v">intimate, low, медленный язык</div></div>'
  '<div class="bf"><div class="k">Lens feel</div><div class="v">85mm, малая глубина резкости</div></div>'
  '<div class="bf"><div class="k">Background</div><div class="v">dark wood, stone, brass</div></div>'
  '<div class="bf"><div class="k">Depth</div><div class="v">сильный отрыв переднего плана</div></div>'
  '<div class="bf"><div class="k">Mood</div><div class="v">quiet luxury, тепло, тишина</div></div>'
  '<div class="bf"><div class="k">Output</div><div class="v">4:5 и 9:16 · 2K+</div></div>'
  '</div>'
  '<div class="gb">'
  '<div class="box good"><div class="lbl">✓ DO</div>тёплый боковой свет, тёмное дерево и латунь, пар, крупная фактура, глубокий передний план.</div>'
  '<div class="box bad"><div class="lbl">✕ DON\'T</div>синий неон, пересвет, глянцевый CGI, лишний дым, кислотные цвета.</div>'
  '</div>'
  '<p class="note">Дальше в этой методичке весь сквозной кейс собирается ровно по этому паспорту — так серия и остаётся одной кампанией.</p>'))

# ============ БАТЧ 2 · БИБЛИОТЕКИ ПРОМПТОВ ============
LIBCSS = r"""
.lc{border:1px solid var(--line);border-radius:13px;padding:12px 15px;margin:9px 0;background:#fff}
.lc .hd{display:flex;align-items:baseline;gap:9px;margin-bottom:2px;flex-wrap:wrap}
.lc .num{font-weight:800;font-size:11pt;color:var(--o)}
.lc .cat{font-weight:800;font-size:6.8pt;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);background:var(--o-tint);padding:3px 8px;border-radius:20px}
.lc .task{font-weight:800;font-size:11pt;color:var(--ink);line-height:1.15}
.lc .prm{background:var(--dark);border-radius:10px;padding:10px 12px;margin:7px 0}
.lc .prm code{font-family:'SF Mono',ui-monospace,Menlo,monospace;font-size:8.4pt;line-height:1.5;color:#ffd9b8;white-space:pre-wrap;word-break:break-word;display:block}
.lc .prm code b{color:#fff;font-weight:700}
.lc .ru{font-size:8.8pt;line-height:1.38;color:var(--body);margin:5px 0}
.lc .ru b{color:var(--ink)}
.lc .meta{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 0}
.lc .mi{font-size:7.8pt;line-height:1.3;background:#f7f1e8;border:1px solid var(--line);border-radius:8px;padding:5px 9px;max-width:100%}
.lc .mi b{color:var(--o);text-transform:uppercase;letter-spacing:.03em;font-size:6.6pt;margin-right:4px}
.lc .fix{font-size:8pt;line-height:1.4;color:var(--body);background:#fbeeea;border:1px solid #f0cabb;border-radius:9px;padding:7px 11px;margin-top:6px}
.lc .fix b{color:#c0492a;text-transform:uppercase;font-size:6.6pt;letter-spacing:.03em;margin-right:4px}
.lc .fix .cx{color:#3f7d34;font-family:ui-monospace,Menlo,monospace;font-size:7.6pt}
.catband{background:linear-gradient(150deg,var(--o-tint),#fff);border:1px solid #f2d3bf;border-radius:11px;padding:10px 15px;margin:10px 0 4px}
.catband b{font-weight:800;font-size:11pt;color:var(--ink)}.catband span{font-size:9pt;color:var(--muted);margin-left:8px}
"""
CSS = CSS + LIBCSS

def addpage(section, inner):
    P.append(page(section, len(P)+1, inner))

def libcard(n, cat, task, code, ru, variable, keep, ref, err, fix):
    return (f'<div class="lc"><div class="hd"><span class="num">{n:02d}</span>'
            f'<span class="cat">{cat}</span><span class="task">{task}</span></div>'
            f'<div class="prm"><code>{code}</code></div>'
            f'<div class="ru">{ru}</div>'
            f'<div class="meta"><span class="mi"><b>Переменная</b>{variable}</span>'
            f'<span class="mi"><b>Не менять</b>{keep}</span><span class="mi"><b>Референс</b>{ref}</span></div>'
            f'<div class="fix"><b>Ошибка</b>{err} <b class="cx" style="color:#3f7d34">→ Правка</b> <span class="cx">{fix}</span></div></div>')

def lib_paginate(section, kick, title, intro, cards, per=2):
    for i in range(0, len(cards), per):
        head = (f'<span class="kick">{kick}</span><h2>{title}</h2><p class="lede2">{intro}</p>' if i == 0 else '')
        addpage(section, head + "".join(cards[i:i+per]))

# ---- Библиотека Midjourney (20) ----
MJ = [
 (1,"A · Личный бренд","Премиальный портрет эксперта",
  "editorial portrait of a male expert, calm confident gaze, dark charcoal studio, warm amber key light "
  "from camera-left, subtle rim light, 85mm look, matte skin texture, deep brown palette, quiet-luxury mood "
  "--ar 4:5 --style raw --stylize 150",
  "База личного бренда: спокойный статус, тёплый ключевой свет слева, матовая кожа.",
  "пол, возраст, одежда","свет и палитру","<code>--oref</code> лицо",
  "пластиковая кожа","add: natural skin texture, visible pores, no retouch"),
 (2,"A · Личный бренд","Тёмная студийная серия",
  "studio portrait, deep near-black background, single warm amber side light, medium close-up, 85mm, "
  "cinematic color grade --ar 4:5 --style raw --stylize 120 --sref [ссылка на master-кадр]",
  "Серия в одном стиле: <code>--sref</code> с master-кадра держит единый свет и грейд.",
  "поза, ракурс","фон и свет","<code>--sref</code> стиль",
  "кадры вразнобой","--sref одного мастера + --sw 100"),
 (3,"A · Личный бренд","Lifestyle-портрет",
  "candid lifestyle portrait of an entrepreneur in a sunlit loft office, natural window light, "
  "shallow depth of field, warm neutral palette, documentary feel, 35mm --ar 4:5 --stylize 180",
  "Живой рабочий кадр: естественный свет из окна, документальная подача.",
  "локация, действие","естественный свет","—",
  "постановочно и «сток»","add: candid moment, natural imperfect pose"),
 (4,"A · Личный бренд","Key visual для Reels",
  "vertical hero frame of a confident creator, dark moody set, single warm beam, strong empty space at top "
  "for text, cinematic --ar 9:16 --style raw --stylize 160",
  "Обложка Reels: вертикаль, воздух сверху под заголовок, один драматичный луч.",
  "герой, цвет луча","формат 9:16","<code>--oref</code> лицо",
  "нет места под текст","add: generous negative space top third"),
 (5,"A · Личный бренд","Обложка образовательного продукта",
  "premium course cover, expert portrait on the right, gradient background brown to black, dramatic rim "
  "light, generous left negative space for title, editorial --ar 4:5 --style raw --stylize 140",
  "Обложка курса: герой справа, слева воздух под тайтл, драматичный контровой.",
  "герой, градиент","композицию под текст","<code>--oref</code> лицо",
  "лицо по центру, текст некуда","subject to right third, keep left clear"),
 (6,"B · Ресторан","Fine dining food photography",
  "editorial food photograph of a seared scallop on dark slate, warm amber side light, delicate rising "
  "steam, glossy reduction sauce, shallow depth of field, near-black background, commercial food styling "
  "--ar 4:5 --style raw --stylize 200",
  "Аппетитный премиум-кадр блюда: пар, блик соуса, тёмный фон, малая ГРИП.",
  "блюдо, соус","свет и фон","<code>--sref</code> стиль серии",
  "плоский свет, «меню»","add: single warm side light, rising steam"),
 (7,"B · Ресторан","Интерьер зала",
  "upscale restaurant interior at dusk, warm candlelight, dark wood and brass, deep perspective, bokeh "
  "highlights, intimate low camera, quiet luxury --ar 4:5 --style raw --stylize 180",
  "Атмосфера вечера: свечи, дерево и латунь, глубокая перспектива, боке.",
  "зал, ракурс","тёплую палитру","<code>--sref</code> стиль",
  "холодный синий свет","warm candlelight only, no blue tint"),
 (8,"B · Ресторан","Шеф за работой",
  "portrait of a focused chef plating a dish, warm kitchen light, hands in frame, steam, dark background, "
  "documentary elegance, 50mm --ar 4:5 --style raw --stylize 150",
  "Человек бренда: сосредоточенность, руки в кадре, пар, тёмный фон.",
  "шеф, блюдо","свет и настроение","<code>--oref</code> лицо",
  "постановочная улыбка","add: focused candid expression, no eye contact"),
 (9,"B · Ресторан","Editorial-кадр истории",
  "editorial restaurant story frame, close-up of hands finishing a plate, warm amber light, dark linen, "
  "subtle film grain, magazine spread aesthetic --ar 4:5 --style raw --stylize 200",
  "Кадр-история для карусели/разворота: крупные руки, фактура, зерно.",
  "деталь, блюдо","свет и грейн","<code>--sref</code> стиль",
  "слишком гладко, «CGI»","add: subtle film grain, natural texture"),
 (10,"B · Ресторан","Key visual кампании",
  "restaurant campaign key visual, signature dish centered, dramatic single warm light, deep shadows, "
  "brass and stone textures, space for headline, luxury advertising --ar 4:5 --style raw --stylize 160",
  "Рекламный ключевой кадр: центр под блюдо, воздух под заголовок, драма света.",
  "блюдо, текстуры","драму света","<code>--sref</code> стиль",
  "нет места под текст","keep top/bottom clear for headline"),
 (11,"C · E-commerce","Hero shot продукта",
  "hero product shot of a matte glass cosmetic bottle on wet dark stone, soft gradient rim light, subtle "
  "reflection, minimal premium background, studio, high detail --ar 4:5 --style raw --stylize 120",
  "Каталожный герой: чистый премиум-фон, мягкий контур света, отражение.",
  "продукт, поверхность","чистоту фона","фото товара → Nano Banana",
  "пёстрый фон отвлекает","minimal seamless background, product centered"),
 (12,"C · E-commerce","Beauty product",
  "beauty product still life, serum dropper on silk, soft diffused light, dewy highlights, pastel-neutral "
  "palette, clean luxury, macro detail --ar 4:5 --style raw --stylize 130",
  "Бьюти-натюрморт: мягкий рассеянный свет, «росистые» блики, макро.",
  "продукт, фактура","мягкий свет","<code>--sref</code> стиль",
  "жёсткие тени","soft diffused light, no hard shadows"),
 (13,"C · E-commerce","Tech product",
  "tech gadget hero shot, brushed aluminum device on dark gradient, crisp edge light, subtle neutral "
  "accents, clean studio, sharp reflections --ar 4:5 --style raw --stylize 110",
  "Техника: чёткий контурный свет, гладкий градиент, резкие отражения.",
  "устройство, акцент","чистоту и резкость","фото товара → Nano Banana",
  "мутные отражения","crisp edge light, sharp clean reflections"),
 (14,"C · E-commerce","Fashion accessory",
  "luxury leather handbag on marble pedestal, warm directional light, soft shadow, editorial fashion "
  "background, rich texture, high-end retail --ar 4:5 --style raw --stylize 150",
  "Аксессуар: подиум-подача, тёплый направленный свет, богатая фактура кожи.",
  "предмет, фон","фактуру кожи","<code>--sref</code> стиль",
  "дешёвый пластиковый вид","emphasize natural leather grain and stitching"),
 (15,"C · E-commerce","Product lifestyle",
  "product in lifestyle context, ceramic mug on a linen breakfast table, morning window light, cozy "
  "neutral palette, shallow depth of field, natural --ar 4:5 --stylize 170",
  "Товар в жизни: утренний свет, уютный стол, естественная сцена.",
  "продукт, сцена","естественность","—",
  "выглядит как реклама","add: candid natural setting, imperfect styling"),
 (16,"D · B2B","Промышленный объект",
  "industrial facility interior, clean modern machinery, controlled cool light with warm accents, strong "
  "leading lines, wide perspective, corporate documentary --ar 16:9 --style raw --stylize 120",
  "Производство премиально: порядок, ведущие линии, холодный свет с тёплым акцентом.",
  "объект, ракурс","чистоту и линии","<code>--sref</code> стиль",
  "хаос и грязь в кадре","clean organized space, strong leading lines"),
 (17,"D · B2B","Архитектура",
  "modern corporate architecture at blue hour, glass facade, warm interior glow, symmetrical composition, "
  "crisp lines, premium real estate --ar 16:9 --style raw --stylize 130",
  "Здание: синий час, тёплое свечение окон, симметрия, чистые линии.",
  "объект, время суток","симметрию","<code>--sref</code> стиль",
  "заваленный горизонт","symmetrical composition, level horizon"),
 (18,"D · B2B","Premium service campaign",
  "premium B2B service key visual, a confident handshake moment in a bright modern office, soft daylight, "
  "trustworthy neutral palette, space for headline --ar 16:9 --stylize 140",
  "Услуга: момент доверия, светлый офис, нейтральная палитра, воздух под текст.",
  "сцена, палитра","доверительный тон","—",
  "постановочно и фальшиво","natural candid interaction, soft daylight"),
 (19,"D · B2B","Founder portrait",
  "corporate founder portrait, confident posture, bright modern office bokeh, soft window daylight, "
  "neutral professional palette, 85mm, approachable authority --ar 4:5 --style raw --stylize 130",
  "Портрет основателя: авторитет + доступность, дневной свет, офисное боке.",
  "герой, фон","профессиональный тон","<code>--oref</code> лицо",
  "слишком строго/холодно","approachable warm expression, soft daylight"),
 (20,"D · B2B","Corporate campaign visual",
  "corporate campaign visual, team collaboration in a bright glass meeting room, natural light, clean "
  "neutral brand palette, documentary realism, wide --ar 16:9 --stylize 130",
  "Командный кадр: стеклянная переговорка, дневной свет, документальный реализм.",
  "команда, сцена","чистую палитру","<code>--sref</code> стиль",
  "«стоковые» позы","candid collaboration, natural glances, no posing"),
]
lib_paginate("Библиотека Midjourney", "Библиотека · Midjourney",
  "20 профессиональных промптов", "Не вариации одной фразы — разные production-задачи. "
  "Копируй промпт, подставляй переменную, держи «не менять», прикладывай нужный референс.",
  [libcard(*m) for m in MJ])

# ---- Библиотека Nano Banana (25) — карточка LOCK/CHANGE/CONTINUITY ----
def nbcard(n, cat, task, code, ru, lock, change, cont, err, fix):
    return (f'<div class="lc"><div class="hd"><span class="num">{n:02d}</span>'
            f'<span class="cat">{cat}</span><span class="task">{task}</span></div>'
            f'<div class="prm"><code>{code}</code></div>'
            f'<div class="ru">{ru}</div>'
            f'<div class="meta"><span class="mi"><b>Lock</b>{lock}</span>'
            f'<span class="mi"><b>Change</b>{change}</span><span class="mi"><b>Continuity</b>{cont}</span></div>'
            f'<div class="fix"><b>Ошибка</b>{err} <b class="cx" style="color:#3f7d34">→ Correction</b> <span class="cx">{fix}</span></div></div>')

NB = [
 (1,"Identity","Сохранить лицо, поменять фон",
  "[загрузи портрет] KEEP the exact same face, hair, beard and outfit 1:1. CHANGE only the background to a "
  "dark upscale studio with warm amber rim light. MATCH the new light to the face.",
  "База переноса: лицо и одежда 1:1, меняем только фон, свет подгоняем.",
  "лицо, волосы, одежда","фон","свет серии","лицо поплыло","KEEP face 1:1, do not beautify or reshape"),
 (2,"Identity","Сохранить лицо, поменять одежду",
  "[портрет] KEEP the exact face, hair and body proportions. CHANGE the outfit to a tailored dark suit. "
  "Match the fabric light to the scene. Do not change the face.",
  "Смена образа без потери человека: лицо и пропорции держим, меняем одежду.",
  "лицо, пропорции","одежда","стиль света","изменилось лицо","restore original face and hairline 1:1"),
 (3,"Identity","Поместить героя в новую локацию",
  "[портрет] KEEP the person 1:1. PLACE them in a sunlit modern office. Add natural window light and a soft "
  "contact shadow so the subject sits naturally in the scene.",
  "Перенос в сцену: тень контакта и свет делают героя «своим» в кадре.",
  "идентичность","локация","палитра серии","герой приклеен","add contact shadow, integrate light on subject"),
 (4,"Identity","Серия сцен, один герой",
  "[портрет] KEEP identity 1:1 across all frames. Generate the same person in three settings — studio, "
  "office, outdoor — same face, hair and outfit, same warm color grade.",
  "Три сцены одним героем: одно лицо, одна одежда, один грейд.",
  "лицо, одежда","3 сцены","грейд серии","лица разные","same identity and grade across all frames"),
 (5,"Identity","Изменить свет, не трогая человека",
  "[портрет] KEEP the face, features and outfit unchanged. CHANGE only the lighting to dramatic warm side "
  "light with soft shadows. Do not alter skin or age.",
  "Пересвет без правки лица: меняем только светотень.",
  "лицо, одежда","свет","мягкие тени","кожа перерисована","keep skin texture, change only lighting"),
 (6,"Identity","Сменить позу, сохранив личность",
  "[портрет] KEEP the exact identity and outfit. CHANGE pose to arms crossed, three-quarter turn. Keep the "
  "face, proportions and clothing consistent.",
  "Новая поза того же человека — лицо и одежда неизменны.",
  "лицо, одежда","поза","пропорции","пропорции сломались","keep realistic body proportions"),
 (7,"Identity","Рекламная композиция с тем же человеком",
  "[портрет] KEEP identity 1:1. Compose an ad key visual: subject on the right third, dark gradient "
  "background, warm rim light, empty left space for a headline.",
  "Из портрета — рекламный ключевой кадр с местом под заголовок.",
  "лицо","композиция, фон","свет бренда","нет места под текст","keep left third clear for headline"),
 (8,"Product","Поменять фон товара",
  "[фото товара] KEEP the product, label, logo and reflections 1:1. CHANGE only the background to a clean "
  "warm studio. Match shadow and light to the product.",
  "Каталожная замена фона: товар и этикетка 1:1.",
  "форма, логотип","фон","свет серии","логотип поплыл","reproduce logo and label exactly 1:1"),
 (9,"Product","Поместить товар в интерьер",
  "[товар] KEEP the product 1:1. PLACE it on a marble kitchen counter with soft morning light and a "
  "realistic contact shadow.",
  "Товар в жизни: интерьер + честная тень контакта.",
  "форма, этикетка","окружение","палитра","товар парит","add realistic contact shadow"),
 (10,"Product","Поменять поверхность-подложку",
  "[товар] KEEP the product 1:1. CHANGE only the surface under it to wet dark stone. Add a matching "
  "reflection consistent with the product.",
  "Смена подложки с корректным отражением.",
  "форма, цвет","поверхность","стиль света","отражение неверное","reflection must match product shape"),
 (11,"Product","Добавить lifestyle-контекст",
  "[товар] KEEP the product 1:1. Add a natural lifestyle context — a hand reaching for it on a breakfast "
  "table. Keep the product untouched.",
  "Контекст использования без правки самого товара.",
  "товар 1:1","контекст","палитра","товар изменился","product stays exactly as source"),
 (12,"Product","Premium hero shot из простого фото",
  "[товар] KEEP geometry, label and logo 1:1. Rebuild as a premium hero shot: dark gradient background, "
  "soft rim light, subtle reflection, minimal composition.",
  "Из бытового снимка — премиальный герой-кадр.",
  "геометрия, логотип","фон, свет","стиль бренда","детали размылись","keep label text crisp and 1:1"),
 (13,"Product","Один товар в нескольких сценах",
  "[товар] KEEP the product identical 1:1. Show it in three scenes — studio, lifestyle, outdoor — same "
  "product, consistent brand lighting.",
  "Линейка сцен одним товаром для карусели/каталога.",
  "товар 1:1","3 сцены","свет бренда","товар «плавает»","identical product across all scenes"),
 (14,"Product","Сохранить логотип и упаковку 1:1",
  "[товар] Reproduce the packaging, logo and all text exactly 1:1, sharp and undistorted. CHANGE only the "
  "environment. Do not redraw or restyle the logo.",
  "Юридически чистый перенос: упаковка и надписи без искажений.",
  "упаковка, текст","окружение","—","буквы поехали","re-render text legible, correct spelling"),
 (15,"E-commerce","Карточка товара",
  "[товар] KEEP product 1:1. Clean white-to-warm gradient background, centered, soft shadow, empty space "
  "at top for title and price. Marketplace-ready.",
  "Готовая карточка: чистый фон, центр, место под тайтл и цену.",
  "товар 1:1","фон, компоновка","—","тесно, нет полей","keep top clear for title and price"),
 (16,"E-commerce","Инфографика по товару",
  "[товар] KEEP product 1:1. Add three clean callout labels pointing to features, legible sans-serif text, "
  "consistent brand colors. (Nano Banana Pro)",
  "Инфографика с читаемыми выносками — сильная сторона Pro.",
  "товар 1:1","выноски, текст","бренд-цвета","текст кривой","Pro model, legible aligned labels"),
 (17,"E-commerce","Брендовый баннер",
  "[фон-референс + товар] Compose a horizontal banner: product on the left, headline in bold legible type "
  "on the right, warm premium scene, brand palette. (Pro)",
  "Баннер за один проход: композиция + встроенный текст.",
  "товар, логотип","композиция, текст","бренд-стиль","текст нечитаем","Pro model for in-image text"),
 (18,"E-commerce","Marketplace-визуал",
  "[товар] KEEP product 1:1. Bright even light, pure background, true colors, no heavy shadows — marketplace "
  "compliance. Leave space for a badge.",
  "Под требования маркетплейса: ровный свет, честный цвет.",
  "товар, цвет","фон, свет","—","цвет искажён","keep true product color, even light"),
 (19,"E-commerce","Text-heavy промо-креатив",
  "[фон] Add a promo layout: headline, subhead and a CTA button, all perfectly legible, correct spelling, "
  "aligned to a grid, brand colors. (Pro)",
  "Плотный по тексту креатив — только Pro тянет чисто.",
  "фон-стиль","весь текст","бренд-цвета","опечатки/каша","Pro, check spelling and alignment"),
 (20,"Food","Сохранить блюдо, изменить окружение",
  "[фото блюда] KEEP the dish 1:1 — plating, garnish and colors. CHANGE only the table and background to "
  "dark linen with warm side light.",
  "Блюдо неизменно, меняем сцену вокруг него.",
  "блюдо 1:1","стол, фон","свет серии","подача изменилась","keep exact plating and garnish"),
 (21,"Food","Премиальная подача",
  "[блюдо] KEEP the dish 1:1. Rebuild the scene as fine-dining: dark slate, warm amber light, rising steam, "
  "shallow depth of field, near-black background.",
  "Из обычного фото — ресторанная премиум-подача.",
  "блюдо 1:1","сцена, свет","стиль ресторана","еда «поплыла»","dish stays exactly as source"),
 (22,"Food","Серия блюд в одном свете",
  "[несколько блюд] KEEP each dish 1:1. Render all on the same dark surface with identical warm side light "
  "and grade — one consistent menu series.",
  "Меню как единая серия: один свет и грейд на все блюда.",
  "каждое блюдо","поверхность, свет","единый грейд","кадры вразнобой","identical light and grade for all"),
 (23,"Composite","Соединить человека и продукт",
  "[портрет + товар] KEEP both identities 1:1 — the exact face and the exact product. Compose them into one "
  "scene: the person presenting the product, with matched lighting.",
  "Композит: лицо и товар держим 1:1, объединяем в один кадр.",
  "лицо + товар","сцена","свет бренда","один из двух исказился","keep both face and product 1:1"),
 (24,"Composite","Объединить несколько референсов",
  "[до 14 референсов] Blend the provided references into one coherent scene, preserving each subject's "
  "identity and a shared warm color grade. (Pro, up to 14 images)",
  "Сборка из многих источников — до 14 референсов в Pro.",
  "все субъекты","сцена","общий грейд","детали смешались","Pro, keep each subject identity"),
 (25,"Composite","Рекламный key visual из источников",
  "[герой + товар + фон] Compose a campaign key visual: keep the hero and product 1:1, place them on the "
  "reference background, leave headline space, unify the lighting. (Pro)",
  "Финальный композит кампании из героя, товара и фона.",
  "герой + товар","компоновка","единый свет","несогласованный свет","unify light across all elements"),
]
lib_paginate("Библиотека Nano Banana", "Библиотека · Nano Banana",
  "25 промптов-правок", "Строятся иначе: сначала LOCK (что держим 1:1), потом CHANGE (что меняем), "
  "потом CONTINUITY (чем связываем серию). Работают и на русском.",
  [nbcard(*x) for x in NB])

# ---- Библиотека correction-промптов (20) ----
CORRCSS = r"""
.cc{border:1px solid var(--line);border-left:3px solid var(--o);border-radius:0 11px 11px 0;padding:10px 14px;margin:8px 0;background:#fff}
.cc .p{font-weight:800;font-size:10pt;color:var(--ink);line-height:1.2}
.cc .p .n{color:var(--o);margin-right:7px}
.cc .cz{font-size:8.6pt;color:var(--muted);line-height:1.35;margin:3px 0 6px}
.cc .cz b{color:var(--body)}
.cc .fx{font-family:'SF Mono',ui-monospace,Menlo,monospace;font-size:8.4pt;line-height:1.45;color:#ffd9b8;background:var(--dark);border-radius:8px;padding:8px 11px}
.cc .ck{font-size:8pt;color:#3f7d34;font-weight:700;margin-top:5px}
.cc .ck b{text-transform:uppercase;font-size:6.8pt;letter-spacing:.04em;color:#3f7d34;margin-right:4px}
"""
CSS = CSS + CORRCSS
def corrcard(n, problem, cause, fix_prompt, check):
    return (f'<div class="cc"><div class="p"><span class="n">{n:02d}</span>{problem}</div>'
            f'<div class="cz"><b>Причина:</b> {cause}</div>'
            f'<div class="fx">{fix_prompt}</div>'
            f'<div class="ck"><b>Проверь</b>{check}</div></div>')

CORR = [
 ("Лицо изменилось","слабый lock или слово «beautify»","KEEP the exact original face 1:1, do not beautify or reshape; redo only the requested edit.","черты лица 1:1 с исходником"),
 ("Голова непропорциональна","сильная правка позы/ракурса","Restore correct head-to-body proportions, keep realistic human anatomy.","соотношение головы и тела"),
 ("Продукт изменил форму","команда «сделай лучше»","KEEP product geometry and proportions exactly 1:1, revert any reshaping.","силуэт совпадает"),
 ("Логотип исказился","модель перерисовала знак","Restore the logo exactly as in the source, sharp and undistorted, do not redraw.","логотип 1:1"),
 ("Надпись нечитаемая","базовая модель или мелкий кегль","Re-render the text perfectly legible, correct spelling and clean kerning. Use Nano Banana Pro.","орфография и читаемость"),
 ("Руки сломались","сложная поза кистей","Fix hands to correct anatomy: five fingers, natural pose.","пальцы и суставы"),
 ("Появился лишний объект","модель «дофантазировала»","Remove the added object, keep only elements present in the original.","нет новых предметов"),
 ("Изменился цвет продукта","свет перекрасил товар","Restore the exact original product color and finish.","цвет как в исходнике"),
 ("Изменился материал","ретушь «улучшила» поверхность","Keep the original material and texture, do not restyle the surface.","фактура сохранена"),
 ("Фон не совпал по свету","новый фон из другого света","Match background light direction and temperature to the subject.","свет фона = свет объекта"),
 ("Герой выглядит приклеенным","нет тени и интеграции","Add a contact shadow and matching light so the subject sits naturally in the scene.","есть тень контакта"),
 ("Неправильная перспектива","объект из другой оптики","Correct perspective so the subject matches the scene vanishing lines.","линии сходятся верно"),
 ("Слишком сильная ретушь кожи","дефолтное «сглаживание»","Reduce skin retouch, restore natural texture and pores.","видна фактура кожи"),
 ("Лицо омолодилось","модель «улучшила» возраст","Keep the original apparent age, restore age-appropriate skin and features.","возраст как в исходнике"),
 ("Одежда изменилась","правка задела образ","Keep the exact original outfit — color, cut and details.","одежда 1:1"),
 ("Композиция стала слабее","правка сдвинула баланс","Restore stronger composition: subject on thirds, clear focal point.","объект по третям"),
 ("Герой слишком маленький","много воздуха вокруг","Scale the subject larger to fill the frame, keep proportions.","объект заполняет кадр"),
 ("Изменился цветовой стиль","грейд «уехал»","Restore the original color grade and palette.","палитра серии"),
 ("Кадр потерял глубину","всё в одном фокусе","Restore foreground-background separation and shallow depth of field.","есть отрыв плана"),
 ("Серия распалась","у кадра свой свет/грейд","Match this frame to the series: same light, palette, grade and camera language.","единый стиль серии"),
]
lib_paginate("Не перегенерируй — исправляй", "Correction library",
  "20 промптов-исправлений", "Профи отличается тем, что чинит результат, а не гонит заново. "
  "Проблема → причина → correction-промпт → что проверить.",
  [corrcard(i+1, *c) for i, c in enumerate(CORR)], per=4)

HTML = f'<meta charset="utf-8"><title>Midjourney + Nano Banana · система визуалов · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
