# HeyGen Video Agent · «Bot Field Notes» — готово к вставке целиком

> Для интерфейса «Продолжить создание видео» (аватар НЕЙРОМОНАХ / доктор Нейро, Seedance уже Вкл).
> Ничего не разделяй на части — вставляй блок 1 целиком в поле «Сценарий», блок 2 целиком в «Инструкции».
> Агент сам решит, где говорит аватар, а где включить Seedance-сцену — по репликам и сценам в тексте.

---

## 1. Поле «СЦЕНАРИЙ» — вставить целиком

```
Я не просил ИИ сделать бота. Я поставил ему техзадание.

[Сцена 1 — оживи приложенное изображение slide-01.png: лёгкий наезд камеры, текст на экране остаётся как есть, не менять]

Сценарий по шагам: старт, тема, имя, контакт, заявка.

[Сцена 2 — оживи приложенное изображение slide-03.png: диаграмма состояний, стрелки будто дорисовываются одна за другой, текст на карточках не менять]

Токен я храню отдельно от кода. Не в коде, не в логах, не в Git. Claude выдал мне не файл, а проект: код, зависимости, инструкцию запуска.

[Сцена 3 — оживи приложенное изображение slide-06.png: файлы проекта будто появляются по одному сверху вниз, текст не менять]

Перед тем как показать бота кому-то, я прогнал четыре теста. Пустой ответ, отмена, повторный запуск и настоящая заявка. Только после этого я сказал, что бот готов.

[Сцена 4 — оживи приложенное изображение slide-07.png: строки таблицы подсвечиваются одна за другой сверху вниз, текст не менять]

Один бот это один инструмент. Это ещё не система.

Систему я собираю на курсе. Боты, тексты, видео, автоматизация — одной связкой.

[Сцена 5 — оживи приложенное изображение slide-10.png: лёгкий наезд камеры на карточку курса, кнопка «Начать курс» слегка пульсирует, текст и цифры не менять]

Сейчас скидка пятьдесят процентов на тариф Про. Успей до тридцатого сентября. Начать курс — alovlab.ru.
```

---

## 2. Поле «ИНСТРУКЦИИ» — вставить целиком

```
Style: premium, dark background, warm orange accent (#FF6A3D), cinematic depth, 9:16 vertical, subtle film grain.
Avatar НЕЙРОМОНАХ speaks the narration lines directly to camera, calm and confident, no big gestures.
For every bracketed [Сцена N — оживи приложенное изображение ...] direction, use the matching attached image
as the exact starting frame and animate it with Seedance image-to-video: subtle motion only (slow push-in,
gentle reveal, elements highlighting in sequence as described). Do NOT redraw, regenerate or replace the
attached image's content — do NOT invent a new scene from text. Keep every word, number and diagram on the
attached image sharp, legible and pixel-accurate, unchanged. This is animation of a real image, not text-to-video.
Subtitles: bottom, large, white text, key word highlighted in orange. Do not let subtitles or UI overlap the
avatar's face, eyes or mouth. Logo only on the final scene. Cut on the beat, confident and fast pace, total
length 34–40 seconds.
```

---

## 3. Вложения — ОБЯЗАТЕЛЬНО прикрепить именно эти 5 файлов

Загружай в «Вложения» ровно эти файлы (не всю папку) — на них уже готовая кириллица и точные цифры,
Seedance должен их оживить, а не рисовать текст/диаграмму заново:

| Файл | Что на нём | Сцена в сценарии |
|---|---|---|
| `exports/carousels/tg-bot-fieldnotes/RU/slide-01.png` | обложка, терминал «claude "собери бота"» | Сцена 1 |
| `exports/carousels/tg-bot-fieldnotes/RU/slide-03.png` | диаграмма состояний /start→ТЕМА→ИМЯ→КОНТАКТ→ЗАЯВКА | Сцена 2 |
| `exports/carousels/tg-bot-fieldnotes/RU/slide-06.png` | файлы проекта (bot.py, requirements.txt, .env.example…) | Сцена 3 |
| `exports/carousels/tg-bot-fieldnotes/RU/slide-07.png` | таблица тестов (/start, пусто, /cancel, заявка) | Сцена 4 |
| `exports/carousels/tg-bot-fieldnotes/RU/slide-10.png` | карточка курса, 99 990→49 990, скидка 50% | Сцена 5 |

Порядок загрузки в HeyGen обычно не важен — агент сам сопоставит вложение со сценой по номеру,
названному в скобках («оживи приложенное изображение slide-XX.png»). Если интерфейс просит выбрать
файл под конкретную сцену вручную — сопоставляй строго по таблице выше.

## 4. Параметры (как на скрине)
Аватар: **НЕЙРОМОНАХ** · Голос: **доктор Нейро** · Seedance: **Вкл** · Субтитры: **Вкл** · Формат: **Авто (9:16)**.

## 5. Проверка после генерации (HeyGen-check)
[ ] в озвучке нет тире, звучит как речь, не как текст · [ ] хук в первые 2 секунды · [ ] каждая [Сцена: …] стала живой Seedance-анимацией, не статикой · [ ] русский текст в сценах читаемый, не искажён · [ ] на аватаре ничего не перекрывает лицо · [ ] финал — курс со скидкой, цифры и дедлайн совпадают со слайдом 10 карусели.
