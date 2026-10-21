# Источники — «Два аватара. Один разговор» (батч 1)

Дата проверки: 19.10.2026. Прямой доступ к code.claude.com из этой среды доступен; прямой доступ к
docs.heygen.com, developers.heygen.com, developers.openai.com и elevenlabs.io заблокирован сетью
этой среды — такие факты помечены как вторичное подтверждение через WebSearch, не прямой просмотр
страницы.

## HeyGen — Audio to Video (глава 2)
- developers.heygen.com/audio-to-video — WebSearch-подтверждение, не прямое чтение.
- docs.heygen.com/docs/using-audio-source-as-voice — WebSearch-подтверждение.
- docs.heygen.com/docs/using-audio-source-as-voice-archived — существование архивной версии
  страницы само по себе подтверждает, что механика менялась.
- docs.heygen.com/reference/limits — лимит 50 МБ (аудио).
- developers.heygen.com/docs/upload-assets — лимит 32 МБ (общая загрузка). Расхождение с пунктом
  выше не разрешено — явно показано в тексте методички.
- help.heygen.com/en/articles/10060327-heygen-api-subscriptions-explained — тарифы API, не
  привязывают Audio to Video к конкретному плану.

## Claude Code (переиспользовано из исследования для guide_klod_montazh_build.py, 16.10.2026)
- code.claude.com/docs/en/memory, /skills, /permissions, /settings, /sub-agents, /hooks-guide —
  прочитаны напрямую.

## Codex CLI (переиспользовано из того же исследования)
- github.com/openai/codex (README, docs/*.md) — частично прямое чтение.
- developers.openai.com/codex/* — WebSearch-подтверждение, прямой доступ заблокирован.

## Открытые пункты (проверить при следующем батче / перед публикацией)
- Точный текущий лимит размера аудиофайла для HeyGen Audio to Video (32 vs 50 МБ).
- Актуальные названия кнопок в интерфейсе HeyGen для выбора режима «подать аудио вместо текста» —
  на дату написания проверялись только через WebSearch, не через живой интерфейс.
- ElevenLabs output_format по тарифам (какие форматы доступны на бесплатном тарифе).
