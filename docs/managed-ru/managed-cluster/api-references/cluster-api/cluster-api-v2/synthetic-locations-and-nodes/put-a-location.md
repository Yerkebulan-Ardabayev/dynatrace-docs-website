---
title: "Synthetic locations API v2 - PUT a location (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location
updated: 2026-02-09
---

Этот API-вызов:

* Private locations: обновляет существующий location.
* Public locations: меняет статус существующего location.

Запрос принимает payload `application/json`.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Параметры

Все вариации модели в зависимости от её типа смотрите в JSON models.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | Dynatrace entity ID synthetic location для обновления. | path | Required |
| body | [SyntheticLocationUpdate](#openapi-definition-SyntheticLocationUpdate) | JSON-тело запроса. Содержит обновлённые параметры location. | body | Required |

### Объекты тела запроса

#### Объект `SyntheticLocationUpdate`

Обновление synthetic location. Это базовый объект, фактический тип зависит от значения поля `type`.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `PUBLIC` -> SyntheticPublicLocationUpdate * `PRIVATE` -> SyntheticPrivateLocationUpdate Возможные значения: * `PRIVATE` * `PUBLIC` | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{


"type": "PRIVATE"


}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Location обновлён. Ответ без тела. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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

## Пример: private location

В этом примере запрос обновляет **private** synthetic location из примера POST-запроса. Меняется имя location на **Linz** и добавляется synthetic node с ID **353074222**.

API-токен передаётся в заголовке **Authorization**.

Код ответа **204** означает успешное обновление.

Можно скачать или скопировать пример тела запроса для своих экспериментов. Не забудьте заменить список нод на ноды, доступные в вашем окружении. Список доступных нод можно получить через запрос GET all nodes.

#### Curl

```
curl -L -X PUT 'https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-493122BFA29674DC' \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \


-H 'Content-Type: application/json' \


--data-raw '{


"type": "PRIVATE",


"name": "Linz",


"countryCode": "AT",


"regionCode": "04",


"city": "Linz",


"status": "ENABLED",


"latitude": 48.306351,


"longitude": 14.287399,


"nodes": [


"290433380",


"353074222"


],


"availabilityLocationOutage": false,


"availabilityNodeOutage": false,


"locationNodeOutageDelayInMillis": 5000


}


'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-493122BFA29674DC
```

#### Тело запроса

```
{


"type": "PRIVATE",


"name": "Linz",


"countryCode": "AT",


"city": "Linz",


"status": "ENABLED",


"latitude": 48.306351,


"longitude": 14.287399,


"nodes": ["290433380", "353074222"],


"availabilityLocationOutage": false,


"availabilityNodeOutage": false,


"locationNodeOutageDelayInMillis": 5000


}
```

#### Код ответа

204

## Пример: public location

В этом примере запрос отключает public location с ID **SYNTHETIC\_LOCATION-0000000000000273**.

API-токен передаётся в заголовке **Authorization**.

Код ответа **204** означает успешное обновление.

#### Curl

```
curl -L -X PUT 'https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-0000000000000273' \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \


-H 'Content-Type: application/json' \


--data-raw '{


"type": "PUBLIC",


"status": "DISABLED"


}


'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-0000000000000273
```

#### Тело запроса

```
{


"type": "PUBLIC",


"status": "DISABLED"


}
```

#### Код ответа

204

## Связанные темы

* Synthetic Monitoring
