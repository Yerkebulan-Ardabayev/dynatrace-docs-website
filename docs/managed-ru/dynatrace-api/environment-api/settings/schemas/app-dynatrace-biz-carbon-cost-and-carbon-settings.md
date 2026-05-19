---
title: Settings API - Cost & Carbon Optimization schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-biz-carbon-cost-and-carbon-settings
scraped: 2026-05-12T11:44:13.934702
---

# Settings API - Cost & Carbon Optimization schema table

# Settings API - Cost & Carbon Optimization schema table

* Published Mar 17, 2025

### Cost & Carbon Optimization (`app:dynatrace.biz.carbon:cost-and-carbon-settings)`

Настройки для AppEngine-приложения Cost & Carbon Optimization.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.biz.carbon:cost-and-carbon-settings` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.carbon:cost-and-carbon-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.biz.carbon:cost-and-carbon-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.carbon:cost-and-carbon-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID workflow `workflowId` | text | - | Optional |
| Ключ API GCP `gcpApiKey` | secret | - | Optional |
| Собирать ли затраты `isCostCollected` | boolean | - | Optional |
| Оптимизация простоя `idlingThresholds` | [TThreshold](#TThreshold) | - | Optional |
| Оптимизация размеров `sizingThresholds` | [TThreshold](#TThreshold) | - | Optional |
| Переопределения дата-центра `customDatacenterOverrides` | [TDataCenterValueOverrides](#TDataCenterValueOverrides)[] | - | Required |
| Индикатор эффективности бизнес-здоровья `businessHealth` | [TBusinessHealth](#TBusinessHealth) | - | Optional |

##### Объект `TThreshold`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Получение по сети `networkReceiving` | [TNetworkThreshold](#TNetworkThreshold) | - | Required |
| Передача по сети `networkTransmitting` | [TNetworkThreshold](#TNetworkThreshold) | - | Required |
| Cpu `cpu` | [TCpuThreshold](#TCpuThreshold) | - | Required |
| Память `memory` | [TCpuThreshold](#TCpuThreshold) | - | Required |

##### Объект `TDataCenterValueOverrides`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID дата-центра `dataCenterId` | text | - | Optional |
| Id `pue` | float | - | Optional |
| Углеродоёмкость `ci` | float | - | Optional |
| Последнее обновление PUE `pueLastUpdate` | zoned\_date\_time | - | Optional |
| Последнее обновление углеродоёмкости `ciLastUpdate` | zoned\_date\_time | - | Optional |

##### Объект `TBusinessHealth`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Событие `event` | [TBusinessEvent](#TBusinessEvent) | - | Required |

##### Объект `TNetworkThreshold`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Значение `value` | integer | - | Required |
| Единица `unit` | enum | Возможные значения: * `bytes/s` * `kilobytes/s` * `megabytes/s` * `gigabytes/s` | Required |

##### Объект `TCpuThreshold`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Порог CPU [%] `value` | integer | - | Required |
| Единица `unit` | enum | Возможные значения: * `%` | Required |

##### Объект `TBusinessEvent`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Выбрать событие `id` | [TBusinessEventId](#TBusinessEventId) | - | Optional |
| Выбрать KPI `attribute` | text | - | Optional |
| Единица KPI `unit` | text | - | Optional |

##### Объект `TBusinessEventId`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Провайдер `provider` | text | - | Required |
| Имя `name` | text | - | Required |