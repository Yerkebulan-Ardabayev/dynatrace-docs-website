---
title: Synthetic locations API v2 - GET a location (Dynatrace Managed)
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-a-location
scraped: 2026-05-12T11:06:10.927412
---

# Synthetic locations API v2 - GET a location (Dynatrace Managed)

# Synthetic locations API v2 - GET a location (Dynatrace Managed)

* Published Jul 26, 2019

Этот API-вызов возвращает параметры указанного location. Запрос возвращает payload `application/json`.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | Dynatrace entity ID нужного location. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticLocation](#openapi-definition-SyntheticLocation) | Успех. Ответ содержит параметры synthetic location. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocation`

Конфигурация synthetic location.

Параметры **countryCode**, **regionCode**, **city** опциональны, поскольку могут быть получены на основе **latitude** и **longitude** location.

Фактический набор полей зависит от типа location. Список фактических объектов смотрите в описании поля **type** или в [Synthetic locations API v2 - JSON models](https://dt-url.net/3n43szj).

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Город location. |
| countryCode | string | Код страны location.  Список доступных кодов стран можно получить через запрос [GET all countries](https://dt-url.net/37030go). |
| countryName | string | Имя страны location. |
| entityId | string | Dynatrace entity ID location. |
| geoLocationId | string | Dynatrace GeoLocation ID location. |
| latitude | number | Широта location в формате `DDD.dddd`. |
| longitude | number | Долгота location в формате `DDD.dddd`. |
| name | string | Имя location. |
| regionCode | string | Код региона location.  Список доступных кодов регионов можно получить через запрос [GET regions of the country](https://dt-url.net/az230x0). |
| regionName | string | Имя региона location. |
| status | string | Статус location:  * `ENABLED`: Location отображается как активный в UI. Можно назначать мониторы на location. * `DISABLED`: Location отображается как неактивный в UI. Нельзя назначать мониторы на location. Уже назначенные мониторы остаются и выполняются с location. * `HIDDEN`: Location не отображается в UI. Нельзя назначать мониторы на location. Установить `HIDDEN` можно только если ни один монитор не назначен. Возможные значения: * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `PUBLIC` -> PublicSyntheticLocation * `PRIVATE` -> PrivateSyntheticLocation * `CLUSTER` -> PrivateSyntheticLocation Возможные значения: * `CLUSTER` * `PRIVATE` * `PUBLIC` |

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

## Формат ответа

Все вариации модели в зависимости от её типа смотрите в [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Получение информации о synthetic nodes через Synthetic v2 API.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticLocation](#openapi-definition-SyntheticLocation) | Успех. Ответ содержит параметры synthetic location. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocation`

Конфигурация synthetic location.

Параметры **countryCode**, **regionCode**, **city** опциональны, поскольку могут быть получены на основе **latitude** и **longitude** location.

Фактический набор полей зависит от типа location. Список фактических объектов смотрите в описании поля **type** или в [Synthetic locations API v2 - JSON models](https://dt-url.net/3n43szj).

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Город location. |
| countryCode | string | Код страны location.  Список доступных кодов стран можно получить через запрос [GET all countries](https://dt-url.net/37030go). |
| countryName | string | Имя страны location. |
| entityId | string | Dynatrace entity ID location. |
| geoLocationId | string | Dynatrace GeoLocation ID location. |
| latitude | number | Широта location в формате `DDD.dddd`. |
| longitude | number | Долгота location в формате `DDD.dddd`. |
| name | string | Имя location. |
| regionCode | string | Код региона location.  Список доступных кодов регионов можно получить через запрос [GET regions of the country](https://dt-url.net/az230x0). |
| regionName | string | Имя региона location. |
| status | string | Статус location:  * `ENABLED`: Location отображается как активный в UI. Можно назначать мониторы на location. * `DISABLED`: Location отображается как неактивный в UI. Нельзя назначать мониторы на location. Уже назначенные мониторы остаются и выполняются с location. * `HIDDEN`: Location не отображается в UI. Нельзя назначать мониторы на location. Установить `HIDDEN` можно только если ни один монитор не назначен. Возможные значения: * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Определяет фактический набор полей в зависимости от значения. Смотрите один из объектов:  * `PUBLIC` -> PublicSyntheticLocation * `PRIVATE` -> PrivateSyntheticLocation * `CLUSTER` -> PrivateSyntheticLocation Возможные значения: * `CLUSTER` * `PRIVATE` * `PUBLIC` |

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

## Пример — public location

В этом примере запрос возвращает детали public location **Amazon US East (N. Virginia)** с ID **SYNTHETIC\_LOCATION-0000000000000064**.

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

## Пример — private location

В этом примере запрос возвращает детали private location **Linz HTTP** с ID **SYNTHETIC\_LOCATION-BB5EE23C1D48AFF5**.

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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать single-URL browser monitor, browser clickpath или HTTP monitor.")