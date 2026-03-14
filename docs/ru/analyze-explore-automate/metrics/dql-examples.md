---
title: DQL примеры timeseries
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/dql-examples
scraped: 2026-03-06T21:20:38.254143
---

# Примеры DQL timeseries

# Примеры DQL timeseries

* Последняя версия Dynatrace
* 8 мин. чтения
* Обновлено 17 октября 2025 г.

Метрики на Grail позволяют точно находить и извлекать любые данные метрик с помощью [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language."). Ознакомившись с [основами запросов DQL](../../platform/grail/dynatrace-query-language/dql-guide.md#metrics "Узнайте, как работает DQL и каковы ключевые концепции DQL.") и [командой timeseries](../../platform/grail/dynatrace-query-language/commands/metric-commands.md "Команды метрик DQL"), используйте примеры на этой странице, чтобы начать получать ответы из ваших метрик.

### Пример 1: Среднее использование CPU по всем хостам

В этом примере вы запросите среднее использование CPU по всем отслеживаемым хостам в вашей среде.

OneAgent собирает измерения CPU с хост-машины. Эти метрики доступны через ключи метрик, начинающиеся с `dt.host.cpu`.

Наблюдение за совокупным использованием CPU по всем хостам поможет визуально подтвердить, как ваша инфраструктура реагирует на скачки нагрузки и восстанавливается после них, а также отслеживать медленные, незаметные тенденции роста со временем.

```
timeseries usage=avg(dt.host.cpu.usage)
```

### Пример 2: Среднее использование CPU по хостам, ограничение до топ-3

В этом примере вы получите среднее использование CPU каждого отслеживаемого хоста и сфокусируетесь на трёх хостах с наибольшим использованием.

OneAgent собирает измерения CPU с хост-машины. Эти метрики доступны через ключи метрик, начинающиеся с `dt.host.cpu`.

Построение графика использования CPU отдельных хостов помогает визуализировать типичное и аномальное использование. Сфокусировавшись на трёх хостах с наибольшим использованием CPU, вы можете начать исследование недостаточно обеспеченных ресурсами приложений. Аналогично, фокус на хостах с наименьшим использованием CPU может выявить избыточное выделение ресурсов и возможности для экономии.

1. Запросите данные.

   ```
   timeseries usage=avg(dt.host.cpu.usage), usage_summary=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



   | fieldsAdd entityName(dt.entity.host)



   | sort usage_summary desc



   | limit 3
   ```
2. Упростите результаты.

   В некоторых ситуациях таблица может быть удобнее линейного графика. Давайте запросим данные, которые лучше всего подходят для табличного вывода, сфокусировавшись на наиболее важных столбцах: `dt.entity.host` и `usage`.

   ```
   timeseries usage=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



   | fieldsAdd entityName(dt.entity.host)



   | sort usage desc



   | limit 3



   | fields dt.entity.host, dt.entity.host.name, usage
   ```

   По сути, это тот же запрос, что и выше, но без временного ряда.

### Пример 3: Среднее использование CPU по IP-адресу хоста

В этом примере вы используете условие `in` для запроса хостов по их IP-адресу.

Используя оператор `in` с `classicEntitySelector`, вы можете фильтровать по `ipAddress` и другим атрибутам хоста.

Использование параметра `filter` команды timeseries более производительно, чем объединение `timeseries` с командой `filter`.

```
timeseries usage=avg(dt.host.cpu.usage),



filter: {in(



dt.entity.host,



classicEntitySelector("type(host),ipAddress(\"10.102.39.126\")")



)}
```

### Пример 4: Количество хостов, отправляющих данные об использовании CPU

В этом примере вы узнаете, как объединить `timeseries` с `summarize`. Сначала вы запросите хосты, отправляющие данные об использовании CPU, а затем подсчитаете количество хостов в результате.

Другие команды DQL также можно объединять с `timeseries`, как показано в предыдущих примерах, но в отличие от них `summarize` дополнительно агрегирует набор данных, возвращённый `timeseries`. Эта двухэтапная агрегация будет полезна, когда ваши вопросы станут более сложными и детализированными.

```
timeseries usage=avg(dt.host.cpu.usage), by:{dt.entity.host}



| summarize count()
```

### Пример 5: Топ хостов по прочитанным байтам с соответствующими записанными байтами

В этом примере вы обогатите один результат контекстом из другой метрики.

Даже при фокусе на операциях чтения диска соответствующие операции записи могут предоставить полезный контекст.

```
timeseries by:{dt.entity.host}, {



bytes_read=sum(dt.host.disk.bytes_read, scalar:true),



bytes_written=sum(dt.host.disk.bytes_written, scalar:true)



}



| sort bytes_read desc



| limit 3



| fields



dt.entity.host,



entityName(dt.entity.host),



bytes_read,



bytes_written
```

### Пример 6: Доступный CPU по узлу Kubernetes

В этом примере вы рассчитаете доступный CPU на всех узлах вашего гипотетического кластера "openfeature".

Для получения временного ряда вместо одиночного значения мы используем оператор `[]` для вычисления разности отдельных значений временных рядов. Результат — ещё один временной ряд, который можно визуализировать с помощью линейного графика.

Доступный CPU важен для эффективного использования ресурсов и предотвращения конкуренции за ресурсы. Временной ряд, визуализированный линейным графиком, — это один из способов показать, как доступный CPU изменяется со временем.

```
timeseries {



cpu_allocatable = min(dt.kubernetes.node.cpu_allocatable),



requests_cpu = max(dt.kubernetes.container.requests_cpu)



},



by:{dt.entity.kubernetes_cluster, dt.entity.kubernetes_node}



| fieldsAdd  // добавляем понятные имена



entityName(dt.entity.kubernetes_cluster),



entityName(dt.entity.kubernetes_node)



| fieldsAdd result = cpu_allocatable[] - requests_cpu[]



| fieldsRemove cpu_allocatable, requests_cpu
```

### Пример 7: Среднее использование CPU хоста по размеру хоста

В этом примере вы узнаете, как использовать [команду `entityAttr`](../../platform/grail/dynatrace-query-language/functions/general-functions.md#entity-attr "Список общих функций DQL.") для анализа использования CPU хоста по размеру хоста.

OneAgent собирает локальный контекст с хоста: информацию о количестве установленных процессоров и объёме памяти. Вы можете добавить эту информацию в запрос с помощью функции `entityAttr`.

Информация на уровне хоста иногда может быть слишком детализированной и сложной для интерпретации. В таких ситуациях правильно выбранный атрибут сущности может помочь исследовать и анализировать, как отдельные хосты вносят вклад в более общие тенденции.

```
timeseries usage=avg(dt.host.cpu.usage, scalar:true), by:{dt.entity.host}



| fieldsAdd cpuCores = entityAttr(dt.entity.host, "cpuCores")



| summarize by:{cpuCores}, avg(usage), count_hosts=count()
```

### Пример 8: Запрос нескольких метрик использования CPU одним запросом

В этом примере вы узнаете, как использовать [команду `append`](../../platform/grail/dynatrace-query-language/commands/correlation-and-join-commands.md#append "Команды корреляции и соединения DQL") для получения нескольких метрик CPU одним запросом.

Объединение запросов в одну команду может быть полезно для сравнения измерений из разных контекстов, так как они будут отображены на одном графике.

Когда вы запрашиваете множество метрик с одного хоста и не выполняете арифметических операций, команда `append` предпочтительнее запроса нескольких метрик одной командой `timeseries`. Команда `append` является сравнительно более гибким вариантом, так как не требует одинаковых аргументов `by` или `filter`. Кроме того, цепочка `append` более эффективна с точки зрения DQL.

```
timeseries idle=avg(dt.host.cpu.idle),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



| append [



timeseries system=avg(dt.host.cpu.system),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



]



| append [



timeseries user=avg(dt.host.cpu.user),



by:{dt.entity.host},



filter:{dt.entity.host == "HOST-EFAB6D2FE7274823"}



]
```

### Пример 9: Процент ошибок соединений по хостам

В этом примере вы примените знания из предыдущих примеров для расчёта процента ошибок и поиска хостов с процессами, имеющими большое количество неудачных соединений.

В этом примере используется параметр `default` для обработки случая, когда ошибок нет. Он вставляет значение `0` везде, где данные отсутствуют.

Расчёт процента ошибок является распространённой и критически важной задачей для мониторинга целей уровня обслуживания. Обнаружение постоянных или повторяющихся высоких процентов ошибок в тестовых средах может указывать на проблему развёртывания до того, как приложение попадёт в продуктивную среду.

```
timeseries {



new = sum(dt.process.network.sessions.new),



reset = sum(dt.process.network.sessions.reset, default:0),



timeout = sum(dt.process.network.sessions.timeout, default:0)



},



by:{dt.entity.host}



| fieldsAdd result = 100 * (reset[] + timeout[]) / new[]



| filter arrayAvg(result) > 0



| sort arrayAvg(result) desc
```

### Пример 10: Мониторинг доступности хостов

В этом примере вы будете отслеживать доступность хостов и подсчитывать те, которые в настоящее время работают.

Вы можете использовать команду timeseries с [параметром `nonempty`](../../platform/grail/dynatrace-query-language/commands/metric-commands.md#expand--nonempty-parameter--1 "Команды метрик DQL") для расчёта доступности хостов. Этот параметр гарантирует получение результата, даже когда данные не соответствуют фильтру — например, когда ни один хост не работает. Это обеспечивает более точное представление доступности хостов.

```
timeseries availability = sum(dt.host.availability, default:0),



nonempty:true,



filter:{availability.state == "up"}
```

### Пример 11: Проба готовности

В этом примере вы запросите [метрики логов](../logs/lma-log-processing/lma-log-metrics.md "Создавайте метрики на основе данных логов и используйте их в Dynatrace как любые другие метрики.") для подсчёта успешных и неудачных проб готовности по хостам.

Вы можете использовать [параметр `union`](../../platform/grail/dynatrace-query-language/commands/metric-commands.md#union "Команды метрик DQL") для охвата всех хостов, включая те, у которых нет ошибок или нет успешных проб.

```
timeseries



failure_count=sum(log.readiness_probe.failure_count, default:0),



success_count=sum(log.readiness_probe.success_count, default:0),



by:{dt.entity.host},



union:true
```

Аргумент `union:true` охватывает все хосты, даже те, у которых не было ошибок или успешных проб.

### Пример 12: Частота ошибок

В этом примере вы запросите частоту ошибок в секунду для конкретного эндпоинта ("/api/accounts"). Используя [параметр `rate`](../../platform/grail/dynatrace-query-language/commands/metric-commands.md#rate "Команды метрик DQL"), вы можете нормализовать данные временного ряда к определённой длительности.

Мониторинг частоты ошибок запросов критически важен для понимания производительности приложения, выявления узких мест и обеспечения оптимального пользовательского опыта.

Dynatrace показывает количество запросов в минуту по умолчанию, так как метрики сервисов Dynatrace собирают данные о запросах с минутной гранулярностью.

```
timeseries sum(dt.service.request.failure_count, rate:1s),



filter:{startsWith(endpoint.name, "/api/accounts")}
```

### Пример 13: Планирование ёмкости

В этом примере вы запросите текущую доступность дискового пространства хоста и используете параметр [`shift`](../../platform/grail/dynatrace-query-language/commands/metric-commands.md#shift "Команды метрик DQL") для сравнения с использованием 7 дней назад.

Мониторинг доступности дискового пространства хоста помогает в планировании ёмкости. Если использование дискового пространства сегодня постоянно выше, чем 7 дней назад, это может сигнализировать о необходимости дополнительных ресурсов хранения. И наоборот, снижение использования может позволить оптимизировать ресурсы.

```
timeseries avail=avg(dt.host.disk.avail), by:{dt.entity.host}, from:-24h



| append [



timeseries avail.yesterday=avg(dt.host.disk.avail), by:{dt.entity.host}, shift:-168h



]



| filter startsWith(entityName(dt.entity.host), "prod-")
```

### Пример 14: Проверка доступности и резервирования хостов

В этом примере вы используете [агрегацию `count`](../../platform/grail/dynatrace-query-language/commands/metric-commands.md#timeseries-count "Команды метрик DQL") для отслеживания количества отслеживаемых хостов в каждой зоне доступности региона AWS us-east-1.

Приложения часто развёртывают хосты в нескольких зонах доступности (AZ) для обеспечения высокой доступности. Подсчёт хостов в каждой AZ помогает убедиться, что распределение сбалансировано и, в случае сетевых проблем или других сбоев в одной AZ, нагрузка может быть переключена на другую AZ.

```
timeseries num_hosts = count(dt.host.cpu.usage),



by:{aws.availability_zone},



filter:{startsWith(aws.availability_zone, "us-east-1")}
```

### Пример 15: Оптимизация производительности

В этом примере вы используете [агрегацию `percentile`](../../platform/grail/dynatrace-query-language/commands/metric-commands.md#timeseries-percentile "Команды метрик DQL") для отслеживания 90-го процентиля времени отклика условного эндпоинта /api/accounts.

Отслеживание [процентилей](https://www.dynatrace.com/news/blog/why-averages-suck-and-percentiles-are-great/) времени отклика сервиса помогает выявлять узкие места и области для улучшения. Если конкретная транзакция постоянно превышает этот порог, вы можете решить, стоит ли её исследовать и дополнительно оптимизировать.

```
timeseries p90 = percentile(dt.service.request.response_time, 90),



filter:{startsWith(endpoint.name, "/api/accounts")}
```

### Пример 16: Правильный выбор размера развёртываний

В этом примере вы используете [функцию `if`](../../platform/grail/dynatrace-query-language/functions/conditional-functions.md#if "Список условных функций DQL.") для маркировки недоиспользованных пар хост-диск.

Определение избыточно обеспеченных ресурсами развёртываний помогает сократить эксплуатационные расходы. Устранив избыточные ресурсы инфраструктуры, вы можете определить правильный размер развёртывания для вашего приложения.

```
timeseries avail=avg(dt.host.disk.avail, scalar:true),



by:{dt.entity.disk, dt.entity.host},



filter:{startsWith(dt.entity.host, "my-app-")}



| fieldsAdd disk_usage=if(avail>450000000000, "underused", else: "optimal")



| limit 3
```

### Пример 17: Разделение использования CPU по аннотациям Kubernetes

В этом примере вы разделите использование CPU по аннотациям Kubernetes.

Вы можете использовать аннотацию Kubernetes `app.kubernetes.io/component` для оценки производительности компонентов вашего приложения. Аннотации являются атрибутами облачного приложения и обычно не принимаются вместе с метрикой. Следует выполнить разделение по облачному приложению и найти соответствующую аннотацию.

Многие [функции команды `summarize`](../../platform/grail/dynatrace-query-language/commands/aggregation-commands.md#summarize "Команды агрегации DQL") принимают итеративные выражения, такие как `cpu_usage[]`, для сохранения временного ряда.

```
timeseries cpu_usage = sum(dt.kubernetes.container.cpu_usage, rollup:max),



by:{dt.entity.cloud_application}



| fieldsAdd annotations = entityAttr(dt.entity.cloud_application, "kubernetesAnnotations")



| fieldsAdd component = annotations[`app.kubernetes.io/component`]



| summarize cpu_usage = sum(cpu_usage[]),



by:{timeframe, interval, component}
```