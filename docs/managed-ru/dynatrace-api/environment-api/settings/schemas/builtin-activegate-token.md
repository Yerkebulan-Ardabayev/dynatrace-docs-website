---
title: Settings API - Network security schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-activegate-token
scraped: 2026-05-12T11:49:27.585943
---

# Settings API - Network security schema table

# Settings API - Network security schema table

* Published Dec 05, 2023

### Сетевая безопасность (`builtin:activegate-token)`

Dynatrace обеспечивает безопасность соединения между элементами окружения Dynatrace из коробки.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:activegate-token` | * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:activegate-token` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:activegate-token` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:activegate-token` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Принудительно включить аутентификацию по токену ActiveGate вручную `authTokenEnforcementManuallyEnabled` | boolean | - | Required |
| Включить уведомления о датах истечения токенов ActiveGate `expiringTokenNotificationsEnabled` | boolean | Примечание: уведомления о токенах ActiveGate отправляются только если в окружении развёрнуты токены ActiveGate с датами истечения и определены уведомления (см. настройки уведомлений (`<your-dynatrace-url>//ui/settings/builtin:problem.notifications`)) | Required |