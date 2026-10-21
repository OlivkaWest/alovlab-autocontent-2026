# -*- coding: utf-8 -*-
"""AlovLab · методичка «Ты придумываешь темы. А их надо подслушивать» (День 3).
Премиум-вёрстка: фикс-A4, светлые страницы, тёмные плашки под промпты. База CSS — из v2."""
import pathlib
from guide_pdf_v2_build import CSS as V2CSS, BRAND, LOGO

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUTDIR = ROOT / "exports" / "guides" / "pain-bank"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "alovlab-guide-pain-bank.html"

EXTRA = r"""
.prompt.rux code{font-family:'Manrope',system-ui,sans-serif;font-size:10pt;line-height:1.6;color:#ffe6cf;white-space:pre-wrap}
.chip{display:flex;gap:10px;align-items:center;background:#1c160d;border:1px solid rgba(255,255,255,.08);border-radius:13px;padding:11px 14px;margin-top:9px}
.chip .av{width:26px;height:26px;border-radius:50%;background:linear-gradient(150deg,#3a3128,#26201a);flex:0 0 auto}
.chip .tx{font-size:11pt;color:#b9ad9b;line-height:1.35}
.chip.on{background:rgba(232,103,42,.14);border-color:rgba(232,103,42,.4)}.chip.on .tx{color:#fff}.chip.on .av{background:linear-gradient(150deg,var(--o2),var(--o))}
.rank{display:flex;gap:9px;margin:12px 0}
.rank .c{flex:1;background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 13px;text-align:center}
.rank .c .k{font-weight:800;font-size:12pt;color:var(--ink)}.rank .c .p{font-size:9pt;color:var(--muted);margin-top:4px;line-height:1.35}
.rank .c .plus{font-weight:800;color:var(--o);font-size:15pt;margin-bottom:4px}
.bankrow{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 13px;margin:7px 0;font-size:9.7pt;line-height:1.4}
.bankrow b{color:var(--ink)}.bankrow .src{color:var(--o);font-weight:700;font-size:8pt;text-transform:uppercase;letter-spacing:.04em}
"""
CSS = V2CSS + EXTRA

def page(section, num, inner):
    header = f'<div class="ph">{BRAND}<span>{section}</span></div>'
    footer = f'<div class="pf"><span>День 3 · банк болей</span><span class="pnum">стр. <b>{num:02d}</b></span></div>'
    return f'<section class="page">{header}<div class="main">{inner}</div>{footer}</section>'

def prompt(tag, code):
    return (f'<div class="prompt rux"><div class="plbl"><span class="tag">{tag}</span>'
            f'<span class="copy">скопировать</span></div><code>{code}</code></div>')

P = []

# P1 · Обложка (тёмная, мотив чипов-реплик)
P.append(f"""<section class="page page--dark" style="padding:0">
  <div style="position:absolute;inset:0;background:radial-gradient(120% 70% at 82% 12%,#2a2013,#160f08 52%,#0c0a07)"></div>
  <div style="position:relative;z-index:2;padding:20mm 22mm 0">
    <span style="display:inline-flex;align-items:center;gap:9px"><img src="data:image/png;base64,{LOGO}" style="width:32px;height:32px;border-radius:9px"><b style="font-weight:800;font-size:16pt;color:#fff">Alov<i style="color:var(--o2);font-style:normal">Lab</i></b></span>
  </div>
  <div style="position:relative;z-index:2;margin-top:auto;padding:0 22mm 22mm">
    <div style="font-weight:800;font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--o2);margin-bottom:14px">AlovLab · практический гайд · День 3</div>
    <h1 style="font-weight:800;font-size:33pt;line-height:1.06;letter-spacing:-.02em;color:#fff;max-width:15ch">Ты придумываешь темы. А их надо <span style="color:var(--o2)">подслушивать.</span></h1>
    <p style="margin-top:16px;font-size:13pt;line-height:1.5;color:#d8cdbd;max-width:40ch">Банк из 10 реальных болей аудитории и 3 самые острые — собранные чужими словами за 15 минут.</p>
    <div style="margin-top:20px">
      <div class="chip"><span class="av"></span><span class="tx">«скидываю 5 кг — за месяц возвращаются с плюсом»</span></div>
      <div class="chip on"><span class="av"></span><span class="tx">на такую фразу нельзя не кликнуть</span></div>
    </div>
  </div>
</section>""")

