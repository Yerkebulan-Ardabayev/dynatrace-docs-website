---
title: Settings API - Extension Execution Controller schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-eec-local
scraped: 2026-05-12T11:44:38.534632
---

# Settings API - Extension Execution Controller schema table

# Settings API - Extension Execution Controller schema table

* Published Dec 05, 2023

### Extension Execution Controller (`builtin:eec.local)`

Конфигурация Extension Execution Controller для развёртывания OneAgent

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:eec.local` | * `group:preferences` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eec.local` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:eec.local` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eec.local` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Extension Execution Controller `enabled` | boolean | - | Required |
| Включить локальный HTTP-API для приёма метрик, логов и событий `ingestActive` | boolean | - | Required |
| Включить Dynatrace StatsD `statsdActive` | boolean | Применимо только к неконтейнеризированным хостам Linux и Windows | Required |
| Профиль производительности `performanceProfile` | enum | Выберите профиль производительности для Extension Execution Controller [Documentation](https://www.dynatrace.com/support/help/shortlink/extensions-concepts#resource-consumption "More about performance profiles") Возможные значения: * `DEFAULT` * `HIGH` | Required |