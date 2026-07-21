---
title: Events API v2 - GET события
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/get-event
scraped: 2026-05-12T12:01:01.653046
---

# Events API v2 - GET события

# Events API v2 - GET события

* Reference
* Published Aug 06, 2021

Возвращает все свойства указанного события.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/events/{eventId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events/{eventId}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `events.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| eventId | string | ID требуемого события. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Event](#openapi-definition-Event) | Успех. Ответ содержит конфигурацию события. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Event`

Конфигурация события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| correlationId | string | ID корреляции события. |
| endTime | integer | Временная метка закрытия события в UTC-миллисекундах.  Имеет значение `null`, если событие всё ещё активно. |
| entityId | [EntityStub](#openapi-definition-EntityStub) | Краткое представление мониторируемой сущности. |
| entityTags | [METag[]](#openapi-definition-METag) | Список тегов связанной сущности. |
| eventId | string | ID события. |
| eventType | string | Тип события. |
| frequentEvent | boolean | Если `true`, событие происходит [часто](https://dt-url.net/4da3kdg?dt=m).  Частое событие не порождает проблему. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | Список всех зон управления, которым принадлежит событие. |
| properties | [EventProperty[]](#openapi-definition-EventProperty) | Список свойств события. |
| startTime | integer | Временная метка возникновения события в UTC-миллисекундах. |
| status | string | Статус события. Элемент может принимать значения * `CLOSED` * `OPEN` |
| suppressAlert | boolean | Статус оповещения во время [технического обслуживания](https://dt-url.net/b2123rg0?dt=m):  * `false`: оповещение работает как обычно. * `true`: оповещение отключено. |
| suppressProblem | boolean | Статус обнаружения проблем во время [технического обслуживания](https://dt-url.net/b2123rg0?dt=m):  * `false`: обнаружение проблем работает как обычно. * `true`: обнаружение проблем отключено. |
| title | string | Заголовок события. |
| underMaintenance | boolean | Если `true`, событие произошло, когда мониторируемая система находилась в режиме технического обслуживания. |

#### Объект `EntityStub`

Краткое представление мониторируемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| entityId | [EntityId](#openapi-definition-EntityId) | Краткое представление мониторируемой сущности. |
| name | string | Имя сущности.  Не включается в ответ, если сущность с соответствующим ID не найдена. |

#### Объект `EntityId`

Краткое представление мониторируемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID сущности. |
| type | string | Тип сущности. |

#### Объект `METag`

Тег мониторируемой сущности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| context | string | Происхождение тега, например AWS или Cloud Foundry.  Пользовательские теги используют значение `CONTEXTLESS`. |
| key | string | Ключ тега. |
| stringRepresentation | string | Строковое представление тега. |
| value | string | Значение тега. |

#### Объект `ManagementZone`

Краткое представление зоны управления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID зоны управления. |
| name | string | Имя зоны управления. |

#### Объект `EventProperty`

Свойство события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ свойства события. |
| value | string | Значение свойства события. |

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
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"correlationId": "933613657e1c8fcf",



"endTime": 1564039524182,



"entityId": {



"entityId": {



"id": "string",



"type": "string"



},



"name": "string"



},



"entityTags": [



{



"context": "string",



"key": "string",



"stringRepresentation": "string",



"value": "string"



}



],



"eventId": "4293884258445543163_1564039524182",



"eventType": "LOW_DISK_SPACE",



"frequentEvent": true,



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"properties": [



{



"key": "string",



"value": "string"



}



],



"startTime": 1564039524182,



"status": "OPEN",



"suppressAlert": true,



"suppressProblem": true,



"title": "High CPU load on host X",



"underMaintenance": true



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

В этом примере запрос получает параметры события с ID **6375436663535938547\_1628496488654**.

Это событие **SYNTHETIC\_GLOBAL\_OUTAGE**, указывающее на глобальный сбой browser monitors.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/6375436663535938547_1628496488654 \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/6375436663535938547_1628496488654
```

#### Тело ответа

```
{



"eventId": "6375436663535938547_1628496488654",



"startTime": 1628496488654,



"endTime": 1628503679796,



"eventType": "SYNTHETIC_GLOBAL_OUTAGE",



"title": "Browser monitor global outage",



"entityId": {



"entityId": {



"id": "SYNTHETIC_TEST-03ABB7F6446D1727",



"type": "SYNTHETIC_TEST"



},



"name": "Maintenance window test"



},



"properties": [



{



"key": "dt.event.group_label",



"value": "Browser monitor global outage"



},



{



"key": "dt.event.is_rootcause_relevant",



"value": "true"



}



],



"status": "CLOSED",



"correlationId": "aecd1653df38ef50",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "Synthetic",



"value": "Browser",



"stringRepresentation": "Synthetic:Browser"



}



],



"managementZones": [



{



"id": "-7832237287622819191",



"name": "Synthetic tests"



}



],



"underMaintenance": true,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



}
```

#### Код ответа

200

## Связанные темы

* [Категории событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий и поддерживаемых типах событий, об их уровнях серьёзности и логике их порождения.")
* [Анализ и корреляция событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Получите представление о секции Events на каждой странице обзора хоста, процесса и сервиса.")