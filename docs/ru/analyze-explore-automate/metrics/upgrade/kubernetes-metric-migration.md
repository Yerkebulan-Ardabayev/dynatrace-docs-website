---
title: Kubernetes руководство по миграции метрик
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/kubernetes-metric-migration
scraped: 2026-03-03T21:26:59.132805
---

# Руководство по миграции метрик Kubernetes


* Latest Dynatrace
* Чтение: 5 мин
* Обновлено 24 июня 2025 г.

Это руководство содержит информацию о миграции метрик Kubernetes на Grail. Как правило, метрика Grail эквивалентна метрике Metrics Classic. Однако в некоторых случаях однозначного соответствия нет:

* Конвергентные: одна метрика Grail представляет несколько метрик Metrics Classic схожей области или с повышенным уровнем детализации.
* Замена: другая метрика Grail представляет метрику Metrics Classic.
* Дивергентные/Вычисляемые: классическая метрика не представлена 1:1 как метрика Grail, но может быть вычислена из других метрик Grail.

## Идентичные метрики

Классические метрики и метрики Grail имеют одинаковый уровень детализации и доступные измерения. Единственное отличие -- ключ метрики.

## Конвергентные метрики

Следующие метрики были объединены. Метрики Grail, заменяющие классические метрики, предлагают повышенный уровень детализации по сравнению с классическими метриками.

Для достижения этого сниженного уровня детализации метрики Grail сначала агрегируются до гранулярности классической метрики. После этого может применяться тот же набор фильтров, и выходные данные классических метрик и метрик Grail идентичны.

Следующий список метрик содержит метрики количества подов и контейнеров, а также метрику количества событий Kubernetes, которая была доступна с более низким уровнем детализации как классическая метрика.

Метрики событий Kubernetes и количества контейнеров/подов

Следующая таблица содержит метрики потребления ресурсов рабочих нагрузок и узлов, которые были доступны как отдельные классические метрики уровня рабочей нагрузки и узла.
В Grail существует единая метрика на уровне контейнера.

**Пример:** Следующий запрос DQL возвращает объём памяти, потребляемой на уровне рабочей нагрузки, на основе агрегированных данных уровня контейнера.

```
timeseries memory_working_set = sum(dt.kubernetes.container.memory_working_set)


by: {


k8s.cluster.name,


k8s.namespace.name,


k8s.workload.name


}
```

Метрики потребления ресурсов уровня рабочей нагрузки и узла

## Заменённые метрики

Эта группа метрик состоит из ключей классических метрик, которые никогда не были доступны в виде метрик Grail.
Вместо этого используется наиболее похожая классическая метрика для определения замены Grail для этих устаревших метрик.
Причина устаревания -- очистка дублирующихся ключей метрик. Для следующих метрик полная идентичность значений между классической метрикой и метрикой Grail невозможна, но они тесно связаны и не сильно отличаются.

## Вычисляемые метрики

Следующий набор классических метрик контейнеров заменяется метриками контейнеров Grail.
Для большинства метрик CPU в этом разделе классические метрики имеют единицу измерения миллиядра (millicores), тогда как метрики Grail имеют единицу измерения наносекунды/минута. Чтобы получить те же значения, метрику Grail необходимо разделить на количество наносекунд в минуте.
(Количество наносекунд в минуте: 60 \* 1000 \* 1000 \* 1000)

Это относится к следующим метрикам Grail.

builtin:containers.cpu.throttledMilliCores

```
timeseries {


throttled_time = avg(dt.containers.cpu.throttled_time, rollup: sum, rate: 1m)


}


| fieldsAdd


ns_per_min = 60 * 1000 * 1000 * 1000


, milli_core_per_core = 1000


| fieldsAdd


throttled_milli_cores = throttled_time[] * milli_core_per_core / ns_per_min


| summarize {


throttled_milli_cores = sum(throttled_milli_cores[] )


}, by: { timeframe, interval }
```

builtin:containers.cpu.usageUserMilliCores

```
timeseries { usage_user_time = avg(dt.containers.cpu.usage_user_time)


}


| fieldsAdd


ns_per_min = 60 * 1000 * 1000 * 1000


, milli_core_per_core = 1000


| fieldsAdd


usage_user_milli_cores = usage_user_time[] * milli_core_per_core / ns_per_min


| summarize { usage_user_milli_cores = sum(usage_user_milli_cores[] )


}, by: { timeframe, interval }
```

