---
title: Failure detection API - POST a parameter set
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/post-parameter-set
---

# Failure detection API - POST a parameter set

# Failure detection API - POST a parameter set

* Справка
* Опубликовано 11 января 2021 г.

Создаёт новый набор параметров обнаружения сбоев.

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, см. в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Тело запроса не должно содержать ID. ID присваивается автоматически Dynatrace и возвращается в составе ответа.

Чтобы найти все варианты модели, зависящие от типа модели, см. [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Learn the variations of JSON models in the Dynatrace failure detection API.").

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [FailureDetectionParameterSet](#openapi-definition-FailureDetectionParameterSet) | Тело JSON запроса. Содержит новый набор параметров обнаружения сбоев.  Dynatrace сгенерирует случайный UUID, если ID не указан. | body | Опционально |

### Объекты тела запроса

#### Объект `FailureDetectionParameterSet`

Набор параметров обнаружения сбоев (FDP).

Эти параметры определяют условия сбоя и успеха.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| brokenLinkDomains | string[] | Список доменов для особой обработки кода ответа HTTP 404.  Если верхний домен *Referer* присутствует в списке ИЛИ совпадает с верхним доменом хоста запроса, код 404 считается сбоем.  Применяется только если **isHttp404NotFoundFailureEnabled** установлен в значение `true`. | Опционально |
| clientSideMissingHttpCodeIsFailure | boolean | Отсутствующий код ответа HTTP на стороне клиента считается сбоем (`true`) или успехом (`false`).  Если не задано, используется значение `false`. | Опционально |
| description | string | Краткое описание набора FDP. | Опционально |
| exceptionOnAnyNodeExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список ошибочных исключений.  Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем. | Опционально |
| failingHttpCodesClientSide | string | Список кодов ответа HTTP на стороне клиента, которые считаются сбоем.  Формат: список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`).  Если не задано, используется диапазон `400-599`. | Опционально |
| failingHttpCodesServerSide | string | Список кодов ответа HTTP на стороне сервера, которые считаются сбоем.  Формат: список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`). Если не задано, используется диапазон `500-599`. | Опционально |
| http404NotFoundFailureEnabled | boolean | Особая обработка кода ответа HTTP 404 включена (`true`) или отключена (`false`). Подробности особой обработки см. в **brokenLinkDomains**.  Применяется только если 404 НЕ входит в список сбойных кодов ответа HTTP, и только для стороны сервера.  Если не задано, используется значение `false`. | Опционально |
| id | string | ID набора параметров. | Опционально |
| ignoreAllExceptions | boolean | Если установлено значение true, все исключения будут игнорироваться. Это означает, что заданные шаблоны исключений не будут иметь никакого эффекта. | Опционально |
| ignoreSpanFailureDetection | boolean | Если установлено значение true, обнаружение сбоев по span будет игнорироваться. | Опционально |
| ignoredExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список игнорируемых исключений.  Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно игнорируется обнаружением сбоев. | Опционально |
| name | string | Отображаемое имя набора FDP.  Длина имени ограничена 150 символами. | Опционально |
| serverSideMissingHttpCodeIsFailure | boolean | Отсутствующий код ответа HTTP на стороне сервера считается сбоем (`true`) или успехом (`false`).  Если не задано, используется значение `false`. | Опционально |
| successForcingExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список исключений успеха.  Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно считается успехом. | Опционально |
| tagConditions | [FdpTagCondition](#openapi-definition-FdpTagCondition)[] | Список условий на основе тегов.  Если выполняется *любое* условие, запрос считается сбоем. | Опционально |

#### Объект `ExceptionPattern`

Список ошибочных исключений.

Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| classPattern | string | - | Опционально |
| messagePattern | string | - | Опционально |

#### Объект `FdpTagCondition`

Конфигурация условия по тегу в наборе FDP.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| predicate | [FdpTagPredicate](#openapi-definition-FdpTagPredicate) | Предикат, проверяющий значение тега.  Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или в разделе [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf?dt=m). | Обязательно |
| tagKey | string | Ключ проверяемого тега. | Обязательно |

#### Объект `FdpTagPredicate`

Предикат, проверяющий значение тега.

Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или в разделе [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf?dt=m).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STRING_EXISTS` -> FdpTagStringExists * `STRING_EQUALS` -> FdpTagStringEquals * `STRING_STARTS_WITH` -> FdpTagStringStartsWith * `STRING_ENDS_WITH` -> FdpTagStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdpTagStringContainsSubstring * `INTEGER_EXISTS` -> FdpTagIntegerExists * `INTEGER_EQUALS` -> FdpTagIntegerEquals * `INTEGER_LESS_THAN` -> FdpTagIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdpTagIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdpTagIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdpTagIntegerGreaterThanOrEqual * `DOUBLE_EXISTS` -> FdpTagDoubleExists * `DOUBLE_EQUALS` -> FdpTagDoubleEquals * `DOUBLE_LESS_THAN` -> FdpTagDoubleLessThan * `DOUBLE_LESS_THAN_OR_EQUAL` -> FdpTagDoubleLessThanOrEqual * `DOUBLE_GREATER_THAN` -> FdpTagDoubleGreaterThan * `DOUBLE_GREATER_THAN_OR_EQUAL` -> FdpTagDoubleGreaterThanOrEqual Элемент может принимать следующие значения * `DOUBLE_EQUALS` * `DOUBLE_EXISTS` * `DOUBLE_GREATER_THAN` * `DOUBLE_GREATER_THAN_OR_EQUAL` * `DOUBLE_LESS_THAN` * `DOUBLE_LESS_THAN_OR_EQUAL` * `INTEGER_EQUALS` * `INTEGER_EXISTS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_EXISTS` * `STRING_STARTS_WITH` | Обязательно |

### JSON модель тела запроса

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успешно. Новый набор параметров обнаружения сбоев создан. Ответ содержит ID нового набора. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

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
| code | integer | HTTP-код состояния |
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

Рекомендуется проверять полезную нагрузку перед отправкой в составе реального запроса. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать его, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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