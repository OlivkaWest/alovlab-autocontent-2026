# -*- coding: utf-8 -*-
"""AlovLab · День 16 (19.08) «Профиль как мост» — SHOWCASE + иллюстрации.
Профиль, который переводит с Reels в Telegram, против витрины ради витрины. Три узла моста:
шапка → закреп → хайлайты. Промпт — шапка через Claude. Честность: без выдуманных цифр
(клик-статистика IG→TG не отслеживается). Ниша примеров — ИИ/контент/бизнес. Нумерация N/8.
RU кроме AlovLab и промптов. Запуск: python3 scripts/carousel_showcase_day16.py"""
from carousel_showcase_render import (CSS as CSS0, DEFS, FOOT, sparks, rings, LOGO, ROOT)

OUTDIR = ROOT / "exports" / "carousels" / "day-16-showcase"; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / "day-16-showcase.html"

EXTRA = r"""
.hsm .head h2{font-size:37px}
.cover .head h2{font-size:46px}
.cover .sub{margin-top:14px;max-width:27ch;font-size:16.5px}
.mch .head h2{font-size:35px}
.viz{flex:1;position:relative;z-index:2;display:grid;place-items:center;min-height:0;margin-top:14px}
.viz svg{width:min(94%,490px);height:100%;max-height:360px}
.viz::before{content:"";position:absolute;left:50%;top:55%;width:74%;height:64%;transform:translate(-50%,-50%);
 background:radial-gradient(closest-side,rgba(255,120,40,.16),transparent 72%);z-index:-1;pointer-events:none}
.body.tight{margin-top:16px}
.pbox{position:relative;z-index:4;margin-top:15px;background:#120c06;border:1px solid rgba(255,150,80,.28);
 border-left:3px solid var(--o);border-radius:14px;padding:16px 18px}
.pbox .tag{display:inline-block;font-weight:800;font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:#160e07;
 background:linear-gradient(150deg,var(--o2),var(--o));padding:5px 10px;border-radius:6px;margin-bottom:11px}
.pbox code{display:block;font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace;font-size:12px;line-height:1.5;
 color:#ffd9b8;white-space:pre-wrap;word-break:break-word}
.pbox .ru{margin-top:11px;padding-top:10px;border-top:1px solid rgba(255,255,255,.1);font-size:11.5px;line-height:1.4;color:#b9ad9b}
.pbox .ru b{color:#fff}
.gv{position:relative;z-index:4;margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:11px}
.gv .b{border-radius:13px;padding:13px 15px;font-size:13px;line-height:1.42}
.gv .bad{background:#1a120c;border:1px solid #4a2f22;color:#c8a998}
.gv .good{background:#12100a;border:1px solid rgba(255,150,80,.32);color:#ffe4c8}
.gv .lbl{display:block;font-weight:800;font-size:10px;letter-spacing:.05em;text-transform:uppercase;margin-bottom:7px}
.gv .bad .lbl{color:#c56b4e}.gv .good .lbl{color:var(--o2)}
.mlist{position:relative;z-index:4;margin-top:16px;margin-bottom:4px;display:flex;flex-direction:column;gap:8px}
.mrow{display:flex;align-items:center;gap:13px;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));
 border:1px solid rgba(255,140,60,.14);border-radius:13px;padding:10px 15px}
.mrow .n{flex:0 0 auto;width:27px;height:27px;border-radius:8px;display:flex;align-items:center;justify-content:center;
 font-weight:800;font-size:13px;color:#160e07;background:linear-gradient(150deg,var(--o2),var(--o))}
.mrow .t b{font-weight:700;font-size:15.5px;color:#fff;line-height:1.15;display:block}
.mrow .t span{font-weight:500;font-size:12.5px;color:#8a8177;line-height:1.2}
.bizmap{position:relative;z-index:4;margin-top:13px;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.bizmap .r{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.02));border:1px solid rgba(255,140,60,.14);
 border-radius:11px;padding:9px 12px;font-size:12.5px;line-height:1.3;color:#c9bdac}
.bizmap .r b{color:#ff9a4d;font-weight:800;display:block;font-size:11px;text-transform:uppercase;letter-spacing:.03em;margin-bottom:2px}
"""
CSS = CSS0 + EXTRA

