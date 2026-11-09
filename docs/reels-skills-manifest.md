# Манифест скиллов для `/alovlab-reels-today`

> Что реально проверено и подключено, что сознательно пропущено и почему. Обновляется при каждой
> проверке новых источников скиллов — не переписывать историю, дописывать.

## Уже существующие в проекте / сессии (не устанавливались заново)

| Скилл | Источник | Локальный путь | Назначение | Результат проверки |
|---|---|---|---|---|
| `alovlab-content` | проект (коммит в этом репозитории) | `.claude/skills/alovlab-content/SKILL.md` | Голос Ильи, форматы, генерация идей | Прочитан целиком 29.09.2026. Дублирует голосовые правила CLAUDE.md, конфликтов нет. |
| `alovlab-core` (session-level) | личный Anthropic-скилл пользователя, не файл репозитория | — | Базовый голос/бриф AlovLab | Доступен через Skill-листинг сессии, отдельно не читался — не требовалось, CLAUDE.md имеет приоритет по правилу самого файла. |
| `alovlab-content` (session-level, anthropic-skills) | личный Anthropic-скилл пользователя | — | То же, что проектный alovlab-content | Дублирует проектный, конфликтов не найдено. |
| `skill-creator` (session-level, anthropic-skills) | предустановлен в этой среде | — | Создание/проверка новых скиллов | Использован метод (не сам инструмент) для структуры нового `alovlab-reels-today` — не потребовалось клонировать `anthropics/skills` отдельно, скилл уже доступен на уровне сессии. |

## Установлены 19.10.2026 (явный запрос пользователя: 30 позиций для видеопродакшна)

Каждый — отдельно открыт по прямой ссылке, лицензия и commit зафиксированы перед копированием в
`.claude/skills/<имя>/`. Полная таблица по всем 30 позициям карусели (включая не найденные и не
установленные) — `SKILLS_INSTALL_REPORT.md` в корне репозитория.

| Скилл | Источник | Commit | Лицензия | Назначение | Конфликт с голосом AlovLab |
|---|---|---|---|---|---|
| `hyperframes` | heygen-com/hyperframes | 2927bf0 | Apache-2.0 | Точка входа монтажа/анимации | Не найден — техническая CLI-библиотека, не генерирует текст контента |
| `hyperframes-core` | heygen-com/hyperframes | 2927bf0 | Apache-2.0 | Контракт композиции | Не найден |
| `hyperframes-cli` | heygen-com/hyperframes | 2927bf0 | Apache-2.0 | CLI-команды рендера | Не найден |
| `hyperframes-audio` | heygen-com/hyperframes | 2927bf0 | Apache-2.0 | Микс звука (фейды, дакинг, EQ) | Не найден |
| `motion-graphics` | heygen-com/hyperframes | 2927bf0 | Apache-2.0 | Короткая моушн-графика | Не найден |
| `embedded-captions` | heygen-com/hyperframes | 2927bf0 | Apache-2.0 | Субтитры поверх видео | Не найден |
| `remotion-best-practices` | remotion-dev/skills | 1441a11 | см. Remotion LICENSE | Роутер остальных remotion-скиллов | Не найден |
| `remotion-create` | remotion-dev/skills | 1441a11 | см. Remotion LICENSE | Создание Remotion-проекта | Не найден |
| `remotion-render` | remotion-dev/skills | 1441a11 | см. Remotion LICENSE | Экспорт видео | Не найден |
| `remotion-captions` | remotion-dev/skills | 1441a11 | см. Remotion LICENSE | Субтитры в Remotion | Не найден |
| `remotion-multimedia` | remotion-dev/skills | 1441a11 | см. Remotion LICENSE | Работа с Mediabunny | Не найден |
| `video-shotcraft` | Vincentwei1021/video-shotcraft | 43bd349 | Apache-2.0 (код); аудио — поэлементно, см. ATTRIBUTION.md внутри | Продуктовые видео из карточек-рецептов | Не найден. Демо/галерея/jianying-export удалены перед коммитом (не нужны для работы) |
| `video-use` | browser-use/video-use | 43cfc56 | MIT | Разговорный монтаж (транскрипт→резка→цвет→субтитры) | Не найден. Требует ELEVENLABS_API_KEY для транскрипции — не настроен |
| `clipify` | louisedesadeleer/clipify | 5f6b75e | MIT | Поиск ярких моментов + нарезка + реframe 9:16 | Не найден |
| `shorts` | agricidaniel/claude-shorts | a369fad | MIT | Long→short, интерактивный отбор сегментов | Не найден |
| `find-broll` | louisedesadeleer/b-roll-finder | 36b8a56 | MIT | Подбор b-roll по транскрипту | Не найден |
| `video-perception` | jordanrendric/claude-video-vision | 4a4f990 | MIT | Извлечение кадров + транскрипция для анализа видео | Не найден |
| `higgsfield` | OSideMedia/higgsfield-ai-prompt-skill | 7075497 | MIT | Промпт-инженерия под Higgsfield (MCSLA) | Не найден. Дополняет, не заменяет уже подключённый MCP `mcp__higgsfield__*` |
| `video_toolkit` | digitalsamba/claude-code-video-toolkit | 959e0fc | MIT | Оркестратор: сценарий→озвучка→музыка→визуал→рендер | Не найден |
| `ffmpeg` | digitalsamba/claude-code-video-toolkit | 959e0fc | MIT | Справочник паттернов ffmpeg под этот тулкит | Не найден |
| `moviepy` | digitalsamba/claude-code-video-toolkit | 959e0fc | MIT | Python-композиция видео (альтернатива Remotion) | Не найден |

