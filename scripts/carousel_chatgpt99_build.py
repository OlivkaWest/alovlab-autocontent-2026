#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = "/home/user/alovlab-autocontent-2026"
OUT = f"{ROOT}/exports/carousels/chatgpt-99"
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920
BG = (9, 9, 8)
WHITE = (245, 245, 245)
GREY = (150, 150, 150)
GREY_DIM = (110, 110, 110)
ORANGE = (243, 123, 34)

FDIR = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FDIR + name, size)

def bold(size): return F("DejaVuSans-Bold.ttf", size)
def reg(size): return F("DejaVuSans.ttf", size)
def mono(size): return F("DejaVuSansMono.ttf", size)
def mono_b(size): return F("DejaVuSansMono-Bold.ttf", size)

LOGO = Image.open(f"{ROOT}/assets/img/logo-mark.png").convert("RGBA")

def spaced(draw, xy, text, font, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        w = draw.textlength(ch, font=font)
        x += w + tracking
    return x

def header(draw, n, total=10):
    x = 64
    y = 60
    draw.text((x, y), "Alov", font=bold(34), fill=WHITE)
    wa = draw.textlength("Alov", font=bold(34))
    draw.text((x + wa, y), "Lab", font=bold(34), fill=ORANGE)
    wl = draw.textlength("Lab", font=bold(34))
    dx = x + wa + wl + 18
    draw.line([(dx, y + 2), (dx, y + 34)], fill=(70, 70, 70), width=2)
    tx = dx + 16
    spaced(draw, (tx, y + 2), "ЛАБОРАТОРИЯ", mono(11), GREY, tracking=1)
    spaced(draw, (tx, y + 18), "НЕЙРОСЕТЕЙ", mono(11), GREY, tracking=1)
    label = f"{n:02d}/{total}"
    lw = draw.textlength(label, font=reg(20))
    rx = W - 64
    draw.line([(rx - lw - 46, y + 16), (rx - lw - 18, y + 16)], fill=(90, 90, 90), width=2)
    draw.text((rx - lw, y + 5), label, font=reg(20), fill=GREY)

def title_block(draw, lines, kicker, top):
    y = top
    for ln in lines:
        draw.text((64, y), ln, font=bold(52), fill=WHITE)
        y += 60
    y += 14
    spaced(draw, (64, y), kicker.upper(), bold(19), ORANGE, tracking=2)
    return y + 40

def glow_panel(im, cx, cy, r, color=ORANGE, alpha=70):
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alpha,))
    ov = ov.filter(ImageFilter.GaussianBlur(r // 2))
    im.alpha_composite(ov)

def slash_watermark(im, cx, cy, size=1500, alpha=14):
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    f = mono_b(size)
    d.text((cx, cy), "/", font=f, fill=(255, 255, 255, alpha))
    im.alpha_composite(ov)

def list_rows(draw, items, x, y_start, width, row_h=100, num_w=58, cmd_size=27, desc_size=22):
    y = y_start
    for num, cmd, desc in items:
        ns = f"{num:02d}"
        draw.text((x, y + 4), ns, font=reg(20), fill=GREY_DIM)
        cx = x + num_w
        draw.text((cx, y), cmd, font=mono_b(cmd_size), fill=WHITE)
        draw.text((cx, y + 34), desc, font=reg(desc_size), fill=GREY)
        y += row_h
    return y

def footer(draw, tagline_lines, y, bottom_right=None, accent_line=True):
    if accent_line:
        draw.line([(64, y), (64 + 90, y)], fill=ORANGE, width=3)
        y += 24
    for ln in tagline_lines:
        col = WHITE if not ln[1] else ORANGE
        draw.text((64, y), ln[0], font=reg(24), fill=col)
        y += 32
    if bottom_right:
        w = draw.textlength(bottom_right, font=bold(24))
        draw.text((W - 64 - w - 40, y - 32), bottom_right, font=bold(24), fill=WHITE)
        ax = W - 64 - 28
        ay = y - 32 + 12
        draw.line([(ax, ay), (ax + 22, ay)], fill=ORANGE, width=3)
        draw.polygon([(ax + 16, ay - 6), (ax + 24, ay), (ax + 16, ay + 6)], fill=ORANGE)

SLIDES = [
    dict(n=2, title=["Стратегия продаж", "и маркетинга"], kicker="Фундамент твоего роста",
         items=[
             (1, "/marketingstrategy", "Полная маркетинговая стратегия"),
             (2, "/salesstrategy", "Стратегия продаж"),
             (3, "/growthstrategy", "Стратегия роста бренда"),
             (4, "/marketingplan", "Пошаговый маркетинговый план"),
             (5, "/salesplan", "План продаж"),
             (6, "/goToMarket", "Вывод продукта на рынок"),
             (7, "/campaignplanner", "План маркетинговой кампании"),
             (8, "/launchplan", "Запуск продукта или услуги"),
             (9, "/growthhack", "Креативные возможности для роста"),
             (10, "/marketingaudit", "Аудит маркетинга"),
             (11, "/salesfunnel", "Воронка продаж"),
         ],
         tagline=[("Стратегия превращает идеи", False), ("в деньги.", False)]),
    dict(n=3, title=["Клиенты", "и аудитория"], kicker="Пойми, для кого ты делаешь",
         items=[
             (12, "/customeravatar", "Портрет идеального клиента"),
             (13, "/buyerpersona", "Образ покупателя"),
             (14, "/audienceinsight", "Анализ потребностей аудитории"),
             (15, "/painpoints", "Главные боли клиентов"),
             (16, "/buyermotivation", "Что мотивирует покупать"),
             (17, "/customerjourney", "Путь клиента"),
             (18, "/customerneeds", "Неудовлетворённые потребности"),
             (19, "/objectionfinder", "Типичные возражения"),
             (20, "/customerpsychology", "Психология решений"),
             (21, "/segment", "Разделение на сегменты"),
             (22, "/targeting", "На какую аудиторию целиться"),
         ],
         tagline=[("Лучший маркетинг —", False), ("это понимание людей.", False)]),
    dict(n=4, title=["Бренд", "и позиционирование"], kicker="Стань заметным",
         items=[
             (23, "/brandpositioning", "Позиционирование бренда"),
             (24, "/valueproposition", "Ценностное предложение"),
             (25, "/usp", "Уникальное торговое предложение"),
             (26, "/brandvoice", "Голос бренда"),
             (27, "/brandmessage", "Главное сообщение"),
             (28, "/brandstory", "История бренда"),
             (29, "/competitorpositioning", "Позиционирование на фоне конкурентов"),
             (30, "/differentiator", "Чем ты отличаешься"),
             (31, "/tagline", "Обещание бренда"),
             (32, "/elevatorpitch", "Маркетинговые слоганы"),
             (33, "/elevatorpitch", "30-секундная презентация"),
         ],
         tagline=[("Сильный бренд", False), ("притягивает клиентов.", False)]),
    dict(n=5, title=["Контент", "и соцсети"], kicker="Делай контент, который работает",
         items=[
             (34, "/contentstrategy", "Контент-стратегия"),
             (35, "/contentcalendar", "Контент-план на 30 дней"),
             (36, "/socialstrategy", "Стратегия постов"),
             (37, "/reelideas", "Идеи коротких видео"),
             (38, "/postideas", "Идеи вовлекающих постов"),
             (39, "/carousel", "Обучающая карусель"),
             (40, "/hook", "Цепляющие хуки"),
             (41, "/caption", "Продающие подписи"),
             (42, "/contentrepurpose", "Перепаковка контента"),
             (43, "/viralcontent", "Идеи вирусного контента"),
             (44, "/engagement", "Повышение вовлечённости"),
         ],
         tagline=[("Контент — это внимание.", True), ("А внимание — продажи.", True)]),
    dict(n=6, title=["Копирайтинг", "и реклама"], kicker="Слова, которые продают",
         items=[
             (45, "/adcopy", "Убедительный рекламный текст"),
             (46, "/facebookad", "Реклама для Facebook"),
             (47, "/googlead", "Варианты объявлений"),
             (48, "/instagramad", "Реклама для Instagram"),
             (49, "/landingpage", "Текст для лендинга"),
             (50, "/headline", "Сильные заголовки"),
             (51, "/salescopy", "Продающий текст"),
             (52, "/emailcopy", "Маркетинговые письма"),
             (53, "/productcopy", "Описания продуктов"),
             (54, "/calltoaction", "Мощные призывы к действию"),
             (55, "/abtestcopy", "A/B варианты текстов"),
         ],
         tagline=[("Правильные слова =", False), ("больше клиентов.", False)]),
    dict(n=7, title=["Лидогенерация", "и продажи"], kicker="Привлекай, общайся, закрывай",
         items=[
             (56, "/leadgen", "Стратегии привлечения лидов"),
             (57, "/prospecting", "Поиск потенциальных клиентов"),
             (58, "/leadmagnet", "Неотразимый лид-магнит"),
             (59, "/coldemail", "Холодные письма"),
             (60, "/coldcall", "Скрипт холодного звонка"),
             (61, "/linkedinoutreach", "Сообщения для LinkedIn"),
             (62, "/followup", "Эффективный follow-up"),
             (63, "/salespitch", "Питч продаж"),
             (64, "/discoverycall", "Скрипт диагностического звонка"),
             (65, "/qualification", "Квалификация клиентов"),
             (66, "/closing", "Как закрывать больше сделок"),
         ],
         tagline=[("Больше разговоров.", False), ("Больше возможностей.", False)]),
    dict(n=8, title=["Психология продаж", "и возражения"], kicker="Понимай людей — продавай легче",
         items=[
             (67, "/objectionhandler", "Ответы на возражения"),
             (68, "/priceobjection", "Работа с ценой"),
             (69, "/trustbuilder", "Повышение доверия"),
             (70, "/urgency", "Создание срочности"),
             (71, "/scarcity", "Идеи дефицита"),
             (72, "/socialproof", "Кейсы и отзывы"),
             (73, "/persuasion", "Убеждающие сообщения"),
             (74, "/negotiation", "Стратегии переговоров"),
             (75, "/closingquestions", "Вопросы для решения о покупке"),
             (76, "/dealrescue", "Возврат «зависших» сделок"),
             (77, "/emailsequence", "Автоматическая email-цепочка"),
         ],
         tagline=[("Люди говорят «нет» не навсегда.", True), ("Нужно просто уметь говорить с ними.", True)]),
    dict(n=9, title=["Удержание клиентов", "и рост"], kicker="Расти на длинной дистанции",
         items=[
             (78, "/welcomeemail", "Приветственные письма"),
             (79, "/nurture", "Прогрев лидов"),
             (80, "/abandonedcart", "Возврат корзины"),
             (81, "/upsell", "Стратегии допродаж"),
             (82, "/crosssell", "Кросс-продажи"),
             (83, "/retention", "Удержание клиентов"),
             (84, "/winback", "Возврат неактивных клиентов"),
             (85, "/referral", "Реферальная программа"),
             (86, "/marketingmetrics", "Ключевые KPI"),
             (87, "/salesmetrics", "KPI продаж"),
             (88, "/conversionaudit", "Аудит воронки"),
         ],
         tagline=[("Удерживать клиентов дешевле,", False), ("чем искать новых.", False)]),
]

def render_single(s):
    im = Image.new("RGBA", (W, H), BG + (255,))
    slash_watermark(im, 660, 1420, size=1600, alpha=13)
    glow_panel(im, W - 60, H - 220, 380, ORANGE, 55)
    d = ImageDraw.Draw(im)
    header(d, s["n"])
    y = title_block(d, s["title"], s["kicker"], top=170)
    y_end = list_rows(d, s["items"], 64, y + 10, W - 128, row_h=115, cmd_size=29, desc_size=23)
    footer(d, s["tagline"], y=1700)
    im.convert("RGB").save(f"{OUT}/slide-{s['n']:02d}.png")
    print("saved", s["n"])

for s in SLIDES:
    render_single(s)

# ---- Slide 10: final, two columns ----
def render_slide10():
    n = 10
    left = [
        (89, "/roianalysis", "Оценка ROI маркетинговых кампаний"),
        (90, "/competitoranalysis", "Анализ конкурентов"),
        (91, "/swot", "SWOT-анализ"),
        (92, "/pricingstrategy", "Ценовая стратегия"),
        (93, "/conversionoptimizer", "Способы повысить конверсию"),
        (94, "/abtest", "Идеи для A/B-тестов"),
    ]
    right = [
        (95, "/funneloptimizer", "Поиск слабых мест в воронке"),
        (96, "/automation", "Какие задачи можно автоматизировать"),
        (97, "/partnerships", "Возможности для партнёрств"),
        (98, "/scalemarketing", "План масштабирования"),
        (99, "/marketingmastermind", "Полный план роста для бизнеса"),
    ]
    im = Image.new("RGBA", (W, H), BG + (255,))
    slash_watermark(im, 660, 1420, size=1600, alpha=13)
    glow_panel(im, W - 40, H - 200, 380, ORANGE, 60)
    d = ImageDraw.Draw(im)
    header(d, n)
    y = title_block(d, ["Аналитика", "и продвинутый рост"], "Принимай решения на данных", top=170)
    col_w = (W - 128 - 40) // 2
    list_rows(d, left, 64, y + 10, col_w, row_h=205, num_w=52, cmd_size=25, desc_size=20)
    list_rows(d, right, 64 + col_w + 40, y + 10, col_w, row_h=205, num_w=52, cmd_size=25, desc_size=20)
    footer(d, [("Используй эти команды.", False), ("Строй системный рост. Действуй.", False)],
           y=1750, bottom_right="Вперёд")
    im.convert("RGB").save(f"{OUT}/slide-{n:02d}.png")
    print("saved", n)

render_slide10()

# ---- Slide 1: cover, resized from user's original to canonical 1080x1920 ----
cover = Image.open(f"{ROOT}/content/carousel-assets/chatgpt-99/cover-src.png").convert("RGB")
cover_resized = cover.resize((W, H), Image.LANCZOS)
cover_resized.save(f"{OUT}/slide-01.png")
print("saved cover 1")
