---
title: Settings API - NetTracer traffic schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-nettracer-traffic
scraped: 2026-05-12T11:38:57.085716
---

# Settings API - NetTracer traffic schema table

# Settings API - NetTracer traffic schema table

* Published Dec 05, 2023

### Трафик NetTracer (`builtin:nettracer.traffic)`

NetTracer: open source инструмент для трассировки TCP-событий и сбора метрик сетевых соединений в Linux.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:nettracer.traffic` | * `group:network-and-discovery` * `group:monitoring` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:nettracer.traffic` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:nettracer.traffic` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:nettracer.traffic` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить сетевой мониторинг трафика NetTracer `netTracer` | boolean | Если отключено, OneAgent не будет использовать NetTracer для сбора сетевых данных из контейнеров. Отключено по умолчанию. Применяется только к Linux-хостам. Требует OneAgent 1.231+. | Required |