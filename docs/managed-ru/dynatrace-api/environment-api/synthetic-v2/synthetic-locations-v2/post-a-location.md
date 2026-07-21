---
title: Synthetic locations API v2 - POST локация
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/post-a-location
scraped: 2026-05-12T11:59:19.579719
---

# Synthetic locations API v2 - POST локация

# Synthetic locations API v2 - POST локация

* Справочник
* Опубликовано 13 марта 2019 г.

Создаёт новую **приватную** синтетическую локацию. Подробнее о создании синтетической локации смотрите [Создание приватной синтетической локации](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для синтетического мониторинга.").

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/locations` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/locations` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `syntheticLocations.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметр

Все вариации модели, зависящие от типа модели, смотрите в [JSON-моделях](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Получение информации о синтетических узлах через Synthetic v2 API.").

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [PrivateSyntheticLocation](#openapi-definition-PrivateSyntheticLocation) | JSON-тело запроса. Содержит параметры новой приватной синтетической локации. | body | Обязательный |

### Объекты тела запроса

#### Объект `PrivateSyntheticLocation`

Конфигурация приватной синтетической локации.

Часть полей наследуется от базового объекта *SyntheticLocation*.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| autoUpdateChromium | boolean | Свойство неконтейнеризированной локации. Авто-обновление Chromium включено (`true`) или отключено (`false`). | Необязательный |
| availabilityLocationOutage | boolean | Оповещение о недоступности локации включено (`true`) или отключено (`false`). Поддерживается только для приватных синтетических локаций. | Необязательный |
| availabilityNodeOutage | boolean | Оповещение о недоступности узла включено (`true`) или отключено (`false`). \n\n Если включено, недоступность *любого* узла в локации вызывает алерт. Поддерживается только для приватных синтетических локаций. | Необязательный |
| availabilityNotificationsEnabled | boolean | Уведомления о недоступности локации и узла включены (`true`) или отключены (`false`). Поддерживается только для приватных синтетических локаций. | Необязательный |
| browserExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение описывает, будут ли браузерные мониторы выполняться на этой локации:  * `false`: выполнение браузерных мониторов отключено. * `true`: выполнение браузерных мониторов включено. | Необязательный |
| city | string | Город локации. | Необязательный |
| countryCode | string | Код страны локации.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go?dt=m). | Необязательный |
| countryName | string | Название страны локации. | Необязательный |
| deploymentType | string | Тип развёртывания локации:  * `STANDARD`: локация развёрнута на Windows или Linux. * `KUBERNETES`: локация развёрнута на Kubernetes. Поле может принимать значения: * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` | Необязательный |
| entityId | string | Dynatrace entity ID локации. | Необязательный |
| fipsMode | string | Свойство контейнеризированной локации, указывающее, включён ли на этой локации режим FIPS:  * `DISABLED`: FIPS не включён на локации. * `ENABLED`: FIPS включён на локации. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS с корпоративным прокси включён на этой локации.   По умолчанию: DISABLED Поле может принимать значения: * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` | Необязательный |
| geoLocationId | string | Dynatrace GeoLocation ID локации. | Необязательный |
| latitude | number | Широта локации в формате `DDD.dddd`. | Обязательный |
| locationNodeOutageDelayInMinutes | integer | Алерт, если недоступность локации или узла длится дольше *X* минут. \n\n Применимо только если `availabilityLocationOutage` или `availabilityNodeOutage` установлено в `true`. Поддерживается только для приватных синтетических локаций. | Необязательный |
| longitude | number | Долгота локации в формате `DDD.dddd`. | Обязательный |
| namExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение описывает, будут ли icmp-мониторы выполняться на этой локации:  * `false`: выполнение icmp-мониторов отключено. * `true`: выполнение icmp-мониторов включено. | Необязательный |
| name | string | Имя локации. | Обязательный |
| nodeNames | object | Сопоставление id и имени узлов, принадлежащих локации. | Необязательный |
| nodes | string[] | Список синтетических узлов, принадлежащих локации.  Список доступных узлов можно получить вызовом [GET all nodes](https://dt-url.net/miy3rpl?dt=m). | Обязательный |
| regionCode | string | Код региона локации.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0?dt=m). | Необязательный |
| regionName | string | Название региона локации. | Необязательный |
| status | string | Статус локации:  * `ENABLED`: локация отображается в UI как активная. Локации можно назначать мониторы. * `DISABLED`: локация отображается в UI как неактивная. Локации нельзя назначать мониторы. Мониторы, уже назначенные локации, останутся там и будут выполняться с этой локации. * `HIDDEN`: локация не отображается в UI. Локации нельзя назначать мониторы. Установить локацию в `HIDDEN` можно только тогда, когда ей не назначен ни один монитор. Поле может принимать значения: * `DISABLED` * `ENABLED` * `HIDDEN` | Необязательный |
| type | string | -Поле может принимать значения: * `CLUSTER` * `PRIVATE` * `PUBLIC` | Обязательный |
| useNewKubernetesVersion | boolean | Свойство контейнеризированной локации. Булево значение описывает, какая версия kubernetes будет использоваться:  * `false`: версия 1.23+, более старая чем 1.26 * `true`: версия 1.26+. | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

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
| **201** | [SyntheticLocationIdsDto](#openapi-definition-SyntheticLocationIdsDto) | Успех. Приватная локация создана. Ответ содержит ID новой локации. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocationIdsDto`

DTO для ID синтетических локаций.

| Поле | Тип | Описание |
| --- | --- | --- |
| entityId | string | Entity ID для передачи |
| geoLocationId | string | GeoLocation ID для передачи |

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

В этом примере запрос создаёт новую приватную синтетическую локацию. Эта локация находится в **Linz, Austria**. Она использует синтетический узел с ID **290433380**.

API-токен передаётся в заголовке **Authorization**.

Можно скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно замените список узлов на узлы, доступные в вашем окружении. Список доступных узлов можно получить запросом [GET all nodes](/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-all "Получение списка всех синтетических узлов через Synthetic v1 API.").

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

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations
```

#### Тело запроса

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

#### Тело ответа

```
{



"entityId": "SYNTHETIC_LOCATION-493122BFA29674DC",



"geoLocationId": "GEOLOCATION-96B57899C9B5A3C7"



}
```

#### Код ответа

200

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")
* [Создание приватной синтетической локации](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для синтетического мониторинга.")