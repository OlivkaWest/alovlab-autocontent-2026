# Шаблон master-промпта для HeyGen Video Agent

> Правило — `content/rules/ALOVLAB-HEYGEN-VIDEO-AGENT-DIRECTOR.md` §14. Заполнять предметно по
> теме текущего выпуска. Никаких абстракций («добавь красивые кадры», «сделай вирусно») — только
> конкретное действие, изображение и его функция. Готовый текст — это Часть 2 ответа на `/reel`
> или `/reel-duo`, одним куском для вставки в Video Agent.

```
PROJECT
[Название ролика. Тема одной фразой.]

FORMAT
Вертикальное видео 9:16. Длительность: [XX-XX сек, ориентир]. Язык: русский.
Аудитория: Россия и СНГ.

AVATAR
Use the avatar already selected by the user in HeyGen. Do not replace, recreate, or substitute it.
[Если /reel-duo: то же самое для второго аватара — только если его паспорт утверждён, см. §5
стандарта. Если не утверждён — не заполнять, вернуться к пользователю.]

VOICE
Use the voice already selected by the user in HeyGen. Do not replace, recreate, or substitute it.

CREATIVE DIRECTION
[Жанр, настроение, характер подачи — одна-две фразы.]

VISUAL LANGUAGE
Палитра AlovLab: графит/светлый нейтральный фон, оранжевый акцент. [Композиция, свет, работа
камеры, типографика — конкретно под эту тему.]

STORYBOARD
[Каждая сцена — отдельным блоком по шаблону templates/heygen-scene.md, вставляется сюда целиком.]

EXACT SPOKEN SCRIPT
[Только реплики для озвучки, без режиссёрских пометок, без тире (GLOBAL-REELS-VOICE-RULE.md §8).
В режиме /reel-duo — реплики разделены по говорящему.]

GENERATED VISUALS
[Seedance-сцены по полному набору полей §8 стандарта: SUBJECT/ACTION/ENVIRONMENT/CAMERA ANGLE/
CAMERA MOVEMENT/LIGHTING/ATMOSPHERE/VISUAL STYLE/DURATION/CONTINUITY/NEGATIVE CONSTRAINTS.]

ATTACHMENTS
[Назначение каждого реально приложенного референса: PHOTO_01 — ..., SCREEN_02 — ... Если
референсов нет — написать "не требуются" или "не приложены".]

MOTION GRAPHICS
[Какие текстовые/графические элементы показывать и когда, синхронно с репликой.]

SUBTITLES
[Где ON, где OFF, по сценам.]

AUDIO
[Музыка/звук — по теме, без дешёвых шаблонов. "Без фоновой музыки" тоже валидный вариант.]

EDITING
[Ритм, склейки, переходы между сценами.]

FINAL FRAME
[Последний кадр — что видно, что звучит, как заканчивается.]

QUALITY CONSTRAINTS
Use the avatar and voice already selected by the user in HeyGen. Do not replace, recreate, or
substitute either one. [+ любые специфичные для этого выпуска запреты: не называть платформу Х,
не придумывать цифры, не показывать вымышленный интерфейс и т.п.]
```
