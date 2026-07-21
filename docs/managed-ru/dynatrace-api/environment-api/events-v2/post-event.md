---
title: Events API v2 - POST события
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v2/post-event
scraped: 2026-05-12T11:11:48.386955
---

# Events API v2 - POST события

# Events API v2 - POST события

* Reference
* Published Nov 05, 2021

Загружает пользовательское событие в Dynatrace.

Запрос принимает данные в формате `application/json`.

Загрузка пользовательских событий потребляет [Davis Data Units (DDUs)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе Davis data units (DDU).") из пула событий.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/events/ingest` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events/ingest` |

## Аутентификация

Для выполнения запроса необходим access token со scope `events.ingest`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| body | [EventIngest](#openapi-definition-EventIngest) | JSON-тело запроса. Содержит свойства нового события. | body | Опциональный |

### Объекты тела запроса

#### Объект `EventIngest`

Конфигурация загружаемого события.

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| endTime | integer | Время окончания события в UTC-миллисекундах.  Если не задано, используется start time плюс timeout. | Опциональный |
| entitySelector | string | [Селектор сущностей](https://dt-url.net/apientityselector?dt=m), определяющий набор сущностей Dynatrace, связываемых с событием.  Можно выбрать только сущности, активные за последние 24 часа. Учтите, что фильтр `entityId` обходит это временное ограничение, что позволяет загружать события для сущностей, неактивных более 24 часов.  Если не задан, событие связывается с сущностью окружения (`dt.entity.environment`). | Опциональный |
| eventType | string | Тип события. Элемент может принимать значения * `AVAILABILITY_EVENT` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `ERROR_EVENT` * `MARKED_FOR_TERMINATION` * `PERFORMANCE_EVENT` * `RESOURCE_CONTENTION_EVENT` * `WARNING` | Обязательный |
| properties | object | Карта свойств события.  * Чтобы задать свойства события с предопределённым поведением, используйте классические свойства `dt.event.*` и `dt.davis.*`. Чтобы проверить, какие свойства относятся к классическому API, см. [Events API v2 - GET всех свойств событий](https://dt-url.net/9622g1w?dt=m). * Чтобы прикрепить к событию информацию о сущности, используйте ключи `dt.entity.*`. * Чтобы передать дополнительную информацию, можно использовать любой ключ вне пространства имён `dt.*`.  Значения свойств события с предопределённым поведением должны соответствовать требованиям соответствующего свойства.  Можно указать максимум 100 свойств. Ключ свойства может содержать до 100 символов. Значение свойства может содержать до 4096 символов. | Опциональный |
| startTime | integer | Время начала события в UTC-миллисекундах.  Если не задано, используется текущая временная метка.  В зависимости от типа события, время начала не должно быть в прошлом более чем на 6 часов для событий, открывающих проблемы, и на 30 дней для info-событий.  В зависимости от типа события, время начала не должно быть в будущем более чем на 5 минут для событий, открывающих проблемы, и на 7 дней для info-событий.  События, которые можно отправлять до 7 дней в будущем:  * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `MARKED_FOR_TERMINATION` | Опциональный |
| timeout | integer | Тайм-аут события в минутах.  Если не задан, используется 15.  Тайм-аут автоматически ограничивается максимумом в 360 минут (6 часов).  События, открывающие проблемы, можно обновлять и тем самым держать открытыми, повторно отправляя ту же payload. | Опциональный |
| title | string | Заголовок события. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

```
{



"endTime": 1,



"entitySelector": "string",



"eventType": "AVAILABILITY_EVENT",



"properties": {},



"startTime": 1,



"timeout": 1,



"title": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EventIngestResults](#openapi-definition-EventIngestResults) | Запрос на загрузку события получен сервером. Тело ответа указывает для каждого события, было ли его создание успешным. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventIngestResults`

Результаты загрузки события.

| Элемент | Тип | Описание |
| --- | --- | --- |
| eventIngestResults | [EventIngestResult[]](#openapi-definition-EventIngestResult) | Результат для каждого созданного отчёта о событии. |
| reportCount | integer | Количество созданных отчётов о событии. |

#### Объект `EventIngestResult`

Результат созданного отчёта о событии.

| Элемент | Тип | Описание |
| --- | --- | --- |
| correlationId | string | ID корреляции созданного события. |
| status | string | Статус загрузки. Элемент может принимать значения * `INVALID_ENTITY_TYPE` * `INVALID_METADATA` * `INVALID_TIMESTAMPS` * `OK` |

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



"eventIngestResults": [



{



"correlationId": "string",



"status": "INVALID_ENTITY_TYPE"



}



],



"reportCount": 1



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

## Примеры

Example 1

Example 2

Example 3

Сценарий использования

Operations-команда хочет направить событие **Marked for termination** на все хосты, запланированные к удалению. Они также хотят включить причину удаления и идентификатор задания. Хосты, подлежащие удалению, сгруппированы в специально выделенной host-group.

В этом примере запрос отправляет событие **Marked for termination** на хосты, запланированные к удалению. Такие хосты идентифицируются host-group **cloud-burst-hosts**. Событие автоматически применяется ко всем хостам, входящим в группу. Причина удаления и номер задания автоматизации передаются как дополнительная информация.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "MARKED_FOR_TERMINATION",



"title": "Planned host downscale",



"entitySelector": "type(HOST),fromRelationship.isInstanceOf(type(HOST_GROUP),entityName(cloud-burst-hosts))",



"properties": {



"job.number": "21234346"



}



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Тело запроса

```
{



"eventType": "MARKED_FOR_TERMINATION",



"title": "Planned host downscale",



"entitySelector": "type(HOST),fromRelationship.isInstanceOf(type(HOST_GROUP),entityName(cloud-burst-hosts))",



"properties": {



"job.number": "21234346"



}



}
```

#### Тело ответа

```
{



"reportCount": 2,



"eventIngestResults": [



{



"correlationId": "41f5d263011a6c9a",



"status": "OK"



},



{



"correlationId": "80eae4d163cc5760",



"status": "OK"



}



]



}
```

#### Код ответа

201

Сценарий использования

DevOps-команда хочет связать свой инструмент нагрузочного тестирования с Dynatrace, чтобы аннотировать сервис, который в данный момент проходит нагрузочный тест. Позднее, когда Dynatrace вызовет проблему, обусловленную нагрузочным тестом, в подробностях проблемы будет содержаться эта информация, что упростит процесс triage.

В этом примере запрос отправляет событие **Custom info** на сервис **BookingService**, помечая его как цель нагрузочного теста.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "CUSTOM_INFO",



"title": "Loadtest start",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"Tool": "MyLoadTool",



"Load per minute": "100",



"Load pattern": "production"



}



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Тело запроса

```
{



"eventType": "CUSTOM_INFO",



"title": "Loadtest start",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"Tool": "MyLoadTool",



"Load per minute": "100",



"Load pattern": "production"



}



}
```

#### Тело ответа

```
{



"reportCount": 1,



"eventIngestResults": [



{



"correlationId": "eba82f647696e485",



"status": "OK"



}



]



}
```

#### Код ответа

201

Сценарий использования

Operations-команда крупного ритейлера хочет триггерить алерт в Dynatrace всякий раз, когда их batch-процесс обновления каталога завершается неудачей. Они хотят создать событие и алерт в Dynatrace, но не хотят, чтобы Davis объединял это извне созданное событие с любым другим, более крупным инцидентом.

В этом примере запрос отправляет событие **Error** на сервис **BookingService**, указывающее на неудачное обновление. Свойство **dt.event.allow\_davis\_merge** установлено в `false`, что предотвращает объединение Davis этого события с любым другим событием.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request POST \



--url https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"eventType": "ERROR_EVENT",



"title": "Product catalog update failed",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"dt.event.allow_davis_merge": "false",



"Catalog": "APAC travels",



"Batch processor": "travel-catalog"



}



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/events/ingest
```

#### Тело запроса

```
{



"eventType": "ERROR_EVENT",



"title": "Product catalog update failed",



"timeout": 30,



"entitySelector": "type(SERVICE),entityName.equals(BookingService)",



"properties": {



"dt.event.allow_davis_merge": "false",



"Catalog": "APAC travels",



"Batch processor": "travel-catalog"



}



}
```

#### Тело ответа

```
{



"reportCount": 1,



"eventIngestResults": [



{



"correlationId": "cefb7ae03ac720b6",



"status": "OK"



}



]



}
```

#### Код ответа

201

## Связанные темы

* [Категории событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий и поддерживаемых типах событий, об их уровнях серьёзности и логике их порождения.")
* [Анализ и корреляция событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation "Получите представление о секции Events на каждой странице обзора хоста, процесса и сервиса.")