---
title: Metrics API examples - List all metrics
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/examples/list-all-metrics
scraped: 2026-05-12T12:10:06.464368
---

# Metrics API examples - List all metrics

# Metrics API examples - List all metrics

* Справочник
* Опубликовано 26 мая 2020 г.

Endpoint [GET metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "Получите список всех метрик, доступных в вашем окружении мониторинга, через Metrics v2 API.") даёт возможность запрашивать несколько метрик вместе с частичными или даже полными дескрипторами метрик.

Этот пример показывает, как получить список всех метрик окружения с основными метаданными.

Самая важная часть, это ключ метрики, так как он используется для идентификации метрики. Однако сам ключ не даёт много информации о метрике. Чтобы узнать о метриках больше, можно добавить эту важную информацию:

* имя метрики, даёт больше понимания того, что метрика измеряет
* единица измерения метрики, показывает, какую единицу использует метрика
* разрешённые агрегации, перечисляет доступные агрегации метрики. API отклоняет запрос для неподдерживаемых агрегаций.

## Настройка запроса

Чтобы получить полный список метрик, нужно задать следующие query-параметры:

* **pageSize** в `500`. Полный список метрик может быть длинным, поэтому мы используем максимально возможное значение.
* **fields** в `displayName,unit,aggregationTypes`. Это убирает из payload все остальные поля, оставляя только те, которые нам интересны. Учтите, что `metricId` здесь опущен, потому что он всегда присутствует в ответе.

Ответ можно получить в двух форматах:

* JSON: задайте заголовок **Accept** запроса в `application/json`.
* CSV-таблица: задайте заголовок **Accept** запроса в `text/csv; header=present`. Если строка заголовка вам не нужна, используйте `text/csv; header=absent`.

Чтобы аутентифицировать запрос, задайте заголовок **Authorization** запроса в `Api-token {your-token}`. Токен должен иметь разрешение **Read metrics** (`metrics.read`).

## Curl

Вот Curl-код запроса. Обязательно используйте URL своего окружения и реальный API-токен.

### JSON payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,unit,aggregationTypes&pageSize=500' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

### CSV-таблица payload

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,unit,aggregationTypes&pageSize=500' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: text/csv; header=present'
```

## URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=displayName,unit,aggregationTypes&pageSize=500
```

## Ответ

Полный список метрик слишком длинный, поэтому в каждом случае он усечён до одних и тех же 3 записей.

### JSON payload

```
{



"totalCount": 1812,



"nextPageKey": null,



"metrics": [



{



"metricId": "builtin:apps.other.apdex.osAndVersion",



"displayName": "Apdex (by os and app version)",



"unit": "NotApplicable",



"aggregationTypes": [



"auto",



"value"



]



},



{



"metricId": "builtin:apps.other.keyUserActions.requestErrorCount.os",



"displayName": "Request error count (by os)",



"unit": "Count",



"aggregationTypes": [



"auto",



"value"



]



},



{



"metricId": "builtin:tech.activemq.CurrentConnectionsCount",



"displayName": "Current connections count",



"unit": "Count",



"aggregationTypes": [



"auto",



"avg",



"count",



"max",



"min",



"sum"



]



}



]



}
```

### CSV-таблица payload

```
metricId,displayName,unit,aggregationTypes



builtin:apps.other.apdex.osAndVersion,Apdex (by os and app version),NotApplicable,"[auto, value]"



builtin:apps.other.keyUserActions.requestErrorCount.os,Request error count (by os),Count,"[auto, value]"



builtin:tech.activemq.CurrentConnectionsCount,Current connections count,Count,"[auto, avg, count, max, min, sum]"
```