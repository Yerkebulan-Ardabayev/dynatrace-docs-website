---
title: Failure detection API - POST a detection rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/post-rule
scraped: 2026-05-12T11:16:21.173769
---

# Failure detection API - POST a detection rule

# Failure detection API - POST a detection rule

* Reference
* Published Jan 11, 2021

Создаёт новое правило обнаружения сбоев.

Новое правило добавляется в конец списка правил. Правила вычисляются сверху вниз; применяется первое совпавшее правило. Чтобы задать определённый порядок, используйте [запрос на изменение порядка](/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules "Изменение порядка правил обнаружения сбоев через Dynatrace API.").

Набор параметров обнаружения сбоев, используемый правилом, должен существовать на момент создания правила.

Запрос возвращает и принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В теле не нужно указывать ID. Идентификатор назначается автоматически Dynatrace и возвращается в составе ответа.

Чтобы найти все вариации модели, зависящие от типа модели, смотрите [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Изучите вариации JSON-моделей в Dynatrace API обнаружения сбоев.").

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [FailureDetectionRule](#openapi-definition-FailureDetectionRule) | JSON-тело запроса. Содержит конфигурацию нового правила обнаружения сбоев.  Dynatrace сгенерирует для вас случайный UUID, если вы не укажете ID. | body | Optional |

### Объекты тела запроса

#### Объект `FailureDetectionRule`

Конфигурация правила обнаружения сбоев.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| conditions | [FailureDetectionCondition[]](#openapi-definition-FailureDetectionCondition) | Список условий правила.  Правило применяется, когда выполнены **все** условия. | Required |
| description | string | Краткое описание правила. | Optional |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). | Required |
| fdpId | string | Набор параметров обнаружения сбоев (FDP) правила.  Укажите здесь ID набора. Набор FDP должен существовать на момент создания правила. | Required |
| id | string | ID правила. | Optional |
| name | string | Отображаемое имя правила.  Длина имени ограничена 150 символами. | Optional |

#### Объект `FailureDetectionCondition`

Условие правила обнаружения сбоев.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| attribute | string | Проверяемый атрибут. Возможные значения: * `PG_NAME` * `PG_TAG` * `SERVICE_MANAGEMENT_ZONES` * `SERVICE_NAME` * `SERVICE_SERVICE_TYPE` * `SERVICE_TAG` | Optional |
| predicate | [FdcPredicate](#openapi-definition-FdcPredicate) | Предикат, проверяющий значение атрибута.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf). | Optional |

#### Объект `FdcPredicate`

Предикат, проверяющий значение атрибута.

Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `STRING_EQUALS` -> FdcPredicateStringEquals * `STRING_STARTS_WITH` -> FdcPredicateStringStartsWith * `STRING_ENDS_WITH` -> FdcPredicateStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdcPredicateStringContains * `INTEGER_EQUALS` -> FdcPredicateIntegerEquals * `INTEGER_LESS_THAN` -> FdcPredicateIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdcPredicateIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdcPredicateIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdcPredicateIntegerGreaterThanOrEqual * `LONG_EQUALS` -> FdcPredicateLongEquals * `LONG_LESS_THAN` -> FdcPredicateLongLessThan * `LONG_LESS_THAN_OR_EQUAL` -> FdcPredicateLongLessThanOrEqual * `LONG_GREATER_THAN` -> FdcPredicateLongGreaterThan * `LONG_GREATER_THAN_OR_EQUAL` -> FdcPredicateLongGreaterThanOrEqual * `TAG_KEY_EQUALS` -> FdcPredicateTagKeyEquals * `TAG_EQUALS` -> FdcPredicateTagEquals * `SERVICE_TYPE_EQUALS` -> FdcPredicateServiceTypeEquals * `MANAGEMENT_ZONES_CONTAINS_ALL` -> FdcPredicateManagementZonesContainsAll * `SET_OF_INTEGERS_CONTAINS_ANY` -> FdcPredicateSetOfIntegersContainsAny * `SET_OF_INTEGERS_CONTAINS_ALL` -> FdcPredicateSetOfIntegersContainsAll Возможные значения: * `INTEGER_EQUALS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `LONG_EQUALS` * `LONG_GREATER_THAN` * `LONG_GREATER_THAN_OR_EQUAL` * `LONG_LESS_THAN` * `LONG_LESS_THAN_OR_EQUAL` * `MANAGEMENT_ZONES_CONTAINS_ALL` * `SERVICE_TYPE_EQUALS` * `SET_OF_INTEGERS_CONTAINS_ALL` * `SET_OF_INTEGERS_CONTAINS_ANY` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_STARTS_WITH` * `TAG_EQUALS` * `TAG_KEY_EQUALS` | Required |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"conditions": [



{



"attribute": "SERVICE_NAME",



"predicate": {



"ignoreCase": false,



"type": "STRING_STARTS_WITH",



"values": [



"shp",



"stg_shp"



]



}



}



],



"description": "for requests from shipping module",



"enabled": true,



"fdpId": "FDP_9",



"id": "R_5",



"name": "shipping"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новое правило обнаружения сбоев создано. Тело ответа содержит ID нового правила. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```