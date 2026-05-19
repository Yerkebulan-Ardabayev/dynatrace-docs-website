---
title: Settings API - Business flow schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-biz-flow-biz-flow-settings
scraped: 2026-05-12T11:43:18.074294
---

# Settings API - Business flow schema table

# Settings API - Business flow schema table

* Published May 20, 2024

### Business flow (`app:dynatrace.biz.flow:biz-flow-settings)`

Настройки для AppEngine-приложения Business flow.

Внимание! Если перечисленные ниже конфигурации изменить здесь, в окружении Settings 2.0, приложение Business Flow, скорее всего, потеряет к ним доступ или будет вести себя непредсказуемо. Настоятельно рекомендуется не вносить здесь никаких изменений и не сохранять их. Если нужно внести изменения, откройте приложение Business Flow.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.biz.flow:biz-flow-settings` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.flow:biz-flow-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.biz.flow:biz-flow-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.flow:biz-flow-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | Имя конфигурации | Optional |
| Описание `description` | text | Описание конфигурации | Optional |
| Версия `version` | integer | - | Optional |
| ID конфигурации `id` | text | - | Optional |
| Шаги `steps` | [TStepType](#TStepType)[] | Шаги конфигурации | Required |
| Подключения `connections` | [TConnectionType](#TConnectionType)[] | - | Required |
| ID корреляции `correlationID` | text | ID корреляции | Optional |
| Метка KPI `kpiLabel` | text | - | Required |
| KPI `kpi` | text | KPI | Optional |
| Событие KPI `kpiEvent` | [TKpiEventType](#TKpiEventType) | - | Optional |
| Единица KPI `kpiUnit` | text | - | Optional |
| Тип вычисления `kpiCalculation` | enum | Возможные значения: * `sum` * `firstEvent` * `lastEvent` | Optional |
| Тип анализа `analysisType` | enum | Возможные значения: * `fulfillment` * `conversion` * `other` | Required |
| Пользовательская метка анализа `analysisCustomLabel` | text | - | Required |
| Единица анализа `analysisUnit` | text | - | Optional |
| ID детекторов аномалий `anomalyDetectorIDs` | [TAnomalyDetectorIDsType](#TAnomalyDetectorIDsType) | - | Optional |
| Включена ли топология Smartscape `isSmartscapeTopologyEnabled` | boolean | - | Required |
| ID сущности Smartscape `smartscapeEntityId` | text | - | Optional |
| Приоритет `priority` | enum | Возможные значения: * `high` * `medium` * `low` * `critical` | Optional |
| Период мониторинга в часах `monitoringTimeframeInHours` | integer | - | Optional |
| Частота мониторинга в часах `monitoringFrequencyInHours` | integer | - | Optional |
| Игнорируется ли лимит запроса по умолчанию `isDefaultQueryLimitIgnored` | boolean | - | Required |

##### Объект `TStepType`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| ID `id` | text | - | Required |
| Является ли корнем `isRoot` | boolean | - | Optional |
| События `events` | [TEventType](#TEventType)[] | - | Required |

##### Объект `TConnectionType`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID `id` | text | - | Required |
| Источник `source` | text | - | Required |
| Цель `target` | text | - | Required |

##### Объект `TKpiEventType`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Провайдер `provider` | text | - | Required |

##### Объект `TAnomalyDetectorIDsType`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ошибки `errors` | text | - | Optional |
| Доход `revenue` | text | - | Optional |
| Средняя длительность `avgDuration` | text | - | Optional |
| Завершённые потоки `completedFlows` | text | - | Optional |

##### Объект `TEventType`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID `id` | text | - | Required |
| ID корреляции `correlationID` | text | - | Optional |
| Имя `name` | text | - | Required |
| Провайдер `provider` | text | - | Required |
| Является ли ошибкой `isError` | boolean | - | Required |
| Отключено ли `isDisabled` | boolean | - | Required |