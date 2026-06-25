---
title: Failure detection API - POST a parameter set
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/post-parameter-set
scraped: 2026-05-12T11:16:16.351421
---

# Failure detection API - POST a parameter set

# Failure detection API - POST a parameter set

* Reference
* Published Jan 11, 2021

Создаёт новый набор параметров обнаружения сбоев.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В теле не нужно указывать ID. Идентификатор назначается автоматически Dynatrace и возвращается в составе ответа.

Чтобы найти все вариации модели, зависящие от типа модели, смотрите [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Изучите вариации JSON-моделей в Dynatrace API обнаружения сбоев.").

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [FailureDetectionParameterSet](#openapi-definition-FailureDetectionParameterSet) | JSON-тело запроса. Содержит новый набор параметров обнаружения сбоев.  Dynatrace сгенерирует для вас случайный UUID, если вы не укажете ID. | body | Optional |

### Объекты тела запроса

#### Объект `FailureDetectionParameterSet`

Набор параметров обнаружения сбоев (FDP).

Эти параметры определяют условия сбоя и успеха.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| brokenLinkDomains | string[] | Список доменов для особой обработки HTTP-кода ответа 404.  Если верхний домен *Referer* присутствует в списке ИЛИ равен верхнему домену хоста запроса, код 404 считается сбоем.  Применимо только когда **isHttp404NotFoundFailureEnabled** установлено в `true`. | Optional |
| clientSideMissingHttpCodeIsFailure | boolean | Отсутствующий HTTP-код ответа на стороне клиента считается сбоем (`true`) или успехом (`false`).  Если не задано, используется `false`. | Optional |
| description | string | Краткое описание набора FDP. | Optional |
| exceptionOnAnyNodeExceptionPatterns | [ExceptionPattern[]](#openapi-definition-ExceptionPattern) | Список ошибочных исключений.  Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем. | Optional |
| failingHttpCodesClientSide | string | Список HTTP-кодов ответа на стороне клиента, которые считаются сбоем.  Формат это список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`).  Если не задано, используется диапазон `400-599`. | Optional |
| failingHttpCodesServerSide | string | Список HTTP-кодов ответа на стороне сервера, которые считаются сбоем.  Формат это список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`).Если не задано, используется диапазон `500-599`. | Optional |
| http404NotFoundFailureEnabled | boolean | Особая обработка HTTP-кода ответа 404 включена (`true`) или отключена (`false`). Подробности особой обработки см. в **brokenLinkDomains**.  Применимо только когда 404 НЕ входит в список HTTP-кодов ответа, считающихся сбоем, и только для стороны сервера.  Если не задано, используется `false`. | Optional |
| id | string | ID набора параметров. | Optional |
| ignoreAllExceptions | boolean | Если установлено в true, все исключения будут игнорироваться. Это означает, что заданные шаблоны исключений не будут иметь никакого эффекта. | Optional |
| ignoreSpanFailureDetection | boolean | Если установлено в true, обнаружение сбоев по span будет игнорироваться. | Optional |
| ignoredExceptionPatterns | [ExceptionPattern[]](#openapi-definition-ExceptionPattern) | Список игнорируемых исключений.  Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно игнорируется обнаружением сбоев. | Optional |
| name | string | Отображаемое имя набора FDP.  Длина имени ограничена 150 символами. | Optional |
| serverSideMissingHttpCodeIsFailure | boolean | Отсутствующий HTTP-код ответа на стороне сервера считается сбоем (`true`) или успехом (`false`).  Если не задано, используется `false`. | Optional |
| successForcingExceptionPatterns | [ExceptionPattern[]](#openapi-definition-ExceptionPattern) | Список исключений успеха.  Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно считается успехом. | Optional |
| tagConditions | [FdpTagCondition[]](#openapi-definition-FdpTagCondition) | Список условий на основе тегов.  Если выполнено *любое* условие, запрос считается сбоем. | Optional |

#### Объект `ExceptionPattern`

Список ошибочных исключений.

Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| classPattern | string | - | Optional |
| messagePattern | string | - | Optional |

#### Объект `FdpTagCondition`

Конфигурация условия по тегу в наборе FDP.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| predicate | [FdpTagPredicate](#openapi-definition-FdpTagPredicate) | Предикат, проверяющий значение тега.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf). | Required |
| tagKey | string | Ключ проверяемого тега. | Required |

#### Объект `FdpTagPredicate`

Предикат, проверяющий значение тега.

Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или см. [Failure detection API - JSON models](https://dt-url.net/9sg3swf).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из следующих объектов:  * `STRING_EXISTS` -> FdpTagStringExists * `STRING_EQUALS` -> FdpTagStringEquals * `STRING_STARTS_WITH` -> FdpTagStringStartsWith * `STRING_ENDS_WITH` -> FdpTagStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdpTagStringContainsSubstring * `INTEGER_EXISTS` -> FdpTagIntegerExists * `INTEGER_EQUALS` -> FdpTagIntegerEquals * `INTEGER_LESS_THAN` -> FdpTagIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdpTagIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdpTagIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdpTagIntegerGreaterThanOrEqual * `DOUBLE_EXISTS` -> FdpTagDoubleExists * `DOUBLE_EQUALS` -> FdpTagDoubleEquals * `DOUBLE_LESS_THAN` -> FdpTagDoubleLessThan * `DOUBLE_LESS_THAN_OR_EQUAL` -> FdpTagDoubleLessThanOrEqual * `DOUBLE_GREATER_THAN` -> FdpTagDoubleGreaterThan * `DOUBLE_GREATER_THAN_OR_EQUAL` -> FdpTagDoubleGreaterThanOrEqual Возможные значения: * `DOUBLE_EQUALS` * `DOUBLE_EXISTS` * `DOUBLE_GREATER_THAN` * `DOUBLE_GREATER_THAN_OR_EQUAL` * `DOUBLE_LESS_THAN` * `DOUBLE_LESS_THAN_OR_EQUAL` * `INTEGER_EQUALS` * `INTEGER_EXISTS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_EXISTS` * `STRING_STARTS_WITH` | Required |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"brokenLinkDomains": [



"mydomain.com"



],



"clientSideMissingHttpCodeIsFailure": false,



"description": "for requests from shipping module",



"failingHttpCodesClientSide": "400-599",



"failingHttpCodesServerSide": "500-599",



"http404NotFoundFailureEnabled": false,



"id": "FDP_9",



"name": "shipping",



"serverSideMissingHttpCodeIsFailure": false,



"successForcingExceptionPatterns": [



{



"classPattern": "NullPointerException",



"messagePattern": ""



}



],



"tagConditions": [



{



"predicate": {



"ignoreCase": true,



"type": "STRING_EQUALS",



"value": "NG"



},



"tagKey": "myTag"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новый набор параметров обнаружения сбоев создан. Тело ответа содержит ID нового набора. |
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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
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