---
title: Миграция из профилей оповещений API в Настройки API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/alerting-profiles-to-settings
scraped: 2026-02-22T21:24:56.639325
---

# Миграция из профилей оповещений API в Настройки API

# Миграция из профилей оповещений API в Настройки API

* Ссылка
* Опубликовано 20 декабря 2022 г.

[Профили оповещений API](/docs/dynatrace-api/configuration-api/alerting-profiles-api "Узнайте, что предлагают профили оповещений Dynatrace API.") были заменены с [версией 1.249 Dynatrace](/docs/whats-new/dynatrace-api/sprint-249 "Журнал изменений для Dynatrace API версии 1.249"). Их заменой являются [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагают Настройки Dynatrace API.") с схемой **Профили оповещений о проблемах** (`builtin:alerting.profile`). Мы рекомендуем вам мигрировать в новые API как можно скорее.

Миграция влияет на URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также на объем токена для аутентификации запросов.

## Базовый URL

| новые Настройки 2.0 | старые Профили оповещений |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/alertingProfiles` |

## Объем аутентификационного токена

| новые Настройки 2.0 | старые Профили оповещений |
| --- | --- |
| **Чтение настроек** (`settings.read`) **Запись настроек** (`settings.write`) | **Чтение конфигурации** (`ReadConfig`) **Запись конфигурации** (`WriteConfig`) |

## Параметры

Чтобы узнать о новых параметрах запроса/тела, см. документацию отдельных запросов в [Настройках API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагают Настройки Dynatrace API.").

В рамках Settings 2.0 каждый профиль оповещения представлен объектом настроек. Объект содержит некоторые метаданные (например, объем или метку времени создания) и саму конфигурацию, инкапсулированную в объект **value**. Содержимое объекта **value** по сути такое же, как конфигурация в устаревших Профили оповещений API. Чтобы узнать о параметрах конфигурации профиля оповещения, запросите схему **Профили оповещений о проблемах** (`builtin:alerting.profile`) с помощью запроса [GET-схема](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотрите схему настроек через Dynatrace API.").

## Примеры

Вот некоторые примеры различий в использовании API.

### Список профилей оповещений

Settings 2.0

Профили оповещений

Чтобы перечислить все профили оповещений, вам нужно запрос [GET-объекты](/docs/dynatrace-api/environment-api/settings/objects/get-objects "Просмотрите несколько объектов настроек через Dynatrace API."). В параметрах запроса установите **schemaIds** в `builtin:alerting.profile` и **scope** в `environment`.

#### URL-адрес запроса

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



"name": "Синтетические чрезвычайные ситуации",



"severityRules": [



{



"severityLevel": "ДОСТУПНОСТЬ",



"delayInMinutes": 0,



"tagFilterIncludeMode": "ВКЛЮЧИТЬ_ЛЮБОЙ",



"tagFilter": [



"SYN_API",



"SYN_DB",



"SYN_SCH"



]



},



{



"severityLevel": "ОШИБКИ",



"delayInMinutes": 5,



"tagFilterIncludeMode": "ВКЛЮЧИТЬ_ЛЮБОЙ",



"tagFilter": [



"SYN_PLUGIN"



]



}



],



"eventFilters": []



},



{



"objectId": "vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQ1ODdkNzk5Yi1mNDI2LTQyNGYtYmY5NS1iZTQ4NzFiYWFlMmO-71TeFdrerQ",



"value": {



"name": "Высокая загрузка ЦП",



"severityRules": [



{



"severityLevel": "ПРОИЗВОДИТЕЛЬНОСТЬ",



"delayInMinutes": 30,



"tagFilterIncludeMode": "НЕТ"


},



{



"severityLevel": "КОНФЛИКТ_РЕСУРСОВ",



"delayInMinutes": 30,



"tagFilterIncludeMode": "ВКЛЮЧИТЬ_ЛЮБОЙ",



"tagFilter": [



"Holox Cluster"


]


},



{



"severityLevel": "НЕДОСТУПНОСТЬ_МОНИТОРИНГА",



"delayInMinutes": 0,



"tagFilterIncludeMode": "НЕТ"


},



{



"severityLevel": "ДОСТУПНОСТЬ",



"delayInMinutes": 0,



"tagFilterIncludeMode": "НЕТ"


}


]


,


"eventFilters": []


}


]


,


"totalCount": 2,


"pageSize": 100


}
```

#### URL-адрес запроса

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles
```

#### Тело ответа

```
{



"values": [



{



"id": "b33b45da-a14a-4478-97d3-23fce29fd767",



"name": "Синтетические чрезвычайные ситуации"


},



{



"id": "39115830-1852-3f0c-a73a-f355a19d338b",



"name": "Высокая загрузка ЦП"


}


]


}
```

### Создание профиля оповещения

Settings 2.0

Профили оповещений

Чтобы создать профиль оповещения, вам нужно запрос [POST-объект](/docs/dynatrace-api/environment-api/settings/objects/post-object "Создайте или проверьте объект настроек через Dynatrace API."). В теле запроса установите **schemaId** в `builtin:alerting.profile` и **scope** в `environment`. Предоставьте конфигурацию профиля оповещения в объекте **value**.

Ответ содержит идентификатор объекта, который вам нужно изменить настройки.

#### URL-адрес запроса

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



"name": "Пример профиля оповещения",



"severityRules": [



{



"severityLevel": "ДОСТУПНОСТЬ",



"delayInMinutes": 0,



"tagFilterIncludeMode": "НЕТ"


}


]


,


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

#### URL-адрес запроса

```
POST https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles
```

Ответ содержит идентификатор конфигурации, который вам нужно изменить настройки.

#### Тело запроса

```
{



"displayName": "Пример профиля оповещения",



"severityRules": [



{



"severityLevel": "ДОСТУПНОСТЬ",



"delayInMinutes": 0,



"tagFilterIncludeMode": "НЕТ"


}


]


,


"eventFilters": []


}
```

#### Тело ответа

```
{



"id": "2640173c-e9a8-31dc-9584-696969c716f5",



"name": "Пример профиля оповещения"


}
```

### Редактирование профиля оповещения

Settings 2.0

Профили оповещений

Чтобы отредактировать профиль оповещения, вам нужно запрос [PUT-объект](/docs/dynatrace-api/environment-api/settings/objects/put-object "Отредактируйте объект настроек через Dynatrace API.").

#### URL-адрес запроса

```
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABABhidWlsdGluOmFsZXJ0aW5nLnByb2ZpbGUABnRlbmFudAAGdGVuYW50ACQzYjAwNDMwOC01ZTZjLTNkNGMtOTNjMS01ZTBiOWRhZTlhZjW-71TeFdrerQ
```

#### Тело запроса

```
{



"schemaId": "builtin:alerting.profile",



"scope": "environment",



"value": {



"name": "Пример профиля оповещения",



"managementZone": "1291856336337388063",



"severityRules": [



{



"severityLevel": "ДОСТУПНОСТЬ",



"delayInMinutes": 0,



"tagFilterIncludeMode": "ВКЛЮЧИТЬ_ВСЕ",



"tagFilter": [



"InfraLinux",



"InraWin"


]


}


]


,


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

#### URL-адрес запроса

```
PUT https://mySampleEnv.live.dynatrace.com/config/v1/alertingProfiles/2640173c-e9a8-31dc-9584-696969c716f5
```

#### Тело запроса

```
{



"name": "Пример профиля оповещения",



"managementZone": "1291856336337388063",



"severityRules": [



{



"severityLevel": "ДОСТУПНОСТЬ",



"delayInMinutes": 0,



"tagFilterIncludeMode": "ВКЛЮЧИТЬ_ВСЕ",



"tagFilter": [



"InfraLinux",



"InraWin"


]


}


]


,


"eventFilters": []


}
```

## Связанные темы

* [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагают Настройки Dynatrace API.")
* [Профили оповещений API](/docs/dynatrace-api/configuration-api/alerting-profiles-api "Узнайте, что предлагают профили оповещений Dynatrace API.")