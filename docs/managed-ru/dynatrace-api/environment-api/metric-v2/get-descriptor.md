---
title: Metrics API - GET дескриптор метрики
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/get-descriptor
scraped: 2026-05-12T11:27:55.353829
---

# Metrics API - GET дескриптор метрики

# Metrics API - GET дескриптор метрики

* Справочник
* Опубликовано 14 июня 2019 г.

Возвращает параметры указанной метрики.

В зависимости от значения заголовка запроса **Accept** запрос возвращает один из следующих типов payload:

* `application/json`
* `text/csv; header=present`, CSV-таблица со строкой заголовка
* `text/csv; header=absent`, CSV-таблица без строки заголовка

Если заголовок **Accept** в запросе не указан, возвращается payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics/{metricKey}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics/{metricKey}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| metricKey | string | Ключ требуемой метрики.  Можно задать дополнительные операторы трансформации, разделяя их двоеточием (`:`). Дополнительную информацию о доступных трансформациях результата и синтаксисе смотрите в [Metrics selector transformations](https://dt-url.net/metricSelector?dt=m) в документации Dynatrace. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MetricDescriptor](#openapi-definition-MetricDescriptor) | Успех |
| **404** | - | Метрика не найдена. |
| **406** | - | Not acceptable. Запрошенный тип медиа не поддерживается. Проверьте заголовок **Accept** в запросе. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `MetricDescriptor`

Дескриптор метрики.

| Поле | Тип | Описание |
| --- | --- | --- |
| aggregationTypes | string[] | Список допустимых агрегаций для этой метрики. Поле может принимать значения: * `auto` * `avg` * `count` * `max` * `median` * `min` * `percentile` * `sum` * `value` |
| billable | boolean | Если `true`, использование метрики тарифицируется.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. |
| created | integer | Метка времени создания метрики.  Встроенные метрики и выражения метрик имеют значение `null`. |
| dduBillable | boolean | Если `true`, использование метрики потребляет [Davis data units](https://dt-url.net/ddu?dt=m). Устарело и всегда `false` для Dynatrace Platform Subscription. Заменено на `isBillable`.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. |
| defaultAggregation | [MetricDefaultAggregation](#openapi-definition-MetricDefaultAggregation) | Агрегация метрики по умолчанию. |
| description | string | Краткое описание метрики. |
| dimensionCardinalities | [MetricDimensionCardinality[]](#openapi-definition-MetricDimensionCardinality) | Кардинальности измерений метрики MINT. |
| dimensionDefinitions | [MetricDimensionDefinition[]](#openapi-definition-MetricDimensionDefinition) | Детальное деление метрики (например, группа процессов и ID процесса для некоторых метрик, связанных с процессами).  Для [ingested metrics](https://dt-url.net/5d63ic1?dt=m) измерения, у которых нет данных за последние 15 дней, пропускаются. |
| displayName | string | Имя метрики в интерфейсе пользователя. |
| entityType | string[] | Список допустимых первичных типов сущностей для этой метрики. Можно использовать для предиката `type` в `entitySelector`. |
| impactRelevant | boolean | Метрика релевантна (`true`) или не релевантна (`false`) для воздействия.  Метрика, релевантная для воздействия, сильно зависит от других метрик и меняется, потому что изменилась нижележащая метрика-первопричина.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. |
| lastWritten | integer | Метка времени последней записи метрики.  Имеет значение `null` для выражений метрик или если данные никогда не записывались. |
| latency | integer | Задержка метрики, в минутах.  Задержка, это ожидаемая задержка отчётности (например, вызванная ограничениями облачных провайдеров или других сторонних источников данных) между наблюдением точки данных метрики и её доступностью в Dynatrace.  Допустимый диапазон значений: от 1 до 60 минут.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. |
| maximumValue | number | Максимально допустимое значение метрики.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. |
| metricId | string | Полностью квалифицированный ключ метрики.  Если использовалась трансформация, она отражается в ключе метрики. |
| metricSelector | string | Селектор метрики, используемый при запросе метрики func:. |
| metricValueType | [MetricValueType](#openapi-definition-MetricValueType) | Тип значения метрики. |
| minimumValue | number | Минимально допустимое значение метрики.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. |
| resolutionInfSupported | boolean | Если 'true', к запросу метрики можно применить resolution=Inf. |
| rootCauseRelevant | boolean | Метрика релевантна (`true`) или не релевантна (`false`) для первопричины.  Метрика, релевантная для первопричины, представляет собой сильный индикатор неисправного компонента.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. |
| scalar | boolean | Указывает, разрешается ли выражение метрики в скаляр (`true`) или в серию (`false`). Скалярный результат всегда содержит одну точку данных. Количество точек данных в серийном результате зависит от используемого разрешения. |
| tags | string[] | Теги, применённые к метрике.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. |
| transformations | string[] | Операторы трансформации, которые можно добавить к текущему списку трансформаций. Поле может принимать значения: * `asGauge` * `default` * `delta` * `evaluateModel` * `filter` * `fold` * `histogram` * `last` * `lastReal` * `limit` * `merge` * `names` * `parents` * `partition` * `rate` * `rollup` * `setUnit` * `smooth` * `sort` * `splitBy` * `timeshift` * `toUnit` |
| unit | string | Единица измерения метрики. |
| unitDisplayFormat | string | Сырое значение хранится в битах или байтах. Интерфейс пользователя может отображать его в этих системах счисления:  Двоичная: 1 MiB = 1024 KiB = 1 048 576 байт  Десятичная: 1 MB = 1000 kB = 1 000 000 байт  Если не задано, используется десятичная система.  [Metric expressions](https://dt-url.net/metricExpression?dt=m) не возвращают это поле. Поле может принимать значения: * `binary` * `decimal` |
| warnings | string[] | Список потенциальных предупреждений, влияющих на этот ID. Например, использование устаревшей функциональности и т. п. |

#### Объект `MetricDefaultAggregation`

Агрегация метрики по умолчанию.

| Поле | Тип | Описание |
| --- | --- | --- |
| parameter | number | Доставляемый процентиль. Допустимые значения: от `0` до `100`.  Применимо только к типу агрегации `percentile`. |
| type | string | Тип агрегации по умолчанию. Поле может принимать значения: * `auto` * `avg` * `count` * `max` * `median` * `min` * `percentile` * `sum` * `value` |

#### Объект `MetricDimensionCardinality`

Кардинальности измерений метрики.

| Поле | Тип | Описание |
| --- | --- | --- |
| estimate | integer | Оценка кардинальности измерения. |
| key | string | Ключ измерения.  Должен быть уникальным в пределах метрики. |
| relative | number | Относительная кардинальность измерения, выраженная в процентах |

#### Объект `MetricDimensionDefinition`

Измерение метрики.

| Поле | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя измерения. |
| index | integer | Уникальный 0-based индекс измерения.  Добавление трансформаций, таких как :names или :parents, может изменить индексы измерений. `null` используется для измерений метрики с гибкими измерениями, на которые можно ссылаться по их ключу измерения, но которые не имеют внутреннего порядка, который можно было бы использовать для индекса. |
| key | string | Ключ измерения.  Должен быть уникальным в пределах метрики. |
| name | string | Имя измерения. |
| type | string | Тип измерения. Поле может принимать значения: * `ENTITY` * `NUMBER` * `OTHER` * `STRING` * `VOID` |

#### Объект `MetricValueType`

Тип значения метрики.

| Поле | Тип | Описание |
| --- | --- | --- |
| type | string | Тип значения метрики Поле может принимать значения: * `error` * `score` * `unknown` |

### JSON-модели тела ответа

```
{



"aggregationTypes": [



"auto",



"value"



],



"created": 1597400123451,



"dduBillable": false,



"defaultAggregation": {



"type": "value"



},



"description": "Percentage of user-space CPU time currently utilized, per host.",



"dimensionCardinalities": [



{



"estimate": 20,



"key": "dt.entity.host",



"relative": 0.2



}



],



"dimensionDefinitions": [



{



"displayName": "Host",



"index": 0,



"key": "dt.entity.host",



"name": "Host",



"type": "ENTITY"



}



],



"displayName": "CPU user",



"entityType": [



"HOST"



],



"lastWritten": 1597400717783,



"latency": 1,



"metricId": "builtin:host.cpu.user:splitBy(\"dt.entity.host\"):max:fold",



"metricValueType": {



"type": "unknown"



},



"scalar": false,



"tags": [],



"transformations": [



"filter",



"fold",



"limit",



"merge",



"names",



"parents",



"timeshift",



"rate",



"sort",



"last",



"splitBy"



],



"unit": "Percent"



}
```

## Пример

В этом примере запрос запрашивает параметры трёх метрик: **builtin:host.cpu.idle**, **builtin:host.cpu.usage** и **builtin:host.disk.avail**.

Метрики **builtin:host.cpu.idle** и **builtin:host.cpu.usage** имеют общий родитель, и их селектор объединён в **builtin:host.cpu.(idle,usage)**.

Ответ в формате `application/json`.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics/builtin:host.disk.avail' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics/builtin:host.disk.avail
```

#### Тело ответа

```
{



"metricId": "builtin:host.disk.avail",



"displayName": "Disk available",



"description": "",



"unit": "Byte",



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



},



{



"key": "dt.entity.disk",



"name": "Disk",



"index": 1,



"type": "ENTITY"



}



]



}
```

CSV-таблица со строкой заголовка выглядит так. Чтобы получить её, измените заголовок **Accept** на `text/csv; header=present`.

```
metricId,displayName,description,unit,entityType,aggregationTypes,transformations,defaultAggregation,dimensionDefinitions



builtin:host.cpu.usage,CPU usage %,Percentage of CPU time currently utilized.,Percent,[HOST],"[auto, avg, max, min]","[filter, fold, merge, names, parents]",avg,[Host:ENTITY]
```

#### Код ответа

200