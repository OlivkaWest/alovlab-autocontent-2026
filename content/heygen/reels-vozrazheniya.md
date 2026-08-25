# HeyGen — Reels Дня 23 (26.08) «„Дорого" — это не про деньги»

Рубрика: «ИИ сделал сам» (метод на глазах). Формат: Reels 9:16, ~33 сек.
Аватар: НЕЙРОМОНАХ. Голос: доктор Нейро · русский. Инструмент: **Claude**.
Выход воронки: **B2C** — лид-магнит (разбор возражений + промпт) **в комментариях под постом (TG + ВК)** → курс.
Хук: **«„Дорого" — это почти никогда не про деньги.»**
Метод в кадре: за возражением прячется настоящая причина — «не верю, что мне поможет».
В озвучке — «Клод»; титром — «Claude». Показываешь Claude — реальный интерфейс Anthropic.
Связка: продолжает День 21 «Карта состояний» (шаг «убеждения/возражения»).

> **CTA-правило (с 26.08):** контент идёт И в Telegram, И в ВК → CTA нейтральный:
> «забирай в комментариях под постом», НЕ «переходи в Telegram / в профиль».

> **HeyGen build instruction (обязательно, дословно):**
> “Generate all non-avatar scenes with Seedance inside HeyGen. Do not use static overlays,
> screenshots or slideshow-style animation.”

---

## 1. Сценарий (таблица · с разметкой сцен)

| Таймкод | Тип | Текст аватара | Визуал (действие) | Текст на экране | Субтитры |
|---|---|---|---|---|---|
| 0–2 | avatar | «Дорого» — это почти никогда не про деньги. | лицо крупно, глаза в камеру, пауза | не про **деньги** | ON |
| 2–8 | non_avatar (Seedance) | Когда человек пишет «дорого», он думает: «не верю, что мне это поможет». | телефон: в директе печатается «а сколько стоит?» → «дороговато» → стирается | что он **думает** | ON |
| 8–12 | avatar | Ответишь про цену — потеряешь его. Отвечай на настоящую причину. | средний план, лёгкий разворот | не цена — **причина** | ON |
| 12–25 | non_avatar (Seedance) | Прошу Клода разложить возражение: что говорят, что на самом деле, чем снять. | скринкаст Claude: печатается промпт → построчно выезжает разбор в 3 строки | что говорят → что за этим → **чем снять** | OFF |
| 25–30 | non_avatar (Seedance) | Бьёшь в настоящую причину — и «дорого» рассыпается. | слово «ДОРОГО» на тёмном фоне трескается и осыпается, из-под него тёплый свет | «дорого» **рассыпается** | ON |
| 30–33 | avatar | Разбор возражений и промпт — в комментариях под постом. Забирай. | лицо + логотип A | гайд ↓ **в комментариях** | ON |

---

## 2. Чистый текст для HeyGen (поле «Сценарий» / реплики аватара)

> «Дорого» — это почти никогда не про деньги.
>
> Когда человек пишет «дорого», он думает: «не верю, что мне это поможет».
>
> Ответишь про цену — потеряешь его. Отвечай на настоящую причину.
>
> Прошу Клода разложить возражение: что говорят, что на самом деле, чем снять.
>
> Бьёшь в настоящую причину — и «дорого» рассыпается.
>
> Разбор возражений и промпт — в комментариях под постом. Забирай.

---

## 3. Режиссёрские указания

- Формат 9:16, 32–33 сек. Аватар НЕЙРОМОНАХ, голос доктор Нейро.
- Тон: спокойный наставник, лёгкая усмешка на «рассыпается». Без давления.
- Паузы: держать после «не про деньги» и после «настоящую причину».
- **avatar_scene:** 0–2, 8–12, 30–33 — лицо чистое, никакой UI/текст не перекрывает лицо, глаза, рот.
- **non_avatar_scene (Seedance):** 2–8, 12–25, 25–30 — оживают ВНУТРИ устройства/сцены. Не статик, не скриншот, не overlay, не slideshow, не зум.
- Ключевой приём: зритель ВИДИТ, как Клод раскладывает возражение — метод на глазах.
- Тёплый свет нарастает к финалу.

---

## 4. B-roll · Seedance-сцены (по одной на non_avatar)

**S1 (2–8) — «сообщение „дорого"»**
`Cinematic macro of a smartphone on a dark desk, a direct-message chat where a message is being typed live: "а сколько стоит?" then "дороговато…", the text cursor blinking and the message being deleted, warm screen glow, shallow depth of field, photoreal, film grain. UI animates inside the phone. No overlays, no people.`

**S2 (12–25) — Claude раскладывает возражение**
`Macro of a laptop screen showing the Claude (Anthropic) interface: a prompt is typed live, then the answer appears line by line as a 3-row breakdown, each row highlighting in warm amber one at a time, cursor moving, warm screen glow on a dark desk, keyboard bokeh, photoreal, film grain. Everything animates inside the screen. No static overlays.`

**S3 (25–30) — «ДОРОГО» рассыпается**
`The word "ДОРОГО" carved in dark stone on a black background cracks and crumbles into dust, warm amber light breaking through the cracks from underneath, cinematic slow motion, dramatic lighting, photoreal, film grain. No people, no other text.`

---

## 5. Готовый промпт для показа (и для лид-магнита)

```
Возьми возражение «[ЧТО ГОВОРЯТ, напр. дорого]» под нишу [ТВОЯ].
Разложи: (1) как звучит вслух; (2) что на самом деле за этим стоит;
(3) чем это снять — без спора о цене и без давления.
Дай короткий ответ, который бьёт в настоящую причину.
```

