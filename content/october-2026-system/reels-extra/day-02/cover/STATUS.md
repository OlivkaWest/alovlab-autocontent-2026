# Обложка дня 2 (доп. рилс) — статус: фон сгенерирован, финальный файл не готов

## Что реально сделано
Фон для обложки сгенерирован через Higgsfield (модель `gpt_image_2_5`, 9:16), концепция: конверт без
адреса — та же метафора, что и на обложке карусели дня 2 («промпт без роли — как письмо без адресата»).
Без лица, без текста, без логотипа — специально оставлено пустое пространство вверху и справа под
заголовок.

- **Job ID:** `35a439d8-b2e4-4bff-9bbb-c4010d9ba540`
- **Ссылка на результат (действительна как минимум на момент генерации):**
  `https://d8j0ntlcm91z4.cloudfront.net/user_2wC9fxqVl9PMYHtH6o6vf0HfQ8Y/hf_20260930_214412_35a439d8-b2e4-4bff-9bbb-c4010d9ba540.png`
- **Higgsfield-проект:** `AlovLab Reels — Day 2 (02.10.2026) covers` (`project_id
  756e4344-f775-423d-b687-ae73954cc5bd`), workspace `ff7d87f2-50c8-419b-a6e9-1229b5456ad5`.

## Почему финального файла нет (честная причина, не отговорка)
Скачать этот файл в файловую систему сессии и домонтировать на него заголовок + логотип AlovLab не
удалось: исходящий HTTPS-трафик на CDN Higgsfield (`*.cloudfront.net`) и на `upload.higgsfield.ai`
заблокирован политикой сети этой среды на уровне egress-прокси (подтверждено
`curl $HTTPS_PROXY/__agentproxy/status` → `connect_rejected`, `gateway answered 403`). Это
организационная политика, не сбой инструмента — по инструкции среды такие блокировки не обходят,
а сообщают о них. По той же причине не получилось загрузить реальное референс-фото Ильи
(`assets/img/ilya-alov.jpg`) для портретного варианта обложки, который просил пользователь как первый
вариант, — значит, честной identity-точной генерации портрета в этой сессии тоже не было.

## Что нужно, чтобы закрыть обложку (два пути)
1. **Вручную, вне этой сессии:** открыть ссылку на результат выше (или найти генерацию по Job ID в
   Higgsfield-проекте), наложить заголовок 2–5 слов (например «ПРОМПТ БЕЗ АДРЕСАТА» или «ПИСЬМО БЕЗ
   ИМЕНИ») шрифтом из действующей визуальной системы каруселей и логотип `assets/img/logo-mark.png`
   в безопасной зоне (низ, не перекрывая конверт) — так же, как уже сделано на обложке карусели дня 2.
2. **В сессии без этого сетевого ограничения:** повторить точно тот же job (промпт ниже) или
   использовать уже готовый результат по ссылке, скачать, наложить текст и логотип программно (PIL) —
   инструмент не проблема, проблема только в сетевом доступе.

## Промпт фона (для повторной генерации, если ссылка выше перестанет быть доступной)
```
Editorial still life photograph, cinematic and premium, for a business/education brand cover. A
single cream-colored business envelope lies diagonally on a dark warm-toned wooden desk, lit by soft
warm directional light from the upper left creating a long soft shadow. The envelope is completely
blank on the visible side (no name, no address, no stamp, no text at all), emphasizing emptiness and
anonymity. Composition leaves generous empty dark space in the upper third and right side of the frame
for a headline to be added later. Deep dark brown and near-black background with a subtle warm orange
rim light along the envelope's edge. Shallow depth of field, soft bokeh. Absolutely no text, no
letters, no logos, no people, no hands anywhere in the image. Mood: quiet, a little melancholic,
premium and minimal, vertical magazine-cover framing.
```
Model: `gpt_image_2_5`, aspect ratio `9:16`.

## Заголовок и логотип — спецификация для домонтажа
- **Заголовок (2–5 слов, RU):** «ПРОМПТ БЕЗ АДРЕСАТА» или «ПИСЬМО БЕЗ ИМЕНИ» — крупно, в верхней
  трети кадра (там осознанно оставлено пустое пространство), стиль — как на обложках карусели
  (градиентный uppercase, белое+оранжевое).
- **Заголовок (EN):** «A LETTER, NO NAME» или «NO ROLE, NO ADDRESS».
- **Логотип:** только `assets/img/logo-mark.png`, небольшой знак в безопасной зоне снизу — не
  перекрывает конверт, не на лице (лица на этой обложке нет).
- Портрет Ильи на этой конкретной обложке не нужен — конверт и так прямо объясняет тему выпуска, как
  просил пользователь; портретный вариант остаётся на будущее, когда сетевое ограничение снимется.
