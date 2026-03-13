---
title: Migrate from Maintenance windows API to Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/maintenance-windows-to-settings
scraped: 2026-03-03T21:32:05.233768
---

# Миграция с API окон обслуживания на Settings API

# Миграция с API окон обслуживания на Settings API

* Справочник
* Опубликовано 21 декабря 2022

[API окон обслуживания](../../configuration-api/maintenance-windows-api.md "Узнайте, что предлагает API конфигурации окон обслуживания Dynatrace.") был объявлен устаревшим в [Dynatrace версии 1.240](../../../whats-new/dynatrace-api/sprint-240.md "Журнал изменений Dynatrace API версии 1.240"). Его заменой является [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.") со схемой **Maintenance windows** (`builtin:alerting.maintenance-window`). Мы рекомендуем выполнить миграцию на новый API при первой возможности.

Миграция затрагивает URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Базовый URL

| новый Settings 2.0 | старый Maintenance windows |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/maintenanceWindows` |

## Область действия токена аутентификации

| новый Settings 2.0 | старый Maintenance windows |
| --- | --- |
| **Read settings** (`settings.read`) **Write settings** (`settings.write`) | **Read configuration** (`ReadConfig`) **Write configuration** (`WriteConfig`) |

## Параметры

Чтобы узнать о новых параметрах запроса/тела, смотрите документацию отдельных запросов в [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.").

В фреймворке Settings 2.0 каждое окно обслуживания представлено объектом настроек. Объект содержит некоторые метаданные (такие как область действия или временная метка создания) и саму конфигурацию, инкапсулированную в объекте **value**. Чтобы узнать о параметрах конфигурации окна обслуживания, запросите схему **Maintenance windows** (`builtin:alerting.maintenance-window`) с помощью запроса [GET a schema](../../environment-api/settings/schemas/get-schema.md "Просмотр схемы настроек через Dynatrace API.").

## Примеры

Вот несколько примеров различий в использовании API.

### Список окон обслуживания

Settings 2.0

Maintenance windows

Чтобы получить список всех окон обслуживания, используйте запрос [GET objects](../../environment-api/settings/objects/get-objects.md "Просмотр нескольких объектов настроек через Dynatrace API."). В параметрах запроса установите **schemaIds** в `builtin:alerting.maintenance-window` и **scope** в `environment`.

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:alerting.maintenance-window&scopes=environment
```

#### Тело ответа

```
{



"items": [



{



"objectId":



"vu9U3hXa3q0AAAABACNidWlsdGluOmFsZXJ0aW5nLm1haW50ZW5hbmNlLXdpbmRvdwAGdGVuYW50AAZ0ZW5hbnQAJDgwMzdjNWM3LTdkNTgtNGQyYy04YzJkLWViMTYxMTBkZTE2Mr7vVN4V2t6t",



"value": {



"enabled": true,



"generalProperties": {



"name": "Synthetic scaling",



"description": "Maintenance window for adaptations of Synthetic monitors",



"maintenanceType": "PLANNED",



"suppression": "DETECT_PROBLEMS_DONT_ALERT",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "ONCE",



"onceRecurrence": {



"startTime": "2022-12-22T09:00:00",



"endTime": "2022-12-22T12:00:00",



"timeZone": "UTC"



}



},



"filters": [



{



"entityType": "HOST",



"entityTags": [



"[AWS]Usage:Synthetic"



],



"managementZones": []



}



]



}



},



{



"objectId": "vu9U3hXa3q0AAAABACNidWlsdGluOmFsZXJ0aW5nLm1haW50ZW5hbmNlLXdpbmRvdwAGdGVuYW50AAZ0ZW5hbnQAJDE3NDgxMWYxLWQ2NjYtNGJhNy1iZmU3LTk5ZGYzMjIyNjY3Mr7vVN4V2t6t",



"value": {



"enabled": true,



"generalProperties": {



"name": "Issue with pre-production environment",



"maintenanceType": "UNPLANNED",



"suppression": "DONT_DETECT_PROBLEMS",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "ONCE",



"onceRecurrence": {



"startTime": "2022-12-10T10:00:00",



"endTime": "2022-12-10T14:00:00",



"timeZone": "Europe/Vienna"



}



},



"filters": [



{



"entityType": "SERVICE",



"entityTags": [



"Env-pre-prod"



],



"managementZones": []



},



{



"entityType": "PROCESS_GROUP",



"entityTags": [



"Env-pre-prod"



],



"managementZones": []



}



]



}



}



],



"totalCount": 2,



"pageSize": 100,



}
```

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows
```

#### Тело ответа

```
{



"values": [



{



"id": "00564256-a294-4ed5-9de6-ecba61500ed2",



"name": "Synthetic scaling",



"description": "Maintenance window for adaptations of Synthetic monitors"



},



{



"id": "01ba0f45-7abe-46a3-94b9-ce377f684973",



"name": "Issue with pre-production environment"



}



]



}
```

### Создание окна обслуживания

Settings 2.0

Maintenance windows

Чтобы создать окно обслуживания, используйте запрос [POST an object](../../environment-api/settings/objects/post-object.md "Создание или валидация объекта настроек через Dynatrace API."). В теле запроса установите **schemaId** в `builtin:alerting.maintenance-window` и **scope** в `environment`. Предоставьте конфигурацию окна обслуживания в объекте **value**.

Ответ содержит идентификатор объекта, который необходим для изменения настроек.

#### URL запроса

```
POST https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects
```

#### Тело запроса

```
[



{



"schemaId": "builtin:alerting.maintenance-window",



"scope": "environment",



"value": {



"enabled": true,



"generalProperties": {



"name": "Sample maintenance window",



"maintenanceType": "PLANNED",



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "MONTHLY",



"monthlyRecurrence": {



"dayOfMonth": 1,



"timeWindow": {



"startTime": "06:00:00",



"endTime": "06:30:00",



"timeZone": "Europe/Vienna"



},



"recurrenceRange": {



"scheduleStartDate": "2022-01-01",



"scheduleEndDate": "2022-12-31"



}



}



},



"filters": [



{



"entityType": "SERVICE",



"entityTags": [



"stage:pre-production"



],



"managementZones": []



}



]



}



}



]
```

#### Тело ответа

```
[



{



"code": 200,



"objectId": "vu9U3hXa3q0AAAABACNidWlsdGluOmFsZXJ0aW5nLm1haW50ZW5hbmNlLXdpbmRvdwAGdGVuYW50AAZ0ZW5hbnQAJDVhMjg2NmE5LTJjZjQtMzIwZC1hNjMxLTI0NTAwYTQ4NmU5Zr7vVN4V2t6t"



}



]
```

#### URL запроса

```
POST https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows
```

Ответ содержит идентификатор конфигурации, который необходим для изменения настроек.

#### Тело запроса

```
{



"name": "Sample maintenance window",



"description": "",



"type": "PLANNED",



"enabled": true,



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"suppressSyntheticMonitorsExecution": false,



"scope": {



"entities": [],



"matches": [



{



"type": "SERVICE",



"tags": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "pre-production"



}



],



"tagCombination": "AND"



}



]



},



