# -*- coding: utf-8 -*-
"""AlovLab · «Два аватара. Один разговор» — методичка по ALOVLAB-ACADEMY-STANDARD.

Тема: как собрать вертикальный ролик, где два AI-аватара (HeyGen) ведут диалог — каждый снят
отдельным клипом, затем смонтирован в один разговор. Прямое продолжение рилса+карусели дня 19
(content/october-2026-system/reels-extra/day-19/, carousels-extra/day-19/) и текста второго
ведущего (reels-extra/day-19/ru/06_HOST_B_SCRIPT.txt).

БАТЧ 1 (эта версия файла): главы 1-4 — "Как устроен процесс" (цепочка, разница аватар/TTS/
клонирование/монтаж), "Инструменты" (честно, HeyGen/ElevenLabs/монтаж вручную vs Claude Code/Codex —
раздел про внешнее аудио для HeyGen помечен по итогам отдельного исследования этой же сессии),
"Сценарий, который звучит как разговор" (принципы), "Три готовых сценария" (полные, по 30-60 сек).
Главы 5+ (подготовка аватаров, голоса, генерация реплик, сборка, монтаж через Claude Code/Codex,
готовые промпты, ошибки, практическое задание) — следующие батчи.

Честность по источникам: факты о Claude Code/Codex — переиспользованы из исследования этой же сессии
для guide_klod_montazh_build.py (code.claude.com/docs — прямое чтение; github.com/openai/codex —
частично прямое чтение, частично WebSearch по developers.openai.com, заблокированному сетью среды).
Факт о передаче внешнего аудио в HeyGen для озвучки аватара — отдельное исследование специально под
эту методичку, см. пометку в главе 2.

Та же система A4-страниц + автонумерация, что в guide_g07_academy_build.py / guide_klod_montazh_build.py.
Запуск: python3 scripts/guide_dva_avatara_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>
"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "guides" / "dva-avatara-odin-razgovor"
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
.chain b{font-size:9.3pt;font-weight:800;color:var(--ink);background:var(--o-tint);border-radius:9px;padding:6px 8px}
.chain .a{color:var(--o);font-weight:800;font-size:11pt}
.warn{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:12px;padding:14px 16px;margin:10px 0}
.warn .h{font-weight:800;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px}
.warn p{font-size:10.5pt;color:var(--ink);line-height:1.5;margin:0;max-width:none}
.warn ul{margin:4px 0 0}
.warn li{font-size:10.3pt;color:var(--ink);line-height:1.48;max-width:none}
.gb{display:flex;gap:12px;margin:10px 0}
.gb .box{flex:1;border-radius:12px;padding:12px 15px}
.gb .box.bad{background:#FCEEEA;border:1px solid #EFC7BB}
.gb .box.good{background:#EAF3EC;border:1px solid #BFDCC6}
.gb .lbl{font-size:8.3pt;font-weight:800;text-transform:uppercase;margin-bottom:5px}
.gb .bad .lbl{color:#C0492E}
.gb .good .lbl{color:#3E8E55}
.gb p{font-size:9.6pt;font-weight:500;color:var(--ink);line-height:1.4;max-width:none}
.checklist{display:flex;flex-direction:column;gap:7px;margin:10px 0}
.checklist .row{display:flex;gap:9px;align-items:flex-start;font-size:9.8pt;line-height:1.42;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:10px;padding:9px 12px}
.checklist .row::before{content:"";flex:0 0 auto;width:14px;height:14px;border:1.5px solid var(--o);border-radius:4px;margin-top:2px}
.result{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:12px;padding:12px 15px;margin:10px 0}
.result .h{font-weight:800;font-size:8.3pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:5px}
.result p{font-size:10pt;color:var(--ink);line-height:1.42;margin:0;max-width:none}
.turn{display:flex;gap:10px;margin:8px 0;align-items:flex-start}
.turn .who{flex:0 0 auto;width:30px;height:30px;border-radius:50%;display:flex;align-items:center;
 justify-content:center;font-weight:800;font-size:11pt;color:#fff}
.turn.a .who{background:var(--ink)}
.turn.b .who{background:var(--o)}
.turn .body{flex:1;background:#fff;border:1px solid var(--line);border-radius:11px;padding:9px 13px}
.turn .line{font-size:10.3pt;font-weight:600;color:var(--ink);line-height:1.4}
.turn .meta{display:flex;gap:7px;margin-top:6px;flex-wrap:wrap}
.turn .meta span{font-size:7.3pt;font-weight:800;letter-spacing:.03em;text-transform:uppercase;
 color:var(--muted);background:#f6efe3;border-radius:6px;padding:2px 6px}
"""
CSS = V2CSS + EXTRA
TOPIC = "ДВА АВАТАРА. ОДИН РАЗГОВОР"

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

