# HeyGen — Reels Дня 23 (26.08) «Клиент написал „дорого"» — v2 (пересборка)

Рубрика: «ИИ сделал сам» (метод на глазах). Формат: Reels 9:16, ~34 сек.
Аватар: НЕЙРОМОНАХ. Голос: доктор Нейро · русский. Инструмент: **Claude**.
Выход воронки: **B2C** — лид-магнит (5 возражений разобраны + промпт) **в комментариях под постом (TG + ВК)** → курс.
Хук: **«Клиент написал „дорого". Ответишь про цену — ты уже проиграл.»**
Крадущаяся техника (то, ради чего сохраняют): **любое возражение = 3 вопроса** —
как звучит → что на самом деле → чем снять. Отвечай на страх под ценой, а не на цену.
В озвучке — «Клод»; титром — «Claude». Показываешь Claude — реальный интерфейс Anthropic.
Связка: продолжает День 21 «Карта состояний» (шаг «убеждения/возражения»).

> **CTA-правило (с 26.08):** контент в Telegram И в ВК → CTA нейтральный: «в комментариях под постом».
> **HeyGen build instruction (дословно):** “Generate all non-avatar scenes with Seedance inside HeyGen.
> Do not use static overlays, screenshots or slideshow-style animation.”

---

## 1. Сценарий (таблица · разметка сцен)

| Таймкод | Тип | Текст аватара | Визуал (действие) | Текст на экране | Субтитры |
|---|---|---|---|---|---|
| 0–3 | avatar | Клиент написал «дорого». Ответишь про цену — ты уже проиграл. | лицо крупно, в упор, пауза после «проиграл» | уже **проиграл** | ON |
| 3–8 | non_avatar (Seedance) | «Дорого» — это не про деньги. Это «а мне точно поможет?». | телефон: в директе печатается «дороговато…», курсор мигает | не про **деньги** | ON |
| 8–13 | avatar | Не защищай цену. Отвечай на страх под ней. Любое возражение — это три вопроса. | средний план, лёгкий наклон вперёд | страх под **ценой** | ON |
| 13–26 | non_avatar (Seedance) | Прошу Клода разложить: как звучит, что на самом деле, чем снять — без спора о цене. | скринкаст Claude: печатается промпт → построчно появляются 3 строки, каждая подсвечивается | как звучит · что на самом деле · **чем снять** | OFF |
| 26–31 | non_avatar (Seedance) | Отвечаешь на страх — и «дорого» превращается в «а как оплатить». | телефон: приходит спокойный ответ → клиент печатает «а как записаться?» | «дорого» → **«как оплатить»** | ON |
| 31–34 | avatar | Разбор пяти возражений и промпт — в комментариях под постом. Забирай. | лицо + логотип A | гайд ↓ **в комментариях** | ON |

---

## 2. Чистый текст для HeyGen (реплики аватара, по порядку)

> Клиент написал «дорого». Ответишь про цену — ты уже проиграл.
>
> «Дорого» — это не про деньги. Это «а мне точно поможет?».
>
> Не защищай цену. Отвечай на страх под ней. Любое возражение — это три вопроса.
>
> Прошу Клода разложить: как звучит, что на самом деле, чем снять — без спора о цене.
>
> Отвечаешь на страх — и «дорого» превращается в «а как оплатить».
>
> Разбор пяти возражений и промпт — в комментариях под постом. Забирай.

---

## 3. Режиссёрские указания

- Формат 9:16, 33–34 сек. Аватар НЕЙРОМОНАХ, голос доктор Нейро.
- Тон: спокойный, уверенный, лёгкая усмешка на «как оплатить». Без давления.
- Паузы: держать после «ты уже проиграл» и после «три вопроса».
- **avatar_scene:** 0–3, 8–13, 31–34 — лицо чистое, никакой UI/текст не перекрывает лицо, глаза, рот.
- **non_avatar_scene (Seedance):** 3–8, 13–26, 26–31 — всё оживает ВНУТРИ устройства. Не статик, не скриншот, не overlay, не slideshow, не зум.
- Ключевой приём: зритель видит **и метод (3 строки на экране), и результат (клиент меняет тон)** — не абстракция.
- Тёплый свет нарастает к финалу.

---

## 4. B-roll · Seedance-сцены

**S1 (3–8) — сообщение «дороговато»**
`Cinematic macro of a smartphone on a dark desk, a direct-message chat where a customer types live "дороговато…", the text cursor blinking, warm screen glow, shallow depth of field, photoreal, film grain. UI animates inside the phone. No overlays, no people.`

**S2 (13–26) — Claude раскладывает возражение на 3 строки**
`Macro of a laptop screen showing the Claude (Anthropic) interface: a prompt is typed live, then the answer builds line by line as three rows — "как звучит", "что на самом деле", "чем снять" — each row lighting up in warm amber one at a time, cursor moving, warm screen glow on a dark desk, keyboard bokeh, photoreal, film grain. Everything animates inside the screen. No static overlays.`

**S3 (26–31) — клиент меняет тон**
`Cinematic macro of the same smartphone chat: a calm helpful reply appears, then the customer starts typing "а как записаться?", warm brightening screen glow, hopeful mood, shallow depth of field, photoreal, film grain. UI animates inside the phone. No people, no other text.`

---

## 5. Готовый промпт (показать в кадре + положить в лид-магнит)

```
Возьми возражение «[ЧТО ГОВОРЯТ, напр. дорого]» под нишу [ТВОЯ].
Разложи на 3 вопроса:
1) как звучит вслух;
2) что за этим на самом деле (какой страх);
3) чем это снять — без спора о цене и без давления.
Дай короткий ответ, который бьёт в страх, а не в цену.
```

