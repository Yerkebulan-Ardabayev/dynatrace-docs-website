---
title: Миграция с Alerting profiles API на Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/alerting-profiles-to-settings
scraped: 2026-03-06T21:34:32.542628
---

# Миграция с Alerting profiles API на Settings API


* Справочник
* Опубликовано 20 декабря 2022 г.

[Alerting profiles API](../../configuration-api/alerting-profiles-api.md "Узнайте, что предлагает Dynatrace Alerting profiles API.") объявлен устаревшим в [Dynatrace версии 1.249](../../../whats-new/dynatrace-api/sprint-249.md "Список изменений Dynatrace API версии 1.249"). Его заменой является [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.") со схемой **Problem alerting profiles** (`builtin:alerting.profile`). Мы рекомендуем выполнить миграцию на новый API при первой возможности.

Миграция затрагивает URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Базовый URL

| новый Settings 2.0 | старый Alerting profiles |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/alertingProfiles` |

## Область действия токена аутентификации

| новый Settings 2.0 | старый Alerting profiles |
| --- | --- |
| **Read settings** (`settings.read`) **Write settings** (`settings.write`) | **Read configuration** (`ReadConfig`) **Write configuration** (`WriteConfig`) |

## Параметры

Чтобы узнать о новых параметрах запросов/тела, см. документацию отдельных запросов в [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.").

В рамках Settings 2.0 каждый профиль оповещений представлен объектом настроек. Объект содержит метаданные (такие как область действия или временная метка создания) и саму конфигурацию, инкапсулированную в объекте **value**. Содержимое **value** по существу совпадает с конфигурацией в устаревшем Alerting profiles API. Чтобы узнать о параметрах конфигурации профиля оповещений, запросите схему **Problem alerting profiles** (`builtin:alerting.profile`) с помощью запроса [GET a schema](../../environment-api/settings/schemas/get-schema.md "Просмотрите схему настроек через Dynatrace API.").

## Примеры

Ниже приведены примеры различий в использовании API.

### Список профилей оповещений

Settings 2.0

Alerting profiles

Чтобы получить список всех профилей оповещений, используйте запрос [GET objects](../../environment-api/settings/objects/get-objects.md "Просмотрите несколько объектов настроек через Dynatrace API."). В параметрах запроса установите **schemaIds** в значение `builtin:alerting.profile`, а **scope** — в значение `environment`.

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:alerting.profile&scopes=environment
```

#### Тело ответа

```
{


"items": [


{


"objectId": "vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQ4M2Q3NDk5YS1mZDY2LTQ1OGYtOGIxNy1iYjNkMzgwN2RmMTa-71TeFdrerQ",


"value": {


"name": "Synthetic Emergencies",


"severityRules": [


{


"severityLevel": "AVAILABILITY",


"delayInMinutes": 0,


"tagFilterIncludeMode": "INCLUDE_ANY",


"tagFilter": [


"SYN_API",


"SYN_DB",


"SYN_SCH"


]


},


{


"severityLevel": "ERRORS",


"delayInMinutes": 5,


"tagFilterIncludeMode": "INCLUDE_ANY",


"tagFilter": [


"SYN_PLUGIN"


]


}


],


"eventFilters": []


}


},


{


"objectId": "vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQ1ODdkNzk5Yi1mNDI2LTQyNGYtYmY5NS1iZTQ4NzFiYWFlMmO-71TeFdrerQ",


"value": {


"name": "CPU high",


"severityRules": [


{


"severityLevel": "PERFORMANCE",


"delayInMinutes": 30,


"tagFilterIncludeMode": "NONE"


},


{


"severityLevel": "RESOURCE_CONTENTION",


"delayInMinutes": 30,


"tagFilterIncludeMode": "INCLUDE_ANY",


"tagFilter": [


"Holox Cluster"


]


},


{


"severityLevel": "MONITORING_UNAVAILABLE",


"delayInMinutes": 0,


"tagFilterIncludeMode": "NONE"


},


{


"severityLevel": "AVAILABILITY",


"delayInMinutes": 0,


"tagFilterIncludeMode": "NONE"


}


],


"eventFilters": []


}


}


],


"totalCount": 2,


"pageSize": 100


}
```

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles
```

#### Тело ответа

```
{


"values": [


{


"id": "b33b45da-a14a-4478-97d3-23fce29fd767",


"name": "Synthetic Emergencies"


},


{


"id": "39115830-1852-3f0c-a73a-f355a19d338b",


"name": "CPU high"


}


]


}
```

### Создание профиля оповещений

Settings 2.0

Alerting profiles

Чтобы создать профиль оповещений, используйте запрос [POST an object](../../environment-api/settings/objects/post-object.md "Создайте или проверьте объект настроек через Dynatrace API."). В теле запроса установите **schemaId** в значение `builtin:alerting.profile`, а **scope** — в значение `environment`. Укажите конфигурацию профиля оповещений в объекте **value**.

Ответ содержит идентификатор объекта, необходимый для изменения настроек.

#### URL запроса

```
POST https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects
```

#### Тело запроса

```
[


{


"schemaId": "builtin:alerting.profile",


"scope": "environment",


"value": {


"name": "Sample alerting profile",


"severityRules": [


{


"severityLevel": "AVAILABILITY",


"delayInMinutes": 0,


"tagFilterIncludeMode": "NONE"


}


],


"eventFilters": []


}


}


]
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
POST https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles
```

Ответ содержит идентификатор конфигурации, необходимый для изменения настроек.

#### Тело запроса

```
{


"displayName": "Sample alerting profile",


"severityRules": [


{


"severityLevel": "AVAILABILITY",


"delayInMinutes": 0,


"tagFilterIncludeMode": "NONE"


}


],


"eventFilters": []


}
```

#### Тело ответа

```
{


"id": "2640173c-e9a8-31dc-9584-696969c716f5",


"name": "Sample alerting profile"


}
```

### Редактирование профиля оповещений

Settings 2.0

Alerting profiles

Чтобы отредактировать профиль оповещений, используйте запрос [PUT an object](../../environment-api/settings/objects/put-object.md "Отредактируйте объект настроек через Dynatrace API.").

#### URL запроса

```
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ
```

#### Тело запроса

```
{


"schemaId": "builtin:alerting.profile",


"scope": "environment",


"value": {


"name": "Sample alerting profile",


"managementZone": "1291856336337388063",


"severityRules": [


{


"severityLevel": "AVAILABILITY",


"delayInMinutes": 0,


"tagFilterIncludeMode": "INCLUDE_ALL",


"tagFilter": [


"InfraLinux",


"InraWin"


]


}


],


"eventFilters": []


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
PUT https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles/2640173c-e9a8-31dc-9584-696969c716f5
```

#### Тело запроса

```
{


"name": "Sample alerting profile",


"managementZone": "1291856336337388063",


"severityRules": [


{


"severityLevel": "AVAILABILITY",


"delayInMinutes": 0,


"tagFilterIncludeMode": "INCLUDE_ALL",


"tagFilter": [


"InfraLinux",


"InraWin"


]


}


],


"eventFilters": []


}
```

## Связанные темы

* [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.")
* [Alerting profiles API](../../configuration-api/alerting-profiles-api.md "Узнайте, что предлагает Dynatrace Alerting profiles API.")