## Проверены по названию, НЕ установлены (сознательное решение)

| Скилл/репозиторий | Источник | Почему не установлен |
|---|---|---|
| `coreyhaines31/marketingskills` (social, content-strategy, copy-editing) | https://github.com/coreyhaines31/marketingskills | Сторонний непроверенный код, который автозагружается будущими сессиями. Не read-only просмотр — установка меняет поведение проекта. Без отдельного явного «да» от пользователя на конкретное содержимое — не устанавливаю. Кроме того авторский голос AlovLab (CLAUDE.md, alovlab-content) уже приоритетнее универсального маркетингового копирайтинга по прямому правилу проекта. |
| `heygen-com/skills`, `developers.heygen.com/skills` | https://github.com/heygen-com/skills | То же соображение про автозагружаемый сторонний код. Дисциплина HeyGen+Seedance для AlovLab уже зашита в CLAUDE.md (Приложение Г) и многократно проверена на практике в этом репозитории — не вижу необходимости тянуть внешний источник поверх уже рабочего процесса без явного запроса. |
| `anthropics/skills` (репозиторий целиком) | https://github.com/anthropics/skills | Не клонировался — `skill-creator`, ради которого он упомянут, уже доступен на уровне этой сессии без установки. |
| `obra/superpowers` | https://github.com/obra/superpowers | Реальный, MIT, проверен напрямую — но это общий фреймворк разработки (TDD, дебаг, код-ревью), не относится к видеопродакшну. Запрос пользователя — скиллы именно для видео, не ставлю нерелевантный. |
| Kling AI Skills (`majiayu000/claude-skill-registry` и аналоги) | — | Низкое доверие (сторонние незнакомые авторы, не Kuaishou/официальный Kling). Доступ к модели Kling уже есть через подключённый MCP `mcp__higgsfield__*` (models_explore) — не вижу смысла тянуть непроверенный дубликат. |
| «Video Editing Skill» / «Video Trimmer» / «Video Editor» (generic) | агрегаторы claudskills.com / claudemarketplaces.com / vibeindex.ai | Не один авторский проект — десятки чужих SKILL.md под общим названием на сайтах-агрегаторах, не оригинальные репозитории авторов. Не устанавливаю с агрегатора без возможности проверить, что контент не изменён относительно оригинала. `video-use`/`clipify`/`claude-shorts` уже закрывают ту же функцию проверенными авторскими репозиториями. |
| Cut Video (Tella) | tella.tv / возможно tellahq/skills | Не удалось напрямую подтвердить файл SKILL.md в репозитории — tella.com недоступен из этой сети. Не устанавливаю неподтверждённое. |
| Vertical Video Editing, Thumbnail Skills, Caption Clip, Omni Captions, Caption Engine, Color Grade AI, Pexo Agent, Video Producer, Audio Editing (`clawfu-skills`, архивирован) | — | Не найдено ни одного настоящего проекта под этим названием после реального поиска (WebSearch), либо репозиторий архивирован/не подтверждён. Честно зафиксировано как «не найден» в `SKILLS_INSTALL_REPORT.md`, не заменено случайным похожим пакетом. |

## Не запускались проверки безопасности внешнего кода (устарело для записи ниже — см. таблицу установленных выше)
Для записей 2026-09-29 и ранее: поскольку ничего стороннего не устанавливалось, отдельная проверка
лицензий/commit SHA не требовалась — зафиксировано явно, а не молчанием. Для установки 19.10.2026 —
проверки лицензии/commit/SKILL.md выполнены для каждой позиции индивидуально (см. таблицу выше и
`SKILLS_INSTALL_REPORT.md`).

## Как обновлять
Если в будущем пользователь явно попросит подключить один из пропущенных скиллов — до установки:
1. открыть настоящий SKILL.md по прямой ссылке;
2. зафиксировать автора, лицензию, commit SHA;
3. проверить содержимое на конфликт с голосом/правилами CLAUDE.md;
4. только потом копировать в `.claude/skills/<имя>/` и дописывать строку в эту таблицу.
