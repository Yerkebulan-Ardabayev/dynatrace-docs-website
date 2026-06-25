---
title: Settings API - Beacon origins for CORS schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-beacon-domain-origins
scraped: 2026-05-12T11:46:58.994446
---

# Settings API - Beacon origins for CORS schema table

# Settings API - Beacon origins for CORS schema table

* Published Dec 05, 2023

### Источники beacon для CORS (`builtin:rum.web.beacon-domain-origins)`

Укажите источники RUM beacon, которые должны приниматься OneAgent и ActiveGate. Dynatrace сопоставляет каждое заданное правило с заголовком запроса `Origin` входящих beacon и копирует источник из совпавшего заголовка в заголовок ответа `Access-Control-Allow-Origin`. Источники beacon, не входящие в набор правил, отклоняются, а ответ beacon возвращает HTTP 403. Если набор правил пуст, источники beacon принимаются с любого домена. Учтите: при включении первого правила приложения, не совпадающие с правилом, перестают собирать RUM-данные.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.beacon-domain-origins` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.beacon-domain-origins` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.beacon-domain-origins` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.beacon-domain-origins` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Сопоставитель `matcher` | enum | Возможные значения: * `EQUALS` * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` | Required |
| Шаблон `pattern` | text | - | Required |