---
title: Synthetic locations API v2 - PUT локация
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-a-location
scraped: 2026-05-12T11:59:23.600704
---

# Synthetic locations API v2 - PUT локация

# Synthetic locations API v2 - PUT локация

* Справочник
* Опубликовано 26 июля 2019 г.

* Приватные локации Обновляет существующую локацию.
* Публичные локации Изменяет статус существующей локации.

Запрос принимает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/locations/{locationId}` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/locations/{locationId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `syntheticLocations.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Получение информации о синтетических узлах через Synthetic v2 API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | Dynatrace entity ID обновляемой синтетической локации. | path | Обязательный |
| body | [SyntheticLocationUpdate](#openapi-definition-SyntheticLocationUpdate) | JSON-тело запроса. Содержит обновлённые параметры локации. | body | Обязательный |

### Объекты тела запроса

#### Объект `SyntheticLocationUpdate`

Обновление синтетической локации. Это базовый объект, точный тип зависит от значения поля `type`.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `PUBLIC` -> SyntheticPublicLocationUpdate * `PRIVATE` -> SyntheticPrivateLocationUpdate Поле может принимать значения: * `PRIVATE` * `PUBLIC` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"type": "PRIVATE"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Локация обновлена. У ответа нет тела. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Пример - приватная локация

В этом примере запрос обновляет **приватную** синтетическую локацию из [примера POST-запроса](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/post-a-location#example "Создание приватной синтетической локации через Synthetic v2 API."). Он меняет имя локации на **Linz** и добавляет синтетический узел с ID **353074222**.

API-токен передаётся в заголовке **Authorization**.

Код ответа **204** означает, что обновление прошло успешно.

Можно скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно замените список узлов на узлы, доступные в вашем окружении. Список доступных узлов можно получить запросом [GET all nodes](/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-all "Получение списка всех синтетических узлов через Synthetic v1 API.").

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

## Пример - публичная локация

В этом примере запрос отключает публичную локацию с ID **SYNTHETIC\_LOCATION-0000000000000273**.

API-токен передаётся в заголовке **Authorization**.

Код ответа **204** означает, что обновление прошло успешно.

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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")