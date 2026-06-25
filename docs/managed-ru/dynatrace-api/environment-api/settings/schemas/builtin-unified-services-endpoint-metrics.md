---
title: Settings API - Endpoint metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-unified-services-endpoint-metrics
scraped: 2026-05-12T11:42:23.086620
---

# Settings API - Endpoint metrics schema table

# Settings API - Endpoint metrics schema table

* Published Dec 05, 2023

### Метрики эндпоинтов (`builtin:unified-services-endpoint-metrics)`

Эта настройка позволяет включить или отключить классические метрики эндпоинтов. Подробнее см. [documentation](https://dt-url.net/gy03cmt).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:unified-services-endpoint-metrics` | * `group:service-detection` | `SERVICE` - Service  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:unified-services-endpoint-metrics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:unified-services-endpoint-metrics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:unified-services-endpoint-metrics` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить классические метрики эндпоинтов `enableEndpointMetrics` | boolean | Записывать ли метрики для эндпоинтов? Обратите внимание, что эта настройка имеет последствия для биллинга и не влияет на метрики в Grail. Подробнее см. эту [documentation](https://dt-url.net/td23cgh). | Required |