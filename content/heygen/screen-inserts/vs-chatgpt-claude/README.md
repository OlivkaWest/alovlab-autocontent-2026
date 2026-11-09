# Панели ChatGPT / Claude для сравнительных роликов (X4 «ChatGPT vs Claude»)

Готовые макеты интерфейсов (2K, читаемый русский) для наложения на экран в HeyGen — как в пайплайне Дня 5
(`content/heygen/reels-claude-day5-video-prompts.md`): Grok рисует среду с пустым экраном → сюда кладём панель.

- `chatgpt-panel-chat.png` — ChatGPT, чистый чат (монохром, таблица-ответ), модель «ChatGPT 5».
- `chatgpt-panel-models.png` — с раскрытым селектором: GPT-5 · GPT-5 Thinking · GPT-5 mini · GPT-4o.
- `claude-panel-chat.png` — Claude, чистый чат (тёплый графит+янтарь), модель «Claude Opus 5».
- `vs-side-by-side.png` — обе панели рядом (референс раскладки для «vs»).
- Claude с моделями — в `../reels-day5/claude-panel-models.png` (Opus 5 · Sonnet 5 · Haiku 4.5 · Fable 5.1).

Пересобрать/поправить текст или модели: `scripts/claude_panel.html`, `scripts/chatgpt_panel.html` + `scripts/shoot_panel.js`.

⚠️ Модели: Claude — по актуальному ряду (Opus 5 / Sonnet 5 / Haiku 4.5 / Fable 5.1). ChatGPT — семейство GPT-5
поставлено по открытым данным 2026; **сверь точные названия текущего ряда OpenAI перед публикацией** (не проверял вживую).
Стиль намеренно разный: ChatGPT монохром+таблица, Claude тёплый+карточка — чтобы в кадре читались как разные продукты.
