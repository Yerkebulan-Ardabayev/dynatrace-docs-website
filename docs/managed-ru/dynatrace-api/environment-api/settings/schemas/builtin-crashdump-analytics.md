---
title: Settings API - Crash dump analytics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-crashdump-analytics
scraped: 2026-05-12T11:45:11.930998
---

# Settings API - Crash dump analytics schema table

# Settings API - Crash dump analytics schema table

* Published Feb 26, 2024

### Аналитика крэш-дампов (`builtin:crashdump.analytics)`

Dynatrace автоматически обнаруживает сбои приложений в Windows и Linux и анализирует core-дампы этих сбоев. Здесь вы можете управлять аналитикой крэш-дампов. Подробнее об анализе сбоев см. [documentation](https://docs.dynatrace.com/docs/shortlink/crash-analysis)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:crashdump.analytics` | - | `HOST` - Host  `HOST_GROUP` - Host Group |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:crashdump.analytics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:crashdump.analytics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:crashdump.analytics` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Аналитика крэш-дампов `enableCrashDumpAnalytics` | boolean | Отключите функцию, чтобы перестать получать информацию о деталях сбоев и потенциальных проблемах. Мы рекомендуем оставлять функцию включённой. | Required |