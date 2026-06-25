---
title: Settings API - Varnish Cache schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-varnish
scraped: 2026-05-12T11:48:51.809657
---

# Settings API - Varnish Cache schema table

# Settings API - Varnish Cache schema table

* Published Dec 05, 2023

### Varnish Cache (`builtin:monitored-technologies.varnish)`

По умолчанию мониторинг Varnish Cache отключён на всех хостах. Если вы хотите включить мониторинг Varnish Cache на отдельных хостах, включите его на этих хостах через их настройки.

Если вы хотите отключить мониторинг Varnish Cache только на отдельных хостах, включите глобальный мониторинг Varnish Cache и отключите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.varnish` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.varnish` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.varnish` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.varnish` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить Varnish Cache `enabled` | boolean | - | Required |