---
title: Settings API - Python schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-python
scraped: 2026-05-12T11:49:33.578343
---

# Settings API - Python schema table

# Settings API - Python schema table

* Published May 05, 2025

### Python (`builtin:monitored-technologies.python)`

По умолчанию мониторинг Python отключён на всех хостах. Если вы хотите включить мониторинг Python на отдельных хостах, включите его на этих хостах через их настройки.

Если вы хотите отключить мониторинг Python только на отдельных хостах, включите глобальный мониторинг Python и отключите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.python` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.python` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.python` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.python` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить Python `enabled` | boolean | - | Required |