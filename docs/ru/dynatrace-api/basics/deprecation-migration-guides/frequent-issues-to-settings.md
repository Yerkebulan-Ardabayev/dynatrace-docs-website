---
title: Миграция с Frequent issue detection API на Settings API
source: https://www.dynatrace.com/docs/dynatrace-api/basics/deprecation-migration-guides/frequent-issues-to-settings
scraped: 2026-03-05T21:39:01.543097
---

# Миграция с API обнаружения частых проблем на Settings API


* Reference
* Published Dec 22, 2022

[API обнаружения частых проблем](../../configuration-api/frequent-issue-detection-api.md "Управление конфигурацией обнаружения частых проблем через Dynatrace API.") был объявлен устаревшим в [Dynatrace версии 1.249](../../../whats-new/dynatrace-api/sprint-249.md "Список изменений для Dynatrace API версии 1.249"). Его замена — [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.") со схемой **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`). Мы рекомендуем выполнить миграцию на новый API при первой возможности.

Миграция затрагивает URL-адреса конечных точек, параметры запросов и параметры тела запроса/ответа, а также область действия токена для аутентификации запросов.

## Базовый URL

| новый Settings 2.0 | старый API обнаружения частых проблем |
| --- | --- |
| `/api/v2/settings` | `/api/config/v1/frequentIssueDetection` |

## Область действия токена аутентификации

| новый Settings 2.0 | старый API обнаружения частых проблем |
| --- | --- |
| **Read settings** (`settings.read`) **Write settings** (`settings.write`) | **Read configuration** (`ReadConfig`) **Write configuration** (`WriteConfig`) |

## Параметры

Чтобы узнать о новых параметрах запроса/тела, см. документацию отдельных запросов в [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.").

В рамках Settings 2.0 каждая конфигурация обнаружения частых проблем представлена объектом настроек. Объект содержит метаданные (такие как область действия или временная метка создания) и саму конфигурацию, инкапсулированную в объекте **value**. Чтобы узнать о параметрах конфигурации обнаружения частых проблем, запросите схему **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`) с помощью запроса [GET a schema](../../environment-api/settings/schemas/get-schema.md "Просмотр схемы настроек через Dynatrace API.").

## Примеры

Ниже приведены примеры различий в использовании API.

### Просмотр конфигурации

Settings 2.0

Frequent issue detection

Для просмотра конфигураций обнаружения частых проблем необходимо использовать запрос [GET objects](../../environment-api/settings/objects/get-objects.md "Просмотр нескольких объектов настроек через Dynatrace API."). В параметрах запроса установите **schemaIds** в значение `builtin:anomaly-detection.frequent-issues` и **scope** в значение `environment`.

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects?schemaIds=builtin:anomaly-detection.frequent-issues&scopes=environment
```

#### Тело ответа

```
{


"items": [


{


"objectId": "vu9U3hXa3q0AAAABAClidWlsdGluOmFub21hbHktZGV0ZWN0aW9uLmZyZXF1ZW50LWlzc3VlcwAGdGVuYW50AAZ0ZW5hbnQAJDNiNjk1ZjA4LWNhZDEtM2Y2OC04ZDM4LTQyODZkNzkzNjlkNL7vVN4V2t6t",


"value": {


"detectFrequentIssuesInApplications": true,


"detectFrequentIssuesInTransactionsAndServices": true,


"detectFrequentIssuesInInfrastructure": true


}


}


],


"totalCount": 1,


"pageSize": 500


}
```

#### URL запроса

```
GET https://mySampleEnv.live.dynatrace.com/config/v1/frequentIssueDetection
```

#### Тело ответа

```
{


"metadata": {


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

Settings 2.0

Frequent issue detection

Для редактирования окна обслуживания необходимо использовать запрос [PUT an object](../../environment-api/settings/objects/put-object.md "Редактирование объекта настроек через Dynatrace API."). В теле запроса установите **schemaId** в значение `builtin:anomaly-detection.frequent-issues` и **scope** в значение `environment`. Укажите конфигурацию обнаружения частых проблем в объекте **value**.

#### URL запроса

```
PUT https://mySampleEnv.live.dynatrace.com/api/v2/settings/objects/vu9U3hXa3q0AAAABAClidWlsdGluOmFub21hbHktZGV0ZWN0aW9uLmZyZXF1ZW50LWlzc3VlcwAGdGVuYW50AAZ0ZW5hbnQAJDNiNjk1ZjA4LWNhZDEtM2Y2OC04ZDM4LTQyODZkNzkzNjlkNL7vVN4V2t6t
```

#### Тело запроса

```
{


"schemaId": "builtin:alerting.maintenance-window",


"scope": "environment",


"value": {


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

#### URL запроса

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

* [Settings API](../../environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.")
* [API обнаружения частых проблем](../../configuration-api/frequent-issue-detection-api.md "Управление конфигурацией обнаружения частых проблем через Dynatrace API.")
