---
title: Settings API - Advanced Settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-monitoring-advanced
scraped: 2026-05-12T11:48:28.587271
---

# Settings API - Advanced Settings schema table

# Settings API - Advanced Settings schema table

* Published Dec 05, 2023

### Расширенные настройки (`builtin:host.monitoring.advanced)`

Вы можете отключить внедрение ProcessAgent и CodeModules.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.monitoring.advanced` | * `group:host-monitoring` | `HOST` - Host |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.advanced` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.monitoring.advanced` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.advanced` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Внедрение ProcessAgent `processAgentInjection` | boolean | Отключение этой настройки отключает многие возможности глубокой видимости процессов, например: трассировку, профилирование, технологически-специфичные метрики (heap usage и т.п.), сбор метрик JMX/PMI, аналитику уязвимостей в рантайме, live-отладку и др. Для режимов Fullstack или Infrastructure отключать эту настройку рекомендуется только для целей траблшутинга.  Отключение автоматического внедрения через [oneagentctl](https://dt-url.net/oneagentctl) имеет приоритет над включением этой настройки и не может быть изменено из веб-интерфейса Dynatrace. | Required |
| Внедрение CodeModule `codeModuleInjection` | boolean | Внедрять CodeModules в режиме Discovery. | Required |