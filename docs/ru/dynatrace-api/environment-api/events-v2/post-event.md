---
title: Events API v2 - POST an event
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/events-v2/post-event
scraped: 2026-03-06T21:28:21.680541
---

# Events API v2 - Отправка события (POST)


Загружает пользовательское событие в Dynatrace.

Запрос принимает полезную нагрузку `application/json`.

Загрузка пользовательских событий потребляет Davis Data Units (DDUs).") из пула событий.

|  |  |  |
| --- | --- | --- |
| POST | Managed | `https://{your-environment-id}.live.dynatrace.com/api/v2/events/ingest` |
| POST | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/events/ingest` |

## Аутентификация

Для выполнения этого запроса вам необходим токен доступа с областью действия `events.ingest`.

Чтобы узнать, как его получить и использовать, см. Tokens and authentication.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| body | [EventIngest](#openapi-definition-EventIngest) | JSON-тело запроса. Содержит свойства нового события. | body | Необязательный |

### Объекты тела запроса

#### Объект `EventIngest`

Конфигурация события для загрузки.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| endTime | integer | Время окончания события в миллисекундах UTC. Если не задано, используется время начала плюс таймаут. | Необязательный |
| entitySelector | string | [Селектор сущностей](https://dt-url.net/apientityselector), определяющий набор сущностей Dynatrace, которые будут связаны с событием. Могут быть выбраны только сущности, активные в течение последних 24 часов. Обратите внимание, что фильтр `entityId` обходит это ограничение по времени, позволяя загружать события для сущностей, неактивных более 24 часов. Если не задано, событие связывается с сущностью среды (`dt.entity.environment`). | Необязательный |
| eventType | string | Тип события. Элемент может содержать следующие значения: * `AVAILABILITY_EVENT` * `CUSTOM_ALERT` * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `ERROR_EVENT` * `MARKED_FOR_TERMINATION` * `PERFORMANCE_EVENT` * `RESOURCE_CONTENTION_EVENT` * `WARNING` | Обязательный |
| properties | object | Карта свойств события. * Для установки свойств события с предопределённым поведением используйте классические свойства `dt.event.*` и `dt.davis.*`. Чтобы проверить, какие свойства относятся к классическому API, см. [Events API v2 - GET all event properties](https://dt-url.net/9622g1w). * Для прикрепления информации о сущности к событию используйте ключи `dt.entity.*`. * Для предоставления дополнительной информации можно использовать любой ключ за пределами пространства имён `dt.*`. Значения свойств события с предопределённым поведением должны соответствовать требованиям соответствующего свойства. Максимально может быть указано 100 свойств. Ключ свойства может содержать до 100 символов. Значение свойства может содержать до 4096 символов. | Необязательный |
| startTime | integer | Время начала события в миллисекундах UTC. Если не задано, используется текущая временная метка. В зависимости от типа события, время начала не должно быть в прошлом более чем на 6 часов для событий, открывающих проблемы, и 30 дней для информационных событий. В зависимости от типа события, время начала не должно быть в будущем более чем на 5 минут для событий, открывающих проблемы, и 7 дней для информационных событий. События, которые можно отправлять на срок до 7 дней в будущее: * `CUSTOM_ANNOTATION` * `CUSTOM_CONFIGURATION` * `CUSTOM_DEPLOYMENT` * `CUSTOM_INFO` * `MARKED_FOR_TERMINATION` | Необязательный |
| timeout | integer | Таймаут события в минутах. Если не задано, используется 15. Таймаут автоматически ограничивается максимумом в 360 минут (6 часов). События, открывающие проблемы, можно обновлять и, следовательно, поддерживать открытыми, отправляя ту же полезную нагрузку повторно. | Необязательный |
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
| **201** | [EventIngestResults](#openapi-definition-EventIngestResults) | Запрос на загрузку события был получен сервером. Тело ответа указывает для каждого события, было ли его создание успешным. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `EventIngestResults`

Результаты загрузки событий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| eventIngestResults | [EventIngestResult[]](#openapi-definition-EventIngestResult) | Результат каждого созданного отчёта о событии. |
| reportCount | integer | Количество созданных отчётов о событиях. |

#### Объект `EventIngestResult`

Результат созданного отчёта о событии.

| Элемент | Тип | Описание |
| --- | --- | --- |
| correlationId | string | Идентификатор корреляции созданного события. |
| status | string | Статус загрузки. Элемент может содержать следующие значения: * `INVALID_ENTITY_TYPE` * `INVALID_METADATA` * `INVALID_TIMESTAMPS` * `OK` |

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
| parameterLocation | string | - Элемент может содержать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

Пример 1

Пример 2

Пример 3

Сценарий использования

Команда эксплуатации хочет отправить событие **Marked for termination** на все хосты, которые планируется удалить. Они также хотят включить причину удаления и идентификатор задачи. Хосты, подлежащие удалению, объединены в специальную группу хостов.

В этом примере запрос отправляет событие **Marked for termination** на хосты, которые планируется удалить. Такие хосты определяются по группе хостов **cloud-burst-hosts**. Событие автоматически применяется ко всем хостам, входящим в эту группу. Причина прекращения работы и номер задачи автоматизации предоставляются в качестве дополнительной информации.

Токен API передаётся в заголовке **Authorization**.

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

Команда DevOps хочет интегрировать свой инструмент нагрузочного тестирования с Dynatrace для аннотирования сервиса, который в данный момент проходит нагрузочное тестирование. Позже, когда Dynatrace обнаружит проблему, вызванную нагрузочным тестом, детали проблемы будут включать эту информацию, упрощая процесс сортировки.

В этом примере запрос отправляет событие **Custom info** на сервис **BookingService**, помечая его как цель нагрузочного теста.

Токен API передаётся в заголовке **Authorization**.

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

Команда эксплуатации крупного ритейлера хочет вызывать оповещение в Dynatrace всякий раз, когда пакетный процесс обновления каталога завершается с ошибкой. Они хотят создать событие и оповещение в Dynatrace, но не хотят, чтобы Dynatrace Intelligence объединял это внешне созданное событие с каким-либо более крупным инцидентом.

В этом примере запрос отправляет событие **Error** на сервис **BookingService**, указывая на неудачное обновление. Свойство **dt.event.allow\_davis\_merge** установлено в `false`, что предотвращает объединение этого события Dynatrace Intelligence с любым другим событием.

Токен API передаётся в заголовке **Authorization**.

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

* Event categories
* Event analysis and correlation
