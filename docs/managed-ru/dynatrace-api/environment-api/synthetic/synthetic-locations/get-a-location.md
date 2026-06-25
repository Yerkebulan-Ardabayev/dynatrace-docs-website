---
title: Synthetic locations API - GET локация
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-a-location
scraped: 2026-05-12T11:56:51.982082
---

# Synthetic locations API - GET локация

# Synthetic locations API - GET локация

* Справочник
* Опубликовано 26 июля 2019 г.

Доступна новая версия этого API, [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Узнайте, что предлагает Dynatrace Synthetic v2 API."). Попробуйте её!

Возвращает параметры указанной локации.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | Dynatrace entity ID требуемой локации. | path | Обязательный |

## Ответ

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models "Узнайте о вариациях моделей в Synthetic locations v1 API.").

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

В этом примере запрос возвращает детали публичной локации **Amazon US East (N. Virginia)**, у которой ID равен **GEOLOCATION-95196F3C9A4F4215**.

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

## Пример - приватная локация

В этом примере запрос возвращает детали приватной локации **Gdansk HTTP**, у которой ID равен **SYNTHETIC\_LOCATION-95196F3C9A4F4215**.

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



"city": "GdaÅsk",



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

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")