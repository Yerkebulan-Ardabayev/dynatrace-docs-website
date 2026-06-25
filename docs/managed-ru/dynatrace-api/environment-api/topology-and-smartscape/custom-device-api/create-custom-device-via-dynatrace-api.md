---
title: Create custom device via the Dynatrace API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/create-custom-device-via-dynatrace-api
scraped: 2026-05-12T11:49:57.855234
---

# Create custom device via the Dynatrace API

# Create custom device via the Dynatrace API

* Reference
* Updated on Mar 22, 2023
* Deprecated

Endpoint **Custom device** API **Topology and Smartscape** позволяет создать custom device с заданным именем в вашем окружении Dynatrace.

На этой странице описано, как создать custom device, не отправляя в него никаких данных.

О том, как сообщать данные в custom device, см. [Report custom device metric via REST API](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Узнайте, как использовать Dynatrace API для отправки точки данных пользовательской метрики в custom device.").

Запрос принимает и возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/infrastructure/custom/{customDeviceId}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/infrastructure/custom/{customDeviceId}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Для этого сценария элемент **series** тела запроса должен быть **опущен**.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| customDeviceId | string | ID custom device.  Если вы используете ID существующего устройства, соответствующие параметры будут обновлены.  Не используйте здесь ID сущности Dynatrace. | path | Required |
| body | [CustomDevicePushMessage](#openapi-definition-CustomDevicePushMessage) | JSON-тело запроса. Содержит параметры custom device. | body | Optional |

### Объекты тела запроса

#### Объект `CustomDevicePushMessage`

Конфигурация custom device.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| configUrl | string | URL веб-страницы конфигурации custom device, например страница входа для firewall или роутера. | Optional |
| displayName | string | Имя custom device, которое появится в пользовательском интерфейсе. | Optional |
| favicon | string | Иконка, отображаемая для вашего пользовательского компонента в Smartscape. Укажите полный URL файла иконки. | Optional |
| group | string | Заданный пользователем ID группы сущности.  ID группы помогает поддерживать согласованную картину связей устройство-группа. Один из многих случаев, где важна правильная группа, это обнаружение сервисов: вы можете определить, какие custom device должны вести к одному сервису, задав им одинаковый ID группы.  Если вы задаёте ID группы, он будет захеширован в ID сущности Dynatrace для custom device. В этом случае custom device может быть частью только одной группы custom device.  Если вы не задаёте ID группы, Dynatrace создаст его на основе ID или типа custom device. Также группа не будет захеширована в ID устройства, что означает, что устройство может менять группы. | Optional |
| hostNames | string[] | Список имён хостов, связанных с custom device.  Эти имена используются для автоматического обнаружения горизонтальной связи взаимодействия между этим компонентом и всеми другими наблюдаемыми компонентами в Smartscape. Как только связь обнаружена, она автоматически отображается на карте Smartscape.  Если вы отправляете значение, существующие значения будут перезаписаны.  Если вы отправляете `null` или пустое значение; или опускаете это поле, существующие значения будут сохранены. | Optional |
| ipAddresses | string[] | Список IP-адресов, принадлежащих custom device.  Эти адреса используются для автоматического обнаружения горизонтальной связи взаимодействия между этим компонентом и всеми другими наблюдаемыми компонентами в Smartscape. Как только связь обнаружена, она автоматически отображается на карте Smartscape.  Если вы отправляете значение (включая пустое значение), существующие значения будут перезаписаны.  Если вы отправляете `null` или опускаете это поле, существующие значения будут сохранены. | Optional |
| listenPorts | integer[] | Список портов, которые слушает custom device.  Эти порты используются для обнаружения горизонтальной связи взаимодействия между этим компонентом и всеми другими наблюдаемыми компонентами в Smartscape.  Как только связь обнаружена, она автоматически отображается на карте Smartscape.  Если порты указаны, следует также добавить хотя бы один IP-адрес или имя хоста для custom device.  Если вы отправляете значение, существующие значения будут перезаписаны.  Если вы отправляете `null`, или пустое значение, или опускаете это поле, существующие значения будут сохранены. | Optional |
| properties | object | Список свойств в виде пар ключ-значение, которые будут показаны под инфографикой вашего custom device. | Optional |
| series | [EntityTimeseriesData[]](#openapi-definition-EntityTimeseriesData) | Список значений метрик, которые сообщаются для custom device.  Метрика, которую вы сообщаете, уже должна существовать в Dynatrace. О том, как создать пользовательскую метрику, см. [Timeseries API v1 - PUT a custom metric](https://dt-url.net/5k143rzb).  Dynatrace агрегирует все значения, которые вы сообщаете для custom device.  Если вы отправляете значение (включая пустое значение), оно будет добавлено к набору существующих значений.  Если вы отправляете `null` или опускаете это поле, набор существующих значений не изменится. | Optional |
| tags | string[] | Список пользовательских тегов, которые вы хотите прикрепить к вашему custom device. | Optional |
| type | string | Определение типа технологии custom device.  Оно должно совпадать с типом технологии метрики, которую вы сообщаете.  Если вы отправляете значение, существующее значение будет перезаписано.  Если вы отправляете `null`, пустое значение или опускаете это поле, существующее значение будет сохранено. | Optional |

#### Объект `EntityTimeseriesData`

Информация о метрике и её точках данных.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dataPoints | array[] | Список точек данных.  Каждая точка данных это массив, содержащий метку времени и значение.  Метка времени это миллисекунды UTC, сообщаемые как число, например: `1520523365557`.  У вас есть гарантированный временной диапазон в **30 минут** в прошлое.  Пользовательская метрика должна быть зарегистрирована **до** того, как вы сможете сообщить значение метрики. Поэтому метка времени для сообщения значения должна быть после времени регистрации метрики. | Required |
| dimensions | object | Измерения точек данных, которые вы отправляете.  Ключ измерения метрики должен быть определён ранее в определении метрики. | Optional |
| timeseriesId | string | ID метрики, в которую вы хотите отправить точки данных. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"configUrl": "http://coffee-machine.dynatrace.internal.com/coffeemachine/manage",



"displayName": "coffeeMachine",



"favicon": "https://www.freefavicon.com/freefavicons/food/cup-of-coffee-152-78475.png",



"group": "myCustomDeviceGroup",



"hostNames": [



"coffee-machine.dynatrace.internal.com"



],



"ipAddresses": [



"10.0.0.1"



],



"listenPorts": [



80



],



"properties": {},



"series": [



{



"dataPoints": [



[



1521542929000,



13



]



],



"dimensions": {



"office": "Linz"



},



"timeseriesId": "custom:created.coffee.metric"



}



],



"tags": [



"office-linz"



],



"type": "coffee machine"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CustomDevicePushResult](#openapi-definition-CustomDevicePushResult) | Успех. Custom device создан или обновлён. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CustomDevicePushResult`

Результат запроса push для custom device. ID сущности вычисляется автоматически.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityId | string | ID сущности Dynatrace для custom device. |
| groupId | string | ID сущности Dynatrace для группы custom device. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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



"groupId": "string"



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

В этом примере запрос создаёт custom device `idOfmyCustomDevice` типа `F5-Firewall`, с IP-адресом `172.16.115.211` и портом прослушивания `9999`. Запрос также указывает некоторые дополнительные параметры.

См. [Report custom device metric via the Dynatrace API](/managed/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Узнайте, как использовать Dynatrace API для отправки точки данных пользовательской метрики в custom device."), чтобы узнать, как отправить данные в только что созданный custom device.

API-токен передаётся в заголовке **Authorization**.

Запрос возвращает ID custom device (см. `entityId`) и его группы (см. `groupId`) в качестве подтверждения.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'



-H 'Content-Type: application/json' \



-d '{



"displayName" : "F5 Firewall 24",



"ipAddresses" : ["172.16.115.211"],



"listenPorts" : ["9999"],



"type" : "F5-Firewall",



"favicon" : "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl" : "http://192.128.0.1:8080",



"tags": [



"REST example"



],



"properties" : {



"Sample Property 1": "Sample value 1"



}



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/custom/idOfmyCustomDevice
```

#### Тело запроса

```
{



"displayName": "F5 Firewall 24",



"ipAddresses": ["172.16.115.211"],



"listenPorts": ["9999"],



"type": "F5-Firewall",



"favicon": "http://assets.dynatrace.com/global/icons/f5.png",



"configUrl": "http://192.128.0.1:8080",



"tags": ["REST example"],



"properties": {



"Sample Property 1": "Sample value 1"



}



}
```

#### Тело ответа

```
{



"entityId": "CUSTOM_DEVICE-6A567B33AADC306E",



"groupId": "CUSTOM_DEVICE_GROUP-FC2E2ABF54F513D8"



}
```

#### Код ответа

200

#### Результат

![Новый custom device в Smartscape](https://dt-cdn.net/images/custom-device-smartscape-1103-ba9b69e490.png)

Новый custom device в Smartscape

![Свойства custom device](https://dt-cdn.net/images/custom-device-658-bb2295e42c.png)

Свойства custom device