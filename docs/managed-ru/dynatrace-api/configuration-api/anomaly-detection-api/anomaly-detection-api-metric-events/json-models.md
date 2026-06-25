---
title: Metric events anomaly detection API - JSON models
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-metric-events/json-models
scraped: 2026-05-12T12:16:15.089523
---

# Metric events anomaly detection API - JSON models

# Metric events anomaly detection API - JSON models

* Reference
* Updated on Apr 26, 2023
* Deprecated

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Metric events** (`builtin:anomaly-detection.metric-events`).

Некоторые JSON-модели API **Metric events anomaly detection** различаются в зависимости от поля **filterType** некоторых объектов. JSON-модели для каждой вариации перечислены ниже.

## Вариации объекта `MetricEventAlertingScope`

Объект `MetricEventAlertingScope` является базовым для областей действия оповещений metric event. Фактический набор полей зависит от поля **filterType** области действия.

### CUSTOM\_DEVICE\_GROUP\_NAME

CustomDeviceGroupNameAlertingScope

Parameters

JSON model

#### Объект `CustomDeviceGroupNameAlertingScope`

Фильтр области действия для имени связанной группы пользовательских устройств.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | Фильтр строкового значения на основе заданного оператора. |

#### Объект `MetricEventTextFilterMetricEventTextFilterOperatorDto`

Фильтр строкового значения на основе заданного оператора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор для сопоставления. Возможные значения: * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | Значение для сопоставления. |

