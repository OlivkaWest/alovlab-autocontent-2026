# -*- coding: utf-8 -*-
"""AlovLab · образовательная карусель «Как написать хук» — прикладная, на примерах.
8 слайдов, 4:5. Переиспользует премиум-систему из carousel_edu_render (CSS, компоненты).
Каждый слайд: мысль + пример (слабый/сильный хук) + вывод + line-иллюстрация.
Запуск: python3 scripts/carousel_hooks_render.py
"""
import pathlib
from carousel_edu_render import CSS, MARK, snum, chip, _art, LOGO, ROOT

OUTDIR = ROOT / "exports" / "carousels" / "hooks"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "hooks.html"

# иллюстрации под тему хука
ARTH = {
 1: _art('<path d="M50 16v30a18 18 0 1 1-18-18"/><circle cx="50" cy="14" r="5"/><path d="M32 28l-7-6m7 6l7-6"/>'),  # крючок
 2: _art('<path d="M34 20h40M34 30h30" opacity=".4"/><path d="M52 40v34"/><path d="M38 60l14 14 14-14"/>'),          # листают вниз
 3: _art('<circle cx="52" cy="52" r="26"/><circle cx="52" cy="52" r="15"/><circle cx="52" cy="52" r="5" fill="currentColor" stroke="none"/>'),  # попадание
 4: _art('<rect x="18" y="28" width="48" height="32" rx="11"/><path d="M30 36l24 16M54 36l-24 16" opacity=".9"/><path d="M32 60v9l9-9"/>'),  # убитый хук
 5: _art('<path d="M28 28h50M28 42h50M28 56h38M28 70h44" opacity=".85"/><g fill="currentColor" stroke="none"><circle cx="20" cy="28" r="3.4"/><circle cx="20" cy="42" r="3.4"/><circle cx="20" cy="56" r="3.4"/><circle cx="20" cy="70" r="3.4"/></g>'),  # список типов
 6: _art('<path d="M20 42h30M20 56h20" opacity=".55"/><circle cx="60" cy="52" r="16"/><path d="M72 64l14 14"/>'),   # лупа на сильной строке
 7: _art('<path d="M16 24h68l-24 30v20l-20 8V54z"/><g fill="currentColor" stroke="none" opacity=".85"><circle cx="28" cy="17" r="3"/><circle cx="41" cy="17" r="3"/><circle cx="54" cy="17" r="3"/><circle cx="67" cy="17" r="3"/><circle cx="50" cy="84" r="4"/></g>'),  # 5→1
 8: _art('<rect x="26" y="22" width="46" height="58" rx="8"/><path d="M36 40h26M36 52h26M36 64h16" opacity=".7"/><path d="M71 19l2.6 7.4 7.4 2.6-7.4 2.6-2.6 7.4-2.6-7.4-7.4-2.6 7.4-2.6z" fill="rgba(255,122,51,.22)"/>'),  # тетрадь
}

