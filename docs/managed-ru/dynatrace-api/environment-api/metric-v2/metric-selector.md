---
title: Metrics API - Metric selector
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/metric-selector
scraped: 2026-05-12T11:12:04.270625
---

# Metrics API - Metric selector

# Metrics API - Metric selector

* Справочник
* Обновлено 31 октября 2025 г.

Metric selector, это мощный инструмент для указания того, какие метрики вы хотите читать через запрос [GET metric data points](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Читайте точки данных одной или нескольких метрик через Metrics v2 API.") или в [**Advanced mode** Data Explorer](/managed/analyze-explore-automate/explorer/explorer-advanced-query-editor "Создавайте продвинутые запросы с помощью advanced mode Data Explorer.").

Кроме того, можно трансформировать результирующий набор точек данных. Эти трансформации изменяют исходные данные метрики.

Даже если вы строите селектор для использования в API-вызове, рекомендуем создавать запрос на вкладке **Code** в Data Explorer, которая предлагает встроенные инструменты (например, автодополнение), помогающие построить запрос.

## Ограничения

* Селектор должен содержать как минимум один ключ метрики.
* За один запрос можно запросить точки данных до 10 метрик.

## Измерения метрики

Многие метрики Dynatrace можно адресовать с более тонкой детализацией с помощью измерений. Например, метрика **builtin:host.disk.avail** имеет два измерения:

* Первичное измерение: **Host**
* Вторичное измерение: **Disk**

Запросите метрику вызовом [GET metric descriptor](/managed/dynatrace-api/environment-api/metric-v2/get-descriptor "Просмотрите дескриптор метрики через Metrics v2 API."), чтобы получить информацию о доступных измерениях: их можно найти в поле **dimensionDefinitions** дескриптора метрики.

Показать пример дескриптора

```
{



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"displayName": "Host",



"index": 0,



"type": "ENTITY"



},



{



"key": "dt.entity.disk",



"name": "Disk",



"displayName": "Disk",



"index": 1,



"type": "ENTITY"



}



]



}
```

Везде, где в примере синтаксиса вы видите плейсхолдер `<dimension>`, можно выбрать конкретное измерение метрики. На измерение можно ссылаться по его ключу. Например, для **builtin:host.disk.avail** это **dt.entity.host** и **dt.entity.disk**.

Операции трансформации изменяют список измерений, добавляя или удаляя их. Последующие трансформации работают с изменённым списком измерений. Запросите дескриптор метрики с предшествующими трансформациями (например, **builtin:host.disk.avail:names**), чтобы увидеть новый список доступных измерений.

### Измерение-остаток

Dynatrace хранит только топ X кортежей измерений (точное число зависит от метрики, агрегации, временного интервала и других факторов). Все остальные кортежи измерений агрегируются в один, называемый измерением-*остатком* (remainder).

Если результат запроса включает это измерение, значения `dimensions` и `dimensionMap` будут `null`. Однако если запись в `dimensionMap` вообще отсутствует, то это не измерение-остаток, а буквальное значение `null`.

## Агрегация по времени

Объём сырых данных, доступных в Dynatrace, затрудняет осмысленное представление данных. Чтобы улучшить читаемость, Dynatrace применяет агрегацию по времени, выравнивая данные по временным слотам. Метод агрегации можно задать через [трансформацию **aggregation**](#aggregation).

Даже если вы не указываете никакой трансформации агрегации, какая-то агрегация всё равно применяется, используя *трансформацию по умолчанию* метрики. Применение трансформации `auto` даёт тот же эффект.

Доступные агрегации различаются для каждой метрики. Проверить доступные агрегации (и агрегацию по умолчанию) можно через вызов [GET metric descriptor](/managed/dynatrace-api/environment-api/metric-v2/get-descriptor "Просмотрите дескриптор метрики через Metrics v2 API."), посмотрев поля **aggregationTypes** и **defaultAggregation**.

Разрешение результирующего временного ряда зависит от таких факторов, как временной интервал запроса и возраст данных. В некоторой степени разрешением можно управлять через query-параметр **resolution** запроса [GET metric data points](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Читайте точки данных одной или нескольких метрик через Metrics v2 API."). Наилучшее доступное разрешение: одна минута. Кроме того, можно агрегировать все точки данных временного ряда в одну точку данных, для этого используйте [трансформацию **fold**](#fold).

#### Пример

Чтобы проиллюстрировать агрегации по времени, рассмотрим пример метрики **CPU usage** (`builtin:host.cpu.usage`).

Показать дескриптор метрики

```
{



"metricId": "builtin:host.cpu.usage",



"displayName": "CPU usage %",



"description": "Percentage of CPU time currently utilized.",



"unit": "Percent",



"dduBillable": false,



"created": 0,



"lastWritten": 1668607995463,



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



"limit",



"merge",



"names",



"parents",



"timeshift",



"sort",



"last",



"splitBy",



"lastReal",



"setUnit"



],



"defaultAggregation": {



"type": "avg"



},



"dimensionDefinitions": [



{



"key": "dt.entity.host",



"name": "Host",



"displayName": "Host",



"index": 0,



"type": "ENTITY"



}



],



"tags": [],



"metricValueType": {



"type": "unknown"



},



"scalar": false,



"resolutionInfSupported": true



}
```

Поскольку её трансформация по умолчанию `avg`, если вы запросите точки данных без применения какой-либо агрегации, вы получите среднее использование CPU для каждого временного слота результирующего временного ряда.

Чтобы получить максимальное использование CPU на временной слот, используйте селектор ниже.

```
builtin:host.cpu.usage:max
```

Если вам нужно единственное наибольшее использование за временной интервал, можно применить трансформацию fold.

```
builtin:host.cpu.usage:fold(max)
```

## Агрегация по пространству

Каждая метрика может нести множество временных рядов для различных измерений. Агрегация по пространству облегчает доступ к интересующим вас измерениям, объединяя всё остальное вместе.

#### Пример

Рассмотрим пример метрики **Session count - estimated** (`builtin:apps.other.sessionCount.osAndGeo`).

Показать дескриптор метрики

```
{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names",



"displayName": "Session count - estimated (by OS, geolocation) [mobile, custom]",



"description": "",



"unit": "Count",



"dduBillable": false,



"created": 0,



"lastWritten": 1668609851154,



"entityType": [



"CUSTOM_APPLICATION",



"MOBILE_APPLICATION"



],



"aggregationTypes": [



"auto",



"value"



],



"transformations": [



"filter",



"fold",



"limit",



"merge",



"names",



"parents",



"timeshift",



"sort",



"last",



"splitBy",



"lastReal",



"setUnit"



],



"defaultAggregation": {



"type": "value"



},



"dimensionDefinitions": [



{



"key": "dt.entity.device_application.name",



"name": "dt.entity.device_application.name",



"displayName": "dt.entity.device_application.name",



"index": 0,



"type": "STRING"



},



{



"key": "dt.entity.device_application",



"name": "Application",



"displayName": "Mobile or custom application",



"index": 1,



"type": "ENTITY"



},



{



"key": "dt.entity.os.name",



"name": "dt.entity.os.name",



"displayName": "dt.entity.os.name",



"index": 2,



"type": "STRING"



},



{



"key": "dt.entity.os",



"name": "Operating system",



"displayName": "OS",



"index": 3,



"type": "ENTITY"



},



{



"key": "dt.entity.geolocation.name",



"name": "dt.entity.geolocation.name",



"displayName": "dt.entity.geolocation.name",



"index": 4,



"type": "STRING"



},



{



"key": "dt.entity.geolocation",



"name": "Geolocation",



"displayName": "Geolocation",



"index": 5,



"type": "ENTITY"



}



],



"tags": [],



"metricValueType": {



"type": "unknown"



},



"scalar": false,



"resolutionInfSupported": true,



"warnings": [



"The field dimensionCardinalities is only supported for untransformed single metric keys and was ignored."



]



}
```

Метрика разбивает временной ряд по приложению, операционной системе и географическому расположению. Если вы хотите исследовать данные для конкретного приложения независимо от ОС и расположения, можно применить [трансформацию **splitBy**](#splitby), как показано ниже.

```
builtin:apps.other.sessionCount.osAndGeo:splitBy("dt.entity.device_application")
```

Можно даже объединить все измерения в одно, опустив аргумент трансформации. Снова рассмотрим метрику **CPU usage** (`builtin:host.cpu.usage`). В примере ниже трансформация объединяет измерения всех ваших хостов в один временной ряд.

```
builtin:host.cpu.usage:splitBy()
```

### Фильтрация данных

Ещё один способ сузить вывод данных: применить [трансформацию **filter**](#filter). Например, можно фильтровать временные ряды на основе определённого порога, подробности смотрите в описании [условия `series`](#series-condition).

В сочетании с агрегацией по пространству можно строить мощные селекторы, как тот, что ниже, который читает максимальное число подов для Kubernetes-кластера `preproduction` с разбивкой по облачному приложению.

```
builtin:kubernetes.pods



:filter(eq("k8s.cluster.name","preproduction"))



:splitBy("dt.entity.cloud_application")



:max
```

Также можно фильтровать данные на основе отслеживаемых сущностей, используя возможности entity selector. Селектор ниже читает использование CPU для всех хостов, у которых есть тег `easyTravel`.

```
builtin:host.cpu.usage



:filter(



in(



"dt.entity.host",entitySelector("type(~"HOST~"),tag(~"easyTravel~")")



)



)
```

## Как использовать metric selector

### Выбор метрик

Чтобы получить временной ряд для метрики, нужно указать её ключ. Можно также указать несколько ключей метрик через запятую (например, `metrickey1,metrickey2`).

При использовании [data explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных инсайтов.") секции ключа метрики, начинающиеся со специальных символов, нужно экранировать кавычками (`""`). Например,

| Принятая метрика | Пример metric selector |
| --- | --- |
| custom.http5xx | `custom.http5xx:splitBy():auto` |
| custom.5xx\_errors | `custom."5xx_errors":splitBy():auto` |

### Применение трансформаций

После выбора метрики к её данным можно применять трансформации. Можно комбинировать любое количество трансформаций. Строка **metric selector** вычисляется слева направо. Каждая последующая трансформация применяется к результату предыдущей трансформации. Рассмотрим пример:

```
builtin:host.cpu.user:sort(value(max,descending)):limit(10)
```

Этот селектор запрашивает данные для метрики **builtin:host.cpu.usage**, сортирует результаты по максимальному использованию CPU и возвращает ряды для топ-10 хостов.

Dynatrace предоставляет богатый набор трансформаций для манипуляции точками данных рядов в соответствии с вашими потребностями. Ниже приведён список всех доступных трансформаций, которые предлагает metric selector.

## Трансформация aggregation

|  |  |
| --- | --- |
| Синтаксис | `:<aggregation>` |
| Аргумент | Желаемая агрегация. |

Указывает агрегацию возвращаемых точек данных. Доступны следующие типы агрегации:

| Синтаксис | Описание |
| --- | --- |
| `:auto` | Применяет агрегацию по умолчанию. Чтобы проверить агрегацию по умолчанию, запросите метрику вызовом [GET metric descriptors](/managed/dynatrace-api/environment-api/metric-v2/get-descriptor "Просмотрите дескриптор метрики через Metrics v2 API.") и посмотрите поле **defaultAggregation**. |
| `:avg` | Вычисляет среднее арифметическое всех значений из временного слота. Все значения `null` игнорируются. |
| `:count` | Берёт количество значений во временном слоте. Все значения `null` игнорируются. |
| `:histogram` | Раскрывает корзины метрики-гистограммы как измерения. Значение измерения `le` обозначает верхнюю границу (меньше или равно) каждой корзины. |
| `:max` | Выбирает наибольшее значение из временного слота. Все значения `null` игнорируются. |
| `:min` | Выбирает наименьшее значение из временного слота. Все значения `null` игнорируются. |
| `:percentile(99.9)` | Вычисляет N-й процентиль, где N от `0` до `100` (включительно). |
| `:sum` | Суммирует все значения из временного слота. Все значения `null` игнорируются. |
| `:value` | Берёт одно значение как есть. Применимо только к ранее агрегированным значениям и метрикам, поддерживающим агрегацию `value`. |

## Трансформация default

|  |  |
| --- | --- |
| Синтаксис | `:default(<number>, always)` |
| Аргументы | * Значение (число с плавающей точкой) для замены значений `null` в результате. * Необязательно Заменять ли пустой результат значениями по умолчанию. Этот аргумент действителен только если ему предшествует **пустая** [трансформация **splitBy**](#splitby). |

Трансформация **default** заменяет значения `null` в payload указанным значением.

Когда `always` не указано, предварительно трансформированный временной ряд должен иметь хотя бы одну точку данных, чтобы трансформация сработала; если у временного ряда нет ни одной точки данных, после трансформации он остаётся пустым.

Показать примеры

До трансформации default

После трансформации default

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.pool.collectionCount",



"data": [



{



"dimensions": [



"PROCESS_GROUP_INSTANCE-A02ED607B5E9DD20",



"30382",



"G1 Old Gen",



"G1 Old Generation"



],



"dimensionMap": {



"poolname": "G1 Old Gen",



"rx_pid": "30382",



"gcname": "G1 Old Generation",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-A02ED607B5E9DD20"



},



"timestamps": [1623585600000, 1623628800000, 1623672000000, 1623715200000],



"values": [3, null, null, 1]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.pool.collectionCount:default(0)",



"data": [



{



"dimensions": [



"PROCESS_GROUP_INSTANCE-A02ED607B5E9DD20",



"30382",



"G1 Old Gen",



"G1 Old Generation"



],



"dimensionMap": {



"poolname": "G1 Old Gen",



"rx_pid": "30382",



"gcname": "G1 Old Generation",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-A02ED607B5E9DD20"



},



"timestamps": [1623585600000, 1623628800000, 1623672000000, 1623715200000],



"values": [3, 0, 0, 1]



}



]



}



]



}
```

До трансформации default always

После трансформации default always

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.fivexx.count:splitBy():auto:default(0)",



"data": [],



"warnings": [



"The :default operator could not be applied as it requires at least one written data point for the metric in the query timeframe."



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.fivexx.count:splitBy():auto:default(0,always)",



"data": [



{



"dimensions": [],



"dimensionMap": {},



"timestamps": [1623585600000, 1623628800000, 1623672000000, 1623715200000],



"values": [0, 0, 0, 0]



}



]



}



]



}
```

## Трансформация delta

|  |  |
| --- | --- |
| Синтаксис | `:delta` |
| Аргументы | Нет |

Трансформация **delta** заменяет каждую точку данных разностью с предыдущей точкой данных (`0`, если разность отрицательна). Первая точка данных исходного набора исключается из результата.

Перед использованием трансформации delta необходимо применить [трансформацию агрегации](#aggregation).

Показать пример

До трансформации delta

После трансформации delta

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.keyRequest.count.server:value",



"data": [



{



"dimensions": ["SERVICE_METHOD-BD61DD6DAC1EFDE1"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-BD61DD6DAC1EFDE1"



},



"timestamps": [1630886400000, 1630929600000, 1630972800000, 1631016000000, 1631059200000],



"values": [8338, 8449, 8343, 8372, 8425]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.keyRequest.count.server:value:delta",



"data": [



{



"dimensions": ["SERVICE_METHOD-BD61DD6DAC1EFDE1"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-BD61DD6DAC1EFDE1"



},



"timestamps": [1630886400000, 1630929600000, 1630972800000, 1631016000000, 1631059200000],



"values": [null, 111, 0, 29, 53]



}



]



}



]



}
```

## Трансформация filter

|  |  |
| --- | --- |
| Синтаксис | `:filter(<condition1>,<condition2>,<conditionN>)` |
| Аргументы | Список условий фильтрации. [Измерение](#dimension) должно соответствовать **всем** условиям, чтобы пройти фильтрацию. |

Трансформация **filter** фильтрует ответ по указанным критериям. Она позволяет фильтровать точки данных по вторичному измерению, так как **entitySelector** поддерживает только первое измерение, которое является сущностью. Сочетание области и трансформации filter помогает максимизировать эффективность фильтрации данных.

### Условия

Трансформация `:filter` поддерживает следующие условия.

| Синтаксис | Описание |
| --- | --- |
| `prefix("<dimension>","<expected prefix>")` | Совпадает, если значение указанного измерения начинается с ожидаемого префикса. |
| `suffix("<dimension>","<expected suffix>")` | Совпадает, если значение указанного измерения заканчивается ожидаемым суффиксом. |
| `contains("<dimension>","<expected contained>")` | Совпадает, если значение указанного измерения содержит ожидаемое значение. |
| `eq("<dimension>","<expected value>")` | Совпадает, если значение указанного измерения равно ожидаемому значению. |
| `ne("<dimension>","<value to be excluded>")` | Обратное условию `eq`. Измерение с указанным именем *исключается* из ответа. |
| `in("<dimension>",entitySelector("<selector>")` | Совпадает, если значение указанного измерения равно *любому* из ожидаемых значений, предоставленных [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройте entity selector для endpoint-ов Environment API."). |
| `existsKey("<dimension>")` | Совпадает, если указанное измерение существует. |
| `remainder("<dimension>")` | Совпадает, если указанное измерение является частью [остатка](#remainder). |
| `series(<aggregation>,<operator>(<reference value>))` | Ответ содержит только ряды с точками данных, соответствующими предоставленному критерию. |

Кавычки (`"`) и тильды (`~`), входящие в состав ключа измерения или значения измерения (включая синтаксис entity selector), должны быть экранированы тильдой (`~`).

#### Условие series

Условие `series` фильтрует агрегированное по времени значение точек данных ряда по предоставленному критерию. То есть применяется указанная агрегация, а затем этот единственный результат сравнивается с эталонным значением с помощью указанного оператора.

Например, для `series(avg, gt(10))` сначала вычисляется среднее по всем точкам данных ряда, а затем это значение проверяется на то, больше ли оно 10. Если ряд не соответствует этому критерию, он удаляется из предоставленного результата. То есть оператор `series` нельзя использовать для фильтрации отдельных точек данных ряда. Чтобы фильтровать отдельные точки данных, нужно использовать [трансформацию **partition**](#partition).

Условие поддерживает следующие агрегации и операторы.

##### Доступные агрегации

* `count`
* `min`
* `max`
* `avg`
* `sum`
* `median`
* `percentile(N)`, где N в диапазоне от `0` до `100`.
* `value`

##### Доступные операторы

* `lt`: меньше чем
* `le`: меньше или равно
* `eq`: равно
* `ne`: не равно
* `gt`: больше чем
* `ge`: больше или равно

### Составное условие

Каждое условие может быть комбинацией подусловий.

| Синтаксис | Описание |
| --- | --- |
| `and(<subcondition1>,<subcondition2>,<subconditionN>)` | Должны выполняться **все** подусловия. |
| `or(<subcondition1>,<subcondition2>,<subconditionN>)` | Должно выполняться **хотя бы одно** подусловие. |
| `not(<subcondition>)` | Инвертирует подусловие. Например, превращает **contains** в **не содержит**. |

### Примеры синтаксиса

```
:filter(or(eq("k8s.cluster.name","Server ~"North~""),eq("k8s.cluster.name","Server ~"West~"")))
```

Фильтрует точки данных до доставленных либо **Server "North"**, либо **Server "West"**.

```
:filter(and(prefix("App Version","2."),ne("dt.entity.os","OS-472A4A3B41095B09")))
```

Фильтрует точки данных до доставленных приложением мажорной версии **2**, которое не работает на операционной системе **OS-472A4A3B41095B09**.

## Трансформация fold

|  |  |
| --- | --- |
| Синтаксис | `:fold(<aggregation>)` |
| Аргументы | Необязательно Требуемый метод [агрегации](#aggregation). |

Трансформация **fold** объединяет список точек данных в одну точку данных. Чтобы получить результат в конкретной агрегации, укажите агрегацию в качестве аргумента. Если указанная агрегация не поддерживается, используется агрегация по умолчанию. Например, `:fold(median)` для метрики-датчика равно `:fold(avg)`, потому что median не поддерживается, а avg по умолчанию. Если агрегация уже была применена ранее в цепочке трансформаций, аргумент игнорируется.

Показать пример

До трансформации fold

После трансформации fold

```
{



"metricId": "builtin:host.disk.avail",



"data": [



{



"dimensions": ["HOST-BB4DF8969CB41C60", "DISK-FB78447211EE76BF"],



"dimensionMap": {



"dt.entity.disk": "DISK-FB78447211EE76BF",



"dt.entity.host": "HOST-BB4DF8969CB41C60"



},



"timestamps": [1612794060000, 1612794120000, 1612794180000],



"values": [4.605786630826667e11, 4.424691002026667e11, 439596351488]



}



]



}
```

```
{



"metricId": "builtin:host.disk.avail:fold",



"data": [



{



"dimensions": ["HOST-BB4DF8969CB41C60", "DISK-FB78447211EE76BF"],



"dimensionMap": {



"dt.entity.disk": "DISK-FB78447211EE76BF",



"dt.entity.host": "HOST-BB4DF8969CB41C60"



},



"timestamps": [1612794480000],



"values": [4.577198298453333e11]



}



]



}
```

## Трансформация last

|  |  |
| --- | --- |
| Синтаксис | `:last<aggregation>` `:lastReal<aggregation>` |
| Аргументы | Необязательно Требуемый метод [агрегации](#aggregation). |

Трансформация **last** возвращает самую свежую точку данных из временного интервала запроса. Чтобы получить результат в конкретной агрегации, укажите агрегацию в качестве аргумента. Если указанная агрегация не поддерживается, используется агрегация по умолчанию. Например, `:last(median)` для метрики-датчика равно `:last(avg)`, потому что median не поддерживается, а avg по умолчанию. Если агрегация уже была применена ранее в цепочке трансформаций, аргумент игнорируется.

Если метрика перед трансформацией содержит несколько кортежей (уникальные сочетания «метрика-измерение-значение измерения»), для всех кортежей применяется самая свежая метка времени. Чтобы получить фактическую последнюю метку времени, используйте оператор `lastReal`.

Показать пример

До трансформации last

После трансформации last

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\")",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [



1617178800000, 1617180000000, 1617181200000, 1617182400000, 1617183600000, 1617184800000



],



"values": [90, 106, 110, 96, 116, 102]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [



1617178800000, 1617180000000, 1617181200000, 1617182400000, 1617183600000, 1617184800000



],



"values": [176, 168, 178, 174, 183, 172]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [



1617178800000, 1617180000000, 1617181200000, 1617182400000, 1617183600000, 1617184800000



],



"values": [1168, 1121, 1154, 1160, 1108, 1135]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\"):last",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1617184800000],



"values": [102]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1617184800000],



"values": [172]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [1617184800000],



"values": [1135]



}



]



}



]



}
```

## Трансформация limit

|  |  |
| --- | --- |
| Синтаксис | `:limit(2)` |
| Аргумент | Максимальное количество кортежей в результате. |

Трансформация **limit** ограничивает количество кортежей (уникальные сочетания «метрика-измерение-значение измерения») в ответе. В ответ включаются только первые X кортежей; остальные отбрасываются.

Чтобы гарантировать, что нужные кортежи находятся вверху результата, примените [трансформацию **sort**](#sort) перед использованием limit.

Показать пример

До трансформации limit

После трансформации limit

```
{



"totalCount": 4,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\"):sort(value(sum,descending))",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1613559180000],



"values": [6593]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1613559180000],



"values": [1002]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [1613559180000],



"values": [564]



}



]



}



]



}
```

```
{



"totalCount": 2,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\"):sort(value(sum,descending)):limit(2)",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1613559180000],



