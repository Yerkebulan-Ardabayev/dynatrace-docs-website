---
title: Synthetic locations API v2 - DELETE a location (Dynatrace Managed)
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/delete-a-location
scraped: 2026-05-12T11:05:53.990527
---

# Synthetic locations API v2 - DELETE a location (Dynatrace Managed)

# Synthetic locations API v2 - DELETE a location (Dynatrace Managed)

* Published Jul 26, 2019

Этот API-вызов удаляет существующий **private** Synthetic location. Удаление необратимо.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | Dynatrace entity ID удаляемого private synthetic location. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Location удалён. Ответ без тела. |
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

## Пример

В этом примере запрос удаляет private Synthetic location из [примера POST-запроса](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/post-a-location#example "Создание private synthetic location через Synthetic v2 API."). Код ответа **204** означает успешное удаление.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-493122BFA29674DC \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-493122BFA29674DC
```

#### Код ответа

204

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать single-URL browser monitor, browser clickpath или HTTP monitor.")