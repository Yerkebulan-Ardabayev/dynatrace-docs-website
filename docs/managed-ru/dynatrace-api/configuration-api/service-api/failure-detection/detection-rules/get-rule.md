---
title: Failure detection API - GET a detection rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/get-rule
scraped: 2026-05-12T11:16:19.930786
---

# Failure detection API - GET a detection rule

# Failure detection API - GET a detection rule

* Reference
* Published Jan 11, 2021

Возвращает указанное правило обнаружения сбоев.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого правила обнаружения сбоев. Должен быть валидным UUID по RFC 4122. | path | Required |

## Ответ

Чтобы найти все вариации модели, зависящие от типа модели, смотрите [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Изучите вариации JSON-моделей в Dynatrace API обнаружения сбоев.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [FailureDetectionRule](#openapi-definition-FailureDetectionRule) | Успех |
| **404** | - | Сбой. Указанная сущность не существует. |

### Объекты тела ответа

#### Объект `FailureDetectionRule`

Конфигурация правила обнаружения сбоев.

| Элемент | Тип | Описание |
| --- | --- | --- |
| conditions | [FailureDetectionCondition[]](#openapi-definition-FailureDetectionCondition) | Список условий правила.  Правило применяется, когда выполнены **все** условия. |
| description | string | Краткое описание правила. |
| enabled | boolean | Правило включено (`true`) или отключено (`false`). |
| fdpId | string | Набор параметров обнаружения сбоев (FDP) правила.  Укажите здесь ID набора. Набор FDP должен существовать на момент создания правила. |
| id | string | ID правила. |
| name | string | Отображаемое имя правила.  Длина имени ограничена 150 символами. |

#### Объект `FailureDetectionCondition`

Условие правила обнаружения сбоев.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attribute | string | Проверяемый атрибут. Возможные значения: * `PG_NAME` * `PG_TAG` * `SERVICE_MANAGEMENT_ZONES` * `SERVICE_NAME` * `SERVICE_SERVICE_TYPE` * `SERVICE_TAG` |
| predicate | [FdcPredicate](#openapi-definition-FdcPredicate) | Предикат, проверяющий значение атрибута.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf). |

#### Объект `FdcPredicate`

Предикат, проверяющий значение атрибута.

Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `STRING_EQUALS` -> FdcPredicateStringEquals * `STRING_STARTS_WITH` -> FdcPredicateStringStartsWith * `STRING_ENDS_WITH` -> FdcPredicateStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdcPredicateStringContains * `INTEGER_EQUALS` -> FdcPredicateIntegerEquals * `INTEGER_LESS_THAN` -> FdcPredicateIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdcPredicateIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdcPredicateIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdcPredicateIntegerGreaterThanOrEqual * `LONG_EQUALS` -> FdcPredicateLongEquals * `LONG_LESS_THAN` -> FdcPredicateLongLessThan * `LONG_LESS_THAN_OR_EQUAL` -> FdcPredicateLongLessThanOrEqual * `LONG_GREATER_THAN` -> FdcPredicateLongGreaterThan * `LONG_GREATER_THAN_OR_EQUAL` -> FdcPredicateLongGreaterThanOrEqual * `TAG_KEY_EQUALS` -> FdcPredicateTagKeyEquals * `TAG_EQUALS` -> FdcPredicateTagEquals * `SERVICE_TYPE_EQUALS` -> FdcPredicateServiceTypeEquals * `MANAGEMENT_ZONES_CONTAINS_ALL` -> FdcPredicateManagementZonesContainsAll * `SET_OF_INTEGERS_CONTAINS_ANY` -> FdcPredicateSetOfIntegersContainsAny * `SET_OF_INTEGERS_CONTAINS_ALL` -> FdcPredicateSetOfIntegersContainsAll Возможные значения: * `INTEGER_EQUALS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `LONG_EQUALS` * `LONG_GREATER_THAN` * `LONG_GREATER_THAN_OR_EQUAL` * `LONG_LESS_THAN` * `LONG_LESS_THAN_OR_EQUAL` * `MANAGEMENT_ZONES_CONTAINS_ALL` * `SERVICE_TYPE_EQUALS` * `SET_OF_INTEGERS_CONTAINS_ALL` * `SET_OF_INTEGERS_CONTAINS_ANY` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_STARTS_WITH` * `TAG_EQUALS` * `TAG_KEY_EQUALS` |

### JSON-модели тела ответа

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