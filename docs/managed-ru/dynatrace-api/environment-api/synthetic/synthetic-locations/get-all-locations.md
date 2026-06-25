---
title: Synthetic locations API - GET все локации
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations
scraped: 2026-05-12T11:57:03.991853
---

# Synthetic locations API - GET все локации

# Synthetic locations API - GET все локации

* Справочник
* Опубликовано 25 июля 2019 г.

Доступна новая версия этого API, [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Узнайте, что предлагает Dynatrace Synthetic v2 API."). Попробуйте её!

Возвращает список всех локаций, публичных и приватных, и их параметры, доступные для вашего окружения.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| cloudPlatform | string | Фильтрует итоговый набор локаций, оставляя те, что размещены на конкретной облачной платформе. Поле может принимать значения: * `AWS` * `AZURE` * `ALIBABA` * `GOOGLE_CLOUD` * `OTHER` | query | Необязательный |
| type | string | Фильтрует итоговый набор локаций, оставляя локации определённого типа. Поле может принимать значения: * `PUBLIC` * `PRIVATE` | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticLocations](#openapi-definition-SyntheticLocations) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocations`

Список синтетических локаций.

| Поле | Тип | Описание |
| --- | --- | --- |
| locations | [LocationCollectionElement[]](#openapi-definition-LocationCollectionElement) | Список синтетических локаций. |

#### Объект `LocationCollectionElement`

Синтетическая локация.

| Поле | Тип | Описание |
| --- | --- | --- |
| capabilities | string[] | Список возможностей локации. |
| cloudPlatform | string | Облачный провайдер, на котором размещена локация.  Применимо только к локациям `PUBLIC`. Поле может принимать значения: * `ALIBABA` * `AMAZON_EC2` * `AZURE` * `DYNATRACE_CLOUD` * `GOOGLE_CLOUD` * `INTEROUTE` * `OTHER` * `UNDEFINED` |
| entityId | string | Dynatrace entity ID локации. |
| ips | string[] | Список IP-адресов, назначенных локации.  Применимо только к локациям `PUBLIC`. |
| name | string | Имя локации. |
| stage | string | Стадия выпуска локации. Поле может принимать значения: * `BETA` * `COMING_SOON` * `DELETED` * `GA` |
| status | string | Статус локации. Поле может принимать значения: * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Тип локации. Поле может принимать значения: * `CLUSTER` * `PRIVATE` * `PUBLIC` |

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



"locations": [



{



"capabilities": [



"BROWSER",



"HTTP"



],



"cloudPlatform": "AMAZON_EC2",



"entityId": "GEOLOCATION-B8D793BCA914E0AF",



"ips": [



"134.189.153.97",



"134.189.153.98"



],



"name": "Gdansk",



"stage": "GA",



"status": "ENABLED",



"type": "PUBLIC"



},



{



"entityId": "SYNTHETIC_LOCATION-53F47ECB33907667",



"name": "My private location",



"status": "ENABLED",



"type": "PRIVATE"



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

## Пример

В этом примере запрос возвращает список всех синтетических локаций, доступных для окружения **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations
```

#### Тело ответа

```
{



"locations": [



{



"name": "Amazon US East (N. Virginia)",



"entityId": "GEOLOCATION-95196F3C9A4F4215",



"type": "PUBLIC",



"cloudPlatform": "AMAZON_EC2",



"ips": [



"134.189.153.97",



"134.189.153.98",



"134.189.153.99"



]



},



{



"name": "AWS Europe (London)",



"entityId": "GEOLOCATION-A9022AAFA0763F56",



"type": "PUBLIC",



"cloudPlatform": "AMAZON_EC2",



"ips": [



"243.22.221.174",



"104.179.71.29"



]



},



{



"name": "Gdansk HTTP",



"entityId": "SYNTHETIC_LOCATION-9C75B59442498323",



"type": "PRIVATE"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")