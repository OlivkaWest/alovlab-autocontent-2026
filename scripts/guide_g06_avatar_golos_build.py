# -*- coding: utf-8 -*-
"""AlovLab · Методичка G06 «Аватар и голос» — к карусели и рилсу дня 15 (15.10.2026). v2.

Правки по прямому ревью пользователя (v2, после первого рендера):
1) "Половина листа пустая" — все тонкие страницы объединены в более плотные (Как работает+Что
   понадобится, Шаблон брифа+Пример), добавлены новые разделы, усилены формулировки, чтобы заполнить
   лист без overflow (проверено визуально по каждой странице после рендера).
2) "Дальше нет нового дизайна" — добавлены новые визуальные компоненты, которых не было ни в одной
   методичке проекта: декоративная waveform-графика на обложке (тема — голос), цветные теговые чипы
   [excited]/[whispers] для аудио-тегов ElevenLabs, тёмные hero-stat плашки для сравнения версий
   HeyGen-аватара. Общая система (светлая основа + тёмные плашки под обложку/промпты) сохранена —
   это правило проекта (Приложение В CLAUDE.md), не вкусовщина, полностью ломать нельзя.
3) "Где промпты для ElevenLabs/HeyGen, где критичные для аватара вещи" — добавлены 2 новые главы:
   «ElevenLabs: Voice Design и Audio Tags» (реальный пример текстового промпта для создания голоса +
   реальный список emotion-тегов модели v3 с примером скрипта) и «HeyGen: критичные требования к
   аватару» (свет/фон/поза/одежда, с hero-stat сравнением версий). Источники — официальные страницы
   elevenlabs.io, всплывшие в поиске (прямой fetch на elevenlabs.io/community.heygen.com из этой среды
   заблокирован сетью) — честно отмечено в тексте и на странице «Источники», не выдано за личную
   проверку интерфейса.

Реестр (guides/00-registry.md): G06 покрывает дни 15-17, оценка объёма ~17 стр. Эта версия закрывает
главу дня 15 целиком (мультиязычный AI-дубляж + ElevenLabs + HeyGen + аватар) — главы под дни 16-17
(более широкий выбор инструментов) можно добавить отдельно, не меняя уже написанное.
Честность по числам (как в carousel.md и 00_START.txt дня 15): ни одно число сторонней платформы
(список языков, точный % качества) не называется без источника — см. главу «Источники».
Та же система A4-страниц + автонумерация, что в guide_day06_format_build.py.
Запуск: python3 scripts/guide_g06_avatar_golos_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>
"""
import math
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "guides" / "G06-avatar-i-golos"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "workbook.html"