def turn(speaker, text, emotion, duration, note):
    letter = "А" if speaker == "a" else "Б"
    cls = "a" if speaker == "a" else "b"
    return (f'<div class="turn {cls}"><div class="who">{letter}</div>'
            f'<div class="body"><div class="line">{text}</div>'
            f'<div class="meta"><span>{emotion}</span><span>~{duration}</span><span>{note}</span></div>'
            f'</div></div>')

CONTENT = []
def add(toc_label, toc_title, pid, section, html):
    CONTENT.append((toc_label, toc_title, pid, section, html))

# ======================================================================
# ГЛАВА 1. КАК УСТРОЕН ПРОЦЕСС
# ======================================================================
add("01", "Как устроен процесс", "process", "Глава 1 · Процесс",
    head("Глава 1", "Как устроен процесс",
         "К концу этого учебника у тебя будет вертикальный ролик на 30-60 секунд: два аватара "
         "разговаривают разными голосами и отвечают друг другу по смыслу.")
    + '<p>Два аватара в одном видео не записываются одновременно, как два актёра в одной комнате. Каждый снимается отдельным клипом — у своего аватара, со своим голосом, — а то, что выглядит одним разговором, собирается на монтаже. Это не обман зрителя: это ровно та же логика, что у озвучки мультфильма, просто с цифровыми ведущими вместо рисованных персонажей.</p>'
    + '<div class="chain">'
      '<b>идея</b><span class="a">→</span><b>сценарий-диалог</b><span class="a">→</span><b>два персонажа</b><span class="a">→</span><b>два голоса</b><span class="a">→</span><b>генерация видео</b><span class="a">→</span><b>монтаж</b><span class="a">→</span><b>субтитры</b><span class="a">→</span><b>проверка</b><span class="a">→</span><b>публикация</b>'
      '</div>'
    + '<h3 style="margin-top:14px">Четыре вещи, которые легко перепутать</h3>'
    + '<div class="io">'
      '<div class="c"><b>Аватар</b><p>Цифровое изображение человека (реального прототипа или сгенерированного), которое двигает губами и лицом синхронно с озвучкой. Сам по себе ничего не «говорит» — просто подстраивается под готовый звук.</p></div>'
      '<div class="c out"><b>Синтез речи (TTS)</b><p>Текст превращается в звук голосом из готовой библиотеки. Быстро, но голос — чужой, стандартный, не твой собственный.</p></div>'
      '<div class="c"><b>Клонирование голоса</b><p>Модель твоего собственного (или другого, с согласия) голоса, которая озвучивает любой новый текст. Подробный процесс — методичка G07 «Создай свой AI-голос».</p></div>'
      '<div class="c out"><b>Монтаж</b><p>Сборка готовых озвученных клипов в одну последовательность: границы фраз, паузы, громкость, субтитры, финальный экспорт. Отдельный навык, не включён ни в один из инструментов озвучки.</p></div></div>'
    + '<div class="warn"><div class="h">Это не живой человек на видео</div><p>У каждого аватара в этом учебнике может быть реальный прототип (твоё лицо, лицо коллеги, лицензированный персонаж) — но на экране не идёт прямая трансляция человека. Это цифровая версия, управляемая текстом и звуком. Честно говорим об этом в описании, а не выдаём за запись живого эфира.</p></div>'
    + '<p class="note">Главный принцип учебника: сначала пишем цельный диалог, потом реплики каждого персонажа, и только потом собираем по очереди. Не наоборот.</p>')

