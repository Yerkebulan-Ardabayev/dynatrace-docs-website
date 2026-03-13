---
title: Metrics API - Metric expressions
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/metric-expressions
scraped: 2026-03-06T21:26:05.262057
---

# Metrics API — Метрические выражения

# Metrics API — Метрические выражения

* Справочник
* Обновлено 29 июля 2022 г.

Метрические выражения позволяют использовать простые арифметические операции непосредственно в селекторе метрик.

Например, следующее выражение вычисляет соотношение (в процентах) двух метрик:

```
metric1 / metric2 * 100
```

В качестве операндов выражения можно использовать метрики или числа.

* Необходимо использовать скобки для принудительного задания порядка операций.
* Все метрики с более чем 1 точкой данных, участвующие в метрическом выражении, должны иметь одинаковое разрешение.
* В качестве операнда можно использовать любую метрику, включая метрики, модифицированные любой [цепочкой трансформаций](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка селектора метрик для Metric v2 API."), а также применять трансформации к результату выражения.

## Ограничения

* Селектор должен содержать хотя бы один ключ метрики.
* В одном запросе можно запросить точки данных не более чем 10 метрик.

Для целей данного ограничения одно выражение (например, `metric2 + metric2`) считается за одну метрику.

## Приоритет

Применяются стандартные математические правила приоритета:

1. Скобки, трансформации метрик
2. Отрицание
3. Умножение, деление
4. Сложение, вычитание

## Агрегация

Если агрегация была применена в цепочке трансформаций, используется эта агрегация. Если трансформация не применялась, используется агрегация по умолчанию. Операнды метрик могут иметь различные агрегации. Например, `metric:max - metric:min`.

## Вычисление выражений

Метрические выражения вычисляются следующим образом:

1. [Формирование пар кортежей](#tuples) для каждой пары метрик.
2. [Выравнивание точек данных](#data) в каждом кортеже.
3. Применение арифметической операции к выровненным точкам данных.

### Кортежи

Арифметические операции используют точки данных кортежей (уникальных комбинаций «метрика — измерение — значение измерения») метрик. Идентичные кортежи каждой метрики объединяются в пары, после чего их точки данных выравниваются.

Если одна метрика безразмерна (имеет только один кортеж без измерений и значений измерений), этот единственный кортеж сопоставляется с каждым кортежем других метрик. То же самое относится к числам.

Несопоставимые кортежи игнорируются выражением и не представлены в результате.

### Точки данных

После формирования пар кортежей точки данных выравниваются, а затем к выровненным точкам данных применяется нужная арифметическая операция.

* Если какая-либо из выровненных точек данных равна `null`, выражение вычисляется как `null`.
* Если в операции участвует число, оно выравнивается с каждой точкой данных метрического операнда.
* Если одна метрика представляет единственную точку данных, а другая — ряд, единственная точка данных выравнивается с каждой точкой данных ряда.
* Если обе метрики представляют единственную точку данных, точки данных выравниваются, и результирующий временной интервал охватывает обе точки данных.
* Если обе метрики представляют ряды, точки данных выравниваются по меткам времени.

Для невыровненных точек данных выражение вычисляется как `null`.

## Лучшие практики

### Используйте только при необходимости

Используйте метрическое выражение только в том случае, если невозможно достичь цели без него. Допустим, вы хотите рассчитать среднее использование CPU двух хостов, `HOST-001` и `HOST-002`. Это можно сделать с помощью метрического выражения:

```
(



builtin:host.cpu.usage:filter(eq("dt.entity.host","HOST-001")):splitBy()



+



builtin:host.cpu.usage:filter(eq("dt.entity.host","HOST-002")):splitBy()



)



/2
```

У такого подхода две проблемы. Во-первых, выражение трудно читать и поэтому подвержено синтаксическим ошибкам. Во-вторых, если один из хостов не в сети, результат выражения будет пустым. Хотя вторую проблему можно решить трансформацией **default**, использование [агрегации среднего](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#aggregation "Настройка селектора метрик для Metric v2 API.") более эффективно:

```
builtin:host.cpu.usage



:filter(



or(



eq("dt.entity.host","HOST-001"),



eq("dt.entity.host","HOST-002")



)



)



:splitBy()



:avg
```

### Не преобразовывайте единицы измерения

Не используйте метрическое выражение для преобразования единиц данных. Используйте вместо этого [трансформацию **toUnit**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#to-unit "Настройка селектора метрик для Metric v2 API."). Единственное исключение — единицы измерения, которые Dynatrace не поддерживает. Используйте запрос [GET all units](/docs/dynatrace-api/environment-api/metrics-units/get-all-units "Получите список всех метрик, доступных для вашей среды мониторинга через Dynatrace API."), чтобы получить список поддерживаемых единиц.

### Использование трансформации limit

Всегда применяйте [трансформацию **limit**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#limit-transformation "Настройка селектора метрик для Metric v2 API.") к результату вычисления, а не к его операндам.

Рассмотрим следующий запрос, который пытается сложить топ-10 значений использования CPU с топ-10 значениями простоя CPU.

```
builtin:host.cpu.usage:sort(value(avg,descending)):limit(10)



+



builtin:host.cpu.idle:sort(value(avg,descending)):limit(10)
```

Если у вас большая среда с сотнями хостов, маловероятно, что 10 хостов с наибольшим использованием CPU окажутся среди 10 хостов с наибольшим временем простоя CPU. У операндов не будет совпадающих кортежей, и результат выражения будет пустым. Решение — применить limit к результату выражения:

```
(



builtin:host.cpu.usage



+



builtin:host.cpu.idle



)



:sort(value(auto,descending))



:limit(10)
```

### Заполнение пробелов в данных с помощью трансформации default

[Трансформация **default**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Настройка селектора метрик для Metric v2 API.") особенно полезна для метрических выражений. Хотя обычно эта трансформация не заполняет точки данных со значением `null`, если метрика не имеет ни одной точки данных во временном диапазоне запроса, в контексте метрического выражения её семантика немного отличается. Пока метрика на любой стороне выражения имеет хотя бы одну точку данных, трансформация заполнит пробелы. Однако если все метрики в выражении не содержат данных, трансформация вернёт пустой результат.

Рассмотрим пример выражения отношения, где мы рассчитываем долю ошибок для ключевых пользовательских действий:

```
builtin:apps.other.keyUserActions.reportedErrorCount.os



/



builtin:apps.other.keyUserActions.requestCount.os
```

Если было много запросов, но ни одной ошибки за выбранный период, результат будет пустым, хотя соотношение ошибок `0` было бы более информативным. Этого можно достичь с помощью трансформации `default(0)`:

```
builtin:apps.other.keyUserActions.reportedErrorCount.os:default(0)



/



builtin:apps.other.keyUserActions.requestCount.os
```

## Примеры

Пример 1. Создание метрики отношения

С помощью метрического выражения вы можете создать собственные метрики отношений. Допустим, мы начинаем со следующих метрик:

* **builtin:service.errors.total.count** — показывает количество ошибок любого типа в сервисе
* **builtin:service.errors.server.successCount** — показывает количество вызовов без серверных ошибок

Из них можно создать метрику отношения ошибок:

```
builtin:service.errors.total.count:value:default(0)



/



(



builtin:service.errors.total.successCount:value:default(0)



+



builtin:service.errors.total.count:value:default(0)



)
```

[Трансформация **default**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Настройка селектора метрик для Metric v2 API.") используется для замены значений временных интервалов со значением `null` на 0.

Метрика 1

Метрика 2

Результат

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [48763, 81283, 80798]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1096, 1124, 1095]



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



"metricId": "builtin:service.errors.total.successCount",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [46182, 77110, 76736]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0, 0, 0]



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



"metricId": "builtin:service.errors.total.count/(builtin:service.errors.total.count+builtin:service.errors.total.successCount)",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.513592079625046, 0.513172930621934, 0.5128924549621035]



},



{



"dimensions": ["SERVICE-BE8B6928C46204B5"],



"dimensionMap": {



"dt.entity.service": "SERVICE-BE8B6928C46204B5"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1, 1, 1]



}



]



}



]



}
```

Пример 2. Вклад отдельного сервиса в общее количество ошибок

Метрика **builtin:service.errors.total.count** показывает количество ошибок по вашим сервисам. Список может быть длинным, и вас может интересовать вклад каждого сервиса в общее количество ошибок. Комбинация трансформаций метрик и метрических выражений может предоставить эту информацию.

Вам нужны следующие трансформации:

* [Трансформация filter](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#filter "Настройка селектора метрик для Metric v2 API.") для получения количества ошибок проверяемого сервиса.
* [Трансформация split by](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Настройка селектора метрик для Metric v2 API.") для объединения количеств ошибок каждого сервиса в одно значение.

Затем используйте следующее выражение:

```
builtin:service.errors.total.count:filter(eq("dt.entity.service","SERVICE-B82BFBCB4E264A98")):value:default(0)