---

## 6. Субтитры (карта ON/OFF)

| Таймкод | Субтитры |
|---|---|
| 0–12 | ON (ударные слова) |
| 12–25 | **OFF** (в кадре читаемый разбор на экране Claude) |
| 25–33 | ON (короткий + CTA) |

Ключевые слова: `не про деньги` → `что он думает` → `не цена — причина` → `чем снять` → `рассыпается` → `в комментариях ↓`.

---

## 7. Три заголовка на обложку

1. «„Дорого" — это не про деньги»
2. «Отвечаешь на цену — теряешь клиента»
3. «Клод разбирает возражение „дорого"»

---

## 8. Описание публикации (~360 знаков · для TG и ВК)

> «Дорого» — это почти никогда не про деньги.
>
> Когда человек пишет «дороговато», он на самом деле думает: «не верю, что мне это поможет». Ответишь про цену или дашь скидку — потеряешь его. Показываю, как Клод раскладывает любое возражение: что говорят → что за этим на самом деле → чем снять, без спора о цене.
>
> Разбор возражений и готовый промпт — в комментариях под этим постом. Забирай.

---

## 9. Финальный CTA

Голос: «Разбор возражений и промпт — в комментариях под постом. Забирай.»
Механика: лид-магнит (разбор «дорого / подумаю / не получится» + промпт) закреплён в комментариях
под постом в Telegram и в ВК. Выход воронки — курс.

═══════════════════════════════════════════════════════════════════
## 10. ГОТОВЫЙ БРИФ ДЛЯ HEYGEN-АГЕНТА (копируй целиком)
═══════════════════════════════════════════════════════════════════

**Настройки:** Aspect 9:16 (vertical) · Length ~33s · Avatar: НЕЙРОМОНАХ · Voice: доктор Нейро (Russian) ·
Subtitles: burned-in, bottom, bold (кроме сцены 4 — OFF) · Style: cinematic, dark graphite + warm amber.

**Instruction to the agent (paste as-is):**
Create a 33-second vertical (9:16) Russian Reel with avatar НЕЙРОМОНАХ (voice: доктор Нейро). Alternate
talking-head avatar scenes with B-roll scenes. **Generate all non-avatar scenes with Seedance inside
HeyGen. Do not use static overlays, screenshots or slideshow-style animation.** On avatar scenes, keep
the face clear — no text or UI over the face, eyes or mouth. On the Claude-screen scene, turn burned-in
subtitles OFF (there is readable text in frame). Warm light grows toward the end.

**SCENE 1 — AVATAR (0–2s)**
Avatar says: «Дорого — это почти никогда не про деньги.»
Framing: close-up, eyes to camera, hold a beat. On-screen word: «не про деньги».

**SCENE 2 — B-ROLL / SEEDANCE (2–8s)**
Voiceover (avatar audio over B-roll): «Когда человек пишет „дорого", он думает: „не верю, что мне это поможет".»
Seedance: Cinematic macro of a smartphone on a dark desk, a direct-message chat typing live "а сколько
стоит?" then "дороговато…", cursor blinking, message being deleted, warm screen glow, shallow depth of
field, photoreal, film grain, UI animates inside the phone, no people.

**SCENE 3 — AVATAR (8–12s)**
Avatar says: «Ответишь про цену — потеряешь его. Отвечай на настоящую причину.»
Framing: medium, slight turn. On-screen word: «не цена — причина».

**SCENE 4 — B-ROLL / SEEDANCE (12–25s) · SUBTITLES OFF**
Voiceover: «Прошу Клода разложить возражение: что говорят, что на самом деле, чем снять.»
Seedance: Macro of a laptop screen showing the Claude (Anthropic) interface; a prompt is typed live, then
the answer appears line by line as a 3-row breakdown, each row highlighting in warm amber one at a time,
cursor moving, warm screen glow, keyboard bokeh, photoreal, film grain, everything animates inside the
screen, no static overlays.

**SCENE 5 — B-ROLL / SEEDANCE (25–30s)**
Voiceover: «Бьёшь в настоящую причину — и „дорого" рассыпается.»
Seedance: The word "ДОРОГО" carved in dark stone on a black background cracks and crumbles into dust,
warm amber light breaking through the cracks, cinematic slow motion, photoreal, film grain, no people.

**SCENE 6 — AVATAR (30–33s)**
Avatar says: «Разбор возражений и промпт — в комментариях под постом. Забирай.»
Framing: close-up + AlovLab logo (orange A). On-screen text: «гайд ↓ в комментариях».

**Full narration (for the voice track, in order):**
«Дорого — это почти никогда не про деньги. Когда человек пишет „дорого", он думает: „не верю, что мне
это поможет". Ответишь про цену — потеряешь его. Отвечай на настоящую причину. Прошу Клода разложить
возражение: что говорят, что на самом деле, чем снять. Бьёшь в настоящую причину — и „дорого"
рассыпается. Разбор возражений и промпт — в комментариях под постом. Забирай.»

═══════════════════════════════════════════════════════════════════

> Честность: реплики — брендовый копирайт; примеры возражений — учебные, без выдуманных цифр и кейсов;
> никаких «скидок» и фейкового дефицита. Показываешь Claude — актуальный интерфейс Anthropic.
> Лид-магнит — в комментариях под постом (TG + ВК).
> **Проверка перед финалом:** если non_avatar-сцена выглядит как слайд/картинка/overlay — брак,
> перегенерировать через Seedance.
