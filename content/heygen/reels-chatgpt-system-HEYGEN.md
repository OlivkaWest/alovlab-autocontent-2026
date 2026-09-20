# REELS · «Отдай свой Instagram ChatGPT» — премиум HeyGen (оживлённая карусель) · 20.09

> Профессиональный расклад под HeyGen Video Agent + Seedance. Тема = карусель `exports/carousels/chatgpt-system/`.
> Идея визуала: слайды карусели ОЖИВАЮТ (наслоение/parallax), аватар Ильи ведёт хук/мысль/CTA.
> ПОДКЛЮЧЕНО (методология из репо): CLAUDE.md Прил. Г (avatar/Seedance) · GLOBAL-REELS-VOICE (без тире) ·
> GLOBAL-CONTENT-DELIVERY · TELEGRAM-FUNNEL-CTA · эталон `content/carousels/restaurant/hero-reel-heygen.md` ·
> заметка PROGRESS: кириллицу рендерит Grok / либо анимируем готовые слайды-PNG (текст уже точный).

## SCORE (0–10)
hook 9 · curiosity 9 · search 9 · mass 9 · save 10 · share 9 · novelty 8 · authority 10 · follow 9 · business 9 → ~9.0/10 → в production.

## CORE IDEA
Не «напиши пост», а система: контекст + команда. 4 команды из карусели оживают на экране, Илья объясняет метод. Финал → Telegram за методичкой.

## HOOK (0–2 сек)
«Хватит просить ChatGPT просто написать пост.»

## FINAL VOICEOVER TEXT (для HeyGen, БЕЗ тире, одна мысль = одно предложение)
Хватит просить ChatGPT просто написать пост.
Так он никогда не станет твоим стратегом.
Я сделал иначе. Я отдал ему весь свой контент.
Сначала гружу контекст о себе и аудитории.
А потом запускаю задачу одной командой.
Одна команда собирает карту аудитории.
Вторая превращает её проблему в лид-магнит.
Третья раскладывает одну мысль на Reels, карусель и пост.
Четвёртая строит путь от просмотра до заявки.
Это уже не промпты. Это система.
Все команды и методичку забирай в Telegram, ссылка в шапке профиля.

---

## HeyGen VIDEO AGENT · НАСТРОЙКИ (как на экране)
- Длительность: **35 sec** (можно 30, тогда режем середину до 3 команд).
- **Seedance: Вкл.**
- Аватар: **НЕЙРОМОНАХ (Илья)**.
- Голос: **доктор Нейро** · язык русский.
- Формат: **9:16, 1080×1920**.
- **Вложения для Seedance (image-to-video):** готовые слайды карусели
  `exports/carousels/chatgpt-system/slide-01…07.png` — оживляем ИХ, текст на них уже идеальный.

## Поле «Сценарий» (это озвучка — вставить FINAL VOICEOVER выше, дословно)

## Поле «Инструкции» (управляет Seedance b-roll и аватаром — вставить дословно)
```
Style: premium, dark, warm orange accent, cinematic depth, 9:16.
Avatar НЕЙРОМОНАХ appears on the hook, on the two key thoughts and on the final CTA.
Between avatar scenes, animate the ATTACHED carousel slides as b-roll (image-to-video):
keep every slide's existing text sharp and unchanged, add only subtle motion —
slow parallax push-in on the phone mockup, gentle float, staggered reveal of the chat bubbles
and checklist items, soft light bloom. Layer the slide elements for depth (background, phone, text).
Generate all non-avatar scenes with Seedance inside HeyGen. Do not use static overlays,
screenshots or slideshow-style animation. Do not regenerate or distort the Russian text on the slides.
Subtitles bottom, large, white, key word in orange. Logo only on the final scene.
```

## SCENE MAP (аватар / оживлённый слайд / Grok)
- S1 non_avatar (Seedance i2v: **slide-01**): обложка оживает — Илья на фото + заголовок «Отдай свой Instagram ChatGPT» наслаиваются, медленный push-in.
- S2 avatar: хук.
- S3 non_avatar (Seedance i2v: **slide-02**): провокация — мокап «напиши пост / дай 30 идей», затем всплывает «контекст + команда».
- S4 avatar: «я отдал ему весь контент… контекст, потом команда».
- S5 non_avatar (Seedance i2v: **slide-03 → 04 → 05 → 06**): 4 команды листаются с наслоением, чек-листы появляются построчно (/contentmix, /audiencemap, /leadidea, /funnelmap).
- S6 avatar: «это уже не промпты, это система».
- S7 non_avatar (Seedance i2v: **slide-07** ИЛИ Grok-сцена «система собирается»): финал.
- S8 avatar: CTA → Telegram.

## АВАТАР-СЦЕНЫ (реплики; лицо чистое, текст не перекрывает)
- S2: «Хватит просить ChatGPT просто написать пост. Так он не станет твоим стратегом.»
- S4: «Я отдал ему весь свой контент. Сначала контекст о себе и аудитории. Потом задача одной командой.»
- S6: «Одна команда — карта аудитории. Другая — лид-магнит. Третья — форматы. Четвёртая — воронка. Это уже система.»
- S8: «Все команды и методичку забирай в Telegram. Ссылка в шапке профиля.»

