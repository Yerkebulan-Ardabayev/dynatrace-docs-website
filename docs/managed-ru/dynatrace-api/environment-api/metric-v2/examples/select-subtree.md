---
title: Metrics API examples - Select full metric subtree
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/examples/select-subtree
scraped: 2026-05-12T12:10:08.554496
---

# Metrics API examples - Select full metric subtree

# Metrics API examples - Select full metric subtree

* Справочник
* Опубликовано 22 июня 2020 г.

Endpoint [GET metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "Получите список всех метрик, доступных в вашем окружении мониторинга, через Metrics v2 API.") даёт возможность выбрать полное поддерево метрик с помощью завершающего символа подстановки звёздочки (`*`). Символ-звёздочка выбирает все метрики родителя без необходимости указывать каждую из них.

Этот пример показывает, как получить дескрипторы всех метрик CPU хоста.

Чтобы сделать ответ короче, мы запросим только следующие параметры:

* Ключ метрики
* Отображаемое имя
* Агрегация по умолчанию

Разумеется, можно запросить полные дескрипторы метрики. О том, как это сделать, смотрите пример [select multiple metrics](/managed/dynatrace-api/environment-api/metric-v2/examples/select-multiple-metrics "Получите список дескрипторов нескольких связанных метрик через Dynatrace API.").

## Настройка запроса

Нужно задать следующие query-параметры:

* **metricSelector** в `builtin:host.cpu.*`.
* **fields** в `displayName,defaultAggregation`. Учтите, что `metricId` здесь опущен, потому что он всегда присутствует в ответе.

Ответ можно получить в двух форматах:

* JSON: задайте заголовок **Accept** запроса в `application/json`.
* CSV-таблица: задайте заголовок **Accept** запроса в `text/csv; header=present`. Если строка заголовка вам не нужна, используйте `text/csv; header=absent`.

Чтобы аутентифицировать запрос, задайте заголовок **Authorization** запроса в `Api-token {your-token}`. Токен должен иметь разрешение **Read metrics** (`metrics.read`).

## Curl

Вот Curl-код запроса. Обязательно используйте URL своего окружения и реальный API-токен.

### JSON payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,defaultAggregation&metricSelector=builtin:host.cpu.*' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

### CSV-таблица payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,defaultAggregation&metricSelector=builtin:host.cpu.*' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: text/csv; header=present'
```

## URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,defaultAggregation&metricSelector=builtin:host.cpu.*
```

## Ответ

Оба примера содержат полный payload; ничего не усечено.

### JSON payload

```
{



"totalCount": 17,



"nextPageKey": null,



"metrics": [



{



"metricId": "builtin:host.cpu.entc",



"displayName": "AIX Entitlement used",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.entConfig",



"displayName": "AIX Entitlement configured",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.idle",



"displayName": "CPU idle",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.iowait",



"displayName": "CPU I/O wait",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.load",



"displayName": "System load",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.load15m",



"displayName": "System load15m",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.load5m",



"displayName": "System load5m",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.msu.avg",



"displayName": "MSU average",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.msu.capacity",



"displayName": "MSU capacity",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.other",



"displayName": "CPU other",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.physc",



"displayName": "AIX Physical consumed",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.steal",



"displayName": "CPU steal",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.system",



"displayName": "CPU system",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.usage",



"displayName": "CPU usage %",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.user",



"displayName": "CPU user",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.ziip.eligible",



"displayName": "zIIP eligible",



"defaultAggregation": {



"type": "avg"



}



},



{



"metricId": "builtin:host.cpu.ziip.usage",



"displayName": "zIIP usage",



"defaultAggregation": {



"type": "avg"



}



}



]



}
```

### CSV-таблица payload

```
metricId,displayName,defaultAggregation



builtin:host.cpu.entc,AIX Entitlement used,avg



builtin:host.cpu.entConfig,AIX Entitlement configured,avg



builtin:host.cpu.idle,CPU idle,avg



builtin:host.cpu.iowait,CPU I/O wait,avg



builtin:host.cpu.load,System load,avg



builtin:host.cpu.load15m,System load15m,avg



builtin:host.cpu.load5m,System load5m,avg



builtin:host.cpu.msu.avg,MSU average,avg



builtin:host.cpu.msu.capacity,MSU capacity,avg



builtin:host.cpu.other,CPU other,avg



builtin:host.cpu.physc,AIX Physical consumed,avg



builtin:host.cpu.steal,CPU steal,avg



builtin:host.cpu.system,CPU system,avg



builtin:host.cpu.usage,CPU usage %,avg



builtin:host.cpu.user,CPU user,avg



builtin:host.cpu.ziip.eligible,zIIP eligible,avg



builtin:host.cpu.ziip.usage,zIIP usage,avg
```