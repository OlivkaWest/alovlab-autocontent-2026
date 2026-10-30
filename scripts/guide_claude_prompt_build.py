# -*- coding: utf-8 -*-
"""AlovLab · тетрадь Дня 4 (31.08) «Как спрашивать ИИ, чтобы не было воды» — премиум-PDF (фикс-A4).
Позиция: ИИ не тупой — вопрос слабый. Каркас точного промпта (роль·цель·контекст·формат·ограничения·пример),
5 ошибок с ДО/ПОСЛЕ промптами, мастер-промпт, промпт-доводчик, 5 готовых промптов, чек-лист.
Очень детально по промптам. Честность: без выдуманных цифр. База CSS — v2.
Запуск: python3 scripts/guide_claude_prompt_build.py"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "claude-prompt"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-claude-prompt.html"

EXTRA = r"""
.rec{display:grid;grid-template-columns:24px 1fr;gap:12px;margin:9px 0;align-items:start}
.rec .n{width:24px;height:24px;border-radius:7px;background:linear-gradient(150deg,var(--o2),var(--o));color:#fff;font-weight:800;font-size:11pt;display:flex;align-items:center;justify-content:center;line-height:1}
.rec .t b{font-weight:800;color:var(--ink);font-size:10.5pt}.rec .t p{margin-top:2px;font-size:9.6pt;line-height:1.44;color:var(--body)}
.prompt code{font-size:8.7pt;line-height:1.5}
.bad{background:#faf0ea;border:1px solid #eccdb9;border-left:3px solid #c56b43;border-radius:11px;padding:10px 13px;margin:9px 0}
.bad .l{display:block;font-weight:800;font-size:8pt;letter-spacing:.05em;text-transform:uppercase;color:#c56b43;margin-bottom:5px}
.bad p{font-size:9.6pt;line-height:1.45;color:#7d6a5c;font-style:italic}
.why{font-size:9.5pt;line-height:1.45;color:var(--body);margin:6px 0 2px}.why b{color:var(--ink);font-weight:800}
.frame{margin:8px 0}
.frame .r{display:grid;grid-template-columns:112px 1fr;gap:12px;align-items:baseline;padding:7px 0;border-bottom:1px solid var(--line)}
.frame .r:last-child{border-bottom:0}
.frame .r b{font-weight:800;font-size:8.6pt;letter-spacing:.04em;text-transform:uppercase;color:var(--o)}
.frame .r p{font-size:9.6pt;line-height:1.4;color:var(--ink)}
"""
CSS = V2CSS + EXTRA
VOICE = "[ГОЛОС] живо, без штампов и воды."

def page(section, num, inner):
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main">{inner}</div>'
            f'<div class="pf"><span>AlovLab · как спрашивать ИИ</span><span class="pnum">стр. <b>{num:02d}</b></span></div></section>')
def head(kick,h2,lead=None):
    l=f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'
def rec(n,t,b): return f'<div class="rec"><div class="n">{n}</div><div class="t"><b>{t}</b><p>{b}</p></div></div>'
def prompt(tag,code,ru=None):
    ru_html=f'<div class="ru"><b>Подсказка:</b> {ru}</div>' if ru else ''
    return f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span><span class="copy">скопировать</span></div><code>{code}</code>{ru_html}</div>'
def bad(txt): return f'<div class="bad"><span class="l">✕ Как НЕ надо</span><p>{txt}</p></div>'
def errpage(section,num,idx,name,why,bad_txt,good_code,hint):
    return page(section,num,
        f'<span class="kick">Ошибка {idx}/5</span><h2>{name}</h2>'
        + f'<p class="why"><b>Почему вода:</b> {why}</p>'
        + bad(bad_txt)
        + prompt("Как НАДО · промпт", good_code, hint))

P=[]

# 01 Обложка
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(122% 74% at 82% 12%,#301f10,#180f08 55%,#0b0906)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · тетрадь дня · День 4</div>
    <h1 style="font-weight:800;font-size:31pt;line-height:1.05;letter-spacing:-.02em;color:#fff;max-width:17ch">Как спрашивать ИИ, чтобы <span style="color:var(--o2)">не было воды.</span></h1>
    <p style="margin-top:16px;font-size:12.5pt;line-height:1.5;color:#d8cdbd;max-width:46ch">ИИ не тупой — вопрос слабый. Внутри: каркас точного промпта, 5 частых ошибок с примерами «до/после» и готовые промпты, которые можно копировать и подставлять свою задачу.</p>
    <div style="margin-top:18px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Каркас промпта</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">5 ошибок · до/после</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Готовые промпты</span>
    </div>
  </div>
</section>""")

# 02 Позиция
P.append(page("Позиция",2,
  head("Главное","ИИ не тупой — вопрос слабый",
    "«Нейросеть выдаёт воду» — почти всегда не про модель. ИИ зеркалит: спросил мутно — получил мутно. Спросил точно — получил точно. Значит, всё решает, КАК ты спрашиваешь.")
  + '<div class="callout result"><div class="h">Формула точного вопроса</div><p>Точный промпт = роль + цель + контекст + формат + ограничения (+ пример). Дальше — по этой формуле разложим каждую ошибку.</p></div>'
  + '<p class="note">Хорошая новость: это навык. Разберёшь 5 ошибок — и «вода» кончится на любой модели.</p>'
))

# 03 Каркас
P.append(page("Каркас промпта",3,
  head("Скелет","6 частей точного промпта",
    "Держи этот каркас в голове. Не обязательно все 6 всегда — но чем больше заполнено, тем чище ответ.")
  + '<div class="frame">'
    '<div class="r"><b>Роль</b><p>Кто отвечает: «ты — копирайтер / маркетолог / редактор».</p></div>'
    '<div class="r"><b>Цель</b><p>Что нужно и зачем: «пост, чтобы читатель записался».</p></div>'
    '<div class="r"><b>Контекст</b><p>Факты, аудитория, примеры — то, чего ИИ не знает.</p></div>'
    '<div class="r"><b>Формат</b><p>Вид ответа: список / таблица / пост на N знаков.</p></div>'
    '<div class="r"><b>Ограничения</b><p>Тон, длина, что нельзя: без штампов, без выдуманных цифр.</p></div>'
    '<div class="r"><b>Пример</b><p>Образец «вход → выход», если есть. Резко повышает точность.</p></div>'
    '</div>'
))

# 04-08 · 5 ошибок
P.append(errpage("Ошибка 1 · размытая задача",4,1,"Размытая задача",
  "«Напиши пост» — ИИ не знает про что, для кого и зачем. Выдаёт общее ни о чём.",
  "Напиши пост про наш продукт.",
  "Ты — копирайтер. Напиши пост для Instagram про [продукт]\n"
  "для аудитории [кто]. Цель: чтобы читатель [действие].\n"
  "Формат: ~800 знаков, хук в первой строке, один CTA,\n"
  "живой язык без штампов. Факты: [3-5 фактов о продукте].\n" + VOICE,
  "чем конкретнее «для кого» и «зачем» — тем меньше воды. Общий пост = общий результат."))

P.append(errpage("Ошибка 2 · ноль контекста",5,2,"Ноль контекста",
  "Не дал фактов и аудиторию — ИИ додумывает за тебя и попадает мимо.",
  "Составь контент-план на неделю.",
  "Составь контент-план на неделю для ниши [ниша].\n"
  "Аудитория: [кто]. Опоры: польза, кейсы, приглашение.\n"
  "Форматы: reels + карусель. Темы, которые заходят: [список].\n"
  "Дай таблицу: день - рубрика - формат - черновик хука.\n" + VOICE,
  "контекст — это то, чего ИИ про тебя не знает. Дай факты, а не проси угадать."))

P.append(errpage("Ошибка 3 · пять задач разом",6,3,"Пять задач в один запрос",
  "Свалил всё в кучу — ИИ распыляется, каждый пункт делает поверхностно.",
  "Придумай название, слоган, 10 постов, воронку и лендинг.",
  "Давай по шагам. Сейчас только одно: придумай 5 вариантов\n"
  "названия для [проект]. Аудитория [кто], тон [какой].\n"
  "Когда выберу — перейдём к слогану.\n" + VOICE,
  "одна задача за раз = глубина вместо каши. Следующий шаг запускаешь после выбора."))

P.append(errpage("Ошибка 4 · нет формата",7,4,"Не задал формат",
  "Не сказал, в каком виде нужен ответ — получаешь простыню вместо того, что удобно.",
  "Расскажи про наши тарифы.",
  "Собери сравнение 3 тарифов таблицей: колонки — тариф,\n"
  "что входит, цена, кому подходит. По данным: [данные].\n"
  "Ничего не выдумывай, чего нет в данных.\n" + VOICE,
  "скажи вид ответа (список/таблица/пост N знаков) — и не придётся переспрашивать."))

P.append(errpage("Ошибка 5 · не проверил",8,5,"Взял первый черновик",
  "Первый ответ почти всегда сыроват. Не попросил доработать — опубликовал воду.",
  "(берёшь первый ответ ИИ и сразу в дело)",
  "Проверь свой ответ: где вода и общие слова?\n"
  "Что можно удалить без потери смысла? Перепиши плотнее,\n"
  "оставь только конкретику и покажи, что убрал.\n" + VOICE,
  "второй прогон с этим промптом убирает 80% воды. Всегда проси доработать."))

# 09 Сводка
P.append(page("5 ошибок → 5 фиксов",9,
  head("Сохрани","Быстрая сверка перед запросом")
  + rec(1,"Размытая задача","→ роль + цель + для кого")
  + rec(2,"Ноль контекста","→ факты, аудитория, примеры")
  + rec(3,"Пять задач разом","→ по одной за раз")
  + rec(4,"Нет формата","→ скажи вид ответа")
  + rec(5,"Не проверил","→ попроси доработать и убрать воду")
  + '<p class="note">Пробежался по пяти пунктам перед отправкой — и на выходе не вода, а результат.</p>'
))

# 10 Мастер-промпт
P.append(page("Мастер-промпт",10,
  head("Универсальный каркас","Один промпт под любую задачу",
    "Копируешь, подставляешь своё в квадратные скобки — и получаешь точный ответ почти на что угодно.")
  + prompt("Мастер-промпт · копировать",
    "Роль: ты — [эксперт по …].\n"
    "Задача: [что нужно], чтобы [зачем / какой результат].\n"
    "Контекст: аудитория [кто]; факты — [список]; примеры — [если есть].\n"
    "Формат ответа: [список / таблица / пост N знаков / …].\n"
    "Ограничения: живой язык, без штампов и воды;\n"
    "не выдумывай факты — чего нет, помечай.\n"
    "Сначала уточни, если чего-то не хватает. Потом сделай.\n" + VOICE,
    "строка «сначала уточни» заставляет ИИ задать вопрос вместо догадки — меньше промахов.")
))

# 11 Промпт-доводчик
P.append(page("Промпт-доводчик",11,
  head("Ленивый способ","Пусть ИИ сам улучшит твой промпт",
    "Не хочешь расписывать — отдай свой кривой промпт Claude и попроси довести до ума.")
  + prompt("Промпт · доводчик",
    "Вот мой промпт: [ВСТАВЬ]. Он даёт водянистый, общий результат.\n"
    "Улучши его: добавь роль, цель, недостающий контекст и формат,\n"
    "задай ограничения против воды. Верни готовый промпт\n"
    "и коротко — что ты добавил и почему.\n" + VOICE,
    "так ты ещё и учишься: видишь, чего не хватало. Через неделю пишешь точные промпты сам.")
))

# 12 Библиотека промптов
P.append(page("Библиотека · 5 промптов",12,
  head("Бонус","Готовые промпты под частые задачи",
    "Скопируй нужный, подставь своё. Все — по каркасу из этой тетради.")
  + prompt("Пост",
    "Ты — копирайтер. Пост для [площадка] про [тема] для [кто].\n"
    "Цель: [действие]. ~800 знаков, хук в 1-й строке, 1 CTA,\n"
    "без штампов. Факты: [список].")
  + prompt("Идеи / хуки",
    "Дай 10 хуков (первых строк) для [тема], аудитория [кто].\n"
    "Разные типы: ошибка, миф, результат, вопрос. Без штампов, коротко.")
))

# 13 Библиотека 2
P.append(page("Библиотека · продолжение",13,
  head("Ещё 3","План · разбор · письмо")
  + prompt("Контент-план",
    "Контент-план на неделю для [ниша], аудитория [кто].\n"
    "Опоры: польза x2, смысл, кейс, приглашение. Таблица:\n"
    "день - рубрика - формат - хук.")
  + prompt("Разбор",
    "Разбери [текст/ссылку] по схеме: оффер - аудитория - хуки -\n"
    "форматы - воронка - гэпы. Только по тому, что видно; нет данных — UNKNOWN.")
  + prompt("Письмо",
    "Напиши письмо [кому] с целью [что должен сделать].\n"
    "Тон [какой], до [N] знаков, один понятный шаг в конце. Без воды.")
))

# 14 Чек-лист
P.append(page("Чек-лист промпта",14,
  head("Перед отправкой","Точный вопрос?")
  + '<div class="callout check"><div class="h">Чек-лист запроса</div>'
    '<div class="row">Есть роль (кто отвечает)</div>'
    '<div class="row">Ясна цель и «для кого»</div>'
    '<div class="row">Дан контекст: факты, аудитория, примеры</div>'
    '<div class="row">Указан формат ответа</div>'
    '<div class="row">Заданы ограничения (тон, без штампов, без выдуманных фактов)</div>'
    '<div class="row">Одна задача за раз</div>'
    '<div class="row">После ответа — попросил доработать и убрать воду</div>'
    '</div>'
  + '<p class="note">Честно: ИИ не заменяет твою голову. Он усиливает точный вопрос — и обнуляет мутный.</p>'
))

# 15 CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:25pt;line-height:1.12;margin:18px 0 8px">Спроси точно —<br><span style="color:var(--o2)">получи чисто.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:48ch;margin:0 auto 20px">Каркас, разбор ошибок и готовые промпты — вся тетрадь дня. Как из точных промптов собрать контент-конвейер, учим на курсе AlovLab.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Чек-лист + промпты — в комментариях под постом</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">Курс → alovlab.ru</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Как спрашивать ИИ · тетрадь · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