# P2 · Что ты соберёшь
P.append(page("Результат дня", 2, """
  <span class="kick">Результат дня</span>
  <h2>Что ты соберёшь</h2>
  <p class="lead">Не список «интересных тем», а банк из 10 болей — не придуманных, а собранных чужими словами. Из них — 3 самые острые, на которых строишь контент всю неделю.</p>
  <div class="flow">
    <div class="node"><b>Ниша</b><span>+ аудитория</span></div><div class="arr">→</div>
    <div class="node"><b>4 источника</b><span>где сидит</span></div><div class="arr">→</div>
    <div class="node"><b>10 болей</b><span>с источником</span></div><div class="arr">→</div>
    <div class="node"><b>3 острые</b><span>отобраны</span></div><div class="arr">→</div>
    <div class="node"><b>Темы</b><span>на неделю</span></div>
  </div>
  <div class="term"><b>Боль</b> — <span>дословная фраза, на которой человек останавливает палец, потому что узнаёт свою жизнь.</span></div>
  <div class="term"><b>Тема из головы</b> — <span>то, что важно тебе. Звучит гладко и правильно — и пролистывается.</span></div>
  <div class="callout result"><div class="h">Обещание</div><p>К концу гайда у тебя банк из 10 болей с источниками и 3 отобранные — готовая опора для тем, хуков и сценариев.</p></div>
"""))

# P3 · Почему это работает
P.append(page("Почему это работает", 3, """
  <span class="kick">Механика</span>
  <h2>Почему подслушанное цепляет, а придуманное — нет</h2>
  <p class="lead">Человек останавливается только на том, что болит у него — и его собственными словами.</p>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Тема из головы</div>«Правильное питание — залог здоровья». Лозунг эксперта. Никто не узнаёт себя → листает.</div>
    <div class="box good"><div class="lbl">✓ Подслушанная боль</div>«Скидываю 5 кг — возвращаются с плюсом». Фраза клиента → «это про меня» → смотрит до конца.</div>
  </div>
  <ul>
    <li>Пишешь свою тему → зритель не узнаёт себя → <strong>листает.</strong></li>
    <li>Берёшь его дословную боль → зритель узнаёт свою жизнь → <strong>останавливается.</strong></li>
  </ul>
  <div class="callout result"><div class="h">Вывод</div><p>Хорошая тема не придумывается. Она подслушивается. Реальная боль уже написана — её надо не сочинить, а найти и скопировать как есть.</p></div>
"""))

# P4 · 4 источника
P.append(page("4 источника", 4, """
  <span class="kick">Где искать</span>
  <h2>Боль лежит в четырёх местах</h2>
  <p class="lead">Это не выдумка — это цитаты. Иди туда, где человек жалуется без фильтра.</p>
  <div class="cards c2">
    <div class="card"><div class="ct">01</div><div class="ch">Комментарии</div><p>Под похожими роликами конкурентов. Промотай и копируй жалобы дословно.</p></div>
    <div class="card"><div class="ct">02</div><div class="ch">Отзывы</div><p>На маркетплейсах и картах — там пишут без вежливости, с деталью.</p></div>
    <div class="card"><div class="ct">03</div><div class="ch">Поиск</div><p>Что люди гуглят по теме: «почему вес возвращается».</p></div>
    <div class="card"><div class="ct">04</div><div class="ch">Переписки</div><p>Где тебя уже спрашивали — это готовые формулировки боли.</p></div>
  </div>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Не работает</div>Опрос друзей «что вам интересно» — вежливые ответы. Это эхо, а не боль.</div>
    <div class="box good"><div class="lbl">✓ Работает</div>Анонимный крик души в комментах — без фильтра, с эмоцией и деталью.</div>
  </div>
"""))

