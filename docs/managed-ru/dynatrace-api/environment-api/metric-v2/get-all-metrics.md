---
title: Metrics API - GET метрики
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics
scraped: 2026-05-12T11:11:59.028466
---

# Metrics API - GET метрики

# Metrics API - GET метрики

* Справочник
* Опубликовано 14 июня 2019 г.

Возвращает список всех доступных метрик.

Вывод можно ограничить с помощью пагинации:

1. Укажите количество результатов на страницу в query-параметре **pageSize**.
2. Затем используйте курсор из поля **nextPageKey** предыдущего ответа в query-параметре **nextPageKey**, чтобы получить следующие страницы.

В зависимости от значения заголовка запроса **Accept** запрос возвращает один из следующих типов payload:

* `application/json`
* `text/csv; header=present`, CSV-таблица со строкой заголовка
* `text/csv; header=absent`, CSV-таблица без строки заголовка

Если заголовок **Accept** в запросе не указан, возвращается payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/metrics` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/metrics` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Находится в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если query-параметр **nextPageKey** не указан.  Когда **nextPageKey** задан для получения следующих страниц, все остальные query-параметры нужно опустить. | query | Необязательный |
| pageSize | integer | Количество схем метрик в одном payload ответа.  Максимально допустимый размер страницы: 500.  Если не задан, используется 100.  Если указано значение больше 500, на страницу возвращается только 500 результатов. | query | Необязательный |
| metricSelector | string | Выбирает метрики для запроса по их ключам.  Можно указать несколько ключей метрик через запятую (например, `metrickey1,metrickey2`). Чтобы выбрать несколько метрик с общим родителем, перечислите последнюю часть нужных ключей метрик в скобках через запятую, сохранив общую часть без изменений. Например, чтобы получить метрики `builtin:host.cpu.idle` и `builtin:host.cpu.user`, напишите: `builtin:host.cpu.(idle,user)`.  Полный набор связанных метрик можно выбрать с помощью завершающего символа подстановки звёздочки (`*`). Например, `builtin:host.*` выбирает все метрики хостов, а `builtin:*` выбирает все метрики, предоставляемые Dynatrace.  Можно задать дополнительные операторы трансформации, разделяя их двоеточием (`:`). Дополнительную информацию о доступных трансформациях результата и синтаксисе смотрите в [Metrics selector transformations](https://dt-url.net/metricSelector?dt=m) в документации Dynatrace.  Этот endpoint поддерживает только трансформации `aggregation`, `merge`, `parents` и `splitBy`.  Если ключ метрики содержит символы, которые нужно экранировать, ключ необходимо взять в кавычки (`"`). Следующие символы внутри ключа метрики в кавычках должны быть экранированы тильдой (`~`):  * Кавычки (`"`) * Тильды (`~`)  Например, чтобы запросить метрику с ключом **ext:selfmonitoring.jmx.Agents: Type "APACHE"**, нужно указать такой селектор:  `"ext:selfmonitoring.jmx.Agents: Type ~"APACHE~""`  Чтобы найти метрики по поисковому термину, а не по metricId, используйте query-параметр **text** вместо этого. | query | Необязательный |
| text | string | Поисковый термин в реестре метрик. Показывает только метрики, содержащие термин в ключе, отображаемом имени или описании. Используйте параметр `metricSelector` вместо этого, чтобы выбрать полную иерархию метрик, а не выполнять текстовый поиск. | query | Необязательный |
| fields | string | Определяет список свойств метрики, включаемых в ответ.  `metricId` включается в результат **всегда**. Дополнительно доступны следующие свойства:  * `displayName`: имя метрики в интерфейсе пользователя. Включено по умолчанию. * `description`: краткое описание метрики. Включено по умолчанию. * `unit`: единица измерения метрики. Включено по умолчанию. * `tags`: теги метрики.  * `dduBillable`: индикатор того, потребляет ли использование метрики [Davis data units](https://dt-url.net/ddu?dt=m). Устарело и всегда `false` для Dynatrace Platform Subscription. Заменено на `billable`. * `billable`: индикатор того, тарифицируется ли использование метрики.  * `created`: метка времени (UTC миллисекунды) создания метрики. * `lastWritten`: метка времени (UTC миллисекунды) последней записи точек данных метрики. * `aggregationTypes`: список допустимых агрегаций для метрики. Учтите, что он может отличаться после применения [трансформации](https://dt-url.net/metricSelector?dt=m). * `defaultAggregation`: агрегация метрики по умолчанию. Используется, когда агрегация не задана или установлена трансформация `:auto`. * `dimensionDefinitions`: детальное деление метрики (например, группа процессов и ID процесса для некоторых метрик, связанных с процессами). * `transformations`: список [трансформаций](https://dt-url.net/metricSelector?dt=m), которые можно применить к метрике. * `entityType`: список типов сущностей, поддерживаемых метрикой. * `minimumValue`: минимально допустимое значение метрики. * `maximumValue`: максимально допустимое значение метрики. * `rootCauseRelevant`: связана ли (true или false) метрика с первопричиной проблемы. Метрика, релевантная для первопричины, представляет собой сильный индикатор неисправного компонента. * `impactRelevant`: релевантна ли (true или false) метрика для воздействия проблемы. Метрика, релевантная для воздействия, сильно зависит от других метрик и меняется, потому что изменилась нижележащая метрика-первопричина. * `metricValueType`: тип значения метрики. Возможные варианты: + `score`: метрика-оценка, где высокие значения указывают на хорошую ситуацию, а низкие на проблему. Пример такой метрики, процент успеха.   + `error`: метрика-ошибка, где высокие значения указывают на проблему, а низкие на хорошую ситуацию. Пример такой метрики, количество ошибок. * `latency`: задержка метрики, в минутах. Задержка, это ожидаемая задержка отчётности (например, вызванная ограничениями облачных провайдеров или других сторонних источников данных) между наблюдением точки данных метрики и её доступностью в Dynatrace. Допустимый диапазон значений: от `1` до `60` минут. * `metricSelector`: нижележащий селектор метрики, используемый метрикой func:. * `scalar`: указывает, разрешается ли выражение метрики в скаляр (`true`) или в серию (`false`).   Скалярный результат всегда содержит одну точку данных. Количество точек данных в серийном результате зависит от используемого разрешения. * `resolutionInfSupported`: если `true`, к запросу метрики можно применить resolution=Inf.  Чтобы добавить свойства, перечислите их с ведущим плюсом `+`. Чтобы исключить свойства по умолчанию, перечислите их с ведущим минусом `-`.  Чтобы указать несколько свойств, объедините их через запятую (например, `fields=+aggregationTypes,-description`).  Если указано только одно свойство, ответ содержит ключ метрики и указанное свойство. Чтобы вернуть только ключи метрик, укажите здесь `metricId`. | query | Необязательный |
| writtenSince | string | Фильтрует результирующий набор метрик до тех, у которых есть точки данных в указанном временном интервале.  Можно использовать один из следующих форматов:  * Метка времени в UTC миллисекундах. * Читаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Можно использовать пробел вместо `T`. Секунды и доли секунды необязательны. * Относительный интервал назад от текущего момента. Формат `now-NU/A`, где `N`, количество, `U`, единица времени, `A`, выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w`, это год назад, выровненный по неделе.   Можно указать относительный интервал и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы | query | Необязательный |
| writtenSinceMode | string | Управляет тем, как применяется фильтр writtenSince.  * `INCLUDE`: включает только метрики, которые были записаны после указанной метки времени writtenSince (отфильтровывает метрики, не записанные с этого момента). * `EXCLUDE`: исключает метрики, которые были записаны после указанной метки времени writtenSince (возвращает только метрики, не записанные с этого момента).  Если не указано, по умолчанию используется `INCLUDE`. | query | Необязательный |
| metadataSelector | string | Область метаданных запроса. В ответ включаются только метрики с указанными свойствами.  Можно задать один или несколько из следующих критериев. Значения регистрозависимы, используется оператор `EQUALS`. Если указано несколько значений, применяется логика **OR**.  * `unit("unit-1","unit-2")` * `tags("tag-1","tag-2")` * `dimensionKey("dimkey-1","dimkey-2")`. Фильтрация применяется только к измерениям, записанным за последние 14 дней. * `custom("true")`. "true", чтобы включить только пользовательские метрики (без namespace или с `ext:`, `calc:`, `func:`, `appmon:`), "false", чтобы их отфильтровать. * `exported("true")`. "true", чтобы включить только экспортированные метрики, "false", чтобы их отфильтровать.  Чтобы задать несколько критериев, разделяйте их запятой (`,`). Например, `tags("feature","cloud"),unit("Percent"),dimensionKey("location"),custom("true")`. В ответ включаются только результаты, соответствующие **всем** критериям.  Например, чтобы получить метрики с тегами **feature** И **cloud** с единицей измерения **Percent** ИЛИ **MegaByte** И измерением с ключом измерения **location**, используйте такой **metadataSelector**: `tags("feature"),unit("Percent","MegaByte"),tags("cloud"),dimensionKey("location")`. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MetricDescriptorCollection](#openapi-definition-MetricDescriptorCollection) | Успех |
| **400** | - | Синтаксическая ошибка или ошибка валидации. В **metricSelector** или **fields** есть синтаксические или семантические ошибки. |
| **404** | - | Метрика не найдена. |
| **406** | - | Not acceptable. Запрошенный тип медиа не поддерживается. Проверьте заголовок **Accept** в запросе. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `MetricDescriptorCollection`

Список метрик вместе с их дескрипторами.

| Поле | Тип | Описание |
| --- | --- | --- |
| metrics | [MetricDescriptor[]](#openapi-definition-MetricDescriptor) | Список метрик вместе с их дескрипторами |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения следующих страниц результата. |
| totalCount | integer | Оценочное количество метрик в результате. |
| warnings | string[] | Список потенциальных предупреждений о запросе. Например, использование устаревшей функциональности и т. п. |

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



"metrics": [



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



"metricId": "builtin:host.cpu.user:splitBy(\"dt.entity.host\"):max:fold",



"metricValueType": {



"type": "unknown"



},



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



},



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



"metricId": "builtin:host.cpu.user:splitBy()",



"metricValueType": {



"type": "unknown"



},



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



],



"nextPageKey": "ABCDEFABCDEFABCDEF_",



"totalCount": 3



}
```

## Пример

В этом примере запрос запрашивает все встроенные метрики (**metricSelector** установлен в `builtin:*`), доступные в окружении **mySampleEnv**. В ответ включены следующие поля:

* metricId
* unit
* aggregationTypes

Для этого query-параметр **fields** установлен в `unit,aggregationTypes`.

API-токен передаётся в заголовке **Authorization**.

Ответ в формате `application/json` и усечён до четырёх записей.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=unit,aggregationTypes&metricSelector=builtin:*' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Accept: application/json'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/metrics?fields=unit,aggregationTypes&metricSelector=builtin:*
```

#### Тело ответа

```
{



"totalCount": 1808,



"nextPageKey": "___a7acX3q0AAAAGAQAJYnVpbHRpbjoqAQA",



"metrics": [



{



"metricId": "builtin:host.cpu.idle",



"unit": "Percent",



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



]



},



{



"metricId": "builtin:host.cpu.load",



"unit": "Ratio",



"aggregationTypes": [



"auto",



"avg",



"max",



"min"



]



},



{



"metricId": "builtin:service.errors.server.count",



"unit": "Count",



"aggregationTypes": [



"auto",



"value"



]



},



{



"metricId": "builtin:service.keyRequest.count.client",



"unit": "Count",



"aggregationTypes": [



"auto",



"value"



]



}



]



}
```

CSV-таблица со строкой заголовка выглядит так. Чтобы получить её, измените заголовок **Accept** на `text/csv; header=present`.

```
metricId,unit,aggregationTypes



builtin:host.cpu.idle,Percent,"[auto, avg, max, min]"



builtin:host.cpu.load,Ratio,"[auto, avg, max, min]"



builtin:service.errors.server.count,Count,"[auto, value]"



builtin:service.keyRequest.count.client,Count,"[auto, value]"
```

#### Код ответа

200