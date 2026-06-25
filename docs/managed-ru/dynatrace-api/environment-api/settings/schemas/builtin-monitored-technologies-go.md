---
title: Settings API - Go schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-go
scraped: 2026-05-12T11:41:49.193722
---

# Settings API - Go schema table

# Settings API - Go schema table

* Published Dec 05, 2023

### Go (`builtin:monitored-technologies.go)`

По умолчанию мониторинг Go включён на всех хостах. Если вы хотите отключить мониторинг Go на отдельных хостах, отключите его на этих хостах через их настройки.

Если вы хотите включить мониторинг Go только на отдельных хостах, отключите глобальный мониторинг Go и включите его на этих хостах через их настройки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.go` | - | `HOST` - Host  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.go` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.go` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.go` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить Go `enabled` | boolean | - | Required |
| Включить статический мониторинг приложений Go `enabledGoStaticMonitoring` | boolean | Подробнее об [known limitations for Go static monitoring](https://www.dynatrace.com/support/help/technology-support/application-software/go/support/go-known-limitations#limitations) | Required |