"schedule": {



"recurrenceType": "MONTHLY",



"recurrence": {



"dayOfMonth": 1,



"startTime": "06:00",



"durationMinutes": 30



},



"start": "2022-01-01 00:00",



"end": "2022-12-31 23:59",



"zoneId": "Europe/Vienna"



}



}
```

#### Тело ответа

```
{



"id": "07f476c6-f1ed-4519-848d-61e52f7e2f24",



"name": "Sample maintenance window"



}
```

### Редактирование окна обслуживания

Settings 2.0

Maintenance windows

Чтобы отредактировать окно обслуживания, используйте запрос [PUT an object](../../environment-api/settings/objects/put-object.md "Редактирование объекта настроек через Dynatrace API.").

#### URL запроса

```
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ
```

#### Тело запроса

```
{



"schemaId": "builtin:alerting.maintenance-window",



"scope": "environment",



"value": {



"enabled": true,



"generalProperties": {



"name": "Sample maintenance window",



"maintenanceType": "PLANNED",



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "MONTHLY",



"monthlyRecurrence": {



"dayOfMonth": 5,



"timeWindow": {



"startTime": "01:00:00",



"endTime": "01:30:00",



"timeZone": "Europe/Vienna"



},



"recurrenceRange": {



"scheduleStartDate": "2022-01-01",



"scheduleEndDate": "2022-12-31"



}



}



},



"filters": [



{



"entityType": "SERVICE",



"entityTags": [



"stage:pre-production"



],



"managementZones": [



"5561909168316319665"



]



}



]



}



}
```

#### Тело ответа

```
[



{



"code": 200,



"objectId": "vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ"



}



]
```

#### URL запроса

```
PUT https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows/07f476c6-f1ed-4519-848d-61e52f7e2f24
```

#### Тело запроса

```
{



"id": "07f476c6-f1ed-4519-848d-61e52f7e2f24",



"name": "Sample MW - old",



"description": "",



"type": "PLANNED",



"enabled": true,



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"suppressSyntheticMonitorsExecution": false,



"scope": {



"entities": [],



"matches": [



{



"mzId": "5561909168316319665",



"type": "SERVICE",



"tags": [



{



"context": "CONTEXTLESS",



"key": "stage",



"value": "pre-production"



}



],



"tagCombination": "AND"



}



]



},



"schedule": {



"recurrenceType": "MONTHLY",



"recurrence": {



"dayOfMonth": 5,



"startTime": "01:00",



"durationMinutes": 30



},



"start": "2022-01-01 00:00",



"end": "2022-12-31 23:59",



"zoneId": "Europe/Vienna"



}



}
```

## Связанные темы

* [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.")
* [API окон обслуживания](../../configuration-api/maintenance-windows-api.md "Узнайте, что предлагает API конфигурации окон обслуживания Dynatrace.")