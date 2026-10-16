# -*- coding: utf-8 -*-
"""AlovLab · «Монтаж с AI-агентом» — методичка к рилсу klod-montazh, по ALOVLAB-ACADEMY-STANDARD.

Тема: как настроить репозиторий, чтобы Claude Code (и, во второй половине, Codex CLI) мог сам
резать клипы, синхронить голос, добавлять титры и экспортировать готовый файл по команде —
какие скиллы подключать, какой репозиторий, какая роль/контекст у агента, какие права доступа
реально защищают исходники, а какие только советуют.

БАТЧ 1 (эта версия файла): главы 1-4 — "Что мы создаём", "Что нужно подготовить", "Репозиторий
под монтаж" (структура папок + CLAUDE.md), "Skill «video-editor»" (полная схема ГДЕ-ЧТО-ЧТО).
Главы 5+ (права доступа и hooks, subagent, Codex CLI, сравнение, финальный проект, бонусы) —
следующие батчи.

Честность по источникам: все факты о Claude Code — из официальной документации
code.claude.com/docs (прочитана напрямую исследовательским агентом в этой сессии, даты страниц —
16.10.2026). Факты о Codex CLI — частично прямое чтение github.com/openai/codex, частично
WebSearch по developers.openai.com (прямой доступ к этому домену заблокирован сетью среды) —
помечено явно как вторичное подтверждение. Там, где источники расходятся (например, точное
название модели по умолчанию в Codex, или статус approval_policy=untrusted между англо- и
португалоязычной версией одной и той же официальной страницы) — показано честно, не выбрано
молча. Версии инструментов меняются быстро — методичка явно просит сверять командой --version
перед тем как полагаться на деталь как на факт.

Та же система A4-страниц + автонумерация, что в guide_g07_academy_build.py.
Запуск: python3 scripts/guide_klod_montazh_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>
"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "guides" / "klod-montazh"
OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "workbook.html"

def timeline_svg(w=600, h=90, color="#ff7a33", opacity=0.55):
    import random
    random.seed(7)
    blocks = []
    x = 0.0
    gap = 7
    track_y = h * 0.42
    track_h = h * 0.3
    while x < w - 10:
        bw = random.uniform(34, 92)
        if x + bw > w:
            bw = w - x
        blocks.append(f'<rect x="{x:.1f}" y="{track_y:.1f}" width="{max(bw-3,4):.1f}" height="{track_h:.1f}" '
                       f'rx="5" fill="{color}" opacity="{opacity}"/>')
        x += bw + gap
    line = f'<rect x="0" y="{h*0.78:.1f}" width="{w}" height="2" fill="{color}" opacity="0.25"/>'
    return (f'<svg viewBox="0 0 {w} {h}" style="width:100%;height:{h}px;display:block" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(blocks)}{line}</svg>')

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
.chain b{font-size:9.6pt;font-weight:800;color:var(--ink);background:var(--o-tint);border-radius:9px;padding:6px 9px}
.chain .a{color:var(--o);font-weight:800;font-size:12pt}
.warn{background:var(--o-tint);border:1px solid #f2d3bf;border-radius:12px;padding:14px 16px;margin:10px 0}
.warn .h{font-weight:800;font-size:9pt;letter-spacing:.06em;text-transform:uppercase;color:var(--o);margin-bottom:6px}
.warn p{font-size:10.5pt;color:var(--ink);line-height:1.5;margin:0;max-width:none}
.warn ul{margin:4px 0 0}
.warn li{font-size:10.3pt;color:var(--ink);line-height:1.48;max-width:none}
.herostat{display:flex;gap:11px;margin:12px 0}
.herostat .tile{flex:1;background:#13100A;border-radius:14px;padding:16px 14px;text-align:center}
.herostat .tile .num{font-weight:800;font-size:17pt;color:#F2A65A;display:block}
.herostat .tile .lbl{font-size:8pt;font-weight:700;letter-spacing:.03em;text-transform:uppercase;color:#cdbfa8;margin-top:4px;display:block}
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
.tree{background:#13100A;border-radius:14px;padding:16px 18px;margin:10px 0;color:#f2eadf}
.tree code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:8.8pt;line-height:1.56;color:#ffd9b8;white-space:pre}
"""
CSS = V2CSS + EXTRA
TOPIC = "МОНТАЖ С AI-АГЕНТОМ · Claude Code и Codex"

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
# ГЛАВА 1. ЧТО МЫ СОЗДАЁМ
# ======================================================================
add("01", "Что мы создаём", "result", "Глава 1 · Результат",
    head("Глава 1", "Что мы создаём",
         "К концу этого учебника у тебя будет репозиторий, в котором AI-агент сам режет клипы, "
         "синхронит голос, добавляет титры и собирает готовый файл по твоей команде.")
    + '<p>Раньше монтаж ролика — это ты сидишь в программе-редакторе и вручную тянешь дорожки, режешь по кадрам, подставляешь титры. Здесь другой подход: ты даёшь задачу текстом («вырежи с 10 по 25 секунду, подставь голос, добавь титры снизу»), а всю черновую механику выполняет AI-агент через обычные консольные инструменты (в первую очередь ffmpeg). Ты проверяешь результат и правишь то, что реально не так.</p>'
    + '<div class="chain">'
      '<b>твоя команда текстом</b><span class="a">→</span><b>агент (Claude Code / Codex)</b><span class="a">→</span><b>ffmpeg режет/собирает</b><span class="a">→</span><b>готовый файл</b>'
      '</div>'
    + '<h3 style="margin-top:14px">Два инструмента в этом учебнике</h3>'
    + '<div class="io">'
      '<div class="c"><b>Claude Code</b><p>Терминальный агент от Anthropic. Основной инструмент этого учебника — умеет читать репозиторий, запускать команды (в том числе ffmpeg), помнить правила проекта через файл CLAUDE.md, подключать Skills (готовые наборы инструкций под задачу).</p></div>'
      '<div class="c out"><b>Codex CLI</b><p>Терминальный агент от OpenAI. Разбираем во второй половине учебника как альтернативу/сравнение — похожая идея (свой файл памяти, свои режимы доступа к системе), но другие названия и детали. Пригодится, если уже пользуешься им или хочешь сравнить.</p></div></div>'
    + '<p class="note">Дальше — два уровня работы с этим учебником и то, чего автоматизация монтажа НЕ заменяет.</p>')