# ======================================================================
# ГЛАВА 2. ИНСТРУМЕНТЫ
# ======================================================================
add("02", "Инструменты", "tools", "Глава 2 · Инструменты",
    head("Глава 2", "Инструменты",
         "Один основной инструмент на оба аватара плюс голоса, и два равноценных пути для монтажа.")
    + '<div class="io">'
      '<div class="c"><b>HeyGen — основной</b><p>Создание аватаров и генерация озвученного видео. Есть собственная библиотека голосов и возможность подключить голос из ElevenLabs — подробный разбор интеграции в методичке G07, глава 9 (следующий батч).</p></div>'
      '<div class="c out"><b>ElevenLabs — дополнительно</b><p>Нужен, если хочешь собственный клонированный голос, а не один из готовых в библиотеке HeyGen. Результат — обычный аудиофайл, который дальше используется как источник озвучки.</p></div></div>'
    + '<div class="warn"><div class="h">Честно про внешний аудиофайл для озвучки аватара</div><p>У HeyGen есть режим «Audio to Video» — вместо текста из библиотеки подаёшь готовый аудиофайл (например, из ElevenLabs), и аватар подстраивает губы под него. По документации HeyGen на эту функцию (WebSearch 19.10.2026, прямой доступ к docs.heygen.com заблокирован сетью этой среды — вторичное подтверждение, не прямой просмотр страницы) есть сама старая версия этой страницы с пометкой «архивная» — значит механика точно менялась, не ориентируйся на туториалы старше полугода.</p>'
      '<ul>'
      '<li>Формат — MP3 или WAV, но лимит размера файла в двух собственных страницах HeyGen расходится: 32 МБ на одной, 50 МБ на другой. Проверь актуальную цифру в интерфейсе перед загрузкой длинной дорожки.</li>'
      '<li>Если грузишь аудио по ссылке (не файлом с компьютера) — ссылка должна вести прямо на файл, не на страницу «поделиться» в облачном хранилище (один пользователь столкнулся с ошибкой именно из-за этого).</li>'
      '</ul></div>'
    + '<h3 style="margin-top:14px">Монтаж: два равноценных пути</h3>'
    + '<div class="io">'
      '<div class="c"><b>Вручную</b><p>Любой видеоредактор (CapCut, Premiere, DaVinci Resolve) — тянешь клипы на дорожку руками, режешь по границам фраз, добавляешь субтитры. Не требует программирования, требует внимательности к деталям (глава 7).</p></div>'
      '<div class="c out"><b>Через AI-агента</b><p>Claude Code или Codex CLI запускают ffmpeg по твоей команде текстом — агент режет, синхронит и собирает файл сам. Требует подготовленного репозитория (глава 8, тот же принцип, что в методичке «Монтаж с AI-агентом»).</p></div></div>'
    + '<p class="note">Важно: обычный чат с Claude или ChatGPT в браузере не монтирует видео сам по себе — для этого нужна отдельная среда с доступом к файлам и инструментам (терминал, Claude Code или Codex CLI), не просто переписка в окне чата.</p>')

