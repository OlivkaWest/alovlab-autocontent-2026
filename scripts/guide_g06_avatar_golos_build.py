# -*- coding: utf-8 -*-
"""AlovLab · Методичка G06 «Аватар и голос» — к карусели и рилсу дня 15 (15.10.2026).
Реестр (guides/00-registry.md): G06 покрывает дни 15-17, оценка объёма ~17 стр. Эта версия закрывает
главу дня 15 (мультиязычный AI-дубляж: пайплайн + чек-лист качества) — главы под дни 16-17 (выбор
аватара, запись голоса) можно добавить отдельно, не меняя уже написанное.
Честность по числам (как в carousel.md и 00_START.txt дня 15): сеть к документации AI-платформ
заблокирована в этой среде, веб-поиск дал противоречивые цифры по числу языков (40+ vs 175+ у одной
и той же платформы) — ни одно число сторонней платформы не называется в методичке. Единственное число
(90+ языков, AlovLab Studio) используется только как отсылка к направлению, не как технический факт
о конкретной AI-платформе дубляжа.
Та же система A4-страниц + автонумерация, что в guide_day06_format_build.py.
Запуск: python3 scripts/guide_g06_avatar_golos_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>
"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "guides" / "G06-avatar-i-golos"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "workbook.html"

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
         "Для кого: нужен диктор на другом языке, рынке или под клиента, без студии и нового актёра озвучки.")
    + '<div class="chain"><b>сценарий</b><span class="a">→</span><b>аватар</b><span class="a">→</span><b>перевод + губы</b><span class="a">→</span><b>готовое видео</b></div>'
    + '<p>Записываешь сценарий один раз. Дальше пайплайн переводит текст и подстраивает движение губ под новый язык — на выходе видео, которое звучит и выглядит так, будто его записали заново на этом языке.</p>'
    + '<div class="cards c2">'
      '<div class="card"><div class="ct">Было</div><div class="ch">Новый язык, новый актёр</div><p>Каждый новый рынок — снова студия, снова запись, снова с нуля.</p></div>'
      '<div class="card"><div class="ct">Стало</div><div class="ch">Один сценарий, много языков</div><p>Пайплайн переводит и подстраивает движение губ под каждый нужный язык.</p></div></div>')

# ---------- Как это работает ----------
add("02", "Как это работает", "how", "Как работает",
    head("Как работает", "Один пайплайн, три операции",
         "Коротко, без привязки к одной конкретной платформе.")
    + '<div class="steps"><div class="step"><div class="sx"><b>Перевод текста.</b> Исходный сценарий переводится на целевой язык, с сохранением смысла и тона.</div></div>'
      '<div class="step"><div class="sx"><b>Синтез голоса.</b> Голос аватара озвучивает переведённый текст на целевом языке.</div></div>'
      '<div class="step"><div class="sx"><b>Подстройка губ.</b> Движение губ на видео подгоняется под новую речь, чтобы не было рассинхрона.</div></div></div>'
    + '<div class="gb"><div class="box bad"><div class="lbl">Без пайплайна</div>Новый язык — это новая студия, новый актёр озвучки, новый монтаж с нуля.</div>'
      '<div class="box good"><div class="lbl">С пайплайном</div>Новый язык — это один прогон уже готового сценария через три операции выше.</div></div>'
    + '<p class="note">Конкретные платформы реализуют эти три операции по-разному и с разным качеством — методичка описывает принцип, не рекламирует один сервис.</p>')

# ---------- Что понадобится ----------
add("03", "Что понадобится", "need", "Что понадобится",
    head("Шаг 01", "Что понадобится",
         "Собери это до того, как начнёшь — тогда не будешь метаться между вкладками посреди работы.")
    + '<div class="cards c3">'
      '<div class="card"><div class="ct">Исходник</div><div class="ch">Сценарий или видео</div><p>Записанный на понятном тебе языке, без сленга и идиом — их сложнее переводить без потери смысла.</p></div>'
      '<div class="card"><div class="ct">Инструмент</div><div class="ch">Платформа с переводом видео</div><p>С функцией перевода текста, синтеза голоса и подстройки губ под новый язык.</p></div>'
      '<div class="card"><div class="ct">Список</div><div class="ch">Целевые языки/рынки</div><p>Конкретный список, не "все языки сразу" — под реальную задачу.</p></div></div>')

# ---------- Workflow ----------
add("04", "Workflow по шагам", "workflow", "Workflow",
    head("Шаг 02", "Workflow по шагам", "")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Подготовь сценарий</b> на исходном языке, без сленга и идиом, которые плохо переводятся.</div></div>'
      '<div class="step"><div class="sx"><b>Запиши или получи аватар-видео</b> на исходном языке.</div></div>'
      '<div class="step"><div class="sx"><b>Выбери целевой язык</b> и прогони платформу на коротком тестовом фрагменте, 10-15 секунд.</div></div>'
      '<div class="step"><div class="sx"><b>Проверь перевод текста человеком</b>, не только автоматически — термины, имена, название бренда.</div></div>'
      '<div class="step"><div class="sx"><b>Прогони полную генерацию</b> и сверь синхронизацию губ и звук в нескольких случайных местах ролика.</div></div></div>'
    + '<div class="callout result"><div class="h">Что должно получиться</div><p>Тестовый фрагмент прошёл проверку человеком, перевод не исказил смысл и не потерял название бренда — только после этого запускаешь полную генерацию.</p></div>')

# ---------- ElevenLabs: запись и клонирование голоса ----------
add("05", "ElevenLabs: запись голоса", "elevenlabs", "ElevenLabs",
    head("Шаг 03", "ElevenLabs: запись и клонирование голоса",
         "Для своего голоса или голоса человека, который дал явное согласие — платформа прямо запрещает клонировать чужой голос без разрешения.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Запиши 1-2 минуты чистой речи.</b> Без фонового шума, только твой голос, обычный разговорный тон.</div></div>'
      '<div class="step"><div class="sx"><b>Используй разные интонации.</b> Вопросы, утверждения, немного эмоций в голосе — так клон звучит живее, не монотонно.</div></div>'
      '<div class="step"><div class="sx"><b>Создай клон в разделе Voices.</b> Add Voice → Clone a Voice, выбери Instant (быстрее) или Professional (точнее, дольше готовится), загрузи запись, дай голосу имя.</div></div>'
      '<div class="step"><div class="sx"><b>Проверь на странице Speech Synthesis.</b> Если звучит неестественно, подбери stability и similarity вручную — стартовая точка обычно в районе 50-70% и 75-85%, но точные значения зависят от версии интерфейса.</div></div>'
      '<div class="step"><div class="sx"><b>Предупреди аудиторию.</b> Если голос звучит публично, честно скажи, что он синтетический.</div></div></div>'
    + '<div class="warn"><div class="h">Согласие обязательно</div><p>Клонировать можно только свой голос или голос человека, который дал на это явное разрешение — это требование самой платформы, не только этическая рекомендация.</p></div>'
    + '<p class="note">Шаги собраны по нескольким независимым руководствам, прямой доступ к elevenlabs.io из этой среды был недоступен при подготовке (сеть заблокирована) — точные названия кнопок, минимальная длительность записи и стартовые значения stability/similarity могли измениться, сверяй с текущим интерфейсом.</p>')

# ---------- Интеграция с HeyGen ----------
add("06", "Интеграция с HeyGen", "heygen", "HeyGen",
    head("Шаг 04", "Интеграция с HeyGen",
         "Два способа подключить голос из ElevenLabs к аватару HeyGen.")
    + '<div class="cards c2">'
      '<div class="card"><div class="ct">Способ 1</div><div class="ch">Через API-ключ</div><p>В HeyGen: вкладка AI Voice, подключить сторонний голос, выбрать ElevenLabs, вставить API-ключ. Голос появится в твоей библиотеке — дальше выбираешь его в сценарии как любой другой.</p></div>'
      '<div class="card"><div class="ct">Способ 2</div><div class="ch">Через готовый аудиофайл</div><p>Сгенерируй озвучку в ElevenLabs отдельно, скачай файл, загрузи его в HeyGen как голос за кадром. Плюс: можно переделать звук, не трогая видео, или сменить аватар, сохранив ту же дорожку.</p></div></div>'
    + '<p class="note">Та же оговорка, что и в предыдущей главе: прямой доступ к community.heygen.com из этой среды был недоступен (сеть заблокирована), шаги собраны по нескольким независимым источникам, один из которых (справка самого HeyGen) выглядел наиболее достоверным, но не был проверен напрямую — сверяй названия вкладок с текущим интерфейсом перед использованием.</p>')

# ---------- Шаблон брифа ----------
BRIEF_TEMPLATE = ("Ниша: [чем занимается бизнес или о чём ролик]\n"
"Целевой рынок и язык: [страна/аудитория, язык дубляжа]\n"
"Тон голоса: [разговорный / деловой / дружелюбный]\n"
"Длительность ролика: [секунды или минуты]\n"
"Не переводить дословно: [названия бренда, продукта, имена людей]\n"
"Ограничения: [что нельзя менять в видео или в тексте]")
add("07", "Шаблон брифа", "brief", "Шаблон брифа",
    head("Шаг 05", "Шаблон брифа",
         "Заполняешь один раз под задачу, дальше используешь для каждого нового языка той же задачи.")
    + prompt("ШАБЛОН БРИФА · ЗАПОЛНИ ПОЛЯ", BRIEF_TEMPLATE))
register_prompt("Шаблон брифа для мультиязычного дубляжа", BRIEF_TEMPLATE)

# ---------- Пример ----------
add("08", "Пример заполненного брифа", "example", "Пример",
    head("Пример", "Заполненный бриф (иллюстративный пример)",
         "Учебный пример для методички, не бриф реального клиента AlovLab.")
    + '<div class="io"><div class="c"><b>Ниша</b><p>Небольшая кофейня, аккаунт в соцсетях на русском языке.</p></div>'
      '<div class="c out"><b>Целевой рынок и язык</b><p>Испаноязычная аудитория, испанский язык.</p></div></div>'
    + '<div class="io" style="margin-top:9px"><div class="c"><b>Тон голоса</b><p>Дружелюбный, разговорный, без официоза.</p></div>'
      '<div class="c out"><b>Не переводить дословно</b><p>Название кофейни, имена бариста, названия фирменных напитков.</p></div></div>')

# ---------- Чек-лист качества ----------
add("09", "Чек-лист качества", "check", "Checklist",
    head("Checklist", "Чек-лист качества перед публикацией",
         "Пройди по пунктам перед тем как показывать ролик аудитории.")
    + '<div class="callout check">'
      '<div class="row">Синхронизация губ выглядит естественно на крупных планах лица.</div>'
      '<div class="row">Паузы и интонация соответствуют смыслу, перевод не звучит слишком быстро или слишком медленно.</div>'
      '<div class="row">Имена, термины и название бренда переведены правильно, не искажены и не переведены дословно, если не нужно.</div>'
      '<div class="row">Субтитры (если есть) не перекрывают лицо и не обрезаны по краям кадра.</div>'
      '<div class="row">Тестовый фрагмент проверен человеком, который понимает целевой язык.</div></div>')

# ---------- Частые ошибки ----------
add("10", "Частые ошибки", "errors", "Ошибки",
    head("Ошибки", "Частые ошибки", "")
    + '<div class="fix">'
      '<div class="r"><b>Доверять переводу вслепую.</b> Машинный перевод может исказить смысл или название бренда — проверка человеком обязательна.</div>'
      '<div class="r"><b>Пропустить тестовый фрагмент.</b> Генерировать сразу весь ролик, не проверив 10-15 секунд, — риск переделывать всё целиком.</div>'
      '<div class="r"><b>Переводить название бренда дословно.</b> Имена и названия продуктов часто должны оставаться как есть, не переводиться.</div>'
      '<div class="r"><b>Игнорировать разницу в длине текста.</b> Перевод короче или длиннее оригинала может сломать тайминг и синхронизацию губ.</div></div>')

# ---------- Advanced ----------
add("11", "Advanced: голос бренда", "advanced", "Advanced",
    head("Advanced", "Голос бренда на разных языках",
         "Как не потерять узнаваемость бренда, когда ролик звучит на новом языке.")
    + '<div class="card"><div class="ct">Глоссарий бренда</div><div class="ch">Список "не переводить"</div><p>Названия продуктов, имена людей, слоганы — фиксируешь один раз, используешь в каждом новом брифе, чтобы не решать заново каждый раз.</p></div>'
    + '<p class="note">Если ролик идёт на несколько языков регулярно, глоссарий экономит больше времени, чем сам пайплайн перевода.</p>')

# ---------- Где уместно ----------
add("12", "Где уместно / где нет", "fit", "Где уместно",
    head("Границы применения", "Где уместно, где нет", "")
    + '<div class="gb"><div class="box good"><div class="lbl">Хорошо подходит</div>Реклама, обучающий контент, обновления продукта для нескольких рынков, корпоративные видео.</div>'
      '<div class="box bad"><div class="lbl">Требует осторожности</div>Юридически значимые документы без проверки юристом, инструкции по безопасности без вычитки человеком, знающим язык.</div></div>')

# ---------- Источники ----------
add("13", "Источники", "sources", "Источники",
    head("Источники", "Честно про числа и шаги в этой методичке", "")
    + '<div class="warn"><div class="h">Статус чисел</div><ul>'
      '<li>Точный список языков, которые поддерживает та или иная AI-платформа дубляжа, и реальное качество синхронизации не проверены — сеть к документации платформ была недоступна при подготовке, а открытые источники дают противоречивые цифры (разброс «40+» до «175+» у одной и той же платформы).</li>'
      '<li>Поэтому в методичке нет конкретного числа языков сторонней платформы — проверяй актуальный список и качество на своей задаче, по тестовому фрагменту (глава «Workflow»).</li>'
      '<li>Пример брифа (стр. 10) — иллюстративный, не бриф реального клиента AlovLab.</li></ul></div>'
    + '<div class="warn" style="margin-top:9px"><div class="h">Статус шагов ElevenLabs и HeyGen (главы «ElevenLabs», «HeyGen»)</div><ul>'
      '<li>Прямой доступ к elevenlabs.io и community.heygen.com из этой среды был недоступен при подготовке (сеть заблокирована) — шаги собраны по нескольким независимым руководствам, не сверены напрямую с официальным интерфейсом.</li>'
      '<li>Названия кнопок, вкладок и стартовые значения настроек (stability/similarity) могут отличаться в текущей версии интерфейса — сверяй перед использованием, не следуй шагам слепо.</li></ul></div>')

# ---------- Сделай сейчас ----------
add("14", "Сделай сейчас", "action", "Сделай сейчас",
    head("Действие", "Сделай сейчас",
         "Пройди за один присест, не откладывай.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Заполни шаблон брифа</b> (стр. 05) под свою реальную задачу.</div></div>'
      '<div class="step"><div class="sx"><b>Прогони тестовый фрагмент</b> 10-15 секунд на целевом языке.</div></div>'
      '<div class="step"><div class="sx"><b>Дай проверить перевод</b> человеку, который знает целевой язык, прежде чем генерировать весь ролик.</div></div></div>')

# ---------- Курс ----------
add("15", "Дальше — на курсе", "course", "Дальше",
    head("Дальше", "Модуль «Земля Аватары» на курсе",
         "Работа с аватарами и голосом разбирается на курсе подробнее, с заданиями и проверкой.")
    + '<p>Курс «Нейросети и ChatGPT для каждого»: 6 видеоуроков, 6 «Земель» (Слова, Изображения, Видео, Звук, Аватары, Знания). Поддержка: закрытый Telegram-канал и ИИ-ассистент по курсу на всех тарифах, личное менторство на тарифе ПРО.</p>'
    + '<div class="warn"><div class="h">Честно про цену</div><ul><li>Цену и состав тарифов проверяй на alovlab.ru перед тем как называть клиенту, здесь намеренно не фиксируем.</li></ul></div>')

# ---------- Команда ----------
add("16", "Путь в команду AlovLab", "team", "Команда",
    head("Путь дальше", "Путь в команду AlovLab",
         "Если тебе заходит собирать такие пайплайны не только для себя, у AlovLab есть открытый путь для сильных учеников.")
    + '<div class="team"><div class="h">Хочешь применять этот навык не только для себя?</div>'
      '<p>AlovLab открыт для учеников, которые хотят двигаться дальше отдельных приёмов: можно заявить о себе команде и претендовать на участие в реальных задачах под бренды по мере появления подходящих проектов.</p>'
      '<div class="dirs"><span>Аватары и дикторы</span><span>Видео-продакшн</span><span>Автоматизация</span></div>'
      '<p style="margin-top:8px">Это путь, а не готовое место и не обещание трудоустройства: конкретные проекты появляются по мере надобности бренда, не гарантированно и не по расписанию.</p></div>')

# ============================================================
# Сборка
# ============================================================
P = []
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · методичка G06</div>
    <h1 style="font-weight:800;font-size:28pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:17ch">Аватар и голос</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Мультиязычный AI-дубляж: пайплайн, запись и клонирование голоса в ElevenLabs, интеграция с HeyGen, шаблон брифа и чек-лист качества.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Пайплайн</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">ElevenLabs + HeyGen</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Шаблон брифа</span>
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
    '<p class="lead">Глава под день 15 календаря (мультиязычный дубляж), включая запись и клонирование голоса в ElevenLabs и интеграцию с HeyGen. Глава под дни 16-17 (выбор аватара) можно добавить сюда же позже. Оглавление кликабельно.</p>'
    f'<div style="margin-top:2px">{"".join(toc_rows)}</div>'))

for label, title, pid, section, html, num in numbered:
    P.append(page(section, num, html, pid=pid))

P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Один сценарий. Любой язык на выходе.</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Шаблон брифа этой методички — копипаст-готовый в prompts.txt рядом с этим файлом.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))

lines = ["AlovLab · G06 «Аватар и голос» — шаблон брифа, копипаст-готовый.\n"]
for title, text in PROMPTS_TXT:
    lines.append(f"### {title}\n{text}\n")
(OUTDIR / "prompts.txt").write_text("\n".join(lines), encoding="utf-8")
print("prompts.txt:", len(PROMPTS_TXT), "prompts")
