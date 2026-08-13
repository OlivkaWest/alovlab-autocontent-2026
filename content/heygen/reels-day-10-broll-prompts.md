# День 10 · B-roll: 6 промптов image-to-video (под HeyGen-анимацию)

Под бриф `reels-day-10-animation-brief.md`. Каждый клип оживляет **свой кадр
раскадровки** (image-to-video: подаёшь картинку-кадр как реф + промпт движения).
Модель: Seedance 2.5 (или Kling/Runway/Higgsfield). Формат 9:16, тёмный фон,
оранжевый акцент. Лупы 2–6 сек.

> ВАЖНО про текст и UI. Модели i2v склонны «плавить» буквы и интерфейс. В каждом
> промпте есть жёсткая страховка: **keep all text, numbers and UI perfectly stable,
> no warping, no morphing letters**. Всё равно проверяй дубли — если текст «дышит»,
> бери дубль спокойнее или делай элемент нативно в HeyGen.

**Легенда пригодности:**
✅ — отлично для image-to-video (физика: свет, вода, камера).
⚠️ — UI-ревил (строки/линии появляются). i2v делает нестабильно — **чище и
дешевле собрать нативно в HeyGen** (Entrance + Start time). Промпт даю как запасной.

---

## Клип 1 · Кривая удержания падает (сцена 3, ~3 сек) — ⚠️
Реф: левая половина кадра 3 («ПОТОК», ступенчатая кривая 100%→0%).

```
@ref keep the dark UI panel, axis labels and layout perfectly stable, no morphing text.
A soft orange glow dot travels along the jagged retention line from top-left down to
bottom-right, leaving a faint fading trail; the line itself stays fixed. Subtle grain,
gentle vignette breathing. Minimal camera drift. Loopable. 9:16.
```
РУ: светящаяся точка «проходит» по уже нарисованной падающей линии — иллюзия черчения,
без риска, что модель перерисует график. **Лучше нативно:** линию рисовать Draw-on в HeyGen.

---

## Клип 2 · Лесенка каркаса загорается (сцена 3, ~3 сек) — ⚠️
Реф: правая половина кадра 3 («КАРКАС», 4 ступени Удар/Боль/Приём/Результат).

```
@ref keep the steps, icons and captions perfectly stable, no morphing text.
A warm orange light rises step by step from the bottom step to the top, each step
briefly blooms with a soft glow and settles; faint spark particles drift upward.
Deep blacks, cinematic. Minimal camera move. Loopable. 9:16.
```
РУ: свет поднимается по ступеням снизу вверх — подсветка зон «по очереди».
**Лучше нативно:** 4 glow-плашки с Entrance по одной.

---

## Клип 3 · Таблица Claude печатается (сцена 4, ~6 сек) — ⚠️ (ключевой)
Реф: нижнее окно кадра 4 (интерфейс Claude, таблица таймкодов).

```
@ref keep the Claude window chrome, header and column titles perfectly stable,
no morphing text. Table rows appear one after another from top to bottom with a soft
type-on feel and a faint orange highlight sweeping across the active row; a thin cursor
blinks. Screen emits a gentle glow. No camera move. 9:16.
```
РУ: строки «печатаются» сверху вниз, по активной идёт оранжевая подсветка.
**Настоятельно лучше нативно/скринкастом:** это самый рискованный кадр для i2v
(текст поплывёт). Идеал — реально записать экран Claude, где строки появляются, ИЛИ
собрать 4 строки в HeyGen с Entrance. i2v-промпт — только если нужен «атмосферный» дубль.

---

## Клип 4 · Дождь по стеклу + свет гаснет (сцена 5, ~5 сек) — ✅
Реф: верх кадра 5 (сплит комната солнце→дождь, мокрое окно).

```
@ref keep room geometry and windows stable, no morphing.
Rain runs down the window glass in realistic droplets and rivulets; warm sunlight on the
left slowly dims into a cold grey overcast on the right as the scene turns rainy.
Reflections shimmer on the wet glass, slow cinematic push-in. Native ambience. 9:16.
```
РУ: капли реально текут, свет «солнце → дождь» гаснет. **Самый выигрышный клип для
i2v** — чистая физика, модель делает отлично. Медленный наезд оживляет стекло.

---

## Клип 5 · Зачёркивание пустой строки (сцена 6, ~1.5 сек) — ⚠️
Реф: окно Claude «черновик» из кадра 6 (строка 5–7 «Также важно отметить…»).

```
@ref keep the Claude window and all rows perfectly stable, no morphing text.
A single thin red strike-through line draws left-to-right across the one filler row,
then the row dims to 40% opacity; a small orange badge fades in below. Nothing else moves.
No camera move. 9:16.
```
РУ: красная линия проходит по одной строке, строка тускнеет. **Лучше нативно:**
Draw-on strike в HeyGen — там линия будет идеально ровной, i2v даст «дрожащую».

---

## Клип 6 · Тетрадь прилетает (сцена 7, ~2 сек) — ✅
Реф: тетрадь Дня 10 из кадра 7 (разворот с таймлайном и таблицей).

```
@ref keep the notebook page content, timeline and table perfectly stable, no morphing text.
The open notebook gently flies in from the bottom with a soft 3D tilt and settles, a subtle
paper texture and warm rim light sweeping across the page; faint depth-of-field on the dark
background. Smooth, premium, slight parallax. Loopable end. 9:16.
```
РУ: тетрадь мягко «прилетает» с лёгким 3D-наклоном. **Хорошо для i2v** — это движение
объекта, а не UI-ревил. Держи наклон небольшим, чтобы текст на странице не поплыл.

---

## Итог: что реально генерить, что делать нативно
- **Генерить в i2v (✅):** Клип 4 (дождь) и Клип 6 (тетрадь) — дают максимум «живости»
  за минимум риска.
- **Собрать нативно в HeyGen (⚠️):** Клипы 1, 2, 3, 5 — это появление строк/линий/света
  по очереди. HeyGen через Entrance + Start time сделает чище, стабильнее и бесплатно.
- **Клип 3 (таблица)** — если хочется «по-настоящему»: записать экран Claude.

> Честность (§0): кадры — концепт-дизайн, не результат клиента. Цифр/цен нет; результат
> в примере — формой. Показываешь ИИ — актуальный интерфейс Claude.
