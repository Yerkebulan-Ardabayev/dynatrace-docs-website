---
title: Synthetic locations API v2 - GET a location (Dynatrace Managed)
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-a-location
---

# Synthetic locations API v2 - GET a location (Dynatrace Managed)

# Synthetic locations API v2 - GET a location (Dynatrace Managed)

* Опубликовано 26 июля 2019 г.

Этот API вызов получает параметры указанной локации. Запрос выдаёт полезную нагрузку `application/json`.

## Аутентификация

Для выполнения этого запроса нужно, чтобы токену API было назначено разрешение **Service Provider API** (`ServiceProviderAPI`). Токен API генерируется через Cluster Management Console (CMC). О том, как получить и использовать его, см. [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Конечная точка

`/api/cluster/v2/synthetic/locations`

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| locationId | string | ID сущности Dynatrace требуемой локации. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticLocation](#openapi-definition-SyntheticLocation) | [PrivateSyntheticLocation](#openapi-definition-PrivateSyntheticLocation) | Успех. Ответ содержит параметры синтетической локации. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocation`

Конфигурация синтетической локации.

Параметры **countryCode**, **regionCode**, **city** необязательны, так как их можно получить на основе **latitude** и **longitude** локации.

Фактический набор полей зависит от типа локации. Список фактических объектов см. в описании поля **type** или в [Synthetic locations API v2 - JSON models﻿](https://dt-url.net/3n43szj?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Город локации. |
| countryCode | string | Код страны локации.  Чтобы получить список доступных кодов стран, используй запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). |
| countryName | string | Название страны локации. |
| entityId | string | ID сущности Dynatrace локации. |
| geoLocationId | string | ID GeoLocation Dynatrace локации. |
| latitude | number | Широта локации в формате `DDD.dddd`. |
| longitude | number | Долгота локации в формате `DDD.dddd`. |
| name | string | Название локации. |
| regionCode | string | Код региона локации.  Чтобы получить список доступных кодов регионов, используй запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). |
| regionName | string | Название региона локации. |
| status | string | Статус локации:  * `ENABLED`: локация отображается как активная в UI. К локации можно назначать мониторы. * `DISABLED`: локация отображается как неактивная в UI. К локации нельзя назначать мониторы. Мониторы, уже назначенные локации, остаются там и продолжают выполняться из этой локации. * `HIDDEN`: локация не отображается в UI. К локации нельзя назначать мониторы. Установить статус `HIDDEN` для локации можно только когда к ней не назначено ни одного монитора. Элемент может принимать эти значения * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `PUBLIC` -> PublicSyntheticLocation * `PRIVATE` -> PrivateSyntheticLocation * `CLUSTER` -> PrivateSyntheticLocation Элемент может принимать эти значения * `CLUSTER` * `PRIVATE` * `PUBLIC` |

#### Объект `PrivateSyntheticLocation`

Конфигурация приватной синтетической локации.

Некоторые поля унаследованы от базового объекта *SyntheticLocation*.

