---
title: Settings API - Request errors schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-request-errors
scraped: 2026-05-12T11:44:19.073340
---

# Settings API - Request errors schema table

# Settings API - Request errors schema table

* Published Dec 05, 2023

### Ошибки запросов (`builtin:rum.mobile.request-errors)`

Создайте правила исключения, чтобы определить, какие HTTP-коды ответа не должны считаться ошибками. По умолчанию Dynatrace считает все коды состояния ответа 4xx и 5xx ошибками веб-запросов.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.request-errors` | - | `MOBILE_APPLICATION` - Mobile App  `CUSTOM_APPLICATION` - Custom Application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.request-errors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.request-errors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.request-errors` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `errorRules` | Set<[RequestErrorRule](#RequestErrorRule)> | - | Required |

##### The `RequestErrorRule` object

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Исключить коды ответа `errorCodes` | text | - | Required |