```
{



"filterType": "CUSTOM_DEVICE_GROUP_NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### ENTITY\_ID

EntityIdAlertingScope

Parameters

JSON model

#### Объект `EntityIdAlertingScope`

Фильтр области действия для идентификатора отслеживаемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityId | string | ID отслеживаемых сущностей для сопоставления. |

```
{



"filterType": "ENTITY_ID",



"entityId": "HOST-B7A6F9EE9F366CB5"



}
```

### HOST\_NAME

HostNameAlertingScope

Parameters

JSON model

#### Объект `HostNameAlertingScope`

Фильтр области действия для имени связанного хоста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | Фильтр строкового значения на основе заданного оператора. |

#### Объект `MetricEventTextFilterMetricEventTextFilterOperatorDto`

Фильтр строкового значения на основе заданного оператора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор для сопоставления. Возможные значения: * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | Значение для сопоставления. |

```
{



"filterType": "HOST_NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### HOST\_GROUP\_NAME

HostGroupNameAlertingScope

Parameters

JSON model

#### Объект `HostGroupNameAlertingScope`

Фильтр области действия для имени связанной группы хостов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | Фильтр строкового значения на основе заданного оператора. |

#### Объект `MetricEventTextFilterMetricEventTextFilterOperatorDto`

Фильтр строкового значения на основе заданного оператора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор для сопоставления. Возможные значения: * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | Значение для сопоставления. |

```
{



"filterType": "HOST_GROUP_NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### MANAGEMENT\_ZONE

ManagementZoneAlertingScope

Parameters

JSON model

#### Объект `ManagementZoneAlertingScope`

Фильтр области действия для идентификатора зоны управления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| mzId | string | ID зоны управления для сопоставления. |

```
{



"filterType": "MANAGEMENT_ZONE",



"mzId": "6958644387494623526"



}
```

### NAME

NameAlertingScope

Parameters

JSON model

#### Объект `NameAlertingScope`

Фильтр области действия для имени отслеживаемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | Фильтр строкового значения на основе заданного оператора. |

#### Объект `MetricEventTextFilterMetricEventTextFilterOperatorDto`

Фильтр строкового значения на основе заданного оператора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор для сопоставления. Возможные значения: * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | Значение для сопоставления. |

```
{



"filterType": "NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### PROCESS\_GROUP\_ID

ProcessGroupIdAlertingScope

Parameters

JSON model

#### Объект `ProcessGroupIdAlertingScope`

Фильтр области действия для идентификатора группы процессов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| processGroupId | string | ID групп процессов для сопоставления. |

```
{



"filterType": "PROCESS_GROUP_ID",



"processGroupId": "PROCESS_GROUP-B34081EFF9E5F516"



}
```

### PROCESS\_GROUP\_NAME

ProcessGroupNameAlertingScope

Parameters

JSON model

#### Объект `ProcessGroupNameAlertingScope`

Фильтр области действия для имени связанной группы процессов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventTextFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventTextFilterOperatorDto) | Фильтр строкового значения на основе заданного оператора. |

#### Объект `MetricEventTextFilterMetricEventTextFilterOperatorDto`

Фильтр строкового значения на основе заданного оператора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор для сопоставления. Возможные значения: * `CONTAINS_CASE_INSENSITIVE` * `CONTAINS_CASE_SENSITIVE` * `EQUALS` |
| value | string | Значение для сопоставления. |

```
{



"filterType": "PROCESS_GROUP_NAME",



"nameFilter": {



"value": "entity name",



"operator": "CONTAINS_CASE_INSENSITIVE"



}



}
```

### TAG

TagFilterAlertingScope

Parameters

JSON model

#### Объект `TagFilterAlertingScope`

Фильтр области действия для тегов на сущностях.

| Элемент | Тип | Описание |
| --- | --- | --- |
| tagFilter | [TagFilter](#openapi-definition-TagFilter) | Фильтр отслеживаемых сущностей на основе тегов. |

#### Объект `TagFilter`

Фильтр отслеживаемых сущностей на основе тегов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. Возможные значения: * `AWS` * `AWS_GENERIC` * `AZURE` * `CLOUD_FOUNDRY` * `CONTEXTLESS` * `ENVIRONMENT` * `GOOGLE_CLOUD` * `KUBERNETES` |
| key | string | Ключ тега.  У пользовательских тегов здесь находится значение тега. |
| value | string | Значение тега.  Не применимо к пользовательским тегам. |

```
{



"filterType": "TAG",



"tagFilter": {



"context": "CONTEXTLESS",



"key": "Infrastructure",



"value": "Linux"



}



}
```

## Вариации объекта `MetricEventDimensions`

Объект `MetricEventDimensions` является базовым для измерений метрик. Фактический набор полей зависит от поля **filterType** измерения.

### ENTITY

MetricEventEntityDimensions

Parameters

JSON model

#### Объект `MetricEventEntityDimensions`

Фильтр для измерений сущностей метрик.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nameFilter | [MetricEventTextFilterMetricEventDimensionsFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventDimensionsFilterOperatorDto) | Фильтр строкового значения на основе заданного оператора. |

#### Объект `MetricEventTextFilterMetricEventDimensionsFilterOperatorDto`

Фильтр строкового значения на основе заданного оператора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор для сопоставления. Возможные значения: * `EQUALS` |
| value | string | Значение для сопоставления. |

```
{



"filterType": "ENTITY",



"name": "dimension",



"index": 1,



"nameFilter": {



"value": "entity name",



"operator": "EQUALS"



}



}
```

### STRING

MetricEventStringDimensions

Parameters

JSON model

#### Объект `MetricEventStringDimensions`

Фильтр для строковых измерений метрик.

| Элемент | Тип | Описание |
| --- | --- | --- |
| textFilter | [MetricEventTextFilterMetricEventDimensionsFilterOperatorDto](#openapi-definition-MetricEventTextFilterMetricEventDimensionsFilterOperatorDto) | Фильтр строкового значения на основе заданного оператора. |

#### Объект `MetricEventTextFilterMetricEventDimensionsFilterOperatorDto`

Фильтр строкового значения на основе заданного оператора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| operator | string | Оператор для сопоставления. Возможные значения: * `EQUALS` |
| value | string | Значение для сопоставления. |

```
{



"filterType": "STRING",



"name": "dimension",



"index": 1,



"textFilter": {



"value": "entity name",



"operator": "EQUALS"



}



}
```

## Вариации объекта `MetricEventMonitoringStrategy`

Объект `MetricEventMonitoringStrategy` является базовым для стратегии мониторинга metric event. Фактический набор полей зависит от поля **type** стратегии.

### AUTO\_ADAPTIVE\_BASELINE

MetricEventAutoAdaptiveBaselineMonitoringStrategy

Parameters

JSON model

#### Объект `MetricEventAutoAdaptiveBaselineMonitoringStrategy`

Авто-адаптивная базовая стратегия для обнаружения аномалий в метриках, которые регулярно меняются со временем, поскольку базовая линия также обновляется автоматически. Пример: обнаружение аномалии в числе принятых сетевых пакетов или в числе действий пользователей со временем.

| Элемент | Тип | Описание |
| --- | --- | --- |
| alertCondition | string | Условие проверки значения **threshold**: выше или ниже. Возможные значения: * `ABOVE` * `BELOW` |
| alertingOnMissingData | boolean | Если true, одноминутные замеры без данных также считаются нарушающими. |
| dealertingSamples | integer | Число одноминутных замеров в окне оценки, которые должны вернуться к норме, чтобы закрыть событие. |
| numberOfSignalFluctuations | number | Определяет коэффициент того, сколько флуктуаций сигнала допустимо. Значения выше базовой линии плюс флуктуация сигнала, умноженная на число допустимых флуктуаций сигнала, вызывают оповещение. |
| samples | integer | Число одноминутных замеров, образующих скользящее окно оценки. |
| violatingSamples | integer | Число одноминутных замеров в окне оценки, которые должны нарушить порог, чтобы вызвать событие. |

```
{



"type": "AUTO_ADAPTIVE_BASELINE",



"samples": 5,



"violatingSamples": 3,



"dealertingSamples": 5,



"alertCondition": "ABOVE",



"alertingOnMissingData": false,



"numberOfSignalFluctuations": 1.0



}
```

### STATIC\_THRESHOLD

MetricEventStaticThresholdMonitoringStrategy

Parameters

JSON model

#### Объект `MetricEventStaticThresholdMonitoringStrategy`

Стратегия мониторинга по статическому порогу для оповещения о жёстких ограничениях в заданной метрике. Пример: нарушение критического лимита памяти.

| Элемент | Тип | Описание |
| --- | --- | --- |
| alertCondition | string | Условие проверки значения **threshold**: выше или ниже. Возможные значения: * `ABOVE` * `BELOW` |
| alertingOnMissingData | boolean | Если true, одноминутные замеры без данных также считаются нарушающими. |
| dealertingSamples | integer | Число одноминутных замеров в окне оценки, которые должны вернуться к норме, чтобы закрыть событие. |
| samples | integer | Число одноминутных замеров, образующих скользящее окно оценки. |
| threshold | number | Значение статического порога на основе указанной единицы. |
| unit | string | Единица порога, соответствующая определению метрики. Возможные значения: * `AMPERE` * `BILLION` * `BIT` * `BIT_PER_HOUR` * `BIT_PER_MINUTE` * `BIT_PER_SECOND` * `BYTE` * `BYTE_PER_HOUR` * `BYTE_PER_MINUTE` * `BYTE_PER_SECOND` * `CORES` * `COUNT` * `DAY` * `DECIBEL_MILLI_WATT` * `GIBI_BYTE` * `GIBI_BYTE_PER_HOUR` * `GIBI_BYTE_PER_MINUTE` * `GIBI_BYTE_PER_SECOND` * `GIGA` * `GIGA_BYTE` * `GIGA_BYTE_PER_HOUR` * `GIGA_BYTE_PER_MINUTE` * `GIGA_BYTE_PER_SECOND` * `HERTZ` * `HOUR` * `KIBI_BYTE` * `KIBI_BYTE_PER_HOUR` * `KIBI_BYTE_PER_MINUTE` * `KIBI_BYTE_PER_SECOND` * `KILO` * `KILO_BYTE` * `KILO_BYTE_PER_HOUR` * `KILO_BYTE_PER_MINUTE` * `KILO_BYTE_PER_SECOND` * `KILO_METRE_PER_HOUR` * `MEBI_BYTE` * `MEBI_BYTE_PER_HOUR` * `MEBI_BYTE_PER_MINUTE` * `MEBI_BYTE_PER_SECOND` * `MEGA` * `MEGA_BYTE` * `MEGA_BYTE_PER_HOUR` * `MEGA_BYTE_PER_MINUTE` * `MEGA_BYTE_PER_SECOND` * `METRE_PER_HOUR` * `METRE_PER_SECOND` * `MICRO_SECOND` * `MILLION` * `MILLI_CORES` * `MILLI_SECOND` * `MILLI_SECOND_PER_MINUTE` * `MINUTE` * `MONTH` * `MSU` * `NANO_SECOND` * `NANO_SECOND_PER_MINUTE` * `NOT_APPLICABLE` * `PERCENT` * `PER_HOUR` * `PER_MINUTE` * `PER_SECOND` * `PIXEL` * `PROMILLE` * `RATIO` * `SECOND` * `STATE` * `TRILLION` * `UNSPECIFIED` * `VOLT` * `WATT` * `WEEK` * `YEAR` |
| violatingSamples | integer | Число одноминутных замеров в окне оценки, которые должны нарушить порог, чтобы вызвать событие. |

```
{



"type": "STATIC_THRESHOLD",



"samples": 3,



"violatingSamples": 1,



"dealertingSamples": 3,



"alertCondition": "BELOW",



"alertingOnMissingData": false,



"threshold": 99,



"unit": "COUNT"



}
```