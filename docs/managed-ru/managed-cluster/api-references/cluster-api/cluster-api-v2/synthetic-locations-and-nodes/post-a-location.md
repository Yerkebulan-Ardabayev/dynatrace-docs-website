---
title: "Synthetic locations API v2 - POST a location (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/post-a-location
updated: 2026-02-09
---

Этот API-вызов создаёт новый **private** synthetic location. Подробнее о создании synthetic location смотрите в Create a private Synthetic location. Запрос принимает и возвращает payload `application/json`.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Параметр

Все вариации модели в зависимости от её типа смотрите в JSON models.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [PrivateSyntheticLocation](#openapi-definition-PrivateSyntheticLocation) | JSON-тело запроса. Содержит параметры нового private synthetic location. | body | Required |

### Объекты тела запроса

#### Объект `PrivateSyntheticLocation`

Конфигурация private synthetic location.

Некоторые поля наследуются от базового объекта *SyntheticLocation*.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| autoUpdateChromium | boolean | Свойство неконтейнеризованного location. Auto upgrade Chromium включён (`true`) или выключен (`false`). | Optional |
| availabilityLocationOutage | boolean | Алертинг по отказу location включён (`true`) или выключен (`false`). Поддерживается только для private Synthetic locations. | Optional |
| availabilityNodeOutage | boolean | Алертинг по отказу ноды включён (`true`) или выключен (`false`). \n\n Если включён, отказ *любой* ноды в location триггерит алерт. Поддерживается только для private Synthetic locations. | Optional |
| availabilityNotificationsEnabled | boolean | Уведомления о отказах location и ноды включены (`true`) или выключены (`false`). Поддерживается только для private Synthetic locations. | Optional |
| browserExecutionSupported | boolean | Свойство контейнеризованного location. Boolean-значение, описывающее, будут ли browser monitors выполняться на этом location:  * `false`: Выполнение browser monitor отключено. * `true`: Выполнение browser monitor включено. | Optional |
| city | string | Город location. | Optional |
| countryCode | string | Код страны location.  Список доступных кодов стран можно получить через запрос [GET all countries](https://dt-url.net/37030go). | Optional |
| countryName | string | Имя страны location. | Optional |
| deploymentType | string | Тип развёртывания location:  * `STANDARD`: Location развёрнут на Windows или Linux. * `KUBERNETES`: Location развёрнут на Kubernetes. Возможные значения: * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` | Optional |
| entityId | string | Dynatrace entity ID location. | Optional |
| fipsMode | string | Свойство контейнеризованного location, указывающее, включён ли FIPS на location:  * `DISABLED`: FIPS не включён на location. * `ENABLED`: FIPS включён на location. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS с corporate proxy включён на этом location.   По умолчанию: DISABLED Возможные значения: * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` | Optional |
| geoLocationId | string | Dynatrace GeoLocation ID location. | Optional |
| latitude | number | Широта location в формате `DDD.dddd`. | Required |
| locationNodeOutageDelayInMinutes | integer | Алерт, если отказ location или ноды длится дольше *X* минут. \n\n Применимо только когда `availabilityLocationOutage` или `availabilityNodeOutage` равны `true`. Поддерживается только для private Synthetic locations. | Optional |
| longitude | number | Долгота location в формате `DDD.dddd`. | Required |
| namExecutionSupported | boolean | Свойство контейнеризованного location. Boolean-значение, описывающее, будут ли icmp monitors выполняться на этом location:  * `false`: Выполнение icmp monitor отключено. * `true`: Выполнение icmp monitor включено. | Optional |
| name | string | Имя location. | Required |
| nodeNames | object | Маппинг id на имя нод, принадлежащих location. | Optional |
| nodes | string[] | Список synthetic nodes, принадлежащих location.  Получить список доступных нод можно через вызов [GET all nodes](https://dt-url.net/miy3rpl). | Required |
| regionCode | string | Код региона location.  Список доступных кодов регионов можно получить через запрос [GET regions of the country](https://dt-url.net/az230x0). | Optional |
| regionName | string | Имя региона location. | Optional |
| status | string | Статус location:  * `ENABLED`: Location отображается как активный в UI. Можно назначать мониторы на location. * `DISABLED`: Location отображается как неактивный в UI. Нельзя назначать мониторы на location. Уже назначенные мониторы остаются и выполняются с location. * `HIDDEN`: Location не отображается в UI. Нельзя назначать мониторы на location. Установить `HIDDEN` можно только если ни один монитор не назначен. Возможные значения: * `DISABLED` * `ENABLED` * `HIDDEN` | Optional |
| type | string | -Возможные значения: * `CLUSTER` * `PRIVATE` * `PUBLIC` | Required |
| useNewKubernetesVersion | boolean | Свойство контейнеризованного location. Boolean-значение, описывающее, какая версия kubernetes будет использоваться:  * `false`: Версия 1.23+, но старее 1.26 * `true`: Версия 1.26+. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **201** | [SyntheticLocationIdsDto](#openapi-definition-SyntheticLocationIdsDto) | Успех. Private location создан. Ответ содержит ID нового location. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticLocationIdsDto`

DTO для ID synthetic location.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityId | string | Передаваемый Entity ID |
| geoLocationId | string | Передаваемый GeoLocation ID |

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

В этом примере запрос создаёт новый private Synthetic location. Этот location находится в **Линце, Австрия**. Используется synthetic node с ID **290433380**.

API-токен передаётся в заголовке **Authorization**.

Можно скачать или скопировать пример тела запроса для своих экспериментов. Не забудьте заменить список нод на ноды, доступные в вашем окружении. Список доступных нод можно получить через запрос GET all nodes.

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

* Synthetic Monitoring
* Create a private Synthetic location
