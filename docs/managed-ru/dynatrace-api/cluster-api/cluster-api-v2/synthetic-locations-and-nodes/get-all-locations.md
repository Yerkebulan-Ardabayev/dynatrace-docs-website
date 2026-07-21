---
title: Synthetic locations API v2 - GET all locations (Dynatrace Managed)
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all-locations
---

# Synthetic locations API v2 - GET all locations (Dynatrace Managed)

# Synthetic locations API v2 - GET all locations (Dynatrace Managed)

* Опубликовано 25 июля 2019 г.

Этот вызов API выводит список всех локаций, публичных и приватных, и их параметров, доступных для окружения. Запрос формирует полезную нагрузку `application/json`.

## Аутентификация

Для выполнения этого запроса нужно, чтобы токену API было назначено разрешение **Service Provider API** (`ServiceProviderAPI`). Сгенерировать токен API можно через Cluster Management Console (CMC). Подробнее о том, как его получить и использовать, см. [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Конечная точка

`/api/cluster/v2/synthetic/locations`

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| cloudPlatform | string | Фильтрует результирующий набор локаций до тех, которые размещены на определённой облачной платформе. Элемент может принимать следующие значения * `AWS` * `AZURE` * `ALIBABA` * `GOOGLE_CLOUD` * `OTHER` | query | Необязательный |
| type | string | Фильтрует результирующий набор локаций до локаций определённого типа. Элемент может принимать следующие значения * `PUBLIC` * `PRIVATE` | query | Необязательный |
| capability | string | Фильтрует результирующий набор локаций до тех, которые поддерживают определённую возможность. Элемент может принимать следующие значения * `BROWSER` * `HTTP` * `HTTP_HIGH_RESOURCE` * `ICMP` * `TCP` * `DNS` | query | Необязательный |

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

| Элемент | Тип | Описание |
| --- | --- | --- |
| locations | [LocationCollectionElement](#openapi-definition-LocationCollectionElement)[] | Список синтетических локаций. |

#### Объект `LocationCollectionElement`

Синтетическая локация.

| Элемент | Тип | Описание |
| --- | --- | --- |
| capabilities | string[] | Список возможностей локации. |
| cloudPlatform | string | Облачный провайдер, на котором размещена локация. Применимо только к локациям `PUBLIC`. Элемент может принимать следующие значения * `ALIBABA` * `AMAZON_EC2` * `AZURE` * `DYNATRACE_CLOUD` * `GOOGLE_CLOUD` * `INTEROUTE` * `OTHER` * `UNDEFINED` |
| deploymentType | string | Тип развёртывания локации. Элемент может принимать следующие значения * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| entityId | string | ID сущности Dynatrace для локации. |
| geoCity | string | Город локации. |
| geoContinent | string | Континент локации. |
| geoCountry | string | Страна локации. |
| geoLatitude | number | Широта локации. |
| geoLocationId | string | ID GeoLocation Dynatrace для локации. |
| geoLongitude | number | Долгота локации. |
| ips | string[] | Список IP-адресов, назначенных локации. Применимо только к локациям `PUBLIC`. |
| lastModificationTimestamp | integer | Временная метка последнего изменения локации. |
| name | string | Название локации. |
| nodes | string[] | Список синтетических узлов, принадлежащих локации. Список доступных узлов можно получить с помощью вызова [GET all nodes﻿](https://dt-url.net/miy3rpl?dt=m). |
| stage | string | Этап релиза локации. Элемент может принимать следующие значения * `BETA` * `COMING_SOON` * `DELETED` * `GA` |
| status | string | Статус локации. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Тип локации. Элемент может принимать следующие значения * `CLUSTER` * `PRIVATE` * `PUBLIC` |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
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

### Модели JSON тела ответа

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

В этом примере запрос выводит список всех синтетических локаций, доступных для окружения **mySampleEnv**.

Токен API передаётся в заголовке **Authorization**.

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



"name": "Gdańsk",



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

## Похожие темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")