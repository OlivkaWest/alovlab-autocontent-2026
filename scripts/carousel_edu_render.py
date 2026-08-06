# -*- coding: utf-8 -*-
"""AlovLab · образовательная карусель (дни 30-day плана) в премиум-визуале.
8 слайдов, 4:5. Тёмный фон, оранжевый акцент, настоящий логотип. Мотив — «подслушанные» реплики.
Каждый слайд: главная мысль + визуальное доказательство + пример снизу + вывод. Без пустых блоков.
Публикуется одним постом. Выход воронки — Telegram за тетрадью дня.
Запуск: python3 scripts/carousel_edu_render.py day-03
"""
import base64, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
LOGO = b64(ROOT / "assets" / "img" / "logo-mark.png")

RANGES = {"cyrillic":"U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
          "latin":"U+0000-00FF,U+2013-2014,U+2018-201E,U+2018,U+2019,U+201C,U+201D,U+00AB,U+00BB,U+2026,U+2192"}
faces=""
for w in (400,500,700,800):
    for sub in ("cyrillic","latin"):
        fp=FONTS/f'manrope-{sub}-{w}.woff2'
        if fp.exists():
            faces+=("@font-face{font-family:'Manrope';font-weight:%d;font-display:swap;"
                    "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s;}\n"
                    % (w, b64(fp), RANGES[sub]))

MARK = f'<span class="mark"><img class="mki" src="data:image/png;base64,{LOGO}" alt=""><span class="mw">Alov<b>Lab</b></span></span>'
def snum(n,total=8): return f'<span class="snum">0{n}<b> / 0{total}</b></span>'

