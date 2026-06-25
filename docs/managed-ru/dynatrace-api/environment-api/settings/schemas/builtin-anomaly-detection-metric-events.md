---
title: Settings API - Metric events schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-anomaly-detection-metric-events
scraped: 2026-05-12T11:49:26.446943
---

# Settings API - Metric events schema table

# Settings API - Metric events schema table

* Опубликовано 05 декабря 2023 г.

### Metric events (`builtin:anomaly-detection.metric-events)`

Конфигурации metric event используются для автоматического обнаружения аномалий в metric timeseries по порогам или baseline.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:anomaly-detection.metric-events` | * `group:anomaly-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.metric-events` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:anomaly-detection.metric-events` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:anomaly-detection.metric-events` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Краткое описание `summary` | text | Текстовое краткое описание записи metric event | Required |
| Определение запроса `queryDefinition` | [QueryDefinition](#QueryDefinition) | - | Required |
| Стратегия мониторинга `modelProperties` | [ModelProperties](#ModelProperties) | - | Required |
| Шаблон события `eventTemplate` | [EventTemplate](#EventTemplate) | - | Required |
| Dimension-ключ сущности для событий `eventEntityDimensionKey` | text | Управляет предпочтительным типом сущности, используемым для срабатывающих событий. | Optional |
| Идентификатор конфигурации `legacyId` | text | - | Optional |

##### Объект `QueryDefinition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип `type` | enum | Возможные значения: * `METRIC_KEY` * `METRIC_SELECTOR` | Required |
| Metric selector `metricSelector` | text | Подробнее см. [Metric Selector](https://dt-url.net/metselad) | Required |
| Ключ метрики `metricKey` | text | - | Required |
| Агрегация `aggregation` | enum | Возможные значения: * `MIN` * `MAX` * `SUM` * `COUNT` * `AVG` * `VALUE` * `MEDIAN` * `PERCENTILE90` | Required |
| Management zone `managementZone` | text | - | Optional |
| Сдвиг запроса `queryOffset` | integer | Сдвиг скользящего evaluation window в минутах для метрик с задержкой | Optional |
| Сущности `entityFilter` | [EntityFilter](#EntityFilter) | Используйте rule-based фильтры, чтобы задать область, которую отслеживает это событие. | Required |
| Dimension filter `dimensionFilter` | [DimensionFilter](#DimensionFilter)[] | - | Required |

##### Объект `ModelProperties`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип модели `type` | enum | Query-definition по metric key поддерживают только статические пороги. Возможные значения: * `STATIC_THRESHOLD` * `AUTO_ADAPTIVE_THRESHOLD` * `SEASONAL_BASELINE` | Required |
| Порог `threshold` | float | Создавать событие при нарушении этого значения | Required |
| Оповещать при отсутствии данных `alertOnNoData` | boolean | Возможность задать оповещение об отсутствии данных в метрике. Если включено, missing data samples трактуются как нарушающие samples, определённые в advanced model properties. Если отключено, отсутствие данных не считается нарушением, но всё равно влияет на dealerting. Для разрежённых timeseries рекомендуется отключить оповещения по missing data, чтобы избежать ложных алертов. Подробнее см. [anomaly detection configuration](https://dt-url.net/lz02mwi). | Required |
| Число колебаний сигнала `signalFluctuation` | float | Управляет тем, сколько раз значение колебания сигнала прибавляется к baseline для получения фактического порога оповещения | Required |
| Tolerance `tolerance` | float | Управляет шириной confidence band; чем больше значение, тем менее чувствительна модель | Required |
| Условие оповещения `alertCondition` | enum | Возможные значения: * `ABOVE` * `BELOW` * `OUTSIDE` | Required |
| Нарушающие samples `violatingSamples` | integer | Сколько одноминутных samples в evaluation window должны нарушить условие, чтобы событие сработало. | Required |
| Скользящее окно `samples` | integer | Сколько одноминутных samples формируют скользящее evaluation window. | Required |
| Dealerting samples `dealertingSamples` | integer | Сколько одноминутных samples в evaluation window должны вернуться к норме, чтобы событие закрылось. | Required |

##### Объект `EventTemplate`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Заголовок `title` | text | Заголовок события, которое нужно триггернуть. Введите '{' для подсказок по плейсхолдерам. | Required |
| Описание `description` | text | Описание события, которое нужно триггернуть. Введите '{' для подсказок по плейсхолдерам. | Required |
| Тип события `eventType` | enum | Тип события, которое нужно триггернуть. Возможные значения: * `INFO` * `ERROR` * `AVAILABILITY` * `SLOWDOWN` * `RESOURCE` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `MARKED_FOR_TERMINATION` * `WARNING` | Required |
| Разрешить объединение `davisMerge` | boolean | DavisÂ® AI попытается смержить это событие в существующие problems, иначе всегда будет создаваться новая problem. | Required |
| Свойства `metadata` | Set<[MetadataItem](#MetadataItem)> | Набор дополнительных key-value свойств, прикрепляемых к срабатывающему событию. Получить список доступных property keys можно через [Events API v2](https://dt-url.net/9622g1w). | Required |

##### Объект `EntityFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Dimension-ключ типа сущности `dimensionKey` | text | Dimension-ключ типа сущности для фильтрации | Optional |
| `conditions` | [EntityFilterCondition](#EntityFilterCondition)[] | - | Required |

##### Объект `DimensionFilter`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Dimension-ключ `dimensionKey` | text | - | Required |
| Оператор `operator` | enum | Возможные значения: * `EQUALS` * `DOES_NOT_EQUAL` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `CONTAINS_CASE_SENSITIVE` * `DOES_NOT_CONTAIN_CASE_SENSITIVE` | Optional |
| Значение dimension `dimensionValue` | text | - | Required |

##### Объект `MetadataItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `metadataKey` | text | Введите 'dt.' для подсказок по ключам. | Required |
| Значение `metadataValue` | text | Введите '{' для подсказок по плейсхолдерам. | Required |

##### Объект `EntityFilterCondition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип фильтра `type` | enum | Возможные значения: * `NAME` * `ENTITY_ID` * `MANAGEMENT_ZONE` * `TAG` * `HOST_NAME` * `HOST_GROUP_NAME` * `PROCESS_GROUP_NAME` * `PROCESS_GROUP_ID` * `CUSTOM_DEVICE_GROUP_NAME` | Required |
| Оператор `operator` | enum | Возможные значения: * `EQUALS` * `DOES_NOT_EQUAL` * `STARTS_WITH` * `DOES_NOT_START_WITH` * `CONTAINS_CASE_SENSITIVE` * `DOES_NOT_CONTAIN_CASE_SENSITIVE` * `CONTAINS_CASE_INSENSITIVE` * `DOES_NOT_CONTAIN_CASE_INSENSITIVE` | Required |
| Значение `value` | text | - | Required |