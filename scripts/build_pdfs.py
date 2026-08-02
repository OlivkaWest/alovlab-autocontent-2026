# -*- coding: utf-8 -*-
"""
Генератор PDF-материалов для лендинга «Автоконтент 2026» (AlovLab).

Собирает два реально скачиваемых файла из подтверждённого содержания
методички интенсива:
  - assets/pdf/startovy-gayd-avtokontent-2026.pdf  — Стартовый гайд (подготовка)
  - assets/pdf/rabochaya-tetrad-avtokontent-2026.pdf — Рабочая тетрадь (шаблоны)

Запуск:  python3 scripts/build_pdfs.py
Зависимость: reportlab (pip install reportlab)

Все тексты взяты из методички AlovLab. Ничего не выдумано.
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
    TableStyle, ListFlowable, ListItem, HRFlowable, PageBreak, KeepTogether,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "pdf")
os.makedirs(OUT, exist_ok=True)

# --- Шрифты с кириллицей ---
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("Body", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Bold", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Mono", os.path.join(FONT_DIR, "DejaVuSansMono.ttf")))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Bold")

# --- Палитра AlovLab ---
INK = colors.HexColor("#17140f")
GRAPHITE = colors.HexColor("#3d3a34")
MUTED = colors.HexColor("#6b675f")
ORANGE = colors.HexColor("#e8672a")
AMBER = colors.HexColor("#c98a3c")
PAPER = colors.HexColor("#faf7f2")
LINE = colors.HexColor("#e4ddd1")
SOFT = colors.HexColor("#f2ece1")

PAGE_W, PAGE_H = A4
MARGIN = 20 * mm

# --- Стили ---
def styles():
    s = {}
    s["kicker"] = ParagraphStyle("kicker", fontName="Bold", fontSize=8.5, leading=12,
                                 textColor=ORANGE, spaceAfter=4, tracking=1)
    s["h1"] = ParagraphStyle("h1", fontName="Bold", fontSize=25, leading=29,
                             textColor=INK, spaceAfter=6)
    s["h2"] = ParagraphStyle("h2", fontName="Bold", fontSize=15, leading=19,
                             textColor=INK, spaceBefore=16, spaceAfter=7)
    s["h3"] = ParagraphStyle("h3", fontName="Bold", fontSize=11.5, leading=15,
                             textColor=GRAPHITE, spaceBefore=10, spaceAfter=3)
    s["body"] = ParagraphStyle("body", fontName="Body", fontSize=10, leading=15.5,
                               textColor=GRAPHITE, spaceAfter=6, alignment=TA_LEFT)
    s["lead"] = ParagraphStyle("lead", fontName="Body", fontSize=11.5, leading=17,
                               textColor=INK, spaceAfter=8)
    s["li"] = ParagraphStyle("li", fontName="Body", fontSize=10, leading=15,
                             textColor=GRAPHITE)
    s["small"] = ParagraphStyle("small", fontName="Body", fontSize=8.5, leading=12,
                                textColor=MUTED)
    s["mono"] = ParagraphStyle("mono", fontName="Mono", fontSize=8.5, leading=13,
                               textColor=INK)
    s["cap"] = ParagraphStyle("cap", fontName="Bold", fontSize=9.5, leading=13,
                              textColor=INK, spaceAfter=2)
    s["quote"] = ParagraphStyle("quote", fontName="Body", fontSize=9.5, leading=14,
                                textColor=MUTED, leftIndent=10)
    return s

S = styles()


def bullets(items, style="li"):
    return ListFlowable(
        [ListItem(Paragraph(t, S[style]), leftIndent=14, value="•") for t in items],
        bulletType="bullet", bulletColor=ORANGE, bulletFontName="Bold",
        bulletFontSize=10, leftIndent=6, spaceAfter=8,
    )


def numbered(items, style="li"):
    return ListFlowable(
        [ListItem(Paragraph(t, S[style]), leftIndent=16) for t in items],
        bulletType="1", bulletColor=ORANGE, bulletFontName="Bold",
        bulletFontSize=10, leftIndent=8, spaceAfter=8,
    )


def callout(title, text):
    inner = [Paragraph(title, S["cap"]), Paragraph(text, S["body"])]
    t = Table([[inner]], colWidths=[PAGE_W - 2 * MARGIN - 2])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), SOFT),
        ("LINEBEFORE", (0, 0), (0, -1), 2.4, ORANGE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


MONO_LIGHT = ParagraphStyle("monolight", fontName="Mono", fontSize=8.5, leading=13,
                            textColor=colors.HexColor("#f4ede1"))

def code_block(lines):
    txt = "<br/>".join(l.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                       for l in lines)
    p = Paragraph(txt, MONO_LIGHT)
    t = Table([[p]], colWidths=[PAGE_W - 2 * MARGIN - 2])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1b1813")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def checklist(items):
    rows = [[Paragraph("☐", ParagraphStyle("box", fontName="Body", fontSize=12,
            textColor=AMBER)), Paragraph(t, S["li"])] for t in items]
    t = Table(rows, colWidths=[10 * mm, PAGE_W - 2 * MARGIN - 10 * mm - 2])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
    ]))
    return t


def field(label, lines=1):
    """Поле для заполнения от руки: подпись + линованные строки."""
    flow = [Paragraph(label, S["cap"])]
    for _ in range(lines):
        flow.append(HRFlowable(width="100%", thickness=0.5, color=LINE,
                               spaceBefore=9, spaceAfter=0))
    flow.append(Spacer(1, 4))
    return KeepTogether(flow)


# --- Оформление страницы (шапка/подвал/обложка) ---
class DocMaker:
    def __init__(self, filename, title, subtitle):
        self.title = title
        self.subtitle = subtitle
        self.doc = BaseDocTemplate(
            filename, pagesize=A4,
            leftMargin=MARGIN, rightMargin=MARGIN,
            topMargin=26 * mm, bottomMargin=20 * mm,
            title=title, author="AlovLab", subject="Автоконтент 2026",
        )
        frame = Frame(MARGIN, 20 * mm, PAGE_W - 2 * MARGIN,
                      PAGE_H - 26 * mm - 20 * mm, id="main")
        self.doc.addPageTemplates([
            PageTemplate(id="cover", frames=[Frame(0, 0, PAGE_W, PAGE_H, id="c")],
                         onPage=self._cover_bg),
            PageTemplate(id="body", frames=[frame],
                         onPage=self._chrome),
        ])

    def _logo(self, c, x, y, scale=1.0, light=False):
        s = 8.5 * scale
        c.saveState()
        c.setFillColor(ORANGE)
        c.roundRect(x, y, s, s, 2.0 * scale, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Bold", 6.6 * scale)
        c.drawCentredString(x + s / 2, y + s / 2 - 2.3 * scale, "A")
        c.setFillColor(colors.white if light else INK)
        c.setFont("Bold", 8.6 * scale)
        c.drawString(x + s + 4 * scale, y + s / 2 - 3 * scale, "AlovLab")
        c.restoreState()

    def _chrome(self, c, doc):
        # шапка
        self._logo(c, MARGIN, PAGE_H - 16 * mm, 1.0)
        c.setFillColor(MUTED)
        c.setFont("Body", 7.5)
        c.drawRightString(PAGE_W - MARGIN, PAGE_H - 13 * mm, "Автоконтент 2026")
        c.setStrokeColor(LINE)
        c.setLineWidth(0.5)
        c.line(MARGIN, PAGE_H - 19 * mm, PAGE_W - MARGIN, PAGE_H - 19 * mm)
        # подвал
        c.setStrokeColor(LINE)
        c.line(MARGIN, 15 * mm, PAGE_W - MARGIN, 15 * mm)
        c.setFillColor(MUTED)
        c.setFont("Body", 7.5)
        c.drawString(MARGIN, 11.5 * mm, "AlovLab · t.me/AlovLab · vk.com/alovlab · alovlab.ru")
        c.drawRightString(PAGE_W - MARGIN, 11.5 * mm, "%d" % doc.page)

    def _cover_bg(self, c, doc):
        c.setFillColor(INK)
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        # тёплое пятно света
        for i, rad in enumerate(range(220, 40, -26)):
            t = i / 7.0
            col = colors.Color(0.91 * (1 - t) + 0.09, 0.40 * (1 - t) + 0.09,
                               0.16 * (1 - t) + 0.06, alpha=0.10)
            c.setFillColor(col)
            c.circle(PAGE_W * 0.78, PAGE_H * 0.74, rad, fill=1, stroke=0)
        self._logo(c, MARGIN, PAGE_H - 34 * mm, 1.6, light=True)
        c.setStrokeColor(colors.HexColor("#2c2820"))
        c.line(MARGIN, PAGE_H - 40 * mm, PAGE_W - MARGIN, PAGE_H - 40 * mm)

        c.setFillColor(ORANGE)
        c.setFont("Bold", 10)
        c.drawString(MARGIN, PAGE_H * 0.52 + 30, "БЕСПЛАТНЫЙ ПРАКТИЧЕСКИЙ ИНТЕНСИВ")
        c.setFillColor(colors.white)
        for i, line in enumerate(self.title.split("\n")):
            c.setFont("Bold", 33)
            c.drawString(MARGIN, PAGE_H * 0.52 - i * 34, line)
        c.setFillColor(colors.HexColor("#cbc3b5"))
        c.setFont("Body", 12.5)
        ty = PAGE_H * 0.52 - len(self.title.split("\n")) * 34 - 10
        for line in self.subtitle.split("\n"):
            c.drawString(MARGIN, ty, line)
            ty -= 18
        c.setFillColor(colors.HexColor("#8a8175"))
        c.setFont("Body", 9)
        c.drawString(MARGIN, 24 * mm, "Илья Алов · Нейромонах · основатель AlovLab")
        c.drawString(MARGIN, 18 * mm, "Материал подготовлен на основе методички интенсива. © AlovLab")

    def build(self, story):
        self.doc.build(story)


# ============================================================
# 1. СТАРТОВЫЙ ГАЙД
# ============================================================
def build_starter_guide():
    path = os.path.join(OUT, "startovy-gayd-avtokontent-2026.pdf")
    dm = DocMaker(path, "Стартовый гайд", "Подготовка к интенсиву за 20–30 минут")
    st = []
    from reportlab.platypus import NextPageTemplate, FrameBreak
    st.append(NextPageTemplate("body"))
    st.append(PageBreak())  # обложка -> контент

    st.append(Paragraph("ЗА 20–30 МИНУТ ДО СТАРТА", S["kicker"]))
    st.append(Paragraph("Стартовый гайд участника", S["h1"]))
    st.append(Paragraph(
        "Три дня вы будете собирать мини-контент-завод для одного выбранного бизнеса. "
        "Чтобы работать с первой минуты, а не настраивать доступы в эфире, "
        "пройдите короткую подготовку ниже.", S["lead"]))
    st.append(HRFlowable(width="100%", thickness=0.7, color=LINE, spaceBefore=6, spaceAfter=6))

    st.append(Paragraph("Что вы соберёте за три дня", S["h2"]))
    st.append(Paragraph(
        "Не разовые генерации, а систему. Отдельная нейросеть — это станок. "
        "Контент-завод — цех, где станки соединены в линию.", S["body"]))
    factory = [
        ("День 1 · Нейросети и контент",
         "Паспорт бизнеса, портрет аудитории, 20–30 тем, контент-план, сценарии и визуал."),
        ("День 2 · Автоматизация",
         "Первая рабочая цепочка: форма → нейросеть → база → уведомление. Без кода."),
        ("День 3 · ИИ-аватар и видео",
         "Паспорт персонажа, голос, сценарий и первое видео с ИИ-аватаром."),
        ("VIP-день · Сборка завода",
         "Расширенная система, упакованная в услугу с ценой."),
    ]
    rows = [[Paragraph(a, S["cap"]), Paragraph(b, S["body"])] for a, b in factory]
    t = Table(rows, colWidths=[52 * mm, PAGE_W - 2 * MARGIN - 52 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
    ]))
    st.append(t)

    st.append(Paragraph("Шаг 1. Выберите один бизнес", S["h2"]))
    st.append(Paragraph(
        "Весь интенсив построен вокруг одного сквозного проекта. Возьмите бизнес, который "
        "понимаете: свой, знакомого или нишу, в которой уже работали.", S["body"]))
    st.append(Paragraph("Можно выбрать из списка:", S["h3"]))
    st.append(bullets([
        "салон красоты", "стоматология", "ресторан", "агентство недвижимости",
        "онлайн-школа", "эксперт", "строительная компания", "магазин одежды",
        "туристическая компания", "автосервис",
    ]))
    st.append(field("Мой бизнес для интенсива:", 1))

    st.append(Paragraph("Шаг 2. Заведите рабочую папку", S["h2"]))
    st.append(Paragraph(
        "Создайте папку в облаке (Google Диск или аналог). Сюда будете складывать все "
        "материалы трёх дней — к финалу это готовая папка, которую можно показать заказчику.",
        S["body"]))

    st.append(Paragraph("Шаг 3. Проверьте доступы", S["h2"]))
    st.append(Paragraph("Обязательный минимум к Дню 1:", S["h3"]))
    st.append(checklist([
        "Одна текстовая нейросеть: ChatGPT <b>или</b> Claude (выберите одну основную и не меняйте по ходу).",
        "Google Таблицы и Google Документы (или Notion) — будущая база контента.",
        "Установлен Telegram — понадобится для уведомлений и проверки.",
    ]))
    st.append(Paragraph("Понадобится позже (можно подключить по ходу):", S["h3"]))
    st.append(checklist([
        "День 2: Google Формы, аккаунт Make или n8n, Telegram-бот (через @BotFather).",
        "День 3: HeyGen, один генератор изображений, CapCut для монтажа.",
    ]))
    st.append(callout(
        "Не регистрируйтесь во всём сразу",
        "Один основной инструмент, доведённый до автоматизма, сильнее пяти открытых вкладок. "
        "Часть сервисов требует оплаты или иностранной карты — проверьте актуальные условия "
        "и работайте на бесплатных уровнях, где это возможно."))

    st.append(Paragraph("Шаг 4. Настройтесь на практику", S["h2"]))
    st.append(Paragraph(
        "Мы не обещаем лёгких денег и волшебной кнопки. Мы показываем рабочий путь: как "
        "соединить нейросети в процесс, встроить проверку человеком и превратить это в услугу. "
        "Результат будет у тех, кто делает вместе с эфиром.", S["body"]))

    st.append(Paragraph("Три принципа интенсива", S["h3"]))
    st.append(numbered([
        "<b>Практика важнее теории.</b> Каждый блок заканчивается результатом, который вы сохраняете.",
        "<b>Система важнее инструмента.</b> Сервисы меняются, логика конвейера остаётся.",
        "<b>Человек не выходит из процесса.</b> ИИ создаёт, человек проверяет, система публикует после одобрения.",
    ]))

    st.append(callout(
        "Чек-лист готовности к Дню 1",
        "Бизнес выбран · рабочая папка создана · есть доступ к ChatGPT или Claude · "
        "установлен Telegram · готовы Google Таблицы. Если всё отмечено — вы готовы стартовать."))

    st.append(Spacer(1, 6))
    st.append(Paragraph(
        "Полную методичку, рабочую тетрадь и библиотеку промптов вы получаете на интенсиве. "
        "До встречи на первом дне.", S["small"]))
    dm.build(st)
    return path


# ============================================================
# 2. РАБОЧАЯ ТЕТРАДЬ
# ============================================================
def build_workbook():
    path = os.path.join(OUT, "rabochaya-tetrad-avtokontent-2026.pdf")
    dm = DocMaker(path, "Рабочая тетрадь", "Шаблоны и поля для практики трёх дней")
    st = []
    from reportlab.platypus import NextPageTemplate
    st.append(NextPageTemplate("body"))
    st.append(PageBreak())

    st.append(Paragraph("ПРАКТИКА ТРЁХ ДНЕЙ", S["kicker"]))
    st.append(Paragraph("Рабочая тетрадь участника", S["h1"]))
    st.append(Paragraph(
        "Заполняйте поля по своему бизнесу прямо во время интенсива. К финалу тетрадь "
        "превращается в готовую папку материалов для заказчика.", S["lead"]))
    st.append(HRFlowable(width="100%", thickness=0.7, color=LINE, spaceBefore=6, spaceAfter=6))

    # --- ДЕНЬ 1 ---
    st.append(Paragraph("День 1 · Нейросети и производство контента", S["h2"]))

    st.append(Paragraph("Схема контент-завода", S["h3"]))
    st.append(code_block([
        "ДАННЫЕ О БИЗНЕСЕ → АНАЛИЗ → ТЕМЫ → СЦЕНАРИИ →",
        "ВИЗУАЛ → ВИДЕО → АДАПТАЦИЯ → ПРОВЕРКА →",
        "ПУБЛИКАЦИЯ → АНАЛИТИКА",
    ]))
    st.append(Paragraph(
        "Отметьте, где обязателен человек (стратегия, проверка фактов, решение о публикации), "
        "а что можно отдать ИИ (черновики, варианты, адаптация, рутина).", S["small"]))

    st.append(Paragraph("Паспорт бизнеса — анкета-бриф", S["h3"]))
    st.append(Paragraph("Заполните коротко, по одному-двум словам на пункт:", S["small"]))
    brief = [
        "Продукт и услуги", "География работы", "Средний чек",
        "Целевая аудитория (кто платит)", "Основные проблемы клиентов",
        "Преимущества перед конкурентами", "Ограничения (чего не обещаем)",
        "Tone of voice (как говорим)", "Запрещённые темы и слова",
        "Площадки (где публикуемся)", "Цели контента", "Основной призыв к действию",
    ]
    for label in brief:
        st.append(field(label, 1))

    st.append(Paragraph("Портрет аудитории — 5 сильных болей", S["h3"]))
    for i in range(5):
        st.append(field("Боль %d" % (i + 1), 1))

    st.append(Paragraph("Язык аудитории — 5 реальных фраз", S["h3"]))
    for i in range(5):
        st.append(field("Фраза %d" % (i + 1), 1))

    st.append(Paragraph("Недельный контент-план", S["h3"]))
    plan_head = ["День", "Площадка", "Тема", "Роль", "Формат", "Хук", "Статус"]
    widths = [14, 22, 34, 22, 20, 34, 22]
    total = PAGE_W - 2 * MARGIN
    cw = [w / sum(widths) * total for w in widths]
    rows = [[Paragraph(h, ParagraphStyle("th", fontName="Bold", fontSize=8,
            textColor=colors.white)) for h in plan_head]]
    for _ in range(7):
        rows.append(["" for _ in plan_head])
    t = Table(rows, colWidths=cw, rowHeights=[8 * mm] + [11 * mm] * 7)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
    ]))
    st.append(t)
    st.append(Spacer(1, 4))

    st.append(Paragraph("Шесть ролей контента (контент-матрица)", S["h3"]))
    st.append(bullets([
        "Привлечение внимания", "Обучение", "Демонстрация результата",
        "Снятие возражений", "Доверие", "Продажа",
    ]))

    st.append(Paragraph("Шесть формул сценария", S["h3"]))
    st.append(numbered([
        "Ошибка → последствие → решение",
        "До → переломный момент → после",
        "Миф → правда → применение",
        "Вопрос → неожиданный ответ → пример",
        "Проблема → система → результат",
        "Комментарий → реакция → разбор",
    ]))
    st.append(callout(
        "Структура короткого видео",
        "Хук (1–3 сек) → конфликт → раскрытие → доказательство → решение → призыв к действию. "
        "Хук бьёт в боль или ломает ожидание. Один сильный CTA, не два."))

    st.append(Paragraph("Формула визуального промпта", S["h3"]))
    st.append(code_block([
        "ЗАДАЧА + ОБЪЕКТ + СРЕДА + КОМПОЗИЦИЯ + СВЕТ +",
        "СТИЛЬ + КАМЕРА + ФОРМАТ + ОГРАНИЧЕНИЯ",
    ]))
    st.append(Paragraph(
        "Всегда указывайте формат: 9:16 для Reels/Shorts, 4:5 для каруселей и постов.", S["small"]))

    st.append(PageBreak())

    # --- ДЕНЬ 2 ---
    st.append(Paragraph("День 2 · Автоматизация и контент-системы", S["h2"]))
    st.append(Paragraph("Путь новичка", S["h3"]))
    st.append(code_block([
        "Google Формы или Telegram → Google Таблицы → Make →",
        "текстовая нейросеть → Google Документы/Notion →",
        "Telegram для проверки",
    ]))
    st.append(Paragraph("Столбцы таблицы-базы", S["h3"]))
    st.append(code_block([
        "ID | Дата | Бизнес | Продукт | Площадка | Цель |",
        "Тема | Формат | Аудитория | Хук | Сценарий | CTA |",
        "Визуальный промпт | Статус | Ссылка | Комментарий",
    ]))

    st.append(Paragraph("Системный промпт контент-агента (формат ответа)", S["h3"]))
    st.append(code_block([
        "ЗАГОЛОВОК: ...",
        "ХУК: ...",
        "СЦЕНАРИЙ: ...",
        "ОПИСАНИЕ: ...",
        "CTA: ...",
        "ВИЗУАЛЬНЫЙ_ПРОМПТ: ...",
        "МЕТКИ_ПРОВЕРКИ: ...",
    ]))
    st.append(Paragraph(
        "Жёсткий формат ответа нужен, чтобы автоматизация разложила результат по столбцам. "
        "Свободный текст разложить нельзя.", S["small"]))

    st.append(Paragraph("Статусы материала (human in the loop)", S["h3"]))
    st.append(code_block([
        "идея → создано → на проверке → нужно исправить →",
        "одобрено → запланировано → опубликовано",
    ]))
    st.append(Paragraph(
        "Ни один материал не уходит в публикацию, минуя статус «одобрено».", S["small"]))

    st.append(Paragraph("Чек-лист редактора", S["h3"]))
    st.append(checklist([
        "Соответствие бренду и tone of voice", "Нет фактических ошибок",
        "Нет запрещённых обещаний и стоп-слов", "Нет повторов с прошлыми материалами",
        "Текст понятен с первого прочтения", "Сильный хук", "Сильный CTA",
        "Есть реальная польза", "Соответствие площадке", "Нет ощущения шаблонного ИИ-текста",
    ]))
    st.append(field("Моя архитектура: какие модули соберу сейчас, что оставлю на потом", 2))

    st.append(PageBreak())

    # --- ДЕНЬ 3 ---
    st.append(Paragraph("День 3 · ИИ-аватар и мини-видеопродакшн", S["h2"]))
    st.append(Paragraph("Мой тип аватара и обоснование выбора", S["h3"]))
    st.append(field("Тип аватара (стандартный / фотоаватар / цифровой двойник / генерированный / говорящее фото)", 1))
    st.append(field("Почему именно он подходит моему бизнесу", 2))

    st.append(Paragraph("Паспорт персонажа", S["h3"]))
    for label in [
        "Внешность (возраст, лицо, причёска, одежда, фирменные цвета)",
        "Подача (характер, манера речи, эмоции, жесты, запрещённые изменения)",
        "Кадр (фон, свет, дистанция камеры, формат 9:16)",
        "Сценарии использования (где и зачем появляется персонаж)",
    ]:
        st.append(field(label, 2))

    st.append(Paragraph("Сценарий на 30 секунд", S["h3"]))
    st.append(code_block([
        "[0–3 сек]  Хук: короткая фраза, которая бьёт в боль",
        "[3–10]     Проблема: что не так сейчас",
        "[10–20]    Решение: главная мысль, один шаг",
        "[20–27]    Доказательство / пример",
        "[27–30]    CTA: одно короткое действие",
    ]))
    for label in ["Хук", "Проблема", "Решение", "Доказательство", "CTA"]:
        st.append(field(label, 1))

    st.append(Paragraph("Чек-лист готового видео", S["h3"]))
    st.append(checklist([
        "Сильный хук в первые 3 секунды", "Синхронизация губ без рассинхрона",
        "Правильное произношение слов и цифр", "Вставки меняются каждые 2–4 секунды",
        "Нет запрещённых визуальных клише", "Субтитры читаемы, в безопасной зоне",
        "Ровный звук", "Формат 9:16", "Один чёткий CTA", "На телефоне всё смотрится хорошо",
    ]))

    st.append(PageBreak())

    # --- ПОСЛЕ ИНТЕНСИВА ---
    st.append(Paragraph("После интенсива · план на 30 дней", S["h2"]))
    weeks = [
        ("Неделя 1 — фундамент",
         "Довести материалы до чистого вида. Выбрать нишу. Собрать один эталонный кейс."),
        ("Неделя 2 — упаковка",
         "Собрать описание услуги «Старт», подготовить демонстрацию, 2–3 примера для портфолио."),
        ("Неделя 3 — первые касания",
         "Список из 10–15 бизнесов. Индивидуальные заходы через наблюдение. Первые разговоры."),
        ("Неделя 4 — первый проект",
         "Взять клиента на «Старт», выполнить, собрать отзыв и кейс, предложить «Систему»."),
    ]
    rows = [[Paragraph(a, S["cap"]), Paragraph(b, S["body"])] for a, b in weeks]
    t = Table(rows, colWidths=[46 * mm, PAGE_W - 2 * MARGIN - 46 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
    ]))
    st.append(t)
    st.append(callout(
        "Принцип роста",
        "Маленький шаг → результат → рост чека. Не гнаться сразу за большим контрактом. "
        "Нет фиксированных данных о рыночных ценах, доход не гарантируется — считайте от "
        "своего времени и ценности результата."))
    st.append(Spacer(1, 8))
    st.append(Paragraph("© AlovLab · Автоконтент 2026 · t.me/AlovLab", S["small"]))
    dm.build(st)
    return path


if __name__ == "__main__":
    p1 = build_starter_guide()
    p2 = build_workbook()
    for p in (p1, p2):
        print("OK", os.path.relpath(p, ROOT), "%.1f KB" % (os.path.getsize(p) / 1024))
