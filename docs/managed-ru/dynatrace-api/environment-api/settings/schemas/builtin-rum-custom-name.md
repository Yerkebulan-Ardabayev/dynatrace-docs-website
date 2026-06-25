---
title: Settings API - Application name and type schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-custom-name
scraped: 2026-05-12T11:49:08.484232
---

# Settings API - Application name and type schema table

# Settings API - Application name and type schema table

* Published Dec 05, 2023

### Имя и тип приложения (`builtin:rum.custom.name)`

Это имя используется для обозначения пользовательского приложения во всём этом окружении Dynatrace. Убедитесь, что у приложения осмысленное имя.
Чтобы использовать другую иконку для представления приложения, измените тип приложения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.custom.name` | * `group:rum-general` | `CUSTOM_APPLICATION` - Custom Application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.custom.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.custom.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.custom.name` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Обновить имя приложения `applicationName` | text | - | Required |
| Обновить тип приложения `applicationType` | enum | Возможные значения: * `iot` * `embedded-pc` * `ufo` * `desktop` * `echo` * `hololens` | Required |