CSS = faces + r"""
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#0c0a07;--o:#e8672a;--o2:#ff7a33;--text:#f7f2e9;--muted:#a99e8c;--dim:#7a6f5e;--line:rgba(247,242,233,.10);--card:#17120b;}
html{background:#0d0b08}
body{font-family:'Manrope',system-ui,sans-serif;background:#0d0b08;color:var(--text);-webkit-font-smoothing:antialiased;
padding:clamp(18px,3.5vw,44px) clamp(12px,3vw,30px)}
.page{max-width:1000px;margin:0 auto}
.lead{margin-bottom:24px}.lead .eb{font-weight:800;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--o2)}
.lead h1{font-weight:800;font-size:clamp(19px,3.2vw,26px);letter-spacing:-.015em;margin:9px 0 0;line-height:1.3}.lead h1 b{color:var(--o2)}
.grid{display:flex;flex-wrap:wrap;gap:22px;justify-content:center}

.slide{position:relative;width:min(540px,92vw);aspect-ratio:4/5;border-radius:22px;overflow:hidden;
background:radial-gradient(120% 82% at 82% 10%,#2a2013 0%,#161009 46%,var(--ink) 100%);
border:1px solid var(--line);padding:30px 28px;display:flex;flex-direction:column;box-shadow:0 22px 46px -26px rgba(0,0,0,.85)}
.slide--plain{background:radial-gradient(120% 80% at 20% 100%,#221a10,#130e08 55%,var(--ink))}
.slide--cta{background:radial-gradient(120% 82% at 50% 16%,#301f10,#150f08 52%,var(--ink))}

.mark{display:inline-flex;align-items:center;gap:8px;position:relative;z-index:3}
.mark .mki{width:26px;height:26px;border-radius:7px;flex:0 0 auto;display:block}
.mark .mw{font-weight:800;font-size:14px;color:#fff}.mark .mw b{color:var(--o2)}
.snum{position:absolute;top:30px;right:28px;font-weight:800;font-size:12px;color:var(--dim);z-index:3;font-variant-numeric:tabular-nums}.snum b{color:var(--o2)}
.eyebrow{font-weight:800;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-top:16px}.eyebrow b{color:var(--o2)}
.h{font-weight:800;letter-spacing:-.028em;color:#fff;line-height:1.06;margin-top:11px}
.h--xl{font-size:37px}.h--lg{font-size:30px}.h--md{font-size:25px}
.a{color:var(--o2)}
.sub{font-size:14px;line-height:1.55;color:var(--muted);margin-top:13px;max-width:36ch}
.mid{display:flex;flex-direction:column}
.viz{margin-top:20px}
.vcap{font-size:12px;color:var(--dim);margin-top:13px;font-style:italic}

/* чипы-реплики с источником */
.chips{display:flex;flex-direction:column;gap:11px}
.chip{display:flex;gap:11px;align-items:center;background:#18130c;border:1px solid var(--line);border-radius:14px;padding:13px 15px}
.chip .av{width:28px;height:28px;border-radius:50%;background:linear-gradient(150deg,#3a3128,#26201a);flex:0 0 auto}
.chip .tx{font-size:13px;line-height:1.35;color:var(--muted)}
.chip .tag{margin-left:auto;font-weight:800;font-size:9px;letter-spacing:.05em;text-transform:uppercase;color:var(--dim);
background:rgba(255,255,255,.05);border-radius:20px;padding:5px 10px;white-space:nowrap;flex:0 0 auto}
.chip.on{background:rgba(232,103,42,.13);border-color:rgba(232,103,42,.42)}
.chip.on .tx{color:#fff}.chip.on .av{background:linear-gradient(150deg,var(--o2),var(--o))}.chip.on .tag{color:var(--o2);background:rgba(232,103,42,.18)}

/* мини-поток */
.mflow{display:flex;align-items:stretch;gap:0;margin:4px 0}
.mflow .n{flex:1;background:#18130c;border:1px solid var(--line);border-radius:13px;padding:14px 8px;text-align:center;display:flex;flex-direction:column;justify-content:center;gap:4px}
.mflow .n b{font-weight:800;font-size:12.5px;color:#fff;line-height:1.15}.mflow .n span{font-size:9px;color:var(--muted)}
.mflow .ar{display:flex;align-items:center;color:var(--o);font-weight:800;font-size:16px;padding:0 7px}

/* два блока */
.two{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-top:12px}
.two .b{background:#18130c;border:1px solid var(--line);border-radius:14px;padding:14px 15px}
.two .b .l{font-weight:800;font-size:9.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--dim);margin-bottom:7px}
.two .b .t{font-size:14px;color:#fff;font-weight:700;line-height:1.32}
.two .b.dim .t{color:var(--muted)}

/* до / после */
.dvs{display:grid;gap:11px;margin-top:6px}
.dvs .b{border-radius:15px;padding:16px 18px}
.dvs .bad{background:#191a1c;border:1px solid rgba(255,255,255,.07)}
.dvs .good{background:rgba(232,103,42,.12);border:1px solid rgba(232,103,42,.42)}
.dvs .l{font-weight:800;font-size:10px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px}
.dvs .bad .l{color:var(--dim)}.dvs .good .l{color:var(--o2)}
.dvs .t{font-size:17px;line-height:1.32;font-weight:700}
.dvs .bad .t{color:var(--muted)}.dvs .good .t{color:#fff}

/* вывод-плашка */
.concl{display:inline-flex;align-items:center;gap:9px;margin-top:14px;font-weight:800;font-size:13.5px;color:var(--o2);
background:rgba(232,103,42,.12);border:1px solid rgba(232,103,42,.32);border-radius:999px;padding:10px 17px}

/* карточки источников */
.src{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}
.src .s{background:#18130c;border:1px solid var(--line);border-radius:14px;padding:14px 15px}
.src .s .n{font-weight:800;font-size:11px;color:var(--o2);letter-spacing:.04em}
.src .s .t{font-weight:800;font-size:15px;color:#fff;margin:6px 0 3px}
.src .s .d{font-size:10.5px;color:var(--muted);line-height:1.3}
.src .s .find{font-size:10px;color:var(--muted);margin-top:8px;padding-top:8px;border-top:1px solid var(--line);line-height:1.3}
.src .s .find b{color:var(--o2);font-weight:800;text-transform:uppercase;letter-spacing:.04em;font-size:8.5px}

/* цитата-пример */
.quote{background:#18130c;border:1px solid rgba(232,103,42,.35);border-radius:18px;padding:19px 21px;margin-top:6px}
.quote .q{font-weight:800;font-size:20px;line-height:1.3;color:#fff}
.quote .meta{display:flex;align-items:center;gap:9px;margin-top:13px}
.quote .meta .av{width:24px;height:24px;border-radius:50%;background:linear-gradient(150deg,var(--o2),var(--o))}
.quote .meta .m{font-size:11px;color:var(--muted)}
.markers{display:flex;gap:9px;margin-top:13px;flex-wrap:wrap}
.markers .m{font-weight:800;font-size:11.5px;color:var(--o2);background:rgba(232,103,42,.12);border:1px solid rgba(232,103,42,.3);border-radius:20px;padding:8px 14px}
.markers .m span{color:var(--muted);font-weight:600}

/* критерии остроты */
.crit{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:6px}
.crit .c{background:#18130c;border:1px solid var(--line);border-radius:13px;padding:14px 12px;text-align:center}
.crit .c .k{font-weight:800;font-size:14.5px;color:#fff}.crit .c .v{font-size:10.5px;color:var(--muted);margin-top:3px;line-height:1.3}
.crit .c .sign{font-size:9.5px;color:var(--dim);margin-top:9px;padding-top:9px;border-top:1px solid var(--line);line-height:1.32}
.crit .c .sign b{color:var(--o2);font-weight:700}
.badge{display:inline-flex;align-items:center;gap:8px;margin-top:14px;font-weight:800;font-size:14px;color:var(--o2);
background:rgba(232,103,42,.12);border:1px solid rgba(232,103,42,.3);border-radius:999px;padding:10px 17px}
.mcheck{margin-top:13px;display:grid;gap:8px}
.mcheck .r{display:flex;align-items:center;gap:10px;font-size:12.5px;color:var(--muted)}
.mcheck .r::before{content:"";width:14px;height:14px;border-radius:4px;border:1.5px solid var(--o);background:rgba(232,103,42,.12);flex:0 0 auto}

/* CTA */
.cta-mid{flex:1;display:flex;flex-direction:column;justify-content:center;gap:15px}
.cta-logo{width:52px;height:52px}
.cta-h{font-weight:800;font-size:29px;line-height:1.08;color:#fff;letter-spacing:-.02em}
.cta-list{display:flex;flex-direction:column;gap:10px;margin-top:2px}
.cta-list .li{display:flex;gap:11px;align-items:flex-start;font-size:13px;color:var(--muted);line-height:1.3}
.cta-list .li i{width:7px;height:7px;border-radius:50%;background:var(--o2);flex:0 0 auto;margin-top:5px}
.cta-list .li b{color:var(--text);font-weight:700}
.cta-btn{align-self:flex-start;font-weight:800;font-size:16px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));
border-radius:13px;padding:15px 24px;box-shadow:0 14px 30px -12px rgba(232,103,42,.8)}

.notes{margin-top:28px;padding-top:18px;border-top:1px solid var(--line);font-size:12.5px;color:var(--dim);line-height:1.7}.notes b{color:var(--muted)}
"""

