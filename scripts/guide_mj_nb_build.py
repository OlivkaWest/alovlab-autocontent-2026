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

HTML = f'<meta charset="utf-8"><title>Midjourney + Nano Banana · система визуалов · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