add("02", "Два уровня", "levels", "Глава 1 · Результат",
    head("Глава 1", "Два уровня в этом учебнике", "")
    + '<div class="io">'
      '<div class="c"><b>Уровень 1 — новичок</b><p>Просто общаешься с агентом в чате: «вырежи этот кусок», «добавь титр здесь». Агент сам решает, какие команды выполнить. Минимальная настройка репозитория.</p></div>'
      '<div class="c out"><b>Уровень 2 — продвинутый</b><p>Готовый Skill с набором проверенных операций, настроенные права доступа, чтобы агент не спрашивал разрешения на каждый чих, и выбор — подложить отдельного subagent под монтаж. Для тех, кто делает это каждую неделю.</p></div></div>'
    + '<div class="warn"><div class="h">Чего это НЕ заменяет</div><p>Это не нейросеть, которая «снимает» видео с нуля — это автоматизация механической работы над уже готовым материалом. Что вырезать и в каком порядке — решаешь ты, агент выполняет.</p></div>'
    + '<p class="note">Агент не «знает» твой проект сам по себе — правила описываешь один раз в файле CLAUDE.md, и дальше он читает их в каждой сессии. Как именно — глава 3.</p>')

# ======================================================================
# ГЛАВА 2. ЧТО НУЖНО ПОДГОТОВИТЬ
# ======================================================================
add("03", "Что нужно подготовить", "prep", "Глава 2 · Подготовка",
    head("Глава 2", "Что нужно подготовить",
         "Прежде чем настраивать репозиторий, собери всё по списку ниже.")
    + '<div class="checklist">'
      '<div class="row">Компьютер (Mac, Linux, или Windows через WSL2 — для Codex CLI это обязательное условие, Claude Code работает и без WSL).</div>'
      '<div class="row">Установленный Claude Code (claude.ai/code) или Codex CLI (или оба — сравнение в главе 9).</div>'
      '<div class="row">Установленный ffmpeg — бесплатный консольный инструмент для резки/сборки видео, без него ни один из агентов монтировать не сможет.</div>'
      '<div class="row">Папка проекта с исходными материалами: отснятые клипы, голосовая дорожка, текст титров.</div>'
      '<div class="row">git — не обязателен для самого монтажа, но полезен, чтобы не потерять настройку репозитория (см. главу 3).</div></div>'
    + '<div class="warn"><div class="h">Проверь версии перед тем как доверять деталям из этой методички</div><p>Оба инструмента быстро меняются. Перед работой выполни <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">claude --version</code> или <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">codex --version</code> и сверь с официальной документацией — часть механизмов в этой методичке привязана к конкретным версиям, это явно отмечено в тексте.</p></div>'
    + '<h3 style="margin-top:14px">Проверка ffmpeg</h3>'
    + '<div class="steps">'
      '<div class="step"><div class="sx">Открой терминал и выполни <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">ffmpeg -version</code>.</div></div>'
      '<div class="step"><div class="sx">Если команда не найдена — установи через менеджер пакетов своей системы (на Mac через Homebrew, на Linux — через apt/dnf, на Windows — через WSL2 или сборку с официального сайта ffmpeg).</div></div>'
      '<div class="step"><div class="sx">Проверь, что агент тоже видит ffmpeg: в чате Claude Code или Codex попроси «выполни ffmpeg -version» — если команда выполнится и покажет версию, всё готово к главе 3.</div></div></div>')