"values": [6593]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1613559180000],



"values": [1002]



}



]



}



]



}
```

## Трансформация merge

|  |  |
| --- | --- |
| Синтаксис | `:merge("<dimension0>","<dimension1>","<dimensionN>")` |
| Аргументы | Список [измерений](#dimension) для удаления. Измерение должно быть указано по своему ключу.  Кавычки (`"`) и тильды (`~`), входящие в состав ключа измерения, должны быть экранированы тильдой (`~`). |

Трансформация **merge** удаляет указанные измерения из результата. Все ряды/значения, у которых после удаления одинаковые измерения, объединяются в один. Значения пересчитываются в соответствии с выбранной агрегацией.

К результату трансформации **merge** можно применить любую агрегацию, включая те, которые исходная метрика не поддерживает.

Показать пример

До трансформации merge

После трансформации merge

```
{



"totalCount": 2,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:synthetic.browser.event.actionDuration.load.geo:count",



"data": [



{



"dimensions": ["SYNTHETIC_TEST_STEP-002D5D5A0230A18F", "GEOLOCATION-B69A5A40388CC698"],



"dimensionMap": {



"dt.entity.synthetic_test_step": "SYNTHETIC_TEST_STEP-97EF148D63564F29",



"dt.entity.geolocation": "GEOLOCATION-0A41430434C388A9"



},



"timestamps": [1559865600000, 1560124800000, 1560384000000],



"values": [143, 156, 217]



},



{



"dimensions": ["SYNTHETIC_TEST_STEP-002D5D5A0230A18F", "GEOLOCATION-43BA84CAB24D7950"],



"timestamps": [1559865600000, 1560124800000, 1560384000000],



"values": [773, 804, 801]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:synthetic.browser.event.actionDuration.load.geo:count:merge(\"dt.entity.geolocation\")",



"data": [



{



"dimensions": ["SYNTHETIC_TEST_STEP-002D5D5A0230A18F"],



"dimensionMap": {



"dt.entity.synthetic_test_step": "SYNTHETIC_TEST_STEP-09D1E2CC97B5878B"



},



"timestamps": [1559865600000, 1560124800000, 1560384000000],



"values": [916, 960, 1018]



}



]



}



]



}
```

