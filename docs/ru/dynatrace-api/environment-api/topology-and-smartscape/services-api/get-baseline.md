---
title: Services API - GET baseline
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/services-api/get-baseline
scraped: 2026-03-05T21:26:57.818899
---

* Устарело

Возвращает базовые данные указанного сервиса.

Запрос возвращает полезную нагрузку в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/services/{meIdentifier}/baseline` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/services/{meIdentifier}/baseline` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `DataExport`.

Сведения о получении и использовании токена см. в разделе Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Местоположение | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace для требуемого сервиса. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ServiceBaselineValues](#openapi-definition-ServiceBaselineValues) | Успешно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ServiceBaselineValues`

Базовые данные для сервиса и его дочерних элементов по метрике продолжительности **Время отклика**.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя сервиса. |
| entityId | string | Идентификатор сервиса. |
| serviceResponseTimeBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные по метрике продолжительности **Время отклика**. |

#### Объект `EntityBaselineData`

Базовые данные для сущности Dynatrace по конкретной метрике продолжительности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| childBaselines | [EntityBaselineData[]](#openapi-definition-EntityBaselineData) | Базовые данные для дочерних сущностей данной сущности, например `SERVICE_METHOD` группы `SERVICE_METHOD_GROUP`. |
| displayName | string | Отображаемое имя сущности. |
| entityId | string | Идентификатор сущности Dynatrace. |
| errorRate | number | Базовое значение частоты ошибок. |
| hasLoadBaseline | boolean | Сущность имеет базовое значение нагрузки (`true`) или нет (`false`). |
| micros90thPercentile | number | Базовое значение 90-го процентиля, в микросекундах. |
| microsMedian | number | Базовое медианное значение, в микросекундах. |

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
| parameterLocation | string | Элемент может принимать следующие значения: `HEADER`, `PATH`, `PAYLOAD_BODY`, `QUERY` |
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

* Сервисы
