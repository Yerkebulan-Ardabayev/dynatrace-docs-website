---
title: Settings API - Exclude XHR requests from monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-xhr-exclusion
scraped: 2026-05-12T11:40:08.551774
---

# Settings API - Exclude XHR requests from monitoring schema table

# Settings API - Exclude XHR requests from monitoring schema table

* Published Dec 05, 2023

### Исключение XHR-запросов из мониторинга (`builtin:rum.web.xhr-exclusion)`

Укажите регулярное выражение для совпадения со всеми URL, которые должны быть исключены из XHR-действий.

Dynatrace поддерживает синтаксис JavaScript Regular Expressions. Разделение по разным протоколам URI не поддерживается (каждый протокол URI будет исключён).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.xhr-exclusion` | * `group:capturing` * `group:capturing.exclusions` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.xhr-exclusion` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.xhr-exclusion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.xhr-exclusion` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| XHR exclusion rule `xhrExclusionRule` | text | **Examples:**  * \/segment1\/segment2 * dynatrace\.com * www\.dynatrace\.com\/segment1\/.\*[a-zA-Z] * www\.dynatrace\.com:8080 * www\.dynatrace\.com:([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]) * www\.dynatrace\.com\?param1=value1&param2=.\*[a-zA-Z] | Required |