# -*- coding: utf-8 -*-
"""AlovLab · «Товар не тот. Проверка ИИ-рекламы перед сдачей» — методичка-спутник к карусели
«Реклама красивая. Товар — другой.» (content/dovodim-do-dela/carousels/day-06/, та же CORE IDEA,
что в Reels дня 6 «Доводим до дела», content/dovodim-do-dela/days/day-06.txt).

Источники:
- Собственная карусель дня 06 (правило трёх точек: силуэт/функциональные детали/пропорции).
- Присланные пользователем файлы (ae449acc-Caption.txt, d749efe8-Generation_Prompts.txt) — честные
  рабочие техники и готовый ретушь-промпт из расширенной версии той же темы (7-слайдовая карусель
  "КРАСИВАЯ ИИ-РЕКЛАМА. ТОВАР НЕ ТОТ."). Промпт и чек-лист перенесены без переписывания содержания,
  только адаптированы под формат методички (переменные, уровни, карточки).
- Ограничение честно перенесено из Caption.txt: приём наложения проверяет только видимый контур при
  одинаковом ракурсе — не доказывает совпадение со всех сторон.

По GLOBAL-METHODOLOGY-RULE.md (обычная методичка меньшего объёма, не связана с «Рилс дня» напрямую,
большой ACADEMY STANDARD объём здесь не обязателен). Система страниц — та же, что в
guide_dva_avatara_build.py / guide_pdf_v2_build.py.
Запуск: python3 scripts/guide_tovar_podmena_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>
"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "dovodim-do-dela" / "guides" / "tovar-podmena"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "workbook.html"

def waveform_svg(n=56, w=600, h=100, color="#ff7a33", opacity=0.55):
    import math
    bar_w = w / (n * 1.7)
    gap = bar_w * 0.7
    bars = []
    for i in range(n):
        v = (math.sin(i * 0.7) * 0.5 + math.sin(i * 0.31 + 1.3) * 0.3 + math.sin(i * 1.1 + 0.5) * 0.2)
        hh = (abs(v) * 0.78 + 0.22) * h
        x = i * (bar_w + gap)
        y = (h - hh) / 2
        bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{hh:.1f}" rx="{bar_w/2:.1f}" fill="{color}" opacity="{opacity}"/>')
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;height:{h}px;display:block" xmlns="http://www.w3.org/2000/svg">{"".join(bars)}</svg>'

EXTRA = r"""
.io{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}
.io .c{border:1px solid var(--line);border-radius:11px;padding:10px 13px;background:#fff}
.io .c.out{background:#fff7ef;border-color:#eccdb9}
.io .c b{font-weight:800;font-size:8pt;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}
.io .c.out b{color:var(--o)}
.io .c p{font-size:9.3pt;line-height:1.4;color:var(--ink);margin-top:3px;max-width:none}
.fix{display:grid;gap:8px;margin:10px 0}
.fix .r{background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 13px;font-size:9.8pt;line-height:1.45;color:var(--body)}
.fix .r b{color:var(--ink)}
a.tocref{color:inherit;text-decoration:none}
a.tocref:hover{text-decoration:underline}
.chain{display:flex;align-items:center;flex-wrap:wrap;gap:7px;margin:10px 0;background:#fff;
 border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.steps3{display:flex;flex-direction:column;gap:10px;margin:10px 0}
.steps3 .s{display:flex;gap:12px;align-items:flex-start;background:#fff;border:1px solid var(--line);
 border-radius:12px;padding:11px 14px}
.steps3 .s .n{flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:var(--o);color:#fff;
 font-weight:800;font-size:12pt;display:flex;align-items:center;justify-content:center}
.steps3 .s p{font-size:10pt;line-height:1.42;color:var(--body)}
.levels{display:grid;grid-template-columns:1fr 1fr 1fr;gap:9px;margin:10px 0}
.levels .lv{border:1px solid var(--line);border-radius:11px;padding:10px 12px;background:#fff}
.levels .lv b{font-size:8.3pt;font-weight:800;color:var(--o);text-transform:uppercase;letter-spacing:.04em}
.levels .lv p{font-size:9pt;line-height:1.4;color:var(--body);margin-top:4px}
.warn{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:12px;padding:14px 16px;margin:10px 0}
.warn .h{font-weight:800;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px}
.warn p{font-size:10.5pt;color:var(--ink);line-height:1.5;margin:0;max-width:none}
.warn ul{margin:4px 0 0}
.warn li{font-size:10.3pt;color:var(--ink);line-height:1.48;max-width:none}
"""

CSS = V2CSS + EXTRA
TOPIC = "ТОВАР НЕ ТОТ. ПРОВЕРКА ПЕРЕД СДАЧЕЙ"

def page(section, num, inner, pid=None):
    idattr = f' id="{pid}"' if pid else ''
    return (f'<section class="page"{idattr}><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main">{inner}</div>'
            f'<div class="pf"><span>AlovLab · {TOPIC}</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None):
    r = f'<div class="ru">{ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span></div>'
            f'<code>{code}</code>{r}</div>')

PROMPTS_TXT = []
def register_prompt(title, text):
    PROMPTS_TXT.append((title, text))

CONTENT = []
def add(toc_label, toc_title, pid, section, html):
    CONTENT.append((toc_label, toc_title, pid, section, html))

# ======================================================================
# ГЛАВА 1. ЗАЧЕМ ЭТО НУЖНО
# ======================================================================
add("01", "Зачем это нужно", "why", "Глава 1 · Зачем это нужно",
    head("Глава 1", "Красивая реклама. Товар не тот.",
         "AI-генерация товара может выглядеть дорого и убедительно — и при этом показывать другую "
         "вещь. Эта методичка — как ловить разницу до того, как её заметит клиент.")
    + '<p>Промпт для генерации обычно описывает сцену: свет, фон, настроение, композицию. Форму '
      'товара он не описывает — потому что кажется, что она и так есть на референсном фото. Модель '
      'при этом держит в фокусе то, что названо словами, а то, что не названо, достраивает по своим '
      'шаблонам: ручку, застёжку, носик, пропорции. Текст в кадре выглядит правильно. Товар — уже '
      'нет. А клиент сверяет именно товар, не текст.</p>'
    + '<div class="warn"><div class="h">Честно про масштаб проблемы</div><p>Это не брак конкретного '
      'инструмента и не повод отказаться от генераций. Это предсказуемое поведение любой модели, '
      'которая заполняет недосказанное по своим паттернам. Задача методички — не бороться с этим, а '
      'научиться замечать и проверять до сдачи.</p></div>'
    + '<p class="note">Дальше — рабочий метод из трёх точек проверки, технология разделения товара и '
      'фона, готовый промпт, чек-лист и таблица «ошибка → фикс».</p>')

# ======================================================================
# ГЛАВА 2. ПРАВИЛО ТРЁХ ТОЧЕК
# ======================================================================
add("02", "Правило трёх точек", "rule3", "Глава 2 · Метод",
    head("Глава 2", "Правило трёх точек",
         "Три места, которые проверяются первыми — до того, как смотреть на свет и композицию.")
    + '<div class="steps3">'
      '<div class="s"><div class="n">1</div><p><b>Силуэт.</b> Наложи исходник и генерацию друг на '
      'друга в одном ракурсе и масштабе — контур должен совпасть.</p></div>'
      '<div class="s"><div class="n">2</div><p><b>Функциональные детали.</b> Ручка, крышка, '
      'застёжка, кнопка, маркировка — пересчитать поштучно, не одним взглядом.</p></div>'
      '<div class="s"><div class="n">3</div><p><b>Пропорции.</b> Ширина к высоте — сверяй с '
      'исходником измерением, не на глаз.</p></div></div>'
    + '<h3 style="margin-top:14px">Как накладывать на практике</h3>'
    + '<p>Один ракурс и один масштаб для обоих изображений. Наложи их друг на друга, начни с '
      'прозрачности 50% — на этом уровне расхождение контура видно сразу, но исходник ещё читается '
      'под генерацией.</p>'
    + '<div class="warn"><div class="h">Честное ограничение метода</div><p>Наложение проверяет '
      'только видимый контур при одинаковом ракурсе. Оно не проверяет форму с других сторон и не '
      'заменяет осмотр детали целиком. Если ракурс в генерации другой — нужно либо новое фото под '
      'тот же угол, либо точная 3D-модель товара для сравнения.</p></div>')

# ======================================================================
# ГЛАВА 3. СБОРКА: ТОВАР ОТДЕЛЬНО, ФОН ОТДЕЛЬНО
# ======================================================================
add("03", "Сборка: товар отдельно, фон отдельно", "assembly", "Глава 3 · Технология",
    head("Глава 3", "Товар отдельно. Фон отдельно.",
         "Самый надёжный способ не потерять форму — вообще не позволять модели её перерисовывать.")
    + '<div class="chain"><b>фото в нужном ракурсе</b><span class="a">→</span>'
      '<b>товар на отдельный слой</b><span class="a">→</span>'
      '<b>генерация окружения</b><span class="a">→</span>'
      '<b>согласование тени и света</b><span class="a">→</span>'
      '<b>сведение в один кадр</b></div>'
    + '<div class="steps3">'
      '<div class="s"><div class="n">1</div><p>Возьми фото товара в том ракурсе, который нужен в '
      'финальном кадре — менять ракурс после вырезания сложнее, чем до.</p></div>'
      '<div class="s"><div class="n">2</div><p>Вырежи товар на отдельный слой. Сохрани исходный файл '
      'товара без изменений — это теперь эталон для сверки на каждом следующем шаге.</p></div>'
      '<div class="s"><div class="n">3</div><p>Генерируй окружение отдельно от товара. Согласуй '
      'перспективу, свет и тени с тем, что уже есть у товара на слое.</p></div></div>'
    + '<div class="levels">'
      '<div class="lv"><b>Быстрый</b><p>Один слой товара + сгенерированный фон позади, без смены '
      'ракурса — быстрее всего, подходит для несложных предметов.</p></div>'
      '<div class="lv"><b>Про</b><p>Добавляется контактная тень и согласование цветовой температуры '
      'света между товаром и фоном — выглядит убедительнее.</p></div>'
      '<div class="lv"><b>Advanced</b><p>Точная 3D-модель товара для любого нужного ракурса — '
      'избавляет от привязки к одному исходному фото.</p></div></div>'
    + '<div class="warn"><div class="h">Если нужен новый ракурс</div><p>Новый ракурс требует либо '
      'другого исходного фото под этот угол, либо точной 3D-модели. Не растягивай и не разворачивай '
      'товар по одной оси в двумерном редакторе — так форма искажается ровно так же, как и при '
      'генерации с нуля.</p></div>')

# ======================================================================
# ГЛАВА 4. РАБОЧИЙ ПРОМПТ
# ======================================================================
PROMPT_RU_READY = (
    "Ты ретушёр товарной рекламы. Используй фото как основу. Создай вокруг кружки светлый каменный "
    "стол и спокойный тёплый фон. Согласуй перспективу и свет с исходником.\n\n"
    "Сохрани корпус, ручку, край, цвет, фактуру и маркировку. Редактируй только окружение. Добавь "
    "контактную тень вне товара.\n\n"
    "Результат: один рекламный кадр без нового текста и лишних предметов."
)
PROMPT_RU_VARIABLE = (
    "Ты ретушёр товарной рекламы. Используй фото как основу. Создай вокруг [ТОВАР] "
    "[ОПИСАНИЕ ОКРУЖЕНИЯ: материал поверхности, время суток, настроение света]. Согласуй "
    "перспективу и свет с исходником.\n\n"
    "Сохрани корпус, [СПИСОК ФУНКЦИОНАЛЬНЫХ ДЕТАЛЕЙ ТОВАРА], цвет, фактуру и маркировку. Редактируй "
    "только окружение. Добавь контактную тень вне товара.\n\n"
    "Результат: один рекламный кадр без нового текста и лишних предметов."
)
register_prompt("Меняем фон, не товар (готовый, кружка на каменном столе)", PROMPT_RU_READY)
register_prompt("Меняем фон, не товар (с переменными под свой товар)", PROMPT_RU_VARIABLE)

add("04", "Рабочий промпт", "prompt", "Глава 4 · Промпт",
    head("Глава 4", "Меняем фон. Не товар.",
         "В редакторе выдели только фон. Товар оставь на отдельном слое. Промпт ниже работает именно "
         "с таким разделением — глава 3.")
    + prompt("Промпт · готовый пример", PROMPT_RU_READY)
    + '<h3 style="margin-top:14px">Версия с переменными — под любой товар</h3>'
    + prompt("Промпт · с переменными", PROMPT_RU_VARIABLE,
             "Что вставить: [ТОВАР] — одним словом; [ОПИСАНИЕ ОКРУЖЕНИЯ] — материал поверхности + "
             "время суток + настроение света; [СПИСОК ДЕТАЛЕЙ] — всё, что обязано остаться (ручка, "
             "крышка, носик, логотип). Что получить: один кадр, где меняется только окружение.")
    + '<div class="warn"><div class="h">Промпт не гарантирует точность</div><p>Запрос описывает '
      'намерение, не гарантирует результат. После каждой генерации — снова сверяй с исходным фото по '
      'правилу трёх точек (глава 2), не доверяй промпту на слово.</p></div>')

# ======================================================================
# ГЛАВА 5. ЧЕК-ЛИСТ ПЕРЕД СДАЧЕЙ
# ======================================================================
add("05", "Чек-лист перед сдачей", "checklist", "Глава 5 · Чек-лист",
    head("Глава 5", "Сверь с фото. Не по памяти.",
         "Три зоны проверки перед тем, как отправить кадр клиенту.")
    + '<div class="io">'
      '<div class="c"><b>Форма</b><p>Корпус, край, пропорции — сверка по правилу трёх точек (глава '
      '2).</p></div>'
      '<div class="c out"><b>Детали</b><p>Ручка, крепления, логотип и надписи — пересчитать '
      'поштучно.</p></div>'
      '<div class="c"><b>Впечатление</b><p>Материал, фактура, цвет с учётом освещения сцены.</p></div>'
      '</div>'
    + '<div class="result"><div class="h">Процедура наложения</div><p>Один ракурс + один масштаб. '
      'Наложи изображения друг на друга. Начни с прозрачности 50% — расхождение контура видно сразу.'
      '</p></div>'
    + '<div class="warn"><div class="h">Повтор честного ограничения</div><p>Наложение показывает '
      'видимый контур при текущем ракурсе. Оно не проверяет скрытую сторону товара — для этого нужен '
      'отдельный кадр или 3D-модель (глава 3).</p></div>')

# ======================================================================
# ГЛАВА 6. ЕСЛИ ДЕТАЛЬ ПОПЛЫЛА
# ======================================================================
add("06", "Если деталь поплыла", "fix", "Глава 6 · Ошибка → фикс",
    head("Глава 6", "Не уговаривай ИИ. Верни исходник.",
         "Три частых несовпадения и что с ними делать — не перегенерировать с нуля.")
    + '<div class="fix">'
      '<div class="r"><b>Другая форма.</b> Верни фото товара отдельным слоем (глава 3) и продолжай '
      'работу только с фоном — не проси модель «исправить» форму текстом, она будет гадать заново.</div>'
      '<div class="r"><b>Пропала или исказилась надпись.</b> Восстанови исходную маркировку с '
      'оригинального файла. Не перегенерируй надпись текстом — читаемый мелкий шрифт почти всегда '
      'искажается при генерации.</div>'
      '<div class="r"><b>Сложный материал (стекло, металл).</b> Проверяй отдельно просветы и '
      'отражения — часто в них остаётся старый фон, даже когда основная форма уже верная.</div></div>'
    + '<p class="note">Общий принцип: похожая вещь не заменяет нужный товар. Если деталь не '
      'получается с первого раза — это сигнал зафиксировать её как исходник, не повод для десятой '
      'попытки с тем же промптом.</p>')

# ======================================================================
# ГЛАВА 7. СДЕЛАЙ СЕЙЧАС
# ======================================================================
add("07", "Сделай сейчас", "action", "Глава 7 · Практика",
    head("Глава 7", "ACTION BLOCK: сделай сейчас",
         "Один реальный прогон метода на своём материале — 15-20 минут.")
    + '<div class="steps3">'
      '<div class="s"><div class="n">1</div><p>Возьми одну свою генерацию товара (или сделай новую) '
      'и её исходное фото в том же ракурсе.</p></div>'
      '<div class="s"><div class="n">2</div><p>Наложи оба изображения, прозрачность 50%, сверь '
      'силуэт — глава 2.</p></div>'
      '<div class="s"><div class="n">3</div><p>Если нашёл несовпадение — примени промпт из главы 4 '
      'с переменными под свой товар, со слоем товара, вырезанным отдельно (глава 3).</p></div>'
      '<div class="s"><div class="n">4</div><p>Пройди чек-лист главы 5 (форма / детали / '
      'впечатление) перед тем, как считать кадр готовым.</p></div></div>'
    + '<div class="result"><div class="h">QUALITY CHECK</div><p>Силуэт совпадает при наложении · '
      'все функциональные детали на месте и пересчитаны · маркировка читается как в оригинале · '
      'материал и фактура не потеряли реализм · проверка сделана после генерации, не вместо неё.</p>'
      '</div>')

# ======================================================================
# ГЛАВА 8. МОСТ В КУРС + ПУТЬ В КОМАНДУ ALOVLAB
# ======================================================================
add("08", "Куда дальше", "next", "Глава 8 · Куда дальше",
    head("Глава 8", "Куда дальше",
         "Этот метод закрывает один конкретный риск — несовпадение товара. Дальше система работы с "
         "изображениями шире.")
    + '<div class="io">'
      '<div class="c"><b>Если хочешь систему, не один приём</b><p>В курсе «Нейросети и ChatGPT для '
      'каждого» разбирается вся «Земля Изображений» — не только проверка товара, а полный путь от '
      'референса до готового рекламного кадра.</p></div>'
      '<div class="c out"><b>Если работаешь с товарной рекламой как бизнес</b><p>AlovLab Studio '
      'собирает визуальный конвейер под бренд — брифы через Telegram @alovlab, ответ за 24 часа. '
      'Цена на сайте не указана — не называем её здесь.</p></div></div>'
    + '<div class="result"><div class="h">Путь в команду AlovLab</div><p>Авторам, которые уверенно '
      'применяют этот метод на своих проектах и готовы показать реальные примеры «до/после» — пишите '
      'в Telegram-канал AlovLab с портфолио. Это не гарантия трудоустройства, а приглашение показать '
      'работу тем, кто ищет исполнителей под конкретные задачи.</p></div>'
    + '<p class="note">Контакты: Telegram t.me/AlovLab (закреп) · alovlab.ru</p>')

# ============================================================
# Сборка
# ============================================================
P = []
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 0">{waveform_svg()}</div>
  <div style="position:relative;z-index:2;padding:10px 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab Academy · методичка</div>
    <h1 style="font-weight:800;font-size:25pt;line-height:1.1;letter-spacing:-.02em;color:#fff;max-width:19ch">Товар не тот. Проверка ИИ-рекламы перед сдачей</h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Правило трёх точек, разделение товара и фона, рабочий промпт и таблица «ошибка → фикс» — спутник к карусели «Реклама красивая. Товар — другой.»</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">8 глав</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Готовый промпт внутри</span>
    </div>
  </div>
</section>""")

FIRST_CONTENT_NUM = 3
toc_rows = []
numbered = []
for i, (label, title, pid, section, html) in enumerate(CONTENT):
    num = FIRST_CONTENT_NUM + i
    numbered.append((label, title, pid, section, html, num))
    toc_rows.append(
        f'<a class="tocref" href="#{pid}"><div style="display:flex;align-items:baseline;gap:10px;padding:5.5px 0;border-bottom:1px solid var(--line2)">'
        f'<span style="font-weight:800;color:var(--o);font-size:9pt;width:24px">{label}</span>'
        f'<span style="font-weight:600;font-size:9.8pt;color:var(--ink)">{title}</span>'
        f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
        f'<span style="font-weight:700;color:var(--muted);font-size:9pt">{num:02d}</span></div></a>')

P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">8 глав</h1>'
    '<p class="lead">От причины несовпадения до готового промпта, чек-листа и таблицы ошибок. '
    'Оглавление кликабельно.</p>'
    f'<div style="margin-top:2px">{"".join(toc_rows)}</div>'))

for label, title, pid, section, html, num in numbered:
    P.append(page(section, num, html, pid=pid))

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))

lines = ["AlovLab · «Товар не тот» — рабочие промпты, копипаст-готовые.\n"]
for title, text in PROMPTS_TXT:
    lines.append(f"### {title}\n{text}\n")
(OUTDIR / "prompts.txt").write_text("\n".join(lines), encoding="utf-8")
print("prompts.txt:", len(PROMPTS_TXT), "items")
