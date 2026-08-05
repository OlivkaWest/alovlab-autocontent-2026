---
name: alovlab-video-prompt
description: >-
  Построение промптов для image-to-video и text-to-video (Higgsfield, Grok/Seedance/
  Kling/Veo). Первый кадр, движение камеры, сохранение персонажа, negative prompt.
  Используй при подготовке B-roll и оживлении кадров.
---

# alovlab-video-prompt

Промпты без мусора («cinematic, masterpiece, 8K»). Конкретика: субъект, свет,
камера, движение, что сохранить, чего избегать.

## Image-to-video (есть готовый кадр)
Сохрани композицию, текст, геометрию, цвета бренда. Движение — slow controlled push-in
или лёгкий pan. Avoid: text deformation, new elements, flicker, sudden camera, duplicates.

## Text-to-video (кадра нет)
Опиши сцену/метафору. Вертикаль 9:16, премиальный свет, спокойная камера, без
читаемого текста и логотипов.

## Персонаж в кадре
Всегда через `alovlab-character-lock`: Identity Lock + negative rules + reference IDs.
Никогда «same man» текстом — только постоянная идентичность.

## Higgsfield (через MCP)
Спека сохраняется в `reels/higgsfield/<scene>_prompt.md` + `_request.json`. Модель
(Seedance/Kling/Veo) выбирается после проверки доступных через MCP. Реальная
генерация — инструментами `mcp__higgsfield__generate_video`.

## Grok (xAI)
Payload по официальной схеме (сверь endpoints). Mock: `XAI_VIDEO_MOCK_MODE=true`.
Сохраняй `reels/grok/<scene>_prompt.md`, `_request.json`, `_response.json`.
