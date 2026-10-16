# -*- coding: utf-8 -*-
"""AlovLab · День 4 · карусель «Угол, а не тема». Одна тема → пять заходов → сильнейший.
Прикладная, на примерах из ниши AlovLab (ИИ/контент). Переиспользует систему carousel_edu.
Запуск: python3 scripts/carousel_day4_render.py
"""
import pathlib
from carousel_edu_render import CSS as CSS0, MARK, snum, chip, _art, LOGO, ROOT

OUTDIR = ROOT / "exports" / "carousels" / "day-04"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-04.html"

EXTRA = r"""
.arow{display:flex;gap:12px;align-items:center;background:#18130c;border:1px solid var(--line);border-radius:12px;padding:12px 15px;margin-top:9px}
.arow .atag{font-weight:800;font-size:9px;letter-spacing:.05em;text-transform:uppercase;color:var(--o2);background:rgba(232,103,42,.14);
border-radius:7px;padding:7px 9px;white-space:nowrap;flex:0 0 auto;min-width:104px;text-align:center}
.arow .atx{font-size:13.5px;color:#fff;line-height:1.28}
.arow.mark{border-color:rgba(232,103,42,.55);background:rgba(232,103,42,.1)}
.arow.mark .flag{margin-left:auto;font-weight:800;font-size:8.5px;letter-spacing:.05em;text-transform:uppercase;color:#160e07;
background:var(--o2);border-radius:20px;padding:6px 10px;flex:0 0 auto}
"""
CSS = CSS0 + EXTRA

ART = {
 1: _art('<rect x="14" y="30" width="30" height="42" rx="6" opacity=".38"/><rect x="52" y="26" width="32" height="50" rx="6" fill="rgba(255,122,51,.12)"/><path d="M60 40h18M60 50h12" opacity=".75"/>'),
 2: _art('<g opacity=".4"><rect x="16" y="20" width="20" height="15" rx="3"/><rect x="42" y="20" width="20" height="15" rx="3"/><rect x="68" y="20" width="20" height="15" rx="3"/><rect x="16" y="43" width="20" height="15" rx="3"/><rect x="42" y="43" width="20" height="15" rx="3"/><rect x="68" y="43" width="20" height="15" rx="3"/><rect x="16" y="66" width="20" height="15" rx="3"/><rect x="42" y="66" width="20" height="15" rx="3"/><rect x="68" y="66" width="20" height="15" rx="3"/></g>'),
 3: _art('<circle cx="50" cy="50" r="12"/><g opacity=".8"><path d="M50 38V18"/><path d="M61 44 78 33"/><path d="M61 56 78 67"/><path d="M39 56 22 67"/><path d="M39 44 22 33"/></g>'),
 4: _art('<path d="M50 80V54"/><path d="M50 54C50 42 30 42 25 26"/><path d="M50 54C50 42 70 42 75 26"/><path d="M19 22l6 4-3 6M81 22l-6 4 3 6" opacity=".85"/>'),
 5: _art('<circle cx="50" cy="80" r="4" fill="currentColor" stroke="none"/><g opacity=".85"><path d="M50 78 28 36"/><path d="M50 78 40 30"/><path d="M50 78 54 28"/><path d="M50 78 64 32"/><path d="M50 78 74 40"/></g>'),
 6: _art('<path d="M50 18l7.5 20.5 21.5 1-16.5 14 5 21.5L50 66l-17.5 9 5-21.5-16.5-14 21.5-1z"/>'),
 7: _art('<g><rect x="20" y="24" width="13" height="13" rx="3"/><rect x="20" y="45" width="13" height="13" rx="3"/><rect x="20" y="66" width="13" height="13" rx="3"/></g><path d="M42 30h38M42 51h38M42 72h28" opacity=".7"/><path d="M22 66l4 6 8-10" stroke-width="3.6"/>'),
 8: _art('<rect x="26" y="22" width="46" height="58" rx="8"/><path d="M36 40h26M36 52h26M36 64h16" opacity=".7"/><path d="M71 19l2.6 7.4 7.4 2.6-7.4 2.6-2.6 7.4-2.6-7.4-7.4-2.6 7.4-2.6z" fill="rgba(255,122,51,.22)"/>'),
}

def arow(tag, tx, mark=False):
    flag = '<span class="flag">рабочий</span>' if mark else ''
    return f'<div class="arow{" mark" if mark else ""}"><span class="atag">{tag}</span><span class="atx">{tx}</span>{flag}</div>'

