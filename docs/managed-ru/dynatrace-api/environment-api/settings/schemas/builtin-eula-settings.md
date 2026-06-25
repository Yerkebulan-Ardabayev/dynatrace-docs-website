---
title: Settings API - Terms of use schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-eula-settings
scraped: 2026-05-12T11:42:01.853647
---

# Settings API - Terms of use schema table

# Settings API - Terms of use schema table

* Published Dec 05, 2023

### Условия использования (`builtin:eula-settings)`

Показывать условия для конечных пользователей (рекомендуется для клиентов, купивших через реселлера).

См. наши сторонние лицензии (`<your-dynatrace-url>//ui/third-party-licenses`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:eula-settings` | * `group:preferences` | `environment`  `environment-default` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eula-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:eula-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eula-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Показывать условия для конечных пользователей новым пользователям, входящим в окружение `enableEula` | boolean | - | Required |