---
title: Мигрировать из Events API v1 в Events API v2
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/events-v1-to-v2
scraped: 2026-02-23T21:35:33.610251
---

# Мигрировать из Events API v1 в Events API v2

# Мигрировать из Events API v1 в Events API v2

* Справка
* Опубликовано 25 нояб. 2022 г.

[Events API v1](/docs/dynatrace-api/environment-api/events-v1 "Узнайте, что можно сделать с помощью Dynatrace Events API.") был заменен [Dynatrace версией 1.243](/docs/whats-new/dynatrace-api/sprint-243 "Журнал изменений для Dynatrace API версии 1.243"). Его заменой является [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Узнайте, что можно сделать с помощью Dynatrace Events API v2."). Мы рекомендуем вам перейти на новую API как можно скорее.

Миграция затрагивает URL-адреса конечных точек, параметры запроса и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Новые функции

Events API v2 предлагает вам следующие новые функции:

* [Селектор сущностей](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Настройте селектор сущностей для Environment API конечных точек.") помогает вам фильтровать события в запросах на чтение и передавать события, которые влияют на несколько сущностей.
* Улучшенная фильтрация событий через селектор событий.
* Унифицированный селектор временного интервала.
* Конечные точки свойств событий.
* Конечные точки типов событий.

## Лицензирование

[Передача](/docs/dynatrace-api/environment-api/events-v2/post-event "Передает событие через Dynatrace API.") пользовательских событий потребляет [Единицы данных Davis (DDU)](/docs/license/monitoring-consumption-classic/davis-data-units "Поймите, как потребление мониторинга Dynatrace рассчитывается на основе единиц данных Davis (DDU).") из пула событий.

## Базовый URL

| новое Events v2 | старое Events v1 |
| --- | --- |
| `/api/v2/events` | `/api/v1/events` |

## Область действия токена аутентификации

| новое Events v2 | старое Events v1 |
| --- | --- |
| **Чтение событий** (`events.read`) **Передача событий** (`events.ingest`) | **Доступ к ленте проблем и событий, метрикам и топологии** (`DataExport`) |

## Параметры

Чтобы узнать о новых параметрах запроса/тела, см. документацию отдельных запросов в [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Узнайте, что можно сделать с помощью Dynatrace Events API v2.").

## Примеры

Вот некоторые примеры различий в использовании API.

### Список событий в временном интервале

В этом примере мы запрашиваем список открытых событий доступности на хостах, которые произошли в течение последних двух часов.

Events v2

Events v1

#### URL-адрес запроса

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



"entityId":).



"entityId":,



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



)



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



)



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



)



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



"entityId":,



"entityId":,



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



)



],



"status": "OPEN",



"correlationId": "360ad37a6f4de7d0",



"entityTags": [



{



"context": "CONTEXTLESS",



"key": "OS",



"value": "Linux",



"stringRepresentation": "OS:Linux"



)



],



"managementZones": [



{



"id": "6143976176513989654",



"name": "Linux"



},



{



"id": "4067143719293196613",



"name": "dev"



)



],



"underMaintenance": false,



"suppressAlert": false,



"suppressProblem": false,



"frequentEvent": false



)



],



"warnings": []



}
```

В Events API v1 невозможно фильтровать ленту событий по статусу события. Кроме того, невозможно выбрать несколько сущностей через селектор сущностей. Вы можете указать только конкретные сущности. Для иллюстрации примера полезная нагрузка показывает одни и те же события, но вам придется найти их в полезной нагрузке с помощью внешних средств.

#### URL-адрес запроса

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



)



],



"id": "-9195326388738983252_1669651221408",



"customProperties":,



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



)



],



"id": "-6354783141434952927_1669649814889",



"correlationId": "360ad37a6f4de7d0",



"source": "builtin"



)



]



}
```

### Передача события третьей стороны

В этом примере мы передаем пользовательское событие информационного типа, которое влияет на все хосты, имя которых начинается с `prod`.

Events v2

Events v1

#### URL-адрес запроса

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



"properties":,



"custom property 1": "my property value 1",



"custom property 2": "my property value 2"



}
```

В Events API v1 невозможно выбрать несколько сущностей через селектор сущностей. Вам необходимо указать каждую сущность или полагаться на теги.

#### URL-адрес запроса

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



"attachRules":,



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



)



]



]



},



"source": "REST API"



}
```

## Связанные темы

* [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Узнайте, что можно сделать с помощью Dynatrace Events API v2.")
* [Events API v1](/docs/dynatrace-api/environment-api/events-v1 "Узнайте, что можно сделать с помощью Dynatrace Events API.")