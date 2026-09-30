# -*- coding: utf-8 -*-
"""AlovLab · Октябрь 2026 · Методичка G02 «Формат и точность ответа» (дни 4-7 календаря).
4 главы: что нельзя вставлять в чат, почему ответы разные, контроль формата, капстоун-сборка.
Запуск: python3 scripts/guide_oct_g02_build.py
Рендер: NODE_PATH=/opt/node22/lib/node_modules node scripts/guide_pdf_v2_shoot.js <html> <pdf> <pagesDir>"""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "content" / "october-2026-system" / "guides" / "G02-format-i-tochnost"
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
"""
CSS = V2CSS + EXTRA

def page(section, num, inner, mid=False):
    body = f'<div class="midwrap">{inner}</div>' if mid else inner
    return (f'<section class="page"><div class="ph">{BRAND}<span>{section}</span></div>'
            f'<div class="main{" mid" if mid else ""}">{body}</div>'
            f'<div class="pf"><span>AlovLab · Формат и точность ответа</span>'
            f'<span class="pnum">стр. <b>{num:02d}</b></span></div></section>')

def head(kick, h2, lead=None):
    l = f'<p class="lead">{lead}</p>' if lead else ''
    return f'<span class="kick">{kick}</span><h2>{h2}</h2>{l}'

def prompt(tag, code, ru=None):
    r = f'<div class="ru">{ru}</div>' if ru else ''
    return (f'<div class="prompt"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code>{r}</div>')

P = []

P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 78% 8%,rgba(218,95,30,.42),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">Октябрь 2026 · Неделя 1, дни 4–7 · G02</div>
    <h1 style="font-weight:800;font-size:28pt;line-height:1.08;letter-spacing:-.02em;color:#fff;max-width:17ch">Формат и точность ответа</h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:42ch">Что нельзя вставлять в чат. Почему ответы разные. Как задать формат. Как собрать всё в личного помощника.</p>
    <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap">
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">4 главы</span>
      <span style="font-size:9pt;font-weight:700;color:#e8dccb;border:1px solid rgba(255,255,255,.25);border-radius:20px;padding:6px 13px">Капстоун недели 1</span>
    </div>
  </div>
</section>""")

toc = [
 ("Г1","Что нельзя вставлять в чат","03"),("Г2","Почему ответы разные","04"),
 ("Г3","Как управлять форматом ответа","05"),("Г3","Пример формата","06"),
 ("Г4","Капстоун: сборка чат-помощника","07"),("Г4","Шаблон сборки","08"),
 ("—","Частые ошибки","09"),("—","Сделай сейчас + самопроверка","10"),
 ("—","Источники и статус проверки","11"),("—","Дальше — на курсе","12"),
 ("—","Путь в команду AlovLab","13"),("—","Контакты","14"),
]
rows = "".join(f'<div style="display:flex;align-items:baseline;gap:10px;padding:6px 0;border-bottom:1px solid var(--line2)">'
               f'<span style="font-weight:800;color:var(--o);font-size:9.5pt;width:26px">{a}</span>'
               f'<span style="font-weight:600;font-size:10.3pt;color:var(--ink)">{b}</span>'
               f'<span style="flex:1;border-bottom:1px dotted var(--line);margin:0 4px"></span>'
               f'<span style="font-weight:700;color:var(--muted);font-size:9.5pt">{c}</span></div>' for a,b,c in toc)
P.append(page("Содержание", 2,
    '<span class="kick">Содержание</span><h1 class="title">Четыре главы к личному помощнику</h1>'
    '<p class="lead">Дни 4–7 календаря AlovLab на октябрь: продолжение G01, капстоун недели 1.</p>'
    f'<div style="margin-top:4px">{rows}</div>'))

