# Видео-промпты (Grok) для Reels Дня 5 «Разбор конкурента» — только B-roll (не-аватарные сцены)

> Эти 3 клипа генеришь в Grok (видео) и вставляешь в HeyGen-студию на места non_avatar-сцен.
> Аватар-сцены (0–3, 9–14, 31–34) делает HeyGen сам — их тут нет.
> Формат: 9:16 vertical. Стиль: cinematic, тёмный графит + тёплый янтарь, фотореализм, film grain.
> ⚠️ Текст на экране (оффер/хуки/воронка/гэпы, кириллица) НЕ прописываю в промпт — генератор его «поедет».
> Лучше: генерь чистое движение UI, а сами подписи добавь ОВЕРЛЕЕМ в HeyGen поверх клипа.

---

## КЛИП 1 — сцена 2 (3–9 сек, ~6 сек) · копируешь ссылку конкурента

**Grok prompt (EN, вставить целиком):**
```
Vertical 9:16 cinematic macro video. A smartphone on a dark graphite desk in warm amber light.
On the screen, a web browser address bar; a competitor's link is being selected and copied, the
text cursor blinking, a subtle "copied" glow pulse. Shallow depth of field, warm screen glow, soft
reflections on the dark desk, gentle slow push-in camera move. Photoreal, cinematic, film grain.
No people, no faces, no logos. UI animates inside the phone screen.
```
**Движение:** курсор выделяет ссылку → лёгкая вспышка «скопировано», медленный наезд камеры.
**Длина:** 5–6 сек.

---

## КЛИП 2 — сцена 4 (14–27 сек, ~13 сек) · Claude строит карту-разбор  ⭐ главный

**Grok prompt (EN, вставить целиком):**
```
Vertical 9:16 cinematic macro video. A laptop screen on a dark graphite desk showing a clean modern
dark app interface. A structured breakdown map builds itself: five horizontal rows appear and light
up one by one in warm amber, each row with a small glowing icon on the left and a bar filling to the
right, like an analysis being assembled live. Cursor moves, warm screen glow, keyboard bokeh in
foreground, slow subtle push-in. Photoreal, cinematic, film grain. Everything animates inside the
screen. No people, no faces, no readable text, no logos.
```
**Движение:** 5 строк-разделов появляются и подсвечиваются по очереди (это «оффер/аудитория/хуки/воронка/гэпы»).
**Подписи** «оффер · аудитория · хуки · воронка · гэпы» — добавь текстом-оверлеем в HeyGen поверх строк.
**Длина:** нужно 13 сек. Если Grok даёт короткие клипы — сгенерь **2 клипа по 6–7 сек** (строки 1–3, потом 4–5 + подсветка) и склей в HeyGen. Или один клип 6 сек и чуть замедлить/растянуть.

---

## КЛИП 3 — сцена 5 (27–31 сек, ~4 сек) · подсветка «гэпов»

**Grok prompt (EN, вставить целиком):**
```
Vertical 9:16 cinematic macro video. Same dark laptop screen interface. The bottom row of the
breakdown brightens and pulses in strong warm amber, a clear highlighted opening standing out from
the dimmer rows above, hopeful confident mood, warm screen glow, shallow depth of field, slight
camera settle. Photoreal, cinematic, film grain. Animates inside the screen. No people, no readable
text, no logos.
```
**Движение:** нижний блок (это «гэпы — чего не делает») ярко подсвечивается на фоне притухших строк.
**Подпись** «гэпы: чего не делает» — оверлеем в HeyGen.
**Длина:** 4 сек.

---

## Общие настройки для Grok (для всех клипов)

- **Соотношение:** 9:16 (vertical).
- **Стиль-хвост, если Grok просит:** `cinematic, dark graphite and warm amber, photoreal, film grain, shallow depth of field, no people`.
- **Референс тона:** тёплый экран — единственный яркий источник; фон тёмный, премиум.
- **Что НЕ включать:** людей, лица, читаемый русский текст в кадре (добавляем оверлеем), фейковые логотипы.

## Как собрать в HeyGen

1. Генеришь 3 клипа (клип 2 — при необходимости двумя частями).
2. Вставляешь как B-roll на тайм-коды: 3–9 · 14–27 · 27–31.
3. Поверх клипа 2 — текст-оверлеи «оффер · аудитория · хуки · воронка · гэпы»; поверх клипа 3 — «гэпы: чего не делает».
4. Субтитры на клипе 2 — **OFF** (чтобы не спорили с оверлеями); на 1 и 3 — по карте субтитров из основного файла рила.
5. Аватар-сцены (0–3, 9–14, 31–34) — по брифу из `reels-claude-day5.md` (раздел 10).
