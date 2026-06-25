---
title: Settings API - Nginx schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-nginx
scraped: 2026-05-12T11:45:21.035241
---

# Settings API - Nginx schema table

# Settings API - Nginx schema table

* Published Dec 05, 2023

### Nginx (`builtin:monitored-technologies.nginx)`

По умолчанию мониторинг Nginx включён на всех хостах. Если вы хотите отключить мониторинг Nginx на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг Nginx только на отдельных хостах, отключите глобальный мониторинг Nginx и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.nginx` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.nginx` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.nginx` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.nginx` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить Nginx `enabled` | boolean | - | Required |