# AlovLab · VIDEO PRODUCTION STACK (skills-команда для Reels)

Зафиксированный стек для производства роликов. Собран после исследования GitHub —
устанавливали не «первый попавшийся», а проверенное по качеству, свежести, безопасности,
применимости и отсутствию конфликтов.

## Что установлено и откуда

| Скилл | Куда | Откуда | Роль | Риск |
|---|---|---|---|---|
| **reel-visual** | `.claude/skills/reel-visual/` | вендорен из **smixs/visual-skills** (CC BY 4.0, атрибуция в `ATTRIBUTION.md`) | DIRECTOR · STORYBOARD · CINEMATOGRAPHY · SEEDANCE 2.5 · CONTINUITY · MOTION | нулевой: только markdown, без скриптов/ключей/сети |
| **alovlab-reel** | `.claude/skills/alovlab-reel/` | собран нами | ОРКЕСТРАТОР + SCRIPT · HOOK · HEYGEN · EDITOR · QC (бренд/голос/воронка/честность) | нулевой: наш markdown |

`reel-visual/references/seedance-25.md` — официальные гайды ByteDance (2026-07-31): 50-слотовая
система рефов, 11-блочный скелет, anti-collapse, anti-AI-face, камера, переходы, failure modes.

## Что НЕ ставили (осознанно)
- **Bomx/super-video-maker-skill** (224★) — полная автоматизация HeyGen+Seedance+Remotion+FFmpeg.
  Причина отказа: исполняет Python-скрипты, требует ключи (HeyGen/OpenAI/Replicate/ElevenLabs/AWS),
  ходит в сеть, качает Chromium, лицензия не указана. Security surface + конфликт с нашим ручным
  флоу. Вернёмся, если понадобится сквозная автоматизация — под ревью и в изоляции.
- **DirectorSKILL / ai-video-storyboard-skill / ai-shortfilm-prompts** — хорошие, но перекрываются
  с `reel-visual`. Держим в резерве; при желании возьмём отдельные приёмы (19 failure modes из
  DirectorSKILL, hook-структуры short-drama из ai-shortfilm-prompts).
- Seedance-библиотеки промптов (awesome-seedance-2 и др.) — это банки данных, не скиллы; берём как
  справку при необходимости, не устанавливаем.

## Как изменился workflow
Раньше: ролик писался «одним проходом». Теперь любой Reels идёт через виртуальную команду
(оркестратор `alovlab-reel`), делегируя крафт `reel-visual`:

```
IDEA → HOOK → SCRIPT → DIRECTOR → STORYBOARD → VISUAL DESIGN
     → SEEDANCE B-ROLL → HEYGEN → EDIT → RETENTION CHECK → FINAL QC
```

Выход — production script из 11 секций (эталоны: `reels-day-10-production-script.md`,
`reels-rubriki-2111-production-script.md`), с жёсткой честностью §0 и QC ≥ 9 по всем метрикам.

## Что запускается автоматически при новом Reels
- Запрос «сделай рилс / production script / сценарий HeyGen / раскадровка / B-roll» →
  срабатывает **`alovlab-reel`** (по описанию-триггеру).
- Внутри него роли DIRECTOR/CINEMATOGRAPHY/SEEDANCE/CONTINUITY вызывают **`reel-visual`**.
- Голос Ильи — через **`alovlab-content`**; HEYGEN/EDIT/QC — через references оркестратора.
- Ничего сомнительного или требующего ключей не запускается.

## Обновление стека
Периодически проверять апдейты `smixs/visual-skills` (последний — 2026-08-04, Seedance 2.5).
Обновление: пере-вендорить `video/` в `reel-visual/`, сверить `ATTRIBUTION.md`.