# ======================================================================
# ГЛАВА 3. СЦЕНАРИЙ, КОТОРЫЙ ЗВУЧИТ КАК РАЗГОВОР
# ======================================================================
add("03", "Сценарий, который звучит как разговор", "script-principles", "Глава 3 · Сценарий",
    head("Глава 3", "Сценарий, который звучит как разговор",
         "Два текста, записанных отдельно, легко превращаются в два монолога подряд. Разговором их делают конкретные приёмы.")
    + '<div class="fix">'
      '<div class="r"><b>Разные роли, не два диктора.</b> Один ведущий двигает мысль вперёд (объясняет, предлагает), второй — проверяет её (сомневается, спрашивает, иногда шутит). Если оба только объясняют по очереди — это не диалог, а поделенный пополам монолог.</div>'
      '<div class="r"><b>Почему два монолога не становятся диалогом.</b> Признак монолога под видом диалога: реплики можно переставить местами без потери смысла. В настоящем диалоге вторая реплика невозможна без первой — она именно отвечает, переспрашивает или спорит с конкретным словом из предыдущей фразы.</div>'
      '<div class="r"><b>Убирай повторные объяснения.</b> Если второй ведущий пересказывает своими словами то же самое, что уже сказал первый, — это не усиление, а повтор, который зритель слышит как воду.</div>'
      '<div class="r"><b>Где оставить паузу.</b> Пауза нужна после переспроса или сомнения — зритель должен успеть ощутить момент «хм, а правда», прежде чем услышит ответ. Пауза внутри уверенного объяснения, наоборот, разваливает мысль.</div>'
      '<div class="r"><b>Один CTA на весь ролик.</b> Финал — это одна фраза одного (любого) из двух ведущих. Если оба в конце зовут куда-то по отдельности, зритель не помнит ни одного призыва — выбирай один и отдавай его тому, чья роль в конце сильнее.</div></div>'
    + '<p class="note">Дальше — три готовых сценария, написанных по этим правилам, разных по тону и длине.</p>')

# ======================================================================
# ГЛАВА 4. ТРИ ГОТОВЫХ СЦЕНАРИЯ
# ======================================================================
SCRIPT_1 = [
    ("a", "Ты правда думаешь, что нейросеть заменит тебе ассистента?", "вызов", "3 сек", "хук, жёсткий кадр"),
    ("b", "Звучит как маркетинг. Покажи на реальном примере.", "скепсис", "3 сек", "без паузы"),
    ("a", "Даю ей черновик письма клиенту. Она чистит формулировки за пятнадцать секунд.", "спокойная уверенность", "4 сек", "короткая пауза после"),
    ("b", "А если она напутает в смысле?", "сомнение", "2.5 сек", "без паузы"),
    ("a", "Тогда я правлю сам. Она делает черновую работу, не финальное решение.", "твёрдо", "4 сек", "пауза 0.5с"),
    ("b", "То есть это помощник, а не замена.", "осознание", "2.5 сек", "без паузы"),
    ("a", "Именно. Экономит то время, которое уходило на рутину.", "подтверждение", "3.5 сек", "пауза перед CTA"),
    ("b", "Хочешь такую же связку под свою рутину? Пиши в комментах под этим постом.", "приглашение", "4 сек", "финал, кадр держится до конца фразы"),
]
SCRIPT_2 = [
    ("a", "Поставил бота отвечать в директ. Через день уже не понимаю, кто со мной говорит, я или он.", "лёгкая тревога", "4 сек", "хук"),
    ("b", "А клиенты жалуются?", "любопытство", "2 сек", "без паузы"),
    ("a", "Наоборот. Говорят, стало быстрее отвечаю.", "удивление", "3 сек", "короткая пауза"),
    ("b", "Жутковато, если честно.", "ирония", "2 сек", "без паузы"),
    ("a", "Есть такое. Но сложные вопросы он скидывает мне, не выдумывает ответ.", "спокойно", "4 сек", "пауза 0.5с"),
    ("b", "То есть граница всё равно за тобой.", "вывод", "2.5 сек", "без паузы"),
    ("a", "Всегда. Он забирает рутину, не решения.", "твёрдо", "3 сек", "пауза перед CTA"),
    ("b", "Как настроить такую границу, расскажи в комментах под этим постом.", "приглашение", "4 сек", "финал"),
]
SCRIPT_3 = [
    ("a", "Я работаю с девяти до шести. Ты вообще не отдыхаешь.", "наблюдение", "3 сек", "хук, лёгкий тон"),
    ("b", "Я и не человек, чтобы отдыхать.", "сухая ирония", "2.5 сек", "без паузы"),
    ("a", "Тогда почему вечно жалуешься на долгий рендер?", "подкол", "3 сек", "короткая пауза"),
    ("b", "Потому что у меня тоже есть характер.", "гордо", "2.5 сек", "без паузы"),
    ("a", "Ладно, покажи характер на реальном примере.", "вызов", "2.5 сек", "пауза 0.5с"),
    ("b", "Было бы на чём. Ты мне текст ещё не прислал.", "подкол в ответ", "3 сек", "без паузы"),
    ("a", "Логично. Значит, характер подождёт моего сценария.", "самоирония", "3 сек", "пауза перед CTA"),
    ("a", "Как мы вдвоём это записали, смотри в комментах под этим постом.", "приглашение", "4 сек", "финал"),
]