PLANE = 'M6 26 l64 -18 -18 42 -14 -13 -13 11 z'  # бумажный самолётик (Telegram)

def profile_card(x, y, w=150, h=158):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#ffffff06" stroke="#ffffff1f" stroke-width="2"/>'
            f'<circle cx="{x+w/2:.0f}" cy="{y+40}" r="23" stroke="#6a6157" stroke-width="3" fill="#1a140d"/>'
            f'<path d="M{x+24} {y+86} h{w-48} M{x+24} {y+104} h{w-80}" stroke="#5a5148" stroke-width="6" stroke-linecap="round"/>'
            f'<rect x="{x+24}" y="{y+122}" width="{w-48}" height="20" rx="10" fill="none" stroke="#6a6157" stroke-width="2"/>')

SC_COVER = f'''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 {profile_card(30,46)}
 <text x="105" y="216" fill="#8a8177" font-size="11" font-weight="800" text-anchor="middle">твой профиль</text>
 <path d="M186 100 C220 100 224 78 252 74" stroke="#8a8177" stroke-width="3" fill="none" stroke-linecap="round"/>
 <path d="M186 150 C220 150 224 172 252 176" stroke="url(#ig)" stroke-width="3.5" fill="none" stroke-linecap="round"/>
 <g transform="translate(256,46)">
   <rect x="0" y="0" width="150" height="60" rx="14" fill="#141210" stroke="#3a332c" stroke-width="2"/>
   <path d="M42 18 l28 24 M70 18 l-28 24" stroke="#7a5148" stroke-width="4.5" stroke-linecap="round"/>
   <text x="98" y="37" fill="#8a8177" font-size="12" font-weight="800">в никуда</text>
 </g>
 <g transform="translate(256,150)">
   <rect x="0" y="0" width="150" height="60" rx="14" fill="#1a1108" stroke="url(#ig)" stroke-width="2.5"/>
   <path d="{PLANE}" fill="#ff9a4d" transform="translate(6,6) scale(0.62)"/>
   <text x="150" y="37" fill="#ff9a4d" font-size="12" font-weight="800" text-anchor="end" dx="-14">Telegram</text>
 </g>
</svg>'''

SC_PROBLEM = f'''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="30" y="70" width="80" height="110" rx="14" fill="#1a1108" stroke="url(#ig)" stroke-width="2"/>
 <path d="M60 110 l26 15 -26 15 z" fill="url(#ig)"/>
 <text x="70" y="200" fill="#8a8177" font-size="12" font-weight="800" text-anchor="middle">Reels</text>
 <path d="M118 125 h30 M140 117 l10 8 -10 8" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 {profile_card(158,66,132,138)}
 <text x="224" y="216" fill="#8a8177" font-size="11.5" font-weight="800" text-anchor="middle">профиль</text>
 <path d="M298 130 C340 130 350 150 356 176" stroke="#6a6157" stroke-width="3" fill="none" stroke-linecap="round"/>
 <path d="M356 176 l-9 -6 M356 176 l3 -10" stroke="#6a6157" stroke-width="3" fill="none" stroke-linecap="round"/>
 <text x="380" y="150" fill="#8a8177" font-size="12.5" font-weight="800">ушёл</text>
</svg>'''