def chip(t, tag, on=False):
    return f'<div class="chip{" on" if on else ""}"><span class="av"></span><span class="tx">{t}</span><span class="tag">{tag}</span></div>'

def render(cfg):
    S = []
    # 1 · cover — живые боли с источниками
    S.append(f"""<article class="slide">
      {MARK}{snum(1)}
      <div class="mid">
        <div class="eyebrow">AlovLab · как найти тему</div>
        <h2 class="h h--xl">Ты придумываешь темы.<br>А их надо <span class="a">подслушивать.</span></h2>
      </div>
      <div class="viz chips">
        {chip('«опять вес встал, не понимаю за что плачу тренеру»','коммент')}
        {chip('«скидываю 5 кг — возвращаются с плюсом»','отзыв',on=True)}
        {chip('«начинаю с понедельника уже полгода»','переписка')}
        <div class="vcap">↑ дословно, как говорит аудитория. Одна из них — готовая тема.</div>
      </div>
    </article>""")

    # 2 · проблема — микро-схема + два блока
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(2)}
      <div class="mid">
        <div class="eyebrow"><b>Проблема</b></div>
        <h2 class="h h--lg">Ты выжимаешь тему<br><span class="a">из себя.</span></h2>
        <p class="sub">Гладко, правильно — и мимо. Люди листают, потому что это твоя тема, а не их боль.</p>
      </div>
      <div class="viz">
        <div class="mflow">
          <div class="n"><b>Твоя голова</b><span>«о чём бы снять»</span></div><div class="ar">→</div>
          <div class="n"><b>Гладкая тема</b><span>правильно и скучно</span></div><div class="ar">→</div>
          <div class="n"><b>Листают</b><span>нет реакции</span></div>
        </div>
        <div class="two">
          <div class="b dim"><div class="l">Твоя тема</div><div class="t">«важность удержания веса»</div></div>
          <div class="b dim"><div class="l">Реакция зрителя</div><div class="t">🖐 листает дальше</div></div>
        </div>
      </div>
    </article>""")

    # 3 · причина — до/после
    S.append(f"""<article class="slide">
      {MARK}{snum(3)}
      <div class="mid">
        <div class="eyebrow"><b>Причина</b></div>
        <h2 class="h h--lg">Зритель не узнаёт<br>чужую тему как <span class="a">свою.</span></h2>
        <p class="sub">Он останавливается только на том, что болит у него — его словами, а не твоими.</p>
      </div>
      <div class="viz dvs">
        <div class="b bad"><div class="l">Твоими словами</div><div class="t">«важность удержания веса»</div></div>
        <div class="b good"><div class="l">Его словами</div><div class="t">«скидываю 5 кг — за месяц возвращаются с плюсом»</div></div>
      </div>
    </article>""")

    # 4 · ошибка — вежливые ответы друзей + вывод
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(4)}
      <div class="mid">
        <div class="eyebrow"><b>Ошибка</b></div>
        <h2 class="h h--lg">Опрос друзей — это<br>не исследование. Это <span class="a">эхо.</span></h2>
        <p class="sub">Знакомые отвечают вежливо и сглаженно. Реальная боль — там, где жалуются анонимно и без фильтра.</p>
      </div>
      <div class="viz chips">
        {chip('«ну снимай про мотивацию, наверное»','друг')}
        {chip('«интересно про питание, да»','друг')}
        {chip('«можно что-то для новичков»','друг')}
        <div style="margin-top:4px"><span class="concl">Вежливый ответ ≠ реальная боль</span></div>
      </div>
    </article>""")

    # 5 · решение — 4 источника с «что искать»
    S.append(f"""<article class="slide">
      {MARK}{snum(5)}
      <div class="mid">
        <div class="eyebrow"><b>Решение</b></div>
        <h2 class="h h--md">Боль лежит в <span class="a">четырёх местах.</span></h2>
        <div class="src">
          <div class="s"><div class="n">01</div><div class="t">Комментарии</div><div class="d">под роликами конкурентов</div><div class="find"><b>искать:</b> жалобы, возражения, повторы</div></div>
          <div class="s"><div class="n">02</div><div class="t">Отзывы</div><div class="d">на маркетплейсах и картах</div><div class="find"><b>искать:</b> недовольство, ожидания, сравнения</div></div>
          <div class="s"><div class="n">03</div><div class="t">Поиск</div><div class="d">что люди гуглят по теме</div><div class="find"><b>искать:</b> «как», «почему», «не могу»</div></div>
          <div class="s"><div class="n">04</div><div class="t">Переписки</div><div class="d">где тебя уже спрашивали</div><div class="find"><b>искать:</b> дословные вопросы, признания</div></div>
        </div>
      </div>
      <div class="vcap">Это не выдумка — это цитаты. Их не надо сочинять, надо найти.</div>
    </article>""")

    # 6 · пример — кейсовый разбор
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(6)}
      <div class="mid">
        <div class="eyebrow"><b>Готовый пример</b></div>
        <h2 class="h h--md">Дословная боль —<br>на неё нельзя <span class="a">не кликнуть.</span></h2>
        <div class="quote">
          <div class="q">«Скидываю 5 кг — за месяц возвращаются с плюсом. Уже боюсь весов.»</div>
          <div class="meta"><span class="av"></span><span class="m">комментарий · ролик про диеты · найдено, не придумано</span></div>
        </div>
        <div class="markers">
          <div class="m">Эмоция <span>· «боюсь»</span></div>
          <div class="m">Конкретика <span>· «5 кг за месяц»</span></div>
          <div class="m">Узнаваемость <span>· «это про меня»</span></div>
        </div>
      </div>
      <div class="vcap">Хорошая тема не звучит как эксперт. Она звучит как человек, у которого болит.</div>
    </article>""")

    # 7 · шаг — критерии + алгоритм + чек
    S.append(f"""<article class="slide">
      {MARK}{snum(7)}
      <div class="mid">
        <div class="eyebrow"><b>Практический шаг</b></div>
        <h2 class="h h--md">Собери <span class="a">10 болей.</span> Выбери <span class="a">3 острые.</span></h2>
        <div class="crit">
          <div class="c"><div class="k">Повтор</div><div class="v">встречается у многих</div><div class="sign"><b>признак:</b> всплывает снова и снова</div></div>
          <div class="c"><div class="k">Деньги / время</div><div class="v">человек уже теряет</div><div class="sign"><b>признак:</b> жалоба про затраты</div></div>
          <div class="c"><div class="k">Стыд / страх</div><div class="v">задевает самооценку</div><div class="sign"><b>признак:</b> неловко признаться</div></div>
        </div>
        <span class="badge">Собрал 10 → выбрал 3 → темы на неделю</span>
        <div class="mcheck">
          <div class="r">фраза живая, не «по-умному»</div>
          <div class="r">боль конкретная, с деталью</div>
          <div class="r">формулировка не переписана</div>
        </div>
      </div>
    </article>""")

    # 8 · CTA — ценность + крупная кнопка
    S.append(f"""<article class="slide slide--cta">
      {MARK}{snum(8)}
      <div class="cta-mid">
        <img class="cta-logo" src="data:image/png;base64,{LOGO}" alt="AlovLab">
        <h2 class="cta-h">Забери банк болей<br>и промпт для <span class="a">Perplexity.</span></h2>
        <div class="cta-list">
          <div class="li"><i></i><b>4 источника болей</b> — где именно искать</div>
          <div class="li"><i></i>как отличить сильную боль от слабой</div>
          <div class="li"><i></i>готовый промпт: <b>10 болей с источниками за 15 минут</b></div>
          <div class="li"><i></i>мини-шаблон контент-плана на неделю</div>
        </div>
        <span class="cta-btn">Тетрадь дня 3 → t.me/AlovLab</span>
      </div>
    </article>""")

    slides = "\n".join(S)
    return f"""<title>Карусель · {cfg['title']} · AlovLab</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 3 · 6 августа</span>
    <h1>Публиковать <b>ОДНИМ постом</b>: 8 слайдов, порядок 1→8. Выход — Telegram за тетрадью дня.</h1></div>
  <div class="grid">
{slides}
  </div>
  <div class="notes"><b>Тема:</b> {cfg['title']} · B2C, ведёт на курс через Telegram-хаб. <b>Честность:</b> пример-цитата — иллюстрация приёма, не реальный клиент; выдуманных цифр/цены нет.</div>
</div>
"""

CONFIGS = {"day-03": {"title": "Боль, которую нельзя пролистнуть"}}

if __name__ == "__main__":
    bid = sys.argv[1] if len(sys.argv) > 1 else "day-03"
    cfg = CONFIGS[bid]
    outdir = ROOT / "exports" / "carousels" / bid; outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / f"{bid}.html"; out.write_text(render(cfg), encoding="utf-8")
    print("HTML:", out)
