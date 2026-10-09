# Карусели AlovLab — шаблон и пайплайн

Премиальная карусель из **6 слайдов**, публикуется **одним постом** в порядке:

`1 обложка → 2 провокация → 3 связка → 4 неделя → 5 пик → 6 CTA`

Каждая карусель — разбор пользы ИИ **в конкретном бизнесе** (кейс). **Ниши не повторяются**
от карусели к карусели (ресторан → кофейня → косметика → ювелирка → автосервис → …).

## Как собрать

```bash
# 1) HTML из конфига бизнеса
python3 scripts/carousel_render.py restaurant

# 2) экспорт каждого слайда в PNG 1080×1350 (4:5)
NODE_PATH=/opt/node22/lib/node_modules node \
  scripts/carousel_shoot.js exports/carousels/restaurant/restaurant.html exports/carousels/restaurant
```

Результат: `exports/carousels/<бизнес>/slide-01.png … slide-06.png`.

## Новый бизнес

Добавь словарь в `CONFIGS` внутри `scripts/carousel_render.py` (или передай путь к JSON-конфигу
тем же ключом). Поля: `label`, `cover_h`, `cover_labels`, `prov_h/prov_sub`, `svyazka` (3 карточки
`tag,en,h,sub`), `nedelya` (5 строк `lg,en,h,sub`), `pik_h/pik_cap/pik_note`. CTA — общий.

## Фото-слоты (реальные кадры)

По умолчанию визуалы — фирменная дизайн-графика (кинокадр + пар + тарелка). Чтобы вшить
**реальные фото**, положи файлы в `content/carousel-assets/<бизнес>/` и укажи их в `photos`:

```python
"photos": {
  "cover_rich": "content/carousel-assets/restaurant/hero.png",  # правый кадр обложки
  "pik":        "content/carousel-assets/restaurant/hero.png",  # герой-кадр слайда 5
  "prov":       "content/carousel-assets/restaurant/feed.png",  # центральный кадр слайда 2
  "svyazka_1":  "content/carousel-assets/restaurant/dish.png",
}
```

Файл существует → вшивается как фон кадра (с затемнением под текст); нет → рисуется графика.

## Правила (обязательно)

- **Без футера.** На слайдах НЕ пишем «Автоконтент 2026 / t.me/AlovLab».
- **Логотип** — только настоящий знак `assets/img/logo-mark.png`, «AlovLab» слитно.
- **Обложка** — один хук + один визуальный конфликт + одна интрига (порог ≥ 8.5, иначе не готово).
- **Пустых зон нет** — блоки растянуты на всю высоту слайда.
- **Показ и аудит** — каждый слайд отдельным PNG, открыть и проверить, разбор «до/после».
- **Честность** — кадры это концепт-дизайн (не «результат клиента»); выдуманных цифр нет;
  цена студии не называется.

Первый собранный кейс: `exports/carousels/restaurant/` (авторский ресторан).
