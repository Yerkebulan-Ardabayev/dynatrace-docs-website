---
title: Applications API - GET baseline
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/get-baseline
scraped: 2026-03-05T21:26:55.942296
---

* Устарело

Получает базовые данные указанного приложения.

Запрос возвращает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications/{meIdentifier}/baseline` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}/baseline` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью `DataExport`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace требуемого приложения. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationBaselineValues](#openapi-definition-ApplicationBaselineValues) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ApplicationBaselineValues`

Базовые данные для приложения и его дочерних элементов для каждой доступной метрики длительности.

Метрика длительности — это одна из следующих:

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
| applicationDomInteractiveBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для метрики длительности **DOM interactive**. |
| applicationHtmlDownloadedBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для метрики длительности **HTML downloaded**. |
| applicationLoadEventEndBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для метрики длительности **Load event end**. |
| applicationLoadEventStartBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для метрики длительности **Load event start**. |
| applicationResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для метрики длительности **Response time**. |
| applicationSpeedIndexBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для метрики длительности **Speed index**. |
| applicationTimeToFirstByteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для метрики длительности **Time to first byte**. |
| applicationVisualCompleteBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для метрики длительности **Visually complete**. |
| displayName | string | Имя приложения, отображаемое в пользовательском интерфейсе. |
| entityId | string | Идентификатор сущности Dynatrace приложения. |

#### Объект `EntityBaselineData`

Базовые данные для сущности Dynatrace для определённой метрики длительности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| childBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для дочерних сущностей данной сущности, например `SERVICE_METHOD` для `SERVICE_METHOD_GROUP`. |
| displayName | string | Отображаемое имя сущности. |
| entityId | string | Идентификатор сущности Dynatrace. |
| errorRate | number | Базовый уровень ошибок. |
| hasLoadBaseline | boolean | Сущность имеет базовый уровень нагрузки (`true`) или не имеет (`false`). |
| micros90thPercentile | number | Базовый 90-й процентиль, в микросекундах. |
| microsMedian | number | Базовая медиана, в микросекундах. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

* [Real User Monitoring](../../../../observe/digital-experience/rum-concepts/rum-overview.md "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")