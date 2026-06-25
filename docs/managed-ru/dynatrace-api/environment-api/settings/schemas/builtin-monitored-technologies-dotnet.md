---
title: Settings API - .NET schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-dotnet
scraped: 2026-05-12T11:42:10.958888
---

# Settings API - .NET schema table

# Settings API - .NET schema table

* Published Dec 05, 2023

### .NET (`builtin:monitored-technologies.dotnet)`

По умолчанию мониторинг .NET включён на всех хостах. Если вы хотите отключить мониторинг .NET на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг .NET только на отдельных хостах, отключите глобальный мониторинг .NET и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.dotnet` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.dotnet` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.dotnet` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.dotnet` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить .NET `enabled` | boolean | - | Required |
| Включить .NET Core `enabledDotNetCore` | boolean | - | Required |