def render():
    S = []
    # 1 · cover
    S.append(f"""<article class="slide">
      {MARK}{snum(1)}{ART[1]}
      <div class="mid">
        <div class="eyebrow">AlovLab · как найти угол</div>
        <h2 class="h h--xl">У тебя и у конкурента —<br>одна тема. Смотрят <span class="a">его.</span></h2>
      </div>
      <div class="viz two">
        <div class="b dim"><div class="l">Твой пост</div><div class="t">тема в лоб</div></div>
        <div class="b"><div class="l">Его пост</div><div class="t" style="color:var(--o2)">та же тема — с другого угла</div></div>
      </div>
    </article>""")

    # 2 · проблема
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(2)}{ART[2]}
      <div class="mid">
        <div class="eyebrow"><b>Проблема</b></div>
        <h2 class="h h--lg">Берёшь тему в лоб —<br>и растворяешься <span class="a">среди таких же.</span></h2>
        <p class="sub">Зритель видел это сто раз и листает не глядя.</p>
      </div>
      <div class="viz chips">
        {chip('«5 нейросетей, которые…»','как у всех')}
        {chip('«Тренды ИИ 2026»','как у всех')}
        {chip('«Как сделать аватар»','как у всех')}
      </div>
    </article>""")

    # 3 · причина
    S.append(f"""<article class="slide">
      {MARK}{snum(3)}{ART[3]}
      <div class="mid">
        <div class="eyebrow"><b>Причина</b></div>
        <h2 class="h h--lg">Тема — не твоя.<br>Она общая. Твоё — <span class="a">угол.</span></h2>
        <p class="sub">Одну тему разбирают тысячи — она ничья. Отличает тебя не тема, а с какой стороны ты в неё входишь.</p>
      </div>
      <div class="viz dvs">
        <div class="b bad"><div class="l">Тема</div><div class="t">одна на всех — «контент с ИИ»</div></div>
        <div class="b good"><div class="l">Угол</div><div class="t">твой заход — с какой стороны заходишь</div></div>
      </div>
    </article>""")

    # 4 · ошибка
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(4)}{ART[4]}
      <div class="mid">
        <div class="eyebrow"><b>Ошибка</b></div>
        <h2 class="h h--lg">Ты ищешь новую тему.<br>А надо — новый <span class="a">заход к старой.</span></h2>
        <p class="sub">Кажется, что не заходит из-за темы. Но сильные берут ту же — и разворачивают иначе.</p>
      </div>
      <div class="viz dvs">
        <div class="b bad"><div class="l">Как обычно</div><div class="t">придумываешь другую тему каждый раз</div></div>
        <div class="b good"><div class="l">Как надо</div><div class="t">тем мало — углов много. Разверни одну</div></div>
      </div>
    </article>""")

    # 5 · решение — 5 типов углов
    S.append(f"""<article class="slide">
      {MARK}{snum(5)}{ART[5]}
      <div class="mid">
        <div class="eyebrow"><b>Решение</b></div>
        <h2 class="h h--md">Одна тема → <span class="a">пять углов.</span></h2>
        {arow('Ошибка','где человек сам себе мешает')}
        {arow('Миф','во что верят — и зря')}
        {arow('Цена','сколько уже потрачено впустую')}
        {arow('Взгляд изнутри','что не говорят вслух')}
        {arow('Вопрос новичка','с чего вообще начать')}
      </div>
    </article>""")

    # 6 · пример
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(6)}{ART[6]}
      <div class="mid">
        <div class="eyebrow"><b>Готовый пример</b></div>
        <h2 class="h h--md">Тема «Reels без съёмок» → <span class="a">5 заходов.</span></h2>
        {arow('Ошибка','«Ты снимаешь сам — хотя ИИ уже умеет»')}
        {arow('Миф','«Дорогой ролик — не про камеру»',mark=True)}
        {arow('Цена','«Смена и команда — за вечер на ноутбуке»')}
        {arow('Изнутри','«Что вырезают из красивых туториалов»')}
        {arow('Вопрос','«С чего начать, если открыл впервые»')}
      </div>
      <div class="vcap">Сильнейший — слом убеждения (миф). Его и берёшь в работу.</div>
    </article>""")

    # 7 · практика
    S.append(f"""<article class="slide">
      {MARK}{snum(7)}{ART[7]}
      <div class="mid">
        <div class="eyebrow"><b>Практический шаг</b></div>
        <h2 class="h h--md">Возьми свою тему. Дай ей <span class="a">5 заходов.</span> Отметь <span class="a">один.</span></h2>
        <p class="sub">Не меняй тему. Задай пять углов и выбери тот, где сильнее «стоп, это про меня».</p>
        <span class="badge">1 тема → 5 углов → 1 рабочий</span>
        <div class="mcheck">
          <div class="r">ошибка · миф · цена</div>
          <div class="r">взгляд изнутри · вопрос новичка</div>
          <div class="r">отметил сильнейший — один</div>
        </div>
      </div>
    </article>""")

    # 8 · CTA
    S.append(f"""<article class="slide slide--cta">
      {MARK}{snum(8)}{ART[8]}
      <div class="cta-mid">
        <img class="cta-logo" src="data:image/png;base64,{LOGO}" alt="AlovLab">
        <h2 class="cta-h">Собери свои <span class="a">5 углов</span> по шаблону.</h2>
        <div class="cta-list">
          <div class="li"><i></i><b>8 типов углов</b> — с примерами под любую тему</div>
          <div class="li"><i></i>критерий силы: какой угол «рабочий»</div>
          <div class="li"><i></i>таблица, куда вписать свою тему</div>
          <div class="li"><i></i>рабочий угол за 15 минут</div>
        </div>
        <span class="cta-btn">Забрать тетрадь → t.me/AlovLab</span>
      </div>
    </article>""")

    slides = "\n".join(S)
    return f"""<title>Карусель · Угол, а не тема · AlovLab</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 4 · 7 августа</span>
    <h1>Публиковать <b>ОДНИМ постом</b>: 8 слайдов, порядок 1→8. Выход — Telegram за тетрадью углов.</h1></div>
  <div class="grid">
{slides}
  </div>
  <div class="notes"><b>Тема:</b> угол, а не тема · B2C, ведёт на курс через Telegram. <b>Честность:</b> примеры углов — иллюстрация приёма; выдуманных цифр/цены нет.</div>
</div>
"""

if __name__ == "__main__":
    OUT.write_text(render(), encoding="utf-8"); print("HTML:", OUT)
