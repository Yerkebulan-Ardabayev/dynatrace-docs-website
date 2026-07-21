---
title: Synthetic locations API - GET a location
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-a-location
---

# Synthetic locations API - GET a location

# Synthetic locations API - GET a location

* Справка
* Опубликовано 26 июля 2019 г.

Доступна новая версия этого API: [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Узнайте, что предлагает Dynatrace Synthetic v2 API."). Ознакомьтесь с ней!

Получает параметры указанной локации.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с одной из следующих областей действия:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

Подробнее о том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | ID сущности Dynatrace требуемой локации. | path | Обязательный |

## Ответ

Полный список вариаций модели, зависящих от типа модели, см. в разделе [JSON models](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models "Изучите вариации моделей в API Synthetic locations v1.").

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticLocation](#openapi-definition-SyntheticLocation) | Успешно. Ответ содержит параметры synthetic-локации. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocation`

Конфигурация synthetic-локации.

Параметры **countryCode**, **regionCode**, **city** необязательны, поскольку их можно получить на основе **latitude** и **longitude** локации.

Фактический набор полей зависит от типа локации. Список актуальных объектов см. в описании поля **type** или в разделе [Synthetic locations API v2 - JSON models﻿](https://dt-url.net/3n43szj?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Город локации. |
| countryCode | string | Код страны локации.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). |
| countryName | string | Название страны локации. |
| entityId | string | ID сущности Dynatrace локации. |
| latitude | number | Широта локации в формате `DDD.dddd`. |
| longitude | number | Долгота локации в формате `DDD.dddd`. |
| name | string | Название локации. |
| regionCode | string | Код региона локации.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). |
| regionName | string | Название региона локации. |
| status | string | Статус локации:  * `ENABLED`: локация отображается как активная в интерфейсе. Мониторам можно назначить эту локацию. * `DISABLED`: локация отображается как неактивная в интерфейсе. Мониторам нельзя назначить эту локацию. Мониторы, уже назначенные на эту локацию, останутся там и будут выполняться с этой локации. * `HIDDEN`: локация не отображается в интерфейсе. Мониторам нельзя назначить эту локацию. Установить для локации статус `HIDDEN` можно только тогда, когда на неё не назначен ни один монитор. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `PUBLIC` -> PublicSyntheticLocation * `PRIVATE` -> PrivateSyntheticLocation * `CLUSTER` -> PrivateSyntheticLocation Элемент может принимать следующие значения * `CLUSTER` * `PRIVATE` * `PUBLIC` |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON модели тела ответа

```
{



"city": "string",



"countryCode": "string",



"countryName": "string",



"entityId": "string",



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

## Пример: публичная локация

В этом примере запрос получает данные публичной локации **Amazon US East (N. Virginia)**, имеющей ID **GEOLOCATION-95196F3C9A4F4215**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/GEOLOCATION-95196F3C9A4F4215 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/GEOLOCATION-95196F3C9A4F4215
```

#### Тело ответа

```
{



"entityId": "GEOLOCATION-95196F3C9A4F4215",



"type": "PUBLIC",



"name": "Amazon US East (N. Virginia)",



"countryCode": "US",



"regionCode": "VA",



"city": "Amazon US East (N. Virginia)",



"latitude": 39.0436,



"longitude": -77.4875,



"cloudPlatform": "AMAZON_EC2",



"ips": [



"134.189.153.97",



"134.189.153.98",



"134.189.153.99"



]



}
```

#### Код ответа

200

## Пример: приватная локация

В этом примере запрос получает данные приватной локации **Gdansk HTTP**, имеющей ID **SYNTHETIC\_LOCATION-95196F3C9A4F4215**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/SYNTHETIC_LOCATION-95196F3C9A4F4215 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/SYNTHETIC_LOCATION-95196F3C9A4F4215
```

#### Тело ответа

```
{



"entityId": "SYNTHETIC_LOCATION-9C75B59442498323",



"type": "PRIVATE",



"name": "Gdansk HTTP",



"countryCode": "PL",



"regionCode": "82",



"city": "Gdańsk",



"latitude": 54.3449,



"longitude": 18.6283,



"nodes": [



"2015649819",



"3086117876"



]



}
```

#### Код ответа

200

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор с одним URL, браузерный clickpath или HTTP-монитор.")