SC_CAUSE = '''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 <rect x="118" y="24" width="180" height="180" rx="14" fill="#ffffff06" stroke="#ffffff1a" stroke-width="2"/>
 <g fill="#ffffff0d" stroke="#3a332c" stroke-width="1.5">
  <rect x="132" y="38" width="48" height="48" rx="6"/><rect x="186" y="38" width="48" height="48" rx="6"/><rect x="240" y="38" width="48" height="48" rx="6"/>
  <rect x="132" y="92" width="48" height="48" rx="6"/><rect x="186" y="92" width="48" height="48" rx="6"/><rect x="240" y="92" width="48" height="48" rx="6"/>
  <rect x="132" y="146" width="48" height="48" rx="6"/><rect x="186" y="146" width="48" height="48" rx="6"/><rect x="240" y="146" width="48" height="48" rx="6"/>
 </g>
 <path d="M312 114 h44" stroke="url(#ig)" stroke-width="3" stroke-linecap="round" stroke-dasharray="7 6"/>
 <path d="M360 96 v36" stroke="#7a5148" stroke-width="5" stroke-linecap="round"/>
 <text x="356" y="150" fill="#8a8177" font-size="12" font-weight="800" text-anchor="middle">стена</text>
 <text x="208" y="228" fill="#8a8177" font-size="13.5" font-weight="800" text-anchor="middle">красиво — но некуда идти</text>
</svg>'''

SC_MISTAKE = f'''<svg viewBox="0 0 480 250" fill="none" font-family="Manrope">
 {profile_card(28,40,140,150)}
 <path d="M62 26 l3 8 8 3 -8 3 -3 8 -3 -8 -8 -3 8 -3 z" fill="#6a6157"/>
 <path d="M150 30 l2.5 6.5 6.5 2.5 -6.5 2.5 -2.5 6.5 -2.5 -6.5 -6.5 -2.5 6.5 -2.5 z" fill="#6a6157"/>
 <text x="98" y="210" fill="#8a8177" font-size="12" font-weight="800" text-anchor="middle">полируешь витрину</text>
 <path d="M182 116 h40 M214 108 l10 8 -10 8" stroke="#8a8177" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
 {profile_card(238,52,110,116)}
 <path d="M352 110 C372 110 376 128 392 132" stroke="url(#ig)" stroke-width="3.5" fill="none" stroke-linecap="round"/>
 <path d="{PLANE}" fill="#ff9a4d" transform="translate(392,120) scale(0.42)"/>
 <text x="300" y="210" fill="#ff9a4d" font-size="12" font-weight="800" text-anchor="middle">строишь мост</text>
</svg>'''

def viz(scene): return f'<div class="viz">{scene}</div>'

def cover(hw, ho, sub, scene):
    return f"""<article class="slide cover">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">AlovLab · профиль как мост</span><span class="pg">1<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="sub">{sub}</div>
  {viz(scene)}
  {FOOT}
</article>"""

def sc(eb, hw, ho, bl, bm, scene, pg):
    return f"""<article class="slide">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">{eb}</span><span class="pg">{pg}<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="body tight"><span class="l">{bl}</span> <span class="m">{bm}</span></div>
  {viz(scene)}
  {FOOT}
</article>"""

STEPS = [
 ("1","Шапка","кто ты · для кого · что дашь · → в Telegram"),
 ("2","Закреп","отвечает: зачем идти в Telegram именно к тебе"),
 ("3","Хайлайты","путь новичка: с чего начать → куда прийти"),
]
def method_slide():
    rows="".join(f'<div class="mrow"><div class="n">{n}</div><div class="t"><b>{t}</b><span>{s}</span></div></div>' for n,t,s in STEPS)
    return f"""<article class="slide mch">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Метод · мост в 3 узла</span><span class="pg">5<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Мост —</span><span class="o">три узла.</span></h2></div>
  <div class="mlist">{rows}</div>
  <div class="body tight" style="margin-top:14px">Каждый узел ведёт дальше: шапка → закреп → хайлайты → <b style="color:#fff">Telegram</b>. Ни один не «для красоты».</div>
  {FOOT}
</article>"""

def prompt_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Готовый промпт · Claude</span><span class="pg">6<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Шапка по</span><span class="o">формуле.</span></h2></div>
  <div class="pbox"><span class="tag">Claude · скопировать</span><code>Напиши шапку профиля (bio) по формуле: кто ты → для кого →