## РАСКАДРОВКА (как ляжет 35 сек)
| Сек | Голос | Кадр | Текст на экране |
|---|---|---|---|
| 0–3 | (хук на аватаре) | S1 обложка оживает → S2 аватар | «напиши пост» = **вода** |
| 3–9 | так он не станет стратегом / я отдал ему весь контент | S3 провокация оживает | контекст + **команда** |
| 9–14 | сначала контекст, потом команда | S4 аватар | не промпт, а **задача** |
| 14–26 | 4 команды подряд | S5 команды листаются, чек-листы появляются | /audiencemap · /leadidea · /contentmix · /funnelmap |
| 26–30 | это уже не промпты, это система | S6 аватар | это **система** |
| 30–35 | забирай в Telegram | S7 финал → S8 аватар + лого | команды → **Telegram** |

## SEEDANCE image-to-video (для оживления слайдов; вложить PNG слайда как старт-кадр)
> Одна лёгкая анимация на слайд, текст НЕ трогаем. Настройки: 9:16, ~3–5 сек, motion слабый-средний, тёплый грейд.
- **slide-01 (обложка):** slow push-in on the portrait, subtle parallax between Ilya and the headline, soft warm light bloom. Keep all text sharp.
- **slide-02 (провокация):** the phone mockup floats, the three grey chat bubbles reveal one by one, a soft orange underline draws under «конкретную задачу командой».
- **slide-03…06 (команды):** gentle parallax push-in on the phone, the ChatGPT answer scrolls slightly, checklist items appear staggered, the `/команда` chip glows. One slide = one clip.
- **slide-07 (финал):** slow push-in on Ilya, the orange «ПИШИ НЕЙРО» button pulses once, downward arrow bounces subtly.
Negative for all: no new text, no distorted letters, no watermark, no face distortion.

## GROK — ПОЛНОСТЬЮ СГЕНЕРЁННЫЕ КАДРЫ (если хочешь видео вместо анимации PNG; кириллица вшита)
> Grok рендерит русский → эти сцены можно генерить с нуля. 9:16, ~5 сек, тёмный премиум, тёплый оранж.
**G-hook · команда печатается**
Vertical 9:16, 5s. A premium smartphone floating in dark space with warm orange rim light, ChatGPT open. A Russian command types into the field: «/audiencemap», then the screen fills with a neat structured answer with headings «Проблемы», «Желания», «Вопросы». Slow push-in, cinematic, crisp readable Russian. No watermark, no gibberish.
**G-system · 4 команды сходятся в систему**
Vertical 9:16, 5s. Four glowing orange command chips «/audiencemap», «/leadidea», «/contentmix», «/funnelmap» float in dark premium space and connect with light lines into one system diagram. Cinematic, warm accent, readable Russian labels. No watermark, no gibberish.
**G-final · телефон с готовой системой**
Vertical 9:16, 5s. A phone on a dark desk, warm rim light, screen shows a tidy content system dashboard in Russian, slow push-in. Premium, photoreal. No watermark, no gibberish.

## МОНТАЖ · ПРЕМИУМ-НАСЛОЕНИЕ (layered look)
- **Наслоение слайдов:** каждый слайд разбираем на слои (фон · телефон · заголовок · чек-лист) и даём им лёгкий parallax-сдвиг + сдвинутое по времени появление → глубина, «дорого».
- **Переходы:** слайд уходит лёгким push + blur, следующий наезжает из глубины. Без кислотных глитчей.
- **Ритм:** склейки в бит, команды листаются быстро (по ~2–3 сек), хук и финал держим на аватаре.
- **Свет:** мягкое оранжевое свечение на переходах, единый тёплый грейд на весь ролик.
- **Субтитры:** снизу, крупные, ключевое слово оранжевым; на слайдах с UI субтитры в safe-zone.
- **Музыка:** спокойный премиум-электрон, нарастание к финалу.

## ON SCREEN TEXT
S1 «Отдай Instagram ChatGPT» · S2 «Хватит просто "напиши пост"» · S3 «Контекст + команда» · S4 «Не промпт, а задача» ·
S5 «/audiencemap /leadidea /contentmix /funnelmap» · S6 «Это система» · S7-8 «Команды + методичка → Telegram (ссылка в профиле)».

## CTA (→ Telegram)
Голос/финал: «Все команды и методичку забирай в Telegram, ссылка в шапке профиля».
On-screen: «17 команд + методичка → Telegram». Ссылка: IG шапка · VK закреп/коммент · TG закреп.
Keyword-механика: «Пиши НЕЙРО» в комментах → автo-ответ со ссылкой в Telegram. B2B: контент-система под бренд → бриф @alovlab.

## DESCRIPTION (Reels-подпись, голос Ильи)
Хватит просить ChatGPT просто написать пост.
Я отдал ему весь свой контент. Сначала контекст о себе и аудитории, потом задача одной командой. Так рождается система, а не разовые посты.
17 таких команд и методичку забирай бесплатно: пиши «НЕЙРО» в комментариях, пришлю доступ в Telegram.

## HASHTAGS
#нейросети #chatgpt #контентплан #smm #ии #нейросеть #промпты #контентмаркетинг #reels #alovlab

## COVER
Тёмный кадр: Илья + телефон с ChatGPT, где вводится команда, тёплый оранж. Верх: «ОТДАЙ INSTAGRAM CHATGPT», низ (оранжевым): «4 КОМАНДЫ = СИСТЕМА».

## HeyGen-CHECK
[x] в озвучке нет тире · [x] одна мысль = одно предложение · [x] хук как начало истории · [x] не-аватар сцены = Seedance i2v (оживление слайдов) или Grok, не статикой · [x] русский текст на слайдах НЕ регенерим (остаётся точным) · [x] на аватаре текст не перекрывает лицо · [x] субтитры в safe-zone на UI · [x] CTA = переход в Telegram.
