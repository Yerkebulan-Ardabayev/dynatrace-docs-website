---
title: Settings API - IIS schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-iis
scraped: 2026-05-12T11:49:04.829677
---

# Settings API - IIS schema table

# Settings API - IIS schema table

* Published Dec 05, 2023

### IIS (`builtin:monitored-technologies.iis)`

По умолчанию мониторинг IIS включён на всех хостах. Если вы хотите отключить мониторинг IIS на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг IIS только на отдельных хостах, отключите глобальный мониторинг IIS и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.iis` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.iis` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.iis` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.iis` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить IIS `enabled` | boolean | - | Required |