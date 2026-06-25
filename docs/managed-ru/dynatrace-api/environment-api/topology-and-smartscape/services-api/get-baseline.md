---
title: Services API - GET baseline
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline
scraped: 2026-05-12T12:01:49.025995
---

# Services API - GET baseline

# Services API - GET baseline

* Reference
* Updated on Mar 22, 2023
* Deprecated

Получает базовую линию указанного сервиса.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}/baseline` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}/baseline` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | ID сущности Dynatrace для нужного сервиса. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ServiceBaselineValues](#openapi-definition-ServiceBaselineValues) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ServiceBaselineValues`

Базовая линия для сервиса и его дочерних элементов по метрике длительности **Response time**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя сервиса. |
| entityId | string | ID сервиса. |
| serviceResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Response time**. |

#### Объект `EntityBaselineData`

Базовая линия для сущности Dynatrace по конкретной метрике длительности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| childBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для дочерних сущностей этой сущности, например `SERVICE_METHOD` у `SERVICE_METHOD_GROUP`. |
| displayName | string | Отображаемое имя сущности. |
| entityId | string | ID сущности Dynatrace. |
| errorRate | number | Базовая линия частоты ошибок. |
| hasLoadBaseline | boolean | У сущности есть базовая линия нагрузки (`true`) или нет (`false`). |
| micros90thPercentile | number | Базовая линия 90-го перцентиля, в микросекундах. |
| microsMedian | number | Медианная базовая линия, в микросекундах. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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



"displayName": "string",



"entityId": "string",



"serviceResponseTimeBaselines": [



{



"childBaselines": [



{}



],



"displayName": "string",



"entityId": "string",



"errorRate": 1,



"hasLoadBaseline": true,



"micros90thPercentile": 1,



"microsMedian": 1



}



]



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

## Связанные темы

* [Сервисы](/managed/observe/application-observability/services "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.")