| Элемент | Тип | Описание |
| --- | --- | --- |
| autoUpdateChromium | boolean | Свойство неконтейнеризированной локации. Автообновление Chromium включено (`true`) или выключено (`false`). |
| availabilityLocationOutage | boolean | Оповещение о простое локации включено (`true`) или выключено (`false`). Поддерживается только для приватных Synthetic-локаций. |
| availabilityNodeOutage | boolean | Оповещение о простое узла включено (`true`) или выключено (`false`). \n\n Если включено, простой *любого* узла в локации вызывает оповещение. Поддерживается только для приватных Synthetic-локаций. |
| availabilityNotificationsEnabled | boolean | Уведомления о простое локации и узла включены (`true`) или выключены (`false`). Поддерживается только для приватных Synthetic-локаций. |
| browserExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение указывает, будут ли выполняться мониторы браузера в этой локации:  * `false`: выполнение browser-мониторов выключено. * `true`: выполнение browser-мониторов включено. |
| city | string | Город локации. |
| countryCode | string | Код страны локации.  Чтобы получить список доступных кодов стран, используй запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). |
| countryName | string | Название страны локации. |
| deploymentType | string | Тип развёртывания локации:  * `STANDARD`: локация развёрнута на Windows или Linux. * `KUBERNETES`: локация развёрнута на Kubernetes. Элемент может принимать эти значения * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| entityId | string | ID сущности Dynatrace локации. |
| fipsMode | string | Свойство контейнеризированной локации, указывающее, включён ли режим FIPS для этой локации:  * `DISABLED`: FIPS не включён для локации. * `ENABLED`: FIPS включён для локации. * `ENABLED_WITH_CORPORATE_PROXY`: для этой локации включён FIPS с корпоративным прокси.   По умолчанию: DISABLED Элемент может принимать эти значения * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` |
| geoLocationId | string | ID GeoLocation Dynatrace локации. |
| latitude | number | Широта локации в формате `DDD.dddd`. |
| locationNodeOutageDelayInMinutes | integer | Оповещать, если простой локации или узла длится дольше *X* минут. \n\n Применимо только когда `availabilityLocationOutage` или `availabilityNodeOutage` установлено в `true`. Поддерживается только для приватных Synthetic-локаций. |
| longitude | number | Долгота локации в формате `DDD.dddd`. |
| namExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение указывает, будут ли выполняться icmp-мониторы в этой локации:  * `false`: выполнение icmp-мониторов выключено. * `true`: выполнение icmp-мониторов включено. |
| name | string | Название локации. |
| nodeNames | object | Сопоставление id с именем узлов, принадлежащих локации. |
| nodes | string[] | Список синтетических узлов, принадлежащих локации.  Список доступных узлов можно получить с помощью вызова [GET all nodes﻿](https://dt-url.net/miy3rpl?dt=m). |
| regionCode | string | Код региона локации.  Чтобы получить список доступных кодов регионов, используй запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). |
| regionName | string | Название региона локации. |
| status | string | Статус локации:  * `ENABLED`: локация отображается как активная в UI. К локации можно назначать мониторы. * `DISABLED`: локация отображается как неактивная в UI. К локации нельзя назначать мониторы. Мониторы, уже назначенные локации, остаются там и продолжают выполняться из этой локации. * `HIDDEN`: локация не отображается в UI. К локации нельзя назначать мониторы. Установить статус `HIDDEN` для локации можно только когда к ней не назначено ни одного монитора. Элемент может принимать эти значения * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | -Элемент может принимать эти значения * `CLUSTER` * `PRIVATE` * `PUBLIC` |
| useNewKubernetesVersion | boolean | Свойство контейнеризированной локации. Булево значение указывает, какая версия kubernetes будет использоваться:  * `false`: версия 1.23+, но старше 1.26 * `true`: версия 1.26+. |

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
| parameterLocation | string | -Элемент может принимать эти значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON модели тела ответа

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

Все вариации модели, зависящие от типа модели, см. в [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SyntheticLocation](#openapi-definition-SyntheticLocation) | [PrivateSyntheticLocation](#openapi-definition-PrivateSyntheticLocation) | Успех. Ответ содержит параметры синтетической локации. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocation`

Конфигурация синтетической локации.

Параметры **countryCode**, **regionCode**, **city** необязательны, так как их можно получить на основе **latitude** и **longitude** локации.

Фактический набор полей зависит от типа локации. Список фактических объектов приведён в описании поля **type** или в [Synthetic locations API v2 - JSON models﻿](https://dt-url.net/3n43szj?dt=m).

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Город локации. |
| countryCode | string | Код страны локации.  Чтобы получить список доступных кодов стран, используй запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). |
| countryName | string | Название страны локации. |
| entityId | string | ID сущности Dynatrace для локации. |
| geoLocationId | string | ID GeoLocation Dynatrace для локации. |
| latitude | number | Широта локации в формате `DDD.dddd`. |
| longitude | number | Долгота локации в формате `DDD.dddd`. |
| name | string | Название локации. |
| regionCode | string | Код региона локации.  Чтобы получить список доступных кодов регионов, используй запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). |
| regionName | string | Название региона локации. |
| status | string | Статус локации:  * `ENABLED`: локация отображается в UI как активная. Можно назначать мониторы на локацию. * `DISABLED`: локация отображается в UI как неактивная. Нельзя назначать мониторы на локацию. Мониторы, уже назначенные на локацию, остаются на ней и выполняются с этой локации. * `HIDDEN`: локация не отображается в UI. Нельзя назначать мониторы на локацию. Установить статус локации как `HIDDEN` можно только если на неё не назначено ни одного монитора. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Определяет фактический набор полей в зависимости от значения. См. один из следующих объектов:  * `PUBLIC` -> PublicSyntheticLocation * `PRIVATE` -> PrivateSyntheticLocation * `CLUSTER` -> PrivateSyntheticLocation Элемент может принимать следующие значения * `CLUSTER` * `PRIVATE` * `PUBLIC` |

#### Объект `PrivateSyntheticLocation`

