---
title: Synthetic locations API v2 - GET локация
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/get-a-location
scraped: 2026-05-12T11:59:21.645841
---

# Synthetic locations API v2 - GET локация

# Synthetic locations API v2 - GET локация

* Справочник
* Опубликовано 26 июля 2019 г.

Возвращает параметры указанной локации.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/locations/{locationId}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/locations/{locationId}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `syntheticLocations.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | Dynatrace entity ID требуемой локации. | path | Обязательный |

## Ответ

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Получение информации о синтетических узлах через Synthetic v2 API.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticLocation](#openapi-definition-SyntheticLocation) | Успех. Ответ содержит параметры синтетической локации. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocation`

Конфигурация синтетической локации.

Параметры **countryCode**, **regionCode**, **city** необязательны, так как их можно получить на основе **latitude** и **longitude** локации.

Фактический набор полей зависит от типа локации. Список фактических объектов смотрите в описании поля **type** или в [Synthetic locations API v2 - JSON-модели](https://dt-url.net/3n43szj).

| Поле | Тип | Описание |
| --- | --- | --- |
| city | string | Город локации. |
| countryCode | string | Код страны локации.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go). |
| countryName | string | Название страны локации. |
| entityId | string | Dynatrace entity ID локации. |
| geoLocationId | string | Dynatrace GeoLocation ID локации. |
| latitude | number | Широта локации в формате `DDD.dddd`. |
| longitude | number | Долгота локации в формате `DDD.dddd`. |
| name | string | Имя локации. |
| regionCode | string | Код региона локации.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0). |
| regionName | string | Название региона локации. |
| status | string | Статус локации:  * `ENABLED`: локация отображается в UI как активная. Локации можно назначать мониторы. * `DISABLED`: локация отображается в UI как неактивная. Локации нельзя назначать мониторы. Мониторы, уже назначенные локации, останутся там и будут выполняться с этой локации. * `HIDDEN`: локация не отображается в UI. Локации нельзя назначать мониторы. Установить локацию в `HIDDEN` можно только тогда, когда ей не назначен ни один монитор. Поле может принимать значения: * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `PUBLIC` -> PublicSyntheticLocation * `PRIVATE` -> PrivateSyntheticLocation * `CLUSTER` -> PrivateSyntheticLocation Поле может принимать значения: * `CLUSTER` * `PRIVATE` * `PUBLIC` |

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



"city": "string",



"countryCode": "string",



"countryName": "string",



"entityId": "string",



"geoLocationId": "string",



"latitude": 1,



"longitude": 1,



"name": "string",



"regionCode": "string",



"regionName": "string",



"status": "DISABLED",



"type": "CLUSTER"



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

## Пример - публичная локация

В этом примере запрос возвращает детали публичной локации **Amazon US East (N. Virginia)**, у которой ID равен **SYNTHETIC\_LOCATION-0000000000000064**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-0000000000000064 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-0000000000000064
```

#### Тело ответа

```
{



"entityId": "SYNTHETIC_LOCATION-0000000000000064",



"type": "PUBLIC",



"name": "GdaÅsk",



"countryCode": "PL",



"regionCode": "EU",



"city": "GdaÅsk",



"latitude": 54.399078,



"longitude": 18.576557,



"status": "ENABLED",



"cloudPlatform": "OTHER",



"ips": [



"120.157.221.247",



"172.158.6.93",



"197.136.70.30",



"227.53.205.237",



"131.123.197.12"



],



"stage": "GA",



"browserType": "Chrome",



"browserVersion": "83.0.4103.61",



"capabilities": [



"BROWSER",



"HTTP"



],



"geoLocationId": "GEOLOCATION-0A41430434C388A9"



}
```

#### Код ответа

200

## Пример - приватная локация

В этом примере запрос возвращает детали приватной локации **Linz HTTP**, у которой ID равен **SYNTHETIC\_LOCATION-BB5EE23C1D48AFF5**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-BB5EE23C1D48AFF5 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-BB5EE23C1D48AFF5
```

#### Тело ответа

```
{



"entityId": "SYNTHETIC_LOCATION-BB5EE23C1D48AFF5",



"type": "PRIVATE",



"name": "Linz HTTP",



"countryCode": "AT",



"regionCode": "04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"status": "ENABLED",



"nodes": [



"137829320"



],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 3000,



"geoLocationId": "GEOLOCATION-427705B3488A4C45"



}
```

#### Код ответа

200

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")