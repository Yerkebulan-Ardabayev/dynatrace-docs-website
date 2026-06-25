---
title: Settings API - Monitoring Mode schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-monitoring-mode
scraped: 2026-05-12T11:41:32.545520
---

# Settings API - Monitoring Mode schema table

# Settings API - Monitoring Mode schema table

* Published Dec 05, 2023

### Режим мониторинга (`builtin:host.monitoring.mode)`

Режим мониторинга OneAgent можно переключить только пока агент подключён.

Учтите: только для этой схемы API [GET objects](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-objects) обычно не возвращает объекты, так как настройки хранятся на агентах. Используйте вместо него API [GET effective values](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-effective-values).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.monitoring.mode` | * `group:host-monitoring` | `HOST` - Host |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.mode` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.monitoring.mode` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.monitoring.mode` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Режим мониторинга `monitoringMode` | enum | Dynatrace OneAgent позволяет мониторить любой аспект окружения, включая все процессы, сервисы и приложения, обнаруженные на хостах.  Режимы мониторинга OneAgent дают гибкость в выборе того, какие возможности OneAgent включены для хоста. Каждый последующий режим увеличивает включённые возможности, но также увеличивает потребление лицензии. Подробнее см. [Monitoring consumption](https://www.dynatrace.com/support/help/shortlink/monitoring-consumption).  Режим мониторинга применяется к процессу после его перезапуска.  Режим мониторинга OneAgent автоматически перезаписывает эту настройку при изменении через [oneagentctl](https://dt-url.net/oneagentctl) или при подключении OneAgent. Возможные значения: * `DISCOVERY` * `INFRA_ONLY` * `FULL_STACK` | Required |