---
title: Миграция с Events API v1 на Events API v2
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/events-v1-to-v2
scraped: 2026-03-06T21:31:20.594704
---

# Миграция с Events API v1 на Events API v2

# Миграция с Events API v1 на Events API v2

* Справочник
* Опубликовано 25 ноября 2022 г.

[Events API v1](../../environment-api/events-v1.md "Узнайте, что можно делать с помощью Dynatrace Events API.") был объявлен устаревшим в [Dynatrace версии 1.243](../../../whats-new/dynatrace-api/sprint-243.md "Журнал изменений Dynatrace API версии 1.243"). Его заменой является [Events API v2](../../environment-api/events-v2.md "Узнайте, что можно делать с помощью Dynatrace Events API v2."). Мы рекомендуем перейти на новый API при первой возможности.

Миграция затрагивает URL конечных точек, параметры запросов, параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Новые возможности

Events API v2 предлагает следующие новые возможности:

* [Селектор сущностей](../../environment-api/entity-v2/entity-selector.md "Настройте селектор сущностей для конечных точек Environment API.") помогает фильтровать события в запросах на чтение и принимать события, затрагивающие несколько сущностей.
* Улучшенная фильтрация событий через селектор событий.
* Унифицированный селектор временного диапазона.
* Конечные точки для свойств событий.
* Конечные точки для типов событий.

## Лицензирование

[Приём](../../environment-api/events-v2/post-event.md "Приём события через API Dynatrace.") пользовательских событий потребляет [единицы данных Davis (DDU)](../../../license/monitoring-consumption-classic/davis-data-units.md "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU).") из пула событий.

## Базовый URL

| новый Events v2 | старый Events v1 |
| --- | --- |
| `/api/v2/events` | `/api/v1/events` |

## Область действия токена аутентификации

| новый Events v2 | старый Events v1 |
| --- | --- |
| **Read events** (`events.read`) **Ingest events** (`events.ingest`) | **Access problem and event feed, metrics, and topology** (`DataExport`) |

## Параметры

Чтобы узнать о новых параметрах запросов/тела, см. документацию отдельных запросов в [Events API v2](../../environment-api/events-v2.md "Узнайте, что можно делать с помощью Dynatrace Events API v2.").

## Примеры

Вот несколько примеров различий в использовании API.

### Получение списка событий за временной период

В этом примере мы запрашиваем список открытых событий доступности на хостах, произошедших за последние два часа.

Events v2

Events v1

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/events?eventSelector=eventType("AVAILABILITY_EVENT"),status("OPEN")&from=now-2h&entitySelector=type("HOST")
```

#### Тело ответа

```
{



"totalCount": 28,



"pageSize": 2,



"nextPageKey": "AQANMTY2OTY0NDE2NjAwOQEADTE2Njk2NTEzNjYwMDkBADtTdHJpbmcoVDFCRlRnPT0pLUxvbmcoMTg0YmVlMjU1NjkpLUxvbmcoYTdjZjQ2NjZlNjIwZjMyMSktMgEAAAACAQAuZXZlbnRUeXBlKCJBVkFJTEFCSUxJVFlfRVZFTlQiKSxzdGF0dXMoIk9QRU4iKQEADHR5cGUoIkhPU1QiKQA=",



"events": [



{



"eventId": "-9195326388738983252_1669651221408",



"startTime": 1669651221408,



"endTime": -1,



"eventType": "AVAILABILITY_EVENT",



"title": "No process found for rule Oracle listener",



"entityId": {



"entityId": {



"id": "HOST-E371A974A078CC54",



"type": "HOST"



},



"name": "frontend-dev"



},



"properties": [



{



"key": "Event source",



"value": "Process availability"



},



{



"key": "Message",



"value": "Missing process matching rule named Oracle listener"



},



{



"key": "custom.message-process-av",



"value": "The {dt.event.title} is on deployment version: {dt.event.deployment.version}"



},



{



"key": "dt.event.group_label",



"value": "Availability event"



},



{



"key": "dt.event.impact_level",



"value": "Infrastructure"



},



{



"key": "dt.event.is_rootcause_relevant",



"value": "true"



},



{



"key": "dt.event.timeout",



"value": "4"



},



{



"key": "dt.event.title",



"value": "No process found for rule Oracle listener"



}



],



"status": "OPEN",



"correlationId": "458a73c38677f1ac",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "frontend",



"stringRepresentation": "frontend"



},



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev",



"stringRepresentation": "stage:dev"



}



],



"managementZones": [



{



"id": "6143976176513989654",



"name": "Infrastructure Linux"



},



{



"id": "4067143719293196613",



"name": "dev"



},



{



"id": "-6114370715062110014",



"name": "frontent"



}



],



"underMaintenance": false,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



},