---

## 6. Субтитры (карта ON/OFF)

| Таймкод | Субтитры |
|---|---|
| 0–13 | ON (ударные слова) |
| 13–26 | **OFF** (на экране читаемые 3 строки Claude) |
| 26–34 | ON (короткий + CTA) |

Ключевые: `уже проиграл` → `не про деньги` → `страх под ценой` → `как звучит · что на самом деле · чем снять` → `«как оплатить»` → `в комментариях ↓`.

---

## 7. Три заголовка на обложку

1. «Клиент написал „дорого"? Ты уже проиграл»
2. «Отвечаешь на цену — теряешь клиента»
3. «Любое возражение = 3 вопроса»

---

## 8. Описание публикации (~360 знаков · TG и ВК)

> Клиент написал «дорого» — и ты уже проиграл, если начал оправдывать цену.
>
> «Дорого» — это почти никогда не про деньги. Это «а мне точно поможет?». Отвечать надо на страх, а не на цену. Показываю приём: любое возражение раскладываешь с Клодом на 3 вопроса — как звучит, что за этим на самом деле, чем снять. И «дорого» превращается в «а как оплатить».
>
> Разбор 5 возражений и готовый промпт — в комментариях под этим постом. Забирай.

---

## 9. Финальный CTA

Голос: «Разбор пяти возражений и промпт — в комментариях под постом. Забирай.»
Механика: лид-магнит (5 частых возражений разобраны по 3 вопросам + промпт) закреплён в комментариях
под постом в Telegram и в ВК. Выход воронки — курс.

═══════════════════════════════════════════════════════════════════
## 10. ГОТОВЫЙ БРИФ ДЛЯ HEYGEN-АГЕНТА (копируй целиком)
═══════════════════════════════════════════════════════════════════

**Настройки:** Aspect 9:16 (vertical) · Length ~34s · Avatar: НЕЙРОМОНАХ · Voice: доктор Нейро (Russian) ·
Subtitles: burned-in, bottom, bold (OFF на сцене 4) · Style: cinematic, dark graphite + warm amber.

**Instruction to the agent (paste as-is):**
Create a 34-second vertical (9:16) Russian Reel with avatar НЕЙРОМОНАХ (voice: доктор Нейро). Alternate
talking-head avatar scenes with B-roll scenes. **Generate all non-avatar scenes with Seedance inside
HeyGen. Do not use static overlays, screenshots or slideshow-style animation.** On avatar scenes keep the
face clear — no text or UI over the face, eyes or mouth. On the Claude-screen scene turn burned-in
subtitles OFF (readable text is in frame). Warm light grows toward the end.

**SCENE 1 — AVATAR (0–3s)**
Says: «Клиент написал „дорого". Ответишь про цену — ты уже проиграл.»
Close-up, eyes to camera, hold a beat after «проиграл». On-screen: «уже проиграл».

**SCENE 2 — B-ROLL / SEEDANCE (3–8s)**
Voiceover: «„Дорого" — это не про деньги. Это „а мне точно поможет?".»
Seedance: Cinematic macro of a smartphone on a dark desk, a chat where a customer types live "дороговато…",
cursor blinking, warm screen glow, shallow depth of field, photoreal, film grain, UI inside the phone, no people.

**SCENE 3 — AVATAR (8–13s)**
Says: «Не защищай цену. Отвечай на страх под ней. Любое возражение — это три вопроса.»
Medium, slight lean-in. On-screen: «страх под ценой».

**SCENE 4 — B-ROLL / SEEDANCE (13–26s) · SUBTITLES OFF**
Voiceover: «Прошу Клода разложить: как звучит, что на самом деле, чем снять — без спора о цене.»
Seedance: Macro of a laptop screen with the Claude (Anthropic) interface; a prompt is typed live, then the
answer builds line by line as three rows — "как звучит", "что на самом деле", "чем снять" — each lighting up
in warm amber one at a time, cursor moving, warm screen glow, keyboard bokeh, photoreal, film grain,
everything inside the screen, no static overlays.

**SCENE 5 — B-ROLL / SEEDANCE (26–31s)**
Voiceover: «Отвечаешь на страх — и „дорого" превращается в „а как оплатить".»
Seedance: Cinematic macro of the same phone chat: a calm helpful reply appears, then the customer starts
typing "а как записаться?", warm brightening glow, hopeful mood, photoreal, film grain, UI inside the phone, no people.

**SCENE 6 — AVATAR (31–34s)**
Says: «Разбор пяти возражений и промпт — в комментариях под постом. Забирай.»
Close-up + AlovLab logo (orange A). On-screen: «гайд ↓ в комментариях».

**Full narration (voice track, in order):**
«Клиент написал „дорого". Ответишь про цену — ты уже проиграл. „Дорого" — это не про деньги. Это „а мне
точно поможет?". Не защищай цену. Отвечай на страх под ней. Любое возражение — это три вопроса. Прошу
Клода разложить: как звучит, что на самом деле, чем снять — без спора о цене. Отвечаешь на страх — и
„дорого" превращается в „а как оплатить". Разбор пяти возражений и промпт — в комментариях под постом. Забирай.»

═══════════════════════════════════════════════════════════════════

> Честность: реплики — брендовый копирайт; примеры возражений — учебные, без выдуманных цифр и кейсов;
> никаких «скидок» и фейкового дефицита. Показываешь Claude — актуальный интерфейс Anthropic.
> Лид-магнит — в комментариях под постом (TG + ВК).
> **Проверка:** если non_avatar-сцена выглядит как слайд/картинка/overlay — брак, перегенерировать через Seedance.
