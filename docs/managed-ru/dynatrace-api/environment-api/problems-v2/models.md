---
title: Problems API v2 - JSON-модели
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/models
scraped: 2026-05-12T12:09:51.787604
---

# Problems API v2 - JSON-модели

# Problems API v2 - JSON-модели

* Справочник
* Опубликовано 12 октября 2020 г.

Некоторые JSON-модели API **Problems v2** различаются в зависимости от **type** модели. JSON-модели для каждой вариации перечислены ниже.

## Вариации объекта `Evidence`

Объект `Evidence`, это базовый объект для доказательств (evidence) проблемы. Фактический набор полей зависит от **type** доказательства.

### AVAILABILITY\_EVIDENCE

AvailabilityEvidenceMetadata

Параметры

JSON-модель

#### Объект `AvailabilityEvidence`

Доказательство по доступности для проблемы.

Указывает на сущность, которая была недоступна в течение жизненного цикла проблемы и может быть связана с первопричиной.

| Поле | Тип | Описание |
| --- | --- | --- |
| endTime | integer | Время окончания доказательства, в UTC миллисекундах. |

```
{



"evidenceType": "AVAILABILITY_EVIDENCE",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602500000000,



"endTime": 1602600000000



}
```

### EVENT

EventEvidenceMetadata

Параметры

JSON-модель

#### Объект `EventEvidence`

Доказательство по событию для проблемы.

Событие, произошедшее в течение жизненного цикла проблемы, которое может быть связано с первопричиной.