{



"eventId": "-6354783141434952927_1669649814889",



"startTime": 1669649814889,



"endTime": -1,



"eventType": "AVAILABILITY_EVENT",



"title": "Host unavailable",



"entityId": {



"entityId": {



"id": "HOST-FD01FA52FB10B433",



"type": "HOST"



},



"name": "GDNVTUBU2004-1"



},



"properties": [



{



"key": "dt.event.group_label",



"value": "Availability event"



},



{



"key": "dt.event.impact_level",



"value": "Infrastructure"



},



{



"key": "dt.event.is_rootcause_relevant",



"value": "true"



},



{



"key": "dt.event.timeout",



"value": "5"



},



{



"key": "dt.event.title",



"value": "Host unavailable"



}



],



"status": "OPEN",



"correlationId": "360ad37a6f4de7d0",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux",



"stringRepresentation": "OS:Linux"



}



],



"managementZones": [



{



"id": "6143976176513989654",



"name": "Linux"



},



{



"id": "4067143719293196613",



"name": "dev"



}



],



"underMaintenance": false,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



}



],



"warnings": []



}
```

В Events API v1 невозможно фильтровать ленту событий по статусу события. Также невозможно выбирать несколько сущностей через селектор сущностей. Можно указать только конкретные сущности. Для наглядности в примере показаны те же события, но вам пришлось бы находить их в ответе внешними средствами.

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v1/events?relativeTime=2hours?eventType=AVAILABILITY_EVENT
```

#### Тело ответа

```
{



"nextEventStartTms": 1669639936928,



"nextEventId": -3132566662524695739,



"nextCursor": "AgEAAAGEvd8xRAEAAAGEvk0ORAAAAQA8U3RyaW5nKFQxQkZUZz09KS1Mb25nKDE4NGJlNGI5YmEwKS1Mb25nKGQ0ODZlMzM3YWNmYzBiNDUpLTk2",



"from": 1669632831812,



"to": 1669640031812,



"totalEventCount": 25703,



"events": [



{



"eventId": -9195326388738983252,



"startTime": 1669651221408,



"endTime": 1669658492185,



"entityId": "HOST-E371A974A078CC54",



"entityName": "frontend-dev",



"severityLevel": "AVAILABILITY",



"impactLevel": "INFRASTRUCTURE",



"eventType": "AVAILABILITY_EVENT",



"eventStatus": "OPEN",



"tags": [



{



"context": "CONTEXTLESS",



"key": "frontend"



},



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "dev"



}



],



"id": "-9195326388738983252_1669651221408",



"customProperties": {



"custom.message-process-av": "The {dt.event.title} is on deployment version: {dt.event.deployment.version}",



"Event source": "Process availability",



"Message": "Missing process matching rule named Oracle listener"



},



"correlationId": "458a73c38677f1ac",



"source": "builtin"



},



{



"eventId": -6354783141434952927,



"startTime": 1669649814889,



"endTime": 1669652093491,



"entityId": "HOST-FD01FA52FB10B433",



"entityName": "GDNVTUBU2004-1",



"severityLevel": "AVAILABILITY",



"impactLevel": "INFRASTRUCTURE",



"eventType": "AVAILABILITY_EVENT",



"eventStatus": "OPEN",



"tags": [



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux"



}



],



"id": "-6354783141434952927_1669649814889",



"correlationId": "360ad37a6f4de7d0",



"source": "builtin"



}



]



}
```

### Приём стороннего события

В этом примере мы принимаем пользовательское информационное событие, затрагивающее все хосты, имя которых начинается с `prod`.

Events v2

Events v1

#### URL запроса

```
POST https://mySampleEnv.live.dynatrace.com/api/v2/events
```

#### Тело запроса

```
{



"eventType": "AVAILABILITY_EVENT",



"title": "Critical service outage",



"timeout": 30,



"entitySelector": "type(HOST),entityName.startsWith(prod)",



"allowDavisMerge": false,



"properties": {



"custom property 1": "my property value 1",



"custom property 2": "my property value 2"



}



}
```

В Events API v1 невозможно выбирать несколько сущностей через селектор сущностей. Необходимо указывать каждую сущность отдельно или использовать теги.

#### URL запроса

```
POST https://mySampleEnv.live.dynatrace.com/api/v1/events
```

#### Тело запроса

```
{



"eventType": "AVAILABILITY_EVENT",



"title": "Critical service outage",



"description": "REST example",



"timeoutMinutes": 30,



"attachRules": {



"tagRule": [



{



"meTypes": [



"HOST"



],



"tags": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "production"



}



]



}



]



},



"source": "REST API"



}
```

## Связанные темы

* [Events API v2](../../environment-api/events-v2.md "Узнайте, что можно делать с помощью Dynatrace Events API v2.")
* [Events API v1](../../environment-api/events-v1.md "Узнайте, что можно делать с помощью Dynatrace Events API.")