---
title: Synthetic locations API v2 - POST a location (Dynatrace Managed)
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/post-a-location
---

# Synthetic locations API v2 - POST a location (Dynatrace Managed)

# Synthetic locations API v2 - POST a location (Dynatrace Managed)

* Опубликовано 13 марта 2019 г.

Этот вызов API создаёт новую **приватную** synthetic location. Подробнее о создании synthetic location смотри [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."). Запрос принимает и возвращает payload в формате `application/json`.

## Аутентификация

Для выполнения этого запроса токену API нужно назначить право доступа **Service Provider API** (`ServiceProviderAPI`). Токен API генерируется через Cluster Management Console (CMC). Как получить и использовать его, описано в [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Параметр

Все вариации модели, зависящие от её типа, перечислены в [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [PrivateSyntheticLocation](#openapi-definition-PrivateSyntheticLocation) | Тело JSON запроса. Содержит параметры новой приватной synthetic location. | body | Обязательный |

### Объекты тела запроса

#### Объект `PrivateSyntheticLocation`

Конфигурация приватной synthetic location.

Часть полей унаследована от базового объекта *SyntheticLocation*.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| autoUpdateChromium | boolean | Свойство неконтейнеризованной location. Автообновление Chromium включено (`true`) или выключено (`false`). | Опциональный |
| availabilityLocationOutage | boolean | Оповещение о недоступности location включено (`true`) или выключено (`false`). Поддерживается только для приватных Synthetic locations. | Опциональный |
| availabilityNodeOutage | boolean | Оповещение о недоступности узла включено (`true`) или выключено (`false`). \n\n Если включено, недоступность *любого* узла в location вызывает оповещение. Поддерживается только для приватных Synthetic locations. | Опциональный |
| availabilityNotificationsEnabled | boolean | Уведомления о недоступности location и узла включены (`true`) или выключены (`false`). Поддерживается только для приватных Synthetic locations. | Опциональный |
| browserExecutionSupported | boolean | Свойство контейнеризованной location. Булево значение показывает, будут ли на этой location выполняться browser-мониторы:  * `false`: выполнение browser-мониторов отключено. * `true`: выполнение browser-мониторов включено. | Опциональный |
| city | string | Город location. | Опциональный |
| countryCode | string | Код страны location.  Список доступных кодов стран можно получить запросом [GET all countries﻿](https://dt-url.net/37030go?dt=m). | Опциональный |
| countryName | string | Название страны location. | Опциональный |
| deploymentType | string | Тип развёртывания location:  * `STANDARD`: location развёрнута на Windows или Linux. * `KUBERNETES`: location развёрнута на Kubernetes. Элемент может принимать значения * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` | Опциональный |
| entityId | string | ID сущности Dynatrace для location. | Опциональный |
| fipsMode | string | Свойство контейнеризованной location, указывающее, включён ли на ней режим FIPS:  * `DISABLED`: FIPS на location не включён. * `ENABLED`: FIPS на location включён. * `ENABLED_WITH_CORPORATE_PROXY`: на location включён FIPS с corporate proxy.   По умолчанию: DISABLED. Элемент может принимать значения * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` | Опциональный |
| geoLocationId | string | ID GeoLocation Dynatrace для location. | Опциональный |
| latitude | number | Широта location в формате `DDD.dddd`. | Обязательный |
| locationNodeOutageDelayInMinutes | integer | Оповещать, если недоступность location или узла длится дольше *X* минут. \n\n Применяется, только если `availabilityLocationOutage` или `availabilityNodeOutage` установлены в `true`. Поддерживается только для приватных Synthetic locations. | Опциональный |
| longitude | number | Долгота location в формате `DDD.dddd`. | Обязательный |
| namExecutionSupported | boolean | Свойство контейнеризованной location. Булево значение показывает, будут ли на этой location выполняться icmp-мониторы:  * `false`: выполнение icmp-мониторов отключено. * `true`: выполнение icmp-мониторов включено. | Опциональный |
| name | string | Название location. | Обязательный |
| nodeNames | object | Соответствие id названию узлов, принадлежащих location. | Опциональный |
| nodes | string[] | Список synthetic-узлов, принадлежащих location.  Список доступных узлов можно получить вызовом [GET all nodes﻿](https://dt-url.net/miy3rpl?dt=m). | Обязательный |
| regionCode | string | Код региона location.  Список доступных кодов регионов можно получить запросом [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). | Опциональный |
| regionName | string | Название региона location. | Опциональный |
| status | string | Статус location:  * `ENABLED`: location отображается в UI как активная. Мониторы можно назначать на эту location. * `DISABLED`: location отображается в UI как неактивная. Мониторы нельзя назначить на эту location. Мониторы, уже назначенные на location, останутся на ней и будут выполняться с этой location. * `HIDDEN`: location не отображается в UI. Мониторы нельзя назначить на эту location. Статус `HIDDEN` можно установить, только если на location не назначено ни одного монитора. Элемент может принимать значения * `DISABLED` * `ENABLED` * `HIDDEN` | Опциональный |
| type | string | -Элемент может принимать значения * `CLUSTER` * `PRIVATE` * `PUBLIC` | Обязательный |
| useNewKubernetesVersion | boolean | Свойство контейнеризованной location. Булево значение показывает, какая версия kubernetes будет использоваться:  * `false`: версия 1.23+, но старше 1.26. * `true`: версия 1.26+. | Опциональный |

### JSON модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Перед использованием в реальном запросе её нужно скорректировать.

```
{



"autoUpdateChromium": true,



"availabilityLocationNodeOutageDelayInMinutes": 5,



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"availabilityNotificationsEnabled": true,



"browserExecutionSupported": true,



"city": "Linz",



"countryCode": "AT",



"deploymentType": "STANDARD",



"fipsMode": "DISABLED",



"latitude": 48.306351,



"longitude": 14.287399,



"maxActiveGateCount": 5,



"minActiveGateCount": 2,



"namExecutionSupported": false,



"name": "Linz Location",



"nodeNames": {



"93302281": "ActiveGate 1"



},



"nodeSize": "S",



"nodes": [



"93302281"



],



"regionCode": "04",



"status": "ENABLED",



"type": "PRIVATE",



"useNewKubernetesVersion": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [SyntheticLocationIdsDto](#openapi-definition-SyntheticLocationIdsDto) | Успех. Приватная location создана. Ответ содержит ID новой location. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocationIdsDto`

DTO для ID synthetic location.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityId | string | Передаваемый ID сущности |
| geoLocationId | string | Передаваемый ID GeoLocation |

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
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON модели тела ответа

```
{



"entityId": "string",



"geoLocationId": "string"



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

В этом примере запрос создаёт новую приватную Synthetic-локацию. Локация находится в **Линце, Австрия**. Используется synthetic-нода с ID **290433380**.

Токен API передаётся в заголовке **Authorization**.

Можно скачать или скопировать тело примера запроса, чтобы протестировать его самостоятельно. Обязательно замени список нод на ноды, доступные в текущей среде. Список доступных нод можно получить запросом [GET all nodes](/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-all "List all synthetic nodes via the Synthetic v1 API.").

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"type": "PRIVATE",



"name": "REST example - Linz",



"countryCode": "AT",



"city": "Linz",



"status": "ENABLED",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": [



"290433380"



],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 5000



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations
```

#### Request body

```
{



"type": "PRIVATE",



"name": "REST example - Linz",



"countryCode": "AT",



"city": "Linz",



"status": "ENABLED",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": ["290433380"],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 5000



}
```

#### Response body

```
{



"entityId": "SYNTHETIC_LOCATION-493122BFA29674DC",



"geoLocationId": "GEOLOCATION-96B57899C9B5A3C7"



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Create a private Synthetic location in Classic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.")