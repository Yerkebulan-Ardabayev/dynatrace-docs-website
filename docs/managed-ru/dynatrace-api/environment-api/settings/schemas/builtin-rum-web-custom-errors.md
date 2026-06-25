---
title: Settings API - Custom errors schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-custom-errors
scraped: 2026-05-12T11:47:19.603264
---

# Settings API - Custom errors schema table

# Settings API - Custom errors schema table

* Published Dec 05, 2023

### Пользовательские ошибки (`builtin:rum.web.custom-errors)`

Создайте правила для захвата пользовательских ошибок и включения их в расчёты Apdex или обнаружение и анализ проблем Davis AI.
Подробнее см. [Configure custom errors](https://dt-url.net/sh220gh).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.custom-errors` | * `group:rum-errors` | `APPLICATION` - Web application  `environment-default` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-errors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.custom-errors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-errors` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Игнорировать пользовательские ошибки в расчётах Apdex `ignoreCustomErrorsInApdexCalculation` | boolean | Эта настройка переопределяет настройки Apdex для отдельных правил, перечисленных ниже | Required |
| `errorRules` | [CustomErrorRule](#CustomErrorRule)[] | - | Required |

##### Объект `CustomErrorRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Сопоставление ключа `keyMatcher` | enum | Возможные значения: * `ALL` * `BEGINS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` | Required |
| Шаблон ключа `keyPattern` | text | Шаблон ключа, нечувствительный к регистру | Required |
| Сопоставление значения `valueMatcher` | enum | Возможные значения: * `ALL` * `BEGINS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` | Required |
| Шаблон значения `valuePattern` | text | Шаблон значения, нечувствительный к регистру | Required |
| Настройки захвата `captureSettings` | [CaptureSettings](#CaptureSettings) | - | Required |

##### Объект `CaptureSettings`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Захватывать эту ошибку `capture` | boolean | - | Required |
| Включать ошибку в расчёты Apdex `impactApdex` | boolean | - | Required |
| Включать ошибку в обнаружение и анализ проблем Davis AI `considerForAi` | boolean | [View more details](https://dt-url.net/hd580p2k) | Required |