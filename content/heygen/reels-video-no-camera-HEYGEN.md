# HeyGen · СБОРКА РИЛСА «Снял ролик без камеры» — пошаговая документация

> Рабочий лист для сборки в HeyGen. Источник контента: `reels-video-no-camera.md`.
> Правила: Приложение Г (avatar/non_avatar + Seedance), GLOBAL-REELS-VOICE (озвучка без тире), TELEGRAM-FUNNEL-CTA (финал → Telegram).

## 0. Настройки проекта
- **Формат:** 9:16, 1080×1920.
- **Аватар:** Илья (Нейромонах). **Голос:** его клон/пресет, язык RU.
- **Субтитры:** включены СНИЗУ; на сценах с UI/текстом (S5, S7) — выключить или увести в safe-zone, чтобы не пересекались.
- **Длина ролика:** 30–38 сек. Музыка: кинематографичная подложка.
- **Грейд:** единый тёплый оранжевый на весь ролик (сцены как один фильм).

## 1. ОБЯЗАТЕЛЬНАЯ ИНСТРУКЦИЯ HeyGen (вставить дословно в бриф проекта)
> **“Generate all non-avatar scenes with Seedance inside HeyGen. Do not use static overlays, screenshots or slideshow-style animation.”**

## 2. РАСКАДРОВКА (по порядку)

| Сцена | Тип | ~сек | Что в кадре / реплика | Субтитры |
|---|---|---|---|---|
| S1 | Seedance | 3 | Кадр рождается из текста → кинокадр (город на закате) | «Кадр из одного описания» |
| S2 | Аватар | 5 | Реплика ниже | «Без камеры» |
| S3 | Seedance | 4 | Три готовые кинасцены подряд (город/продукт/портрет) | «Готовые сцены» |
| S4 | Аватар | 5 | Реплика ниже | «Опиши: кадр, свет, камера» |
| S5 | Seedance | 4 | Таймлайн монтажа, сцены встают в ряд + музыка/подписи | выкл / safe-zone |
| S6 | Аватар | 4 | Реплика ниже | «Видео это не про камеру» |
| S7 | Seedance | 4 | Готовый вертикальный ролик играет в телефоне | выкл / safe-zone |
| S8 | Аватар | 5 | CTA (реплика ниже) | «Промпты + гайд → Telegram (ссылка в профиле)» |

## 3. РЕПЛИКИ АВАТАРА (вставлять в текстовое поле аватар-сцен; без тире)
- **S2:** Этот кадр никто не снимал. Его написали словами. Ни камеры, ни актёров, ни площадки.
- **S4:** Я просто описал сцену. Что в кадре, какой свет, как движется камера. Нейросеть сняла её за пару минут.
- **S6:** Я собрал сцены в один ролик. Видео это не про камеру, это про то, как поставить кадр.
- **S8:** Промпты сцен и гайд по монтажу лежат в Telegram. Ссылка в шапке профиля. Забирай и собери свой ролик.

> Правило аватара: текст, UI и графика НЕ перекрывают лицо, глаза и рот. Субтитры не заходят на лицо.

## 4. SEEDANCE-ПРОМПТЫ (для non-avatar сцен; continuity — единый тёплый грейд)
**S1 —** dark cinematic screen, a single line of text glows and a rich film frame materializes from it; slow push-in; a Russian caption as a clean separate layer; warm moody light; text-to-image dissolve; ends on a full cinematic frame. NEGATIVE: no gibberish, no watermark, no distorted faces.
**S3 —** three short cinematic shots back to back: a city street at sunset, a premium product close-up, a confident portrait; subtle move in each; expensive ad look; ends on the portrait. NEGATIVE: no gibberish, no watermark, no distorted faces.
**S5 —** a video editor timeline, clips snapping into a row, a music waveform and captions appear; static camera; screen glow; editor UI readable. NEGATIVE: no gibberish, no watermark.
**S7 —** a phone on a dark desk plays the finished vertical ad, warm rim light; slow push-in to the screen. NEGATIVE: no gibberish, no watermark.

> Русский текст в Seedance-сцены НЕ вшивать (поплывёт) — подписи добавляются слоем на монтаже. UI на русском держать читаемым, отдельным слоем.

## 5. ПОРЯДОК СБОРКИ В HeyGen
1. Создать проект 9:16, выбрать аватара Илью и его голос (RU).
2. В бриф проекта вставить инструкцию из §1.
3. Добавить сцены по таблице §2 в порядке S1…S8.
4. Аватар-сцены (S2,S4,S6,S8): вставить реплики §3, проверить, что лицо не перекрыто.
5. Non-avatar сцены (S1,S3,S5,S7): пометить как Seedance motion, вставить промпты §4.
6. Субтитры: включить снизу, на S5/S7 выключить/safe-zone.
7. Наложить музыку, выставить единый грейд, склейки под бит.
8. Экспорт 9:16.

## 6. ЧЕК-ЛИСТ ПЕРЕД ЭКСПОРТОМ (HeyGen-check)
- [ ] В озвучке нет тире, одна мысль = одно предложение.
- [ ] Хук в первые 2 секунды, цепляет.
- [ ] Каждая non-avatar сцена — Seedance motion (не картинка/скриншот/overlay/slideshow/zoom).
- [ ] На аватаре ничего не перекрывает лицо/глаза/рот.
- [ ] На S5/S7 субтитры не пересекают UI.
- [ ] Единый грейд и темп, ролик смотрится как один фильм.
- [ ] Финал ведёт в Telegram (ссылка: IG шапка / VK закреп / TG закреп).
- [ ] Русский текст в кадре читается, добавлен слоем (не вшит в генерацию).