# ======================================================================
# ГЛАВА 3. РЕПОЗИТОРИЙ ПОД МОНТАЖ (ключевая глава)
# ======================================================================
add("04", "Структура папок", "repo-structure", "Глава 3.1 · Репозиторий",
    head("Глава 3.1", "Структура папок",
         "Прежде чем агент тронет хоть один файл, реши, где что лежит. Это не формальность — именно эта структура защищает исходники в главе 5.")
    + '<div class="tree"><code>reels-edit/                    ← корень репозитория\n'
      'CLAUDE.md                     ← правила проекта (глава 3.2)\n'
      '.gitignore                    ← исключает тяжёлые папки из git\n'
      '.claude/\n'
      '  settings.json                ← права доступа, общие для команды (глава 5)\n'
      '  settings.local.json          ← личные права, не в git (глава 5)\n'
      '  skills/\n'
      '    video-editor/\n'
      '      SKILL.md                 ← сам skill (глава 4)\n'
      '      reference.md             ← шпаргалка по командам ffmpeg\n'
      '      scripts/                 ← готовые обёртки над ffmpeg\n'
      'footage/                       ← исходные клипы, НИКОГДА не правятся\n'
      'voiceover/                     ← аудиодорожки озвучки\n'
      'scenes/                        ← текстовые планы монтажа (что откуда куда)\n'
      'work/                          ← промежуточные файлы, можно удалять\n'
      'exports/                       ← готовые файлы на выдачу</code></div>'
    + '<div class="io">'
      '<div class="c"><b>footage/</b><p>Сырые материалы. По правилу проекта — только читаются, никогда не перезаписываются. Это защищает тебя от ситуации «агент случайно затёр оригинал».</p></div>'
      '<div class="c out"><b>exports/</b><p>Только готовые файлы на выдачу, с понятными именами (дата + название ролика), не <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">final2.mp4</code>.</p></div></div>'
    + '<p class="note">Эта структура — не единственно верная, но рабочая отправная точка. Дальше в этой главе — что писать в CLAUDE.md, чтобы агент эту структуру соблюдал.</p>')

