---
title: Failure detection API - GET a parameter set
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/parameter-set/get-parameter-set
---

# Failure detection API - GET a parameter set

# Failure detection API - GET a parameter set

* Справочник
* Опубликовано 11 января 2021 г.

Получает указанный набор параметров обнаружения сбоев.

Запрос выдаёт содержимое типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/parameterSets/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Подробнее о том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного набора параметров обнаружения сбоев. Должен быть валидным UUID по RFC 4122. | путь | Обязательный |

## Ответ

Чтобы найти все варианты модели, зависящие от типа модели, см. [JSON models](/managed/dynatrace-api/configuration-api/service-api/failure-detection/json-models "Learn the variations of JSON models in the Dynatrace failure detection API.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [FailureDetectionParameterSet](#openapi-definition-FailureDetectionParameterSet) | Успех |
| **404** | - | Ошибка. Указанная сущность не существует. |

### Объекты тела ответа

#### Объект `FailureDetectionParameterSet`

Набор параметров обнаружения сбоев (FDP).

Эти параметры определяют условия сбоя и успеха.

| Элемент | Тип | Описание |
| --- | --- | --- |
| brokenLinkDomains | string[] | Список доменов для особой обработки HTTP-кода ответа 404. Если верхний домен *Referer* присутствует в списке ИЛИ равен верхнему домену хоста запроса, код 404 считается сбоем. Применимо только когда **isHttp404NotFoundFailureEnabled** установлен в `true`. |
| clientSideMissingHttpCodeIsFailure | boolean | Отсутствующий HTTP-код ответа на стороне клиента считается сбоем (`true`) или успехом (`false`). Если не задано, используется `false`. |
| description | string | Краткое описание набора FDP. |
| exceptionOnAnyNodeExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список сбойных исключений. Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем. |
| failingHttpCodesClientSide | string | Список HTTP-кодов ответа на стороне клиента, которые считаются сбоем. Формат, это список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`). Если не задано, используется диапазон `400-599`. |
| failingHttpCodesServerSide | string | Список HTTP-кодов ответа на стороне сервера, которые считаются сбоем. Формат, это список диапазонов и отдельных значений (например, `500-599, 400-499, 1008`). Если не задано, используется диапазон `500-599`. |
| http404NotFoundFailureEnabled | boolean | Особая обработка HTTP-кода ответа 404 включена (`true`) или отключена (`false`). Подробности особой обработки см. в **brokenLinkDomains**. Применимо только когда 404 НЕ входит в список сбойных HTTP-кодов ответа, и только для стороны сервера. Если не задано, используется `false`. |
| id | string | ID набора параметров. |
| ignoreAllExceptions | boolean | Если установлено в true, все исключения будут игнорироваться. Это значит, что заданные шаблоны исключений не будут иметь никакого эффекта. |
| ignoreSpanFailureDetection | boolean | Если установлено в true, обнаружение сбоев по span будет игнорироваться. |
| ignoredExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список игнорируемых исключений. Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно игнорируется обнаружением сбоев. |
| name | string | Отображаемое имя набора FDP. Длина имени ограничена 150 символами. |
| serverSideMissingHttpCodeIsFailure | boolean | Отсутствующий HTTP-код ответа на стороне сервера считается сбоем (`true`) или успехом (`false`). Если не задано, используется `false`. |
| successForcingExceptionPatterns | [ExceptionPattern](#openapi-definition-ExceptionPattern)[] | Список исключений успеха. Если исключение на входном узле сервиса соответствует *любому* из этих шаблонов, оно считается успехом. |
| tagConditions | [FdpTagCondition](#openapi-definition-FdpTagCondition)[] | Список условий на основе тегов. Если выполняется *любое* условие, запрос считается сбоем. |

#### Объект `ExceptionPattern`

Список сбойных исключений.

Если исключение на *любом* узле сервиса соответствует *любому* из этих шаблонов, оно считается сбоем.

| Элемент | Тип | Описание |
| --- | --- | --- |
| classPattern | string | - |
| messagePattern | string | - |

#### Объект `FdpTagCondition`

Конфигурация условия по тегу в наборе FDP.

| Элемент | Тип | Описание |
| --- | --- | --- |
| predicate | [FdpTagPredicate](#openapi-definition-FdpTagPredicate) | Предикат, проверяющий значение тега. Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или в [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf?dt=m). |
| tagKey | string | Ключ проверяемого тега. |

#### Объект `FdpTagPredicate`

Предикат, проверяющий значение тега.

Фактический набор полей зависит от типа предиката. Список фактических объектов см. в описании поля **type** или в [Failure detection API - JSON models﻿](https://dt-url.net/9sg3swf?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `STRING_EXISTS` -> FdpTagStringExists * `STRING_EQUALS` -> FdpTagStringEquals * `STRING_STARTS_WITH` -> FdpTagStringStartsWith * `STRING_ENDS_WITH` -> FdpTagStringEndsWith * `STRING_CONTAINS_SUBSTRING` -> FdpTagStringContainsSubstring * `INTEGER_EXISTS` -> FdpTagIntegerExists * `INTEGER_EQUALS` -> FdpTagIntegerEquals * `INTEGER_LESS_THAN` -> FdpTagIntegerLessThan * `INTEGER_LESS_THAN_OR_EQUAL` -> FdpTagIntegerLessThanOrEqual * `INTEGER_GREATER_THAN` -> FdpTagIntegerGreaterThan * `INTEGER_GREATER_THAN_OR_EQUAL` -> FdpTagIntegerGreaterThanOrEqual * `DOUBLE_EXISTS` -> FdpTagDoubleExists * `DOUBLE_EQUALS` -> FdpTagDoubleEquals * `DOUBLE_LESS_THAN` -> FdpTagDoubleLessThan * `DOUBLE_LESS_THAN_OR_EQUAL` -> FdpTagDoubleLessThanOrEqual * `DOUBLE_GREATER_THAN` -> FdpTagDoubleGreaterThan * `DOUBLE_GREATER_THAN_OR_EQUAL` -> FdpTagDoubleGreaterThanOrEqual Элемент может принимать следующие значения * `DOUBLE_EQUALS` * `DOUBLE_EXISTS` * `DOUBLE_GREATER_THAN` * `DOUBLE_GREATER_THAN_OR_EQUAL` * `DOUBLE_LESS_THAN` * `DOUBLE_LESS_THAN_OR_EQUAL` * `INTEGER_EQUALS` * `INTEGER_EXISTS` * `INTEGER_GREATER_THAN` * `INTEGER_GREATER_THAN_OR_EQUAL` * `INTEGER_LESS_THAN` * `INTEGER_LESS_THAN_OR_EQUAL` * `STRING_CONTAINS_SUBSTRING` * `STRING_ENDS_WITH` * `STRING_EQUALS` * `STRING_EXISTS` * `STRING_STARTS_WITH` |

### Пример тела ответа JSON models

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