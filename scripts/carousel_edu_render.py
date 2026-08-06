# -*- coding: utf-8 -*-
"""AlovLab · образовательная карусель (дни 30-day плана) в премиум-визуале.
8 слайдов, 4:5. Тёмный фон, оранжевый акцент, настоящий логотип. Сквозной мотив — чипы-реплики.
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
.h--xl{font-size:38px}.h--lg{font-size:31px}.h--md{font-size:26px}
.a{color:var(--o2)}
.sub{font-size:14px;line-height:1.55;color:var(--muted);margin-top:14px;max-width:34ch}
.mid{display:flex;flex-direction:column}
.viz{margin-top:22px}

/* чипы-реплики */
.chips{display:flex;flex-direction:column;gap:11px}
.chip{display:flex;gap:11px;align-items:flex-start;background:#18130c;border:1px solid var(--line);border-radius:14px;padding:12px 14px}
.chip .av{width:30px;height:30px;border-radius:50%;background:linear-gradient(150deg,#3a3128,#26201a);flex:0 0 auto}
.chip .tx{font-size:12.5px;line-height:1.4;color:var(--muted)}
.chip.on{background:rgba(232,103,42,.12);border-color:rgba(232,103,42,.4)}
.chip.on .tx{color:#fff}.chip.on .av{background:linear-gradient(150deg,var(--o2),var(--o))}
.chip.ghost{opacity:.5}
.chip .tx b{color:var(--o2)}

/* карточки источников */
.src{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}
.src .s{background:#18130c;border:1px solid var(--line);border-radius:14px;padding:15px 16px}
.src .s .n{font-weight:800;font-size:11px;color:var(--o2);letter-spacing:.04em}
.src .s .t{font-weight:800;font-size:15px;color:#fff;margin:7px 0 3px}
.src .s .d{font-size:11px;color:var(--muted);line-height:1.35}

/* критерии */
.crit{display:flex;gap:10px;margin-top:18px;flex-wrap:wrap}
.crit .c{flex:1;min-width:0;background:#18130c;border:1px solid var(--line);border-radius:13px;padding:14px 12px;text-align:center}
.crit .c .k{font-weight:800;font-size:15px;color:#fff}.crit .c .v{font-size:10.5px;color:var(--muted);margin-top:3px;line-height:1.3}
.badge{display:inline-flex;align-items:center;gap:8px;margin-top:16px;font-weight:800;font-size:13px;color:var(--o2);
background:rgba(232,103,42,.12);border:1px solid rgba(232,103,42,.3);border-radius:999px;padding:8px 15px}

/* большая реплика-пример */
.quote{background:#18130c;border:1px solid rgba(232,103,42,.35);border-radius:18px;padding:20px 22px;margin-top:18px}
.quote .q{font-weight:800;font-size:20px;line-height:1.3;color:#fff}
.quote .meta{display:flex;align-items:center;gap:9px;margin-top:14px}
.quote .meta .av{width:26px;height:26px;border-radius:50%;background:linear-gradient(150deg,var(--o2),var(--o))}
.quote .meta .m{font-size:11px;color:var(--muted)}

/* CTA */
.cta-mid{flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px}
.cta-logo{width:52px;height:52px}
.cta-h{font-weight:800;font-size:30px;line-height:1.08;color:#fff;letter-spacing:-.02em}
.cta-list{display:flex;flex-direction:column;gap:9px;margin-top:2px}
.cta-list .li{display:flex;gap:10px;align-items:center;font-size:13px;color:var(--muted)}
.cta-list .li i{width:6px;height:6px;border-radius:50%;background:var(--o2);flex:0 0 auto}
.cta-list .li b{color:var(--text);font-weight:700}
.cta-btn{align-self:flex-start;font-weight:800;font-size:15px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o));
border-radius:12px;padding:13px 20px;box-shadow:0 12px 26px -12px rgba(232,103,42,.75)}

.notes{margin-top:28px;padding-top:18px;border-top:1px solid var(--line);font-size:12.5px;color:var(--dim);line-height:1.7}.notes b{color:var(--muted)}
"""

def chip(t, cls=""):
    return f'<div class="chip {cls}"><span class="av"></span><span class="tx">{t}</span></div>'

