---
title: Metrics API - FAQ
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v2/metric-faq
scraped: 2026-05-12T12:31:49.014586
---

# Metrics API - FAQ

# Metrics API - FAQ

* Справочник
* Обновлено 16 ноября 2022 г.

## Запрос метрик

Почему последняя метка времени результата в будущем?

В Dynatrace точки данных метрик хранятся во временных слотах разных разрешений. Самая тонкая гранулярность временного слота: одна минута.
Метки времени, возвращаемые endpoint-ом запроса метрик, это *времена окончания* этих временных слотов.

Например, если текущее время 09:24, и вы запрашиваете последние 6 часов с разрешением 1 час, метка времени последней точки данных будет сегодня в 10:00. Подробности смотрите в [Timeframe note](/managed/dynatrace-api/environment-api/metric-v2/get-data-points#timeframe-note "Читайте точки данных одной или нескольких метрик через Metrics v2 API.").

Почему возвращаемые значения растут при большем временном интервале?

Точки данных, возвращаемые endpoint-ом запроса, агрегированы по времени. В зависимости от временного интервала запроса разрешение точек данных может быть минутами, часами, днями или даже годами. Если вы запрашиваете больший временной интервал, разрешение ваших данных, вероятно, будет грубее, что вызывает бо́льшие значения для агрегаций, таких как `sum` или `count`.

Если вы хотите иметь сопоставимые результаты для разных разрешений, используйте [трансформацию **rate**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#rate "Настройте metric selector для Metric v2 API."). Например, `:rate(1m)` даёт вам значение в минуту.

Почему значение процентной метрики больше 100% при использовании fold?

Например, следующий запрос может вернуть значения выше 100%, хотя единица измерения метрики, `Percent`.

```
builtin:host.availability:splitBy():avg:fold
```

Первопричина этой проблемы в том, что когда вы применяете [трансформацию **aggregation**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#aggregation "Настройте metric selector для Metric v2 API.") (вызывая `:avg` в примере выше), семантика метрики теряется и недоступна для трансформаций, происходящих позже в цепочке трансформаций. То есть, когда вызывается [трансформация **fold**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#fold "Настройте metric selector для Metric v2 API."), информация о том, что значения нужно усреднять, больше недоступна, и вместо этого применяется агрегация `sum`.

Чтобы предотвратить эту проблему, не выполняйте агрегацию перед трансформацией fold.

```
builtin:host.availability:splitBy():fold
```

Почему значение измерения null?

Если к измерению метрики применяется [top x](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#remainder "Настройте metric selector для Metric v2 API."), сохраняются только *x* значений измерения. Все остальные значения измерения записываются в измерение `remainder`, которое имеет значение `null`.

Как получить читаемые имена отслеживаемых сущностей?

По умолчанию ответ запроса содержит только ID отслеживаемых сущностей (например, `HOST-E1784F5E3F9987CD`).

Если вы хотите иметь в ответе и имя сущности, нужно использовать [трансформацию **names**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#names "Настройте metric selector для Metric v2 API."). Читаемое имя тогда доступно в `dimensionMap` под ключом измерения `dt.entity.<entityType>.name` (например, `dt.entity.host.name`).

Почему результат моего выражения метрики пуст?

Есть несколько причин, по которым выражение метрики может дать пустой результат:

* Ключи измерений метрик, используемых в выражении, не совпадают.

  Если у вас метрики с разными ключами измерений, нужно выровнять измерения метрик, чтобы сделать вычисление возможным. Для этого можно использовать трансформацию [**split by**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Настройте metric selector для Metric v2 API.") или [**merge**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#merge "Настройте metric selector для Metric v2 API."). Рассмотрим этот запрос:

  ```
  builtin:host.cpu.iowait



  /



  builtin:host.disk.throughput.read
  ```

  Он выдаст ошибку `Metric expression contains non-matching dimension-keys.`, потому что метрика **builtin:host.cpu.iowait** имеет только одно измерение (**dt.entity.host**), тогда как **builtin:host.disk.throughput.read** имеет два (**dt.entity.host** и **dt.entity.disk**). Чтобы запрос заработал, нужно избавиться от измерения disk (например, с помощью трансформации **merge**).

  ```
  builtin:host.cpu.iowait



  /



  builtin:host.disk.throughput.read:merge(dt.entity.disk)
  ```
* Значения измерений не совпадают.

  Например, следующее выражение даст пустой результат, потому что разные значения измерений нельзя объединить.

  ```
  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-001))



  /



  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-002))
  ```

  Решение в этом случае: полностью убрать измерения с помощью [трансформации **splitBy**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Настройте metric selector для Metric v2 API.").

  ```
  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-001)):splitBy()



  /



  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-002)):splitBy()
  ```

  Ещё одна причина отсутствия совпадающих кортежей: применение [трансформации **limit**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#limit "Настройте metric selector для Metric v2 API.") к операнду выражения может привести к отфильтровыванию совпадающих измерений. **Всегда** применяйте трансформацию **limit** к результату выражения, а не к его операндам.

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
* Для метрики нет данных.

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

Почему я могу применить агрегацию, которую метрика не поддерживает?

После выполнения агрегации по пространству с помощью трансформации [**split by**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#splitby "Настройте metric selector для Metric v2 API.") или [**merge**](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#merge "Настройте metric selector для Metric v2 API.") к результату можно применить произвольные агрегации.

Например, можно выполнить следующий запрос, хотя метрика нативно не поддерживает процентили.

```
builtin:host.cpu.user:splitBy("dt.entity.host"):percentile(50)
```

Однако, поскольку метрика имеет только одно измерение (**dt.entity.host**), на самом деле никакие значения не агрегируются по пространству. Следовательно, агрегация `percentile(50)` даст тот же результат, что и `percentile(99)`, потому что оценка процентиля в этом случае основана только на одной точке данных.

## Приём метрик

Почему моя принятая точка данных недоступна?

Есть несколько причин, по которым точка данных может быть недоступна. Попробуйте следующие решения.

* Убедитесь, что вы получаете ответ с HTTP-кодом состояния `202` для endpoint-а приёма.
* Может пройти пара минут, прежде чем принятая точка данных станет доступна через Metrics REST API и в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных инсайтов."). Решение: подождать.
* Используйте дашборд **Metric & Dimension Usage + Rejections**, чтобы проверить, не была ли точка данных отклонена на более позднем этапе. Точка данных может быть принята endpoint-ом приёма, но позже отклонена, потому что был нарушен инвариант.
* Проверьте используемые фильтры. Точка данных может быть отфильтрована зоной управления или фильтром временного интервала.

Почему мои ключи метрик имеют суффикс '.count' или '.gauge'?

Метрики с разными [типами payload](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.") не могут иметь одинаковый ключ. Поэтому:

* метрики `count` автоматически получают суффикс `.count`, если их ключ метрики ещё не заканчивается на `.count` или `_count`
* метрики `gauge` автоматически получают суффикс `.gauge`, если их ключ заканчивается на `.count` или `_count`

Почему метаданные моей метрики не обновляются?

Записать метаданные метрики через [протокол приёма](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#metadata "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.") можно только если *они не были заданы ранее*. Чтобы обновить метаданные метрики, нужно использовать [metric browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser#metadata "Просматривайте метрики с помощью metrics browser Dynatrace.").

Почему принятое измерение отсутствует?

Если вы принимаете измерение с пустым значением, весь кортеж измерения отбрасывается во время приёма. Например, если вы принимаете `myMetric,dimEmpty="" 1`, измерение `dimEmpty` удаляется.