# P5 · Пошагово
P.append(page("Пошагово", 5, """
  <span class="kick">Инструкция</span>
  <h2>Как собрать банк за 15 минут</h2>
  <div class="steps">
    <div class="step"><div class="sx"><b>Определи, где сидит аудитория</b> — 3–5 конкретных мест.</div></div>
    <div class="step"><div class="sx"><b>Собери сырые цитаты руками</b> — открой 2–3 ролика конкурентов, копируй жалобы дословно.</div></div>
    <div class="step"><div class="sx"><b>Открой Perplexity</b> и вставь основной промпт (стр. 6), подставив нишу и аудиторию.</div></div>
    <div class="step"><div class="sx"><b>Сведи в один банк</b> — ручные цитаты + находки, убери дубли. Цель — 10 болей с источником.</div></div>
    <div class="step"><div class="sx"><b>Оцени остроту</b> каждой по трём признакам (стр. 8).</div></div>
    <div class="step"><div class="sx"><b>Прогони через промпты улучшения и оценки</b> (стр. 7) — отбракуй выдуманное.</div></div>
    <div class="step"><div class="sx"><b>Выбери 3 самые острые</b> — это результат дня.</div></div>
  </div>
"""))

# P6 · Основной промпт (Perplexity)
P.append(page("Промпт · Perplexity", 6, prompt(
  "Основной промпт · собрать 10 болей с источниками",
  """Ты — исследователь аудитории. Помоги собрать реальные боли, а не придуманные темы.
Ниша: [НИША]. Аудитория: [АУДИТОРИЯ].
Где сидит аудитория: [МЕСТА] (комментарии под похожими роликами, отзывы на маркетплейсах и картах, вопросы в поиске).

Найди 10 реальных болей этой аудитории. Для каждой дай:
1) БОЛЬ — дословной живой фразой, как её говорит сам человек (с эмоцией и деталью, не причёсывай);
2) ИСТОЧНИК — где такое встречается (тип: комменты / отзывы / поиск), по возможности ссылка;
3) ПОЧЕМУ БОЛИТ — одна строка.

Правила: не выдумывай, бери только то, что реально встречается. Никаких общих лозунгов. Разные боли, без дублей по смыслу.""") + """
  <span class="kick" style="margin-top:16px;display:block">Что подставить</span>
  <div class="cards c3">
    <div class="card"><div class="ct">[НИША]</div><p>что ты продаёшь</p></div>
    <div class="card"><div class="ct">[АУДИТОРИЯ]</div><p>портрет из дня 2</p></div>
    <div class="card"><div class="ct">[МЕСТА]</div><p>3–5 источников боли</p></div>
  </div>
  <p class="note">Perplexity ищет по живому вебу и даёт ссылки — так проверяешь, что боль настоящая, а не сгенерирована. Промпт можно гонять и в Claude/ChatGPT с веб-поиском.</p>
"""))

# P7 · Промпты улучшения и оценки
_p7a = prompt("Улучшение · в дословные фразы",
  "Вот мой банк болей: [БАНК БОЛЕЙ].\nПереформулируй каждую так, как сказал бы сам клиент вслух: короче, конкретнее, с эмоцией и деталью. Убери экспертные обороты и лозунги. Покажи было → стало по каждой.")
_p7b = prompt("Жёсткая оценка · отбраковать",
  "Оцени мой банк строго, как редактор, который его отклонит: [БАНК БОЛЕЙ].\nПо каждой реши: реальная или выдумана. Отбрось выдуманные и лозунги. Оставшиеся оцени по остроте: повтор, деньги/время, стыд/страх — по плюсу за каждый. Отсортируй и назови 3 самые острые. Ничего не хвали из вежливости.")
P.append(page("Промпты · доводка", 7,
  '<span class="kick">Доводка</span>'
  '<h2>Переписать в живые фразы и отбраковать выдуманное</h2>' + _p7a + _p7b))