def waveform_svg(n=56, w=600, h=100, color="#ff7a33", opacity=0.55):
    """Декоративная звуковая волна для обложки — тема методички про голос, не абстрактный узор."""
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
.team{background:linear-gradient(150deg,#241a10,#15100a);border:1px solid #3a2a18;border-radius:14px;padding:16px 19px;margin:10px 0;color:#f0e8dc}
.team .h{font-weight:800;font-size:12.5pt;color:#fff;margin-bottom:6px}.team p{font-size:9.8pt;line-height:1.5;color:#cdbfa8;max-width:none}
.team .dirs{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 3px}
.team .dirs span{font-size:8.4pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.2);border-radius:16px;padding:4px 10px}
a.tocref{color:inherit;text-decoration:none}
a.tocref:hover{text-decoration:underline}
.chain{display:flex;align-items:center;flex-wrap:wrap;gap:8px;margin:10px 0;background:#fff;
 border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.chain b{font-size:10.5pt;font-weight:800;color:var(--ink);background:var(--o-tint);border-radius:9px;padding:6px 11px}
.chain .a{color:var(--o);font-weight:800;font-size:13pt}
.warn{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:12px;padding:14px 16px;margin:10px 0}
.warn .h{font-weight:800;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px}
.warn p{font-size:10.5pt;color:var(--ink);line-height:1.5;margin:0;max-width:none}
.warn ul{margin:4px 0 0}
.warn li{font-size:10.3pt;color:var(--ink);line-height:1.48;max-width:none}
.tagchips{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
.tagchips span{font-family:'SF Mono',ui-monospace,Menlo,monospace;font-size:10pt;font-weight:700;
 color:#8a5a2a;background:#f1e9db;border:1px solid #e7d9bd;border-radius:20px;padding:6px 14px}
.herostat{display:flex;gap:11px;margin:12px 0}
.herostat .tile{flex:1;background:#13100A;border-radius:14px;padding:16px 14px;text-align:center}
.herostat .tile .num{font-weight:800;font-size:19pt;color:#F2A65A;display:block}
.herostat .tile .lbl{font-size:8.3pt;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:#cdbfa8;margin-top:4px;display:block}
"""
CSS = V2CSS + EXTRA
TOPIC = "Аватар и голос · G06"

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

# ---------- Результат ----------
add("01", "Что ты сделаешь к концу", "result", "Результат",
    head("Результат", "Что ты сделаешь к концу методички",
         "Для кого: нужен диктор на другом языке, рынке или под клиента — без студии и нового актёра озвучки.")
    + '<div class="chain"><b>сценарий</b><span class="a">→</span><b>аватар</b><span class="a">→</span><b>перевод + губы</b><span class="a">→</span><b>готовое видео</b></div>'
    + '<p>Записываешь сценарий один раз. Дальше пайплайн переводит текст и подстраивает движение губ под новый язык — на выходе видео, которое звучит и выглядит так, будто его записали заново на этом языке.</p>'
    + '<div class="cards c2">'
      '<div class="card"><div class="ct">Было</div><div class="ch">Новый язык, новый актёр</div><p>Каждый новый рынок — снова студия, снова запись, снова с нуля.</p></div>'
      '<div class="card"><div class="ct">Стало</div><div class="ch">Один сценарий, много языков</div><p>Пайплайн переводит и подстраивает движение губ под каждый нужный язык.</p></div></div>'
    + '<div class="cards c3" style="margin-top:9px">'
      '<div class="card"><div class="ct">Настройка</div><div class="ch">Один раз</div><p>Голос в ElevenLabs + бриф под задачу — дальше переиспользуешь.</p></div>'
      '<div class="card"><div class="ct">Тест</div><div class="ch">Короткий фрагмент</div><p>10-15 секунд перед тем как генерировать весь ролик.</p></div>'
      '<div class="card"><div class="ct">Генерация</div><div class="ch">Зависит от длины</div><p>Чем длиннее ролик, тем дольше рендер на платформе.</p></div></div>')

# ---------- Как это работает + Что понадобится ----------
add("02", "Как это работает", "how", "Как работает",
    head("Как работает", "Один пайплайн, три операции",
         "За кулисами один фокус: переводится не видео целиком — под новую речь перекраивается рот.")
    + '<div class="steps"><div class="step"><div class="sx"><b>Перевод текста.</b> Исходный сценарий переводится на целевой язык, с сохранением смысла и тона.</div></div>'
      '<div class="step"><div class="sx"><b>Синтез голоса.</b> Голос аватара озвучивает переведённый текст на целевом языке.</div></div>'
      '<div class="step"><div class="sx"><b>Подстройка губ.</b> Движение губ на видео подгоняется под новую речь, чтобы не было рассинхрона.</div></div></div>'
    + '<div class="gb"><div class="box bad"><div class="lbl">Без пайплайна</div>Новый язык — это новая студия, новый актёр озвучки, новый монтаж с нуля.</div>'
      '<div class="box good"><div class="lbl">С пайплайном</div>Новый язык — это один прогон уже готового сценария через три операции выше.</div></div>'
    + '<h3>Что понадобится до старта</h3>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Исходник</div><div class="ch">Сценарий или видео</div><p>На понятном тебе языке, без сленга и идиом — их сложнее переводить без потери смысла.</p></div>'
      '<div class="card"><div class="ct">Инструмент</div><div class="ch">ElevenLabs + HeyGen</div><p>Голос — в ElevenLabs, аватар и подстройка губ — в HeyGen (главы ниже).</p></div>'
      '<div class="card"><div class="ct">Список</div><div class="ch">Целевые языки/рынки</div><p>Конкретный список, не "все языки сразу" — под реальную задачу.</p></div></div>'
    + '<p class="note">Конкретные платформы реализуют эти три операции по-разному и с разным качеством — методичка описывает принцип и две реальные платформы (ElevenLabs, HeyGen), не рекламирует один сервис.</p>')

# ---------- Workflow ----------
add("03", "Workflow по шагам", "workflow", "Workflow",
    head("Шаг 01", "Workflow по шагам",
         "Пять шагов между «есть идея» и «готовое видео на новом языке».")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Подготовь сценарий</b> на исходном языке, без сленга и идиом, которые плохо переводятся.</div></div>'
      '<div class="step"><div class="sx"><b>Запиши или получи аватар-видео</b> на исходном языке (критичные требования к записи — глава «HeyGen: критичные требования к аватару»).</div></div>'
      '<div class="step"><div class="sx"><b>Выбери целевой язык</b> и прогони платформу на коротком тестовом фрагменте, 10-15 секунд.</div></div>'
      '<div class="step"><div class="sx"><b>Проверь перевод текста человеком</b>, не только автоматически — термины, имена, название бренда.</div></div>'
      '<div class="step"><div class="sx"><b>Прогони полную генерацию</b> и сверь синхронизацию губ и звук в нескольких случайных местах ролика.</div></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div><p>Тестовый фрагмент прошёл проверку человеком, перевод не исказил смысл и не потерял название бренда — только после этого запускаешь полную генерацию.</p></div>'
    + '<h3 style="margin-top:14px">Сколько это занимает по времени</h3>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Шаги 1-2</div><div class="ch">Один раз на проект</div><p>Сценарий и запись аватара переиспользуются для всех языков дальше.</p></div>'
      '<div class="card"><div class="ct">Шаги 3-4</div><div class="ch">~10-15 минут на язык</div><p>Тест, перевод и проверка человеком — главная статья времени на каждый новый язык.</p></div>'
      '<div class="card"><div class="ct">Шаг 5</div><div class="ch">Зависит от длины</div><p>Рендер полного ролика идёт на стороне платформы, не на твоём устройстве.</p></div></div>')

# ---------- ElevenLabs: запись и клонирование голоса ----------
add("04", "ElevenLabs: запись голоса", "elevenlabs", "ElevenLabs",
    head("Шаг 02", "ElevenLabs: запись и клонирование голоса",
         "Для своего голоса или голоса человека, который дал явное согласие — платформа прямо запрещает клонировать чужой голос без разрешения.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Запиши 1-2 минуты чистой речи.</b> Без фонового шума, только твой голос, обычный разговорный тон.</div></div>'
      '<div class="step"><div class="sx"><b>Используй разные интонации.</b> Вопросы, утверждения, немного эмоций в голосе — так клон звучит живее, не монотонно.</div></div>'
      '<div class="step"><div class="sx"><b>Создай клон в разделе Voices.</b> Add Voice → Clone a Voice, выбери Instant (быстрее) или Professional (точнее, дольше готовится), загрузи запись, дай голосу имя.</div></div>'
      '<div class="step"><div class="sx"><b>Проверь на странице Speech Synthesis.</b> Если звучит неестественно, подбери stability и similarity вручную — стартовая точка обычно в районе 50-70% и 75-85%.</div></div>'
      '<div class="step"><div class="sx"><b>Предупреди аудиторию.</b> Если голос звучит публично, честно скажи, что он синтетический.</div></div></div>'
    + '<div class="warn"><div class="h">Согласие обязательно</div><p>Клонировать можно только свой голос или голос человека, который дал на это явное разрешение — это требование самой платформы, не только этическая рекомендация.</p></div>'
    + '<div class="gb" style="margin-top:12px"><div class="box bad"><div class="lbl">Плохая запись</div>Эхо от стен, звук с улицы, диктофон телефона в кармане, запись через Bluetooth-наушники.</div>'
      '<div class="box good"><div class="lbl">Хорошая запись</div>Небольшая комната с мягкой мебелью, проводная гарнитура или обычный микрофон, телефон на расстоянии ладони.</div></div>'
    + '<h3 style="margin-top:14px">Какую модель синтеза выбрать</h3>'
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Multilingual v2</div><div class="ch">Качество</div><p>Самая стабильная интонация и акцент, дольше генерирует — выбор для финального ролика, который пойдёт в публикацию.</p></div>'
      '<div class="card"><div class="ct">Flash v2.5</div><div class="ch">Скорость</div><p>Низкая задержка, заметно быстрее — для черновика или быстрой проверки фразы, не для финала.</p></div>'
      '<div class="card"><div class="ct">Eleven v3</div><div class="ch">Эмоции (alpha)</div><p>Понимает audio-теги из следующей главы, но платформа сама помечает модель как альфа-версию.</p></div></div>')

# ---------- ElevenLabs: Voice Design и Audio Tags ----------
VOICE_DESIGN_EXAMPLE = "Спокойный мужской голос рассказчика, 40 лет, лёгкий южный акцент, неторопливый темп, тёплая интонация."
TAGGED_SCRIPT_EXAMPLE = "Это получилось! [excited] Погоди, ты серьёзно? [whispers] Я никому не говорил. [laughs]"
add("05", "Voice Design и Audio Tags", "voicedesign", "ElevenLabs · Продвинутый",
    head("ElevenLabs · Продвинутый уровень", "Voice Design и Audio Tags",
         "Голос необязательно записывать — иногда его можно просто описать словами, а внутри текста заставить шептать или кричать.")
    + prompt("VOICE DESIGN · ОПИСАНИЕ ГОЛОСА ТЕКСТОМ", VOICE_DESIGN_EXAMPLE,
             ru="Описываешь акцент, пол, темп, тон и манеру речи — платформа предлагает несколько вариантов голоса на выбор. Короткого промпта вроде «спокойный мужской рассказчик» тоже достаточно.")
    + '<h3>Теги эмоций (модель Eleven v3)</h3>'
    + '<div class="tagchips"><span>[excited]</span><span>[sad]</span><span>[whispers]</span><span>[shouts]</span><span>[laughs]</span><span>[sighs]</span></div>'
    + prompt("ПРИМЕР СО ВСТАВЛЕННЫМИ ТЕГАМИ", TAGGED_SCRIPT_EXAMPLE)
    + '<div class="warn"><div class="h">Прежде чем полагаться на теги</div><p>Тег работает, только если сам голос умеет так звучать — голосу, обученному на энергичной речи, сложно по-настоящему прошептать. Используй настройку стабильности Creative или Natural, не Robust: она меньше реагирует на теги. Промпт короче 250 знаков часто даёт нестабильный результат.</p></div>'
    + '<p class="note">Собрано по официальным страницам ElevenLabs — прямой доступ к elevenlabs.io из этой среды заблокирован сетью, модель v3 сама помечена платформой как alpha, сверяй точный список тегов перед использованием.</p>')
register_prompt("ElevenLabs Voice Design — пример описания голоса", VOICE_DESIGN_EXAMPLE)
register_prompt("ElevenLabs Audio Tags — пример скрипта с тегами", TAGGED_SCRIPT_EXAMPLE)

# ---------- Интеграция с HeyGen ----------
add("06", "Интеграция с HeyGen", "heygen", "HeyGen",
    head("Шаг 03", "Интеграция с HeyGen",
         "Три способа подключить голос из ElevenLabs к аватару HeyGen.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Способ 1</div><div class="ch">Через API-ключ</div><p>В HeyGen: вкладка AI Voice, подключить сторонний голос, выбрать ElevenLabs, вставить API-ключ. Голос появится в твоей библиотеке — дальше выбираешь его в сценарии как любой другой.</p></div>'
      '<div class="card"><div class="ct">Способ 2</div><div class="ch">Через готовый аудиофайл</div><p>Сгенерируй озвучку в ElevenLabs отдельно, скачай файл, загрузи его в HeyGen как голос за кадром. Плюс: можно переделать звук, не трогая видео, или сменить аватар, сохранив ту же дорожку.</p></div>'
      '<div class="card"><div class="ct">Способ 3</div><div class="ch">Встроенный Video Translate</div><p>У HeyGen есть своя функция перевода готового ролика одним действием, без ручной сборки через ElevenLabs — быстрее, но меньше контроля над интонацией и тегами эмоций.</p></div></div>'
    + '<h3>Как выбрать способ</h3>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Один язык, нужно быстро проверить гипотезу</b> — способ 1: подключил ключ один раз, дальше просто переключаешь голос в сценарии.</div></div>'
      '<div class="step"><div class="sx"><b>Несколько языков или нужно вручную доработать звук</b> (убрать паузу, поправить ударение) перед финальной сборкой — способ 2: правишь аудиофайл отдельно и заливаешь готовый.</div></div>'
      '<div class="step"><div class="sx"><b>Нужен черновик на новом языке за пару минут</b>, без тонкой настройки голоса — способ 3: быстрее всего, но проверь результат перед публикацией строже обычного.</div></div></div>'
    + '<div class="warn"><div class="h">Держи голос и аватар в одной версии проекта</div><p>Если между языками меняешь только дорожку голоса, а аватар и исходное видео остаются те же — синхронизация губ пересчитывается автоматически. Если меняешь ещё и аватара, проверяй синхронизацию заново для каждого языка, не полагайся на результат с другого ролика.</p></div>'
    + '<p class="note">Прямой доступ к community.heygen.com из этой среды заблокирован сетью, шаги собраны по нескольким независимым источникам, один из которых (справка самого HeyGen) выглядел наиболее достоверным, но не проверен напрямую — сверяй названия вкладок с текущим интерфейсом.</p>')

# ---------- HeyGen: критичные требования к аватару ----------
add("07", "Критичные требования к аватару", "avatarcheck", "HeyGen · Аватар",
    head("HeyGen · Чек-лист перед записью", "Критичные требования к аватару",
         "Качество аватара на 80% решается не промптом, а тем, что было в кадре на записи.")
    + '<div class="herostat">'
      '<div class="tile"><span class="num">~15 сек</span><span class="lbl">Новая версия аватара</span></div>'
      '<div class="tile"><span class="num">1-5 мин</span><span class="lbl">Более старые версии</span></div></div>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Свет.</b> Яркий и ровный, без резких теней на лице.</div></div>'
      '<div class="step"><div class="sx"><b>Фон.</b> Простой, нейтральный, без узора и лишних предметов.</div></div>'
      '<div class="step"><div class="sx"><b>Поза.</b> Смотри прямо в камеру, глаза на уровне линзы, без резких движений и наклонов.</div></div>'
      '<div class="step"><div class="sx"><b>Одежда и поведение.</b> Однотонная одежда, без бликующих очков, без громкого дыхания и движений в паузах.</div></div>'
      '<div class="step"><div class="sx"><b>Естественность.</b> Лёгкие кивки и моргание — это нормально, не старайся замереть: полная неподвижность в кадре на выходе выглядит более неестественно, чем живая, но спокойная речь.</div></div></div>'
    + '<div class="gb" style="margin-top:12px"><div class="box bad"><div class="lbl">Плохая запись</div>Контровой свет из окна за спиной, пёстрый фон с узором, резкие повороты головы, попытка сидеть абсолютно неподвижно.</div>'
      '<div class="box good"><div class="lbl">Хорошая запись</div>Свет спереди или сбоку, ровный однотонный фон, спокойный взгляд в камеру, естественные паузы между фразами.</div></div>'
    + '<div class="warn" style="margin-top:12px"><div class="h">Версия решает требования</div><p>Точная длительность записи и строгость требований зависят от версии аватара на платформе и могут измениться — сверяй на странице создания аватара перед записью, не полагайся на цифры из старого руководства.</p></div>')

# ---------- Шаблон брифа + Пример ----------
BRIEF_TEMPLATE = ("Ниша: [чем занимается бизнес или о чём ролик]\n"
"Целевой рынок и язык: [страна/аудитория, язык дубляжа]\n"
"Тон голоса: [разговорный / деловой / дружелюбный]\n"
"Длительность ролика: [секунды или минуты]\n"
"Не переводить дословно: [названия бренда, продукта, имена людей]\n"
"Ограничения: [что нельзя менять в видео или в тексте]")
add("08", "Шаблон брифа + пример", "brief", "Шаблон брифа",
    head("Шаг 04", "Шаблон брифа",
         "Заполняешь один раз под задачу, дальше используешь для каждого нового языка той же задачи.")
    + prompt("ШАБЛОН БРИФА · ЗАПОЛНИ ПОЛЯ", BRIEF_TEMPLATE)
    + '<h3>Пример (иллюстративный, не бриф реального клиента AlovLab)</h3>'
    + '<div class="io"><div class="c"><b>Ниша</b><p>Небольшая кофейня, аккаунт в соцсетях на русском языке.</p></div>'
      '<div class="c out"><b>Целевой рынок и язык</b><p>Испаноязычная аудитория, испанский язык.</p></div></div>'
    + '<div class="io" style="margin-top:9px"><div class="c"><b>Тон голоса</b><p>Дружелюбный, разговорный, без официоза.</p></div>'
      '<div class="c out"><b>Не переводить дословно</b><p>Название кофейни, имена бариста, названия фирменных напитков.</p></div></div>'
    + '<div class="io" style="margin-top:9px"><div class="c"><b>Длительность ролика</b><p>25-30 секунд, под формат Reels.</p></div>'
      '<div class="c out"><b>Ограничения</b><p>Не менять фон и логотип кофейни в кадре, не добавлять субтитры поверх лица.</p></div></div>')
register_prompt("Шаблон брифа для мультиязычного дубляжа", BRIEF_TEMPLATE)

# ---------- Чек-лист качества ----------
add("09", "Чек-лист качества", "check", "Checklist",
    head("Checklist", "Чек-лист качества перед публикацией",
         "Пройди по пунктам перед тем как показывать ролик аудитории.")
    + '<div class="callout check">'
      '<div class="row">Синхронизация губ выглядит естественно на крупных планах лица.</div>'
      '<div class="row">Паузы и интонация соответствуют смыслу, перевод не звучит слишком быстро или слишком медленно.</div>'
      '<div class="row">Имена, термины и название бренда переведены правильно, не искажены и не переведены дословно, если не нужно.</div>'
      '<div class="row">Субтитры (если есть) не перекрывают лицо и не обрезаны по краям кадра.</div>'
      '<div class="row">Тестовый фрагмент проверен человеком, который понимает целевой язык.</div>'
      '<div class="row">Если используешь audio-теги — голос реально меняет подачу, не просто скорость речи.</div>'
      '<div class="row">Аватар записан при ровном свете и на простом фоне — переделать запись дешевле, чем получить недовольного клиента.</div>'
      '<div class="row">Если использовал встроенный Video Translate (способ 3 HeyGen) — пересмотрел результат внимательнее обычного, контроля над интонацией там меньше.</div>'
      '<div class="row">Если менял и голос, и аватара одновременно — синхронизация перепроверена именно для этой пары, не предположена по аналогии с другим роликом.</div>'
      '<div class="row">Если ролик на несколько языков станет регулярным — заведён глоссарий бренда, список «не переводить» (глава Advanced).</div></div>')

# ---------- Частые ошибки ----------
add("10", "Частые ошибки", "errors", "Ошибки",
    head("Ошибки", "Частые ошибки", "")
    + '<div class="fix">'
      '<div class="r"><b>Доверять переводу вслепую.</b> Машинный перевод может исказить смысл или название бренда — проверка человеком обязательна.</div>'
      '<div class="r"><b>Пропустить тестовый фрагмент.</b> Генерировать сразу весь ролик, не проверив 10-15 секунд, — риск переделывать всё целиком.</div>'
      '<div class="r"><b>Переводить название бренда дословно.</b> Имена и названия продуктов часто должны оставаться как есть, не переводиться.</div>'
      '<div class="r"><b>Игнорировать разницу в длине текста.</b> Перевод короче или длиннее оригинала может сломать тайминг и синхронизацию губ.</div>'
      '<div class="r"><b>Записывать аватар в темноте или на фоне с узором.</b> Модель хуже считывает детали лица, итог выглядит смазанным.</div>'
      '<div class="r"><b>Ждать от тега [whispers] эффекта на энергичном голосе.</b> Если голос обучен только на громкой речи, результат звучит неестественно.</div>'
      '<div class="r"><b>Копировать настройки stability и similarity с другого ролика.</b> Один и тот же голос звучит по-разному на разных языках — подбирай заново, не переноси вслепую.</div>'
      '<div class="r"><b>Публиковать синтетический голос без предупреждения.</b> Если аудитория может принять его за живого человека, честно скажи, что голос искусственный.</div></div>')

# ---------- Advanced: голос бренда + Где уместно ----------
add("11", "Advanced: голос бренда", "advanced", "Advanced",
    head("Advanced", "Голос бренда на разных языках",
         "Как не потерять узнаваемость бренда, когда ролик звучит на новом языке.")
    + '<div class="card"><div class="ct">Глоссарий бренда</div><div class="ch">Список "не переводить"</div><p>Названия продуктов, имена людей, слоганы — фиксируешь один раз, используешь в каждом новом брифе, чтобы не решать заново каждый раз.</p></div>'
    + '<p class="note">Если ролик идёт на несколько языков регулярно, глоссарий экономит больше времени, чем сам пайплайн перевода.</p>'
    + '<h3>Пример строки глоссария</h3>'
    + '<div class="io"><div class="c"><b>Термин</b><p>«AlovLab» (название бренда)</p></div>'
      '<div class="c out"><b>Правило</b><p>Не переводить и не транслитерировать ни на одном языке, писать латиницей как есть.</p></div></div>'
    + '<h3 style="margin-top:14px">Где уместно, где нет</h3>'
    + '<div class="gb"><div class="box good"><div class="lbl">Хорошо подходит</div>Реклама, обучающий контент, обновления продукта для нескольких рынков, корпоративные видео.</div>'
      '<div class="box bad"><div class="lbl">Требует осторожности</div>Юридически значимые документы без проверки юристом, инструкции по безопасности без вычитки человеком, знающим язык.</div></div>')

# ---------- Источники ----------
add("12", "Источники", "sources", "Источники",
    head("Источники", "Честно про числа и шаги в этой методичке", "")
    + '<div class="warn"><div class="h">Статус чисел</div><ul>'
      '<li>Точный список языков, которые поддерживает та или иная AI-платформа дубляжа, и реальное качество синхронизации не проверены — сеть к документации платформ была недоступна при подготовке, а открытые источники дают противоречивые цифры (разброс «40+» до «175+» у одной и той же платформы).</li>'
      '<li>Поэтому в методичке нет конкретного числа языков сторонней платформы — проверяй актуальный список и качество на своей задаче, по тестовому фрагменту (глава «Workflow»).</li>'
      '<li>Пример брифа (стр. 08) — иллюстративный, не бриф реального клиента AlovLab.</li></ul></div>'
    + '<div class="warn" style="margin-top:9px"><div class="h">Статус шагов ElevenLabs и HeyGen (все 4 главы)</div><ul>'
      '<li>Прямой доступ к elevenlabs.io и community.heygen.com из этой среды заблокирован сетью при подготовке — шаги, список audio-тегов и требования к аватару собраны по нескольким официальным и независимым источникам, всплывшим в поиске, не сверены напрямую с живым интерфейсом.</li>'
      '<li>Названия кнопок, вкладок, точные значения настроек и требования к записи аватара зависят от версии платформы и могли измениться — сверяй перед использованием, не следуй шагам слепо.</li></ul></div>'
    + '<h3 style="margin-top:14px">Как снизить риск на своей задаче</h3>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Всегда начинай с теста</b> на 10-15 секунд (глава «Workflow») — это ловит расхождение с методичкой раньше, чем полный рендер.</div></div>'
      '<div class="step"><div class="sx"><b>Сохраняй скриншот интерфейса</b> на дату, когда платформой пользовался в последний раз — если меняешь её редко, сравнение быстро покажет, что изменилось.</div></div></div>')

# ---------- Сделай сейчас ----------
add("13", "Сделай сейчас", "action", "Сделай сейчас",
    head("Действие", "Сделай сейчас",
         "Пройди за один присест, не откладывай.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Заполни шаблон брифа</b> (стр. 08) под свою реальную задачу.</div></div>'
      '<div class="step"><div class="sx"><b>Прогони тестовый фрагмент</b> 10-15 секунд на целевом языке.</div></div>'
      '<div class="step"><div class="sx"><b>Попробуй один audio-тег</b> на своём голосе и послушай, меняется ли подача на самом деле, не только скорость.</div></div>'
      '<div class="step"><div class="sx"><b>Дай проверить перевод</b> человеку, который знает целевой язык, прежде чем генерировать весь ролик.</div></div>'
      '<div class="step"><div class="sx"><b>Заведи глоссарий бренда</b> (глава «Advanced»), если это не разовая задача, а регулярный мультиязычный контент.</div></div></div>'
    + '<div class="callout result" style="margin-top:14px"><div class="h">Итог методички</div><p>Один раз настроил голос и бриф — дальше пайплайн «сценарий → аватар → перевод + губы → готовое видео» (стр. 03) переиспользуется для каждого нового языка без новой студии и нового актёра озвучки.</p></div>')

# ---------- Курс ----------
add("14", "Дальше — на курсе", "course", "Дальше",
    head("Дальше", "Модуль «Земля Аватары» на курсе",
         "Работа с аватарами и голосом разбирается на курсе подробнее, с заданиями и проверкой.")
    + '<p>Курс «Нейросети и ChatGPT для каждого»: 6 видеоуроков, 6 «Земель» (Слова, Изображения, Видео, Звук, Аватары, Знания).</p>'
    + '<div class="cards c3" style="margin-top:9px">'
      '<div class="card"><div class="ct">МИНИ</div><div class="ch">Попробовать</div><p>1-й модуль «Земля Слов» + закрытый Telegram-канал + ИИ-ассистент по курсу.</p></div>'
      '<div class="card"><div class="ct">БАЗОВЫЙ</div><div class="ch">Полный курс</div><p>Все 6 видеоуроков + Telegram-канал + ИИ-ассистент + обновления материалов.</p></div>'
      '<div class="card"><div class="ct">ПРО</div><div class="ch">Хит продаж</div><p>Всё из Базового + доступ навсегда + сертификат + проверка заданий + личное менторство + приватный клуб.</p></div></div>'
    + '<div class="warn" style="margin-top:12px"><div class="h">Честно про цену</div><ul><li>Цену и точный состав тарифов проверяй на alovlab.ru перед тем как называть клиенту, здесь намеренно не фиксируем.</li></ul></div>')

# ---------- Команда ----------
add("15", "Путь в команду AlovLab", "team", "Команда",
    head("Путь дальше", "Путь в команду AlovLab",
         "Если тебе заходит собирать такие пайплайны не только для себя, у AlovLab есть открытый путь для сильных учеников.")
    + '<div class="team"><div class="h">Хочешь применять этот навык не только для себя?</div>'
      '<p>AlovLab открыт для учеников, которые хотят двигаться дальше отдельных приёмов: можно заявить о себе команде и претендовать на участие в реальных задачах под бренды по мере появления подходящих проектов.</p>'
      '<div class="dirs"><span>Аватары и дикторы</span><span>Видео-продакшн</span><span>Автоматизация</span></div>'
      '<p style="margin-top:8px">Это путь, а не готовое место и не обещание трудоустройства: конкретные проекты появляются по мере надобности бренда, не гарантированно и не по расписанию.</p></div>'
    + '<h3 style="margin-top:14px">Как заявить о себе</h3>'
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Пройди модуль «Земля Аватары»</b> с проверкой заданий — доступно на тарифе ПРО.</div></div>'
      '<div class="step"><div class="sx"><b>Собери свой пайплайн</b> на реальном примере и сохрани результат как часть портфолио.</div></div>'
      '<div class="step"><div class="sx"><b>Заяви о себе в приватном клубе курса</b>, когда появится подходящая задача под один из брендов.</div></div></div>')

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
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · методичка G06</div>
    <h1 style="font-weight:800;font-size:28pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:17ch">Аватар и голос</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Пайплайн мультиязычного дубляжа, ElevenLabs (клонирование, Voice Design, Audio Tags), критичные требования HeyGen-аватара, шаблон брифа.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Пайплайн</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">ElevenLabs + HeyGen</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Audio Tags</span>
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
    '<span class="kick">Содержание</span><h1 class="title">Пайплайн, бриф, чек-лист</h1>'
    '<p class="lead">Полная глава под день 15 календаря: мультиязычный дубляж, ElevenLabs (клонирование, Voice Design, Audio Tags), HeyGen (интеграция + требования к аватару). Оглавление кликабельно.</p>'
    f'<div style="margin-top:2px">{"".join(toc_rows)}</div>'))

for label, title, pid, section, html, num in numbered:
    P.append(page(section, num, html, pid=pid))

P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Один сценарий. Любой язык на выходе.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Шаблон брифа и примеры промптов этой методички — копипаст-готовые в prompts.txt рядом с этим файлом.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))

lines = ["AlovLab · G06 «Аватар и голос» — все промпты методички, копипаст-готовые.\n"]
for title, text in PROMPTS_TXT:
    lines.append(f"### {title}\n{text}\n")
(OUTDIR / "prompts.txt").write_text("\n".join(lines), encoding="utf-8")
print("prompts.txt:", len(PROMPTS_TXT), "prompts")
