---
title: Пользовательские метаданные метрик
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata
scraped: 2026-03-06T21:33:32.965519
---

# Метаданные пользовательских метрик


Чтобы добавить больше контекста к точкам данных и их измерениям, ваша пользовательская метрика может содержать дополнительную полезную информацию, такую как единица измерения, отображаемое имя и диапазоны значений.

Такую информацию можно предоставить через метаданные пользовательских метрик. Метаданные хранятся независимо от точек данных и связаны с ними через ключ метрики. Вы можете передавать точки данных и задавать метаданные в любом порядке.

Нельзя предоставлять метаданные для встроенных или вычисляемых метрик; метаданные поддерживаются только для пользовательских принятых метрик.

## Доступные параметры

Для метаданных метрик доступны следующие параметры.

Параметры

Пример JSON

#### Объект `MetricProperties`

Свойства метрики.

#### Объект `MetricDimensions`

Измерение метрики.

```
{


"displayName": "Total revenue",


"description": "Total store revenue by region, city, and store",


"unit": "Unspecified",


"sourceEntityType": "string",


"tags": ["KPI", "Business"],


"metricProperties": {


"maxValue": 1000000,


"minValue": 0,


"rootCauseRelevant": false,


"impactRelevant": true,


"valueType": "score",


"latency": 1


},


"dimensions": [


{


"key": "city",


"displayName": "City name"


},


{


"key": "country",


"displayName": "Country name"


},


{


"key": "region",


"displayName": "Sales region"


},


{


"key": "store",


"displayName": "Store #"


}


]


}
```

## Установка метаданных метрики

Используйте вызов [POST an object](../../../../dynatrace-api/environment-api/settings/objects/post-object.md "Создание или проверка объекта настроек через API Dynatrace.") API настроек для предоставления метаданных вашей метрики. Используйте следующие параметры в теле запроса:

| Поле | Значение |
| --- | --- |
| scope | metric-{your-metric-key} |
| schemaId | builtin:metric.metadata |
| value | Нужный набор метаданных. См. доступные поля выше. |

Пример тела запроса

```
[


{


"scope": "metric-business.shop.revenue",


"schemaId": "builtin:metric.metadata",


"value": {


"displayName": "Total revenue",


"description": "Total store revenue by region, city, and store",


"unit": "Unspecified",


"sourceEntityType": "string",


"tags": ["KPI", "Business"],


"metricProperties": {


"maxValue": 1000000,


"minValue": 0,


"rootCauseRelevant": false,


"impactRelevant": true,


"valueType": "score",


"latency": 1


},


"dimensions": [


{


"key": "city",


"displayName": "City name"


},


{


"key": "country",


"displayName": "Country name"


},


{


"key": "region",


"displayName": "Sales region"


},


{


"key": "store",


"displayName": "Store #"


}


]


}


}


]
```

Кроме того, вы можете:

* Отправить метаданные через [протокол приёма данных](metric-ingestion-protocol.md#metadata "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.").
* Настроить метаданные метрики в [браузере метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace.").

## Просмотр метаданных метрики

Вы можете получить метаданные метрики через вызов [GET metric descriptor](../../../../dynatrace-api/environment-api/metric-v2/get-descriptor.md "Просмотр дескриптора метрики через Metrics v2 API.") API метрик v2 или через [браузер метрик](../../../../analyze-explore-automate/dashboards-classic/metrics-browser.md "Просмотр метрик с помощью браузера метрик Dynatrace.").

## Связанные темы

* [API метрик — POST для загрузки точек данных](../../../../dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md "Загрузка пользовательских метрик в Dynatrace через Metrics v2 API.")
* [API настроек](../../../../dynatrace-api/environment-api/settings.md "Узнайте, что предлагает API настроек Dynatrace.")
