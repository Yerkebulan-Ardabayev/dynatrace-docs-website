---
title: Settings API - Process group monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-host-process-groups-monitoring-state
scraped: 2026-05-12T11:44:16.924875
---

# Settings API - Process group monitoring schema table

# Settings API - Process group monitoring schema table

* Published Dec 05, 2023

### Мониторинг групп процессов (`builtin:host.process-groups.monitoring-state)`

Включите или отключите мониторинг для определённых групп процессов на этом хосте

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:host.process-groups.monitoring-state` | - | `HOST` - Host |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.process-groups.monitoring-state` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:host.process-groups.monitoring-state` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:host.process-groups.monitoring-state` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Группа процессов `ProcessGroup` | text | - | Required |
| Состояние мониторинга `MonitoringState` | enum | Возможные значения: * `MONITORING_OFF` * `MONITORING_ON` * `DEFAULT` | Required |