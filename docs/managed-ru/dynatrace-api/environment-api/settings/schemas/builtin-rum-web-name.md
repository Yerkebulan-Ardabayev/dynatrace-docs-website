---
title: Settings API - Application name schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-name
scraped: 2026-05-12T11:39:19.266529
---

# Settings API - Application name schema table

# Settings API - Application name schema table

* Published Dec 05, 2023

### Имя приложения (`builtin:rum.web.name)`

Это имя используется для обозначения вашего приложения во всём этом окружении Dynatrace. Убедитесь, что у приложения осмысленное имя.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.name` | * `group:rum-settings` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.name` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обновить имя приложения `applicationName` | text | - | Required |