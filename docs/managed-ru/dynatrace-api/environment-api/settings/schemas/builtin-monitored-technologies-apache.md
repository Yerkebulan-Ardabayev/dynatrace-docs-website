---
title: Settings API - Apache HTTP Server schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-apache
scraped: 2026-05-12T11:41:36.393745
---

# Settings API - Apache HTTP Server schema table

# Settings API - Apache HTTP Server schema table

* Published Dec 05, 2023

### Apache HTTP Server (`builtin:monitored-technologies.apache)`

По умолчанию мониторинг Apache HTTP Server включён на всех хостах. Если вы хотите отключить мониторинг Apache HTTP Server на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг Apache HTTP Server только на отдельных хостах, отключите глобальный мониторинг Apache HTTP Server и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.apache` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.apache` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.apache` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.apache` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить Apache HTTP Server `enabled` | boolean | - | Required |