---
name: alovlab-character-lock
description: >-
  Стабильность аватара Нейромонах между сценами и роликами. Используй при «лицо
  снова не похоже», «персонаж плывёт», перед любой генерацией сцены с Нейромонахом
  и при проверке готовых кадров. Опирается на assets/characters/neuromonk.
---

# alovlab-character-lock

Идентичность Нейромонаха критична. Не полагайся на «same man, consistent character» —
этого мало. Используй постоянную систему.

## Источник идентичности (приоритет)
1. Higgsfield Soul ID — если создан (`identity.json.higgsfield_soul_id.reference_id`).
2. Постоянный HeyGen avatar (`HEYGEN_AVATAR_ID` + `HEYGEN_VOICE_ID`).
3. Character Bible: `assets/characters/neuromonk/CHARACTER.md` + `visual_rules.json`.

Новый Soul ID / новый образ — **только по отдельной команде**, не автоматически.

## Перед генерацией сцены
1. Есть ли в сцене Нейромонах? Нет → не добавляй персонажа в prompt.
2. Да → подгрузи утверждённые референсы + `identity_lock`.
3. Вставь Identity Lock (см. CHARACTER.md) и negative rules (`negative_rules.md`).
4. Сохрани использованные reference IDs и prompt рядом со сценой.

## После генерации — проверка (identity check)
Лысая голова · форма черепа · борода · возраст · глаза · нос · уши · телосложение ·
нет «чужого лица» · пропорции · нет фотошопного стыка · кожа естественна · узнаваем.
Не прошло → статус `identity_failed`, сцена в финал не идёт, перегенерируй.

## Запись на сцену
```json
{ "character":"neuromonk","identity_source":"heygen_avatar","reference_ids":[],
  "identity_lock":true,"outfit_id":"","visual_review":"pending" }
```