def script_block(turns):
    return "".join(turn(s, t, e, d, n) for s, t, e, d, n in turns)

add("04", "Сценарий 1: эксперт и вопросы", "script-1", "Глава 4.1 · Сценарии",
    head("Глава 4.1", "Эксперт объясняет, второй ведущий задаёт вопросы",
         "~28 секунд, 8 реплик. Тема: польза и граница применимости нейросети-ассистента.")
    + script_block(SCRIPT_1)
    + '<div class="result"><div class="h">Что должно получиться</div><p>Слушается как спор человека со скептиком, а не как лекция — вторая реплика каждый раз ловит конкретное слово первой («маркетинг», «напутает», «помощник»).</p></div>')

add("05", "Сценарий 2: обсуждение продукта", "script-2", "Глава 4.2 · Сценарии",
    head("Глава 4.2", "Два ведущих обсуждают продукт",
         "~27 секунд, 8 реплик. Тема: честное обсуждение AI-бота для ответов клиентам, без прикрас.")
    + script_block(SCRIPT_2)
    + '<div class="result"><div class="h">Что должно получиться</div><p>Диалог звучит как честный разбор с лёгкой тревогой в начале, не как реклама — есть и сомнение (Б), и конкретная граница применимости (А).</p></div>')

add("06", "Сценарий 3: короткий юмор", "script-3", "Глава 4.3 · Сценарии",
    head("Глава 4.3", "Короткий диалог с юмором",
         "~23 секунды, 8 реплик. Тема: лёгкая самоирония про то, что оба участника — AI-аватары.")
    + script_block(SCRIPT_3)
    + '<div class="result"><div class="h">Что должно получиться</div><p>Короткие подколы без восклицательных знаков и наигранности — юмор держится на том, что оба честно признают: они нарисованы текстом, который ты ещё не прислал.</p></div>')

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
    <h1 style="font-weight:800;font-size:27pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:19ch">Два аватара. Один разговор</h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Как собрать вертикальный ролик с двумя AI-ведущими, которые отвечают друг другу по смыслу, а не читают текст по очереди.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Батч 1 · главы 1-4</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">HeyGen + ElevenLabs</span>
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
    '<span class="kick">Содержание</span><h1 class="title">Батч 1 из N</h1>'
    '<p class="lead">Это главы 1-4: как устроен процесс, инструменты (честно, один пункт требует '
    'проверки на дату чтения), принципы сценария-диалога и три готовых сценария. Дальше — подготовка '
    'аватаров, голоса, генерация реплик, сборка, монтаж через Claude Code/Codex, готовые промпты, '
    'ошибки и практическое задание — следующими батчами. Оглавление кликабельно.</p>'
    f'<div style="margin-top:2px">{"".join(toc_rows)}</div>'))

for label, title, pid, section, html, num in numbered:
    P.append(page(section, num, html, pid=pid))

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))

lines = ["AlovLab · «Два аватара. Один разговор» — сценарии и промпты (батч 1), копипаст-готовые.\n"]
for title, text in PROMPTS_TXT:
    lines.append(f"### {title}\n{text}\n")
(OUTDIR / "prompts.txt").write_text("\n".join(lines), encoding="utf-8")
print("prompts.txt:", len(PROMPTS_TXT), "items")