P.append(page("Глава 1 · Приватность", 3,
    head("Глава 1", "Что нельзя вставлять в чат",
         "Для кого: любой, кто работает с чужими данными. Результат: проверенная привычка обезличивания.")
    + '<table class="ref"><tr><th>№</th><th>Категория</th><th>Пример</th></tr>'
      '<tr><td>1</td><td><b>Пароли/доступы</b></td><td>Даже «временный» токен</td></tr>'
      '<tr><td>2</td><td><b>Договоры без обезличивания</b></td><td>ФИО, суммы, реквизиты сторон</td></tr>'
      '<tr><td>3</td><td><b>Финансы клиента</b></td><td>Выписки, доходы, платёжные данные</td></tr>'
      '<tr><td>4</td><td><b>Медданные</b></td><td>Диагнозы, история болезни</td></tr>'
      '<tr><td>5</td><td><b>Чужие личные данные</b></td><td>Телефон/адрес без согласия человека</td></tr></table>'
    + '<p class="note">Вместо этого — обезличивай: «Клиент А» вместо имени, «N рублей» вместо суммы, сохраняй только структуру задачи.</p>'))

P.append(page("Глава 2 · Вариативность", 4,
    head("Глава 2", "Почему ответы разные",
         "Для кого: любой пользователь ChatGPT. Результат: использовать вариативность осознанно.")
    + '<p>Модель не хранит готовый ответ — собирает его заново при каждом запуске, поэтому один и тот же промпт может дать разные, но одинаково валидные ответы.</p>'
    + prompt("ПРОМПТ НА НЕСКОЛЬКО ВАРИАНТОВ · СКОПИРОВАТЬ",
             "[твой обычный рабочий запрос]\nДай три разных варианта ответа, не один. Пронумеруй их.")
    + '<div class="callout result"><div class="h">Что должно получиться</div><p>Для важного текста — выбор из нескольких вариантов, а не единственная попытка.</p></div>'))

P.append(page("Глава 3 · Формат", 5,
    head("Глава 3", "Как управлять форматом ответа",
         "Для кого: тот, кто переделывает ответы руками. Результат: формат задан заранее, не правится потом.")
    + '<div class="gb"><div class="box bad"><div class="lbl">Без формата</div>Сплошной текст — читать можно, использовать нужно после ручной переделки.</div>'
      '<div class="box good"><div class="lbl">С форматом</div>Та же просьба + «оформи как таблицу» — готовый результат сразу.</div></div>'))

P.append(page("Глава 3 · Пример", 6,
    prompt("ШАБЛОН ФОРМАТА · СКОПИРОВАТЬ",
           "[твой вопрос]\nОформи ответ как: [таблица / нумерованный список / шаблон с полями: ...].")
    + '<p class="note">«Покрасивее» — не формат. Формат — это конкретная структура, которую можно назвать одним словом: таблица, список, шаблон.</p>'))

P.append(page("Глава 4 · Капстоун", 7,
    head("Глава 4", "Капстоун: сборка личного чат-помощника",
         "Для кого: тот, кто прошёл главы G01 и G02. Результат: один настроенный чат под свою задачу.")
    + '<div class="flow"><div class="node"><b>Инструкции</b><span>роль+контекст</span></div><div class="arr">→</div>'
      '<div class="node"><b>Ограничения</b><span>+формат</span></div><div class="arr">→</div>'
      '<div class="node"><b>Проверка</b><span>3 шага Г3 (G01)</span></div><div class="arr">→</div>'
      '<div class="node"><b>Помощник</b><span>готов к работе</span></div></div>'
    + '<p>Это не новый инструмент — это настроенный разговор под конкретную повторяющуюся задачу, использующий все пять приёмов недели.</p>'))

P.append(page("Глава 4 · Шаблон", 8,
    prompt("ШАБЛОН СБОРКИ · СКОПИРОВАТЬ",
           "Я [роль], моя задача: [конкретная повторяющаяся задача].\n[Контекст, который нужен для этой задачи].\nОграничения: [что нельзя].\nФормат ответа: [структура].\nЕсли данных не хватает — спрашивай, не додумывай.\nПри необходимости даю три варианта, не один.")
    + '<div class="callout check"><div class="h">Проверка перед использованием</div><p>Помощник настроен под одну твою реальную задачу, не абстрактно «для всего».</p></div>'))