add("05", "CLAUDE.md: что туда писать", "claude-md", "Глава 3.2 · Репозиторий",
    head("Глава 3.2", "CLAUDE.md: что туда писать",
         "CLAUDE.md — файл в корне репозитория, который Claude Code читает автоматически в начале каждой сессии. Это и есть «контекст и роль» агента для этого проекта.")
    + prompt("CLAUDE.MD (ПРИМЕР ДЛЯ ЭТОГО ПРОЕКТА)",
             "# Монтаж Reels\n\n"
             "Роль: ты монтажёр-ассистент. Выполняешь задачи по монтажу текущего ролика, не\n"
             "придумываешь креатив сам — решения о порядке кадров и смысле принимает человек.\n\n"
             "Структура: footage/ — исходники, НИКОГДА не перезаписывай и не удаляй файлы в этой\n"
             "папке. voiceover/ — аудиодорожки. scenes/ — текстовые планы монтажа. work/ —\n"
             "промежуточные файлы, можно перезаписывать свободно. exports/ — готовые файлы,\n"
             "называй их <дата>_<название>.mp4.\n\n"
             "Инструменты: используй ffmpeg через Bash для всех операций с видео. Перед сборкой\n"
             "финального файла прогоняй ffprobe и сообщай длительность и разрешение результата.")
    + '<div class="warn"><div class="h">Важно: CLAUDE.md — это контекст, не охрана</div><p>По официальной документации Claude Code, CLAUDE.md передаётся агенту как обычное сообщение — агент старается следовать написанному, но это не жёсткое ограничение на уровне системы. Фраза «никогда не перезаписывай footage/» в CLAUDE.md — это сильная подсказка, а не гарантия. Настоящая защита — права доступа и hooks из главы 5. Не путай «попросил вежливо» с «запретил технически».</p></div>')
register_prompt("CLAUDE.md для проекта монтажа Reels", "см. полный текст в главе 3.2 методички")

add("06", "CLAUDE.md: три практических момента", "claude-md-2", "Глава 3.3 · Репозиторий",
    head("Глава 3.3", "CLAUDE.md: три практических момента", "")
    + '<div class="fix">'
      '<div class="r"><b>Размер.</b> Официальная рекомендация — держать файл компактным (ориентир до ~200 строк), с разделами по заголовкам. Длинный файл агент читает хуже, не лучше.</div>'
      '<div class="r"><b>Личные заметки.</b> Если хочешь что-то только для себя, а не для всей команды — используй отдельный <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">CLAUDE.local.md</code> и добавь его в <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">.gitignore</code> — общий CLAUDE.md в git видит вся команда.</div>'
      '<div class="r"><b>Проверка.</b> Команда <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">/context</code> внутри Claude Code показывает, какие файлы памяти реально загружены в этой сессии — полезно, если кажется, что агент «не слушается» написанного.</div>'
      '<div class="r"><b>Импорты.</b> Если хочешь вынести шпаргалку по ffmpeg в отдельный файл, подключи её строкой <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">@scenes/ffmpeg-cheatsheet.md</code> прямо в CLAUDE.md — Claude Code подхватит её при чтении.</div></div>'
    + '<p class="note">Дальше — сам skill «video-editor»: готовая инструкция, которую Claude Code подключает сам, когда видит подходящий запрос.</p>')

