---
title: Переход с обнаружения частых проблем API на Настройки API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/frequent-issues-to-settings
scraped: 2026-02-21T21:23:13.705033
---

# Переход с обнаружения частых проблем API на Настройки API

# Переход с обнаружения частых проблем API на Настройки API

* Ссылка
* Опубликовано 22 декабря 2022 года

[Обнаружение частых проблем API](/docs/dynatrace-api/configuration-api/frequent-issue-detection-api "Управление конфигурацией обнаружения частых проблем через Dynatrace API.") было устарено с [Dynatrace версии 1.249](/docs/whats-new/dynatrace-api/sprint-249 "Журнал изменений Dynatrace API версии 1.249"). Его заменой является [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.") с схемой **Обнаружение частых проблем** (`builtin:anomaly-detection.frequent-issues`). Мы рекомендуем перейти на новую API как можно скорее.

Миграция затрагивает URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Базовый URL

| новые Настройки 2.0 | старое Обнаружение частых проблем |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/frequentIssueDetection` |

## Область действия токена аутентификации

| новые Настройки 2.0 | старое Обнаружение частых проблем |
| --- | --- |
| **Чтение настроек** (`settings.read`) **Запись настроек** (`settings.write`) | **Чтение конфигурации** (`ReadConfig`) **Запись конфигурации** (`WriteConfig`) |

## Параметры

Чтобы узнать о новых параметрах запроса/тела, см. документацию отдельных запросов в [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.").

В рамках Настроек 2.0 каждая конфигурация обнаружения частых проблем представлена объектом настроек. Объект содержит некоторые метаданные (например, область или метка времени создания) и саму конфигурацию, инкапсулированную в объект **значение**. Чтобы узнать о параметрах конфигурации обнаружения частых проблем, запросите схему **Обнаружение частых проблем** (`builtin:anomaly-detection.frequent-issues`) с помощью запроса [Получить схему](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотреть схему настроек через Dynatrace API.").

## Примеры

Вот некоторые примеры различий в использовании API.

### Просмотр конфигурации

Настройки 2.0

Обнаружение частых проблем

Чтобы просмотреть конфигурации обнаружения частых проблем, вам необходим запрос [Получить объекты](/docs/dynatrace-api/environment-api/settings/objects/get-objects "Просмотреть несколько объектов настроек через Dynatrace API."). В параметрах запроса установите **schemaIds** в `builtin:anomaly-detection.frequent-issues` и **scope** в `environment`.

#### URL-адрес запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:anomaly-detection.frequent-issues&scopes=environment
```

#### Тело ответа

```
{



"items": [



{



"objectId": "vu9U3hXa3q0AAAABAClidWlsdGluOmFub21hbHktZGV0ZWN0aW9uLmZyZXF1ZW50LWlzc3VlcwAGdGVuYW50AAZ0ZW5hbnQAJDNiNjk1ZjA4LWNhZDEtM2Y2OC04ZDM4LTQyODZkNzkzNjlkNL7vVN4V2t6t",



"value":).



"detectFrequentIssuesInApplications": true,



"detectFrequentIssuesInTransactionsAndServices": true,



"detectFrequentIssuesInInfrastructure": true



}



]



"totalCount": 1,



"pageSize": 500



}
```

#### URL-адрес запроса

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/frequentIssueDetection
```

#### Тело ответа

```
{



"metadata":.



"currentConfigurationVersions": [



"1.0.2"



],



"configurationVersions": [],



"clusterVersion": "1.258.0.20221221-200358"



},



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": true



}
```

### Обновление конфигурации

Настройки 2.0

Обнаружение частых проблем

Чтобы отредактировать окно обслуживания, вам необходим запрос [Изменить объект](/docs/dynatrace-api/environment-api/settings/objects/put-object "Изменить объект настроек через Dynatrace API."). В теле запроса установите **schemaId** в `builtin:anomaly-detection.frequent-issues` и **scope** в `environment`. Предоставьте конфигурацию обнаружения частых проблем в объекте **значение**.

#### URL-адрес запроса

```
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABAClidWlsdGluOmFub21hbHktZGV0ZWN0aW9uLmZyZXF1ZW50LWlzc3VlcwAGdGVuYW50AAZ0ZW5hbnQAJDNiNjk1ZjA4LWNhZDEtM2Y2OC04ZDM4LTQyODZkNzkzNjlkNL7vVN4V2t6t
```

#### Тело запроса

```
{



"schemaId": "builtin:alerting.maintenance-window",



"scope": "environment",



"value":.



"detectFrequentIssuesInApplications": true,



"detectFrequentIssuesInTransactionsAndServices": true,



"detectFrequentIssuesInInfrastructure": true



}



}
```

#### Тело ответа

```
[



{



"code": 200,



"objectId": "vu9U3hXa3q0AAAABAClidWlsdGluOmFub21hbHktZGV0ZWN0aW9uLmZyZXF1ZW50LWlzc3VlcwAGdGVuYW50AAZ0ZW5hbnQAJDNiNjk1ZjA4LWNhZDEtM2Y2OC04ZDM4LTQyODZkNzkzNjlkNL7vVN4V2t6t"



}



]
```

#### URL-адрес запроса

```
PUT https://mySampleEnv.live.dynatrace.com/config/v1/frequentIssueDetection/07f476c6-f1ed-4519-848d-61e52f7e2f24
```

#### Тело запроса

```
{



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": false



}
```

## Связанные темы

* [Настройки API](/docs/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Настройки API.")
* [Обнаружение частых проблем API](/docs/dynatrace-api/configuration-api/frequent-issue-detection-api "Управление конфигурацией обнаружения частых проблем через Dynatrace API.")