## Трансформация names

|  |  |
| --- | --- |
| Синтаксис | `:names` |
| Аргументы | Нет |
| Ограничения | Применяется только к измерениям типа сущность. |

Трансформация **names** добавляет имя [значения измерения](#dimension) в массив **dimensions** и объект **dimensionMap** ответа. Имя каждого измерения помещается перед **ID** измерения.

Показать пример

До трансформации names

После трансформации names

```
{



"dimensions": ["HOST-BB4DF8969CB41C60", "DISK-FB78447211EE76BF"],



"dimensionMap": {



"dt.entity.disk": "DISK-FB78447211EE76BF",



"dt.entity.host": "HOST-BB4DF8969CB41C60"



}



}
```

```
{



"dimensions": ["l-009", "HOST-BB4DF8969CB41C60", "C:\\", "DISK-FB78447211EE76BF"],



"dimensionMap": {



"dt.entity.disk.name": "C:\\",



"dt.entity.disk": "DISK-FB78447211EE76BF",



"dt.entity.host.name": "l-009",



"dt.entity.host": "HOST-BB4DF8969CB41C60"



}



}
```

## Трансформация parents

|  |  |
| --- | --- |
| Синтаксис | `:parents` |
| Аргументы | Нет |
| Ограничения | Применяется только к измерениям типа сущность из перечисленных ниже. |

Трансформация **parents** добавляет родителя [измерения](#dimension) в массив **dimensions** и объект **dimensionMap** ответа. Родитель каждого измерения помещается перед самим измерением.

Эта трансформация работает только если сущность измерения является частью другой, более крупной сущности. Например, `PROCESS_GROUP_INSTANCE` всегда является дочерней по отношению к `HOST`, на котором он работает. Поддерживаются следующие связи.

| Дочернее измерение | Родительское измерение |
| --- | --- |
| SERVICE\_METHOD | SERVICE |
| SERVICE\_INSTANCE | SERVICE |
| APPLICATION\_METHOD | APPLICATION |
| PROCESS\_GROUP\_INSTANCE | HOST |
| DISK | HOST |
| NETWORK\_INTERFACE | HOST |
| SYNTHETIC\_TEST\_STEP | SYNTHETIC\_TEST |
| HTTP\_CHECK\_STEP | HTTP\_CHECK |
| EXTERNAL\_SYNTHETIC\_TEST\_STEP | EXTERNAL\_SYNTHETIC\_TEST |

Показать пример

До трансформации parents

После трансформации parents

```
{



"dimensions": ["SERVICE_METHOD-D9D3A16FA577BF1C"],



"dimensionMap": {



"dt.entity.service": "SERVICE-C22F1E8EA66FF4C5"



}



}
```

```
{



"dimensions": ["SERVICE-C22F1E8EA66FF4C5", "SERVICE_METHOD-D9D3A16FA577BF1C"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-D9D3A16FA577BF1C",



"dt.entity.service": "SERVICE-C22F1E8EA66FF4C5"



}



}
```

## Трансформация partition

|  |  |
| --- | --- |
| Синтаксис | `:partition("<partition dimension key>",<partition1>,<partitionN>)` |
| Аргументы | * Ключ измерения-раздела, это **не** существующее измерение, а новое, которое создаст трансформация.  Кавычки (`"`) и тильды (`~`), входящие в состав ключа измерения, должны быть экранированы тильдой (`~`). * Список применяемых разделов, как их задать, смотрите в разделе [Синтаксис partition](#partition-syntax) ниже. |

Трансформация **partition** разбивает точки данных ряда на основе указанных критериев. Она вводит новое измерение (измерение-раздел) со значением, определяемым критерием раздела. Точки данных из исходного ряда распределяются между одним или несколькими новыми рядами в соответствии с критериями раздела. В каждом новом ряду точки данных, не прошедшие критерий или уже взятые другим критерием, заменяются на `null`.

### Синтаксис partition

Одна трансформация может содержать несколько разделов. Они вычисляются сверху вниз; применяется первый совпавший раздел.

Каждый раздел должен содержать значение для измерения-раздела, которое будет помечать прошедшие точки данных, и критерий, по которому фильтровать точки данных.

Учтите, что в одном операторе partition можно использовать либо условие `value`, либо условие `dimension`, но не оба сразу. Условия `otherwise` можно использовать всегда.

#### Условия value

Перед использованием условий value внутри трансформации partition необходимо применить [трансформацию агрегации](#aggregation).

```
value("<partition dimension value>",<criterion>)
```

Доступны следующие критерии:

| Синтаксис | Описание |
| --- | --- |
| `lt(X)` | Меньше X |
| `le(X)` | Меньше или равно X |
| `eq(X)` | Равно X |
| `ne(X)` | Не равно X |
| `ge(X)` | Больше или равно X |
| `gt(X)` | Больше X |
| `range(X,Y)` | Больше или равно X и меньше Y |
| `or(<criterion1>,<criterionN>)` | Должен выполняться хотя бы один подкритерий. |
| `and(<criterion1>,<criterionN>)` | Должны выполняться все подкритерии. |
| `not(<criterion>)` | Инвертированный критерий, совпадающий со всеми значениями, которые **не** выполняют критерий |

#### Условия dimension

```
dimension("<partition dimension value>",<criterion>)
```

Доступны следующие критерии.

| Синтаксис | Описание |
| --- | --- |
| `prefix("<dimension>","<expected prefix>")` | Совпадает, если значение указанного измерения начинается с ожидаемого префикса. |
| `suffix("<dimension>","<expected suffix>")` | Совпадает, если значение указанного измерения заканчивается ожидаемым суффиксом. |
| `contains("<dimension>","<expected contained>")` | Совпадает, если значение указанного измерения содержит ожидаемое значение. |
| `eq("<dimension>","<expected value>")` | Совпадает, если значение указанного измерения равно ожидаемому значению. |
| `ne("<dimension>","<value to be excluded>")` | Обратное условию `eq`, измерение с указанным именем **исключается** из ответа. |
| `or(<criterion1>,<criterionN>)` | Должен выполняться хотя бы один подкритерий. |
| `and(<criterion1>,<criterionN>)` | Должны выполняться все подкритерии. |
| `not(<criterion>)` | Инвертированный критерий, совпадающий со всеми значениями, которые **не** выполняют критерий |

#### Условие otherwise

```
otherwise("<partition dimension value>")
```

Универсальный оператор, совпадающий со всеми значениями, используйте его в конце цепочки разделов как случай по умолчанию.

Показать пример

В этом примере используется следующая трансформация partition.

```
:partition(



"Action duration",



value("slow",gt(200)),



value("fast",lt(100)),



value("normal",otherwise)



)
```

Она добавляет измерение **Action duration** к метрике и разбивает точки данных на три категории на его основе.

* `fast` для действий быстрее `100` миллисекунд
* `slow` для действий медленнее `200` миллисекунд
* `normal` для всех остальных действий

До трансформации partition

После трансформации partition

```
{



"totalCount": 1,



"nextPageKey": null,



"resolution": "10m",



"result": [



{



"metricId": "builtin:apps.web.action.domInteractive.load.browser:avg",



"data": [



{



"dimensions": ["APPLICATION_METHOD-E418A4BC1DC2C911", "BROWSER-EFB8A292CB368A8D"],



"dimensionMap": {



"dt.entity.browser": "BROWSER-EFB8A292CB368A8D",



"dt.entity.application_method": "APPLICATION_METHOD-E418A4BC1DC2C911"



},



"timestamps": [



1637152200000, 1637152800000, 1637153400000, 1637154000000, 1637154600000,



1637155200000, 1637155800000, 1637156400000, 1637157000000, 1637157600000,



1637158200000, 1637158800000, 1637159400000



],



"values": [155, 215, 247, 118, 94, 119, 67, 159, 114, 169, 113, 75, 160]



}



]



}



]



}
```

```
{



"totalCount": 3,



"nextPageKey": null,



"resolution": "10m",



"result": [



{



"metricId": "builtin:apps.web.action.domInteractive.load.browser:avg:partition(\"Action duration\",value(slow,gt(200)),value(fast,lt(100)),value(normal,otherwise))",



"data": [



{



"dimensions": [



"BROWSER-EFB8A292CB368A8D",



"APPLICATION_METHOD-E418A4BC1DC2C911",



"normal"



],



"dimensionMap": {



"dt.entity.browser": "BROWSER-EFB8A292CB368A8D",



"dt.entity.application_method": "APPLICATION_METHOD-E418A4BC1DC2C911",



"Action duration": "normal"



},



"timestamps": [



1637152200000, 1637152800000, 1637153400000, 1637154000000, 1637154600000,



1637155200000, 1637155800000, 1637156400000, 1637157000000, 1637157600000,



1637158200000, 1637158800000, 1637159400000



],



"values": [155, null, null, 118, null, 119, null, 159, 114, 169, 113, null, 160]



},



{



"dimensions": ["BROWSER-EFB8A292CB368A8D", "APPLICATION_METHOD-E418A4BC1DC2C911", "fast"],



"dimensionMap": {



"dt.entity.browser": "BROWSER-EFB8A292CB368A8D",



"dt.entity.application_method": "APPLICATION_METHOD-E418A4BC1DC2C911",



"Action duration": "fast"



},



"timestamps": [



1637154000000, 1637154600000, 1637155200000, 1637155800000, 1637156400000,



1637157000000, 1637157600000, 1637158200000, 1637158800000, 1637159400000,



1637160000000, 1637160600000, 1637161200000



],



"values": [null, null, null, null, 94, null, 67, null, null, null, null, 75, null]



},



{



"dimensions": ["BROWSER-EFB8A292CB368A8D", "APPLICATION_METHOD-E418A4BC1DC2C911", "slow"],



"dimensionMap": {



"dt.entity.browser": "BROWSER-EFB8A292CB368A8D",



"dt.entity.application_method": "APPLICATION_METHOD-E418A4BC1DC2C911",



"Action duration": "slow"



},



"timestamps": [



1637154000000, 1637154600000, 1637155200000, 1637155800000, 1637156400000,



1637157000000, 1637157600000, 1637158200000, 1637158800000, 1637159400000,



1637160000000, 1637160600000, 1637161200000



],



"values": [null, 215, 247, null, null, null, null, null, null, null, null, null, null]



}



]



}



]



}
```

## Трансформация rate

|  |  |
| --- | --- |
| Синтаксис | `:rate(5m)` |
| Аргумент | База ставки. Поддерживаются следующие значения:  `s`: в секунду  `m`: в минуту  `h`: в час  `d`: в день  `w`: в неделю  `M`: в месяц  `y`: в год |

Трансформация **rate** конвертирует метрику на основе счётчика (например, байты) в метрику на основе ставки (например, байты в минуту).

Любой аргумент можно изменить целочисленным множителем. Например, `5m` означает ставку **за 5 минут**. Если аргумент не указан, используется ставка **за 1 минуту**.

Трансформацию rate можно использовать с любой метрикой, поддерживающей агрегацию `VALUE`. Запросите метрику вызовом [GET metric descriptors](/managed/dynatrace-api/environment-api/metric-v2/get-descriptor "Просмотрите дескриптор метрики через Metrics v2 API."), чтобы получить информацию о доступных агрегациях. Если метрика не поддерживает агрегацию `VALUE`, сначала примените [трансформацию агрегации](#aggregation), а затем трансформацию rate.

* Перед использованием трансформации rate необходимо применить [трансформацию агрегации](#aggregation).
* Трансформацию rate можно использовать только один раз в одной цепочке трансформаций.

## Трансформация rollup

|  |  |
| --- | --- |
| Синтаксис | `:rollup(avg,15m)` |
| Аргументы | * Требуемая агрегация rollup. Поддерживаемые агрегации: + `avg`   + `count`   + `max`   + `median`   + `min`   + `percentile(N)`, где N в диапазоне от `0` до `100`.   + `sum`   + `value` * Длительность окна rollup в минутах. Длительность должна быть кратна разрешению запроса. Например, если разрешение пять минут, rollup может быть `5m`, `10m`, `15m` и так далее. |

Трансформация **rollup** сглаживает точки данных, убирая любые всплески из запрашиваемого временного интервала.

Трансформация берёт каждую точку данных из временного интервала запроса, формирует окно rollup, заглядывая в прошлые точки данных (так что исходная точка данных становится *последней* точкой окна), вычисляет требуемую агрегацию всех исходных значений, а затем заменяет каждую точку данных в окне результатом вычисления.

Например, если вы укажете `:rollup(avg,5m)`, а разрешение запроса одна минута, трансформация берёт точку данных, добавляет четыре предыдущие точки данных, чтобы сформировать окно rollup, а затем использует среднее этих пяти точек данных для вычисления итогового значения точки данных.

Ограничения

* Перед использованием трансформации rollup необходимо применить [трансформацию агрегации](#aggregation).
* Длительность окна rollup ограничена **60 минутами**.
* Делать rollup можно только для данных за последние **2 недели** (включая окна rollup). То есть самая старая точка данных вашего запроса не может быть в прошлом дальше, чем `2w-windowDuration`.

Показать пример

До трансформации rollup

После трансформации rollup

![Трансформация rollup - до](https://dt-cdn.net/images/rollup-before-872-84448811b4.png)

Трансформация rollup - до

![Трансформация rollup - после](https://dt-cdn.net/images/rollup-after-876-3776eb8906.png)

Трансформация rollup - после

## Трансформация smooth

|  |  |
| --- | --- |
| Синтаксис | `:smooth(skipfirst)` |
| Аргумент | Стратегия сглаживания. Поддерживается только стратегия `skipfirst`. |

Трансформация **smooth** сглаживает ряд точек данных после пропуска данных (одна или несколько точек данных со значением `null`).

Стратегия `skipfirst` заменяет первую точку данных после пропуска данных на `null`.

Показать пример

До трансформации smooth

После трансформации smooth

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.keyRequest.count.server",



"data": [



{



"dimensions": ["SERVICE_METHOD-BBA9C77B774B0C15"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-BBA9C77B774B0C15"



},



"timestamps": [



1628618460000, 1628618520000, 1628618580000, 1628618640000, 1628618700000,



1628618760000, 1628618820000, 1628618880000, 1628618940000, 1628619000000



],



"values": [null, 15, 13, 15, null, null, 28, 14, 14, 13]



}



]



}



]



}
```

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.keyRequest.count.server:smooth(skipfirst)",



"data": [



{



"dimensions": ["SERVICE_METHOD-BBA9C77B774B0C15"],



"dimensionMap": {



"dt.entity.service_method": "SERVICE_METHOD-BBA9C77B774B0C15"



},



"timestamps": [



1628618460000, 1628618520000, 1628618580000, 1628618640000, 1628618700000,



1628618760000, 1628618820000, 1628618880000, 1628618940000, 1628619000000



],



"values": [null, null, 13, 15, null, null, null, 14, 14, 13]



}



]



}



]



}
```

## Трансформация sort

|  |  |
| --- | --- |
| Синтаксис | `:sort(<sorting key 1>,<sorting key 2>)` |
| Аргументы | Один или несколько ключей сортировки. |

Трансформация **sort** задаёт порядок кортежей (уникальные сочетания «метрика-измерение-значение измерения») в ответе. Можно указать один или несколько критериев сортировки. Первый критерий используется для сортировки. Дальнейшие критерии используются для разрешения ничьих. Можно выбрать направление сортировки:

* `ascending`
* `descending`

Также можно указать тип сортировки:

* `lexical`
* `natural`

### Сортировка по измерению

Чтобы отсортировать результаты по значению измерения, используйте ключ `dimension("<dimension>", <direction>)` или `dimension("<dimension>", <direction>, <type>)`. Кавычки (`"`) и тильды (`~`), входящие в состав ключа измерения, должны быть экранированы тильдой (`~`).

Измерения-сущности сортируются лексикографически (`0..9a..z`) по значениям Dynatrace entity ID.

Строковые измерения сортируются лексикографически.

#### Тип сортировки

Тип сортировки определяет порядок значений измерения.

Тип сортировки `lexical` упорядочивает строки измерений лексикографически (например, `1,11,2,21,3`). Это тип сортировки по умолчанию, когда тип явно не указан, как в `dimension("<dimension>", ascending)`. Его также можно указать явно через `dimension("<dimension>", <direction>, lexical)`.

Тип сортировки `natural` упорядочивает строки измерений в дружественном человеку, естественном порядке (например, `1,2,3,11,21`). Его можно указать через `dimension("<dimension>", <direction>, natural)`.

### Сортировка по точкам данных

Чтобы отсортировать результаты по точкам данных метрики в измерении, используйте ключ `value(<aggregation>,<direction>`).

Доступны следующие агрегации:

* `avg`
* `count`
* `max`
* `median`
* `min`
* `sum`
* `percentile(N)`, где N в диапазоне от `0` до `100`.
* `value`

Агрегация используется только для сортировки и не влияет на возвращаемые точки данных.

Сортировка применяется к результирующим точкам данных всей цепочки трансформаций до трансформации **sort**. Если в цепочке трансформаций нет [трансформации **aggregation**](#aggregation), сортировка применяется к агрегации метрики по умолчанию.

Показать пример

До трансформации sort

После трансформации sort

```
{



"totalCount": 4,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\")",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1613557980000],



"values": [6543]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1613557980000],



"values": [1009]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [1613557980000],



"values": [6673]



},



{



"dimensions": ["Lichtenstein"],



"dimensionMap": {



"dt.entity.geolocation.name": "Lichtenstein"



},



"timestamps": [1613557980000],



"values": [86]



}



]



}



]



}
```

```
{



"totalCount": 4,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\"):sort(dimension(\"dt.entity.geolocation.name\",ascending))",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1613557440000],



"values": [6543]



},



{



"dimensions": ["Germany"],



"dimensionMap": {



"dt.entity.geolocation.name": "Germany"



},



"timestamps": [1613557440000],



"values": [6673]



},



{



"dimensions": ["Lichtenstein"],



"dimensionMap": {



"dt.entity.geolocation.name": "Lichtenstein"



},



"timestamps": [1613557980000],



"values": [86]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1613557440000],



"values": [1009]



}



]



}



]



}
```

## Трансформация split by

|  |  |
| --- | --- |
| Синтаксис | `:splitBy("<dimension0>","<dimension1>","<dimensionN>")` |
| Аргументы | Список [измерений](#dimension), которые нужно сохранить в результате. Измерение должно быть указано по своему ключу.  Кавычки (`"`) и тильды (`~`), входящие в состав ключа измерения, должны быть экранированы тильдой (`~`). |

Трансформация **split by** сохраняет указанные измерения в результате и объединяет все остальные измерения. Значения пересчитываются в соответствии с выбранной агрегацией. Учитываются только ряды метрики, у которых есть каждое из указанных измерений.

К результату трансформации **split by** можно применить любую агрегацию, включая те, которые исходная метрика не поддерживает.

Показать пример

До трансформации split by

После трансформации split by

```
{



"totalCount": 4,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names",



"data": [



{



"dimensions": [



"easyTravel Demo",



"MOBILE_APPLICATION-752C288D59734C79",



"Android",



"OS-472A4A3B41095B09",



"Switzerland",



"GEOLOCATION-976217DC7560B588"



],



"dimensionMap": {



"dt.entity.device_application.name": "easyTravel Demo",



"dt.entity.os": "OS-472A4A3B41095B09",



"dt.entity.os.name": "Android",



"dt.entity.device_application": "MOBILE_APPLICATION-752C288D59734C79",



"dt.entity.geolocation.name": "Switzerland",



"dt.entity.geolocation": "GEOLOCATION-976217DC7560B588"



},



"timestamps": [1612950360000],



"values": [557]



},



{



"dimensions": [



"easyTravel Demo",



"MOBILE_APPLICATION-752C288D59734C79",



"Android",



"OS-472A4A3B41095B09",



"Austria",



"GEOLOCATION-EADFE05E062C8D33"



],



"dimensionMap": {



"dt.entity.device_application.name": "easyTravel Demo",



"dt.entity.os": "OS-472A4A3B41095B09",



"dt.entity.os.name": "Android",



"dt.entity.device_application": "MOBILE_APPLICATION-752C288D59734C79",



"dt.entity.geolocation.name": "Austria",



"dt.entity.geolocation": "GEOLOCATION-EADFE05E062C8D33"



},



"timestamps": [1612950360000],



"values": [328]



},



{



"dimensions": [



"easyTravel Demo",



"MOBILE_APPLICATION-752C288D59734C79",



"iOS",



"OS-62028BEE737F03D4",



"Switzerland",



"GEOLOCATION-976217DC7560B588"



],



"dimensionMap": {



"dt.entity.device_application.name": "easyTravel Demo",



"dt.entity.os": "OS-62028BEE737F03D4",



"dt.entity.os.name": "iOS",



"dt.entity.device_application": "MOBILE_APPLICATION-752C288D59734C79",



"dt.entity.geolocation.name": "Switzerland",



"dt.entity.geolocation": "GEOLOCATION-976217DC7560B588"



},



"timestamps": [1612950360000],



"values": [383]



},



{



"dimensions": [



"easyTravel Demo",



"MOBILE_APPLICATION-752C288D59734C79",



"iOS",



"OS-62028BEE737F03D4",



"Austria",



"GEOLOCATION-EADFE05E062C8D33"



],



"dimensionMap": {



"dt.entity.device_application.name": "easyTravel Demo",



"dt.entity.os": "OS-62028BEE737F03D4",



"dt.entity.os.name": "iOS",



"dt.entity.device_application": "MOBILE_APPLICATION-752C288D59734C79",



"dt.entity.geolocation.name": "Austria",



"dt.entity.geolocation": "GEOLOCATION-EADFE05E062C8D33"



},



"timestamps": [1612950360000],



"values": [214]



}



]



}



]



}
```

```
{



"totalCount": 2,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:apps.other.sessionCount.osAndGeo:names:splitBy(\"dt.entity.geolocation.name\")",



"data": [



{



"dimensions": ["Austria"],



"dimensionMap": {



"dt.entity.geolocation.name": "Austria"



},



"timestamps": [1612950360000],



"values": [542]



},



{



"dimensions": ["Switzerland"],



"dimensionMap": {



"dt.entity.geolocation.name": "Switzerland"



},



"timestamps": [1612950360000],



"values": [940]



}



]



}



]



}
```

## Трансформация time shift

|  |  |
| --- | --- |
| Синтаксис | `:timeshift(5m)` |
| Аргумент | Период сдвига. Поддерживаются следующие значения:  `s`: секунды  `m`: минуты  `h`: часы  `d`: дни  `w`: недели |

Трансформация **time shift** сдвигает временной интервал, заданный query-параметрами **from** и **to**, и сопоставляет результирующие точки данных меткам времени из исходного временного интервала. Она может помочь обрабатывать данные из разных часовых поясов или поместить вчерашние и сегодняшние данные на одну диаграмму для визуального сравнения.

Положительный аргумент сдвигает временной интервал в будущее; отрицательный аргумент сдвигает временной интервал в прошлое. В любом случае действует ограничение в **5 лет**.

Эту трансформацию можно использовать для обработки данных из разных часовых поясов.

Рассмотрим пример с временным интервалом от `1615550400000` (12 марта 2021 13:00 CET) до `1615557600000` (12 марта 2021 15:00 CET) и сдвигом времени `-1d` (один день в прошлое).

1. Точки данных будут запрошены для временного интервала от `1615464000000` (11 марта 2021 13:00 CET) до `1615471200000` (11 марта 2021 15:00 CET).
2. Метки времени в ответе будут выровнены по исходному временному интервалу. Например, точка данных с меткой времени `1615465800000` (11 марта 2021 13:30 CET) будет возвращена как `1615552200000` (12 марта 2021 13:30 CET).

## Трансформации единиц измерения

### Set unit

|  |  |
| --- | --- |
| Синтаксис | `:setUnit(<unit>)` |
| Аргумент | Желаемая единица измерения.  Чтобы получить список доступных единиц измерения, используйте API-вызов [GET all units](/managed/dynatrace-api/environment-api/metrics-units/get-all-units "Получите список всех метрик, доступных для вашего окружения мониторинга, через Dynatrace API."). |

Трансформация **setUnit** задаёт единицу измерения в метаданных метрики.

Эта трансформация **не** влияет на точки данных.

### To unit

|  |  |
| --- | --- |
| Синтаксис | `:toUnit(<sourceUnit>,<targetUnit>)` |
| Аргументы | Исходная и целевая единица измерения трансформации.  Чтобы получить список доступных единиц измерения, используйте API-вызов [GET all units](/managed/dynatrace-api/environment-api/metrics-units/get-all-units "Получите список всех метрик, доступных для вашего окружения мониторинга, через Dynatrace API."). |

Трансформация **toUnit** конвертирует точки данных из исходной единицы измерения в целевую. Если указанные единицы несовместимы, исходная единица сохраняется, а в ответ включается предупреждение.

Перед использованием трансформаций единиц измерения необходимо применить [трансформацию агрегации](#aggregation).

## Связанные темы

* [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных инсайтов.")
* [Environment API v2 - Entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройте entity selector для endpoint-ов Environment API.")
* [[GitHub] Examples of metric selector queries](https://dt-url.net/metric-selector-by-example)