# ======================================================================
# ГЛАВА 4. SKILL «VIDEO-EDITOR»
# ======================================================================
add("07", "Skill «video-editor»: собираем", "skill-editor-1", "Глава 4.1 · Skill",
    head("Глава 4.1", "Skill «video-editor»: собираем",
         "Skill — это папка с готовой инструкцией под конкретную задачу, которую Claude Code подключает сам, когда видит подходящий запрос. Разбираем по схеме: где находится → что срабатывает → что внутри → что вводим.")
    + '<div class="fix">'
      '<div class="r"><b>ГДЕ НАХОДИТСЯ.</b> Файл <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">.claude/skills/video-editor/SKILL.md</code> в корне репозитория (личный skill, доступный только тебе на этой машине, живёт в <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">~/.claude/skills/</code> — но для проекта с командой правильнее держать его в репозитории).</div>'
      '<div class="r"><b>ЧТО СРАБАТЫВАЕТ.</b> Поле <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">description</code> в самом верху SKILL.md. Claude Code сравнивает твой запрос с этим описанием и сам решает, подключать ли skill — или ты вызываешь его вручную командой <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">/video-editor</code>.</div>'
      '<div class="r"><b>ЧТО ВНУТРИ.</b> YAML-заголовок (между строк <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">---</code>) с полями name/description/allowed-tools, а дальше обычный текст-инструкция для агента. Рядом может лежать папка <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">scripts/</code> с готовыми обёртками команд.</div>'
      '<div class="r"><b>ЧТО ВВОДИМ.</b> Описание задачи простыми словами + список разрешённых команд (allowed-tools) + текст-инструкция, что куда писать и чего не трогать. Пример — в следующей главе.</div></div>'
    + '<p class="note">Дальше — полный пример такого SKILL.md целиком, готовый к копированию.</p>')
register_prompt("SKILL.md для видео-монтажа (video-editor)",
                 "---\nname: video-editor\ndescription: Монтирует вертикальное короткое видео через "
                 "ffmpeg. Используй, когда просят вырезать клип по таймкодам, склеить несколько "
                 "клипов, добавить титры/подпись, подставить дорожку озвучки или собрать финальный "
                 "файл 9:16.\nallowed-tools:\n  - Bash(ffmpeg *)\n  - Bash(ffprobe *)\n---\n\n"
                 "Исходники в footage/ — никогда не изменяй и не перезаписывай.\nПромежуточные файлы "
                 "пиши в work/, финальные — в exports/.\nПеред сборкой финального файла прогони "
                 "ffprobe и сообщи длительность и разрешение.")

add("08", "Skill «video-editor»: готовый пример", "skill-editor-example", "Глава 4.2 · Skill",
    head("Глава 4.2", "Skill «video-editor»: готовый пример", "")
    + prompt("SKILL.MD (.claude/skills/video-editor/SKILL.md)",
             "---\n"
             "name: video-editor\n"
             "description: Монтирует вертикальное короткое видео через ffmpeg. Используй, когда\n"
             "  просят вырезать клип по таймкодам, склеить несколько клипов, добавить\n"
             "  титры/подпись, подставить дорожку озвучки или собрать финальный файл 9:16.\n"
             "allowed-tools:\n"
             "  - Bash(ffmpeg *)\n"
             "  - Bash(ffprobe *)\n"
             "---\n\n"
             "Исходники в footage/ — никогда не изменяй и не перезаписывай.\n"
             "Промежуточные файлы пиши в work/, финальные — в exports/.\n"
             "Перед сборкой финального файла прогони ffprobe и сообщи длительность и разрешение.")
    + '<p class="note">allowed-tools здесь — это подсказка самому Claude Code, какими командами пользоваться в рамках skill; жёсткие правила доступа (чтобы не спрашивать разрешения на каждый запуск ffmpeg) настраиваются отдельно в settings.json — это глава 5.</p>')

