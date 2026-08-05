# AlovLab Automation — производство Reels по дате внутри Claude Code

Это **не сайт и не веб-приложение**. Это локальный тулинг (CLI + файлы + API),
которым управляют командами Claude Code. Ты пишешь «Сделай ролик на 5 августа» —
тулинг находит контент этого дня, пишет сценарий, разбивает на сцены, гонит аватара
через HeyGen, добирает B-roll (Higgsfield/Grok/FFmpeg) и сам монтирует вертикальный MP4.

```
дата → контент дня → сценарий Reels → сцены → HeyGen (аватар)
     → B-roll (Higgsfield / Grok / FFmpeg) → монтаж FFmpeg → субтитры → логотип → final.mp4
```

Лендинг проекта (`../index.html`) не трогается — это отдельная статика.

## Установка и запуск

```bash
cd automation
npm install
cp .env.example .env      # заполни ключи (можно оставить mock)
npm run alovlab -- doctor # статус HeyGen / Grok / Higgsfield / FFmpeg
```

Требуется Node ≥ 20 и **полноценный FFmpeg** (с libx264) + ffprobe:

```bash
# Debian/Ubuntu
apt-get install -y ffmpeg
# либо укажи путь вручную в .env:  FFMPEG_PATH=/usr/bin/ffmpeg  FFPROBE_PATH=/usr/bin/ffprobe
```
> Урезанный ffmpeg из Playwright не подходит (нет libx264) — тулинг использует его
> только как крайний fallback и честно ругается, если кодеков нет.

## Команды

```bash
npm run alovlab -- doctor                 # подключения и режимы
npm run alovlab -- index                  # собрать content/index.json по реальным дням
npm run alovlab -- content 2026-08-05     # показать материал дня
npm run alovlab -- script  «5 августа»    # только сценарий + сцен-план (без HeyGen)
npm run alovlab -- scenes  2026-08-05     # показать сцен-план
npm run alovlab -- route   2026-08-05     # маршрутизация сцен по генераторам
npm run alovlab -- reel    2026-08-05     # ПОЛНЫЙ цикл → готовый MP4
npm run alovlab -- assemble 2026-08-05    # пересобрать монтаж (без HeyGen)
npm run alovlab -- regen-scene 2026-08-05 2   # перегенерировать ОДНУ сцену
npm run alovlab -- status  2026-08-05     # статус дня
```

Дату понимает и по-русски («5 августа» → `2026-08-05`, год из текущей даты), и в ISO.

## Как хранится контент дня

```
content/2026-08/2026-08-05/
  source/     meta.json · carousel.md · post.md      # исходный материал дня
  carousel/   01_cover.png … 07_cta.png              # PNG-карточки (b-roll)
  visuals/    готовые изображения/видео дня           # опционально
  reels/
    reels_script_vN.json · reels_script.md
    storyboard_vN.json · generation_plan_vN.json · edit_plan_vN.json
    subtitles.srt · subtitles.ass
    heygen/    avatar_master_payload.json · _response.json · avatar_master.mp4
    grok/      <scene>_prompt.md · _request.json · _response.json
    higgsfield/<scene>_prompt.md · _request.json
    broll/     <scene>.mp4
    render/    final_reels_vN.mp4
    generation.log
  status.json  # статус дня, версии, heygen_jobs
```

Формат дня описан в `../content/README.md`. Новый день — просто такая же папка;
`content` (адаптер) прочитает её сам. Ничего не выдумывается: чего нет в `source/`,
попадает в `missing[]`, а если дня нет — тулинг честно говорит «материал не найден».

## Три генератора видео

| Что | Когда | Как подключается |
|---|---|---|
| **HeyGen** | говорит Нейромонах (хук, реплики, финал, CTA) | REST API, ключ в `.env` |
| **Higgsfield** | оживить готовый кадр (image-to-video), cinematic B-roll | **MCP внутри Claude Code** (`mcp.higgsfield.ai/mcp`) |
| **Grok (xAI)** | создать недостающую сцену с нуля (text-to-video) | REST API, ключ в `.env` |
| **FFmpeg** | хватает карточки/push-in — не тратим кредиты | локально |

