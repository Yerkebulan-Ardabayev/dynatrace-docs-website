---
title: Metrics API examples - Select multiple metrics
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/examples/select-multiple-metrics
scraped: 2026-05-12T12:10:04.516117
---

# Metrics API examples - Select multiple metrics

# Metrics API examples - Select multiple metrics

* Справочник
* Опубликовано 16 июня 2020 г.

Endpoint [GET metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "Получите список всех метрик, доступных в вашем окружении мониторинга, через Metrics v2 API.") даёт возможность запрашивать несколько метрик вместе с частичными или даже полными дескрипторами метрик.

Этот пример показывает, как получить дескрипторы нескольких метрик одного родителя:

* CPU idle (`builtin:host.cpu.idle`)
* System load (`builtin:host.cpu.load`)
* CPU usage % (`builtin:host.cpu.usage`)

Для каждой мы запросим полные дескрипторы:

* Ключ метрики
* Отображаемое имя
* Описание
* Единицы измерения
* Поддерживаемые типы сущностей
* Поддерживаемые агрегации
* Агрегация по умолчанию
* Поддерживаемые трансформации
* Измерения

## Настройка запроса

Нужно задать следующие query-параметры:

* **metricSelector** в `builtin:host.cpu.(idle,usage,load)`
* **fields** в `displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions`. Учтите, что `metricId` здесь опущен, потому что он всегда присутствует в ответе.

Ответ можно получить в двух форматах:

* JSON: задайте заголовок **Accept** запроса в `application/json`.
* CSV-таблица: задайте заголовок **Accept** запроса в `text/csv; header=present`. Если строка заголовка вам не нужна, используйте `text/csv; header=absent`.

Чтобы аутентифицировать запрос, задайте заголовок **Authorization** запроса в `Api-token {your-token}`. Токен должен иметь разрешение **Read metrics** (`metrics.read`).

## Curl

Вот Curl-код запроса. Обязательно используйте URL своего окружения и реальный API-токен.

### JSON payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions&metricSelector=builtin:host.cpu.(idle,usage,load)' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

### CSV-таблица payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions&metricSelector=builtin:host.cpu.(idle,usage,load)' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: text/csv; header=present'
```

## URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions&metricSelector=builtin:host.cpu.(idle,usage,load)
```

## Ответ

Оба примера содержат полный payload, ничего не усечено.

### JSON payload

```
{



"totalCount": 3,



"nextPageKey": null,



"metrics": [



{



"metricId": "builtin:host.cpu.idle",



"displayName": "CPU idle",



"description": "",



"unit": "Percent",



"entityType": [



"HOST"



],



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



],



"transformations": [



"filter",



"fold",



"merge",



"names",



"parents"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"index": 0,



"type": "ENTITY"



}



]



},



{



"metricId": "builtin:host.cpu.load",



"displayName": "System load",



"description": "",



"unit": "Ratio",



"entityType": [



"HOST"



],



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



],



"transformations": [



"filter",



"fold",



"merge",



"names",



"parents"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"index": 0,



"type": "ENTITY"



}



]



},



{



"metricId": "builtin:host.cpu.usage",



"displayName": "CPU usage %",



"description": "Percentage of CPU time currently utilized.",



"unit": "Percent",



"entityType": [



"HOST"



],



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



],



"transformations": [



"filter",



"fold",



"merge",



"names",



"parents"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"index": 0,



"type": "ENTITY"



}



]



}



]



}
```

### CSV-таблица payload

```
metricId,displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions



builtin:host.cpu.idle,CPU idle,,Percent,[HOST],"[auto, avg, max, min]","[filter, fold, merge, names, parents]",avg,[Host:ENTITY]



builtin:host.cpu.load,System load,,Ratio,[HOST],"[auto, avg, max, min]","[filter, fold, merge, names, parents]",avg,[Host:ENTITY]



builtin:host.cpu.usage,CPU usage %,Percentage of CPU time currently utilized.,Percent,[HOST],"[auto, avg, max, min]","[filter, fold, merge, names, parents]",avg,[Host:ENTITY]
```