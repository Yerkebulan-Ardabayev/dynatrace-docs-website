---
title: Synthetic locations API v2 - GET все локации
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/get-all-locations
scraped: 2026-05-12T11:59:15.344934
---

# Synthetic locations API v2 - GET все локации

# Synthetic locations API v2 - GET все локации

* Справочник
* Опубликовано 25 июля 2019 г.

Возвращает список всех локаций, публичных и приватных, и их параметры, доступные для вашего окружения.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/locations` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/locations` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `syntheticLocations.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| cloudPlatform | string | Фильтрует итоговый набор локаций, оставляя те, что размещены на конкретной облачной платформе. Поле может принимать значения: * `AWS` * `AZURE` * `ALIBABA` * `GOOGLE_CLOUD` * `OTHER` | query | Необязательный |
| type | string | Фильтрует итоговый набор локаций, оставляя локации определённого типа. Поле может принимать значения: * `PUBLIC` * `PRIVATE` | query | Необязательный |
| capability | string | Фильтрует итоговый набор локаций, оставляя те, что поддерживают конкретную возможность. Поле может принимать значения: * `BROWSER` * `HTTP` * `HTTP_HIGH_RESOURCE` * `ICMP` * `TCP` * `DNS` | query | Необязательный |

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
| deploymentType | string | Тип развёртывания локации Поле может принимать значения: * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| entityId | string | Dynatrace entity ID локации. |
| geoCity | string | Город локации. |
| geoContinent | string | Континент локации. |
| geoCountry | string | Страна локации. |
| geoLatitude | number | Широта локации. |
| geoLocationId | string | Dynatrace GeoLocation ID локации. |
| geoLongitude | number | Долгота локации. |
| ips | string[] | Список IP-адресов, назначенных локации.  Применимо только к локациям `PUBLIC`. |
| lastModificationTimestamp | integer | Метка времени последнего изменения локации. |
| name | string | Имя локации. |
| nodes | string[] | Список синтетических узлов, принадлежащих локации.  Список доступных узлов можно получить вызовом [GET all nodes](https://dt-url.net/miy3rpl?dt=m). |
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



"entityId": "SYNTHETIC_LOCATION-53F47ECB33907667",



"geoCity": "Gdansk",



"geoContinent": "Europe",



"geoCountry": "Poland",



"geoLatitude": "54.399078369140625",



"geoLocationId": "GEOLOCATION-95196F3C9A4F4215",



"geoLongitude": "18.576557159423828",



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



"geoLocationId": "GEOLOCATION-95196F3C9A4F4215",



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



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations
```

#### Тело ответа

```
{



"locations": [



{



"name": "Amazon US East (N. Virginia)",



"entityId": "SYNTHETIC_LOCATION-0000000000000004",



"type": "PUBLIC",



"cloudPlatform": "AMAZON_EC2",



"ips": [



"79.50.224.74",



"96.124.117.100"



],



"stage": "GA",



"status": "ENABLED",



"capabilities": [



"BROWSER"



],



"geoLocationId": "GEOLOCATION-95196F3C9A4F4215"



},



{



"name": "GdaÅsk",



"entityId": "SYNTHETIC_LOCATION-0000000000000064",



"type": "PUBLIC",



"cloudPlatform": "OTHER",



"ips": [



"120.157.221.247",



"172.158.6.93",



"197.136.70.30",



"227.53.205.237",



"131.123.197.12"



],



"stage": "GA",



"status": "ENABLED",



"capabilities": [



"BROWSER",



"HTTP"



],



"geoLocationId": "GEOLOCATION-0A41430434C388A9"



},



{



"name": "Linz HTTP",



"entityId": "SYNTHETIC_LOCATION-BB5EE23C1D48AFF5",



"type": "PRIVATE",



"status": "ENABLED",



"geoLocationId": "GEOLOCATION-427705B3488A4C45"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")