| Поле | Тип | Описание |
| --- | --- | --- |
| data | [Event](#openapi-definition-Event) | Конфигурация события. |
| endTime | integer | Метка времени окончания события, в UTC миллисекундах. Имеет значение `-1`, если событие ещё активно. |
| eventId | string | ID события. |
| eventType | string | Тип события. |

#### Объект `Event`

Конфигурация события.

| Поле | Тип | Описание |
| --- | --- | --- |
| correlationId | string | Корреляционный ID события. |
| endTime | integer | Метка времени, когда событие было закрыто, в UTC миллисекундах. Имеет значение `null`, если событие ещё активно. |
| entityId | [EntityStub](#openapi-definition-EntityStub) | Краткое представление отслеживаемой сущности. |
| entityTags | [METag[]](#openapi-definition-METag) | Список тегов связанной сущности. |
| eventId | string | ID события. |
| eventType | string | Тип события. |
| frequentEvent | boolean | Если `true`, событие происходит [часто](https://dt-url.net/4da3kdg?dt=m). Частое событие не вызывает проблему. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | Список всех зон управления, к которым относится событие. |
| properties | [EventProperty[]](#openapi-definition-EventProperty) | Список свойств события. |
| startTime | integer | Метка времени, когда событие было поднято, в UTC миллисекундах. |
| status | string | Статус события. Поле может принимать значения: * `CLOSED` * `OPEN` |
| suppressAlert | boolean | Статус оповещения во время [обслуживания (maintenance)](https://dt-url.net/b2123rg0?dt=m): * `false`: оповещения работают как обычно. * `true`: оповещения отключены. |
| suppressProblem | boolean | Статус детекции проблем во время [обслуживания (maintenance)](https://dt-url.net/b2123rg0?dt=m): * `false`: детекция проблем работает как обычно. * `true`: детекция проблем отключена. |
| title | string | Заголовок события. |
| underMaintenance | boolean | Если `true`, событие произошло, когда отслеживаемая система находилась на обслуживании. |

#### Объект `EntityStub`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | Краткое представление отслеживаемой сущности. |
| name | string | Имя сущности. Не включается в ответ, если сущность с соответствующим ID не найдена. |

#### Объект `EntityId`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

#### Объект `METag`

Тег отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| context | string | Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| stringRepresentation | string | Строковое представление тега. |
| value | string | Значение тега. |

#### Объект `ManagementZone`

Краткое представление зоны управления.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID зоны управления. |
| name | string | Имя зоны управления. |

#### Объект `EventProperty`

Свойство события.

| Поле | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ свойства события. |
| value | string | Значение свойства события. |

```
{



"evidenceType": "EVENT",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602511312869,



"eventId": "string",



"eventType": "string"



}
```

### MAINTENANCE\_WINDOW

MaintenanceWindowEvidenceMetadata

Параметры

JSON-модель

#### Объект `MaintenanceWindowEvidence`

Доказательство по окну обслуживания для проблемы.

Окно обслуживания, в течение которого возникла проблема.

| Поле | Тип | Описание |
| --- | --- | --- |
| endTime | integer | Время окончания доказательства, в UTC миллисекундах. |
| maintenanceWindowConfigId | string | ID связанного окна обслуживания. |

```
{



"evidenceType": "MAINTENANCE_WINDOW",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602500000000,



"maintenanceWindowConfigId": "string",



"endTime": 1602600000000



}
```

### METRIC

MetricEvidenceMetadata

Параметры

JSON-модель

#### Объект `MetricEvidence`

Доказательство по метрике для проблемы.

Изменение поведения метрики, которое указывает на проблему и/или является её первопричиной.

| Поле | Тип | Описание |
| --- | --- | --- |
| endTime | integer | Время окончания доказательства, в UTC миллисекундах. Значение `null` означает, что доказательство всё ещё открыто. |
| metricId | string | ID метрики. |
| unit | string | Единица измерения метрики. Поле может принимать значения: * `Ampere` * `Billion` * `Bit` * `BitPerHour` * `BitPerMinute` * `BitPerSecond` * `Byte` * `BytePerHour` * `BytePerMinute` * `BytePerSecond` * `Cores` * `Count` * `Day` * `DecibelMilliWatt` * `GibiByte` * `GibiBytePerHour` * `GibiBytePerMinute` * `GibiBytePerSecond` * `Giga` * `GigaByte` * `GigaBytePerHour` * `GigaBytePerMinute` * `GigaBytePerSecond` * `Hertz` * `Hour` * `KibiByte` * `KibiBytePerHour` * `KibiBytePerMinute` * `KibiBytePerSecond` * `Kilo` * `KiloByte` * `KiloBytePerHour` * `KiloBytePerMinute` * `KiloBytePerSecond` * `KiloMetrePerHour` * `MSU` * `MebiByte` * `MebiBytePerHour` * `MebiBytePerMinute` * `MebiBytePerSecond` * `Mega` * `MegaByte` * `MegaBytePerHour` * `MegaBytePerMinute` * `MegaBytePerSecond` * `MetrePerHour` * `MetrePerSecond` * `MicroSecond` * `MilliCores` * `MilliSecond` * `MilliSecondPerMinute` * `Million` * `Minute` * `Month` * `NanoSecond` * `NanoSecondPerMinute` * `NotApplicable` * `PerHour` * `PerMinute` * `PerSecond` * `Percent` * `Pixel` * `Promille` * `Ratio` * `Second` * `State` * `Trillion` * `Unspecified` * `Volt` * `Watt` * `Week` * `Year` |
| valueAfterChangePoint | number | Значение метрики после начала проблемы. |
| valueBeforeChangePoint | number | Значение метрики до начала проблемы. |

```
{



"evidenceType": "METRIC",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602500000000,



"metricId": "string",



"valueBeforeChangePoint": 2,



"valueAfterChangePoint": 3,



"unit": "Count",



"endTime": 1602600000000



}
```

### TRANSACTIONAL

TransactionalEvidenceMetadata

Параметры

JSON-модель

#### Объект `TransactionalEvidence`

Транзакционное доказательство для проблемы.

Поведение метрики в транзакции, которое указывает на проблему и/или является её первопричиной.

| Поле | Тип | Описание |
| --- | --- | --- |
| endTime | integer | Время окончания доказательства, в UTC миллисекундах. |
| unit | string | Единица измерения метрики. |
| valueAfterChangePoint | number | Значение метрики после начала проблемы. |
| valueBeforeChangePoint | number | Значение метрики до начала проблемы. |

```
{



"evidenceType": "TRANSACTIONAL",



"displayName": "string",



"entity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"groupingEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"rootCauseRelevant": true,



"startTime": 1602500000000,



"valueBeforeChangePoint": 2,



"valueAfterChangePoint": 3,



"unit": "Count",



"endTime": 1602600000000



}
```

## Вариации объекта `Impact`

Объект `Impact`, это базовый объект для воздействий (impact) проблемы. Фактический набор полей зависит от **type** воздействия.

### APPLICATION

ApplicationImpactDto

Параметры

JSON-модель

#### Объект `ApplicationImpact`

Анализ воздействия проблемы на приложение.

| Поле | Тип | Описание |
| --- | --- | --- |
| estimatedAffectedUsers | integer | Оценочное число затронутых пользователей. |
| impactType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов: * `SERVICE` -> ServiceImpact * `APPLICATION` -> ApplicationImpact * `MOBILE` -> MobileImpact * `CUSTOM_APPLICATION` -> CustomApplicationImpact Поле может принимать значения: * `APPLICATION` * `CUSTOM_APPLICATION` * `MOBILE` * `SERVICE` |
| impactedEntity | [EntityStub](#openapi-definition-EntityStub) | Краткое представление отслеживаемой сущности. |

#### Объект `EntityStub`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | Краткое представление отслеживаемой сущности. |
| name | string | Имя сущности. Не включается в ответ, если сущность с соответствующим ID не найдена. |

#### Объект `EntityId`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

```
{



"impactType": "APPLICATION",



"impactedEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"estimatedAffectedUsers": 5



}
```

### CUSTOM\_APPLICATION

CustomApplicationImpactDto

Параметры

JSON-модель

#### Объект `CustomApplicationImpact`

Анализ воздействия проблемы на пользовательское приложение.

| Поле | Тип | Описание |
| --- | --- | --- |
| estimatedAffectedUsers | integer | Оценочное число затронутых пользователей. |
| impactType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов: * `SERVICE` -> ServiceImpact * `APPLICATION` -> ApplicationImpact * `MOBILE` -> MobileImpact * `CUSTOM_APPLICATION` -> CustomApplicationImpact Поле может принимать значения: * `APPLICATION` * `CUSTOM_APPLICATION` * `MOBILE` * `SERVICE` |
| impactedEntity | [EntityStub](#openapi-definition-EntityStub) | Краткое представление отслеживаемой сущности. |

#### Объект `EntityStub`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | Краткое представление отслеживаемой сущности. |
| name | string | Имя сущности. Не включается в ответ, если сущность с соответствующим ID не найдена. |

#### Объект `EntityId`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

```
{



"impactType": "CUSTOM_APPLICATION",



"impactedEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"estimatedAffectedUsers": 5



}
```

### MOBILE

MobileImpactDto

Параметры

JSON-модель

#### Объект `MobileImpact`

Анализ воздействия проблемы на мобильное приложение.

| Поле | Тип | Описание |
| --- | --- | --- |
| estimatedAffectedUsers | integer | Оценочное число затронутых пользователей. |
| impactType | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов: * `SERVICE` -> ServiceImpact * `APPLICATION` -> ApplicationImpact * `MOBILE` -> MobileImpact * `CUSTOM_APPLICATION` -> CustomApplicationImpact Поле может принимать значения: * `APPLICATION` * `CUSTOM_APPLICATION` * `MOBILE` * `SERVICE` |
| impactedEntity | [EntityStub](#openapi-definition-EntityStub) | Краткое представление отслеживаемой сущности. |

#### Объект `EntityStub`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | Краткое представление отслеживаемой сущности. |
| name | string | Имя сущности. Не включается в ответ, если сущность с соответствующим ID не найдена. |

#### Объект `EntityId`

Краткое представление отслеживаемой сущности.

| Поле | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

```
{



"impactType": "MOBILE",



"impactedEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"estimatedAffectedUsers": 5



}
```

### SERVICE

ServiceImpactDto

Параметры

JSON-модель

#### Объект `ServiceImpact`

Анализ воздействия проблемы на сервис.

| Поле | Тип | Описание |
| --- | --- | --- |
| numberOfPotentiallyAffectedServiceCalls | integer | Количество потенциально затронутых сервисов. |

```
{



"impactType": "SERVICE",



"impactedEntity": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"estimatedAffectedUsers": 5,



"numberOfPotentiallyAffectedServiceCalls": 50



}
```