Конфигурация приватной синтетической локации.

Некоторые поля наследуются от базового объекта *SyntheticLocation*.

| Элемент | Тип | Описание |
| --- | --- | --- |
| autoUpdateChromium | boolean | Свойство неконтейнеризированной локации. Автообновление Chromium включено (`true`) или выключено (`false`). |
| availabilityLocationOutage | boolean | Оповещение о простое локации включено (`true`) или выключено (`false`). Поддерживается только для приватных Synthetic-локаций. |
| availabilityNodeOutage | boolean | Оповещение о простое узла включено (`true`) или выключено (`false`). \n\n Если включено, простой *любого* узла в локации вызывает оповещение. Поддерживается только для приватных Synthetic-локаций. |
| availabilityNotificationsEnabled | boolean | Уведомления о простое локации и узла включены (`true`) или выключены (`false`). Поддерживается только для приватных Synthetic-локаций. |
| browserExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение показывает, будут ли на этой локации выполняться browser-мониторы:  * `false`: выполнение browser-мониторов отключено. * `true`: выполнение browser-мониторов включено. |
| city | string | Город локации. |
| countryCode | string | Код страны локации.  Чтобы получить список доступных кодов стран, используй запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). |
| countryName | string | Название страны локации. |
| deploymentType | string | Тип развёртывания локации:  * `STANDARD`: локация развёрнута на Windows или Linux. * `KUBERNETES`: локация развёрнута на Kubernetes. Элемент может принимать следующие значения * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| entityId | string | ID сущности Dynatrace для локации. |
| fipsMode | string | Свойство контейнеризированной локации, показывающее, включён ли режим FIPS на этой локации:  * `DISABLED`: FIPS не включён на локации. * `ENABLED`: FIPS включён на локации. * `ENABLED_WITH_CORPORATE_PROXY`: на локации включён FIPS с корпоративным прокси.   По умолчанию: DISABLED. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` |
| geoLocationId | string | ID GeoLocation Dynatrace для локации. |
| latitude | number | Широта локации в формате `DDD.dddd`. |
| locationNodeOutageDelayInMinutes | integer | Оповещать, если простой локации или узла длится дольше *X* минут. \n\n Применимо только когда `availabilityLocationOutage` или `availabilityNodeOutage` установлены в `true`. Поддерживается только для приватных Synthetic-локаций. |
| longitude | number | Долгота локации в формате `DDD.dddd`. |
| namExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение показывает, будут ли на этой локации выполняться icmp-мониторы:  * `false`: выполнение icmp-мониторов отключено. * `true`: выполнение icmp-мониторов включено. |
| name | string | Название локации. |
| nodeNames | object | Соответствие id названию узлов, принадлежащих локации. |
| nodes | string[] | Список синтетических узлов, принадлежащих локации.  Список доступных узлов можно получить вызовом [GET all nodes﻿](https://dt-url.net/miy3rpl?dt=m). |
| regionCode | string | Код региона локации.  Чтобы получить список доступных кодов регионов, используй запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). |
| regionName | string | Название региона локации. |
| status | string | Статус локации:  * `ENABLED`: локация отображается в UI как активная. Можно назначать мониторы на локацию. * `DISABLED`: локация отображается в UI как неактивная. Нельзя назначать мониторы на локацию. Мониторы, уже назначенные на локацию, остаются на ней и выполняются с этой локации. * `HIDDEN`: локация не отображается в UI. Нельзя назначать мониторы на локацию. Установить статус локации как `HIDDEN` можно только если на неё не назначено ни одного монитора. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | -Элемент может принимать следующие значения * `CLUSTER` * `PRIVATE` * `PUBLIC` |
| useNewKubernetesVersion | boolean | Свойство контейнеризированной локации. Булево значение показывает, какая версия kubernetes будет использоваться:  * `false`: версия 1.23+, но старше 1.26. * `true`: версия 1.26+. |

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

### Модели JSON тела ответа

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

В этом примере запрос получает детали публичной локации **Amazon US East (N. Virginia)** с ID **SYNTHETIC\_LOCATION-0000000000000064**.

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



"name": "Gdańsk",



"countryCode": "PL",



"regionCode": "EU",



"city": "Gdańsk",



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

В этом примере запрос получает данные приватной локации **Linz HTTP** с идентификатором **SYNTHETIC\_LOCATION-BB5EE23C1D48AFF5**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-BB5EE23C1D48AFF5 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-BB5EE23C1D48AFF5
```

#### Response body

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

## Похожие темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")