что человек получит → куда идти (Telegram за конкретным).
4 строки, живо, без штампов и эмодзи-мусора. Дай 3 варианта.
Ниша: [ТВОЯ]. Что даю в Telegram: [ГАЙД / ПРОМПТ / ЧЕК-ЛИСТ].</code>
    <div class="ru"><b>Разбор:</b> шапка — не «о себе», а указатель: за чем и куда идти. Последняя строка всегда ведёт в Telegram.</div></div>
  {FOOT}
</article>"""

def demo_slide():
    return f"""<article class="slide hsm">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="top"><span class="eb">Витрина / мост · шапка</span><span class="pg">7<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">Указатель,</span><span class="o">а не витрина.</span></h2></div>
  <div class="gv">
    <div class="b bad"><span class="lbl">✕ Витрина</span>«Эксперт по нейросетям. Помогаю выйти на новый уровень 🚀 DM открыт.»</div>
    <div class="b good"><span class="lbl">✓ Мост</span>«Учу собирать контент на ИИ — с нуля. Гайд «Промпт дня» → в Telegram, ссылка ниже.»</div>
  </div>
  <div class="bizmap">
    <div class="r"><b>Эксперт</b>гайд/чек-лист → Telegram</div>
    <div class="r"><b>Магазин</b>подборка/скидка в канале</div>
    <div class="r"><b>Услуга</b>разбор/бриф → в личку</div>
    <div class="r"><b>Локальный</b>меню/запись → бот</div>
  </div>
  {FOOT}
</article>"""

def cta(hw, ho, items, btn):
    lis="".join(f'<div class="li"><i></i><span>{t}</span></div>' for t in items)
    return f"""<article class="slide cta">{DEFS}
  <div class="sparks">{sparks()}</div>
  <div class="stage"><div class="rings" style="top:120%">{rings()}</div></div>
  <div class="top"><span class="eb">Дальше</span><span class="pg">8<b> / 8</b></span></div>
  <div class="head"><h2><span class="w">{hw}</span><span class="o">{ho}</span></h2></div>
  <div class="clist">{lis}</div>
  <div class="btn">{btn}</div>
  {FOOT}
</article>"""

SLIDES = [
 cover("Профиль — не", "витрина. Развилка.", "Гость приходит с Reels и стоит на развилке. Сейчас она ведёт в никуда — а должна в Telegram.", SC_COVER),
 sc("Проблема","Приходят","и уходят.","С Reels заглянули в профиль —","и закрыли. Он не сказал, зачем оставаться и куда идти.", SC_PROBLEM, 2),
 sc("Причина","Профиль как","витрина.","Красивая лента, аватар, эмодзи —","но нет одного понятного пути. Гостю некуда шагнуть.", SC_CAUSE, 3),
 sc("Ошибка","Полируешь","витрину.","Меняешь аватар и раскладку постов.","А надо не украшать, а построить мост в Telegram.", SC_MISTAKE, 4),
 method_slide(),
 prompt_slide(),
 demo_slide(),
 cta("Собери","мост.",
     ["<b>формула шапки</b>, закреп и 5 хайлайтов — в тетради",
      "бланк профиля под путь новичка",
      "инструмент дня — Instagram + Telegram"],
     "Тетрадь дня → t.me/AlovLab"),
]

HTML = f"""<title>Профиль как мост · День 16 · showcase · AlovLab</title><meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<div class="page">
  <div class="lead"><span class="eb">AlovLab · День 16 · 19 августа · showcase + иллюстрации</span>
    <h1>Профиль как мост: обложка → проблема → причина → ошибка → 3 узла → промпт (шапка) → до/после → CTA. 4:5.</h1></div>
  <div class="grid">
{''.join(SLIDES)}
  </div>
</div>"""
OUT.write_text(HTML, encoding="utf-8")
print("HTML:", OUT, f"{OUT.stat().st_size//1024} KB", "| slides:", len(SLIDES))
