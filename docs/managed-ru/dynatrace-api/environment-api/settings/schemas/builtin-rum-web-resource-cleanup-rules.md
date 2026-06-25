---
title: Settings API - Resource URL cleanup rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-resource-cleanup-rules
scraped: 2026-05-12T11:48:05.682344
---

# Settings API - Resource URL cleanup rules schema table

# Settings API - Resource URL cleanup rules schema table

* Опубликовано 05 декабря 2023 г.

### Правила очистки URL ресурсов (`builtin:rum.web.resource-cleanup-rules)`

Resource URL cleanup rules используются для агрегации URL ресурсов, которые в остальном идентичны, но различаются динамическими элементами: идентификаторами (например, из REST API), query-строками (например, случайные аргументы, отключающие кеширование) и прочими session-данными. После того как такие session-специфичные детали отбрасываются, URL отображаются в агрегированном виде в waterfall analysis. Учтите, что resource URL cleanup rules выполняются в порядке, указанном ниже. Подробнее о cleanup rules см. [Define URL cleanup rules](https://dt-url.net/resource-cleanup-rules-response-codes).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:rum.web.resource-cleanup-rules` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.content-resources` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.resource-cleanup-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.resource-cleanup-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.resource-cleanup-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | Например: *Mask journeyId* | Required |
| Регулярное выражение `regularExpression` | text | Например: `(.*)(journeyId=)-?\d+(.*)` | Required |
| Заменить на `replaceWith` | text | Например: `$1$2\*$3` | Required |