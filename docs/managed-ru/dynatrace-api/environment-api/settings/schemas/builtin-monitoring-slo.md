---
title: Settings API - Service-level objective definitions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitoring-slo
scraped: 2026-05-12T11:46:04.234712
---

# Settings API - Service-level objective definitions schema table

# Settings API - Service-level objective definitions schema table

* Published Dec 05, 2023

### Описания целей уровня обслуживания (SLO) (`builtin:monitoring.slo)`

Задайте пользовательские [Service-level objectives](https://dt-url.net/slos) (SLO), чтобы помочь в выполнении соглашений об уровне обслуживания вашей организации. Создайте до 10000 пользовательских SLO для этого Dynatrace-окружения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitoring.slo` | * `group:cloud-automation.monitoring.slo` * `group:cloud-automation` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoring.slo` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitoring.slo` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoring.slo` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя SLO `name` | text | - | Required |
| Описание `customDescription` | text | Описание SLO | Optional |
| Имя метрики `metricName` | text | - | Required |
| Задайте выражение метрики, измеряющее success rate этого SLO `metricExpression` | text | Подробнее см. на Metrics page (`<your-dynatrace-url>//ui/metrics "Metrics page"`). | Required |
| Тип вычисления `evaluationType` | enum | Выберите "Aggregate", чтобы измерения этой success-метрики агрегировались в одну метрику percentage-rate. Возможные значения: * `AGGREGATE` | Required |
| Селектор сущностей `filter` | text | Задайте параметр фильтра (entitySelector) в любом GET-вызове, чтобы вычислять этот SLO только для конкретных сервисов (например, type("SERVICE")). Подробнее см. в [Entity Selector documentation](https://dt-url.net/entityselector). | Required |
| Временной диапазон, в котором вычисляется SLO `evaluationWindow` | text | Задайте временной диапазон, в котором будет вычисляться SLO. В качестве диапазона можно вводить выражения вида -1h (последний час), -1w (последняя неделя) или сложные выражения вида -2d to now (последние два дня), -1d/d to now/d (от начала вчерашнего дня до начала сегодняшнего). | Required |
| Целевой процент `targetSuccess` | float | Задайте целевое значение SLO. Процент ниже этого значения означает failure. | Required |
| Процент предупреждения `targetWarning` | float | Задайте значение SLO для предупреждения. В состоянии warning SLO ещё выполняется, но приближается к failure. | Required |
| `errorBudgetBurnRate` | [ErrorBudgetBurnRate](#ErrorBudgetBurnRate) | - | Required |

##### Объект `ErrorBudgetBurnRate`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включена визуализация burn rate `burnRateVisualizationEnabled` | boolean | - | Required |
| Порог fast-burn `fastBurnThreshold` | float | Порог определяет, когда burn rate помечается как fast-burning (high-emergency). Burn rate ниже этого порога (и больше 1) выделяется как slow-burn (low-emergency). | Required |