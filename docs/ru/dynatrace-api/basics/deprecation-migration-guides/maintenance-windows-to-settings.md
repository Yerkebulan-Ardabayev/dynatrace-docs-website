---
title: Миграция с Maintenance windows API на Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/maintenance-windows-to-settings
scraped: 2026-02-20T21:12:40.495628
---

# Миграция с Maintenance windows API на Settings API

# Миграция с Maintenance windows API на Settings API

* Ссылка
* Опубликовано 21 декабря 2022 г.

[Maintenance windows API](/docs/dynatrace-api/configuration-api/maintenance-windows-api "Узнайте, что предлагает конфигурация Dynatrace maintenance windows API.") был заменен на [Settings API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") с схемой **Maintenance windows** (`builtin:alerting.maintenance-window`) в версии [Dynatrace 1.240](/docs/whats-new/dynatrace-api/sprint-240 "Журнал изменений для Dynatrace API версии 1.240"). Мы рекомендуем вам мигрировать на новую версию API как можно скорее.

Миграция затрагивает URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

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

В рамках Settings 2.0 каждое окно обслуживания представлено объектом настроек. Объект содержит некоторые метаданные (например, область или метка времени создания) и саму конфигурацию, инкапсулированную в объект **value**. Чтобы узнать о параметрах конфигурации окна обслуживания, запросите схему **Maintenance windows** (`builtin:alerting.maintenance-window`) с помощью запроса [GET-схемы](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр схемы настроек через Dynatrace API.").

## Примеры

Вот некоторые примеры различий в использовании API.

### Список окон обслуживания

Settings 2.0

Окна обслуживания

Чтобы просмотреть все окна обслуживания, вам необходим запрос [GET-объектов](/docs/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких объектов настроек через Dynatrace API."). В параметрах запроса установите **schemaIds** в `builtin:alerting.maintenance-window` и **scope** в `environment`.

#### URL-запроса

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
"name": "Масштабирование синтетики",
"description": "Окно обслуживания для адаптации синтетических мониторов",
"maintenanceType": "Плановое",
"suppression": "Обнаруживать проблемы, не отправлять уведомления",
"disableSyntheticMonitorExecution": false
},
"schedule": {
"scheduleType": "Одноразовое",
"onceRecurrence": {
"startTime": "2022-12-22T09:00:00",
"endTime": "2022-12-22T12:00:00",
"timeZone": "UTC"
}
},
"filters": [
{
"entityType": "Хост",
"entityTags": [
"[AWS]Использование:Синтетика"
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
"maintenanceType": "Неплановое",
"suppression": "Не обнаруживать проблемы",
"disableSyntheticMonitorExecution": false
},
"schedule": {
"scheduleType": "Одноразовое",
"onceRecurrence": {
"startTime": "2022-12-10T10:00:00",
"endTime": "2022-12-10T14:00:00",
"timeZone": "Europe/Vienna"
}
},
"filters": [
{
"entityType": "Сервис",
"entityTags": [
"Среда-предпроизводство"
],
"managementZones": []
},
{
"entityType": "Группа процессов",
"entityTags": [
"Среда-предпроизводство"
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

#### URL-запроса

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows
```

#### Тело ответа

```
{
"values": [
{
"id": "00564256-a294-4ed5-9de6-ecba61500ed2",
"name": "Масштабирование синтетики",
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

Чтобы создать окно обслуживания, вам необходим запрос [POST-объекта](/docs/dynatrace-api/environment-api/settings/objects/post-object "Создание или проверка объекта настроек через Dynatrace API."). В теле запроса установите **schemaId** в `builtin:alerting.maintenance-window` и **scope** в `environment`. Предоставьте конфигурацию окна обслуживания в объекте **value**.

Ответ содержит идентификатор объекта, который необходим для изменения настроек.

#### URL-запроса

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
"maintenanceType": "Плановое",
"suppression": "Обнаруживать проблемы и отправлять уведомления",
"disableSyntheticMonitorExecution": false
},
"schedule": {
"scheduleType": "Ежемесячно",
"monthlyRecurrence": {
"dayOfMonth": 1,
"timeWindow": {
"startTime": "06:00:00",
"endTime": "06:30:00",
"timeZone": "Europe/Vienna"
}
},
"recurrenceRange": {
"scheduleStartDate": "2022-01-01",
"scheduleEndDate": "2022-12-31"
}
}
},
"filters": [
{
"entityType": "Сервис",
"entityTags": [
"Стадия:предпроизводство"
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

#### URL-запроса

```
POST https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows
```

Ответ содержит идентификатор конфигурации, который необходим для изменения настроек.

#### Тело запроса

```
{
"name": "Пример окна обслуживания",
"description": "",
"type": "Плановое",
"enabled": true,
"suppression": "Обнаруживать проблемы и отправлять уведомления",
"suppressSyntheticMonitorsExecution": false,
"scope": {
"entities": [],
"matches": [
{
"type": "Сервис",
"tags": [
{
"context": "CONTEXTLESS",
"key": "стадия",
"value": "предпроизводство"
}
],
"tagCombination": "AND"
}
]
},
"schedule": {
"recurrenceType": "Ежемесячно",
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

# Настройки 2.0

## Окна обслуживания

Чтобы редактировать окно обслуживания, вам необходимо выполнить запрос [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Редактировать объект настроек через Dynatrace API.") .

#### URL запроса

```bash
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ
```

#### Тело запроса

```json
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

```json
[
  {
    "code": 200,
    "objectId": "vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ"
  }
]
```

#### URL запроса

```bash
PUT https://mySampleEnv.live.dynatrace.com/config/v1/maintenanceWindows/07f476c6-f1ed-4519-848d-61e52f7e2f24
```

#### Тело запроса

```json
{
  "id": "07f476c6-f1ed-4519-848d-61e52f7e2f24",
  "name": "Пример MW - старый",
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

* [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.") 
* [Окна обслуживания API](/docs/dynatrace-api/configuration-api/maintenance-windows-api "Узнайте, что предлагает Dynatrace конфигурация окон обслуживания API.")