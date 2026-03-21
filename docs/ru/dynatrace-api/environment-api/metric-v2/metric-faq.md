---
title: Metrics API - часто задаваемые вопросы
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/metric-faq
scraped: 2026-03-04T21:34:23.609587
---

# Metrics API - FAQ


## Запрос метрик

Почему последняя метка времени в результате находится в будущем?

В Dynatrace точки данных метрик хранятся во временных слотах различного разрешения. Наименьшая гранулярность временного слота составляет одну минуту.
Метки времени, возвращаемые эндпоинтом запроса метрик, являются *временем окончания* этих временных слотов.

Например, если текущее время 09:24 и вы запрашиваете данные за последние 6 часов с разрешением 1 час, метка времени последней точки данных будет сегодня в 10:00. Подробнее см. [Примечание о временных рамках](get-data-points.md#timeframe-note "Read data points of one or multiple metrics via Metrics v2 API.").

Почему возвращаемые значения увеличиваются при большем временном диапазоне?

Точки данных, возвращаемые эндпоинтом запроса, агрегированы по времени. В зависимости от временных рамок запроса разрешение точек данных может составлять минуты, часы, дни или даже годы. Если вы запрашиваете больший временной диапазон, разрешение ваших данных, скорее всего, будет более грубым, что приведёт к большим значениям для таких агрегаций, как `sum` или `count`.

Если вы хотите получить сопоставимые результаты для различных разрешений, используйте [преобразование **rate**](metric-selector.md#rate "Configure the metric selector for the Metric v2 API."). Например, `:rate(1m)` предоставит вам значение в минуту.

Почему значение процентной метрики превышает 100% при использовании fold?

Например, следующий запрос может вернуть значения выше 100%, даже если единица измерения метрики — `Percent`.

```
builtin:host.availability:splitBy():avg:fold
```

Причина этой проблемы заключается в том, что при применении [преобразования **aggregation**](metric-selector.md#aggregation "Configure the metric selector for the Metric v2 API.") (вызов `:avg` в примере выше) семантика метрики теряется и становится недоступной для преобразований, которые выполняются позже в цепочке преобразований. То есть, когда вызывается [преобразование **fold**](metric-selector.md#fold "Configure the metric selector for the Metric v2 API."), информация о том, что значения должны быть усреднены, больше недоступна, и вместо этого применяется агрегация `sum`.

Чтобы предотвратить эту проблему, не выполняйте агрегацию перед преобразованием fold.

```
builtin:host.availability:splitBy():fold
```

Почему значение измерения равно null?

Если к измерению метрики применяется [top x](metric-selector.md#remainder "Configure the metric selector for the Metric v2 API."), сохраняются только *x* значений измерения. Все остальные значения измерения записываются в измерение `remainder`, которое имеет значение `null`.

Как получить понятные имена для отслеживаемых сущностей?

По умолчанию ответ запроса содержит только идентификаторы отслеживаемых сущностей (например, `HOST-E1784F5E3F9987CD`).

Если вы хотите, чтобы имя сущности также присутствовало в ответе, необходимо использовать [преобразование **names**](metric-selector.md#names "Configure the metric selector for the Metric v2 API."). Понятное имя затем будет доступно в `dimensionMap` под ключом измерения `dt.entity.<entityType>.name` (например, `dt.entity.host.name`).

Почему результат моего метрического выражения пуст?

Существует несколько причин, по которым метрическое выражение может дать пустой результат:

* Ключи измерений метрик, используемых в выражении, не совпадают.

  Если у вас есть метрики с разными ключами измерений, необходимо выровнять измерения метрик, чтобы сделать вычисление возможным. Для этого можно использовать преобразование [**split by**](metric-selector.md#splitby "Configure the metric selector for the Metric v2 API.") или [**merge**](metric-selector.md#merge "Configure the metric selector for the Metric v2 API."). Рассмотрим этот запрос:

  ```
  builtin:host.cpu.iowait


  /


  builtin:host.disk.throughput.read
  ```

  Он выдаст ошибку `Metric expression contains non-matching dimension-keys.`, потому что метрика **builtin:host.cpu.iowait** имеет только одно измерение (**dt.entity.host**), тогда как **builtin:host.disk.throughput.read** имеет два (**dt.entity.host** и **dt.entity.disk**). Чтобы запрос работал, необходимо избавиться от измерения disk (например, с помощью преобразования **merge**).

  ```
  builtin:host.cpu.iowait


  /


  builtin:host.disk.throughput.read:merge(dt.entity.disk)
  ```
* Значения измерений не совпадают.

  Например, следующее выражение вернёт пустой результат, потому что разные значения измерений не могут быть объединены.

  ```
  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-001))


  /


  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-002))
  ```

  Решение в этом случае — полностью убрать измерения с помощью [преобразования **splitBy**](metric-selector.md#splitby "Configure the metric selector for the Metric v2 API.").

  ```
  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-001)):splitBy()


  /


  builtin:host.cpu.iowait:filter(eq(dt.entity.host,HOST-002)):splitBy()
  ```

  Ещё одна причина, по которой нет совпадающих кортежей: применение [преобразования **limit**](metric-selector.md#limit "Configure the metric selector for the Metric v2 API.") к операнду выражения может привести к отфильтровыванию совпадающих измерений. **Всегда** применяйте преобразование **limit** к результату выражения, а не к его операндам.

  Рассмотрим следующий запрос, который пытается сложить 10 наибольших значений CPU usage с 10 наибольшими значениями CPU idle.

  ```
  builtin:host.cpu.usage:sort(value(avg,descending)):limit(10)


  +


  builtin:host.cpu.idle:sort(value(avg,descending)):limit(10)
  ```

  Если у вас большая среда с сотнями хостов, маловероятно, что 10 хостов с наибольшей загрузкой CPU окажутся среди 10 хостов с наибольшим временем простоя CPU. У операндов не будет совпадающих кортежей, поэтому результат выражения будет пустым. Решение — применить limit к результату выражения:

  ```
  (


  builtin:host.cpu.usage


  +


  builtin:host.cpu.idle


  )


  :sort(value(auto,descending))


  :limit(10)
  ```
* Данные для метрики отсутствуют.

  Рассмотрим этот пример выражения отношения, где мы вычисляем долю ошибок для ключевых пользовательских действий:

  ```
  builtin:apps.other.keyUserActions.reportedErrorCount.os


  /


  builtin:apps.other.keyUserActions.requestCount.os
  ```

  Если во временном диапазоне много запросов, но нет ни одной ошибки, результат будет пустым, хотя доля ошибок `0` была бы более информативной. Этого можно добиться с помощью преобразования `default(0)`:

  ```
  builtin:apps.other.keyUserActions.reportedErrorCount.os:default(0)


  /


  builtin:apps.other.keyUserActions.requestCount.os
  ```

Почему я могу применить агрегацию, которую метрика не поддерживает?

После выполнения пространственной агрегации с помощью преобразования [**split by**](metric-selector.md#splitby "Configure the metric selector for the Metric v2 API.") или [**merge**](metric-selector.md#merge "Configure the metric selector for the Metric v2 API.") вы можете применять произвольные агрегации к результату.

Например, вы можете выполнить следующий запрос, даже если метрика нативно не поддерживает перцентили.

```
builtin:host.cpu.user:splitBy("dt.entity.host"):percentile(50)
```

Однако, поскольку метрика имеет только одно измерение (**dt.entity.host**), фактически никакие значения не агрегируются пространственно. Следовательно, агрегация `percentile(50)` даст тот же результат, что и `percentile(99)`, потому что оценка перцентиля основана на одной точке данных в данном случае.

## Приём метрик

Почему моя принятая точка данных недоступна?

Существует несколько причин, по которым точка данных может быть недоступна. Попробуйте следующие решения.

* Убедитесь, что вы получаете ответ с HTTP-кодом `202` от эндпоинта приёма.
* Может потребоваться несколько минут, прежде чем принятая точка данных станет доступна через Metrics REST API и в [Data Explorer](../../../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights."). Решение — подождать.
* Используйте дашборд **Metric & Dimension Usage + Rejections**, чтобы проверить, не была ли точка данных отклонена на более позднем этапе. Точка данных может быть принята эндпоинтом приёма, но позже отклонена из-за нарушения инварианта.
* Проверьте используемые фильтры. Точка данных может быть отфильтрована зоной управления или фильтром временных рамок.

Почему к ключам моих метрик добавляются суффиксы '.count' или '.gauge'?

Метрики с разными [типами полезной нагрузки](../../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#payload "Learn how the data ingestion protocol for Dynatrace Metrics API works.") не могут иметь один и тот же ключ. Поэтому:

* Метрики типа `count` автоматически получают суффикс `.count`, если только ключ метрики не заканчивается на `.count` или `_count`
* Метрики типа `gauge` автоматически получают суффикс `.gauge`, если их ключ заканчивается на `.count` или `_count`

Почему метаданные моей метрики не обновляются?

Вы можете записать метаданные метрики через [протокол приёма](../../../ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol.md#metadata "Learn how the data ingestion protocol for Dynatrace Metrics API works.") только если *они не были установлены ранее*. Для обновления метаданных метрики необходимо использовать [браузер метрик](../../../analyze-explore-automate/dashboards-classic/metrics-browser.md#metadata "Browse metrics with the Dynatrace metrics browser.").

Почему принятое измерение отсутствует?

Если вы принимаете измерение с пустым значением, весь кортеж измерений удаляется во время приёма. Например, если вы принимаете `myMetric,dimEmpty="" 1`, измерение `dimEmpty` удаляется.