def render():
    S = []
    # 1 · cover
    S.append(f"""<article class="slide">
      {MARK}{snum(1)}{ARTH[1]}
      <div class="mid">
        <div class="eyebrow">AlovLab · как писать хук</div>
        <h2 class="h h--xl">Первую строку читают все.<br>Дальше — <span class="a">только если зацепил.</span></h2>
      </div>
      <div class="viz chips">
        {chip('«Сегодня хочу рассказать про нейросети…»','слабо')}
        {chip('«Ты платишь за то, что ИИ делает за 5 минут»','сильно',on=True)}
        <div class="vcap">↑ одна строка решает: читают тебя или листают.</div>
      </div>
    </article>""")

    # 2 · проблема
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(2)}{ARTH[2]}
      <div class="mid">
        <div class="eyebrow"><b>Проблема</b></div>
        <h2 class="h h--lg">Ты начинаешь<br><span class="a">с разгона.</span></h2>
        <p class="sub">Пока ты «подводишь к теме», палец уже листает. Разгон дочитывают только те, кто и так подписан.</p>
      </div>
      <div class="viz chips">
        {chip('«В этом посте я расскажу…»','разгон')}
        {chip('«Друзья, давно не виделись…»','разгон')}
        <div style="margin-top:4px"><span class="concl">Разгон = потерянная первая секунда</span></div>
      </div>
    </article>""")

    # 3 · принцип
    S.append(f"""<article class="slide">
      {MARK}{snum(3)}{ARTH[3]}
      <div class="mid">
        <div class="eyebrow"><b>Принцип</b></div>
        <h2 class="h h--lg">Хук — это не вступление.<br>Это <span class="a">обещание или конфликт.</span></h2>
        <p class="sub">Первая строка должна вешать вопрос, на который хочется ответ.</p>
      </div>
      <div class="viz dvs">
        <div class="b bad"><div class="l">Вступление</div><div class="t">«Сегодня поговорим о том, как…»</div></div>
        <div class="b good"><div class="l">Конфликт</div><div class="t">«Ты постишь каждый день — и всё равно тишина»</div></div>
      </div>
    </article>""")

    # 4 · ошибки
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(4)}{ARTH[4]}
      <div class="mid">
        <div class="eyebrow"><b>Ошибка</b></div>
        <h2 class="h h--lg">Три начала, которые<br><span class="a">убивают пост.</span></h2>
        <p class="sub">Это не хуки. Это разгон, который просят пролистнуть.</p>
      </div>
      <div class="viz chips">
        {chip('«Привет, друзья!»','приветствие')}
        {chip('«В этом видео разберём…»','анонс')}
        {chip('«А вы когда-нибудь задумывались…»','пустой вопрос')}
      </div>
    </article>""")

    # 5 · типы хуков (solution)
    def hc(t, ex): return f'<div class="s"><div class="n">{t}</div><div class="t" style="font-size:13px;font-weight:700;margin-top:6px">{ex}</div></div>'
    S.append(f"""<article class="slide">
      {MARK}{snum(5)}{ARTH[5]}
      <div class="mid">
        <div class="eyebrow"><b>Решение</b></div>
        <h2 class="h h--md">6 хуков, которые <span class="a">цепляют.</span></h2>
        <div class="src">
          {hc('Ошибка','«Ты пишешь промпт не так»')}
          {hc('Результат','«Собрал ролик за вечер — без съёмок»')}
          {hc('Конфликт','«Дорогой продукт. Дешёвый контент»')}
          {hc('Вопрос новичка','«Почему картинка выходит дёшево?»')}
          {hc('До / после','«Было: сток. Стало: свой стиль»')}
          {hc('Разрушение мифа','«Дело не в нейросети»')}
        </div>
      </div>
    </article>""")

    # 6 · пример
    S.append(f"""<article class="slide slide--plain">
      {MARK}{snum(6)}{ARTH[6]}
      <div class="mid">
        <div class="eyebrow"><b>Пример</b></div>
        <h2 class="h h--md">Одна тема — <span class="a">слабый и сильный</span> хук.</h2>
        <div class="dvs" style="margin-top:14px">
          <div class="b bad"><div class="l">Слабо</div><div class="t">«Расскажу, чем полезны нейросети»</div></div>
          <div class="b good"><div class="l">Сильно</div><div class="t">«ИИ не заменит тебя. Заменит тот, кто им пользуется»</div></div>
        </div>
      </div>
      <div class="vcap">Сильный хук вешает конфликт в первой строке. Разгон — выкинь.</div>
    </article>""")

    # 7 · практика
    S.append(f"""<article class="slide">
      {MARK}{snum(7)}{ARTH[7]}
      <div class="mid">
        <div class="eyebrow"><b>Практический шаг</b></div>
        <h2 class="h h--md">Напиши <span class="a">5 хуков</span> к одной теме. Оставь <span class="a">1.</span></h2>
        <p class="sub">Не улучшай первый — накидай пять разных и выбери самый острый.</p>
        <span class="badge">5 хуков → 1 сильный → пост</span>
        <div class="mcheck">
          <div class="r">первое слово уже работает</div>
          <div class="r">нет приветствия и разгона</div>
          <div class="r">есть конфликт или обещание</div>
        </div>
      </div>
    </article>""")

    # 8 · CTA
    S.append(f"""<article class="slide slide--cta">
      {MARK}{snum(8)}{ARTH[8]}
      <div class="cta-mid">
        <img class="cta-logo" src="data:image/png;base64,{LOGO}" alt="AlovLab">
        <h2 class="cta-h">Забери <span class="a">8 типов хуков</span> и шаблон.</h2>
        <div class="cta-list">
          <div class="li"><i></i><b>8 типов хуков</b> — с примерами под любой пост</div>
          <div class="li"><i></i>формула сильного хука за 9 слов</div>
          <div class="li"><i></i>чек «слабый → сильный» на каждую строку</div>
          <div class="li"><i></i>шаблон: 5 хуков к теме за 5 минут</div>
        </div>
        <span class="cta-btn">Забрать в Telegram → t.me/AlovLab</span>
      </div>
    </article>""")

    slides = "\n".join(S)
    return f"""<title>Карусель · Как написать хук · AlovLab</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · как писать хук</span>
    <h1>Публиковать <b>ОДНИМ постом</b>: 8 слайдов, порядок 1→8. Выход — Telegram за шаблоном хуков.</h1></div>
  <div class="grid">
{slides}
  </div>
  <div class="notes"><b>Тема:</b> как написать хук, который не пролистнут · B2C, ведёт на курс через Telegram. <b>Честность:</b> примеры хуков — иллюстрация приёма; выдуманных цифр/цены нет.</div>
</div>
"""

if __name__ == "__main__":
    OUT.write_text(render(), encoding="utf-8")
    print("HTML:", OUT)
