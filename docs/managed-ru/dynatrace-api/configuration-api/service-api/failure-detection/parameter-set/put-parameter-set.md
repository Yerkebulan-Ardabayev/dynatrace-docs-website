---
title: Failure detection API - PUT a parameter set
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/put-parameter-set
---

# Failure detection API - PUT a parameter set

# Failure detection API - PUT a parameter set

* Справка
* Опубликовано 11 янв. 2021 г.

Обновляет указанный набор параметров обнаружения сбоев.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа со scope `WriteConfig`.

О том, как его получить и использовать, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Список всех вариаций модели, зависящих от её типа, см. в [моделях JSON](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Learn the variations of JSON models in the Dynatrace failure detection API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного набора параметров обнаружения сбоев. Должен быть корректным RFC 4122 UUID. | path | Обязательный |
| body | [FailureDetectionParameterSet](#openapi-definition-FailureDetectionParameterSet) | Тело запроса JSON. Содержит обновлённый набор параметров обнаружения сбоев.  ID нельзя обновить этим запросом. Вместо этого нужно использовать запрос смены ID. | body | Необязательный |

### Объекты тела запроса

#### Объект `FailureDetectionParameterSet`

Набор параметров обнаружения сбоев (FDP).

Эти параметры задают условия сбоя и успеха.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| brokenLinkDomains | string[] | Список доменов для особой обработки HTTP-кода ответа 404.  Если верхний домен *Referer* присутствует в списке ИЛИ совпадает с верхним доменом хоста запроса, код 404 считается сбоем.  Применимо, только если **isHttp404NotFoundFailureEnabled** установлен в `true`. | Необязательный |
| clientSideMissingHttpCodeIsFailure | boolean | Отсутствующий HTTP-код ответа на стороне клиента считается сбоем (`true`) или успехом (`false`).  Если не задано, используется `false`. | Необязательный |
| description | string | Краткое описание набора FDP. | Необязательный |
| exceptionOnAnyNodeExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список ошибочных исключений.  Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем. | Необязательный |
| failingHttpCodesClientSide | string | Список HTTP-кодов ответа на стороне клиента, которые считаются сбоем.  Формат: список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`).  Если не задано, используется диапазон `400-599`. | Необязательный |
| failingHttpCodesServerSide | string | Список HTTP-кодов ответа на стороне сервера, которые считаются сбоем.  Формат: список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`).Если не задано, используется диапазон `500-599`. | Необязательный |
| http404NotFoundFailureEnabled | boolean | Особая обработка HTTP-кода ответа 404 включена (`true`) или отключена (`false`). Подробности особой обработки см. в **brokenLinkDomains**.  Применимо, только если 404 НЕ входит в список сбойных HTTP-кодов ответа, и только для стороны сервера.  Если не задано, используется `false`. | Необязательный |
| id | string | ID набора параметров. | Необязательный |
| ignoreAllExceptions | boolean | Если установлено в true, все исключения будут игнорироваться. Это означает, что заданные шаблоны исключений не будут иметь эффекта. | Необязательный |
| ignoreSpanFailureDetection | boolean | Если установлено в true, обнаружение сбоев по span будет игнорироваться. | Необязательный |
| ignoredExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список игнорируемых исключений.  Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно игнорируется обнаружением сбоев. | Необязательный |
| name | string | Отображаемое имя набора FDP.  Длина имени ограничена 150 символами. | Необязательный |
| serverSideMissingHttpCodeIsFailure | boolean | Отсутствующий HTTP-код ответа на стороне сервера считается сбоем (`true`) или успехом (`false`).  Если не задано, используется `false`. | Необязательный |
| successForcingExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список исключений успеха.  Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно считается успехом. | Необязательный |
| tagConditions | [FdpTagCondition](#openapi-definition-FdpTagCondition)[] | Список условий на основе тегов.  Если выполнено *любое* условие, запрос считается сбоем. | Необязательный |

#### Объект `ExceptionPattern`

Список ошибочных исключений.

Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| classPattern | string | - | Необязательный |
| messagePattern | string | - | Необязательный |

#### Объект `FdpTagCondition`

Конфигурация условия по тегу в наборе FDP.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| predicate | [FdpTagPredicate](#openapi-definition-FdpTagPredicate) | Предикат, проверяющий значение тега.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или в [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf?dt=m). | Обязательный |
| tagKey | string | Ключ проверяемого тега. | Обязательный |

#### Объект `FdpTagPredicate`

Предикат, проверяющий значение тега.

Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или в [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STRING_EXISTS` -> FdpTagStringExists * `STRING_EQUALS` -> FdpTagStringEquals * `STRING_STARTS_WITH` -> FdpTagStringStartsWith * `STRING_ENDS_WITH` -> FdpTagStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdpTagStringContainsSubstring * `INTEGER_EXISTS` -> FdpTagIntegerExists * `INTEGER_EQUALS` -> FdpTagIntegerEquals * `INTEGER_LESS_THAN` -> FdpTagIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdpTagIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdpTagIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdpTagIntegerGreaterThanOrEqual * `DOUBLE_EXISTS` -> FdpTagDoubleExists * `DOUBLE_EQUALS` -> FdpTagDoubleEquals * `DOUBLE_LESS_THAN` -> FdpTagDoubleLessThan * `DOUBLE_LESS_THAN_OR_EQUAL` -> FdpTagDoubleLessThanOrEqual * `DOUBLE_GREATER_THAN` -> FdpTagDoubleGreaterThan * `DOUBLE_GREATER_THAN_OR_EQUAL` -> FdpTagDoubleGreaterThanOrEqual Элемент может принимать следующие значения * `DOUBLE_EQUALS` * `DOUBLE_EXISTS` * `DOUBLE_GREATER_THAN` * `DOUBLE_GREATER_THAN_OR_EQUAL` * `DOUBLE_LESS_THAN` * `DOUBLE_LESS_THAN_OR_EQUAL` * `INTEGER_EQUALS` * `INTEGER_EXISTS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_EXISTS` * `STRING_STARTS_WITH` | Обязательный |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Создан новый набор параметров обнаружения сбоев. Ответ содержит ID нового набора. |
| **204** | - | Успешно. Набор параметров обнаружения сбоев обновлён. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введены некорректные данные. |

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
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой её в составе реального запроса. Код ответа **204** означает, что полезная нагрузка валидна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Отправленная конфигурация валидна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введены недопустимые данные. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели JSON тела ответа

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