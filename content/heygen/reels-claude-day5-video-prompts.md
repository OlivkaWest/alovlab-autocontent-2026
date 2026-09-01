# Видео-промпты (Grok) для Reels Дня 5 «Разбор конкурента» — v2, профессиональный пайплайн

> Профи-правда: **Grok (и любой AI-видеогенератор) кириллицу «поедет» и не нарисует пиксельно-точную панель
> Claude.** Поэтому «читабельный русский + оригинальная панель Claude с последними моделями» через сам Grok
> получить нельзя. Правильно разделить труд:
>
> **Grok** = кинематографичная СРЕДА (стол, руки, свет, боке, движение камеры) с **пустым светящимся экраном**.
> **Панель Claude** (русский текст + актуальные модели) = готовый чёткий макет, который ты **накладываешь на
> экран в HeyGen** (screen-replace / overlay). Так текст всегда резкий и читаемый.
>
> Готовые макеты панели (2K, вставляй в HeyGen):
> `content/heygen/screen-inserts/reels-day5/claude-panel-chat.png` — чистый чат (основной)
> `content/heygen/screen-inserts/reels-day5/claude-panel-models.png` — с раскрытым списком моделей (Opus 5 · Sonnet 5 · Haiku 4.5 · Fable 5.1)
> Пересобрать/поправить: `scripts/claude_panel.html` + `scripts/shoot_panel.js`.

---

## ПАЙПЛАЙН на каждую экранную сцену

1. В Grok генеришь клип СРЕДЫ (ноутбук на тёмном столе, тёплый свет), экран — **чистая светящаяся поверхность без текста**.
2. В HeyGen кладёшь поверх экрана мой PNG-макет Claude (подгоняешь по углам экрана — corner-pin / screen replace).
3. Оживляешь макет в HeyGen: лёгкий зум/скролл/пошаговое проявление строк (оффер→…→гэпы), мигающий курсор уже есть на макете.
4. Русский на макете уже чёткий — ничего дорисовывать в Grok не нужно.

---

## КЛИП 1 — сцена 2 (3–9 сек) · копируешь ссылку конкурента

**Grok prompt (EN):**
```
Vertical 9:16 cinematic macro video, 5 seconds. A smartphone on a dark graphite desk in warm amber light,
a hand places it down. The phone screen glows softly with a neutral browser shape but NO readable text,
a bright empty highlight bar where a link would be. Shallow depth of field, warm reflections, slow push-in,
50mm look, photoreal, film grain, moody premium. No people faces, no logos, no on-screen text.
```
**В HeyGen:** на подсвеченную строку наложи маленький оверлей-ссылку (лат. буквы норм) или оставь как есть; титр «ссылка → разбор».

---

## КЛИП 2 — сцена 4 (14–27 сек) · Claude строит разбор  ⭐ главный

**Grok prompt (EN) — только среда, экран пустой:**
```
Vertical 9:16 cinematic macro video, 6-8 seconds. An open laptop on a dark graphite desk, warm amber lamp
light, keyboard bokeh in the foreground, gentle steam from a mug at the edge. The laptop screen is a clean
bright glowing surface with NO text and NO interface — just an even warm-white glow ready for a screen
overlay. Slow cinematic push-in toward the screen, shallow depth of field, 35mm look, photoreal, film grain,
premium tech still-life. No people, no logos, no readable text on screen.
```
**В HeyGen:**
- Наложи `claude-panel-chat.png` на экран (corner-pin по углам дисплея).
- Оживи: строки ОФФЕР → АУДИТОРИЯ → ХУКИ → ВОРОНКА → ГЭПЫ проявляются по одной (fade/slide), курсор на «Гэпы» уже мигает.
- Хочешь подчеркнуть свежие модели — на 1–2 сек подмени на `claude-panel-models.png` (виден список Opus 5 / Sonnet 5 / Haiku 4.5 / Fable 5.1), потом обратно на чат.
- Субтитры OFF (панель читается сама).

---

## КЛИП 3 — сцена 5 (27–31 сек) · подсветка «гэпов»

**Grok prompt (EN) — среда:**
```
Vertical 9:16 cinematic macro video, 4 seconds. Same laptop and desk, warm amber light intensifies slightly,
the bright glowing screen surface stays clean with NO text, a subtle warm bloom grows from the lower part of
the screen. Very slow camera settle, shallow depth of field, photoreal, film grain, hopeful confident mood.
No people, no logos, no readable text.
```
**В HeyGen:** оставь на экране ту же панель Claude, сделай **зум/пуш на строку «ГЭПЫ»** (она уже подсвечена оранжевым) — акцент «его дыры → твой ход». Титр можно не ставить, строка читается.

---

## Общие настройки Grok (все клипы)

- **Aspect:** 9:16 vertical.
- **Экран — ВСЕГДА пустой светящийся** (без текста и без UI): текст добавляем макетом в HeyGen.
- **Стиль-хвост:** `cinematic, dark graphite and warm amber, photoreal, film grain, shallow depth of field, 35–50mm, premium, no people, no logos, no on-screen text`.
- **Движение:** медленный push-in / settle — премиум, не дёрганый.

## Почему так (профи-обоснование)

- Читаемость: нативно сгенерированный AI-текст на кириллице почти всегда кривой → на паузе видно брак. Оверлей-макет = резко и правильно.
- Достоверность: панель Claude — реальный интерфейс с актуальными моделями (Opus 5 / Sonnet 5 / Haiku 4.5 / Fable 5.1), а не «нечто похожее».
- Контроль: можешь в любой момент поменять текст разбора/модель в `scripts/claude_panel.html` и перерендерить, не трогая видео.

## Honesty

Разбор на панели — учебный шаблон метода (оффер/аудитория/хуки/воронка/гэпы), без выдуманных цифр о конкретном конкуренте. Показываем реальный Claude. Модели названы точно.
