---
title: "Synthetic locations API v2 - GET all locations (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all-locations
updated: 2026-02-09
---

Этот API-вызов возвращает список всех locations (public и private) и их параметров, доступных в вашем окружении. Запрос возвращает payload `application/json`.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| cloudPlatform | string | Фильтрует результирующий набор locations по конкретной cloud-платформе. Возможные значения: * `AWS` * `AZURE` * `ALIBABA` * `GOOGLE_CLOUD` * `OTHER` | query | Optional |
| type | string | Фильтрует результирующий набор locations по конкретному типу. Возможные значения: * `PUBLIC` * `PRIVATE` | query | Optional |
| capability | string | Фильтрует результирующий набор locations по поддерживаемой capability. Возможные значения: * `BROWSER` * `HTTP` * `HTTP_HIGH_RESOURCE` * `ICMP` * `TCP` * `DNS` | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticLocations](#openapi-definition-SyntheticLocations) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocations`

Список synthetic locations.

| Элемент | Тип | Описание |
| --- | --- | --- |
| locations | [LocationCollectionElement[]](#openapi-definition-LocationCollectionElement) | Список synthetic locations. |

#### Объект `LocationCollectionElement`

Synthetic location.

| Элемент | Тип | Описание |
| --- | --- | --- |
| capabilities | string[] | Список capabilities location. |
| cloudPlatform | string | Cloud-провайдер, на котором хостится location.  Применимо только к `PUBLIC` locations. Возможные значения: * `ALIBABA` * `AMAZON_EC2` * `AZURE` * `DYNATRACE_CLOUD` * `GOOGLE_CLOUD` * `INTEROUTE` * `OTHER` * `UNDEFINED` |
| deploymentType | string | Тип развёртывания location. Возможные значения: * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| entityId | string | Dynatrace entity ID location. |
| geoCity | string | Город location. |
| geoContinent | string | Континент location. |
| geoCountry | string | Страна location. |
| geoLatitude | number | Широта location. |
| geoLocationId | string | Dynatrace GeoLocation ID location. |
| geoLongitude | number | Долгота location. |
| ips | string[] | Список IP-адресов, назначенных location.  Применимо только к `PUBLIC` locations. |
| lastModificationTimestamp | integer | Timestamp последнего изменения location. |
| name | string | Имя location. |
| nodes | string[] | Список synthetic nodes, принадлежащих location.  Получить список доступных нод можно через вызов [GET all nodes](https://dt-url.net/miy3rpl). |
| stage | string | Release stage location. Возможные значения: * `BETA` * `COMING_SOON` * `DELETED` * `GA` |
| status | string | Статус location. Возможные значения: * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Тип location. Возможные значения: * `CLUSTER` * `PRIVATE` * `PUBLIC` |

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

В этом примере запрос возвращает все synthetic locations, доступные в окружении **mySampleEnv**.

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


"name": "GdaÅsk",


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

* Synthetic Monitoring