builtin:containers.cpu.usageSystemMilliCores

```
timeseries {


usage_system_time = avg(dt.containers.cpu.usage_system_time)


}


| fieldsAdd


ns_per_min = 60 * 1000 * 1000 * 1000


, milli_core_per_core = 1000


| fieldsAdd


usage_system_milli_cores = usage_system_time[] * milli_core_per_core / ns_per_min


| summarize {


usage_system_milli_cores = sum(usage_system_milli_cores[] )


}, by: { timeframe, interval }
```

builtin:containers.cpu.usageMilliCores

```
timeseries {


usage_user_time = avg(dt.containers.cpu.usage_user_time)


, usage_system_time = avg(dt.containers.cpu.usage_system_time)


}


| fieldsAdd


ns_per_min = 60 * 1000 * 1000 * 1000


, milli_core_per_core = 1000


| fieldsAdd


usage_milli_cores = (usage_user_time[] + usage_system_time[] )


* milli_core_per_core / ns_per_min


| summarize {


usage_milli_cores = sum(usage_milli_cores[] )


}, by: { timeframe, interval }
```

builtin:containers.cpu.usagePercent

```
timeseries {


// for total usage, user and system cpu usage are added


userCpuUsage = avg(dt.containers.cpu.usage_user_time)


, systemCpuUsage = avg(dt.containers.cpu.usage_system_time)


// cpu logical counts are the fallback, if the throttling ratio doesn't exist


, cpuLogicalCount = avg(dt.containers.cpu.logical_cores)


}


// filter statement ...


// leftOuter join allows the throttling ratio to be null


| join [


timeseries {


throttlingRatio = avg(dt.containers.cpu.throttling_ratio)


// same filter statement as above ...


}


], on: { interval, timeframe}, fields: { throttlingRatio}, kind:leftOuter


| fieldsAdd


// sum of system and user cpu usage


numerator = userCpuUsage[] + systemCpuUsage[]


// throttling ratio, or as a fallback cpu logical count.


, denominator = coalesce(throttlingRatio, cpuLogicalCount)


, nanoseconds_per_minute  = 60 * 1000 * 1000 * 1000


| fields


interval, timeframe


, cpuUsagePercent = 100.0 * numerator[] / ( denominator[] * nanoseconds_per_minute)
```

builtin:containers.cpu.usageTime

```
timeseries {


usageUserTime = avg(dt.containers.cpu.usage_user_time)


, usageSystemTime = avg(dt.containers.cpu.usage_system_time)


}


, by: { dt.entity.container_group_instance},


| fields


interval, timeframe


, usageTime = usageSystemTime[] + usageUserTime[]
```

builtin:containers.memory.limitPercent

```
timeseries {


limit_bytes = avg(dt.containers.memory.limit_bytes),


physical_total_bytes = avg(dt.containers.memory.physical_total_bytes)


}


| fieldsAdd


limit_percent = (limit_bytes[] / physical_total_bytes[] ) * 100


| summarize {


limit_percent = sum(limit_percent[] )


}, by: { timeframe, interval }
```

builtin:containers.memory.usagePercent

```
timeseries {


memoryLimits = avg(dt.containers.memory.limit_bytes)


, totalPhysicalMemory = avg(dt.containers.memory.physical_total_bytes)


, residentSetBytes = avg(dt.containers.memory.resident_set_bytes)


}


, by: { dt.entity.container_group_instance}


| fieldsAdd


denominator = if (


arrayFirst(memoryLimits) > 0,


then: memoryLimits,


else: totalPhysicalMemory


)


| fields


dt.entity.container_group_instance


, interval, timeframe


, memoryUsagePercent = 100 * residentSetBytes[] / denominator[]
```

## Связанные темы

* [Использование запросов DQL](../../../platform/grail/dynatrace-query-language/dql-guide.md "Узнайте, как работает DQL и каковы ключевые концепции DQL.")
* [Notebooks](../../dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и обменивайтесь информацией из данных наблюдаемости -- всё в одном совместном настраиваемом рабочем пространстве.")