add("09", "Skill «video-editor»: добавляем скрипты", "skill-editor-2", "Глава 4.3 · Skill",
    head("Глава 4.3", "Skill «video-editor»: добавляем скрипты",
         "Вместо того чтобы агент каждый раз сам придумывал ffmpeg-команду с нуля, можно положить рядом готовые проверенные скрипты — это снижает риск ошибки в сложном синтаксисе фильтров.")
    + '<div class="io">'
      '<div class="c"><b>trim.sh</b><p>Вырезает кусок клипа по таймкодам начала и конца — одна из самых частых операций.</p></div>'
      '<div class="c out"><b>concat.sh</b><p>Склеивает несколько клипов подряд в один файл.</p></div>'
      '<div class="c"><b>overlay_text.sh</b><p>Накладывает текстовую подпись/титр поверх видео в заданной позиции и с заданным временем появления.</p></div>'
      '<div class="c out"><b>mux_voice.sh</b><p>Подставляет отдельную аудиодорожку озвучки поверх видео, синхронизируя по длительности.</p></div></div>'
    + '<div class="fix"><div class="r"><b>Как агент их находит.</b> В тексте SKILL.md скрипты называются через переменную <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">${CLAUDE_SKILL_DIR}</code> — она разворачивается в путь до папки самого skill, так что ссылка остаётся верной независимо от того, где именно лежит репозиторий на твоём компьютере.</div></div>'
    + prompt("SKILL.MD — ССЫЛКА НА СКРИПТ",
             "Для вырезания фрагмента запускай:\n"
             "${CLAUDE_SKILL_DIR}/scripts/trim.sh <входной_файл> <начало> <конец> <выходной_файл>\n\n"
             "Пример: ${CLAUDE_SKILL_DIR}/scripts/trim.sh footage/clip-01.mp4 00:00:10 00:00:25 "
             "work/clip-01-trim.mp4")
    + '<div class="warn"><div class="h">Честно про эту методичку</div><p>Сами файлы <code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">trim.sh</code>/<code style="font-family:ui-monospace,monospace;background:#f1e9db;padding:1px 5px;border-radius:4px;color:#8a5a2a">concat.sh</code> и остальные — не вложены как готовые бинарные файлы в этот PDF. Содержимое каждого — это одна строка вызова ffmpeg с понятными параметрами (обрезка по времени, склейка через список файлов, наложение текста фильтром drawtext, замена звуковой дорожки). Собрать их самостоятельно по документации ffmpeg — следующий бонусный блок методички (глава 13, бонусы), либо попроси агента написать их за тебя по этому же описанию задачи.</p></div>')

# ============================================================
# Сборка
# ============================================================
P = []
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 0">{timeline_svg()}</div>
  <div style="position:relative;z-index:2;padding:10px 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab Academy · методичка к рилсу «Монтаж теперь делает Клод»</div>
    <h1 style="font-weight:800;font-size:27pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:19ch">Монтаж с AI-агентом</h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Claude Code и Codex: какой репозиторий, какие скиллы, какая роль и контекст у агента, чтобы он сам монтировал твои ролики.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Батч 1 · главы 1-4</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Claude Code + Codex CLI</span>
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
    '<p class="lead">Это главы 1-4 из планируемых ~13: что создаём, что подготовить, репозиторий '
    'под монтаж, первый skill. Дальше — права доступа и hooks (реальная защита исходников), '
    'отдельный subagent, Codex CLI с нуля, сравнение инструментов, финальный проект, бонусы — '
    'следующими батчами. Оглавление кликабельно.</p>'
    f'<div style="margin-top:2px">{"".join(toc_rows)}</div>'))

for label, title, pid, section, html, num in numbered:
    P.append(page(section, num, html, pid=pid))

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))

lines = ["AlovLab · «Монтаж с AI-агентом» — промпты/конфиги (батч 1), копипаст-готовые.\n"]
for title, text in PROMPTS_TXT:
    lines.append(f"### {title}\n{text}\n")
(OUTDIR / "prompts.txt").write_text("\n".join(lines), encoding="utf-8")
print("prompts.txt:", len(PROMPTS_TXT), "items")
