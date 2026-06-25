---
title: Settings API - Envoy schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-open-tracing-native
scraped: 2026-05-12T11:43:58.281687
---

# Settings API - Envoy schema table

# Settings API - Envoy schema table

* Published Dec 05, 2023

### Envoy (`builtin:monitored-technologies.open-tracing-native)`

По умолчанию мониторинг Envoy отключён на всех хостах. Если вы хотите включить мониторинг Envoy на отдельных хостах, включите его на этих хостах через их настройки.

Если вы хотите отключить мониторинг Envoy только на отдельных хостах, включите глобальный мониторинг Envoy и отключите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.open-tracing-native` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.open-tracing-native` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.open-tracing-native` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.open-tracing-native` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить Envoy `enabled` | boolean | - | Required |