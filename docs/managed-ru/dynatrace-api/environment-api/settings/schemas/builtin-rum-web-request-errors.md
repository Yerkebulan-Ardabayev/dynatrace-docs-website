---
title: Settings API - Request errors schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-request-errors
scraped: 2026-05-12T11:42:18.893365
---

# Settings API - Request errors schema table

# Settings API - Request errors schema table

* Published Dec 05, 2023

### Ошибки запросов (`builtin:rum.web.request-errors)`

Создавайте правила захвата и обнаружения, чтобы включить ошибки запросов в расчёты Apdex или в обнаружение и анализ проблем Davis AI.
Подробнее см. [Configure request errors](https://dt-url.net/13020hh).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.request-errors` | * `group:rum-errors` | `APPLICATION` - Web application  `environment-default` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.request-errors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.request-errors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.request-errors` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Игнорировать ошибки запросов в расчётах Apdex `ignoreRequestErrorsInApdexCalculation` | boolean | This setting overrides Apdex settings for individual rules listed below | Required |
| `errorRules` | [RequestErrorRule](#RequestErrorRule)[] | - | Required |

##### Объект `RequestErrorRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Сопоставление по коду ошибки `errorCodes` | text | - | Optional |
| Сопоставление по ошибкам с failed image requests `considerFailedImages` | boolean | - | Required |
| Сопоставление по ошибкам с CSP-нарушениями `considerCspViolations` | boolean | - | Required |
| Настройки фильтра `filterSettings` | [FilterSettings](#FilterSettings) | - | Required |
| Настройки захвата `captureSettings` | [CaptureSettings](#CaptureSettings) | - | Required |

##### Объект `FilterSettings`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Фильтр по URL `filter` | enum | Возможные значения: * `BEGINS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` | Optional |
| URL `url` | text | - | Required |

##### Объект `CaptureSettings`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Захватывать эту ошибку `capture` | boolean | - | Required |
| Включать ошибку в расчёты Apdex `impactApdex` | boolean | - | Required |
| Включать ошибку в обнаружение и анализ проблем Davis AI `considerForAi` | boolean | [View more details](https://dt-url.net/hd580p2k) | Required |