P.append(page("Ошибки", 9,
    head("Ошибки", "Частые ошибки глав 1–4", "")
    + '<div class="fix">'
      '<div class="r"><b>Глава 1.</b> «Обезличу потом» — данные уже отправлены в сервис к моменту, когда вспомнил.</div>'
      '<div class="r"><b>Глава 2.</b> Берёшь первый ответ как единственно верный для важного текста.</div>'
      '<div class="r"><b>Глава 3.</b> Просишь «красивее» вместо конкретного формата — снова переделываешь руками.</div>'
      '<div class="r"><b>Глава 4.</b> Настраиваешь помощника «под всё сразу» — получаешь снова обобщённый инструмент.</div></div>'))

P.append(page("Сделай сейчас", 10,
    head("Действие", "Сделай сейчас", "Собери своего помощника за один присест.")
    + '<div class="steps">'
      '<div class="step"><div class="sx"><b>Проверь последние 10 чатов</b> на пункты из главы 1.</div></div>'
      '<div class="step"><div class="sx"><b>Собери шаблон сборки</b> из главы 4 под одну свою повторяющуюся задачу.</div></div>'
      '<div class="step"><div class="sx"><b>Используй его сегодня же</b> на реальном вопросе.</div></div></div>'
    + '<div class="callout check"><div class="h">Самопроверка</div>'
      '<div class="row">Ни один чат за последний месяц не содержит данных из главы 1.</div>'
      '<div class="row">Помощник настроен под конкретную задачу, не абстрактно.</div>'
      '<div class="row">Формат ответа задаётся заранее, не правится вручную после.</div></div>'))

P.append(page("Источники", 11,
    head("Источники", "Статус проверки", "")
    + '<div class="warn"><div class="h">Статус</div><ul>'
      '<li>Категории данных (глава 1) — общий принцип защиты данных, не привязаны к конкретному продукту.</li>'
      '<li>Объяснение вариативности ответов (глава 2) — общий принцип работы языковых моделей.</li>'
      '<li>Примеры — учебные, не реальные клиентские данные.</li></ul></div>'))

P.append(page("Дальше", 12,
    head("Дальше", "Модуль «Земля Слов» на курсе",
         "Поддержка на курсе: закрытый Telegram-канал + ИИ-ассистент по курсу (все тарифы), личное менторство — тариф ПРО.")
    + '<div class="warn"><div class="h">Честно про цену</div><ul><li>Тарифы на октябрь не переподтверждены вживую — цену здесь не называем, проверь на alovlab.ru.</li></ul></div>'))

P.append(page("Команда", 13,
    head("Путь дальше", "Путь в команду AlovLab",
         "Если настройка чат-помощников — то, что нравится собирать, есть куда расти.")
    + '<div class="team"><div class="h">Собираешь помощников уверенно?</div>'
      '<p>Сильные ученики AlovLab заходят в реальные проекты под задачи брендов.</p>'
      '<div class="dirs"><span>Промпт-системы</span><span>Контент-ассистенты</span><span>Автоматизация</span></div>'
      '<p style="margin-top:8px">Практика, не обещание трудоустройства.</p></div>'))

P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,rgba(218,95,30,.4),rgba(19,16,10,0) 55%),linear-gradient(180deg,#1c160d,#0d0b07)"></div>
  <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22mm">
    <img src="data:image/png;base64,{LOGO}" style="width:64px;height:64px;border-radius:16px;margin-bottom:18px">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.2em;text-transform:uppercase;color:var(--o2);margin-bottom:12px">AlovLab · Октябрь 2026</div>
    <h1 style="font-weight:800;font-size:26pt;line-height:1.1;color:#fff;max-width:22ch">Неделя 1 готова. Дальше — визуал</h1>
    <p style="margin-top:16px;font-size:12pt;line-height:1.6;color:#d8cdbd;max-width:44ch">Методичка G03 (дни 8–9) — кинематографичные изображения промптом.</p>
    <div style="margin-top:22px;display:flex;gap:9px;flex-wrap:wrap;justify-content:center">
      <span style="font-size:10pt;font-weight:700;color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:22px;padding:8px 16px">Telegram · t.me/AlovLab</span>
    </div>
  </div>
</section>""")

html = ("<!doctype html><html lang=ru><head><meta charset=utf-8>"
        f"<style>{CSS}</style></head><body>{''.join(P)}</body></html>")
OUT.write_text(html, encoding="utf-8")
print("HTML:", OUT, "pages:", len(P))