/



builtin:service.errors.total.count:splitBy():value:default(0) * 100
```

[Трансформация **default**](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#default "Настройка селектора метрик для Metric v2 API.") используется для замены значений временных интервалов со значением `null` на 0.

Выделенный сервис

Общее количество

Процент

```
{



"totalCount": 1,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:service.errors.total.count:filter(eq(\"dt.entity.service\",SERVICE-B82BFBCB4E264A98))",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [48763, 81283, 80798]



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



"metricId": "builtin:service.errors.total.count:splitBy()",



"data": [



{



"dimensions": [],



"dimensionMap": {},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [49882, 82425, 81911]



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



"metricId": "builtin:service.errors.total.count:filter(eq(\"dt.entity.service\",SERVICE-B82BFBCB4E264A98))/builtin:service.errors.total.count:splitBy()*100",



"data": [



{



"dimensions": ["SERVICE-B82BFBCB4E264A98"],



"dimensionMap": {



"dt.entity.service": "SERVICE-B82BFBCB4E264A98"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [97.75670582574877, 98.61449802851077, 98.64120814054277]



}



]



}



]



}
```

Пример 3. Средняя продолжительность сборки мусора (GC)

Метрика **builtin:tech.jvm.memory.gc.collectionTime** показывает общую продолжительность всех сборок мусора за временной интервал. Информация об отдельных сборках недоступна, но мы можем использовать метрику **builtin:tech.jvm.memory.pool.collectionCount**, показывающую количество сборок за период, чтобы получить среднюю продолжительность одной сборки мусора.

Перед началом расчёта необходимо выровнять измерения обеих метрик. Для этого нужно применить трансформацию **split by** с аргументом `dt.entity.process_group_instance` к метрике **builtin:tech.jvm.memory.pool.collectionCount**.

Дополнительно можно отсортировать результат в порядке убывания, применив [трансформацию sort](/docs/dynatrace-api/environment-api/metric-v2/metric-selector#sort "Настройка селектора метрик для Metric v2 API."). Выражение выглядит так:

```
(



builtin:tech.jvm.memory.gc.collectionTime



/



builtin:tech.jvm.memory.pool.collectionCount:splitBy("dt.entity.process_group_instance")



):sort(value(max,descending))
```

Общее время GC

Количество GC

Средняя продолжительность GC

```
{



"totalCount": 3,



"nextPageKey": null,



"result": [



{



"metricId": "builtin:tech.jvm.memory.gc.collectionTime",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [164670, 171630, 163044]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [6883411, 5977311, 6356225]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [163368, 162924, 170502]



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



"metricId": "builtin:tech.jvm.memory.pool.collectionCount:splitBy(\"dt.entity.process_group_instance\")",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1727814, 1720686, 1691604]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [31363, 30588, 31419.5]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [1697262, 1703742, 1722612]



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



"metricId": "(builtin:tech.jvm.memory.gc.collectionTime/builtin:tech.jvm.memory.pool.collectionCount:splitBy(\"dt.entity.process_group_instance\")):sort(value(max,descending))",



"data": [



{



"dimensions": ["PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-92605BB8AE962F1C"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [219.47552848898383, 195.41359356610437, 202.3019144162065]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-18A5241823ABC769"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-18A5241823ABC769"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.09530539745597616, 0.09974510166294141, 0.09638426014599162]



},



{



"dimensions": ["PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"],



"dimensionMap": {



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-4285F2EF6B79E8A9"



},



"timestamps": [1619913600000, 1620086400000, 1620259200000],



"values": [0.09625384884596486, 0.09562715481569392, 0.09897876016189368]



}



]



}



]



}
```

Дополнительные примеры см. на [странице Github «Metric Expressions by Example»](https://dt-url.net/metric-expressions-by-example).

## Вводное видео

Обратите внимание, что синтаксис, используемый в этом видео, основан на старом синтаксисе, который требовал скобок вокруг каждой метрики и числа выражения.

Metric Expressions