Маршрут выбирается автоматически (`src/generators/router.ts`) и пишется в
`generation_plan_vN.json`. Аватар никогда не подменяется чужим персонажем.

### HeyGen — подключение
1. Ключ: HeyGen → Settings → API. Вставь в `.env`: `HEYGEN_API_KEY=...`
2. Постоянный аватар и голос Нейромонаха: `HEYGEN_AVATAR_ID=...`, `HEYGEN_VOICE_ID=...`
   (id аватара/голоса — в HeyGen: раздел Avatars / Voices). Без них в реальном
   режиме тулинг покажет: «Добавь HEYGEN_AVATAR_ID и HEYGEN_VOICE_ID».
3. `HEYGEN_MOCK_MODE=false` — включить реальную генерацию.

### Higgsfield — подключение (через MCP)
Higgsfield уже подключается как MCP-сервер Claude Code — ключ в `.env` не нужен.
Проверка: инструменты `mcp__higgsfield__*` доступны в сессии. Реальную генерацию
B-roll выполняет Claude через эти инструменты; тулинг готовит спеку задачи
(`reels/higgsfield/<scene>_prompt.md` + `_request.json`). Модель (Seedance/Kling/Veo)
выбирается **после** проверки доступных моделей через MCP, не наугад.

### Grok (xAI) — подключение
1. Ключ xAI: console.x.ai → API Keys. В `.env`: `XAI_API_KEY=...`
2. **Важно:** endpoints генерации видео xAI надо сверить с официальной документацией
   и вписать `XAI_VIDEO_ENDPOINT` / `XAI_VIDEO_STATUS_ENDPOINT`. Пока они пусты,
   реальный запуск честно останавливается (мы не выдумываем схему API).
3. `XAI_VIDEO_MOCK_MODE=false` — включить реальную генерацию.

## Mock-режим (по умолчанию)

`HEYGEN_MOCK_MODE=true`, `XAI_VIDEO_MOCK_MODE=true`, `HIGGSFIELD_MOCK_MODE=true` —
весь цикл проходит **без ключей и без трат**: тестовые video_id, тот же путь статусов,
локальные тестовые MP4, реальный монтаж и проверка финала. Mock не выдаётся за
настоящую интеграцию — в отчёте видно `MOCK`.

## Монтаж и безопасность

- Единый формат: 1080×1920 · 9:16 · H.264 · AAC · 30 fps. Горизонталь — pad/scale
  без обрезки лиц и текста.
- Голос Нейромонаха идёт поверх B-roll, музыка тише голоса, логотип только в финале.
- FFmpeg запускается через `execFile` **массивом аргументов** (`shell:false`).
  Пользовательский текст не попадает в строку команды; субтитры вшиваются из файла.
  `assertSafeArg` отсекает пробелы и управляющие символы.
- Финал проверяется ffprobe: существует, 1080×1920, есть видео+аудио, длительность.
  Не прошёл — не называем готовым.

## Перегенерация одной сцены

```bash
npm run alovlab -- regen-scene 2026-08-05 2   # только сцена 2, новая версия
npm run alovlab -- assemble    2026-08-05      # пересобрать финал
```
Изменение монтажа/субтитров/логотипа **не** перезапускает HeyGen.

## Тесты и проверки

```bash
npm run typecheck   # tsc --noEmit
npm run test        # vitest (54 теста): сценарий, валидация сцен, HeyGen payload,
                    # статус, ошибки API, retry, скачивание, версии, PNG-имена,
                    # сборка FFmpeg-команды, защита от shell injection, mock
npm run build       # компиляция в dist/
```

## Диагностика ошибок

- `doctor` — покажет режимы и что не задано.
- «материал не найден» — нет папки `content/<month>/<date>/` или пустой `source/`.
- «Добавь HEYGEN_AVATAR_ID и HEYGEN_VOICE_ID» — в реальном режиме нет id аватара/голоса.
- «FFmpeg не найден» — задай `FFMPEG_PATH` или поставь ffmpeg с libx264.
- Grok «не задан XAI_VIDEO_ENDPOINT» — сверь endpoints с доками xAI и впиши в `.env`.
- Всё состояние дня — в `status.json` и `reels/generation.log` (переживает перезапуск).