# P8 · Острота + пример банка
P.append(page("Острота", 8, """
  <span class="kick">Отбор</span>
  <h2>Как отличить острую боль от слабой</h2>
  <p class="lead">Рядом с каждой болью ставь плюсы. Три плюса — острая. Ноль-один — слабая, в топ не идёт.</p>
  <div class="rank">
    <div class="c"><div class="plus">+</div><div class="k">Повтор</div><div class="p">встречается у многих</div></div>
    <div class="c"><div class="plus">+</div><div class="k">Деньги / время</div><div class="p">человек уже теряет</div></div>
    <div class="c"><div class="plus">+</div><div class="k">Стыд / страх</div><div class="p">задевает самооценку</div></div>
  </div>
  <span class="kick" style="display:block;margin-top:6px">Фрагмент банка (нутрициолог)</span>
  <div class="bankrow"><span class="src">комменты · +++</span><br>«Скидываю 5 кг, за месяц возвращаются с плюсом. Уже боюсь весов.» — <b>годы усилий впустую + стыд</b></div>
  <div class="bankrow"><span class="src">отзыв · ++</span><br>«Перепробовала всё: кето, ПП, голодание. Вес стоит.» — <b>деньги и время на ветер</b></div>
  <div class="bankrow"><span class="src">поиск · ++</span><br>«Ем мало, а вес не уходит. Что со мной не так?» — <b>страх «поломанного» обмена</b></div>
"""))

# P9 · Готовый пример
P.append(page("Пример", 9, """
  <span class="kick">Готовый пример</span>
  <h2>Одна фраза — готовый заход</h2>
  <div class="gb">
    <div class="box bad"><div class="lbl">✕ Слабо (из головы)</div>«Правильное питание — залог здоровья и хорошего самочувствия.» Лозунг эксперта. Никто не узнаёт себя.</div>
    <div class="box good"><div class="lbl">✓ Сильно (подслушано)</div>«Скидываю 5 кг, а через месяц возвращаются с плюсом. Уже боюсь вставать на весы.»</div>
  </div>
  <div class="callout result"><div class="h">Почему второй сильнее</div><p>Это фраза самого клиента, а не эксперта. Повтор + деньги/время + стыд — три признака остроты из трёх. Из неё сразу готовы тема, хук и сценарий ролика.</p></div>
  <p class="note">Нутрициолог не сочинила эту фразу — нашла дословно в комментариях под чужим роликом про диеты. Копируй как есть: с эмоцией, деталью и даже ошибками.</p>
"""))

# P10 · Чек-лист + задание
P.append(page("Чек-лист · задание", 10, """
  <span class="kick">Контроль</span>
  <h2>Проверь перед тем, как взять в работу</h2>
  <div class="callout check"><div class="h">Чек-лист банка</div>
    <div class="row">Боль сформулирована чужими словами, а не как лозунг</div>
    <div class="row">У каждой боли есть источник (ссылка или «комменты под роликом»)</div>
    <div class="row">Боль реальная, а не выдумана из головы</div>
    <div class="row">В топ-3 — боли с наибольшей остротой (повтор + деньги + стыд)</div>
    <div class="row">Все боли под одну аудиторию, без чужих</div>
  </div>
  <div class="callout result"><div class="h">Задание дня</div><p>Собери банк из 10 болей чужими словами, каждую с источником. Отбери 3 самые острые. Их держи под рукой — завтра из одной боли сделаем пять разных заходов.</p></div>
"""))

# P11 · CTA
P.append(f"""<section class="page page--dark" style="justify-content:center;text-align:center">
  <img src="data:image/png;base64,{LOGO}" style="width:52px;height:52px;border-radius:13px;margin:0 auto">
  <h2 style="color:#fff;font-size:27pt;line-height:1.1;margin:18px 0 8px">Забери шаблон банка<br>и промпт для <span style="color:var(--o2)">Perplexity.</span></h2>
  <p style="color:#b9ad9b;font-size:11pt;line-height:1.5;max-width:44ch;margin:0 auto 20px">В тетради дня — 4 источника болей, как отличить сильную от слабой и готовые промпты, чтобы собрать 10 болей с источниками за 15 минут.</p>
  <div style="display:flex;gap:9px;justify-content:center;flex-wrap:wrap">
    <span style="font-weight:800;font-size:11pt;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));padding:11px 18px;border-radius:10px">Тетрадь дня 3 · t.me/AlovLab</span>
    <span style="font-weight:800;font-size:11pt;color:var(--o2);border:1px solid rgba(232,103,42,.5);padding:11px 18px;border-radius:10px">VK · vk.com/alovlab</span>
  </div>
</section>""")

HTML = f'<meta charset="utf-8"><title>Гайд · Ты придумываешь темы. А их надо подслушивать · AlovLab</title><style>{CSS}</style>' + "\n".join(P)
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| pages:", len(P))
