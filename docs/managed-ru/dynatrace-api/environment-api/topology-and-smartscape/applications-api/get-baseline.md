---
title: Applications API - GET baseline
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline
scraped: 2026-05-12T12:01:44.023948
---

# Applications API - GET baseline

# Applications API - GET baseline

* Reference
* Updated on Mar 22, 2023
* Deprecated

Получает базовую линию указанного приложения.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}/baseline` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}/baseline` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | ID сущности Dynatrace для нужного приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationBaselineValues](#openapi-definition-ApplicationBaselineValues) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApplicationBaselineValues`

Базовая линия для приложения и его дочерних элементов по каждой доступной метрике длительности.

Метрика длительности это одна из следующих:

* **DOM interactive**
* **HTML downloaded**
* **Load event end**
* **Load event start**
* **Response time**
* **Speed index**
* **Time to first byte**
* **Visually complete**

| Элемент | Тип | Описание |
| --- | --- | --- |
| applicationDomInteractiveBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **DOM interactive**. |
| applicationHtmlDownloadedBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **HTML downloaded**. |
| applicationLoadEventEndBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Load event end**. |
| applicationLoadEventStartBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Load event start**. |
| applicationResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Response time**. |
| applicationSpeedIndexBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Speed index**. |
| applicationTimeToFirstByteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Time to first byte**. |
| applicationVisualCompleteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовая линия для метрики длительности **Visually complete**. |
| displayName | string | Имя приложения в том виде, как оно отображается в UI. |
| entityId | string | ID сущности Dynatrace для приложения. |

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



"applicationDomInteractiveBaselines": [



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



],



"applicationHtmlDownloadedBaselines": [



{}



],



"applicationLoadEventEndBaselines": [



{}



],



"applicationLoadEventStartBaselines": [



{}



],



"applicationResponseTimeBaselines": [



{}



],



"applicationSpeedIndexBaselines": [



{}



],



"applicationTimeToFirstByteBaselines": [



{}



],



"applicationVisualCompleteBaselines": [



{}



],



"displayName": "string",



"entityId": "string"



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

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")