---
title: Metrics API - Metric expressions
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/metric-expressions
scraped: 2026-05-12T11:11:42.814914
---

# Metrics API - Metric expressions

# Metrics API - Metric expressions

* Справочник
* Обновлено 29 июля 2022 г.

Выражения метрик позволяют использовать простые арифметические операции прямо в metric selector.

Например, это выражение вычисляет отношение (в процентах) двух метрик:

```
metric1 / metric2 * 100
```

В качестве операндов выражения можно использовать метрики или числа.

* Чтобы задать порядок операций, нужно использовать скобки.
* Все метрики с более чем 1 точкой данных, участвующие в выражении метрики, должны быть одного разрешения.
* В качестве операнда можно использовать любую метрику, включая метрики, изменённые любой [цепочкой трансформаций](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Настройте metric selector для Metric v2 API."), и можно применять трансформации к результату выражения.

## Ограничения

* Селектор должен содержать как минимум один ключ метрики.
* За один запрос можно запросить точки данных до 10 метрик.

Для целей этого ограничения одно выражение (например, `metric2 + metric2`) считается за одну метрику.

## Приоритет операций

Применяются стандартные правила математического приоритета:

1. Скобки, трансформации метрик
2. Отрицание
3. Умножение, деление
4. Сложение, вычитание

## Агрегация

Если агрегация была применена в цепочке трансформаций, используется эта агрегация. Если трансформация не применялась, используется агрегация по умолчанию. Ваши операнды-метрики могут быть с разными агрегациями. Например, `metric:max - metric:min`.

## Разрешение выражений

Выражения метрик разрешаются следующим образом:

1. [Формируются пары кортежей](#tuples) для каждой пары метрик.
2. [Выравниваются точки данных](#data) в каждом кортеже.
3. Применяется арифметическая операция к выровненным точкам данных.

### Кортежи

Арифметические операции используют точки данных кортежей (уникальные сочетания «метрика-измерение-значение измерения») метрик. Идентичные кортежи каждой метрики объединяются в пары, а затем их точки данных выравниваются.

Если одна метрика безразмерна (имеет только один кортеж без измерений и значений измерений), то этот единственный кортеж объединяется с каждым кортежем других метрик. То же относится к числам.

Кортежи, не образующие пар, игнорируются выражением и не представлены в результате.

### Точки данных

После формирования пар кортежей точки данных выравниваются, а затем к выровненным точкам данных применяется нужная арифметическая операция.

* Если любая из выровненных точек данных равна `null`, выражение разрешается в `null`.
* Если в операции участвует число, оно выравнивается с каждой точкой данных операнда-метрики.
* Если одна метрика, это одна точка данных, а другая серия, эта одна точка данных выравнивается с каждой точкой данных серии.
* Если обе метрики, это одна точка данных, точки данных выравниваются, и результирующий временной слот покрывает обе точки данных.
* Если обе метрики серии, точки данных выравниваются по меткам времени.

Для любых невыровненных точек данных выражение разрешается в `null`.

## Лучшие практики

### Используйте только при необходимости

Используйте выражение метрики только если без него не достичь цели. Допустим, вы хотите вычислить среднее использование CPU двух хостов, `HOST-001` и `HOST-002`. Это можно сделать выражением метрики:

```
(



builtin:host.cpu.usage:filter(eq("dt.entity.host","HOST-001")):splitBy()



+



builtin:host.cpu.usage:filter(eq("dt.entity.host","HOST-002")):splitBy()



)



/2
```

С этим подходом есть две проблемы. Во-первых, выражение трудно читать и поэтому оно подвержено синтаксическим ошибкам. Во-вторых, если один из хостов офлайн, результат выражения пуст. Хотя вторую проблему можно решить трансформацией **default**, использование [средней агрегации](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#aggregation "Настройте metric selector для Metric v2 API.") эффективнее:

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

### Не конвертируйте единицы измерения

Не используйте выражение метрики для конвертации единицы измерения данных. Вместо этого используйте [трансформацию **toUnit**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#to-unit "Настройте metric selector для Metric v2 API."). Единственное исключение из этого правила: единицы измерения, которые Dynatrace не поддерживает. Используйте запрос [GET all units](/managed/dynatrace-api/environment-api/metrics-units/get-all-units "Получите список всех метрик, доступных для вашего окружения мониторинга, через Dynatrace API."), чтобы получить список поддерживаемых единиц измерения.

### Использование трансформации limit

Всегда применяйте [трансформацию **limit**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#limit-transformation "Настройте metric selector для Metric v2 API.") к результату вычисления, а не к его операндам.

Рассмотрим следующий запрос, который пытается сложить топ-10 времён использования CPU с топ-10 времён простоя CPU.

```
builtin:host.cpu.usage:sort(value(avg,descending)):limit(10)



+



builtin:host.cpu.idle:sort(value(avg,descending)):limit(10)
```

Если у вас большое окружение с сотнями хостов, маловероятно, что 10 хостов с наибольшим использованием CPU окажутся среди 10 хостов с наибольшим временем простоя CPU. У операндов не будет совпадающих кортежей, поэтому результат выражения будет пустым. Решение: применить limit к результату выражения вместо этого:

```
(



builtin:host.cpu.usage



+



builtin:host.cpu.idle



)



:sort(value(auto,descending))



:limit(10)
```

### Закрывайте пропуски данных трансформацией default

[Трансформация **default**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#default "Настройте metric selector для Metric v2 API.") особенно ценна для выражений метрик. Хотя обычно трансформация не заполняет точки данных `null`, если у метрики нет ни одной точки данных во временном интервале запроса, в контексте выражения метрики её семантика немного иная. Пока метрика по любую сторону выражения имеет хотя бы одну точку данных, трансформация заполнит пропуски. Однако если у всех метрик в выражении данные отсутствуют, трансформация вернёт пустые результаты.

Рассмотрим этот пример выражения-отношения, где мы вычисляем долю ошибок для ключевых пользовательских действий:

```
builtin:apps.other.keyUserActions.reportedErrorCount.os



/



builtin:apps.other.keyUserActions.requestCount.os
```

Если в вашем временном интервале много запросов, но ни одной ошибки, результат будет пустым, хотя доля ошибок `0` была бы более осмысленной. Этого можно достичь трансформацией `default(0)`:

```
builtin:apps.other.keyUserActions.reportedErrorCount.os:default(0)



/



builtin:apps.other.keyUserActions.requestCount.os
```

## Примеры

Пример 1. Построение метрики-отношения

С помощью выражения метрики можно строить собственные метрики-отношения. Предположим, мы начинаем со следующих метрик:

* **builtin:service.errors.total.count** показывает количество ошибок любого типа в сервисе
* **builtin:service.errors.server.successCount** показывает количество вызовов без ошибок на стороне сервера

Из них можно построить метрику доли ошибок:

```
builtin:service.errors.total.count:value:default(0)



/



(



builtin:service.errors.total.successCount:value:default(0)



+



builtin:service.errors.total.count:value:default(0)



)
```

[Трансформация **default**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#default "Настройте metric selector для Metric v2 API.") используется для замены значений временных слотов, имеющих значение `null`, на 0.

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

Пример 2. Вклад одного сервиса в общее количество ошибок

Метрика **builtin:service.errors.total.count** показывает количество ошибок по вашим сервисам. Список может быть длинным, и вам может быть интересен вклад каждого сервиса в количество ошибок. Сочетание трансформаций метрик и выражений метрик может предоставить эту информацию.

Вам нужны эти трансформации:

* [трансформация filter](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#filter "Настройте metric selector для Metric v2 API."), чтобы получить количество ошибок для проверяемого сервиса.
* [трансформация split by](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Настройте metric selector для Metric v2 API."), чтобы объединить отдельные количества ошибок каждого сервиса в одно.

Затем используйте это выражение:

```
builtin:service.errors.total.count:filter(eq("dt.entity.service","SERVICE-B82BFBCB4E264A98")):value:default(0)



/



builtin:service.errors.total.count:splitBy():value:default(0) * 100
```

[Трансформация **default**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#default "Настройте metric selector для Metric v2 API.") используется для замены значений временных слотов, имеющих значение `null`, на 0.

Изолированный сервис

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

Пример 3. Средняя длительность GC

Метрика **builtin:tech.jvm.memory.gc.collectionTime** показывает суммарную длительность всех сборок мусора во временном слоте. Информация об отдельных временах GC недоступна, но можно использовать метрику **builtin:tech.jvm.memory.pool.collectionCount**, показывающую количество GC за время, чтобы получить среднюю длительность сборки мусора.

Прежде чем начать вычисление, нужно выровнять измерения обеих метрик. Для этого нужно применить трансформацию **split by** с аргументом `dt.entity.process_group_instance` к метрике **builtin:tech.jvm.memory.pool.collectionCount**.

Кроме того, можно отсортировать результат по убыванию, применив [трансформацию sort](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#sort "Настройте metric selector для Metric v2 API."). Выражение выглядит так:

```
(



builtin:tech.jvm.memory.gc.collectionTime



/



builtin:tech.jvm.memory.pool.collectionCount:splitBy("dt.entity.process_group_instance")



):sort(value(max,descending))
```

Общее время GC

Количество GC

Средняя длительность GC

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

Больше примеров смотрите на [Github-странице 'Metric Expressions by Example'](https://dt-url.net/metric-expressions-by-example).

## Вводное видео

Учтите, что синтаксис, используемый в этом видео, основан на старом синтаксисе, который требовал скобок вокруг каждой метрики и числа выражения.

Metric Expressions