def render(cfg):
    S = []
    # 1 · cover
    S.append(f"""<article class="slide">
      {MARK}{snum(1)}
      <div class="mid">
        <div class="eyebrow">AlovLab · как найти тему</div>
        <h2 class="h h--xl">Ты придумываешь темы.<br>А их надо <span class="a">подслушивать.</span></h2>
      </div>
      <div class="viz chips">
        {chip('«опять вес встал, не понимаю за что плачу тренеру»')}
        {chip('«скидываю 5 кг — возвращаются с плюсом»','on')}
        {chip('«начинаю с понедельника уже полгода»','ghost')}
      </div>
    </article>""")
    # 2 · проблема
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(2)}
      <div class="mid">
        <div class="eyebrow"><b>Проблема</b></div>
        <h2 class="h h--lg">Ты выжимаешь тему<br><span class="a">из себя.</span></h2>
        <p class="sub">Смотришь в потолок, придумываешь «о чём бы снять». Выходит гладко, правильно — и мимо. Люди листают, потому что это твоя тема, а не их боль.</p>
      </div>
      <div class="viz chips">
        {chip('твоя тема: «важность удержания веса»','ghost')}
        {chip('реакция зрителя: 🖐 листает дальше','ghost')}
      </div>
    </article>""")
    # 3 · причина
    S.append(f"""<article class="slide">
      {MARK}{snum(3)}
      <div class="mid">
        <div class="eyebrow"><b>Причина</b></div>
        <h2 class="h h--lg">Тему из головы<br>зритель не узнаёт<br>как <span class="a">свою.</span></h2>
        <p class="sub">Ты пишешь про то, что важно тебе. А человек останавливается только на том, что болит у него — его словами, а не твоими.</p>
      </div>
      <div class="viz chips">
        {chip('«важность удержания веса» — твоими словами')}
        {chip('«скидываю 5 кг — возвращаются с плюсом» — его словами','on')}
      </div>
    </article>""")
    # 4 · ошибка
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(4)}
      <div class="mid">
        <div class="eyebrow"><b>Ошибка</b></div>
        <h2 class="h h--lg">Опрос друзей —<br>это не исследование.<br>Это <span class="a">эхо.</span></h2>
        <p class="sub">Спрашиваешь знакомых «что вам интересно» — и слышишь вежливые ответы. Реальная боль лежит там, где человек жалуется анонимно и без фильтра.</p>
      </div>
      <div class="viz chips">
        {chip('друг: «ну снимай про мотивацию, наверное»','ghost')}
        {chip('друг: «интересно про питание, да»','ghost')}
      </div>
    </article>""")
    # 5 · решение
    S.append(f"""<article class="slide">
      {MARK}{snum(5)}
      <div class="mid">
        <div class="eyebrow"><b>Решение</b></div>
        <h2 class="h h--md">Боль лежит в <span class="a">четырёх местах.</span><br>Иди и собери.</h2>
        <div class="src">
          <div class="s"><div class="n">01</div><div class="t">Комментарии</div><div class="d">под похожими роликами конкурентов</div></div>
          <div class="s"><div class="n">02</div><div class="t">Отзывы</div><div class="d">на маркетплейсах и картах</div></div>
          <div class="s"><div class="n">03</div><div class="t">Поиск</div><div class="d">что люди гуглят по теме</div></div>
          <div class="s"><div class="n">04</div><div class="t">Переписки</div><div class="d">где тебя уже спрашивали</div></div>
        </div>
      </div>
      <p class="sub">Это не выдумка — это цитаты. Их не надо сочинять, надо найти.</p>
    </article>""")
    # 6 · пример
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(6)}
      <div class="mid">
        <div class="eyebrow"><b>Готовый пример</b></div>
        <h2 class="h h--md">Дословная боль —<br>на неё нельзя <span class="a">не кликнуть.</span></h2>
        <div class="quote">
          <div class="q">«Скидываю 5 кг — за месяц возвращаются с плюсом»</div>
          <div class="meta"><span class="av"></span><span class="m">комментарий · ролик про диеты · найдено, не придумано</span></div>
        </div>
      </div>
      <p class="sub">Нутрициолог не сочинила эту фразу. Она скопировала её как есть — с эмоцией и деталью.</p>
    </article>""")
    # 7 · шаг
    S.append(f"""<article class="slide">
      {MARK}{snum(7)}
      <div class="mid">
        <div class="eyebrow"><b>Практический шаг</b></div>
        <h2 class="h h--md">Собери <span class="a">10 болей</span> чужими словами. Выбери <span class="a">3 самые острые.</span></h2>
        <p class="sub">Не переформулируй в «правильное». Копируй как есть. Острая боль — та, где сходятся три признака:</p>
        <div class="crit">
          <div class="c"><div class="k">Повтор</div><div class="v">встречается у многих</div></div>
          <div class="c"><div class="k">Деньги / время</div><div class="v">человек уже теряет</div></div>
          <div class="c"><div class="k">Стыд / страх</div><div class="v">задевает самооценку</div></div>
        </div>
      </div>
      <span class="badge">10 болей → 3 острые → темы на неделю</span>
    </article>""")
    # 8 · CTA
    S.append(f"""<article class="slide slide--cta">
      {MARK}{snum(8)}
      <div class="cta-mid">
        <img class="cta-logo" src="data:image/png;base64,{LOGO}" alt="AlovLab">
        <h2 class="cta-h">Забери банк болей<br>и промпт для <span class="a">Perplexity.</span></h2>
        <div class="cta-list">
          <div class="li"><i></i><b>4 источника болей</b> — где искать</div>
          <div class="li"><i></i>как отличить сильную боль от слабой</div>
          <div class="li"><i></i>готовый промпт: <b>10 болей с источниками за 15 минут</b></div>
        </div>
        <span class="cta-btn">Тетрадь дня 3 → t.me/AlovLab</span>
      </div>
    </article>""")

    css = CSS
    slides = "\n".join(S)
    return f"""<title>Карусель · {cfg['title']} · AlovLab</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{css}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 3 · 6 августа</span>
    <h1>Публиковать <b>ОДНИМ постом</b>: 8 слайдов, порядок 1→8. Выход — Telegram за тетрадью дня.</h1></div>
  <div class="grid">
{slides}
  </div>
  <div class="notes"><b>Тема:</b> {cfg['title']} · B2C, ведёт на курс через Telegram-хаб. <b>Честность:</b> пример-цитата — иллюстрация приёма, не реальный клиент; выдуманных цифр/цены нет.</div>
</div>
"""

CONFIGS = {
  "day-03": {"title": "Боль, которую нельзя пролистнуть"},
}

if __name__ == "__main__":
    bid = sys.argv[1] if len(sys.argv) > 1 else "day-03"
    cfg = CONFIGS[bid]
    outdir = ROOT / "exports" / "carousels" / bid
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / f"{bid}.html"
    out.write_text(render(cfg), encoding="utf-8")
    print("HTML:", out)
