---
title: Миграция с Problems API v1 на Problems API v2
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/problems-v1-to-v2
scraped: 2026-03-06T21:38:12.631540
---

# Миграция с Problems API v1 на Problems API v2


* Справочник
* Опубликовано 30 ноября 2022 г.

[Problems API v1](../../environment-api/problems.md "Узнайте, что предлагает Dynatrace Problems v1 API.") был объявлен устаревшим в [версии Dynatrace 1.243](../../../whats-new/dynatrace-api/sprint-243.md "Список изменений для версии Dynatrace API 1.243"). Его заменой является [Problems API v2](../../environment-api/problems-v2.md "Узнайте, что предлагает Dynatrace Problems v2 API."). Мы рекомендуем выполнить миграцию на новый API при первой возможности.

Миграция затрагивает URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Новые возможности

Events API v2 предлагает следующие новые возможности:

* [Селектор сущностей](../../environment-api/entity-v2/entity-selector.md "Настройте селектор сущностей для конечных точек Environment API.") помогает фильтровать проблемы в запросах на чтение.
* Улучшенная фильтрация проблем с помощью селектора проблем.
* Унифицированный селектор временного интервала.

## Базовый URL

| новый Problems v2 | старый Problems v1 |
| --- | --- |
| `/api/v2/problems` | `/api/v1/problem` |

## Область действия токена аутентификации

| новый Problems v2 | старый Problems v1 |
| --- | --- |
| **Read problems** (`problems.read`) **Write problems** (`problems.write`) | **Access problem and event feed, metrics, and topology** (`DataExport`) |

## Параметры

Подробнее о новых параметрах запросов/тела см. документацию отдельных запросов в [Problems API v2](../../environment-api/problems-v2.md "Узнайте, что предлагает Dynatrace Problems v2 API.").

## Пример

В этом примере мы запрашиваем список открытых проблем на хостах, возникших за последние два часа.

Problems v2

Problems v1

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/problems?from=now-2h&problemSelector=status("open")&entitySelector=type("HOST")
```

#### Тело ответа

```
{


"totalCount": 2,


"pageSize": 50,


"problems": [


{


"problemId": "-6156404735398726308_1669823466223V2",


"displayId": "P-221194163",


"title": "Host or monitoring unavailable",


"impactLevel": "INFRASTRUCTURE",


"severityLevel": "AVAILABILITY",


"status": "OPEN",


"affectedEntities": [


{


"entityId": {


"id": "HOST-E371A974A078CC54",


"type": "HOST"


},


"name": "frontend-dev"


}


],


"impactedEntities": [


{


"entityId": {


"id": "HOST-E371A974A078CC54",


"type": "HOST"


},


"name": "frontend-dev"


}


],


"rootCauseEntity": null,


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


"problemFilters": [


{


"id": "ca786d1f-e6cf-4451-b9dc-9c27c5c339e1",


"name": "Infrastructure alerts"


},


{


"id": "d03022be-d0e3-4089-b02d-ebec9ae87da4",


"name": "Frontend alerts"


}


],


"startTime": 1669823466223,


"endTime": -1


},


{


"problemId": "7188776519218424524_1669820820000V2",


"displayId": "P-221194115",


"title": "High memory usage",


"impactLevel": "INFRASTRUCTURE",


"severityLevel": "CUSTOM_ALERT",


"status": "OPEN",


"affectedEntities": [


{


"entityId": {


"id": "HOST-0F5789A6850FA907",


"type": "HOST"


},


"name": "easyTravel.bookingService.Win.1"


}


],


"impactedEntities": [


{


"entityId": {


"id": "HOST-0F5789A6850FA907",


"type": "HOST"


},


"name": "easyTravel.bookingService.Win.dev.1"


}


],


"rootCauseEntity": null,


"managementZones": [


{


"id": "4067143719293196613",


"name": "dev"


},


{


"id": "7918335421727549830",


"name": "Infrastructure windows"


},


{


"id": "-6239538939987181652",


"name": "Booking service"


}


],


"entityTags": [


{


"context": "CONTEXTLESS",


"key": "stage",


"value": "dev",


"stringRepresentation": "stage:dev"


},


{


"context": "CONTEXTLESS",


"key": "bookingService",


"stringRepresentation": "bookingService"


}


],


"problemFilters": [


{


"id": "ca786d1f-e6cf-4451-b9dc-9c27c5c339e1",


"name": "Infrastructure alerts"


},


{


"id": "ff956dac-8709-3546-bf2b-d82195e7ef6a",


"name": "Booking service alerts"


}


],


"startTime": 1669821000000,


"endTime": -1


}


],


"warnings": []


}
```

В Events API v1 невозможно выбрать несколько сущностей с помощью селектора сущностей. Приходится полагаться на теги. В иллюстративных целях пример полезной нагрузки показывает те же проблемы, но для их нахождения в полезной нагрузке вам потребуются внешние средства.

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v1/problem/feed?relativeTime=2hours&status=OPEN&tag=stage:dev
```

#### Тело ответа

```
{


"result": {


"problems": [


{


"id": "-6156404735398726308_1669823466223V2",


"startTime": 1669823466223,


"endTime": -1,


"displayName": "P-221194163",


"impactLevel": "INFRASTRUCTURE",


"status": "OPEN",


"severityLevel": "AVAILABILITY",


"commentCount": 0,


"tagsOfAffectedEntities": [


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


"rankedImpacts": [


{


"entityId": "HOST-E371A974A078CC54",


"entityName": "frontend-dev",


"severityLevel": "AVAILABILITY",


"impactLevel": "INFRASTRUCTURE",


"eventType": "CONNECTION_LOST"


}


],


"affectedCounts": {


"INFRASTRUCTURE": 1,


"SERVICE": 0,


"APPLICATION": 0,


"ENVIRONMENT": 0


},


"recoveredCounts": {


"INFRASTRUCTURE": 0,


"SERVICE": 0,


"APPLICATION": 0,


"ENVIRONMENT": 0


},


"hasRootCause": false


},


{


"id": "7188776519218424524_1669820820000V2",


"startTime": 1669821000000,


"endTime": -1,


"displayName": "P-221194115",


"impactLevel": "INFRASTRUCTURE",


"status": "OPEN",


"severityLevel": "CUSTOM_ALERT",


"commentCount": 0,


"tagsOfAffectedEntities": [


{


"context": "CONTEXTLESS",


"key": "stage",


"value": "dev"


},


{


"context": "CONTEXTLESS",


"key": "bookingService"


}


],


"rankedImpacts": [


{


"entityId": "HOST-0F5789A6850FA907",


"entityName": "easyTravel.bookingService.Win.1",


"severityLevel": "CUSTOM_ALERT",


"impactLevel": "INFRASTRUCTURE",


"eventType": "CUSTOM_ALERT"


}


],


"affectedCounts": {


"INFRASTRUCTURE": 1,


"SERVICE": 0,


"APPLICATION": 0,


"ENVIRONMENT": 0


},


"recoveredCounts": {


"INFRASTRUCTURE": 0,


"SERVICE": 0,


"APPLICATION": 0,


"ENVIRONMENT": 0


},


"hasRootCause": false


}


]


}


}
```

## Связанные темы

* [Problems API v2](../../environment-api/problems-v2.md "Узнайте, что предлагает Dynatrace Problems v2 API.")
* [Problems API v1](../../environment-api/problems.md "Узнайте, что предлагает Dynatrace Problems v1 API.")
