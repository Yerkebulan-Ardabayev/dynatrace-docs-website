---
title: Миграция с Maintenance windows API на Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/maintenance-windows-to-settings
scraped: 2026-02-24T21:24:14.367536
---

# Миграция с Maintenance windows API на Settings API

# Миграция с Maintenance windows API на Settings API

* Ссылка
* Опубликовано 21 декабря 2022 г.

[Maintenance windows API](/docs/dynatrace-api/configuration-api/maintenance-windows-api "Узнайте, что предлагает конфигурация Dynatrace maintenance windows API.") был заменен на [Settings API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") с схемой **Maintenance windows** (`builtin:alerting.maintenance-window`) начиная с [Dynatrace версии 1.240](/docs/whats-new/dynatrace-api/sprint-240 "Журнал изменений для Dynatrace API версии 1.240"). Мы рекомендуем вам мигрировать на новую версию API как можно скорее.

Миграция затрагивает URL-адреса конечных точек, параметры запроса и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Базовый URL

| новый Settings 2.0 | старый Maintenance windows |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/maintenanceWindows` |

## Область действия токена аутентификации

| новый Settings 2.0 | старый Maintenance windows |
| --- | --- |
| **Чтение настроек** (`settings.read`) **Запись настроек** (`settings.write`) | **Чтение конфигурации** (`ReadConfig`) **Запись конфигурации** (`WriteConfig`) |

## Параметры

Чтобы узнать о новых параметрах запроса/тела, см. документацию отдельных запросов в [Settings API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.").

В рамках Settings 2.0 каждый окно обслуживания представлен объектом настроек. Объект содержит некоторые метаданные (например, область или метка времени создания) и саму конфигурацию, инкапсулированную в объекте **value**. Чтобы узнать о параметрах конфигурации окна обслуживания, запросите схему **Maintenance windows** (`builtin:alerting.maintenance-window`) с помощью запроса [GET схему](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр схемы настроек через Dynatrace API.").

## Примеры

Вот некоторые примеры различий в использовании API.

### Список окон обслуживания

Settings 2.0

Окна обслуживания

Чтобы просмотреть все окна обслуживания, вам необходим запрос [GET объекты](/docs/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких объектов настроек через Dynatrace API."). В параметрах запроса установите **schemaIds** в `builtin:alerting.maintenance-window` и **scope** в `environment`.

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:alerting.maintenance-window&scopes=environment
```

#### Тело ответа

```
{
"items": [
{
"objectId": "vu9U3hXa3q0AAAABACNidWlsdGluOmFsZXJ0aW5nLm1haW50ZW5hbmNlLXdpbmRvdwAGdGVuYW50AAZ0ZW5hbnQAJDgwMzdjNWM3LTdkNTgtNGQyYy04YzJkLWViMTYxMTBkZTE2Mr7vVN4V2t6t",
"value": {
"enabled": true,
"generalProperties": {
"name": "Масштабирование синтетического мониторинга",
"description": "Окно обслуживания для адаптации синтетических мониторов",
"maintenanceType": "ПЛАНОВОЕ",
"suppression": "ОБНАРУЖИТЬ_ПРОБЛЕМЫ_НО_НЕ_ОПОВЕЩАТЬ",
"disableSyntheticMonitorExecution": false
},
"schedule": {
"scheduleType": "ОДНОРАЗОВО",
"onceRecurrence": {
"startTime": "2022-12-22T09:00:00",
"endTime": "2022-12-22T12:00:00",
"timeZone": "UTC"
}
},
"filters": [
{
"entityType": "ХОСТ",
"entityTags": [
"[AWS]Использование:Синтетический"
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
"name": "Проблема с предпроизводственной средой",
"maintenanceType": "НЕПЛАНОВОЕ",
"suppression": "НЕ_ОБНАРУЖИТЬ_ПРОБЛЕМЫ",
"disableSyntheticMonitorExecution": false
},
"schedule": {
"scheduleType": "ОДНОРАЗОВО",
"onceRecurrence": {
"startTime": "2022-12-10T10:00:00",
"endTime": "2022-12-10T14:00:00",
"timeZone": "Europe/Vienna"
}
},
"filters": [
{
"entityType": "СЕРВИС",
"entityTags": [
"Env-pre-prod"
],
"managementZones": []
},
{
"entityType": "ГРУППА_ПРОЦЕССОВ",
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
"pageSize": 100
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
"name": "Масштабирование синтетического мониторинга",
"description": "Окно обслуживания для адаптации синтетических мониторов"
},
{
"id": "01ba0f45-7abe-46a3-94b9-ce377f684973",
"name": "Проблема с предпроизводственной средой"
}
]
}
```

### Создание окна обслуживания

Settings 2.0

Окна обслуживания

Чтобы создать окно обслуживания, вам необходим запрос [POST объект](/docs/dynatrace-api/environment-api/settings/objects/post-object "Создание или проверка объекта настроек через Dynatrace API."). В теле запроса установите **schemaId** в `builtin:alerting.maintenance-window` и **scope** в `environment`. Предоставьте конфигурацию окна обслуживания в объекте **value**.

Ответ содержит идентификатор объекта, который вам необходимо изменить настройки.

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
"name": "Пример окна обслуживания",
"maintenanceType": "ПЛАНОВОЕ",
"suppression": "ОБНАРУЖИТЬ_ПРОБЛЕМЫ_И_ОПОВЕЩАТЬ",
"disableSyntheticMonitorExecution": false
},
"schedule": {
"scheduleType": "ЕЖЕМЕСЯЧНО",
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
"entityType": "СЕРВИС",
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

Ответ содержит идентификатор конфигурации, который вам необходимо изменить настройки.

#### Тело запроса

```
{
"name": "Пример окна обслуживания",
"description": "",
"type": "ПЛАНОВОЕ",
"enabled": true,
"suppression": "ОБНАРУЖИТЬ_ПРОБЛЕМЫ_И_ОПОВЕЩАТЬ",
"suppressSyntheticMonitorsExecution": false,
"scope": {
"entities": [],
"matches": [
{
"type": "СЕРВИС",
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
"recurrenceType": "ЕЖЕМЕСЯЧНО",
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
"name": "Пример окна обслуживания"
}
```

### Редактирование окна обслуживания

Настройки 2.0

Окна обслуживания

Чтобы редактировать окно обслуживания, вам необходимо выполнить запрос [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Редактировать объект настроек через Dynatrace API.") .

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



"name": "Пример окна обслуживания",



"maintenanceType": "PLANNED",



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"disableSyntheticMonitorExecution": false



},



"schedule": {



"scheduleType": "MONTHLY",



"monthlyRecurrence": {



"dayOfMonth": 5,



"timeWindow":).



"startTime": "01:00:00",



"endTime": "01:30:00",



"timeZone": "Europe/Vienna"



},



"recurrenceRange":.



"scheduleStartDate": "2022-01-01",



"scheduleEndDate": "2022-12-31"



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



"name": "Пример MW - старое",



"description": "",



"type": "PLANNED",



"enabled": true,



"suppression": "DETECT_PROBLEMS_AND_ALERT",



"suppressSyntheticMonitorsExecution": false,



"scope":.



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



]



],



"tagCombination": "AND"



]



],



"schedule":.



"recurrenceType": "MONTHLY",



"recurrence":.



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

* [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.") 
* [Окна обслуживания API](/docs/dynatrace-api/configuration-api/maintenance-windows-api "Узнайте, что предлагает Dynatrace конфигурация окон обслуживания API.")