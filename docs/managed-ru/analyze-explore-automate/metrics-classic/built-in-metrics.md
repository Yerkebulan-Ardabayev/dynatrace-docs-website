---
title: Встроенные метрики
source: https://docs.dynatrace.com/managed/analyze-explore-automate/metrics-classic/built-in-metrics
---

# Встроенные метрики

# Встроенные метрики

* Справочник
* 3 мин чтения
* Обновлено 24 июля 2026 г.

Каждая поддерживаемая Dynatrace технология предоставляет несколько «встроенных» метрик. Встроенные метрики включены в продукт из коробки, в некоторых случаях в составе встроенных расширений.

Метрики на основе расширений OneAgent или ActiveGate (префикс `ext:`) и вычисляемые метрики (префикс `calc:`) являются пользовательскими метриками, а не встроенными; [потребление DDU](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Узнайте, как рассчитывается потребление единиц данных Davis и затраты на отслеживаемые метрики.") для этих метрик может существенно варьироваться в зависимости от способа использования Dynatrace.

Префикс `ext:` используется метриками из [расширений OneAgent](/managed/ingest-from/extensions/develop-your-extensions "Разработайте собственные Extensions в Dynatrace.") и [расширений ActiveGate](/managed/ingest-from/extensions/develop-your-extensions "Разработайте собственные Extensions в Dynatrace."), а также [классическими метриками для интеграции AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Интеграция метрик из Amazon CloudWatch.").

Несмотря на сходство в названиях, метрики интеграции AWS **не** основаны на расширениях.

Чтобы просмотреть все метрики, доступные в **вашей** среде, используйте вызов API [GET metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "Список всех метрик, доступных в среде мониторинга, через API Metrics v2."). Рекомендуется использовать следующие параметры запроса:

* `pageSize=500`: для получения максимально возможного количества метрик в одном ответе.
* `fields=displayName,unit,aggregationTypes,dduBillable`: для получения того же набора полей, что отображается в этих таблицах.
* В зависимости от того, какие метрики нужно запросить, указать одно из следующих значений параметра **metricSelector**:

  + `metricSelector=ext:*`: для получения всех метрик из расширений.
  + `metricSelector=calc:*`: для получения всех вычисляемых метрик.
  + Не указывать параметр для получения **всех** метрик среды.

В следующих разделах описаны несоответствия и ограничения встроенных метрик Dynatrace.

Потребление метрик, генерируемое неопределёнными хостами

Когда хост активен хотя бы какое-то время в пределах 15-минутного расчётного окна, фиксируется отслеживаемое использование. В некоторых случаях хост может быть активен достаточно долго, чтобы сгенерировать отслеживаемое использование, но недостаточно долго для сохранения имени хоста в Dynatrace. В таких случаях хост отображается как **Undefined**.

Это затрагивает встроенные метрики мониторинга хостов, доступные по каждому хосту:

* `builtin:billing.foundation_and_discovery.metric_data_points.ingested_by_host`
* `builtin:billing.foundation_and_discovery.usage_per_host`
* `builtin:billing.full_stack_monitoring.metric_data_points.ingested_by_host`
* `builtin:billing.full_stack_monitoring.usage_per_host`
* `builtin:billing.infrastructure_monitoring.metric_data_points.ingested_by_host`
* `builtin:billing.infrastructure_monitoring.usage_per_host`

Метрики приложений и биллинга для мобильных и пользовательских приложений

Раздел [Other applications metrics](#other-applications-metrics) содержит метрики, собираемые для мобильных и пользовательских приложений. Эти метрики с префиксом `builtin:apps.other` собираются без указания типа приложения (мобильное или пользовательское). При этом [«биллинговые» метрики приложений](#apps) с префиксом `builtin:billing.apps` разделены по типам приложений:

* Мобильные приложения:

  + `builtin:billing.apps.mobile.sessionsWithoutReplayByApplication`
  + `builtin:billing.apps.mobile.sessionsWithReplayByApplication`
  + `builtin:billing.apps.mobile.userActionPropertiesByMobileApplication`
* Пользовательские приложения:

  + `builtin:billing.apps.custom.sessionsWithoutReplayByApplication`
  + `builtin:billing.apps.custom.userActionPropertiesByDeviceApplication`

Биллинговые метрики учитывают как оплачиваемые, так и неоплачиваемые сессии

Следующие «биллинговые» метрики подсчёта сессий представляют собой сумму оплачиваемых **и неоплачиваемых** пользовательских сессий.

* `builtin:billing.apps.custom.sessionsWithoutReplayByApplication`
* `builtin:billing.apps.mobile.sessionsWithReplayByApplication`
* `builtin:billing.apps.mobile.sessionsWithoutReplayByApplication`
* `builtin:billing.apps.web.sessionsWithReplayByApplication`
* `builtin:billing.apps.web.sessionsWithoutReplayByApplication`

Чтобы получить только количество оплачиваемых сессий, нужно установить фильтр **Type** в значение **Billed**.

Различные единицы измерения для метрик длительности запросов

Для аналогичных метрик длительности запросов для мобильных и пользовательских приложений используются разные единицы измерения.

`builtin:apps.other.keyUserActions.requestDuration.os` измеряется в микросекундах, тогда как другие метрики длительности запросов (`builtin:apps.other.requestTimes.osAndVersion` и `builtin:apps.other.requestTimes.osAndProvider`) измеряются в миллисекундах.

Пользовательские и встроенные метрики

Пользовательские метрики определяются или устанавливаются пользователем, тогда как встроенные метрики по умолчанию входят в состав продукта. Некоторые встроенные метрики отключены по умолчанию и при включении потребляют [DDU](/managed/license/classic-licensing/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU)."). Эти метрики охватывают широкий спектр поддерживаемых технологий: Apache Tomcat, NGINX, Couchbase, RabbitMQ, Cassandra, Jetty и многие другие.

Пользовательская метрика, это новый тип метрики с идентификатором и единицей измерения, задаваемыми пользователем. Семантика пользовательских метрик определяется пользователем и не входит в стандартную установку OneAgent. Пользовательские метрики отправляются в Dynatrace через [различные интерфейсы](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace."). После определения пользовательской метрики её можно передавать для нескольких отслеживаемых компонентов. Пользовательская метрика каждого компонента образует отдельный временной ряд.

Например, если определить новую пользовательскую метрику `Files count`, подсчитывающую вновь созданные файлы в каталоге, эту метрику можно собирать как для одного хоста, так и для двух отдельных хостов. Сбор одной и той же метрики для двух отдельных хостов даёт два временных ряда одного и того же типа пользовательской метрики, как показано в примере ниже:

![Custom metrics](https://dt-cdn.net/images/custommetrics2-1329-59422c6592.png)

Пользовательские метрики

Для целей [расчёта потребления мониторинга](/managed/license/classic-licensing/davis-data-units/metric-cost-calculation "Узнайте, как рассчитывается потребление единиц данных Davis и затраты на отслеживаемые метрики.") сбор одной и той же пользовательской метрики для двух хостов считается как две отдельные пользовательские метрики.

## Приложения

### Пользовательские

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:apps.custom.reportedErrorCount | Reported error count (by OS, app version) [custom]  Количество всех зафиксированных ошибок. | Count | autovalue |
| builtin:apps.custom.sessionCount | Session count (by OS, app version) [custom]  Количество захваченных пользовательских сессий. | Count | autovalue |

### Мобильные

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:apps.mobile.sessionCount | Session count (by OS, app version, crash replay feature status) [mobile]  Количество захваченных пользовательских сессий. | Count | autovalue |
| builtin:apps.mobile.sessionCount.sessionReplayStatus | Session count (by OS, app version, full replay feature status) [mobile]  Количество захваченных пользовательских сессий. | Count | autovalue |
| builtin:apps.mobile.reportedErrorCount | Reported error count (by OS, app version) [mobile]  Количество всех зафиксированных ошибок. | Count | autovalue |

### Веб-приложения

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| `builtin:apps.web.action.affectedUas` | Доля пользовательских действий, затронутых ошибками JavaScript (по key user action, user type) [web]  Процент key user actions с обнаруженными ошибками JavaScript. | Процент (%) | autovalue |
| `builtin:apps.web.action.apdex` | Apdex (по key user action) [web]  Средний рейтинг Apdex для key user actions. |  | autoavg |
| `builtin:apps.web.action.count.custom.browser` | Количество действий (custom action) (по key user action, browser) [web]  Количество custom actions, помеченных как key user actions. | Количество | autovalue |
| `builtin:apps.web.action.count.load.browser` | Количество действий (load action) (по key user action, browser) [web]  Количество load actions, помеченных как key user actions. | Количество | autovalue |
| `builtin:apps.web.action.count.xhr.browser` | Количество действий (XHR action) (по key user action, browser) [web]  Количество XHR actions, помеченных как key user actions. | Количество | autovalue |
| `builtin:apps.web.action.cumulativeLayoutShift.load.userType` | Cumulative Layout Shift (load action) (по key user action, user type) [web]  Показатель, измеряющий непредвиденное смещение видимых элементов веб-страницы. Вычисляется для load actions, помеченных как key user actions. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.cumulativeLayoutShift.load.userType.geo` | Cumulative Layout Shift (load action) (по key user action, geolocation, user type) [web]  Показатель, измеряющий непредвиденное смещение видимых элементов веб-страницы. Вычисляется для load actions, помеченных как key user actions. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.cumulativeLayoutShift.load.browser` | Cumulative Layout Shift (load action) (по key user action, browser) [web]  Показатель, измеряющий непредвиденное смещение видимых элементов веб-страницы. Вычисляется для load actions, помеченных как key user actions. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.domInteractive.load.browser` | DOM interactive (load action) (по key user action, browser) [web]  Время до момента, когда статус страницы устанавливается в «interactive» и она готова принимать ввод пользователя. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.duration.custom.browser` | Длительность действий (custom action) (по key user action, browser) [web]  Длительность custom actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.duration.load.browser` | Длительность действий (load action) (по key user action, browser) [web]  Длительность load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.duration.xhr.browser` | Длительность действий (XHR action) (по key user action, browser) [web]  Длительность XHR actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.firstByte.load.browser` | Время до первого байта (load action) (по key user action, browser) [web]  Время до получения первого байта ответа от сервера, соответствующих кэшей приложения или локального ресурса. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.firstByte.xhr.browser` | Время до первого байта (XHR action) (по key user action, browser) [web]  Время до получения первого байта ответа от сервера, соответствующих кэшей приложения или локального ресурса. Вычисляется для XHR actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.firstInputDelay.load.userType` | First Input Delay (load action) (по key user action, user type) [web]  Время от первого взаимодействия со страницей до момента, когда user agent может ответить на это взаимодействие. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.firstInputDelay.load.userType.geo` | First Input Delay (load action) (по key user action, geolocation, user type) [web]  Время от первого взаимодействия со страницей до момента, когда user agent может ответить на это взаимодействие. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.firstInputDelay.load.browser` | First Input Delay (load action) (по key user action, browser) [web]  Время от первого взаимодействия со страницей до момента, когда user agent может ответить на это взаимодействие. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.largestContentfulPaint.load.userType` | Largest Contentful Paint (load action) (по key user action, user type) [web]  Время до рендеринга наибольшего элемента в области просмотра. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.largestContentfulPaint.load.userType.geo` | Largest Contentful Paint (load action) (по key user action, geolocation, user type) [web]  Время до рендеринга наибольшего элемента в области просмотра. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.largestContentfulPaint.load.browser` | Largest Contentful Paint (load action) (по key user action, browser) [web]  Время до рендеринга наибольшего элемента в области просмотра. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.loadEventEnd.load.browser` | Конец события load (load action) (по key user action, browser) [web]  Время завершения события load страницы. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.loadEventStart.load.browser` | Начало события load (load action) (по key user action, browser) [web]  Время начала события load страницы. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.networkContribution.load` | Вклад сети (load action) (по key user action, user type) [web]  Время на запрос и получение ресурсов (включая DNS lookup, редирект и время установки TCP-соединения). Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.networkContribution.xhr` | Вклад сети (XHR action) (по key user action, user type) [web]  Время на запрос и получение ресурсов (включая DNS lookup, редирект и время установки TCP-соединения). Вычисляется для XHR actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.responseEnd.load.browser` | Конец ответа (load action) (по key user action, browser) [web]  (AKA HTML downloaded) Время до получения user agent'ом последнего байта ответа или закрытия транспортного соединения, в зависимости от того, что наступит раньше. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.responseEnd.xhr.browser` | Конец ответа (XHR action) (по key user action, browser) [web]  Время до получения user agent'ом последнего байта ответа или закрытия транспортного соединения, в зависимости от того, что наступит раньше. Вычисляется для XHR actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.serverContribution.load` | Вклад сервера (load action) (по key user action, user type) [web]  Время на серверную обработку страницы. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.serverContribution.xhr` | Вклад сервера (XHR action) (по key user action, user type) [web]  Время на серверную обработку страницы. Вычисляется для XHR actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.speedIndex.load.browser` | Speed index (load action) (по key user action, browser) [web]  Показатель, измеряющий скорость отрисовки видимых частей страницы. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.visuallyComplete.load.browser` | Visually complete (load action) (по key user action, browser) [web]  Время полной отрисовки содержимого в области просмотра. Вычисляется для load actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.visuallyComplete.xhr.browser` | Visually complete (XHR action) (по key user action, browser) [web]  Время полной отрисовки содержимого в области просмотра. Вычисляется для XHR actions, помеченных как key user actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.action.countOfErrors` | Количество ошибок (по key user action, user type, error type, error origin) [web]  Количество обнаруженных ошибок, произошедших во время key user actions. | Количество | autovalue |
| `builtin:apps.web.action.countOfUserActionsWithErrors` | Количество пользовательских действий с ошибками (по key user action, user type) [web]  Количество key user actions с обнаруженными ошибками. | Количество | autovalue |
| `builtin:apps.web.action.jsErrorsDuringUa` | Количество ошибок JavaScript во время пользовательских действий (по key user action, user type) [web]  Количество обнаруженных ошибок JavaScript, произошедших во время key user actions. | Количество | autovalue |
| `builtin:apps.web.action.jsErrorsWithoutUa` | Количество ошибок JavaScript без пользовательских действий (по key user action, user type) [web]  Количество обнаруженных отдельных ошибок JavaScript (произошедших между key user actions). | Количество | autovalue |
| `builtin:apps.web.action.percentageOfUserActionsAffectedByErrors` | Доля пользовательских действий, затронутых ошибками (по key user action, user type) [web]  Процент key user actions с обнаруженными ошибками. | Процент (%) | autovalue |
| `builtin:apps.web.actionCount.custom.browser` | Количество действий (custom action) (по browser) [web]  Количество custom actions. | Количество | autovalue |
| `builtin:apps.web.actionCount.load.browser` | Количество действий (load action) (по browser) [web]  Количество load actions. | Количество | autovalue |
| `builtin:apps.web.actionCount.xhr.browser` | Количество действий (XHR action) (по browser) [web]  Количество XHR actions. | Количество | autovalue |
| `builtin:apps.web.actionCount.category` | Количество действий (по категории Apdex) [web]  Количество пользовательских действий. | Количество | autovalue |
| `builtin:apps.web.actionCount.summary` | Количество действий с ключевой метрикой производительности (по типу действия, geolocation, user type) [web]  Количество пользовательских действий, для которых определена ключевая метрика производительности и сопоставлена геолокация. | Количество | autovalue |
| `builtin:apps.web.actionDuration.custom.browser` | Длительность действий (custom action) (по browser) [web]  Длительность custom actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.actionDuration.load.browser` | Длительность действий (load action) (по browser) [web]  Длительность load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.actionDuration.xhr.browser` | Длительность действий (XHR action) (по browser) [web]  Длительность XHR actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.actionsPerSession` | Среднее количество действий на сессию (по users, user type) [web]  Среднее количество пользовательских действий за одну пользовательскую сессию. | Количество | autoavg |
| `builtin:apps.web.activeSessions` | Количество сессий (оценочное количество активных сессий) (по users, user type) [web]  Оценочное количество активных пользовательских сессий. Активная сессия, это та, в которой подтверждена активность пользователя в данный момент. Для этой метрики с высокой кардинальностью применяется алгоритм HyperLogLog для приближённого подсчёта сессий. | Количество | autovalue |
| `builtin:apps.web.activeUsersEst` | Количество пользователей (оценочное количество активных пользователей) (по users, user type) [web]  Оценочное количество уникальных активных пользователей. Для этой метрики с высокой кардинальностью применяется алгоритм HyperLogLog для приближённого подсчёта пользователей. | Количество | autovalue |
| `builtin:apps.web.affectedUas` | Доля пользовательских действий, затронутых ошибками JavaScript (по user type) [web]  Процент пользовательских действий с обнаруженными ошибками JavaScript. | Процент (%) | autovalue |
| `builtin:apps.web.apdex.userType` | Apdex (по user type) [web] |  | autoavg |
| `builtin:apps.web.apdex.userType.geoBig` | Apdex (по geolocation, user type) [web]  Средний рейтинг Apdex для пользовательских действий с сопоставленной геолокацией. |  | autoavg |
| `builtin:apps.web.bouncedSessionRatio` | Показатель отказов (по users, user type) [web]  Процент сессий, в которых пользователи просмотрели только одну страницу и сформировали только один веб-запрос. Вычисляется делением одностраничных сессий на все сессии. | Процент (%) | autovalue |
| `builtin:apps.web.conversionRate` | Коэффициент конверсии (сессии) (по users, user type) [web]  Процент сессий, в которых достигнута хотя бы одна цель конверсии. Вычисляется делением конвертированных сессий на все сессии. | Процент (%) | autovalue |
| `builtin:apps.web.converted` | Количество сессий (конвертированные сессии) (по users, user type) [web]  Количество сессий, в которых достигнута хотя бы одна цель конверсии. | Количество | autovalue |
| `builtin:apps.web.cumulativeLayoutShift.load.userType` | Cumulative Layout Shift (load action) (по user type) [web]  Показатель, измеряющий непредвиденное смещение видимых элементов веб-страницы. Вычисляется для load actions. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.cumulativeLayoutShift.load.userType.geo` | Cumulative Layout Shift (load action) (по geolocation, user type) [web]  Показатель, измеряющий непредвиденное смещение видимых элементов веб-страницы. Вычисляется для load actions. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.cumulativeLayoutShift.load.browser` | Cumulative Layout Shift (load action) (по browser) [web]  Показатель, измеряющий непредвиденное смещение видимых элементов веб-страницы. Вычисляется для load actions. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.domInteractive.load.browser` | DOM interactive (load action) (по browser) [web]  Время до момента, когда статус страницы устанавливается в «interactive» и она готова принимать ввод пользователя. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.endedSessions` | Количество сессий (оценочное количество завершённых сессий) (по users, user type) [web]  Количество завершённых пользовательских сессий. | Количество | autovalue |
| `builtin:apps.web.event.count.rageClick` | Количество rage clicks [web]  Количество обнаруженных rage clicks. | Количество | autovalue |
| `builtin:apps.web.firstByte.load.browser` | Время до первого байта (load action) (по browser) [web]  Время до получения первого байта ответа от сервера, соответствующих кэшей приложения или локального ресурса. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.firstByte.xhr.browser` | Время до первого байта (XHR action) (по browser) [web]  Время до получения первого байта ответа от сервера, соответствующих кэшей приложения или локального ресурса. Вычисляется для XHR actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.firstInputDelay.load.userType` | First Input Delay (load action) (по user type) [web]  Время от первого взаимодействия со страницей до момента, когда user agent может ответить на это взаимодействие. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.firstInputDelay.load.userType.geo` | First Input Delay (load action) (по geolocation, user type) [web]  Время от первого взаимодействия со страницей до момента, когда user agent может ответить на это взаимодействие. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.firstInputDelay.load.browser` | First Input Delay (load action) (по browser) [web]  Время от первого взаимодействия со страницей до момента, когда user agent может ответить на это взаимодействие. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.largestContentfulPaint.load.userType` | Largest Contentful Paint (load action) (по user type) [web]  Время до рендеринга наибольшего элемента в области просмотра. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.largestContentfulPaint.load.userType.geo` | Largest Contentful Paint (load action) (по geolocation, user type) [web]  Время до рендеринга наибольшего элемента в области просмотра. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.largestContentfulPaint.load.browser` | Largest Contentful Paint (load action) (по browser) [web]  Время до рендеринга наибольшего элемента в области просмотра. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.loadEventEnd.load.browser` | Конец события load (load action) (по browser) [web]  Время завершения события load страницы. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.loadEventStart.load.browser` | Начало события load (load action) (по browser) [web]  Время начала события load страницы. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.networkContribution.load` | Вклад сети (load action) (по user type) [web]  Время на запрос и получение ресурсов (включая DNS lookup, редирект и время установки TCP-соединения). Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.networkContribution.xhr` | Вклад сети (XHR action) (по user type) [web]  Время на запрос и получение ресурсов (включая DNS lookup, редирект и время установки TCP-соединения). Вычисляется для XHR actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.responseEnd.load.browser` | Конец ответа (load action) (по browser) [web]  (AKA HTML downloaded) Время до получения user agent'ом последнего байта ответа или закрытия транспортного соединения, в зависимости от того, что наступит раньше. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.responseEnd.xhr.browser` | Конец ответа (XHR action) (по browser) [web]  Время до получения user agent'ом последнего байта ответа или закрытия транспортного соединения, в зависимости от того, что наступит раньше. Вычисляется для XHR actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.serverContribution.load` | Вклад сервера (load action) (по user type) [web]  Время на серверную обработку страницы. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.serverContribution.xhr` | Вклад сервера (XHR action) (по user type) [web]  Время на серверную обработку страницы. Вычисляется для XHR actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.sessionDuration` | Длительность сессии (по users, user type) [web]  Средняя длительность пользовательских сессий. | Микросекунда | autoavg |
| `builtin:apps.web.speedIndex.load.browser` | Speed index (load action) (по browser) [web]  Показатель, измеряющий скорость отрисовки видимых частей страницы. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.startedSessions` | Количество сессий (оценочное количество начатых сессий) (по users, user type) [web]  Количество начатых пользовательских сессий. | Количество | autovalue |
| `builtin:apps.web.visuallyComplete.load.browser` | Visually complete (load action) (по browser) [web]  Время полной отрисовки содержимого в области просмотра. Вычисляется для load actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.visuallyComplete.xhr.browser` | Visually complete (XHR action) (по browser) [web]  Время полной отрисовки содержимого в области просмотра. Вычисляется для XHR actions. | Миллисекунда | autoavgcountmaxmedianminpercentilesum |
| `builtin:apps.web.countOfErrors` | Количество ошибок (по user type, error type, error origin) [web]  Количество обнаруженных ошибок. | Количество | autovalue |
| `builtin:apps.web.countOfErrorsDuringUserActions` | Количество ошибок во время пользовательских действий (по user type, error type, error origin) [web]  Количество обнаруженных ошибок, произошедших во время пользовательских действий. | Количество | autovalue |
| `builtin:apps.web.countOfStandaloneErrors` | Количество отдельных ошибок (по user type, error type, error origin) [web]  Количество обнаруженных отдельных ошибок (произошедших между пользовательскими действиями). | Количество | autovalue |
| `builtin:apps.web.countOfUserActionsWithErrors` | Количество пользовательских действий с ошибками (по user type) [web]  Количество пользовательских действий с обнаруженными ошибками. | Количество | autovalue |
| `builtin:apps.web.errorCountForDavis` | Количество ошибок для Davis (по user type, error type, error origin, error context)) [web]  Количество ошибок, включённых в анализ и обнаружение проблем Davis AI. | Количество | autovalue |
| `builtin:apps.web.interactionToNextPaint` | Interaction to next paint | Миллисекунда | autocountmaxmedianminpercentile |
| `builtin:apps.web.jsErrorsDuringUa` | Количество ошибок JavaScript во время пользовательских действий (по user type) [web]  Количество обнаруженных ошибок JavaScript, произошедших во время пользовательских действий. | Количество | autovalue |
| `builtin:apps.web.jsErrorsWithoutUa` | Количество ошибок JavaScript без пользовательских действий (по user type) [web]  Количество обнаруженных отдельных ошибок JavaScript (произошедших между пользовательскими действиями). | Количество | autovalue |
| `builtin:apps.web.percentageOfUserActionsAffectedByErrors` | Доля пользовательских действий, затронутых ошибками (по user type) [web]  Процент пользовательских действий с обнаруженными ошибками. | Процент (%) | autovalue |

### Мобильные и пользовательские приложения

| Metric key | Название и описание | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:apps.other.apdex.osAndGeo | Apdex (по ОС, геолокации) [mobile, custom]  Рейтинг Apdex для всех зафиксированных пользовательских действий. |  | autovalue |
| builtin:apps.other.apdex.osAndVersion | Apdex (по ОС, версии приложения) [mobile, custom]  Рейтинг Apdex для всех зафиксированных пользовательских действий. |  | autovalue |
| builtin:apps.other.crashAffectedUsers.os | Количество пользователей, приблизительно затронутых сбоями (по ОС) [mobile, custom]  Приблизительное число уникальных пользователей, затронутых сбоем. Для этой метрики с высокой кардинальностью используется алгоритм HyperLogLog для приближённого подсчёта числа пользователей. | Count | autovalue |
| builtin:apps.other.crashAffectedUsers.osAndVersion-std | Количество пользователей, приблизительно затронутых сбоями (по ОС, версии приложения) [mobile, custom]  Приблизительное число уникальных пользователей, затронутых сбоем. Для этой метрики с высокой кардинальностью используется алгоритм HyperLogLog для приближённого подсчёта числа пользователей. | Count | autovalue |
| builtin:apps.other.crashAffectedUsersRate.os | Доля пользователей, приблизительно затронутых сбоями (по ОС) [mobile, custom]  Приблизительный процент уникальных пользователей, затронутых сбоем. Для этой метрики с высокой кардинальностью используется алгоритм HyperLogLog для приближённого подсчёта числа пользователей. | Percent (%) | autovalue |
| builtin:apps.other.crashCount.osAndGeo | Количество сбоев (по ОС, геолокации) [mobile, custom]  Число обнаруженных сбоев. | Count | autovalue |
| builtin:apps.other.crashCount.osAndVersion | Количество сбоев (по ОС, версии приложения) [mobile, custom]  Число обнаруженных сбоев. | Count | autovalue |
| builtin:apps.other.crashCount.osAndVersion-std | Количество сбоев (по ОС, версии приложения) [mobile, custom]  Число обнаруженных сбоев. | Count | autovalue |
| builtin:apps.other.crashFreeUsersRate.os | Доля пользователей, приблизительно не затронутых сбоями (по ОС) [mobile, custom]  Приблизительный процент уникальных пользователей, не затронутых сбоем. Для этой метрики с высокой кардинальностью используется алгоритм HyperLogLog для приближённого подсчёта числа пользователей. | Percent (%) | autovalue |
| builtin:apps.other.keyUserActions.apdexValue.os | Apdex (по ключевому пользовательскому действию, ОС) [mobile, custom]  Рейтинг Apdex для всех зафиксированных ключевых пользовательских действий. |  | autovalue |
| builtin:apps.other.keyUserActions.count.osAndApdex | Количество действий (по ключевому пользовательскому действию, ОС, категории Apdex) [mobile, custom]  Число зафиксированных ключевых пользовательских действий. | Count | autovalue |
| builtin:apps.other.keyUserActions.duration.os | Длительность действия (по ключевому пользовательскому действию, ОС) [mobile, custom]  Длительность ключевых пользовательских действий. | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.keyUserActions.reportedErrorCount.os | Количество зафиксированных ошибок (по ключевому пользовательскому действию, ОС) [mobile, custom]  Число зафиксированных ошибок для ключевых пользовательских действий. | Count | autovalue |
| builtin:apps.other.keyUserActions.requestCount.os | Количество запросов (по ключевому пользовательскому действию, ОС) [mobile, custom]  Число зафиксированных веб-запросов, связанных с ключевыми пользовательскими действиями. | Count | autovalue |
| builtin:apps.other.keyUserActions.requestDuration.os | Длительность запроса (по ключевому пользовательскому действию, ОС) [mobile, custom]  Длительность веб-запросов для ключевых пользовательских действий. Обратите внимание: эта метрика измеряется в микросекундах, тогда как другие метрики длительности запросов для мобильных и пользовательских приложений измеряются в миллисекундах. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.keyUserActions.requestErrorCount.os | Количество ошибок запросов (по ключевому пользовательскому действию, ОС) [mobile, custom]  Число обнаруженных ошибок веб-запросов для ключевых пользовательских действий. | Count | autovalue |
| builtin:apps.other.keyUserActions.requestErrorRate.os | Доля ошибок запросов (по ключевому пользовательскому действию, ОС) [mobile, custom]  Процент веб-запросов с обнаруженными ошибками для ключевых пользовательских действий. | Percent (%) | autovalue |
| builtin:apps.other.newUsers.os | Количество новых пользователей (по ОС) [mobile, custom]  Число пользователей, запустивших приложение впервые. Метрика привязана к конкретным устройствам, поэтому пользователь считается несколько раз, если устанавливает приложение на нескольких устройствах. Метрика не различает нескольких пользователей, совместно использующих одно устройство и одну установку приложения. | Count | autovalue |
| builtin:apps.other.requestCount.osAndProvider | Количество запросов (по ОС, провайдеру) [mobile, custom]  Число зафиксированных веб-запросов. | Count | autovalue |
| builtin:apps.other.requestCount.osAndVersion | Количество запросов (по ОС, версии приложения) [mobile, custom]  Число зафиксированных веб-запросов. | Count | autovalue |
| builtin:apps.other.requestErrorCount.osAndProvider | Количество ошибок запросов (по ОС, провайдеру) [mobile, custom]  Число обнаруженных ошибок веб-запросов. | Count | autovalue |
| builtin:apps.other.requestErrorCount.osAndVersion | Количество ошибок запросов (по ОС, версии приложения) [mobile, custom]  Число обнаруженных ошибок веб-запросов. | Count | autovalue |
| builtin:apps.other.requestErrorRate.osAndProvider | Доля ошибок запросов (по ОС, провайдеру) [mobile, custom]  Процент веб-запросов с обнаруженными ошибками. | Percent (%) | autovalue |
| builtin:apps.other.requestErrorRate.osAndVersion | Доля ошибок запросов (по ОС, версии приложения) [mobile, custom]  Процент веб-запросов с обнаруженными ошибками. | Percent (%) | autovalue |
| builtin:apps.other.requestTimes.osAndProvider | Длительность запроса (по ОС, провайдеру) [mobile, custom]  Длительность веб-запросов. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.requestTimes.osAndVersion | Длительность запроса (по ОС, версии приложения) [mobile, custom]  Длительность веб-запросов. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.sessionCount.agentVersionAndOs | Количество сессий (по версии агента, ОС) [mobile, custom]  Число зафиксированных пользовательских сессий. | Count | autovalue |
| builtin:apps.other.sessionCount.osAndCrashReportingLevel | Количество сессий (по ОС, уровню отчётности о сбоях) [mobile, custom]  Число зафиксированных пользовательских сессий. | Count | autovalue |
| builtin:apps.other.sessionCount.osAndDataCollectionLevel | Количество сессий (по ОС, уровню сбора данных) [mobile, custom]  Число зафиксированных пользовательских сессий. | Count | autovalue |
| builtin:apps.other.sessionCount.osAndGeo | Приблизительное количество сессий (по ОС, геолокации) [mobile, custom]  Приблизительное число зафиксированных пользовательских сессий. Для этой метрики с высокой кардинальностью используется алгоритм HyperLogLog для приближённого подсчёта числа сессий. | Count | autovalue |
| builtin:apps.other.sessionCount.osAndVersion-std | Количество сессий (по ОС, версии приложения) [mobile, custom]  Число зафиксированных пользовательских сессий. | Count | autovalue |
| builtin:apps.other.uaCount.geoAndApdex | Количество действий (по геолокации, категории Apdex) [mobile, custom]  Число зафиксированных пользовательских действий. | Count | autovalue |
| builtin:apps.other.uaCount.osAndApdex | Количество действий (по ОС, категории Apdex) [mobile, custom]  Число зафиксированных пользовательских действий. | Count | autovalue |
| builtin:apps.other.uaCount.osAndVersion | Количество действий (по ОС, версии приложения) [mobile, custom]  Число зафиксированных пользовательских действий. | Count | autovalue |
| builtin:apps.other.uaDuration.osAndVersion | Длительность действия (по ОС, версии приложения) [mobile, custom]  Длительность пользовательских действий. | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:apps.other.userCount.osAndGeo | Приблизительное количество пользователей (по ОС, геолокации) [mobile, custom]  Приблизительное число уникальных пользователей с определённой геолокацией. Метрика основана на `internalUserId`. Когда `dataCollectionLevel` установлен в `performance` или `off`, значение `internalUserId` обновляется при каждом запуске приложения. Для этой метрики с высокой кардинальностью используется алгоритм HyperLogLog для приближённого подсчёта числа пользователей. | Count | autovalue |
| builtin:apps.other.userCount.osAndVersion-std | Приблизительное количество пользователей (по ОС, версии приложения) [mobile, custom]  Приблизительное число уникальных пользователей. Метрика основана на `internalUserId`. Когда `dataCollectionLevel` установлен в `performance` или `off`, значение `internalUserId` обновляется при каждом запуске приложения. Для этой метрики с высокой кардинальностью используется алгоритм HyperLogLog для приближённого подсчёта числа пользователей. | Count | autovalue |

## Billing

### Applications

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:billing.apps.custom.sessionsWithoutReplayByApplication | Количество сессий: тарифицируемые и нетарифицируемые [custom]  Количество тарифицируемых и нетарифицируемых пользовательских сессий. Чтобы получить только тарифицируемые сессии, установите фильтр "Type" в значение "Billed". | Count | autovalue |
| builtin:billing.apps.custom.userActionPropertiesByDeviceApplication | Суммарные свойства действий пользователя и сессий  Количество тарифицируемых свойств действий пользователя и пользовательских сессий. | Count | autovalue |
| builtin:billing.apps.mobile.sessionsWithReplayByApplication | Количество сессий: тарифицируемые и нетарифицируемые, с Session Replay [mobile]  Количество тарифицируемых и нетарифицируемых пользовательских сессий, содержащих данные Session Replay. Чтобы получить только тарифицируемые сессии, установите фильтр "Type" в значение "Billed". | Count | autovalue |
| builtin:billing.apps.mobile.sessionsWithoutReplayByApplication | Количество сессий: тарифицируемые и нетарифицируемые [mobile]  Общее количество тарифицируемых и нетарифицируемых пользовательских сессий (с данными Session Replay и без них). Чтобы получить только тарифицируемые сессии, установите фильтр "Type" в значение "Billed". | Count | autovalue |
| builtin:billing.apps.mobile.userActionPropertiesByMobileApplication | Суммарные свойства действий пользователя и сессий  Количество тарифицируемых свойств действий пользователя и пользовательских сессий. | Count | autovalue |
| builtin:billing.apps.web.sessionsWithReplayByApplication | Количество сессий: тарифицируемые и нетарифицируемые, с Session Replay [web]  Количество тарифицируемых и нетарифицируемых пользовательских сессий, содержащих данные Session Replay. Чтобы получить только тарифицируемые сессии, установите фильтр "Type" в значение "Billed". | Count | autovalue |
| builtin:billing.apps.web.sessionsWithoutReplayByApplication | Количество сессий: тарифицируемые и нетарифицируемые, без Session Replay [web]  Количество тарифицируемых и нетарифицируемых пользовательских сессий, не содержащих данные Session Replay. Чтобы получить только тарифицируемые сессии, установите фильтр "Type" в значение "Billed". | Count | autovalue |
| builtin:billing.apps.web.userActionPropertiesByApplication | Суммарные свойства действий пользователя и сессий  Количество тарифицируемых свойств действий пользователя и пользовательских сессий. | Count | autovalue |

### Custom events classic

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:billing.custom\_events\_classic.usage | (DPS) Суммарное использование биллинга Custom Events Classic  Количество пользовательских событий, принятых в систему, агрегированное по всем отслеживаемым сущностям. Пользовательские события включают события, отправленные в Dynatrace через Events API, а также события, созданные правилом извлечения событий из журнала. Используйте эту суммарную метрику для запросов по длительным временным диапазонам без потери точности и производительности. | Count | autovalue |
| builtin:billing.custom\_events\_classic.usage\_by\_entity | (DPS) Использование биллинга Custom Events Classic по отслеживаемой сущности  Количество пользовательских событий, принятых в систему, с разбивкой по отслеживаемым сущностям. Пользовательские события включают события, отправленные в Dynatrace через Events API, а также события, созданные правилом извлечения событий из журнала. Подробнее о тарифицируемых событиях см. метрику usage\_by\_event\_info. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными диапазонами используйте суммарную метрику. | Count | autovalue |
| builtin:billing.custom\_events\_classic.usage\_by\_event\_info | (DPS) Использование биллинга Custom Events Classic по информации о событии  Количество пользовательских событий, принятых в систему, с разбивкой по информации о событии. Пользовательские события включают события, отправленные в Dynatrace через Events API, а также события, созданные правилом извлечения событий из журнала. Информация содержит контекст события и идентификатор конфигурации. Подробнее о связанных отслеживаемых сущностях см. метрику usage\_by\_entity. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными диапазонами используйте суммарную метрику. | Count | autovalue |

### Custom metrics classic

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:billing.custom\_metrics\_classic.raw.usage\_by\_metric\_key | (DPS) Записанные точки данных метрик по ключу метрики  Количество зарегистрированных точек данных метрик с разбивкой по ключу метрики. Эта метрика не учитывает включённые точки данных метрик, доступные в вашей среде. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage | (DPS) Суммарные тарифицируемые точки данных метрик  Общее количество точек данных метрик после вычета включённых точек данных. Это значение тарифной карточки, используемое для биллинга. Используйте эту суммарную метрику для запросов по длительным временным диапазонам без потери точности и производительности. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.foundation\_and\_discovery | (DPS) Суммарные точки данных метрик, тарифицируемые для хостов Foundation & Discovery  Количество точек данных метрик, тарифицируемых для хостов Foundation & Discovery. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.fullstack\_hosts | (DPS) Суммарные точки данных метрик, тарифицируемые для Full-Stack хостов  Количество точек данных метрик, тарифицируемых для Full-Stack хостов. Чтобы просмотреть нескорректированное использование по хосту, используйте builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested\_by\_host . Эта запаздывающая метрика публикуется с интервалом 15 минут и задержкой до 15 минут. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.infrastructure\_hosts | (DPS) Суммарные точки данных метрик, тарифицируемые для хостов под мониторингом Infrastructure  Количество точек данных метрик, тарифицируемых для хостов под мониторингом Infrastructure. Чтобы просмотреть нескорректированное использование по хосту, используйте builtin:billing.infrastructure\_monitoring.metric\_data\_points.ingested\_by\_host . Эта запаздывающая метрика публикуется с интервалом 15 минут и задержкой до 15 минут. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.other | (DPS) Суммарные точки данных метрик, тарифицируемые по прочим сущностям  Количество тарифицируемых точек данных метрик, которые не могут быть отнесены к хосту. Значения, передаваемые в этой метрике, не участвуют во вычете включённых метрик и тарифицируются без изменений. Эта запаздывающая метрика публикуется с интервалом 15 минут и задержкой до 15 минут. о просмотре отслеживаемых сущностей, потребляющих это использование, используйте метрику other\_by\_entity. | Count | autovalue |
| builtin:billing.custom\_metrics\_classic.usage.other\_by\_entity | (DPS) Тарифицируемые точки данных метрик, переданные с разбивкой по прочим сущностям  Количество тарифицируемых точек данных метрик с разбивкой по сущностям, которые не могут быть отнесены к хосту. Значения, передаваемые в этой метрике, не участвуют во вычете включённых метрик и тарифицируются без изменений. Эта запаздывающая метрика публикуется с интервалом 15 минут и задержкой до 15 минут. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными диапазонами используйте суммарную метрику. | Count | autovalue |

### Custom traces classic

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:billing.custom\_traces\_classic.usage | (DPS) Суммарное использование биллинга Custom Traces Classic  Количество span'ов, принятых в систему, агрегированное по всем отслеживаемым сущностям. Span, это единичная операция внутри распределённой трассировки, принятая в Dynatrace. Используйте эту суммарную метрику для запросов по длительным временным диапазонам без потери точности и производительности. | Count | autovalue |
| builtin:billing.custom\_traces\_classic.usage\_by\_entity | (DPS) Использование биллинга Custom Traces Classic по отслеживаемой сущности  Количество span'ов, принятых в систему, с разбивкой по отслеживаемым сущностям. Span, это единичная операция внутри распределённой трассировки, принятая в Dynatrace. Подробнее о типах span'ов см. метрику usage\_by\_span\_type. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными диапазонами используйте суммарную метрику. | Count | autovalue |
| builtin:billing.custom\_traces\_classic.usage\_by\_span\_type | (DPS) Использование биллинга Custom Traces Classic по типу span'а  Количество span'ов, принятых в систему, с разбивкой по типу span'а. Span, это единичная операция внутри распределённой трассировки, принятая в Dynatrace. Виды span'ов: CLIENT, SERVER, PRODUCER, CONSUMER или INTERNAL. Подробнее о связанных отслеживаемых сущностях см. метрику usage\_by\_entity. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными диапазонами используйте суммарную метрику. | Count | autovalue |

### DDU

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.ddu.events.byDescription | Потребление DDU событий по описанию события  Лицензионное потребление Davis data units из пула событий с разбивкой по информации о событии |  | autovalue |
| builtin:billing.ddu.events.byEntity | Потребление DDU событий по отслеживаемой сущности  Лицензионное потребление Davis data units из пула событий с разбивкой по отслеживаемой сущности |  | autovalue |
| builtin:billing.ddu.events.total | Общее потребление DDU событий  Суммарное лицензионное потребление Davis data units по всем отслеживаемым сущностям в пуле событий |  | autovalue |
| builtin:billing.ddu.log.byDescription | Потребление DDU логов по пути к лог-файлу  Лицензионное потребление Davis data units из пула логов с разбивкой по пути к лог-файлу |  | autovalue |
| builtin:billing.ddu.log.byEntity | Потребление DDU логов по отслеживаемой сущности  Лицензионное потребление Davis data units из пула логов с разбивкой по отслеживаемой сущности |  | autovalue |
| builtin:billing.ddu.log.total | Общее потребление DDU логов  Суммарное лицензионное потребление Davis data units по всем логам в пуле логов |  | autovalue |
| builtin:billing.ddu.metrics.byEntity | Потребление DDU метрик по отслеживаемой сущности  Лицензионное потребление Davis data units из пула метрик с разбивкой по отслеживаемой сущности |  | autovalue |
| builtin:billing.ddu.metrics.byEntityRaw | Потребление DDU метрик по отслеживаемой сущности без учёта DDU, включённых в host unit  Лицензионное потребление Davis data units из пула метрик с разбивкой по отслеживаемой сущности (агрегирует метрики, включённые в host unit, поэтому значение может быть выше фактического потребления) |  | autovalue |
| builtin:billing.ddu.metrics.byMetric | DDU зарегистрированных метрик по ключу метрики  Использование Davis data units из пула метрик с разбивкой по ключу метрики |  | autovalue |
| builtin:billing.ddu.metrics.total | Общее потребление DDU метрик  Суммарное лицензионное потребление Davis data units по всем метрикам в пуле метрик |  | autovalue |
| builtin:billing.ddu.serverless.byDescription | Потребление DDU serverless по функции  Лицензионное потребление Davis data units из пула serverless с разбивкой по Amazon Resource Names (ARN) |  | autovalue |
| builtin:billing.ddu.serverless.byEntity | Потребление DDU serverless по сервису  Лицензионное потребление Davis data units из пула serverless с разбивкой по сервису |  | autovalue |
| builtin:billing.ddu.serverless.total | Общее потребление DDU serverless  Суммарное лицензионное потребление Davis data units по всем сервисам в пуле serverless |  | autovalue |
| builtin:billing.ddu.traces.byDescription | Потребление DDU трейсов по типу спана  Лицензионное потребление Davis data units из пула трейсов с разбивкой по SpanKind в соответствии со спецификацией OpenTelemetry |  | autovalue |
| builtin:billing.ddu.traces.byEntity | Потребление DDU трейсов по отслеживаемой сущности  Лицензионное потребление Davis data units из пула трейсов с разбивкой по отслеживаемой сущности |  | autovalue |
| builtin:billing.ddu.traces.total | Общее потребление DDU трейсов  Суммарное лицензионное потребление Davis data units по всем отслеживаемым сущностям в пуле трейсов |  | autovalue |
| builtin:billing.ddu.includedMetricDduPerHost | DDU, включённые на хост  Включённые Davis data units на хост |  | autovalue |
| builtin:billing.ddu.includedMetricPerHost | Включённые точки данных метрик на хост  Включённые точки данных метрик на хост |  | autovalue |

### Events

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.events.business\_events.ingest.usage | [Deprecated] (DPS) Использование business events, Ingest & Process  Использование business events в части Ingest & Process, отслеживается в байтах, принятых за час. Это запаздывающая метрика, сообщается ежечасно за предыдущий час. Значения метрик поступают с задержкой до одного часа. [Deprecated] Метрика заменена событиями биллингового использования. | Byte | autovalue |
| builtin:billing.events.business\_events.query.usage | [Deprecated] (DPS) Использование business events, Query  Использование business events в части Query, отслеживается в байтах, прочитанных за час. Это запаздывающая метрика, сообщается ежечасно за предыдущий час. Значения метрик поступают с задержкой до одного часа. [Deprecated] Метрика заменена событиями биллингового использования. | Byte | autovalue |
| builtin:billing.events.business\_events.retain.usage | [Deprecated] (DPS) Использование business events, Retain  Использование business events в части Retain, отслеживается как общий объём хранилища за час в байтах. Это запаздывающая метрика, сообщается ежечасно за предыдущий час. Значения метрик поступают с задержкой до одного часа. [Deprecated] Метрика заменена событиями биллингового использования. | Byte | autoavgmaxmin |

### Foundation and discovery

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.foundation\_and\_discovery.metric\_data\_points.ingested | (DPS) Принятые точки данных метрик для Foundation & Discovery  Количество точек данных метрик, агрегированных по всем хостам Foundation & Discovery. | Count | autovalue |
| builtin:billing.foundation\_and\_discovery.metric\_data\_points.ingested\_by\_host | (DPS) Принятые точки данных метрик для Foundation & Discovery на хост  Количество точек данных метрик с разбивкой по хостам Foundation & Discovery. См. [подробнее﻿](https://dt-url.net/et231ii). | Count | autovalue |
| builtin:billing.foundation\_and\_discovery.usage | (DPS) Биллинговое использование Foundation & Discovery  Общее количество хосто-часов, отслеживаемых через Foundation & Discovery, с учётом интервалов по 15 минут. | Count | autovalue |
| builtin:billing.foundation\_and\_discovery.usage\_per\_host | (DPS) Биллинговое использование Foundation & Discovery на хост  Хосто-часы, отслеживаемые через Foundation & Discovery, с учётом интервалов по 15 минут. См. [подробнее﻿](https://dt-url.net/et231ii). | Count | autovalue |

### Full stack monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.full\_stack\_monitoring.metric\_data\_points.included | (DPS) Доступные включённые точки данных метрик для Full-Stack хостов  Общее количество включённых точек данных метрик, которые можно вычесть из точек данных, зафиксированных Full-Stack хостами. Это запаздывающая метрика, сообщается с интервалом 15 минут и задержкой до 15 минут. Чтобы просмотреть количество применённых включённых точек данных метрик, используйте builtin:billing.full\_stack\_monitoring.metric\_data\_points.included\_used . Если разница между этой метрикой и применёнными метриками больше 0, значит через Full-Stack Monitoring можно принять дополнительные метрики без дополнительных затрат. | Count | autovalue |
| builtin:billing.full\_stack\_monitoring.metric\_data\_points.included\_used | (DPS) Использованные включённые точки данных метрик для Full-Stack хостов  Количество потреблённых включённых точек данных метрик на хост, отслеживаемый через Full-Stack Monitoring. Это запаздывающая метрика, сообщается с интервалом 15 минут и задержкой до 15 минут. Чтобы просмотреть потенциально доступное количество включённых метрик, используйте builtin:billing.full\_stack\_monitoring.metric\_data\_points.included\_used . Если разница между этой метрикой и доступными метриками больше нуля, это означает, что на Full-Stack хостах можно принять дополнительные метрики без дополнительных затрат. | Count | autovalue |
| builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested | (DPS) Суммарное количество точек данных метрик, зафиксированных Full-Stack хостами  Количество точек данных метрик, агрегированных по всем Full-Stack хостам. Значения этой метрики учитываются при вычете включённых точек данных метрик. Используйте эту суммарную метрику для запросов по длинным временным диапазонам без потери точности и производительности. Это запаздывающая метрика, сообщается с интервалом 15 минут и задержкой до 15 минут. Чтобы просмотреть использование по каждому хосту отдельно, используйте builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested\_by\_host . | Count | autovalue |
| builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested\_by\_host | (DPS) Точки данных метрик, зафиксированные и разбитые по Full-Stack хостам  Количество точек данных метрик с разбивкой по Full-Stack хостам. Значения этой метрики учитываются при вычете включённых точек данных метрик. Это запаздывающая метрика, сообщается с интервалом 15 минут и задержкой до 15 минут. Пул доступных включённых метрик за «15-минутный интервал» отображается через builtin:billing.full\_stack\_monitoring.metric\_data\_points.included . Для повышения производительности и предотвращения превышения лимитов запросов при работе с длинными временными диапазонами используйте суммарную метрику. См. [подробнее﻿](https://dt-url.net/et231ii). | Count | autovalue |
| builtin:billing.full\_stack\_monitoring.usage | (DPS) Биллинговое использование Full-Stack Monitoring  Суммарный объём памяти (GiB) хостов, отслеживаемых в режиме full-stack, с учётом интервалов по 15 минут. Используйте эту суммарную метрику для запросов по длинным временным диапазонам без потери точности и производительности. Для просмотра хостов, формирующих потребление, обратитесь к метрике usage\_per\_host. Для просмотра контейнеров, формирующих потребление, обратитесь к метрике usage\_per\_container. | GibiByte | autovalue |
| builtin:billing.full\_stack\_monitoring.usage\_per\_container | (DPS) Использование Full-Stack по типу контейнера  Суммарный объём памяти (GiB) контейнеров, отслеживаемых в режиме full-stack, с учётом интервалов по 15 минут. | GibiByte | autovalue |
| builtin:billing.full\_stack\_monitoring.usage\_per\_host | (DPS) Биллинговое использование Full-Stack Monitoring на хост  Объём памяти (GiB) на хост, отслеживаемый в режиме full-stack, с учётом интервалов по 15 минут. Например, хост с 8 GiB оперативной памяти, отслеживаемый в течение 1 часа, формирует 4 точки данных со значением `2`. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длинными временными диапазонами используйте суммарную метрику. См. [подробнее﻿](https://dt-url.net/et231ii). | GibiByte | autovalue |

### Infrastructure monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.infrastructure\_monitoring.metric\_data\_points.included | (DPS) Доступные включённые точки метрик для хостов, мониторируемых в режиме Infrastructure  Общее количество включённых точек метрик, которые можно вычесть из точек метрик, передаваемых хостами, мониторируемыми в режиме Infrastructure. Эта запаздывающая метрика передаётся с интервалом 15 минут с задержкой до 15 минут. Чтобы посмотреть количество применённых включённых точек метрик, нужно использовать builtin:billing.infrastructure\_monitoring.metric\_data\_points.included\_used . Если разница между этой метрикой и применёнными метриками больше нуля, значит на хостах, мониторируемых в режиме Infrastructure, можно принимать больше метрик без дополнительных расходов. | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.metric\_data\_points.included\_used | (DPS) Использованные включённые точки метрик для хостов, мониторируемых в режиме Infrastructure  Количество потреблённых включённых точек метрик для хостов, мониторируемых в режиме Infrastructure. Эта запаздывающая метрика передаётся с интервалом 15 минут с задержкой до 15 минут. Чтобы посмотреть количество потенциально доступных включённых метрик, нужно использовать builtin:billing.infrastructure\_monitoring.metric\_data\_points.included\_used . Если разница между этой метрикой и доступными метриками больше нуля, значит на хостах, мониторируемых в режиме Infrastructure, можно принимать больше метрик без дополнительных расходов. | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.metric\_data\_points.ingested | (DPS) Суммарные точки метрик, переданные хостами, мониторируемыми в режиме Infrastructure  Количество точек метрик, агрегированных по всем хостам, мониторируемым в режиме Infrastructure. Значения, передаваемые в этой метрике, подпадают под вычет включённых точек метрик. Эту суммарную метрику нужно использовать для запросов за длительные периоды без потери точности и производительности. Эта запаздывающая метрика передаётся с интервалом 15 минут с задержкой до 15 минут. Для просмотра использования в разбивке по хостам нужно использовать builtin:billing.full\_stack\_monitoring.metric\_data\_points.ingested\_by\_host . | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.metric\_data\_points.ingested\_by\_host | (DPS) Точки метрик, переданные хостами, мониторируемыми в режиме Infrastructure, в разбивке по хостам  Количество точек метрик в разбивке по хостам, мониторируемым в режиме Infrastructure. Значения, передаваемые в этой метрике, подпадают под вычет включённых точек метрик. Эта запаздывающая метрика передаётся с интервалом 15 минут с задержкой до 15 минут. Пул доступных включённых метрик для «15-минутного интервала» доступен через builtin:billing.infrastructure\_monitoring.metric\_data\_points.included . Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными периодами нужно использовать суммарную метрику. Подробнее: [further details﻿](https://dt-url.net/et231ii). | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.usage | (DPS) Потребление Infrastructure Monitoring для выставления счётов  Общее количество хост-часов, мониторируемых в режиме только инфраструктуры, с подсчётом за 15-минутные интервалы. Эту суммарную метрику нужно использовать для запросов за длительные периоды без потери точности и производительности. Для получения сведений о хостах, формирующих потребление, нужно обратиться к метрике usage\_per\_host. | Count | autovalue |
| builtin:billing.infrastructure\_monitoring.usage\_per\_host | (DPS) Потребление Infrastructure Monitoring для выставления счётов в разбивке по хостам  Хост-часы, мониторируемые в режиме только инфраструктуры, с подсчётом за 15-минутные интервалы. Хост, мониторируемый в течение всего часа, даёт 4 точки данных со значением 0.25 вне зависимости от объёма памяти. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными периодами нужно использовать суммарную метрику. Подробнее: [further details﻿](https://dt-url.net/et231ii). | Count | autovalue |

### Kubernetes monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.kubernetes\_monitoring.usage | (DPS) Потребление Kubernetes Platform Monitoring для выставления счётов  Общее количество мониторируемых Kubernetes подов в час, в разбивке по кластерам и пространствам имён, с подсчётом за 15-минутные интервалы. Под, мониторируемый в течение всего часа, даёт 4 точки данных со значением 0.25. | Count | autovalue |

### Log

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.log.ingest.usage | (DPS) Потребление Log Management and Analytics, Ingest & Process  Потребление Log Management and Analytics по функции Ingest & Process, отслеживается как количество байт, принятых за час. Эта запаздывающая метрика передаётся ежечасно за предыдущий час. Значения метрик передаются с задержкой до одного часа. | Byte | autovalue |
| builtin:billing.log.query.usage | (DPS) Потребление Log Management and Analytics, Query  Потребление Log Management and Analytics по функции Query, отслеживается как количество байт, прочитанных за час. Эта запаздывающая метрика передаётся ежечасно за предыдущий час. Значения метрик передаются с задержкой до одного часа. | Byte | autovalue |
| builtin:billing.log.retain.usage | (DPS) Потребление Log Management and Analytics, Retain  Потребление Log Management and Analytics по функции Retain, отслеживается как суммарный объём хранилища, используемый за час, в байтах. Эта запаздывающая метрика передаётся ежечасно за предыдущий час. Значения метрик передаются с задержкой до одного часа. | Byte | autoavgmaxmin |

### Log monitoring classic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.log\_monitoring\_classic.usage | (DPS) Суммарное потребление Log Monitoring Classic для выставления счётов  Количество записей журнала, принятых и агрегированных по всем мониторируемым сущностям. Запись журнала распознаётся по наличию временной метки или объекта JSON. Эту суммарную метрику нужно использовать для запросов за длительные периоды без потери точности и производительности. | Count | autovalue |
| builtin:billing.log\_monitoring\_classic.usage\_by\_entity | (DPS) Потребление Log Monitoring Classic для выставления счётов в разбивке по мониторируемым сущностям  Количество записей журнала, принятых в разбивке по мониторируемым сущностям. Запись журнала распознаётся по наличию временной метки или объекта JSON. Для получения сведений о пути к журналу нужно обратиться к метрике usage\_by\_log\_path. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными периодами нужно использовать суммарную метрику. | Count | autovalue |
| builtin:billing.log\_monitoring\_classic.usage\_by\_log\_path | (DPS) Потребление Log Monitoring Classic для выставления счётов в разбивке по пути к журналу  Количество записей журнала, принятых в разбивке по пути к журналу. Запись журнала распознаётся по наличию временной метки или объекта JSON. Для получения сведений о связанных мониторируемых сущностях нужно обратиться к метрике usage\_by\_entity. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными периодами нужно использовать суммарную метрику. | Count | autovalue |

### Mainframe monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.mainframe\_monitoring.usage | (DPS) Потребление Mainframe Monitoring для выставления счётов  Общее количество MSU-часов, находящихся под мониторингом, с подсчётом за 15-минутные интервалы. | MSU | autovalue |

### Real user monitoring

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.real\_user\_monitoring.mobile.property.usage | (DPS) Total Real-User Monitoring Property (mobile) billing usage  (Mobile) Количество свойств пользовательских действий и сессий. Подробнее о расчёте потребления, см. документацию или builtin:billing.real\_user\_monitoring.web.property.usage\_by\_application . Используйте эту суммарную метрику для запросов на длительных временных промежутках без потери точности или производительности. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.property.usage\_by\_application | (DPS) Real-User Monitoring Property (mobile) billing usage by application  (Mobile) Количество свойств пользовательских действий и сессий по приложению. Тарифицируемое значение рассчитывается на основе количества сессий, указанных в builtin:billing.real\_user\_monitoring.mobile.session.usage\_by\_app + builtin:billing.real\_user\_monitoring.mobile.session\_with\_replay.usage\_by\_app , плюс количество настроенных свойств, превышающих включённое количество свойств (бесплатных), предоставляемых для данного приложения. Точки данных записываются только для тарифицируемых сессий. Если значение равно 0, у вас есть доступные точки данных метрики. Эта запаздывающая метрика отчитывается ежечасно за предыдущий час. Значения метрик публикуются с задержкой до одного часа. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными промежутками используйте суммарную метрику. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.session.usage | (DPS) Total Real-User Monitoring (mobile) billing usage  (Mobile) Количество сессий без Session Replay. Тарифицируемое значение за каждую сессию, это длительность сессии в часах. Например, сессия длиной 3 часа даёт одно значение точки данных равное `3`. Если две сессии заканчиваются в одну и ту же минуту, значения суммируются. Используйте эту суммарную метрику для запросов на длительных временных промежутках без потери точности или производительности. Чтобы просмотреть приложения, потребляющие это использование, обратитесь к метрике usage\_by\_app. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.session.usage\_by\_app | (DPS) Real-User Monitoring (mobile) billing usage by application  (Mobile) Количество сессий без Session Replay с разбивкой по приложению. Тарифицируемое значение за каждую сессию, это длительность сессии в часах. Например, сессия длиной 3 часа даёт одно значение точки данных равное `3`. Если две сессии одного приложения заканчиваются в одну и ту же минуту, значения суммируются. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными промежутками используйте суммарную метрику. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.session\_with\_replay.usage | (DPS) Total Real-User Monitoring (mobile) with Session Replay billing usage  (Mobile) Количество сессий с Session Replay. Тарифицируемое значение за каждую сессию, это длительность сессии в часах. Например, сессия длиной 3 часа даёт одно значение точки данных равное `3`. Если две сессии заканчиваются в одну и ту же минуту, значения суммируются. Используйте эту суммарную метрику для запросов на длительных временных промежутках без потери точности или производительности. Чтобы просмотреть приложения, потребляющие это использование, обратитесь к метрике usage\_by\_app. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.mobile.session\_with\_replay.usage\_by\_app | (DPS) Real-User Monitoring (mobile) with Session Replay billing usage by application  (Mobile) Количество сессий с Session Replay с разбивкой по приложению. Тарифицируемое значение за каждую сессию, это длительность сессии в часах. Например, сессия длиной 3 часа даёт одно значение точки данных равное `3`. Если две сессии одного приложения заканчиваются в одну и ту же минуту, значения суммируются. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными промежутками используйте суммарную метрику. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.property.usage | (DPS) Total Real-User Monitoring Property (web) billing usage  (Web) Количество свойств пользовательских действий и сессий. Подробнее о расчёте потребления, см. документацию или builtin:billing.real\_user\_monitoring.web.property.usage\_by\_application . Используйте эту суммарную метрику для запросов на длительных временных промежутках без потери точности или производительности. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.property.usage\_by\_application | (DPS) Real-User Monitoring Property (web) billing usage by application  (Web) Количество свойств пользовательских действий и сессий по приложению. Тарифицируемое значение рассчитывается на основе количества сессий, указанных в builtin:billing.real\_user\_monitoring.web.session.usage\_by\_app + builtin:billing.real\_user\_monitoring.web.session\_with\_replay.usage\_by\_app , плюс количество настроенных свойств, превышающих включённое количество свойств (бесплатных), предоставляемых для данного приложения. Точки данных записываются только для тарифицируемых сессий. Если значение равно 0, у вас есть доступные точки данных метрики. Эта запаздывающая метрика отчитывается ежечасно за предыдущий час. Значения метрик публикуются с задержкой до одного часа. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными промежутками используйте суммарную метрику. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.session.usage | (DPS) Total Real-User Monitoring (web) billing usage  (Web) Количество сессий без Session Replay. Тарифицируемое значение за каждую сессию, это длительность сессии в часах. Например, сессия длиной 3 часа даёт одно значение точки данных равное `3`. Если две сессии заканчиваются в одну и ту же минуту, значения суммируются. Используйте эту суммарную метрику для запросов на длительных временных промежутках без потери точности или производительности. Чтобы просмотреть приложения, потребляющие это использование, обратитесь к метрике usage\_by\_app. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.session.usage\_by\_app | (DPS) Real-User Monitoring (web) billing usage by application  (Web) Количество сессий без Session Replay с разбивкой по приложению. Тарифицируемое значение за каждую сессию, это длительность сессии в часах. Например, сессия длиной 3 часа даёт одно значение точки данных равное `3`. Если две сессии одного приложения заканчиваются в одну и ту же минуту, значения суммируются. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными промежутками используйте суммарную метрику. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.session\_with\_replay.usage | (DPS) Total Real-User Monitoring (web) with Session Replay billing usage  (Web) Количество сессий с Session Replay. Тарифицируемое значение за каждую сессию, это длительность сессии в часах. Например, сессия длиной 3 часа даёт одно значение точки данных равное `3`. Если две сессии заканчиваются в одну и ту же минуту, значения суммируются. Используйте эту суммарную метрику для запросов на длительных временных промежутках без потери точности или производительности. Чтобы просмотреть приложения, потребляющие это использование, обратитесь к метрике usage\_by\_app. | Count | autovalue |
| builtin:billing.real\_user\_monitoring.web.session\_with\_replay.usage\_by\_app | (DPS) Real-User Monitoring (web) with Session Replay billing usage by application  (Web) Количество сессий с Session Replay с разбивкой по приложению. Тарифицируемое значение за каждую сессию, это длительность сессии в часах. Например, сессия длиной 3 часа даёт одно значение точки данных равное `3`. Если две сессии одного приложения заканчиваются в одну и ту же минуту, значения суммируются. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными промежутками используйте суммарную метрику. | Count | autovalue |

### Runtime application protection

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.runtime\_application\_protection.usage | (DPS) Runtime Application Protection billing usage  Суммарный объём памяти в GiB хостов, защищённых с помощью Runtime Application Protection (Application Security), измеряемый с интервалом 15 минут. Используйте эту суммарную метрику для запросов на длительных временных промежутках без потери точности или производительности. Подробнее о мониторируемых хостах, см. метрику usage\_per\_host. | GibiByte | autovalue |
| builtin:billing.runtime\_application\_protection.usage\_per\_host | (DPS) Runtime Application Protection billing usage per host  Объём памяти в GiB на хост, защищённый с помощью Runtime Application Protection (Application Security), измеряемый с интервалом 15 минут. Например, хост с 8 GiB оперативной памяти, мониторируемый в течение 1 часа, даёт 4 точки данных со значением `2`. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными промежутками используйте суммарную метрику. | GibiByte | autovalue |

### Runtime vulnerability analytics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.runtime\_vulnerability\_analytics.usage | (DPS) Runtime Vulnerability Analytics billing usage  Суммарный объём памяти в GiB хостов, защищённых с помощью Runtime Vulnerability Analytics (Application Security), измеряемый с интервалом 15 минут. Используйте эту суммарную метрику для запросов на длительных временных промежутках без потери точности или производительности. Подробнее о мониторируемых хостах, см. метрику usage\_per\_host. | GibiByte | autovalue |
| builtin:billing.runtime\_vulnerability\_analytics.usage\_per\_host | (DPS) Runtime Vulnerability Analytics billing usage per host  Объём памяти в GiB на хост, защищённый с помощью Runtime Vulnerability Analytics (Application Security), измеряемый с интервалом 15 минут. Например, хост с 8 GiB оперативной памяти, мониторируемый в течение 1 часа, даёт 4 точки данных со значением `2`. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длительными временными промежутками используйте суммарную метрику. | GibiByte | autovalue |

### Serverless functions classic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.serverless\_functions\_classic.usage | (DPS) Total Serverless Functions Classic billing usage  Количество вызовов бессерверной функции, агрегированное по всем отслеживаемым сущностям. Термин «вызовы функции» эквивалентен понятиям «запросы к функции» и «выполнения функции». Используйте эту суммарную метрику для запросов к длинным временным промежуткам без потери точности и производительности. | Count | autovalue |
| builtin:billing.serverless\_functions\_classic.usage\_by\_entity | (DPS) Serverless Functions Classic billing usage by monitored entity  Количество вызовов бессерверной функции с разбивкой по отслеживаемым сущностям. Термин «вызовы функции» эквивалентен понятиям «запросы к функции» и «выполнения функции». Подробности о том, какие именно функции вызываются, см. в метрике usage\_by\_function. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длинными временными промежутками используйте суммарную метрику. | Count | autovalue |
| builtin:billing.serverless\_functions\_classic.usage\_by\_function | (DPS) Serverless Functions Classic billing usage by function  Количество вызовов бессерверной функции с разбивкой по функциям. Термин «вызовы функции» эквивалентен понятиям «запросы к функции» и «выполнения функции». Подробности об отслеживаемых сущностях см. в метрике usage\_by\_entity. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длинными временными промежутками используйте суммарную метрику. | Count | autovalue |

### Synthetic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:billing.synthetic.actions | Actions  Количество тарифицируемых действий, потреблённых браузерными мониторами. | Count | autovalue |
| builtin:billing.synthetic.actions.usage | (DPS) Total Browser Monitor or Clickpath billing usage  Количество синтетических действий, инициирующих веб-запрос, включающий загрузку страницы, событие навигации или действие, запускающее XHR- или Fetch-запрос. Прокрутка, нажатия клавиш или клики, не инициирующие веб-запросы, не учитываются как такие действия. Используйте эту суммарную метрику для запросов к длинным временным промежуткам без потери точности и производительности. | Count | autovalue |
| builtin:billing.synthetic.actions.usage\_by\_browser\_monitor | (DPS) Browser Monitor or Clickpath billing usage per synthetic browser monitor  Количество синтетических действий, инициирующих веб-запрос, включающий загрузку страницы, событие навигации или действие, запускающее XHR- или Fetch-запрос. Прокрутка, нажатия клавиш или клики, не инициирующие веб-запросы, не учитываются как такие действия. Действия разбиты по синтетическим браузерным мониторам, которые их вызвали. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длинными временными промежутками используйте суммарную метрику. | Count | autovalue |
| builtin:billing.synthetic.external | Third-party results  Количество тарифицируемых результатов, потреблённых мониторами сторонних поставщиков. | Count | autovalue |
| builtin:billing.synthetic.external.usage | (DPS) Total Third-Party Synthetic API Ingestion billing usage  Количество результатов синтетического тестирования, переданных в Dynatrace посредством Synthetic 3rd party API. Используйте эту суммарную метрику для запросов к длинным временным промежуткам без потери точности и производительности. | Count | autovalue |
| builtin:billing.synthetic.external.usage\_by\_third\_party\_monitor | (DPS) Third-Party Synthetic API Ingestion billing usage per external browser monitor  Количество результатов синтетического тестирования, переданных в Dynatrace посредством Synthetic 3rd party API. Поступающие данные разбиты по внешним синтетическим браузерным мониторам, для которых были загружены результаты. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длинными временными промежутками используйте суммарную метрику. | Count | autovalue |
| builtin:billing.synthetic.requests | Requests  Количество тарифицируемых запросов, потреблённых HTTP-мониторами. | Count | autovalue |
| builtin:billing.synthetic.requests.usage | (DPS) Total HTTP monitor billing usage  Количество HTTP-запросов, выполненных в ходе работы синтетического HTTP-монитора. Используйте эту суммарную метрику для запросов к длинным временным промежуткам без потери точности и производительности. | Count | autovalue |
| builtin:billing.synthetic.requests.usage\_by\_http\_monitor | (DPS) HTTP monitor billing usage per HTTP monitor  Количество выполненных HTTP-запросов с разбивкой по синтетическим HTTP-мониторам. Для повышения производительности и предотвращения превышения лимитов запросов при работе с длинными временными промежутками используйте суммарную метрику. | Count | autovalue |

## Cloud

### AWS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.aws.az.running | Количество запущенных EC2 instances (AZ) | Count | autoavgmaxmin |

### Azure

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.azure.region.vms.initializing | Количество запускаемых VM в регионе | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.running | Количество активных VM в регионе | Count | autoavgmaxmin |
| builtin:cloud.azure.region.vms.stopped | Количество остановленных VM в регионе | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.initializing | Количество запускаемых VM в scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.running | Количество активных VM в scale set | Count | autoavgmaxmin |
| builtin:cloud.azure.vmScaleSet.vms.stopped | Количество остановленных VM в scale set | Count | autoavgmaxmin |

### Cloud Foundry

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.cloudfoundry.auctioneer.fetchDuration | CF: Time to fetch cell states  Время, затраченное auctioneer на получение состояния от всех cell в ходе проведения аукциона. | Nanosecond | autoavgmaxmin |
| builtin:cloud.cloudfoundry.auctioneer.lprFailed | CF: App instance placement failures  Количество экземпляров приложений, которые auctioneer не смог разместить на Diego cells. | Count | autovalue |
| builtin:cloud.cloudfoundry.auctioneer.lprStarted | CF: App instance starts  Количество экземпляров приложений, успешно размещённых auctioneer на Diego cells. | Count | autovalue |
| builtin:cloud.cloudfoundry.auctioneer.taskFailed | CF: Task placement failures  Количество задач, которые auctioneer не смог разместить на Diego cells. | Count | autovalue |
| builtin:cloud.cloudfoundry.http.badGateways | CF: 502 responses  Количество ответов, свидетельствующих о недопустимых ответах сервиса от приложения. | Count | autovalue |
| builtin:cloud.cloudfoundry.http.latency | CF: Response latency  Среднее время отклика от приложения до клиентов. | Millisecond | autoavgmaxmin |
| builtin:cloud.cloudfoundry.http.responses5xx | CF: 5xx responses  Количество ответов, свидетельствующих о повторяющихся сбоях приложений или проблемах с ответами от приложений. | Count | autovalue |
| builtin:cloud.cloudfoundry.http.totalRequests | CF: Total requests  Общее количество запросов, отражающее суммарный трафик. | Count | autovalue |

### Openstack

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.openstack.vm.cpu.usage | Использование CPU | Percent (%) | autoavgmaxmin |
| builtin:cloud.openstack.vm.disk.allocation | Выделение дискового пространства | Byte | autoavgmaxmin |
| builtin:cloud.openstack.vm.disk.capacity | Ёмкость диска | Byte | autoavgmaxmin |
| builtin:cloud.openstack.vm.memory.resident | Резидентная память | Byte | autoavgmaxmin |
| builtin:cloud.openstack.vm.memory.usage | Использование памяти | Byte | autoavgmaxmin |
| builtin:cloud.openstack.vm.net.rx | Скорость входящих байт сети | Byte/second | autoavgmaxmin |
| builtin:cloud.openstack.vm.net.tx | Скорость исходящих байт сети | Byte/second | autoavgmaxmin |

### VMware

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:cloud.vmware.hypervisor.cpu.usage | Использование CPU хоста, % | Percent (%) | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.disk.usage | Скорость использования диска хоста | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.commandsAborted | Прерванные команды диска хоста | Count | autovalue |
| builtin:cloud.vmware.hypervisor.hostdisk.queueLatency | Задержка очереди диска хоста | Millisecond | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.rIops | IOPS чтения диска хоста | Per second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.readLatency | Задержка чтения диска хоста | Millisecond | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.readRate | Скорость чтения диска хоста | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.wIops | IOPS записи диска хоста | Per second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.writeLatency | Задержка записи диска хоста | Millisecond | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.hostdisk.writeRate | Скорость записи диска хоста | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.compressionRate | Скорость сжатия памяти хоста | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.consumed | Потреблённая память хоста | Kibibyte | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.decompressionRate | Скорость распаковки памяти хоста | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.swapIn | Скорость swap in хоста | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.mem.swapOut | Скорость swap out хоста | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.net.rx | Скорость приёма данных по сети хоста | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.net.tx | Скорость передачи данных по сети хоста | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.nic.dataRx | Скорость приёма данных | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.nic.dataTx | Скорость передачи данных | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.nic.packetsRxDropped | Отброшенные входящие пакеты | Count | autovalue |
| builtin:cloud.vmware.hypervisor.nic.packetsTxDropped | Отброшенные исходящие пакеты | Count | autovalue |
| builtin:cloud.vmware.hypervisor.vms.count | Количество ВМ | Count | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.vms.powerOff | Количество выключенных ВМ | Count | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.vms.suspended | Количество приостановленных ВМ | Count | autoavgmaxmin |
| builtin:cloud.vmware.hypervisor.availability | Доступность хоста, % | Percent (%) | autoavg |
| builtin:cloud.vmware.vm.cpu.readyPerc | CPU ready ВМ, % | Percent (%) | autoavgmaxmin |
| builtin:cloud.vmware.vm.cpu.swapWait | Ожидание swap ВМ | Millisecond | autovalue |
| builtin:cloud.vmware.vm.cpu.usage | Использование CPU ВМ, МГц | Count | autoavgmaxmin |
| builtin:cloud.vmware.vm.cpu.usagePerc | Использование CPU ВМ, % | Percent (%) | autoavgmaxmin |
| builtin:cloud.vmware.vm.disk.usage | Скорость использования диска ВМ | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.active | Активная память ВМ | Kibibyte | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.compressionRate | Скорость сжатия памяти ВМ | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.consumed | Потреблённая память ВМ | Kibibyte | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.decompressionRate | Скорость распаковки памяти ВМ | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.swapIn | Скорость swap in ВМ | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.vm.mem.swapOut | Скорость swap out ВМ | Kibibyte/second | autoavgmaxmin |
| builtin:cloud.vmware.vm.net.rx | Скорость приёма данных по сети ВМ | kB/s | autoavgmaxmin |
| builtin:cloud.vmware.vm.net.tx | Скорость передачи данных по сети ВМ | kB/s | autoavgmaxmin |

## Containers

### CPU

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:containers.cpu.limit | Containers: лимит CPU, mCores  Лимит ресурса CPU на контейнер в миллиядрах. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.logicalCores | Containers: логические ядра CPU  Количество логических ядер CPU хоста. | Cores | autoavgmaxmin |
| builtin:containers.cpu.shares | Containers: доли CPU  Количество долей CPU, выделенных на контейнер. | Count | autoavgmaxmin |
| builtin:containers.cpu.throttledMilliCores | Containers: троттлинг CPU, mCores  Троттлинг CPU на контейнер в миллиядрах. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.throttledTime | Containers: время троттлинга CPU, нс/мин  Суммарное время действия троттлинга для контейнера в наносекундах в минуту. | Nanosecond/minute | autoavgmaxmin |
| builtin:containers.cpu.usageMilliCores | Containers: использование CPU, mCores  Использование CPU на контейнер в миллиядрах. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.usagePercent | Containers: использование CPU, % от лимита  Процент использования CPU на контейнер относительно лимита ресурса CPU. Если лимит CPU не задан, используются логические ядра. | Percent (%) | autoavgmaxmin |
| builtin:containers.cpu.usageSystemMilliCores | Containers: системное использование CPU, mCores  Системное использование CPU на контейнер в миллиядрах. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.usageSystemTime | Containers: системное время использования CPU, нс/мин  Использованное системное время на контейнер в наносекундах в минуту. | Nanosecond/minute | autoavgmaxmin |
| builtin:containers.cpu.usageTime | Containers: время использования CPU, нс/мин  Суммарное использованное системное и пользовательское время на контейнер в наносекундах в минуту. | Nanosecond/minute | autoavgmaxmin |
| builtin:containers.cpu.usageUserMilliCores | Containers: пользовательское использование CPU, mCores  Пользовательское использование CPU на контейнер в миллиядрах. | Millicores | autoavgmaxmin |
| builtin:containers.cpu.usageUserTime | Containers: пользовательское время использования CPU, нс/мин  Использованное пользовательское время на контейнер в наносекундах в минуту. | Nanosecond/minute | autoavgmaxmin |

### Memory

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:containers.memory.cacheBytes | Containers: кэш памяти, байты  Память кэша страниц на контейнер в байтах. | Byte | autoavgmaxmin |
| builtin:containers.memory.limitBytes | Containers: лимит памяти, байты  Лимит памяти на контейнер в байтах. Если лимит не задан, значение отсутствует. | Byte | autoavgmaxmin |
| builtin:containers.memory.limitPercent | Containers: лимит памяти, % от физической памяти  Процентный лимит памяти на контейнер относительно суммарной физической памяти. Если лимит не задан, значение отсутствует. | Percent (%) | autoavg |
| builtin:containers.memory.outOfMemoryKills | Containers: завершения по нехватке памяти  Количество завершений контейнера по нехватке памяти. | Count | autovalue |
| builtin:containers.memory.physicalTotalBytes | Containers: суммарная физическая память, байты  Суммарная физическая память хоста в байтах. | Byte | autoavgmaxmin |
| builtin:containers.memory.residentSetBytes | Containers: использование памяти, байты  Resident set size (Linux) или private working set size (Windows) на контейнер в байтах. | Byte | autoavgmaxmin |
| builtin:containers.memory.usagePercent | Containers: использование памяти, % от лимита  Resident set size (Linux) или private working set size (Windows) на контейнер в процентах относительно лимита памяти контейнера. Если лимит не задан, берётся суммарная физическая память. | Percent (%) | autoavgmaxmin |

## Dashboards

### Other dashboards metrics

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:dashboards.viewCount | Количество просмотров дашборда | Count | autovalue |

## Infrastructure

### Availability

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.availability.state | Доступность хоста  Метрика состояния доступности хоста, сообщается с интервалом 1 минута. | Count | autovalue |

### CPU

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.cpu.gcpu.usage | z/OS General CPU usage  Процент использования центрального процессора общего назначения (GCP) | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.msu.avg | z/OS Rolling 4 hour MSU average  4-часовое скользящее среднее потреблённых million service units на данном LPAR | MSU | autoavgmaxmin |
| builtin:host.cpu.msu.capacity | z/OS MSU capacity  Общая ёмкость million service units на данном LPAR | MSU | autoavgmaxmin |
| builtin:host.cpu.ziip.eligible | z/OS zIIP eligible time  Время, пригодное для zIIP, затраченное на центральном процессоре общего назначения (GCP) с момента запуска процесса в минуту | Секунда | autoavgcountmaxminsum |
| builtin:host.cpu.entConfig | AIX Entitlement configured  Capacity Entitlement, это количество виртуальных процессоров, назначенных разделу AIX. Измеряется в долях процессора, равных 0.1 или 0.01. Подробнее об Entitlement: см. [Assigning the appropriate processor entitled capacity﻿](https://dt-url.net/3n234vz) в официальной документации IBM. | Отношение | autoavgmaxmin |
| builtin:host.cpu.entc | AIX Entitlement used  Процент использованного Entitlement. Capacity Entitlement, это количество виртуальных ядер, назначенных разделу AIX. Смотрите подробнее об Entitlement, см. [Assigning the appropriate processor entitled capacity﻿](https://dt-url.net/3n234vz) в официальной документации IBM. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.idle | CPU idle  Среднее время CPU, когда процессор не имел задач для выполнения | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.iowait | CPU I/O wait  Процент времени, когда CPU простаивал при наличии незавершённого запроса ввода-вывода. Недоступно на Windows. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.load | System load  Среднее количество процессов, выполняемых CPU или ожидающих выполнения, за последнюю минуту | Отношение | autoavgmaxmin |
| builtin:host.cpu.load15m | System load15m  Среднее количество процессов, выполняемых CPU или ожидающих выполнения, за последние 15 минут | Отношение | autoavgmaxmin |
| builtin:host.cpu.load5m | System load5m  Среднее количество процессов, выполняемых CPU или ожидающих выполнения, за последние 5 минут | Отношение | autoavgmaxmin |
| builtin:host.cpu.other | CPU other  Среднее время CPU, затраченное на прочие задачи: обслуживание запросов прерываний (IRQ), запуск виртуальных машин под управлением ядра хоста (когда хост выступает гипервизором для ВМ). Доступно только для хостов Linux | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.physc | AIX Physical consumed  Суммарное количество CPU, потреблённых разделом AIX | Отношение | autoavgmaxmin |
| builtin:host.cpu.steal | CPU steal  Среднее время CPU, когда виртуальная машина ожидает получения тактов процессора от гипервизора. В виртуальной среде такты процессора распределяются между виртуальными машинами на сервере-гипервизоре. Если на виртуализированном хосте наблюдается высокое значение CPU steal, это означает, что такты процессора забираются у виртуальной машины для других целей. Это может указывать на перегруженность гипервизора. Доступно только для хостов Linux | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.system | CPU system  Среднее время CPU, когда процессор работал в режиме ядра | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.usage | CPU usage %  Процент времени CPU, когда процессор был задействован. Значение, близкое к 100%, означает, что большинство вычислительных ресурсов хоста используется и CPU не может принять дополнительную нагрузку | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.user | CPU user  Среднее время CPU, когда процессор работал в пользовательском режиме | Процент (%) | autoavgmaxmin |

### DNS

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.dns.errorCount | Number of DNS errors by type  Количество ошибок DNS по типу | Количество | autoavgcountmaxminsum |
| builtin:host.dns.orphanCount | Number of orphaned DNS responses  Количество потерянных DNS-ответов на хосте | Количество | autoavgcountmaxminsum |
| builtin:host.dns.queryCount | Number of DNS queries  Количество DNS-запросов на хосте | Количество | autoavgcountmaxminsum |
| builtin:host.dns.queryTime | DNS query time sum  Суммарное время всех DNS-запросов на хосте | Миллисекунда | autoavgcountmaxminsum |
| builtin:host.dns.singleQueryTime | DNS query time  Среднее время DNS-запроса. Вычисляется как суммарное время DNS-запросов, делённое на количество DNS-запросов для каждой пары хост и DNS-сервер. | Миллисекунда | autoavgmaxmin |
| builtin:host.dns.singleQueryTimeByDnsIp | DNS query time by DNS server  Взвешенное среднее время DNS-запроса по IP-адресу DNS-сервера. Вычисляется как суммарное время DNS-запросов, делённое на количество DNS-запросов. При взвешивании учитывается количество запросов от каждого хоста. | Миллисекунда | autoavgmaxmin |
| builtin:host.dns.singleQueryTimeByHost | DNS query time on host  Взвешенное среднее время DNS-запроса на хосте. Вычисляется как суммарное время DNS-запросов, делённое на количество DNS-запросов на хосте. При взвешивании учитывается количество запросов к каждому DNS-серверу | Миллисекунда | autoavgmaxmin |

### Диск

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.disk.throughput.read | Disk throughput read  Пропускная способность файловой системы при чтении в битах в секунду | бит/с | autoavgmaxmin |
| builtin:host.disk.throughput.write | Disk throughput write  Пропускная способность файловой системы при записи в битах в секунду | бит/с | autoavgmaxmin |
| builtin:host.disk.avail | Disk available  Объём свободного пространства, доступного пользователю в файловой системе. На Linux и AIX, это свободное пространство для непривилегированного пользователя, без учёта части, зарезервированной для root. | Байт | autoavgmaxmin |
| builtin:host.disk.bytesRead | Disk read bytes per second  Скорость чтения из файловой системы в байтах в секунду | Байт/с | autoavgmaxmin |
| builtin:host.disk.bytesWritten | Disk write bytes per second  Скорость записи в файловую систему в байтах в секунду | Байт/с | autoavgmaxmin |
| builtin:host.disk.free | Disk available %  Процент свободного пространства, доступного пользователю в файловой системе. На Linux и AIX, это процент свободного пространства для непривилегированного пользователя, без учёта части, зарезервированной для root. | Процент (%) | autoavgmaxmin |
| builtin:host.disk.inodesAvail | Inodes available %  Процент свободных inode, доступных непривилегированному пользователю в файловой системе. Метрика недоступна на Windows. | Процент (%) | autoavgmaxmin |
| builtin:host.disk.inodesTotal | Inodes total  Общее количество inode, доступных непривилегированному пользователю в файловой системе. Метрика недоступна на Windows. | Количество | autoavgmaxmin |
| builtin:host.disk.queueLength | Disk average queue length  Среднее количество операций чтения и записи в очереди диска | Количество | autoavgmaxmin |
| builtin:host.disk.readOps | Disk read operations per second  Количество операций чтения из файловой системы в секунду | В секунду | autoavgmaxmin |
| builtin:host.disk.readTime | Disk read time  Среднее время чтения из файловой системы. Показывает среднюю задержку диска при чтении. | Миллисекунда | autoavgcountmaxminsum |
| builtin:host.disk.used | Disk used  Объём используемого пространства в файловой системе | Байт | autoavgmaxmin |
| builtin:host.disk.usedPct | Disk used %  Процент используемого пространства в файловой системе | Процент (%) | autoavgmaxmin |
| builtin:host.disk.utilTime | Disk utilization time  Процент времени, затраченного на операции ввода-вывода диска | Процент (%) | autoavgmaxmin |
| builtin:host.disk.writeOps | Disk write operations per second  Количество операций записи в файловую систему в секунду | В секунду | autoavgmaxmin |
| builtin:host.disk.writeTime | Disk write time  Среднее время записи в файловую систему. Показывает среднюю задержку диска при записи. | Миллисекунда | autoavgcountmaxminsum |

### Дескрипторы

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.handles.fileDescriptorsMax | File descriptors max  Максимальное количество файловых дескрипторов, доступных для использования | Количество | autoavgmaxmin |
| builtin:host.handles.fileDescriptorsUsed | File descriptors used  Количество используемых файловых дескрипторов | Количество | autoavgmaxmin |

### Потоки ядра

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.kernelThreads.blocked | AIX Kernel threads blocked  Длина очереди подкачки. Очередь подкачки содержит потоки, готовые к выполнению, но вытесненные из памяти вместе с текущими выполняющимися потоками | Количество | autoavgmaxmin |
| builtin:host.kernelThreads.ioEventWait | AIX Kernel threads I/O event wait  Количество потоков, ожидающих прямого (cio) ввода-вывода файловой системы, плюс количество процессов, заблокированных в ожидании буферизованного ввода-вывода | Количество | autoavgcountmaxminsum |
| builtin:host.kernelThreads.ioMessageWait | AIX Kernel threads I/O message wait  Количество потоков, находящихся в состоянии ожидания операций прямого (raw) ввода-вывода в данный момент. Операции прямого ввода-вывода позволяют приложениям напрямую записывать данные на уровень Logical Volume Manager (LVM) | Количество | autoavgcountmaxminsum |
| builtin:host.kernelThreads.running | AIX Kernel threads runnable  Количество потоков, готовых к выполнению (запущенных или ожидающих процессорного времени). Среднее количество таких потоков отображается в первом столбце вывода команды vmstat | Количество | autoavgmaxmin |

### Memory

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.mem.avail.bytes | Memory available  Объём памяти (RAM), доступной на хосте. Память, доступная для выделения новым или существующим процессам. Доступная память, это оценка того, сколько памяти можно использовать без обращения к свопу. | Byte | autoavgmaxmin |
| builtin:host.mem.avail.pct | Memory available %  Процент памяти (RAM), доступной на хосте. Память, доступная для выделения новым или существующим процессам. Доступная память, это оценка того, сколько памяти можно использовать без обращения к свопу. Показывает доступную память в процентах. | Percent (%) | autoavgmaxmin |
| builtin:host.mem.avail.pfps | Page faults per second  Количество ошибок страниц в секунду на отслеживаемом хосте. Значение включает мягкие и жёсткие ошибки страниц. | Per second | autoavgmaxmin |
| builtin:host.mem.swap.avail | Swap available  Объём доступной памяти подкачки или пространства подкачки (иначе называемого пейджингом, то есть дисковым компонентом системы виртуальной памяти). | Byte | autoavgmaxmin |
| builtin:host.mem.swap.total | Swap total  Общий объём памяти подкачки или пространства подкачки (иначе называемого пейджингом, то есть дисковым компонентом системы виртуальной памяти), доступного для использования. | Byte | autovalue |
| builtin:host.mem.swap.used | Swap used  Объём используемой памяти подкачки или пространства подкачки (иначе называемого пейджингом, то есть дисковым компонентом системы виртуальной памяти). | Byte | autoavgmaxmin |
| builtin:host.mem.kernel | Kernel memory  Память, используемая системным ядром. Включает память, занятую основными компонентами ОС и драйверами устройств. Как правило, значение очень мало. | Byte | autoavgmaxmin |
| builtin:host.mem.recl | Memory reclaimable  Использование памяти для конкретных целей. Возвращаемая память вычисляется как доступная память (оценка того, сколько памяти можно использовать без обращения к свопу) минус свободная память (объём памяти, который в данный момент не используется ни для чего). Подробнее о возвращаемой памяти см. в [этой публикации блога﻿](https://www.dynatrace.com/news/blog/improved-host-memory-metrics-now-include-reclaimable-memory/). | Byte | autoavgmaxmin |
| builtin:host.mem.total | Memory total  Объём памяти (RAM), установленной в системе. | Byte | autovalue |
| builtin:host.mem.usage | Memory used %  Показывает процент памяти, используемой в данный момент. Используемая память вычисляется в OneAgent следующим образом: used = total - available. Поэтому метрика используемой памяти, отображаемая в представлениях анализа Dynatrace, не равна метрике используемой памяти, которую показывают системные инструменты. При этом важно помнить, что системные инструменты сообщают об используемой памяти именно так по историческим причинам, и этот конкретный способ вычисления используемой памяти не отражает в полной мере то, как ядро Linux управляет памятью в современных системах. Разница в этих измерениях весьма существенна. Примечание: вычисляется как 100% - «Memory available %». | Percent (%) | autoavgmaxmin |
| builtin:host.mem.used | Memory used  Используемая память вычисляется в OneAgent следующим образом: used = total - available. Поэтому метрика используемой памяти, отображаемая в представлениях анализа Dynatrace, не равна метрике используемой памяти, которую показывают системные инструменты. При этом важно помнить, что системные инструменты сообщают об используемой памяти именно так по историческим причинам, и этот конкретный способ вычисления используемой памяти не отражает в полной мере то, как ядро Linux управляет памятью в современных системах. Разница в этих измерениях весьма существенна. | Byte | autoavgmaxmin |

### Network

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.net.nic.packets.dropped | NIC packets dropped  Пакеты, отброшенные сетевым интерфейсом на хосте | Per second | autovalue |
| builtin:host.net.nic.packets.droppedRx | NIC received packets dropped  Входящие пакеты, отброшенные сетевым интерфейсом на хосте | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.droppedTx | NIC sent packets dropped  Исходящие пакеты, отброшенные сетевым интерфейсом на хосте | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.errors | NIC packet errors  Ошибки пакетов сетевого интерфейса на хосте | Per second | autovalue |
| builtin:host.net.nic.packets.errorsRx | NIC received packet errors  Ошибки входящих пакетов сетевого интерфейса на хосте | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.errorsTx | NIC sent packet errors  Ошибки исходящих пакетов сетевого интерфейса на хосте | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.rx | NIC packets received  Пакеты, полученные сетевым интерфейсом на хосте | Per second | autoavgmaxmin |
| builtin:host.net.nic.packets.tx | NIC packets sent  Пакеты, отправленные сетевым интерфейсом на хосте | Per second | autoavgmaxmin |
| builtin:host.net.nic.bytesRx | NIC bytes received  Байты, полученные сетевым интерфейсом на хосте | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.bytesTx | NIC bytes sent on host  Байты, отправленные сетевым интерфейсом на хосте | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.connectivity | NIC connectivity  Подключение сетевого интерфейса на хосте | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilRx | NIC receive link utilization  Утилизация входящего канала сетевого интерфейса на хосте | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilTx | NIC transmit link utilization  Утилизация исходящего канала сетевого интерфейса на хосте | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.retransmission | NIC retransmission  Повторные передачи сетевого интерфейса на хосте | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.retransmissionIn | NIC received packets retransmission  Повторные передачи сетевого интерфейса для входящих пакетов на хосте | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.retransmissionOut | NIC sent packets retransmission  Повторные передачи сетевого интерфейса для исходящих пакетов на хосте | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.traffic | Traffic  Сетевой трафик на хосте | bit/s | autovalue |
| builtin:host.net.nic.trafficIn | Traffic in  Входящий трафик на хосте | bit/s | autoavgmaxmin |
| builtin:host.net.nic.trafficOut | Traffic out  Исходящий трафик с хоста | bit/s | autoavgmaxmin |
| builtin:host.net.packets.rxBaseReceived | Host retransmission base received  Агрегированная базовая скорость получения данных для повторных передач процессов хоста в секунду | Per second | autoavgmaxmin |
| builtin:host.net.packets.rxBaseSent | Host retransmission base sent  Агрегированная базовая скорость отправки данных для повторных передач процессов хоста в секунду | Per second | autoavgmaxmin |
| builtin:host.net.packets.rxReceived | Host retransmitted packets received  Агрегированное количество повторно переданных пакетов, полученных процессами хоста в секунду | Per second | autoavgmaxmin |
| builtin:host.net.packets.rxSent | Host retransmitted packets sent  Агрегированное количество повторно переданных пакетов, отправленных процессами хоста в секунду | Per second | autoavgmaxmin |
| builtin:host.net.sessions.local.errRst | Localhost session reset received  Агрегированное количество сбросов сессий, получаемых процессами хоста в секунду на localhost | Per second | autoavgmaxmin |
| builtin:host.net.sessions.local.errTmout | Localhost session timeout received  Агрегированное количество таймаутов сессий, получаемых процессами хоста в секунду на localhost | Per second | autoavgmaxmin |
| builtin:host.net.sessions.local.new | Localhost new session received  Агрегированное количество новых сессий, получаемых процессами хоста в секунду на localhost | Per second | autoavgmaxmin |
| builtin:host.net.sessions.errRst | Host session reset received  Агрегированное количество сбросов сессий, получаемых процессами хоста в секунду | Per second | autoavgmaxmin |
| builtin:host.net.sessions.errTmout | Host session timeout received  Агрегированное количество таймаутов сессий, получаемых процессами хоста в секунду | Per second | autoavgmaxmin |
| builtin:host.net.sessions.new | Host new session received  Агрегированное количество новых сессий, получаемых процессами хоста в секунду | Per second | autoavgmaxmin |
| builtin:host.net.bytesRx | Host bytes received  Агрегированное количество байт, получаемых процессами хоста в секунду | Byte/second | autoavgmaxmin |
| builtin:host.net.bytesTx | Host bytes sent  Агрегированное количество байт, отправляемых процессами хоста в секунду | Byte/second | autoavgmaxmin |

### OS service

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.osService.availability | OS Service availability  Метрика предоставляет статус службы ОС. Если служба ОС запущена, модуль ОС сообщает значение «1». В любом другом случае метрика принимает значение «0». Обратите внимание, что эта метрика предоставляет данные только из мониторинга Classic Windows services (поддерживается только на Windows), который в настоящее время заменён новым мониторингом OS Services. Подробнее см. в разделе [Classic Windows services monitoring﻿](https://dt-url.net/classic-windows-services). | Count | autoavgmaxmin |

### Processes

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.osProcessStats.osProcessCount | Количество процессов ОС  Метрика показывает среднее количество процессов, работавших на хосте в течение одной минуты. Сообщаемое количество процессов основано на процессах, обнаруженных модулем ОС, который считывает данные циклами по 10 секунд. | Count | autoavgmaxmin |
| builtin:host.osProcessStats.pgiCount | Количество PGI  Метрика показывает количество PGI, созданных модулем ОС за каждую минуту. Включает все PGI, даже те, которые считаются неважными и не передаются в Dynatrace. | Count | autoavgmaxmin |
| builtin:host.osProcessStats.pgiReportedCount | Количество переданных PGI  Метрика показывает количество PGI, созданных и переданных модулем ОС за каждую минуту. Включает только PGI, которые считаются важными и передаются в Dynatrace. Важными считаются PGI, в которых OneAgent распознаёт технологию, открытые сетевые порты, значительное потребление ресурсов, либо PGI, созданные через правила декларативной группировки процессов. Подробнее о том, что делает процесс важным: [Which are the most important processes?﻿](https://dt-url.net/most-important-processes) | Count | autoavgmaxmin |

### RemotePluginAgent

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.remotePluginAgent.selfMonitoring.executionTime | Время выполнения | Millisecond | autovalue |

### z/OS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.zos.gcpu\_time | z/OS General CPU time  Суммарное время General CPU за минуту | Count | autoavgcountmaxminsum |
| builtin:host.zos.msu\_hours | z/OS Consumed MSUs per SMF interval (SMF70EDT)  Количество потреблённых MSU за интервал SMF (SMF70EDT) | Count | autoavgcountmaxminsum |
| builtin:host.zos.ziip\_time | z/OS zIIP time  Суммарное время zIIP за минуту | Count | autoavgcountmaxminsum |
| builtin:host.zos.ziip\_usage | z/OS zIIP usage  Активно используемые zIIP в процентах от доступных zIIP | Count | autoavgcountmaxminsum |

### Other infrastructure metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:host.availability | Коэффициент доступности  Операционная метрика доступности для хостов | Percent (%) | autoavg |
| builtin:host.uptime | Время работы хоста  Время с момента последней загрузки хоста. Требуется OneAgent 1.259+. Метрика не поддерживается для развёртываний OneAgent только с мониторингом приложений. | Second | autoavgmaxmin |

## Kubernetes

### Cluster

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.cluster.readyz | Kubernetes: Cluster readyz status  Текущий статус сервера API кластера Kubernetes, возвращаемый эндпоинтом /readyz (0 или 1). |  | autoavgmaxmin |

### Container

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.container.oom\_kills | Kubernetes: Container, количество OOM kill  Метрика измеряет количество завершений контейнеров по нехватке памяти (OOM kill). Наиболее детальный уровень агрегации, контейнер. Значение соответствует статусу `OOMKilled` контейнера в поле container status ресурса pod. Метрика записывается только при наличии хотя бы одного OOM kill. | Count | autovalue |
| builtin:kubernetes.container.restarts | Kubernetes: Container, количество перезапусков  Метрика измеряет количество перезапусков контейнера. Наиболее детальный уровень агрегации, контейнер. Значение соответствует дельте поля `restartCount` в container status ресурса pod. Метрика записывается только при наличии хотя бы одного перезапуска. | Count | autovalue |

### Node

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.node.conditions | Kubernetes: Node conditions  Метрика описывает статус узла Kubernetes. Наиболее детальный уровень агрегации, узел. | Count | autoavgmaxmin |
| builtin:kubernetes.node.cpu\_allocatable | Kubernetes: Node, выделяемые ресурсы CPU  Метрика измеряет суммарный выделяемый CPU. Наиболее детальный уровень агрегации, узел. Значение соответствует allocatable cpu узла. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.cpu\_throttled | Kubernetes: Container, троттлинг CPU (по узлу)  Метрика измеряет суммарный троттлинг CPU по контейнерам. Наиболее детальный уровень агрегации, узел. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.cpu\_usage | Kubernetes: Container, использование CPU (по узлу)  Метрика измеряет суммарный CPU, потреблённый контейнерами (пользовательское + системное использование). Наиболее детальный уровень агрегации, узел. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.limits\_cpu | Kubernetes: Pod, лимиты CPU (по узлу)  Метрика измеряет лимиты CPU. Наиболее детальный уровень агрегации, узел. Значение, сумма лимитов CPU всех контейнеров приложения в pod. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.limits\_memory | Kubernetes: Pod, лимиты памяти (по узлу)  Метрика измеряет лимиты памяти. Наиболее детальный уровень агрегации, узел. Значение, сумма лимитов памяти всех контейнеров приложения в pod. | Byte | autoavgmaxmin |
| builtin:kubernetes.node.memory\_allocatable | Kubernetes: Node, выделяемая память  Метрика измеряет суммарный объём выделяемой памяти. Наиболее детальный уровень агрегации, узел. Значение соответствует allocatable memory узла. | Byte | autoavgmaxmin |
| builtin:kubernetes.node.memory\_working\_set | Kubernetes: Container, рабочий набор памяти (по узлу)  Метрика измеряет текущую память рабочего набора (память, которую нельзя освободить под давлением) по контейнерам. OOM Killer срабатывает, если рабочий набор превышает лимит. Наиболее детальный уровень агрегации, узел. | Byte | autoavgmaxmin |
| builtin:kubernetes.node.pods | Kubernetes: Количество pod (по узлу)  Метрика измеряет количество pod. Наиболее детальный уровень агрегации, узел. Значение соответствует общему количеству pod. | Count | autoavgmaxmin |
| builtin:kubernetes.node.pods\_allocatable | Kubernetes: Node, выделяемое количество pod  Метрика измеряет суммарное количество выделяемых pod. Наиболее детальный уровень агрегации, узел. Значение соответствует allocatable pods узла. | Count | autoavgmaxmin |
| builtin:kubernetes.node.requests\_cpu | Kubernetes: Pod, запросы CPU (по узлу)  Метрика измеряет запросы CPU. Наиболее детальный уровень агрегации, узел. Значение, сумма запросов CPU всех контейнеров приложения в pod. | Millicores | autoavgmaxmin |
| builtin:kubernetes.node.requests\_memory | Kubernetes: Pod, запросы памяти (по узлу)  Метрика измеряет запросы памяти. Наиболее детальный уровень агрегации, узел. Значение, сумма запросов памяти всех контейнеров приложения в pod. | Byte | autoavgmaxmin |

### Persistentvolumeclaim

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.persistentvolumeclaim.available | Kubernetes: PVC, доступно  Метрика измеряет количество доступных байт в томе. Наиболее детальный уровень агрегации, persistent volume claim. | Byte | autoavgmaxmin |
| builtin:kubernetes.persistentvolumeclaim.capacity | Kubernetes: PVC, ёмкость  Метрика измеряет ёмкость тома в байтах. Наиболее детальный уровень агрегации, persistent volume claim. | Byte | autoavgmaxmin |
| builtin:kubernetes.persistentvolumeclaim.used | Kubernetes: PVC, использовано  Метрика измеряет количество использованных байт в томе. Наиболее детальный уровень агрегации, persistent volume claim. | Byte | autoavgmaxmin |

### Resource Quota

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.resourcequota.limits\_cpu | Kubernetes: Resource quota - лимиты CPU  Метрика измеряет квоту лимита CPU. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует лимитам CPU в рамках resource quota. | Millicores | autoavgmaxmin |
| builtin:kubernetes.resourcequota.limits\_cpu\_used | Kubernetes: Resource quota - использованные лимиты CPU  Метрика измеряет использованную квоту лимита CPU. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует использованным лимитам CPU в рамках resource quota. | Millicores | autoavgmaxmin |
| builtin:kubernetes.resourcequota.limits\_memory | Kubernetes: Resource quota - лимиты памяти  Метрика измеряет квоту лимита памяти. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует лимитам памяти в рамках resource quota. | Byte | autoavgmaxmin |
| builtin:kubernetes.resourcequota.limits\_memory\_used | Kubernetes: Resource quota - использованные лимиты памяти  Метрика измеряет использованную квоту лимита памяти. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует использованным лимитам памяти в рамках resource quota. | Byte | autoavgmaxmin |
| builtin:kubernetes.resourcequota.pods | Kubernetes: Resource quota - количество подов  Метрика измеряет квоту подов. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует подам в рамках resource quota. | Count | autoavgmaxmin |
| builtin:kubernetes.resourcequota.pods\_used | Kubernetes: Resource quota - использованное количество подов  Метрика измеряет использованную квоту подов. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует использованным подам в рамках resource quota. | Count | autoavgmaxmin |
| builtin:kubernetes.resourcequota.requests\_cpu | Kubernetes: Resource quota - CPU requests  Метрика измеряет квоту CPU requests. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует CPU requests в рамках resource quota. | Millicores | autoavgmaxmin |
| builtin:kubernetes.resourcequota.requests\_cpu\_used | Kubernetes: Resource quota - использованные CPU requests  Метрика измеряет использованную квоту CPU requests. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует использованным CPU requests в рамках resource quota. | Millicores | autoavgmaxmin |
| builtin:kubernetes.resourcequota.requests\_memory | Kubernetes: Resource quota - memory requests  Метрика измеряет квоту memory requests. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует memory requests в рамках resource quota. | Byte | autoavgmaxmin |
| builtin:kubernetes.resourcequota.requests\_memory\_used | Kubernetes: Resource quota - использованные memory requests  Метрика измеряет использованную квоту memory requests. Наиболее детальный уровень агрегации, это resource quota. Значение соответствует использованным memory requests в рамках resource quota. | Byte | autoavgmaxmin |

### Workload

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.workload.conditions | Kubernetes: Workload conditions  Метрика описывает состояние workload Kubernetes. Наиболее детальный уровень агрегации, это workload. | Count | autoavgmaxmin |
| builtin:kubernetes.workload.containers\_desired | Kubernetes: Pod - желаемое количество контейнеров  Метрика измеряет количество желаемых контейнеров. Наиболее детальный уровень агрегации, это workload. Значение, это количество всех контейнеров в спецификации пода. | Count | autoavgmaxmin |
| builtin:kubernetes.workload.cpu\_throttled | Kubernetes: Container - CPU throttled (by workload)  Метрика измеряет суммарное троттлинг CPU по контейнеру. Наиболее детальный уровень агрегации, это workload. | Millicores | autoavgmaxmin |
| builtin:kubernetes.workload.cpu\_usage | Kubernetes: Container - CPU usage (by workload)  Метрика измеряет суммарный CPU, потреблённый контейнером (пользовательское использование + системное использование). Наиболее детальный уровень агрегации, это workload. | Millicores | autoavgmaxmin |
| builtin:kubernetes.workload.limits\_cpu | Kubernetes: Pod - CPU limits (by workload)  Метрика измеряет лимиты CPU. Наиболее детальный уровень агрегации, это workload. Значение, это сумма лимитов CPU всех app-контейнеров пода. | Millicores | autoavgmaxmin |
| builtin:kubernetes.workload.limits\_memory | Kubernetes: Pod - memory limits (by workload)  Метрика измеряет лимиты памяти. Наиболее детальный уровень агрегации, это workload. Значение, это сумма лимитов памяти всех app-контейнеров пода. | Byte | autoavgmaxmin |
| builtin:kubernetes.workload.memory\_resident\_set\_size | [Deprecated] Kubernetes: Container - Memory RSS (by workload)  Метрика измеряет реальный resident set size (RSS) по контейнеру. RSS, это объём физической памяти, используемой cgroup контейнера: либо total\_rss + total\_mapped\_file (cgroup v1), либо anon + file\_mapped (cgroup v2). Наиболее детальный уровень агрегации, это workload. Устарело, используйте builtin:kubernetes.workload.memory\_working\_set. | Byte | autoavgmaxmin |
| builtin:kubernetes.workload.memory\_working\_set | Kubernetes: Container - Working set memory (by workload)  Метрика измеряет текущий working set memory (память, которую невозможно освободить под давлением) по контейнеру. OOM Killer запускается, если working set превышает лимит. Наиболее детальный уровень агрегации, это workload. | Byte | autoavgmaxmin |
| builtin:kubernetes.workload.pods\_desired | Kubernetes: Workload - желаемое количество подов  Метрика измеряет количество желаемых подов. Наиболее детальный уровень агрегации, это workload. Значение соответствует полю `replicas` в ресурсе deployment и полю `desiredNumberScheduled` в статусе ресурса daemon set (как пример). | Count | autoavgmaxmin |
| builtin:kubernetes.workload.requests\_cpu | Kubernetes: Pod - CPU requests (by workload)  Метрика измеряет CPU requests. Наиболее детальный уровень агрегации, это workload. Значение, это сумма CPU requests всех app-контейнеров пода. | Millicores | autoavgmaxmin |
| builtin:kubernetes.workload.requests\_memory | Kubernetes: Pod - memory requests (by workload)  Метрика измеряет memory requests. Наиболее детальный уровень агрегации, это workload. Значение, это сумма memory requests всех app-контейнеров пода. | Byte | autoavgmaxmin |

### Other kubernetes metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:kubernetes.containers | Kubernetes: Количество контейнеров  Метрика измеряет количество контейнеров. Наиболее детальный уровень агрегации, это workload. Метрика считает количество всех контейнеров. | Count | autoavgmaxmin |
| builtin:kubernetes.events | Kubernetes: Количество событий  Метрика считает события Kubernetes. Наиболее детальный уровень агрегации, это причина события. Значение соответствует количеству событий, возвращаемых эндпоинтом событий Kubernetes. Метрика зависит от мониторинга событий Kubernetes. Точки данных за период, в течение которого мониторинг событий отключён, не отображаются. | Count | autovalue |
| builtin:kubernetes.nodes | Kubernetes: Количество нод  Метрика измеряет количество нод. Наиболее детальный уровень агрегации, это кластер. Значение, это количество всех нод. | Count | autoavgmaxmin |
| builtin:kubernetes.pods | Kubernetes: Количество подов (by workload)  Метрика измеряет количество подов. Наиболее детальный уровень агрегации, это workload. Значение соответствует количеству всех подов. | Count | autoavgmaxmin |
| builtin:kubernetes.workloads | Kubernetes: Количество workload'ов  Метрика измеряет количество workload'ов. Наиболее детальный уровень агрегации, это namespace. Значение соответствует количеству всех workload'ов. | Count | autoavgmaxmin |

## Process

### Availability

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:pgi.availability.state | Process availability  Метрика состояния доступности процесса, сообщается с интервалом 1 минута | Count | autovalue |

### Other process metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:pgi.availability | Process Availability rate  Метрика операционной доступности для PGI | Percent (%) | autoavg |

## Process

### Прочие метрики процессов

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:process.bytesReceived | Входящий трафик процесса  Метрика показывает объём входящего трафика процесса. Помогает выявлять процессы, создающие высокую сетевую нагрузку на хосте. Результат выражается в килобайтах. Поддерживает измерения: "PID" (process.pid), "Parent PID" (process.parent\_pid), "process owner" (process.owner), "process executable name" (process.executable.name), "process executable path" (process.executable.path), "process command line" (process.command\_line) и "Process group instance" (dt.entity.process\_group\_instance). Метрика собирается только если функция Process instance snapshot включена и активирована; период сбора ограничен рамками функции. Подробнее: [Process instance snapshots﻿](https://dt-url.net/process-instance-snapshots-doc). | kB | autoavgcountmaxminsum |
| builtin:process.bytesSent | Исходящий трафик процесса  Метрика показывает объём исходящего трафика процесса. Помогает выявлять процессы, создающие высокую сетевую нагрузку на хосте. Результат выражается в килобайтах. Поддерживает измерения: "PID" (process.pid), "Parent PID" (process.parent\_pid), "process owner" (process.owner), "process executable name" (process.executable.name), "process executable path" (process.executable.path), "process command line" (process.command\_line) и "Process group instance" (dt.entity.process\_group\_instance). Метрика собирается только если функция Process instance snapshot включена и активирована; период сбора ограничен рамками функции. Подробнее: [Process instance snapshots﻿](https://dt-url.net/process-instance-snapshots-doc). | kB | autoavgcountmaxminsum |
| builtin:process.cpu | Среднее потребление CPU процессом  Метрика показывает процент использования CPU процессом. Значение метрики, это сумма процессорного времени всех воркеров процесса, делённая на суммарное доступное процессорное время. Результат выражается в процентах. Значение 100% означает, что процесс использует все доступные ресурсы CPU хоста. Поддерживает измерения: "PID" (process.pid), "Parent PID" (process.parent\_pid), "process owner" (process.owner), "process executable name" (process.executable.name), "process executable path" (process.executable.path), "process command line" (process.command\_line) и "Process group instance" (dt.entity.process\_group\_instance). Метрика собирается только если функция Process instance snapshot включена и активирована; период сбора ограничен рамками функции. Подробнее: [Process instance snapshots﻿](https://dt-url.net/process-instance-snapshots-doc). | Percent (%) | autoavgcountmaxminsum |
| builtin:process.memory | Потребление памяти процессом  Метрика показывает объём памяти, используемый процессом. Помогает выявлять процессы с высоким потреблением памяти и утечками памяти. Результат выражается в байтах. Поддерживает измерения: "PID" (process.pid), "Parent PID" (process.parent\_pid), "process owner" (process.owner), "process executable name" (process.executable.name), "process executable path" (process.executable.path), "process command line" (process.command\_line) и "Process group instance" (dt.entity.process\_group\_instance). Метрика собирается только если функция Process instance snapshot включена и активирована; период сбора ограничен рамками функции. Подробнее: [Process instance snapshots﻿](https://dt-url.net/process-instance-snapshots-doc). | Byte | autoavgcountmaxminsum |

## Queue

### Прочие метрики очередей

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:queue.incoming\_requests | Входящие сообщения  Количество входящих сообщений в очереди или топике | Count | autoavgcountmaxminsum |
| builtin:queue.outgoing\_requests | Исходящие сообщения  Количество исходящих сообщений из очереди или топика | Count | autoavgcountmaxminsum |

## Security

### Attack

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:security.attack.new | Новые атаки  Количество атак, зафиксированных за последнее время. Метрика поддерживает селектор management zone. | Count | autovalue |

### Security problems

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:security.securityProblem.muted.new.global | Новые заглушённые проблемы безопасности (global)  Количество уязвимостей, заглушённых за последнее время. Значение метрики не зависит от настроенных management zone (и потому является глобальным). | Count | autovalue |
| builtin:security.securityProblem.open.new.global | Новые открытые проблемы безопасности (global)  Количество уязвимостей, созданных за последнее время. Значение метрики не зависит от настроенных management zone (и потому является глобальным). | Count | autovalue |
| builtin:security.securityProblem.open.new.managementZone | Новые открытые проблемы безопасности (split by Management Zone)  Количество уязвимостей, созданных за последнее время. Значение метрики разбито по management zone. | Count | autovalue |
| builtin:security.securityProblem.open.global | Открытые проблемы безопасности (global)  Количество актуальных открытых уязвимостей за последнюю минуту. Значение метрики не зависит от настроенных management zone (и потому является глобальным). | Count | autoavgmaxmin |
| builtin:security.securityProblem.open.managementZone | Открытые проблемы безопасности (split by Management Zone)  Количество актуальных открытых уязвимостей за последнюю минуту. Значение метрики разбито по management zone. | Count | autoavgmaxmin |
| builtin:security.securityProblem.resolved.new.global | Новые решённые проблемы безопасности (global)  Количество уязвимостей, устранённых за последнее время. Значение метрики не зависит от настроенных management zone (и потому является глобальным). | Count | autovalue |

### Vulnerabilities

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:security.vulnerabilities.global.countAffectedProcessGroups.all | Vulnerabilities, количество затронутых групп процессов (global)  Общее количество уникальных затронутых групп процессов по всем открытым уязвимостям в разрезе технологий. Значение метрики не зависит от настроенных management zone (и потому является глобальным). | Count | autoavgmaxmin |
| builtin:security.vulnerabilities.global.countAffectedProcessGroups.notMuted | Vulnerabilities, количество затронутых незаглушённых групп процессов (global)  Общее количество уникальных затронутых групп процессов по всем открытым, незаглушённым уязвимостям в разрезе технологий. Значение метрики не зависит от настроенных management zone (и потому является глобальным). | Count | autoavgmaxmin |
| builtin:security.vulnerabilities.countAffectedEntities | Vulnerabilities, количество затронутых сущностей  Общее количество уникальных затронутых сущностей по всем открытым уязвимостям. Метрика поддерживает селектор management zone. | Count | autovalue |

## Services

### CPU

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:service.cpu.perRequest | Процессорное время  Процессорное время, потреблённое конкретным запросом. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Microsecond | autoavgcountmaxminsum |
| builtin:service.cpu.time | Процессорное время сервиса  Процессорное время, потреблённое конкретным сервисом. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Microsecond | autovalue |

### Database connections

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:service.dbconnections.failure | Неудачные подключения  Количество неуспешных попыток подключения относительно всех попыток подключения. О том, как анализировать базы данных, см. [Analyze database services﻿](https://dt-url.net/database-services). | Count | autovalue |
| builtin:service.dbconnections.failureRate | Доля неудачных подключений  Доля неуспешных попыток подключения относительно всех попыток подключения. О том, как анализировать базы данных, см. [Analyze database services﻿](https://dt-url.net/database-services). | Percent (%) | autovalue |
| builtin:service.dbconnections.success | Успешные подключения  Общее количество успешно установленных подключений к базе данных данным сервисом. О том, как анализировать базы данных, см. [Analyze database services﻿](https://dt-url.net/database-services). | Count | autovalue |
| builtin:service.dbconnections.successRate | Доля успешных подключений  Доля успешных попыток подключения относительно всех попыток подключения. О том, как анализировать базы данных, см. [Analyze database services﻿](https://dt-url.net/database-services). | Percent (%) | autovalue |
| builtin:service.dbconnections.total | Общее количество подключений  Общее количество попыток установить подключение к базе данных данным сервисом. О том, как анализировать базы данных, см. [Analyze database services﻿](https://dt-url.net/database-services). | Count | autovalue |

### Errors

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:service.errors.client.count` | Количество ошибок на стороне клиента. Неуспешные запросы к сервису, измеренные на стороне клиента. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.errors.client.rate` | Доля сбоев (ошибки на стороне клиента) | Percent (%) | autoavg |
| `builtin:service.errors.client.successCount` | Количество вызовов без ошибок на стороне клиента | Count | autovalue |
| `builtin:service.errors.fivexx.count` | Количество ошибок HTTP 5xx. HTTP-запросы с кодом состояния от 500 до 599 для заданного ключевого запроса, измеренные на стороне сервера. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.errors.fivexx.rate` | Доля сбоев (ошибки HTTP 5xx) | Percent (%) | autoavg |
| `builtin:service.errors.fivexx.successCount` | Количество вызовов без ошибок HTTP 5xx | Count | autovalue |
| `builtin:service.errors.fourxx.count` | Количество ошибок HTTP 4xx. HTTP-запросы с кодом состояния от 400 до 499 для заданного ключевого запроса, измеренные на стороне сервера. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.errors.fourxx.rate` | Доля сбоев (ошибки HTTP 4xx) | Percent (%) | autoavg |
| `builtin:service.errors.fourxx.successCount` | Количество вызовов без ошибок HTTP 4xx | Count | autovalue |
| `builtin:service.errors.server.count` | Количество ошибок на стороне сервера. Неуспешные запросы к сервису, измеренные на стороне сервера. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.errors.server.rate` | Доля сбоев (ошибки на стороне сервера) | Percent (%) | autoavg |
| `builtin:service.errors.server.successCount` | Количество вызовов без ошибок на стороне сервера | Count | autovalue |
| `builtin:service.errors.total.count` | Количество ошибок любого типа. Неуспешные запросы к сервису, измеренные на стороне сервера или клиента. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.errors.total.rate` | Доля сбоев (ошибки любого типа) | Percent (%) | autoavg |
| `builtin:service.errors.total.successCount` | Количество вызовов без ошибок любого типа | Count | autovalue |

### Key requests

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:service.keyRequest.count.client` | Количество запросов, сторона клиента. Число запросов для заданного ключевого запроса, измеренное на стороне клиента. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Count | autovalue |
| `builtin:service.keyRequest.count.server` | Количество запросов, сторона сервера. Число запросов для заданного ключевого запроса, измеренное на стороне сервера. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Count | autovalue |
| `builtin:service.keyRequest.count.total` | Количество запросов. Число запросов для заданного ключевого запроса. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Count | autovalue |
| `builtin:service.keyRequest.cpu.perRequest` | CPU на запрос. Время CPU для заданного ключевого запроса. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxminsum |
| `builtin:service.keyRequest.cpu.time` | Время CPU ключевого запроса сервиса. Время CPU для заданного ключевого запроса. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxminsum |
| `builtin:service.keyRequest.errors.client.count` | Количество ошибок на стороне клиента. Неуспешные запросы для заданного ключевого запроса, измеренные на стороне клиента. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.keyRequest.errors.client.rate` | Доля сбоев (ошибки на стороне клиента) | Percent (%) | autoavg |
| `builtin:service.keyRequest.errors.client.successCount` | Количество вызовов без ошибок на стороне клиента | Count | autovalue |
| `builtin:service.keyRequest.errors.fivexx.count` | Количество ошибок HTTP 5xx. Доля HTTP-запросов с кодом состояния от 500 до 599 для заданного ключевого запроса. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.keyRequest.errors.fivexx.rate` | Доля сбоев (ошибки HTTP 5xx) | Percent (%) | autoavg |
| `builtin:service.keyRequest.errors.fivexx.successCount` | Количество вызовов без ошибок HTTP 5xx | Count | autovalue |
| `builtin:service.keyRequest.errors.fourxx.count` | Количество ошибок HTTP 4xx. Доля HTTP-запросов с кодом состояния от 400 до 499 для заданного ключевого запроса. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.keyRequest.errors.fourxx.rate` | Доля сбоев (ошибки HTTP 4xx) | Percent (%) | autoavg |
| `builtin:service.keyRequest.errors.fourxx.successCount` | Количество вызовов без ошибок HTTP 4xx | Count | autovalue |
| `builtin:service.keyRequest.errors.server.count` | Количество ошибок на стороне сервера. Неуспешные запросы для заданного ключевого запроса, измеренные на стороне сервера. Подробнее об обнаружении сбоев: [Configure service failure detection﻿](https://dt-url.net/service-failuredetection). | Count | autovalue |
| `builtin:service.keyRequest.errors.server.rate` | Доля сбоев (ошибки на стороне сервера) | Percent (%) | autoavg |
| `builtin:service.keyRequest.errors.server.successCount` | Количество вызовов без ошибок на стороне сервера | Count | autovalue |
| `builtin:service.keyRequest.response.client` | Время отклика на стороне клиента. Время отклика для заданного ключевого запроса, измеренное на стороне клиента. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:service.keyRequest.response.server` | Время отклика на стороне сервера. Время отклика для заданного ключевого запроса, измеренное на стороне сервера. Метрика записывается для каждого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:service.keyRequest.response.time` | Время отклика ключевого запроса. Время отклика для заданного ключевого запроса. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:service.keyRequest.successes.server.rate` | Доля успешных запросов (сторона сервера) | Percent (%) | autoavg |
| `builtin:service.keyRequest.dbChildCallCount` | Количество вызовов к базам данных | Count | autovalue |
| `builtin:service.keyRequest.dbChildCallTime` | Время, затраченное на вызовы к базам данных | Microsecond | autovalue |
| `builtin:service.keyRequest.ioTime` | Время ввода/вывода | Microsecond | autovalue |
| `builtin:service.keyRequest.lockTime` | Время ожидания блокировок | Microsecond | autovalue |
| `builtin:service.keyRequest.nonDbChildCallCount` | Количество вызовов к другим сервисам | Count | autovalue |
| `builtin:service.keyRequest.nonDbChildCallTime` | Время, затраченное на вызовы к другим сервисам | Microsecond | autovalue |
| `builtin:service.keyRequest.totalProcessingTime` | Общее время обработки. Суммарное время обработки для заданного ключевого запроса, включая возможную дополнительную асинхронную обработку. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах: [Monitor key request﻿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:service.keyRequest.waitTime` | Время ожидания | Microsecond | autovalue |

### Request

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.request.service\_mesh.count | Unified service mesh request count  Количество запросов service mesh, полученных данным сервисом. О том, как Dynatrace определяет сервисы, см. [Service detection and naming﻿](https://dt-url.net/am-service-meshes). | Count | autovalue |
| builtin:service.request.service\_mesh.count\_service\_aggregation | Unified service mesh request count (by service)  Количество запросов service mesh, полученных данным сервисом. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace определяет сервисы, см. [Service detection and naming﻿](https://dt-url.net/am-service-meshes). | Count | autovalue |
| builtin:service.request.service\_mesh.failure\_count | Unified service mesh request failure count  Количество неуспешных запросов service mesh, полученных данным сервисом. О том, как Dynatrace определяет сбои сервисов, см. [Configure service failure detection﻿](https://dt-url.net/service-mesh-failuredetection). | Count | autovalue |
| builtin:service.request.service\_mesh.failure\_count\_service\_aggregation | Unified service mesh request failure count (by service)  Количество неуспешных запросов service mesh, полученных данным сервисом. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace определяет сбои сервисов, см. [Configure service failure detection﻿](https://dt-url.net/service-mesh-failuredetection). | Count | autovalue |
| builtin:service.request.service\_mesh.response\_time | Unified service mesh request response time  Время ответа входящего трафика service mesh, измеренное в микросекундах. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile |
| builtin:service.request.service\_mesh.response\_time\_service\_aggregation | Unified service mesh request response time (by service)  Время ответа входящего трафика service mesh, измеренное в микросекундах. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile |
| builtin:service.request.count\_chart | Unified service request count (by service, endpoint)  Количество запросов, полученных данным сервисом. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace определяет и анализирует сервисы, см. [Services﻿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.count\_service\_aggregation | Unified service request count (by service)  Количество запросов, полученных данным сервисом. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace определяет и анализирует сервисы, см. [Services﻿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.failure\_count | Unified service failure count  Количество неуспешных запросов, полученных данным сервисом. О том, как Dynatrace определяет и анализирует сервисы, см. [Services﻿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.failure\_count\_chart | Unified service failure count (by service, endpoint)  Количество неуспешных запросов, полученных данным сервисом. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace определяет и анализирует сервисы, см. [Services﻿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.failure\_count\_service\_aggregation | Unified service failure count (by service)  Количество неуспешных запросов, полученных данным сервисом. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace определяет и анализирует сервисы, см. [Services﻿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.request.response\_time\_chart | Unified service request response time (by service, endpoint)  Время ответа сервиса, измеренное в микросекундах на стороне сервера. Время ответа, это время до отправки ответа вызывающему приложению, процессу или другому сервису. Не включает последующую асинхронную обработку. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile |
| builtin:service.request.response\_time\_service\_aggregation | Unified service request response time (by service)  Время ответа сервиса, измеренное в микросекундах на стороне сервера. Время ответа, это время до отправки ответа вызывающему приложению, процессу или другому сервису. Не включает последующую асинхронную обработку. Сокращённые измерения для ускорения построения графиков. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile |

### Request count

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.requestCount.client | Request count - client  Количество запросов, полученных данным сервисом, измеренное на стороне клиента. Метрика поддерживает разбивку по сервисам. О том, как Dynatrace определяет и анализирует сервисы, см. [Services﻿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.requestCount.server | Request count - server  Количество запросов, полученных данным сервисом, измеренное на стороне сервера. Метрика поддерживает разбивку по сервисам. О том, как Dynatrace определяет и анализирует сервисы, см. [Services﻿](https://dt-url.net/am-services). | Count | autovalue |
| builtin:service.requestCount.total | Request count  Количество запросов, полученных данным сервисом. Метрика поддерживает разбивку по сервисам. О том, как Dynatrace определяет и анализирует сервисы, см. [Services﻿](https://dt-url.net/am-services). | Count | autovalue |

### Response time

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.response.group.client | Client side response time  Время ответа для данного ключевого запроса по типу запроса, измеренное на стороне клиента. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах см. [Monitor key request﻿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.response.group.server | Server side response time  Время ответа для данного ключевого запроса по типу запроса, измеренное на стороне сервера. Метрика записывается для каждого ключевого запроса. Подробнее о ключевых запросах см. [Monitor key request﻿](https://dt-url.net/key-request). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.response.client | Client side response time | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.response.server | Server side response time | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.response.time | Response time  Время, затраченное конкретным сервисом до отправки ответа вызывающему приложению, процессу, сервису и т.д. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Microsecond | autoavgcountmaxmedianminpercentilesum |

### Success rate

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.successes.server.rate | Success rate (server side) | Percent (%) | autoavg |

### Total processing time

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.totalProcessingTime.group.totalProcessingTime | Total processing time  Суммарное время обработки конкретного типа запроса, включая асинхронную обработку. Учитывается то, что асинхронная обработка может продолжаться после отправки ответа. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Microsecond | autoavgcountmaxmedianminpercentilesum |

### Other services metrics

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:service.totalProcessingTime | Total processing time  Суммарное время обработки конкретного сервиса, включая асинхронную обработку. Учитывается то, что асинхронная обработка может продолжаться после отправки ответа. О том, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings﻿](https://dt-url.net/service-timings). | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:service.dbChildCallCount | Number of calls to databases | Count | autovalue |
| builtin:service.dbChildCallTime | Time spent in database calls | Microsecond | autovalue |
| builtin:service.ioTime | IO time | Microsecond | autovalue |
| builtin:service.lockTime | Lock time | Microsecond | autovalue |
| builtin:service.nonDbChildCallCount | Number of calls to other services | Count | autovalue |
| builtin:service.nonDbChildCallTime | Time spent in calls to other services | Microsecond | autovalue |
| builtin:service.waitTime | Wait time | Microsecond | autovalue |

## Synthetic monitoring

### Browser

| Metric key | Название и описание | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:synthetic.browser.actionDuration.custom` | Длительность действия, custom action [browser monitor]  Длительность пользовательских (custom) действий; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.actionDuration.custom.geo` | Длительность действия, custom action (по геолокации) [browser monitor]  Длительность пользовательских (custom) действий; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.actionDuration.load` | Длительность действия, load action [browser monitor]  Длительность действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.actionDuration.load.geo` | Длительность действия, load action (по геолокации) [browser monitor]  Длительность действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.actionDuration.xhr` | Длительность действия, XHR action [browser monitor]  Длительность XHR-действий; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.actionDuration.xhr.geo` | Длительность действия, XHR action (по геолокации) [browser monitor]  Длительность XHR-действий; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.availability` | Доступность монитора [browser monitor] | Count | autoavgcountmaxminsum |
| `builtin:synthetic.browser.availability.location.total` | Коэффициент доступности (по локации) [browser monitor]  Коэффициент доступности browser-мониторов. | Percent (%) | autoavg |
| `builtin:synthetic.browser.availability.location.totalWoMaintenanceWindow` | Коэффициент доступности без учёта окон обслуживания (по локации) [browser monitor]  Коэффициент доступности browser-мониторов без учёта окон обслуживания. | Percent (%) | autoavg |
| `builtin:synthetic.browser.cumulativeLayoutShift.load` | Cumulative layout shift, load action [browser monitor]  Оценка непредвиденного смещения видимых элементов страницы. Рассчитывается для действий загрузки; разбивка по монитору. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.cumulativeLayoutShift.load.geo` | Cumulative layout shift, load action (по геолокации) [browser monitor]  Оценка непредвиденного смещения видимых элементов страницы. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.domInteractive.load` | DOM interactive, load action [browser monitor]  Время до перехода страницы в состояние «interactive» и готовности принимать ввод. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.domInteractive.load.geo` | DOM interactive, load action (по геолокации) [browser monitor]  Время до перехода страницы в состояние «interactive» и готовности принимать ввод. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.errorCodes` | Детализация ошибок (по коду ошибки) [browser monitor]  Количество обнаруженных ошибок; разбивка по монитору, коду ошибки. | Count | autovalue |
| `builtin:synthetic.browser.errorCodes.geo` | Детализация ошибок (по геолокации, коду ошибки) [browser monitor]  Количество обнаруженных ошибок; разбивка по запускам монитора. | Count | autovalue |
| `builtin:synthetic.browser.event.actionDuration.custom` | Длительность действия, custom action (по событию) [browser monitor]  Длительность пользовательских (custom) действий; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.actionDuration.custom.geo` | Длительность действия, custom action (по событию, геолокации) [browser monitor]  Длительность пользовательских (custom) действий; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.actionDuration.load` | Длительность действия, load action (по событию) [browser monitor]  Длительность действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.actionDuration.load.geo` | Длительность действия, load action (по событию, геолокации) [browser monitor]  Длительность действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.actionDuration.xhr` | Длительность действия, XHR action (по событию) [browser monitor]  Длительность XHR-действий; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.actionDuration.xhr.geo` | Длительность действия, XHR action (по событию, геолокации) [browser monitor]  Длительность XHR-действий; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.cumulativeLayoutShift.load` | Cumulative layout shift, load action (по событию) [browser monitor]  Оценка непредвиденного смещения видимых элементов страницы. Рассчитывается для действий загрузки; разбивка по событию. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.cumulativeLayoutShift.load.geo` | Cumulative layout shift, load action (по событию, геолокации) [browser monitor]  Оценка непредвиденного смещения видимых элементов страницы. Рассчитывается для действий загрузки; разбивка по событию, геолокации. |  | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.domInteractive.load` | DOM interactive, load action (по событию) [browser monitor]  Время до перехода страницы в состояние «interactive» и готовности принимать ввод. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.domInteractive.load.geo` | DOM interactive, load action (по событию, геолокации) [browser monitor]  Время до перехода страницы в состояние «interactive» и готовности принимать ввод. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.errorCodes` | Детализация ошибок (по событию, коду ошибки) [browser monitor]  Количество обнаруженных ошибок; разбивка по событию, коду ошибки. | Count | autovalue |
| `builtin:synthetic.browser.event.errorCodes.geo` | Детализация ошибок (по событию, геолокации, коду ошибки) [browser monitor]  Количество обнаруженных ошибок; разбивка по событию, геолокации, коду ошибки. | Count | autovalue |
| `builtin:synthetic.browser.event.failure` | Количество неудачных событий (по событию) [browser monitor]  Количество неудачных событий монитора; разбивка по событию. | Count | autovalue |
| `builtin:synthetic.browser.event.failure.geo` | Количество неудачных событий (по событию, геолокации) [browser monitor]  Количество неудачных событий монитора; разбивка по событию, геолокации. | Count | autovalue |
| `builtin:synthetic.browser.event.firstByte.load` | Время до первого байта, load action (по событию) [browser monitor]  Время до получения первого байта ответа от сервера, кэшей приложения или локального ресурса. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.firstByte.load.geo` | Время до первого байта, load action (по событию, геолокации) [browser monitor]  Время до получения первого байта ответа от сервера, кэшей приложения или локального ресурса. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.firstByte.xhr` | Время до первого байта, XHR action (по событию) [browser monitor]  Время до получения первого байта ответа от сервера, кэшей приложения или локального ресурса. Рассчитывается для XHR-действий; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.firstByte.xhr.geo` | Время до первого байта, XHR action (по событию, геолокации) [browser monitor]  Время до получения первого байта ответа от сервера, кэшей приложения или локального ресурса. Рассчитывается для XHR-действий; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.largestContentfulPaint.load` | Largest contentful paint, load action (по событию) [browser monitor]  Время до отрисовки наибольшего элемента в области просмотра. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.largestContentfulPaint.load.geo` | Largest contentful paint, load action (по событию, геолокации) [browser monitor]  Время до отрисовки наибольшего элемента в области просмотра. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.loadEventEnd.load` | Конец события загрузки, load action (по событию) [browser monitor]  Время до завершения события загрузки страницы. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.loadEventEnd.load.geo` | Конец события загрузки, load action (по событию, геолокации) [browser monitor]  Время до завершения события загрузки страницы. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.loadEventStart.load` | Начало события загрузки, load action (по событию) [browser monitor]  Время до начала события загрузки страницы. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.loadEventStart.load.geo` | Начало события загрузки, load action (по событию, геолокации) [browser monitor]  Время до начала события загрузки страницы. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.networkContribution.load` | Вклад сети, load action (по событию) [browser monitor]  Время на запрос и получение ресурсов (включая DNS-поиск, редиректы и время TCP-соединения). Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.networkContribution.load.geo` | Вклад сети, load action (по событию, геолокации) [browser monitor]  Время на запрос и получение ресурсов (включая DNS-поиск, редиректы и время TCP-соединения). Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.networkContribution.xhr` | Вклад сети, XHR action (по событию) [browser monitor]  Время на запрос и получение ресурсов (включая DNS-поиск, редиректы и время TCP-соединения). Рассчитывается для XHR-действий; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.networkContribution.xhr.geo` | Вклад сети, XHR action (по событию, геолокации) [browser monitor]  Время на запрос и получение ресурсов (включая DNS-поиск, редиректы и время TCP-соединения). Рассчитывается для XHR-действий; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.responseEnd.load` | Конец ответа, load action (по событию) [browser monitor]  (также HTML downloaded) Время до получения user agent последнего байта ответа или закрытия транспортного соединения, смотря что наступит раньше. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.responseEnd.load.geo` | Конец ответа, load action (по событию, геолокации) [browser monitor]  (также HTML downloaded) Время до получения user agent последнего байта ответа или закрытия транспортного соединения, смотря что наступит раньше. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.responseEnd.xhr` | Конец ответа, XHR action (по событию) [browser monitor]  (также HTML downloaded) Время до получения user agent последнего байта ответа или закрытия транспортного соединения, смотря что наступит раньше. Рассчитывается для XHR-действий; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.responseEnd.xhr.geo` | Конец ответа, XHR action (по событию, геолокации) [browser monitor]  (также HTML downloaded) Время до получения user agent последнего байта ответа или закрытия транспортного соединения, смотря что наступит раньше. Рассчитывается для XHR-действий; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.serverContribution.load` | Вклад сервера, load action (по событию) [browser monitor]  Время на серверную обработку страницы. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.serverContribution.load.geo` | Вклад сервера, load action (по событию, геолокации) [browser monitor]  Время на серверную обработку страницы. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.serverContribution.xhr` | Вклад сервера, XHR action (по событию) [browser monitor]  Время на серверную обработку страницы. Рассчитывается для XHR-действий; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.serverContribution.xhr.geo` | Вклад сервера, XHR action (по событию, геолокации) [browser monitor]  Время на серверную обработку страницы. Рассчитывается для XHR-действий; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.speedIndex.load` | Speed index, load action (по событию) [browser monitor]  Оценка скорости отрисовки видимой части страницы. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.speedIndex.load.geo` | Speed index, load action (по событию, геолокации) [browser monitor]  Оценка скорости отрисовки видимой части страницы. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.success` | Количество успешных событий (по событию) [browser monitor]  Количество успешных событий монитора; разбивка по событию. | Count | autovalue |
| `builtin:synthetic.browser.event.success.geo` | Количество успешных событий (по событию, геолокации) [browser monitor]  Количество успешных событий монитора; разбивка по событию, геолокации. | Count | autovalue |
| `builtin:synthetic.browser.event.total` | Общее количество событий (по событию) [browser monitor]  Общее количество запусков событий монитора; разбивка по событию. | Count | autovalue |
| `builtin:synthetic.browser.event.total.geo` | Общее количество событий (по событию, геолокации) [browser monitor]  Общее количество запусков событий монитора; разбивка по событию, геолокации. | Count | autovalue |
| `builtin:synthetic.browser.event.totalDuration` | Суммарная длительность (по событию) [browser monitor]  Длительность всех действий в событии; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.totalDuration.geo` | Суммарная длительность (по событию, геолокации) [browser monitor]  Длительность всех действий в событии; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.visuallyComplete.load` | Visually complete, load action (по событию) [browser monitor]  Время до полной отрисовки содержимого в области просмотра. Рассчитывается для действий загрузки; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.visuallyComplete.load.geo` | Visually complete, load action (по событию, геолокации) [browser monitor]  Время до полной отрисовки содержимого в области просмотра. Рассчитывается для действий загрузки; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.event.visuallyComplete.xhr` | Visually complete, XHR action (по событию) [browser monitor]  Время до полной отрисовки содержимого в области просмотра. Рассчитывается для XHR-действий; разбивка по событию. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.event.visuallyComplete.xhr.geo` | Visually complete, XHR action (по событию, геолокации) [browser monitor]  Время до полной отрисовки содержимого в области просмотра. Рассчитывается для XHR-действий; разбивка по событию, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.failure` | Количество неудачных запусков [browser monitor]  Количество неудачных запусков монитора; разбивка по монитору. | Count | autovalue |
| `builtin:synthetic.browser.failure.geo` | Количество неудачных запусков (по геолокации) [browser monitor]  Количество неудачных запусков монитора; разбивка по монитору, геолокации. | Count | autovalue |
| `builtin:synthetic.browser.firstByte.load` | Время до первого байта, load action [browser monitor]  Время до получения первого байта ответа от сервера, кэшей приложения или локального ресурса. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.firstByte.load.geo` | Время до первого байта, load action (по геолокации) [browser monitor]  Время до получения первого байта ответа от сервера, кэшей приложения или локального ресурса. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.firstByte.xhr` | Время до первого байта, XHR action [browser monitor]  Время до получения первого байта ответа от сервера, кэшей приложения или локального ресурса. Рассчитывается для XHR-действий; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.firstByte.xhr.geo` | Время до первого байта, XHR action (по геолокации) [browser monitor]  Время до получения первого байта ответа от сервера, кэшей приложения или локального ресурса. Рассчитывается для XHR-действий; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.largestContentfulPaint.load` | Largest contentful paint, load action [browser monitor]  Время до отрисовки наибольшего элемента в области просмотра. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.largestContentfulPaint.load.geo` | Largest contentful paint, load action (по геолокации) [browser monitor]  Время до отрисовки наибольшего элемента в области просмотра. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.loadEventEnd.load` | Конец события загрузки, load action [browser monitor]  Время до завершения события загрузки страницы. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.loadEventEnd.load.geo` | Конец события загрузки, load action (по геолокации) [browser monitor]  Время до завершения события загрузки страницы. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.loadEventStart.load` | Начало события загрузки, load action [browser monitor]  Время до начала события загрузки страницы. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.loadEventStart.load.geo` | Начало события загрузки, load action (по геолокации) [browser monitor]  Время до начала события загрузки страницы. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.networkContribution.load` | Вклад сети, load action [browser monitor]  Время на запрос и получение ресурсов (включая DNS-поиск, редиректы и время TCP-соединения). Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.networkContribution.load.geo` | Вклад сети, load action (по геолокации) [browser monitor]  Время на запрос и получение ресурсов (включая DNS-поиск, редиректы и время TCP-соединения). Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.networkContribution.xhr` | Вклад сети, XHR action [browser monitor]  Время на запрос и получение ресурсов (включая DNS-поиск, редиректы и время TCP-соединения). Рассчитывается для XHR-действий; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.networkContribution.xhr.geo` | Вклад сети, XHR action (по геолокации) [browser monitor]  Время на запрос и получение ресурсов (включая DNS-поиск, редиректы и время TCP-соединения). Рассчитывается для XHR-действий; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.responseEnd.load` | Конец ответа, load action [browser monitor]  (также HTML downloaded) Время до получения user agent последнего байта ответа или закрытия транспортного соединения, смотря что наступит раньше. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.responseEnd.load.geo` | Конец ответа, load action (по геолокации) [browser monitor]  (также HTML downloaded) Время до получения user agent последнего байта ответа или закрытия транспортного соединения, смотря что наступит раньше. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.responseEnd.xhr` | Конец ответа, XHR action [browser monitor]  (также HTML downloaded) Время до получения user agent последнего байта ответа или закрытия транспортного соединения, смотря что наступит раньше. Рассчитывается для XHR-действий; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.responseEnd.xhr.geo` | Конец ответа, XHR action (по геолокации) [browser monitor]  (также HTML downloaded) Время до получения user agent последнего байта ответа или закрытия транспортного соединения, смотря что наступит раньше. Рассчитывается для XHR-действий; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.serverContribution.load` | Вклад сервера, load action [browser monitor]  Время на серверную обработку страницы. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.serverContribution.load.geo` | Вклад сервера, load action (по геолокации) [browser monitor]  Время на серверную обработку страницы. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.serverContribution.xhr` | Вклад сервера, XHR action [browser monitor]  Время на серверную обработку страницы. Рассчитывается для XHR-действий; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.serverContribution.xhr.geo` | Вклад сервера, XHR action (по геолокации) [browser monitor]  Время на серверную обработку страницы. Рассчитывается для XHR-действий; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.speedIndex.load` | Speed index, load action [browser monitor]  Оценка скорости отрисовки видимой части страницы. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.speedIndex.load.geo` | Speed index, load action (по геолокации) [browser monitor]  Оценка скорости отрисовки видимой части страницы. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.step.user_actions.duration` | Длительность пользовательских действий (шаг) [browser monitor]  Длительность отдельного шага browser-монитора, измеренная от начала первого пользовательского действия шага до конца последнего пользовательского действия шага. Источник метрики, новый RUM JavaScript. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.step.user_actions.total_duration` | Суммарная длительность пользовательских действий (шаг) [browser monitor]  Суммарная длительность отдельного шага browser-монитора, рассчитанная как сумма длительностей всех пользовательских действий шага. Источник метрики, новый RUM JavaScript. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.step.user_events.duration` | Длительность пользовательских событий (шаг) [browser monitor]  Длительность отдельного шага browser-монитора, измеренная от начала первого пользовательского события шага до конца последнего пользовательского события шага. Источник метрики, новый RUM JavaScript. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.step.user_events.total_duration` | Суммарная длительность пользовательских событий (шаг) [browser monitor]  Суммарная длительность отдельного шага browser-монитора, рассчитанная как сумма длительностей всех пользовательских событий шага. Источник метрики, новый RUM JavaScript. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.step.duration` | Длительность (шаг) [browser monitor]  Длительность отдельного шага browser-монитора, рассчитанная как сумма длительностей событий пользовательских действий шага. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.success` | Количество успешных запусков [browser monitor]  Количество успешных запусков монитора; разбивка по монитору. | Count | autovalue |
| `builtin:synthetic.browser.success.geo` | Количество успешных запусков (по геолокации) [browser monitor]  Количество успешных запусков монитора; разбивка по монитору, геолокации. | Count | autovalue |
| `builtin:synthetic.browser.total` | Общее количество запусков [browser monitor]  Общее количество запусков монитора; разбивка по монитору. | Count | autovalue |
| `builtin:synthetic.browser.total.geo` | Общее количество запусков (по геолокации) [browser monitor]  Общее количество запусков монитора; разбивка по монитору, геолокации. | Count | autovalue |
| `builtin:synthetic.browser.totalDuration` | Суммарная длительность [browser monitor]  Длительность всех действий в событии; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.totalDuration.geo` | Суммарная длительность (по геолокации) [browser monitor]  Длительность всех действий в событии; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.user_actions.duration` | Длительность пользовательских действий [browser monitor]  Длительность browser-монитора, рассчитанная как сумма длительностей пользовательских действий на уровне всех шагов. Источник метрики, новый RUM JavaScript. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.user_actions.total_duration` | Суммарная длительность пользовательских действий [browser monitor]  Суммарная длительность browser-монитора, рассчитанная как сумма значений метрики «User actions total duration» по всем шагам. Источник метрики, новый RUM JavaScript. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.user_events.duration` | Длительность пользовательских событий [browser monitor]  Длительность browser-монитора, рассчитанная как сумма длительностей пользовательских событий на уровне всех шагов. Источник метрики, новый RUM JavaScript. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.user_events.total_duration` | Суммарная длительность пользовательских событий [browser monitor]  Суммарная длительность browser-монитора, рассчитанная как сумма значений метрики «User events total duration» по всем шагам. Источник метрики, новый RUM JavaScript. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.visuallyComplete.load` | Visually complete, load action [browser monitor]  Время до полной отрисовки содержимого в области просмотра. Рассчитывается для действий загрузки; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.visuallyComplete.load.geo` | Visually complete, load action (по геолокации) [browser monitor]  Время до полной отрисовки содержимого в области просмотра. Рассчитывается для действий загрузки; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.visuallyComplete.xhr` | Visually complete, XHR action [browser monitor]  Время до полной отрисовки содержимого в области просмотра. Рассчитывается для XHR-действий; разбивка по монитору. | Millisecond | autoavgcountmaxmedianminpercentilesum |
| `builtin:synthetic.browser.visuallyComplete.xhr.geo` | Visually complete, XHR action (по геолокации) [browser monitor]  Время до полной отрисовки содержимого в области просмотра. Рассчитывается для XHR-действий; разбивка по монитору, геолокации. | Millisecond | autoavgcountmaxminsum |
| `builtin:synthetic.browser.duration` | Длительность [browser monitor]  Длительность browser-монитора, рассчитанная как сумма длительностей всех шагов. | Millisecond | autoavgcountmaxminsum |

### HTTP

| Metric key | Название и описание | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.http.availability | Доступность монитора [HTTP monitor] | Count | autoavgcountmaxminsum |
| builtin:synthetic.http.availability.location.total | Коэффициент доступности (по локации) [HTTP monitor]  Коэффициент доступности HTTP-мониторов. | Percent (%) | autoavg |
| builtin:synthetic.http.availability.location.totalWoMaintenanceWindow | Коэффициент доступности с исключением окон обслуживания (по локации) [HTTP monitor]  Коэффициент доступности HTTP-мониторов без учёта окон обслуживания. | Percent (%) | autoavg |
| builtin:synthetic.http.dns.geo | Время DNS-поиска (по локации) [HTTP monitor]  Время, затраченное на разрешение имени хоста для целевого URL по сумме всех запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.duration.geo | Длительность (по локации) [HTTP monitor]  Суммарная длительность всех запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.execution.status | Количество выполнений (по статусу) [HTTP monitor]  Число выполнений монитора. | Count | autovalue |
| builtin:synthetic.http.request.dns.geo | Время DNS-поиска (по запросу, локации) [HTTP monitor]  Время, затраченное на разрешение имени хоста для целевого URL для отдельных HTTP-запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.duration.geo | Длительность (по запросу, локации) [HTTP monitor]  Длительность отдельных HTTP-запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.responseSize.geo | Размер ответа (по запросу, локации) [HTTP monitor]  Размер ответа отдельных HTTP-запросов. | Byte | autoavgcountmaxminsum |
| builtin:synthetic.http.request.tcpConnectTime.geo | Время TCP-подключения (по запросу, локации) [HTTP monitor]  Время, затраченное на установку TCP-соединения с сервером (включая SSL) для отдельных HTTP-запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.timeToFirstByte.geo | Время до первого байта (по запросу, локации) [HTTP monitor]  Время от отправки запроса до получения первого байта ответа от сервера, соответствующих кэшей приложения или локального ресурса. Вычисляется для отдельных HTTP-запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.tlsHandshakeTime.geo | Время TLS-рукопожатия (по запросу, локации) [HTTP monitor]  Время, затраченное на завершение TLS-рукопожатия для отдельных HTTP-запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.durationThreshold | Пороговое значение длительности (запрос) (по запросу) [HTTP monitor]  Порог производительности для отдельных HTTP-запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.request.resultStatus | Количество по статусу результата (по запросу, локации) [HTTP monitor]  Число выполнений запроса со статусом результата «успех»/«ошибка». | Count | autoavgcountmaxminsum |
| builtin:synthetic.http.request.statusCode | Количество по коду статуса (по запросу, локации) [HTTP monitor]  Число выполнений запроса, завершившихся с HTTP-кодом статуса. | Count | autovalue |
| builtin:synthetic.http.responseSize.geo | Размер ответа (по локации) [HTTP monitor]  Суммарный размер ответов всех запросов. | Byte | autoavgcountmaxminsum |
| builtin:synthetic.http.tcpConnectTime.geo | Время TCP-подключения (по локации) [HTTP monitor]  Время, затраченное на установку TCP-соединения с сервером (включая SSL) по сумме всех запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.timeToFirstByte.geo | Время до первого байта (по локации) [HTTP monitor]  Время от отправки запроса до получения первого байта ответа от сервера, соответствующих кэшей приложения или локального ресурса. Вычисляется по сумме всех запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.tlsHandshakeTime.geo | Время TLS-рукопожатия (по локации) [HTTP monitor]  Время, затраченное на завершение TLS-рукопожатия по сумме всех запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.durationThreshold | Пороговое значение длительности [HTTP monitor]  Порог производительности по сумме всех запросов. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.http.resultStatus | Количество по статусу результата (по локации) [HTTP monitor]  Число выполнений монитора со статусом результата «успех»/«ошибка». | Count | autoavgcountmaxminsum |
| builtin:synthetic.http.statusCode | Количество по коду статуса (по локации) [HTTP monitor]  Число выполнений монитора, завершившихся с HTTP-кодом статуса. | Count | autovalue |

### Location

| Metric key | Название и описание | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.location.node.component.healthStatus | Количество по статусу работоспособности узла [synthetic]  Число частных Synthetic-узлов и их статус работоспособности. | Count | autoavgcountmaxminsum |
| builtin:synthetic.location.healthStatus | Количество по статусу работоспособности частной локации [synthetic]  Число частных Synthetic-локаций и их статус работоспособности. | Count | autoavgcountmaxminsum |

### MultiProtocol

| Metric key | Название и описание | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.multiProtocol.availability | Доступность монитора [Network Availability monitor] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.availability.excludingMaintenanceWindows | Доступность монитора с исключением окон обслуживания [Network Availability monitor] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.dns.resolutionTime | Время разрешения DNS-запроса [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.packetsReceived | Количество успешных ICMP-пакетов [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.packetsSent | Количество ICMP-пакетов [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.requestExecutionTime | Время выполнения ICMP-запроса [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.roundTripTime | Время кругового обхода ICMP [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.icmp.successRate | Коэффициент успешности ICMP-запросов [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.request.availability | Доступность запроса [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.request.availability.excludingMaintenanceWindows | Доступность запроса с исключением окон обслуживания [Network Availability request] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.request.executionTime | Время выполнения запроса [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.request.executions | Количество выполнений (по статусу) [Network Availability request] | Count | autovalue |
| builtin:synthetic.multiProtocol.step.availability | Доступность шага [Network Availability step] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.step.availability.excludingMaintenanceWindows | Доступность шага с исключением окон обслуживания [Network Availability step] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.step.executionTime | Время выполнения шага [Network Availability step] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.step.executions | Количество выполнений (по статусу) [Network Availability step] | Count | autovalue |
| builtin:synthetic.multiProtocol.step.successRate | Коэффициент успешности шага [Network Availability step] | Count | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.tcp.connectionTime | Время TCP-подключения для запроса [Network Availability request] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.executionTime | Время выполнения монитора [Network Availability monitor] | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.multiProtocol.executions | Количество выполнений (по статусу) [Network Availability monitor] | Count | autovalue |
| builtin:synthetic.multiProtocol.successRate | Коэффициент успешности монитора [Network Availability monitor] | Count | autoavgcountmaxminsum |

### Third party

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:synthetic.external.availability.location.total | Availability rate (by location) [third-party monitor]  Показатель доступности сторонних мониторов. | Percent (%) | autoavg |
| builtin:synthetic.external.availability.location.totalWoMaintenanceWindow | Availability rate - excl. maintenance windows (by location) [third-party monitor]  Показатель доступности сторонних мониторов без учёта окон обслуживания. | Percent (%) | autoavg |
| builtin:synthetic.external.errorDetails | Error count [third-party monitor]  Количество обнаруженных ошибок с разбивкой по монитору, шагу и коду ошибки. | Count | autovalue |
| builtin:synthetic.external.errorDetails.geo | Error count (by location) [third-party monitor]  Количество обнаруженных ошибок с разбивкой по монитору, локации, шагу и коду ошибки. | Count | autovalue |
| builtin:synthetic.external.quality | Test quality rate [third-party monitor]  Показатель качества теста. Рассчитывается делением успешных шагов на общее количество выполненных шагов с разбивкой по монитору. | Percent (%) | autoavgmaxmin |
| builtin:synthetic.external.quality.geo | Test quality rate (by location) [third-party monitor]  Показатель качества теста. Рассчитывается делением успешных шагов на общее количество выполненных шагов с разбивкой по монитору и локации. | Percent (%) | autoavgmaxmin |
| builtin:synthetic.external.responseTime | Response time [third-party monitor]  Время отклика сторонних мониторов с разбивкой по монитору. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.external.responseTime.geo | Response time (by location) [third-party monitor]  Время отклика сторонних мониторов с разбивкой по монитору и локации. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.external.step.responseTime | Response time (by step) [third-party monitor]  Время отклика сторонних мониторов с разбивкой по шагу. | Millisecond | autoavgcountmaxminsum |
| builtin:synthetic.external.step.responseTime.geo | Response time (by step, location) [third-party monitor]  Время отклика сторонних мониторов с разбивкой по шагу и локации. | Millisecond | autoavgcountmaxminsum |

## Technologies

### .NET

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.dotnet.gc.gen0Collections | .NET garbage collection (# Gen 0)  Количество завершённых запусков GC, собравших объекты в куче Gen0 за указанный период, https://dt-url.net/i1038bq | Count | autovalue |
| builtin:tech.dotnet.gc.gen1Collections | .NET garbage collection (# Gen 1)  Количество завершённых запусков GC, собравших объекты в куче Gen1 за указанный период, https://dt-url.net/i1038bq | Count | autovalue |
| builtin:tech.dotnet.gc.gen2Collections | .NET garbage collection (# Gen 2)  Количество завершённых запусков GC, собравших объекты в куче Gen2 за указанный период, https://dt-url.net/i1038bq | Count | autovalue |
| builtin:tech.dotnet.gc.timePercentage | .NET % time in GC  Процент времени, затраченного на сборку мусора | Percent (%) | autoavgmaxmin |
| builtin:tech.dotnet.jit.timePercentage | .NET % time in JIT  Процент времени, затраченного на JIT-компиляцию | Percent (%) | autoavgmaxmin |
| builtin:tech.dotnet.managedThreads.avgNumOfActiveThreads | .NET average number of active threads | Count | autoavgmaxmin |
| builtin:tech.dotnet.memory.LOHConsumption | .NET memory consumption (Large Object Heap)  Потребление памяти .NET объектами в Large Object Heap, https://dt-url.net/es238z7 | Byte | autoavgmaxmin |
| builtin:tech.dotnet.memory.gen0Consumption | .NET memory consumption (heap size Gen 0)  Потребление памяти .NET объектами в куче Gen0, https://dt-url.net/i1038bq | Byte | autoavgmaxmin |
| builtin:tech.dotnet.memory.gen1Consumption | .NET memory consumption (heap size Gen 1)  Потребление памяти .NET объектами в куче Gen1, https://dt-url.net/i1038bq | Byte | autoavgmaxmin |
| builtin:tech.dotnet.memory.gen2Consumption | .NET memory consumption (heap size Gen 2)  Потребление памяти .NET объектами в куче Gen2, https://dt-url.net/i1038bq | Byte | autoavgmaxmin |
| builtin:tech.dotnet.perfmon."#BytesInAllHeaps" | Bytes in all heaps | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#Gen0Collections" | Gen 0 Collections | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#Gen1Collections" | Gen 1 Collections | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#Gen2Collections" | Gen 2 Collections | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#OfCurrentLogicalThreads" | Logical threads | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#OfCurrentPhysicalThreads" | Physical threads | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#TotalCommittedBytes" | Committed bytes | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."#TotalReservedBytes" | Reserved bytes | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon."%TimeInGC" | Time in GC | Percent (%) | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.ContentionRate | Contention rate | Per second | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.CurrentQueueLength | Queue length | Count | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.Gen0HeapSize | Gen 0 Heap size | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.Gen1HeapSize | Gen 1 Heap size | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.perfmon.Gen2HeapSize | Gen 2 Heap size | Byte | autoavgcountmaxminsum |
| builtin:tech.dotnet.threadpool.ioCompletionThreads | .NET managed thread pool active io completion threads  Активные потоки завершения ввода-вывода в управляемом пуле потоков .NET | Count | autoavgmaxmin |
| builtin:tech.dotnet.threadpool.queuedWorkItems | .NET managed thread pool queued work items  Рабочие элементы в очереди управляемого пула потоков .NET | Count | autoavgmaxmin |
| builtin:tech.dotnet.threadpool.workerThreads | .NET managed thread pool active worker threads  Активные рабочие потоки в управляемом пуле потоков .NET | Count | autoavgmaxmin |

### Apache Hadoop

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.Hadoop.hdfs.BlocksTotal | Количество блоков | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CacheCapacity | Ёмкость кэша | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CacheUsed | Использование кэша | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CapacityRemaining | Оставшаяся ёмкость | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CapacityTotal | Общая ёмкость | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CapacityUsed | Используемая ёмкость | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CapacityUsedNonDFS | Ёмкость, используемая не DFS | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.CorruptBlocks | Повреждённые блоки | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.EstimatedCapacityLostTotal | Оценочные общие потери ёмкости | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesAppended | Файлы с дозаписью | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesCreated | Созданные файлы | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesDeleted | Удалённые файлы | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesRenamed | Переименованные файлы | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.FilesTotal | Количество файлов | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumDeadDataNodes | Недоступные DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumDecomDeadDataNodes | Недоступные выводимые из эксплуатации DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumDecomLiveDataNodes | Активные выводимые из эксплуатации DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumDecommissioningDataNodes | Количество выводимых из эксплуатации DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumLiveDataNodes | Активные DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumStaleDataNodes | Количество устаревших DataNodes | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.NumberOfMissingBlocks | Количество отсутствующих блоков | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.PendingDeletionBlocks | Блоки, ожидающие удаления | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.PendingReplicationBlocks | Блоки, ожидающие репликации | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.ScheduledReplicationBlocks | Блоки с запланированной репликацией | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.TotalLoad | Общая нагрузка | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.UnderReplicatedBlocks | Блоки с недостаточной репликацией | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.hdfs.VolumeFailuresTotal | Общее число сбоев томов | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AllocatedContainers | Выделенные контейнеры | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AllocatedMB | Выделенная память | MB | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AllocatedVCores | Выделенные ресурсы ЦП в виртуальных ядрах | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsCompleted | Завершённые приложения | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsFailed | Приложения с ошибкой | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsKilled | Остановленные приложения | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsPending | Приложения в очереди | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsRunning | Запущенные приложения | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AppsSubmitted | Отправленные приложения | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AvailableMB | Доступная память | MB | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.AvailableVCores | Доступные ресурсы ЦП в виртуальных ядрах | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumActiveNMs | Активные NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumDecommissionedNMs | Выведенные из эксплуатации NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumLostNMs | Потерянные NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumRebootedNMs | Перезагруженные NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.NumUnhealthyNMs | Неработоспособные NodeManagers | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.PendingMB | Запросы памяти в очереди | MB | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.PendingVCores | Запросы ресурсов ЦП в виртуальных ядрах в очереди | Count | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.ReservedMB | Зарезервированная память | MB | autoavgcountmaxminsum |
| builtin:tech.Hadoop.yarn.ReservedVCores | Запросы зарезервированных ресурсов ЦП в виртуальных ядрах | Count | autoavgcountmaxminsum |

### Apache Tomcat

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.tomcat.connectionPool.maxActive | Максимум активных | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.maxActiveGlobal | Максимум активных (глобально) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.maxTotal | Максимум всего | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.maxTotalGlobal | Максимум всего (глобально) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numActive | Количество активных | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numActiveGlobal | Количество активных (глобально) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numIdle | Количество простаивающих | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numIdleGlobal | Количество простаивающих (глобально) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numWaiters | Количество ожидающих | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.numWaitersGlobal | Количество ожидающих (глобально) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.waitCount | Количество ожиданий | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.connectionPool.waitCountGlobal | Количество ожиданий (глобально) | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.bytesReceivedPerSecond | Tomcat: принятые байты / с | Byte/second | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.bytesSentPerSecond | Tomcat: отправленные байты / с | Byte/second | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.currentThreadsBusy | Tomcat: занятые потоки | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.currentThreadsIdle | Tomcat: простаивающие потоки | Count | autoavgcountmaxminsum |
| builtin:tech.tomcat.tomcat.requestCountPerSecond | Tomcat: количество запросов / с | Per second | autoavgcountmaxminsum |

### Couchbase

| Ключ метрики | Название и описание | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.couchbase.cluster.basicStats.diskFetches | cluster basicStats diskFetches | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.count.membase | cluster count membase | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.count.memcached | cluster count memcached | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.cmd\_get | cluster samples cmd\_get | В секунду | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.cmd\_set | cluster samples cmd\_set | В секунду | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.curr\_items | cluster samples curr\_items | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ep\_cache\_miss\_rate | cluster samples ep\_cache\_miss\_rate | Процент (%) | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ep\_num\_value\_ejects | cluster samples ep\_num\_value\_ejects | В минуту | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ep\_oom\_errors | cluster samples ep\_oom\_errors | В секунду | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ep\_tmp\_oom\_errors | cluster samples ep\_tmp\_oom\_errors | В секунду | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.ops | cluster samples ops | В секунду | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.samples.swap\_used | cluster samples swap\_used | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.status.healthy | cluster status healthy | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.status.unhealthy | cluster status unhealthy | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.status.warmup | cluster status warmup | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.free | cluster storageTotals hdd free | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.quotaTotal | cluster storageTotals hdd quotaTotal | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.total | cluster storageTotals hdd total | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.used | cluster storageTotals hdd used | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.hdd.usedByData | cluster storageTotals hdd usedByData | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.percentageUsage | cluster storageTotals ram percentageUsage | Процент (%) | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.quotaTotal | cluster storageTotals ram quotaTotal | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.quotaTotalPerNode | cluster storageTotals ram quotaTotalPerNode | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.quotaUsed | cluster storageTotals ram quotaUsed | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.quotaUsedPerNode | cluster storageTotals ram quotaUsedPerNode | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.total | cluster storageTotals ram total | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.used | cluster storageTotals ram used | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.cluster.storageTotals.ram.usedByData | cluster storageTotals ram usedByData | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.basicStats.diskFetches | liveview basicStats diskFetches | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.basicStats.diskUsed | liveview basicStats diskUsed | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.basicStats.memUsed | liveview basicStats memUsed | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.cmd\_get | liveview samples cmd\_get | В секунду | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.cmd\_set | liveview samples cmd\_set | В секунду | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.couch\_docs\_data\_size | liveview samples couch\_docs\_data\_size | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.couch\_total\_disk\_size | liveview samples couch\_total\_disk\_size | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.disk\_write\_queue | liveview samples disk\_write\_queue | Количество | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.ep\_cache\_miss\_rate | liveview samples ep\_cache\_miss\_rate | В секунду | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.ep\_mem\_high\_wat | liveview samples ep\_mem\_high\_wat | Байт | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.ep\_num\_value\_ejects | liveview samples ep\_num\_value\_ejects | В минуту | autoavgcountmaxminsum |
| builtin:tech.couchbase.liveview.samples.ops | liveview samples ops | В секунду | autoavgcountmaxminsum |

### Custom device

| Ключ метрики | Название и описание | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.customDevice.count | Количество Custom Device | Количество | autovalue |

### Elastic search

| Ключ метрики | Название и описание | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.elasticsearch.local.indices.docs.count | Количество документов | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.docs.deleted | Удалённые документы | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.fielddata.evictions | Вытеснения данных полей | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.fielddata.memory\_size\_in\_bytes | Размер данных полей | Байт | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.query\_cache.cache\_count | Количество записей в кэше запросов | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.query\_cache.cache\_size | Размер кэша запросов | Байт | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.query\_cache.evictions | Вытеснения из кэша запросов | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.segments.count | Количество сегментов | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.shards.replication | Шарды-реплики | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.indices.count | Количество индексов | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.active\_primary\_shards | Активные первичные шарды | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.active\_shards | Активные шарды | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.delayed\_unassigned\_shards | Задержанные неназначенные шарды | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.initializing\_shards | Инициализируемые шарды | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.number\_of\_data\_nodes | Количество узлов данных | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.number\_of\_nodes | Количество узлов | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.relocating\_shards | Перемещаемые шарды | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.status-green | Статус green | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.status-red | Статус red | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.status-unknown | Статус unknown | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.status-yellow | Статус yellow | Количество | autoavgcountmaxminsum |
| builtin:tech.elasticsearch.local.unassigned\_shards | Неназначенные шарды | Количество | autoavgcountmaxminsum |

### Generic

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:tech.generic.cpu.groupSuspensionTime | Суммарное процессорное время группы процессов во время приостановок GC  Метрика предоставляет статистику использования CPU для групп процессов технологий со сборкой мусора. Значение метрики, это сумма процессорного времени, затраченного во время приостановок сборщика мусора для каждого процесса (включая его рабочие потоки) в группе процессов. Имеет измерение "Process Group". | Microsecond | autovalue |
| builtin:tech.generic.cpu.groupTotalTime | Суммарное процессорное время группы процессов  Метрика предоставляет суммарное процессорное время, используемое группой процессов. Значение метрики, это сумма процессорного времени каждого процесса (включая его рабочие потоки) в группе процессов. Результат выражается в микросекундах. Помогает определить наиболее CPU-интенсивные технологии в отслеживаемой среде. Имеет измерение "Process Group". | Microsecond | autovalue |
| builtin:tech.generic.cpu.suspensionTime | Суммарное процессорное время процесса во время приостановок GC  Метрика предоставляет статистику использования CPU для процессов со сборкой мусора. Значение метрики, это сумма процессорного времени, затраченного во время приостановок сборщика мусора для всех рабочих потоков процесса. Имеет измерение "Process" (dt.entity.process\_group\_instance). | Microsecond | autovalue |
| builtin:tech.generic.cpu.totalTime | Суммарное процессорное время процесса  Метрика предоставляет процессорное время, используемое процессом. Значение метрики, это сумма процессорного времени каждого рабочего потока процесса. Результат выражается в микросекундах. Имеет измерение "Process" (dt.entity.process\_group\_instance). | Microsecond | autovalue |
| builtin:tech.generic.cpu.usage | Использование CPU процессом  Метрика представляет процент использования CPU процессом. Значение метрики, это сумма процессорного времени каждого рабочего потока, делённая на общее доступное процессорное время. Результат выражается в процентах. Значение 100% означает, что процесс использует все доступные ресурсы CPU хоста. | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.gcpu.time | Время общего CPU z/OS  Время, затраченное на универсальном центральном процессоре (GCP) после запуска процесса в минуту | Second | autoavgcountmaxminsum |
| builtin:tech.generic.gcpu.usage | Использование общего CPU z/OS  Процент использования универсального центрального процессора (GCP) | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.handles.fileDescriptorsPercentUsed | Использование файловых дескрипторов процесса на PID  Метрика предоставляет статистику использования файловых дескрипторов. Поддерживается на Linux. Значение метрики, это наибольший процент использования текущего лимита файловых дескрипторов среди рабочих потоков процесса. Отправляется раз в минуту с гранулярностью 10 секунд (шесть выборок агрегируются каждую минуту). Предоставляет два измерения: "Process" (`dt.entity.process_group_instance`) и измерение pid, соответствующее PID с наибольшим процентом использования доступных дескрипторов. | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.handles.fileDescriptorsPercentUsed.new |  |  | autoavgmaxmin |
| builtin:tech.generic.handles.fileDescriptorsMax | Максимум файловых дескрипторов процесса  Метрика предоставляет статистику ограничений ресурса файловых дескрипторов. Поддерживается на Linux. Значение метрики, это суммарный лимит файловых дескрипторов, которые могут открыть все рабочие потоки процесса. Отправляется раз в минуту с гранулярностью 10 секунд (шесть выборок агрегируются каждую минуту). | Count | autoavgmaxmin |
| builtin:tech.generic.handles.fileDescriptorsUsed | Использованные файловые дескрипторы процесса  Метрика предоставляет статистику использования файловых дескрипторов. Поддерживается на Linux. Значение метрики, это суммарное количество файловых дескрипторов, открытых всеми рабочими потоками процесса. Позволяет обнаружить процессы, способные привести систему к достижению лимита открытых файловых дескрипторов. | Count | autoavgmaxmin |
| builtin:tech.generic.io.bytesRead | Байты чтения I/O процесса  Метрика предоставляет статистику операций чтения I/O процесса. Значение метрики, это сумма байт, прочитанных из уровня хранилища всеми рабочими потоками процесса в секунду. Высокие значения помогают выявить узкие места, снижающие производительность процесса из-за низкой скорости чтения устройства хранения. | Byte/second | autoavgmaxmin |
| builtin:tech.generic.io.bytesTotal | Суммарные байты I/O процесса  Метрика предоставляет статистику операций I/O процесса. Значение метрики, это сумма байт, прочитанных и записанных всеми рабочими потоками процесса в секунду. | Byte/second | autovalue |
| builtin:tech.generic.io.bytesWritten | Байты записи I/O процесса  Метрика предоставляет статистику операций записи I/O процесса. Значение метрики, это сумма байт, записанных на уровень хранилища всеми рабочими потоками процесса в секунду. Высокие значения помогают выявить узкие места, снижающие производительность процесса из-за низкой скорости записи устройства хранения. | Byte/second | autoavgmaxmin |
| builtin:tech.generic.io.reqBytesRead | Запрошенные байты чтения I/O процесса  Метрика предоставляет статистику операций чтения I/O, запрашиваемых процессом. Поддерживается только на Linux и AIX. Значение метрики, это сумма байт, запрошенных для чтения из хранилища рабочими процессами в секунду. Включает дополнительные операции чтения, например, терминальный I/O. Не отражает фактические операции дискового I/O, так как часть операции чтения могла быть выполнена из кэша страниц. | Byte/second | autoavgmaxmin |
| builtin:tech.generic.io.reqBytesWrite | Запрошенные байты записи I/O процесса  Метрика предоставляет статистику операций записи I/O, запрашиваемых процессом. Поддерживается на Linux и AIX. Значение метрики, это сумма байт, запрошенных для записи в хранилище процессами PGI в секунду. Включает дополнительные операции записи, например, терминальный I/O. Не отражает фактические операции дискового I/O, так как часть операции записи могла быть выполнена из кэша страниц. | Byte/second | autoavgmaxmin |
| builtin:tech.generic.mem.usage | Использование памяти процессом  Метрика представляет процент памяти, используемой процессом. Помогает выявить процессы с высоким потреблением памяти и утечки памяти. Значение метрики, это сумма памяти, используемой каждым рабочим потоком процесса, делённая на общий объём доступной памяти хоста. | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.mem.usage.new | Использование памяти процессом  Метрика представляет процент памяти, используемой процессом. Помогает выявить процессы с высоким потреблением памяти и утечки памяти. Значение метрики, это сумма памяти, используемой каждым рабочим потоком процесса, делённая на общий объём доступной памяти хоста. | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.mem.exhaustedMem | Счётчик событий исчерпания памяти процесса  Метрика представляет счётчик событий "Memory resource exhausted" для процесса. Значение метрики, это количество событий, сгенерированных всеми рабочими потоками процесса за минуту. JVM генерирует события исчерпания памяти при нехватке памяти. Метрика помогает выявить Java-процессы с избыточным потреблением памяти. | Count | autovalue |
| builtin:tech.generic.mem.pageFaults | Счётчик страничных ошибок процесса  Метрика представляет частоту страничных ошибок процесса. Значение метрики, это сумма страничных ошибок в единицу времени для каждого рабочего потока процесса. Страничная ошибка возникает, когда процесс обращается к блоку памяти, не хранящемуся в ОЗУ, и этот блок нужно найти в виртуальной памяти и загрузить из хранилища. Чем меньше значение, тем лучше. Большое количество страничных ошибок может свидетельствовать о снижении производительности из-за недостаточного объёма памяти. | Per second | autoavgmaxmin |
| builtin:tech.generic.mem.workingSetSize | Память процесса  Метрика представляет объём памяти, используемой процессом. Помогает выявить процессы с высоким потреблением памяти и утечки памяти. Значение метрики, это сумма используемой памяти каждого рабочего потока процесса (включая разделяемую память). | Byte | autoavgmaxmin |
| builtin:tech.generic.network.packets.baseReRx | Базовые полученные повторные передачи  Количество базовых повторно переданных пакетов, полученных в секунду на хосте | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.baseReRxAggr | Базовые полученные повторные передачи  Количество базовых повторно переданных пакетов, полученных в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.baseReTx | Базовые отправленные повторные передачи  Количество базовых повторно переданных пакетов, отправленных в секунду на хосте | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.baseReTxAggr | Базовые отправленные повторные передачи  Количество базовых повторно переданных пакетов, отправленных в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.reRx | Полученные повторно переданные пакеты  Количество повторно переданных пакетов, полученных в секунду на хосте | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.reRxAggr | Полученные повторно переданные пакеты  Количество повторно переданных пакетов, полученных в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.reTx | Отправленные повторно переданные пакеты  Количество базовых повторно переданных пакетов, отправленных в секунду на хосте | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.reTxAggr | Повторно переданные пакеты  Количество повторно переданных пакетов, отправленных в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.retransmission | Повторные передачи пакетов  Процент повторных передач пакетов | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.network.packets.retransmissionIn | Входящие повторные передачи пакетов  Процент входящих повторных передач пакетов | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.network.packets.retransmissionOut | Исходящие повторные передачи пакетов  Процент исходящих повторных передач пакетов | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.network.packets.rx | Полученные пакеты  Количество пакетов, полученных в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.packets.tx | Отправленные пакеты  Количество пакетов, отправленных в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.connectivity | TCP-связность  Процент успешно установленных TCP-сессий | Percent (%) | autoavgmaxmin |
| builtin:tech.generic.network.sessions.new | Полученные новые сессии  Количество новых входящих TCP-сессий в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.newAggr | Полученные новые сессии  Количество новых полученных сессий в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.newLocal | Полученные новые сессии  Количество новых полученных сессий в секунду на localhost | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.reset | Полученные сбросы сессий  Количество входящих TCP-сессий с ошибкой сброса в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.resetAggr | Полученные сбросы сессий  Количество полученных сбросов сессий в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.resetLocal | Полученные сбросы сессий  Количество полученных сбросов сессий в секунду на localhost | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.timeout | Полученные тайм-ауты сессий  Количество входящих TCP-сессий с ошибкой тайм-аута в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.timeoutAggr | Полученные тайм-ауты сессий  Количество полученных тайм-аутов сессий в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.sessions.timeoutLocal | Полученные тайм-ауты сессий  Количество полученных тайм-аутов сессий в секунду на localhost | Per second | autoavgmaxmin |
| builtin:tech.generic.network.traffic.traffic | Трафик  Суммарный входящий и исходящий сетевой трафик | bit/s | autovalue |
| builtin:tech.generic.network.traffic.trafficIn | Входящий трафик  Входящий сетевой трафик на PGI | bit/s | autoavgmaxmin |
| builtin:tech.generic.network.traffic.trafficOut | Исходящий трафик  Исходящий сетевой трафик с PGI | bit/s | autoavgmaxmin |
| builtin:tech.generic.network.bytesRx | Полученные байты  Количество байт, полученных в секунду | Byte/second | autoavgmaxmin |
| builtin:tech.generic.network.bytesTx | Отправленные байты  Количество байт, отправленных в секунду | Byte/second | autoavgmaxmin |
| builtin:tech.generic.network.latency | Время подтверждения приёма (RTT)  Средняя задержка между исходящими TCP-данными и ACK | Millisecond | autoavgmaxmin |
| builtin:tech.generic.network.load | Запросы  Количество запросов в секунду | Per second | autoavgmaxmin |
| builtin:tech.generic.network.responsiveness | Отзывчивость сервера  Отзывчивость сервера в микросекундах | Microsecond | autoavgcountmaxmedianminpercentilesum |
| builtin:tech.generic.network.roundTrip | Время двустороннего обмена (RTT)  Среднее RTT рукопожатия TCP-сессии | Millisecond | autoavgmaxmin |
| builtin:tech.generic.network.throughput | Пропускная способность  Используемая полоса пропускания сети | Byte/second | autoavgmaxmin |
| builtin:tech.generic.count | Количество процессов в группе процессов  Метрика предоставляет количество процессов в группе процессов. Показывает, сколько экземпляров технологии запущено в отслеживаемой среде. Имеет измерение "Process Group". | Count | autovalue |
| builtin:tech.generic.processCount | Рабочие процессы  Метрика представляет количество рабочих процессов. Слишком малое количество рабочих процессов может привести к деградации производительности, слишком большое, к нерациональному расходованию доступных ресурсов. Конфигурация рабочих процессов должна соответствовать средней нагрузке и обеспечивать масштабирование при росте спроса. | Count | autoavgmaxmin |
| builtin:tech.generic.threadsExhausted | Счётчик событий исчерпания потоков процесса  Метрика представляет счётчик событий "Thread resource exhausted" для процесса. Значение метрики, это количество событий, сгенерированных всеми рабочими потоками процесса за минуту. JVM генерирует события исчерпания потоков, когда не может создать новый поток. Метрика помогает выявить Java-процессы с избыточным потреблением памяти. | Count | autovalue |
| builtin:tech.generic.ziip | Время zIIP z/OS  Время, затраченное на системном интегрированном информационном процессоре z (zIIP) после запуска процесса в минуту | Second | autoavgcountmaxminsum |
| builtin:tech.generic.ziipEligible | Допустимое время zIIP z/OS  Допустимое для zIIP время, затраченное на универсальном центральном процессоре (GCP) после запуска процесса в минуту | Second | autoavgcountmaxminsum |

### Go

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.go.http.badGateways | Go: 502 responses  Количество ответов, указывающих на недопустимые ответы сервиса, которые производит приложение. | Count | autovalue |
| builtin:tech.go.http.latency | Go: Response latency  Среднее время ответа от приложения до клиентов. | Millisecond | autoavgmaxmin |
| builtin:tech.go.http.responses5xx | Go: 5xx responses  Количество ответов, указывающих на систематически падающие приложения или проблемы с ответами от приложений. | Count | autovalue |
| builtin:tech.go.http.totalRequests | Go: Total requests  Количество всех запросов, отражающее общий поток трафика. | Count | autovalue |
| builtin:tech.go.memory.heap.idle | Go: Heap idle size  Объём памяти, не выделенной под heap или стек. Незанятая память может быть возвращена операционной системе либо удержана Go runtime для последующего переназначения под heap или стек. | Byte | autoavgmaxmin |
| builtin:tech.go.memory.heap.live | Go: Heap live size  Объём памяти, считающейся живой сборщиком мусора Go. Метрика накапливает память, удержанную последним запуском сборщика мусора, а также выделенную с тех пор. | Byte | autoavgmaxmin |
| builtin:tech.go.memory.heap.objCount | Go: Heap allocated Go objects count  Количество объектов Go, размещённых на Go heap. | Count | autoavgmaxmin |
| builtin:tech.go.memory.pool.committed | Go: Committed memory  Объём памяти, зафиксированной в heap Go runtime. | Byte | autoavgmaxmin |
| builtin:tech.go.memory.pool.used | Go: Used memory  Объём памяти, используемой heap Go runtime. | Byte | autoavgmaxmin |
| builtin:tech.go.memory.gcCount | Go: Garbage collector invocation count  Количество запусков сборщика мусора Go. | Count | autovalue |
| builtin:tech.go.native.cgoCalls | Go: Go to C language (cgo) call count  Количество вызовов из Go в язык C (cgo). | Count | autovalue |
| builtin:tech.go.native.sysCalls | Go: Go runtime system call count  Количество системных вызовов, выполненных Go runtime. В это число не входят системные вызовы, совершённые пользовательским кодом. | Count | autovalue |
| builtin:tech.go.scheduling.g.avgNumOfActiveRoutines | Go: Average number of active Goroutines  Среднее количество активных Goroutine. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.g.avgNumOfInactiveRoutines | Go: Average number of inactive Goroutines  Среднее количество неактивных Goroutine. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.g.runningCount | Go: Application Goroutine count  Количество Goroutine, созданных пользовательским приложением. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.g.systemCount | Go: System Goroutine count  Количество Goroutine, созданных Go runtime. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.m.count | Go: Worker thread count  Количество потоков операционной системы, созданных для выполнения Goroutine. Go не завершает рабочие потоки, а удерживает их в припаркованном состоянии для последующего повторного использования. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.m.idlingCount | Go: Parked worker thread count  Количество рабочих потоков, припаркованных Go runtime. Припаркованный рабочий поток не потребляет циклы CPU до тех пор, пока Go runtime не распаркует его. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.m.spinningCount | Go: Out-of-work worker thread count  Количество рабочих потоков, в контексте планировщика которых больше нет Goroutine для выполнения. В такой ситуации рабочий поток пытается похитить Goroutine из другого контекста планировщика или глобальной очереди запуска. Если похищение не удаётся, рабочий поток через некоторое время паркует себя. Этот же механизм применяется при высокой нагрузке: когда существует простаивающий контекст планировщика, Go runtime распарковывает припаркованный рабочий поток и связывает его с этим контекстом. Распаркованный рабочий поток переходит в состояние «без работы» и начинает похищение Goroutine. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.p.idleCount | Go: Idle scheduling context count  Количество контекстов планировщика, в которых больше нет Goroutine для выполнения и получение Goroutine из глобальной очереди запуска или других контекстов планировщика завершилось неудачей. | Count | autoavgmaxmin |
| builtin:tech.go.scheduling.globalQSize | Go: Global Goroutine run queue size  Количество Goroutine в глобальной очереди запуска. Goroutine помещаются в глобальную очередь запуска, если рабочий поток, использованный для выполнения блокирующего системного вызова, не может получить контекст планировщика. Контексты планировщика периодически забирают Goroutine из глобальной очереди запуска. | Count | autoavgmaxmin |

### JVM

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:tech.jvm.classes.loaded` | JVM loaded classes Количество классов, загруженных в данный момент в виртуальную машину Java, https://dt-url.net/l2c34jw | Count | autoavgmaxmin |
| `builtin:tech.jvm.classes.total` | JVM total number of loaded classes Общее количество классов, загруженных с момента запуска виртуальной машины Java, https://dt-url.net/d0y347x | Count | autoavgmaxmin |
| `builtin:tech.jvm.classes.unloaded` | JVM unloaded classes Общее количество классов, выгруженных с момента запуска виртуальной машины Java, https://dt-url.net/d7g34bi | Count | autoavgmaxmin |
| `builtin:tech.jvm.memory.gc.activationCount` | Garbage collection total activation count Общее количество сборок мусора, выполненных во всех пулах, https://dt-url.net/oz834vd | Count | autovalue |
| `builtin:tech.jvm.memory.gc.collectionTime` | Garbage collection total collection time Приблизительное накопленное время сборки мусора в миллисекундах для всех пулов, https://dt-url.net/oz834vd | Millisecond | autovalue |
| `builtin:tech.jvm.memory.gc.suspensionTime` | Garbage collection suspension time Время в миллисекундах между началом и окончанием пауз GC, https://dt-url.net/zj434js | Percent (%) | autoavgmaxmin |
| `builtin:tech.jvm.memory.pool.collectionCount` | Garbage collection count Общее количество сборок мусора, выполненных в данном пуле, https://dt-url.net/z9034yg | Count | autovalue |
| `builtin:tech.jvm.memory.pool.collectionTime` | Garbage collection time Приблизительное накопленное время сборки мусора в миллисекундах в данном пуле, https://dt-url.net/z9034yg | Millisecond | autovalue |
| `builtin:tech.jvm.memory.pool.committed` | JVM heap memory pool committed bytes Объём памяти (в байтах), гарантированно доступный для использования виртуальной машиной Java, https://dt-url.net/1j034o0 | Byte | autoavgmaxmin |
| `builtin:tech.jvm.memory.pool.max` | JVM heap memory max bytes Максимальный объём памяти (в байтах), доступный для управления памятью, https://dt-url.net/1j034o0 | Byte | autoavgmaxmin |
| `builtin:tech.jvm.memory.pool.used` | JVM heap memory pool used bytes Объём памяти, используемый пулом памяти в данный момент (в байтах), https://dt-url.net/1j034o0 | Byte | autoavgmaxmin |
| `builtin:tech.jvm.memory.runtime.free` | JVM runtime free memory Приблизительный суммарный объём памяти (в байтах), доступной для выделения будущим объектам, https://dt-url.net/2mm34yx | Byte | autoavgmaxmin |
| `builtin:tech.jvm.memory.runtime.max` | JVM runtime max memory Максимальный объём памяти (в байтах), который виртуальная машина будет пытаться использовать, https://dt-url.net/lzq34mm | Byte | autoavgmaxmin |
| `builtin:tech.jvm.memory.runtime.total` | JVM runtime total memory Суммарный объём памяти (в байтах), доступной для текущих и будущих объектов, https://dt-url.net/otu34eo | Byte | autoavgmaxmin |
| `builtin:tech.jvm.memory.memAllocationBytes` | Process memory allocation bytes Байты, выделенные памятью процесса | Byte | autovalue |
| `builtin:tech.jvm.memory.memAllocationCount` | Process memory allocation objects count Количество объектов, выделенных памятью процесса | Count | autovalue |
| `builtin:tech.jvm.memory.memSurvivorsBytes` | Process memory survived objects bytes Байты выживших объектов памяти процесса | Byte | autovalue |
| `builtin:tech.jvm.memory.memSurvivorsCount` | Process memory survived objects count Количество выживших объектов памяти процесса | Count | autovalue |
| `builtin:tech.jvm.spark.aliveWorkers` | Alive workers Активные воркеры | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.aliveWorkers.gauge` | Alive workers Активные воркеры | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.apps` | Master apps Приложения мастера | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.apps.gauge` | Master apps Приложения мастера | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.Count` | Processing time - count Время обработки, количество | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.Count.timer` | Processing time - count Время обработки, количество | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.Mean` | Processing time - mean Время обработки, среднее | Millisecond | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.Mean.timer` | Processing time - mean Время обработки, среднее | Millisecond | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.OneMinuteRate` | Processing time - one minute rate Время обработки, частота за минуту | Per second | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.OneMinuteRate.timer` | Processing time - one minute rate Время обработки, частота за минуту | Per second | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.activeJobs` | Active jobs Активные задания | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.activeJobs.gauge` | Active jobs Активные задания | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.allJobs` | Total jobs Всего заданий | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.allJobs.gauge` | Total jobs Всего заданий | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.failedStages` | Failed stages Этапы с ошибками | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.failedStages.gauge` | Failed stages Этапы с ошибками | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.runningStages` | Running stages Выполняющиеся этапы | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.runningStages.gauge` | Running stages Выполняющиеся этапы | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.waitingStages` | Waiting stages Ожидающие этапы | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.driver.waitingStages.gauge` | Waiting stages Ожидающие этапы | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.waitingApps` | Waiting apps Ожидающие приложения | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.waitingApps.gauge` | Waiting apps Ожидающие приложения | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.workers` | Master workers Воркеры мастера | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.spark.workers.gauge` | Master workers Воркеры мастера | Count | autoavgcountmaxminsum |
| `builtin:tech.jvm.threads.avgActiveThreadCount` | JVM average number of active threads Среднее количество активных потоков JVM | Count | autoavgmaxmin |
| `builtin:tech.jvm.threads.avgInactiveThreadCount` | JVM average number of inactive threads Среднее количество неактивных потоков JVM | Count | autoavgmaxmin |
| `builtin:tech.jvm.threads.count` | JVM thread count Текущее количество живых потоков, включая демонические и не-демонические, https://dt-url.net/s02346y | Count | autoavgmaxmin |
| `builtin:tech.jvm.threads.totalCpuTime` | JVM total CPU time Суммарное процессорное время JVM | Millisecond | autovalue |

### Kafka

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:tech.kafka.pg.kafka.controller.ControllerStats.LeaderElectionRateAndTimeMs.OneMinuteRate` | Kafka broker - Leader election rate Kafka broker, частота выборов лидера | Millisecond | autoavgcountmaxminsum |
| `builtin:tech.kafka.pg.kafka.controller.ControllerStats.UncleanLeaderElectionsPerSec.OneMinuteRate` | Kafka broker - Unclean election rate Kafka broker, частота некорректных выборов | Per second | autoavgcountmaxminsum |
| `builtin:tech.kafka.pg.kafka.controller.KafkaController.ActiveControllerCount.Value` | Kafka controller - Active cluster controllers Kafka controller, активные контроллеры кластера | Count | autoavgcountmaxminsum |
| `builtin:tech.kafka.pg.kafka.controller.KafkaController.OfflinePartitionsCount.Value` | Kafka controller - Offline partitions Kafka controller, разделы без лидера | Count | autoavgcountmaxminsum |
| `builtin:tech.kafka.pg.kafka.server.ReplicaManager.PartitionCount.Value` | Kafka broker - Partitions Kafka broker, разделы | Count | autoavgcountmaxminsum |
| `builtin:tech.kafka.pg.kafka.server.ReplicaManager.UnderReplicatedPartitions.Value` | Kafka broker - Under replicated partitions Kafka broker, разделы с недостаточной репликацией | Count | autoavgcountmaxminsum |

### Nettracer

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:tech.nettracer.bytes_rx` | Bytes received Количество принятых байт | Byte | autoavgcountmaxminsum |
| `builtin:tech.nettracer.bytes_tx` | Bytes transmitted Количество переданных байт | Byte | autoavgcountmaxminsum |
| `builtin:tech.nettracer.pkts_retr` | Retransmitted packets Количество повторно переданных пакетов | Count | autovalue |
| `builtin:tech.nettracer.pkts_rx` | Packets received Количество принятых пакетов | Count | autovalue |
| `builtin:tech.nettracer.pkts_tx` | Packets transmitted Количество переданных пакетов | Count | autovalue |
| `builtin:tech.nettracer.retr_percentage` | Retransmission Процент повторно переданных пакетов | Percent (%) | autoavgmaxmin |
| `builtin:tech.nettracer.rtt` | Round trip time Время кругового обхода в миллисекундах. Агрегирует данные активных сессий | Millisecond | autoavgcountmaxminsum |
| `builtin:tech.nettracer.traffic` | Network traffic Суммарный входящий и исходящий сетевой трафик в битах в секунду | bit/s | autovalue |
| `builtin:tech.nettracer.traffic_rx` | Incoming traffic Входящий сетевой трафик в битах в секунду | bit/s | autovalue |
| `builtin:tech.nettracer.traffic_tx` | Outgoing traffic Исходящий сетевой трафик в битах в секунду | bit/s | autovalue |

### Nginx

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.nginx.cache.freeSpace | Свободное место в кэше Nginx Plus | MB | autoavgmaxmin |
| builtin:tech.nginx.cache.hitRatio | Коэффициент попаданий в кэш Nginx Plus | Percent (%) | autoavgmaxmin |
| builtin:tech.nginx.cache.hits | Попадания в кэш Nginx Plus | Per second | autoavgmaxmin |
| builtin:tech.nginx.cache.misses | Промахи кэша Nginx Plus | Per second | autoavgmaxmin |
| builtin:tech.nginx.cache.usedSpace | Используемое место в кэше Nginx Plus | MB | autoavgmaxmin |
| builtin:tech.nginx.serverZones.active | Активные серверные зоны Nginx Plus | Count | autoavgmaxmin |
| builtin:tech.nginx.serverZones.inactive | Неактивные серверные зоны Nginx Plus | Count | autoavgmaxmin |
| builtin:tech.nginx.serverZones.requests | Запросы серверной зоны Nginx Plus | Per second | autoavgmaxmin |
| builtin:tech.nginx.serverZones.trafficIn | Входящий трафик серверной зоны Nginx Plus | Byte/second | autoavgmaxmin |
| builtin:tech.nginx.serverZones.trafficOut | Исходящий трафик серверной зоны Nginx Plus | Byte/second | autoavgmaxmin |
| builtin:tech.nginx.upstream.healthy | Работоспособные upstream-серверы Nginx Plus | Count | autoavgmaxmin |
| builtin:tech.nginx.upstream.requests | Запросы к upstream Nginx Plus | Per second | autoavgmaxmin |
| builtin:tech.nginx.upstream.trafficIn | Входящий трафик upstream Nginx Plus | Byte/second | autoavgmaxmin |
| builtin:tech.nginx.upstream.trafficOut | Исходящий трафик upstream Nginx Plus | Byte/second | autoavgmaxmin |
| builtin:tech.nginx.upstream.unhealthy | Неработоспособные upstream-серверы Nginx Plus | Count | autoavgmaxmin |

### Node.js

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.nodejs.uvLoop.activeHandles | Node.js: активные дескрипторы  Среднее количество активных дескрипторов в цикле событий | Count | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.count | Node.js: частота тиков цикла событий  Среднее количество итераций цикла событий (за интервал 10 секунд) | Count | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.loopLatency | Node.js: задержка цикла событий  Средняя задержка ожидаемого завершения события | Nanosecond | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.processedLatency | Node.js: задержка обработки работы  Средняя задержка между постановкой рабочего элемента в очередь и вызовом callback | Nanosecond | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.totalTime | Node.js: длительность тика цикла событий  Средняя длительность одной итерации цикла событий (тика) | Nanosecond | autoavgmaxmin |
| builtin:tech.nodejs.uvLoop.utilization | Node.js: утилизация цикла событий  Утилизация цикла событий, это процент времени, в течение которого цикл событий был активен | Percent (%) | autoavgmaxmin |
| builtin:tech.nodejs.v8heap.gcHeapUsed | Node.js: использованная куча GC  Общий размер выделенной кучи V8, занятой данными приложения (снимок памяти после GC) | Byte | autoavgmaxmin |
| builtin:tech.nodejs.v8heap.rss | Node.js: размер резидентного набора процесса (RSS)  Объём пространства, занятого в основной памяти | Byte | autoavgmaxmin |
| builtin:tech.nodejs.v8heap.total | Node.js: общий размер кучи V8  Общий размер выделенной кучи V8 | Byte | autoavgmaxmin |
| builtin:tech.nodejs.v8heap.used | Node.js: используемая куча V8  Общий размер выделенной кучи V8, занятой данными приложения (периодический снимок памяти) | Byte | autoavgmaxmin |
| builtin:tech.nodejs.avgNumberOfActiveThreads | Node.js: количество активных потоков  Среднее количество активных рабочих потоков Node.js | Count | autoavgmaxmin |

### Oracle Database

| Metric key | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.oracleDb.cd.cpu.background | Использование CPU фоновыми процессами | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.cpu.foreground | Использование CPU активными процессами | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.cpu.idle | Простой CPU | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.cpu.other | CPU прочих процессов | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.io.bytesRead | Физически прочитанные байты | Байт | autovalue |
| builtin:tech.oracleDb.cd.io.bytesWritten | Физически записанные байты | Байт | autovalue |
| builtin:tech.oracleDb.cd.io.wait | Суммарное время ожидания | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.memory.pga.size.allocated | Выделено PGA | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateLimit | Агрегированный лимит PGA | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.pga.size.pgaAggregateTarget | Агрегированная цель PGA | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.pga.usedForWorkAreas | PGA, используемый для рабочих областей | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.sga.cacheBuffer.sharedPoolFree | Свободный shared pool | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoLogSpaceWaitTime | Время ожидания пространства redo log | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoSizeIncrease | Прирост размера redo | Количество | autovalue |
| builtin:tech.oracleDb.cd.memory.sga.redoBuffer.redoWriteTime | Время записи redo | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.memory.bufferCacheHit | Попадания в кэш буфера | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.memory.sortsInMemory | Сортировки в памяти | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.cd.queries.connMgmt | Время на управление соединениями | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.queries.other | Время на прочие операции | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.queries.plSqlExec | Затраченное время выполнения PL SQL | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.queries.sqlExec | Время выполнения SQL | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.queries.sqlParse | Время на разбор SQL | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.sessions.active | Активные сессии | Количество | autoavgmaxmin |
| builtin:tech.oracleDb.cd.sessions.all | Все сессии | Количество | autoavgmaxmin |
| builtin:tech.oracleDb.cd.sessions.userCalls | Количество вызовов пользователя | Количество | autovalue |
| builtin:tech.oracleDb.cd.slow.time.application | Время ожидания приложения | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.slow.time.cluster | Время ожидания кластера | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.slow.time.concurrency | Время ожидания конкурентного доступа | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.slow.time.cpu | Время CPU | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.slow.time.elapsed | Затраченное время | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.slow.time.userIo | Время ожидания пользовательского ввода-вывода | Микросекунда | autovalue |
| builtin:tech.oracleDb.cd.slow.bufferGets | Обращения к буферу | Количество | autovalue |
| builtin:tech.oracleDb.cd.slow.directWrites | Прямые записи | Количество | autovalue |
| builtin:tech.oracleDb.cd.slow.diskReads | Чтения с диска | Количество | autovalue |
| builtin:tech.oracleDb.cd.slow.executions | Выполнения | Количество | autovalue |
| builtin:tech.oracleDb.cd.slow.parseCalls | Вызовы разбора | Количество | autovalue |
| builtin:tech.oracleDb.cd.slow.rowsProcessed | Обработано строк | Количество | autovalue |
| builtin:tech.oracleDb.cd.tablespaces.totalSpace | Общее пространство | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.cd.tablespaces.usedSpace | Использованное пространство | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.cd.wait.count | Количество событий ожидания | Количество | autovalue |
| builtin:tech.oracleDb.cd.wait.time | Суммарное время ожидания | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.cpu.background | Использование CPU фоновыми процессами | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.cpu.foreground | Использование CPU активными процессами | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.cpu.idle | Простой CPU | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.cpu.other | CPU прочих процессов | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.io.bytesRead | Физически прочитанные байты | Байт | autovalue |
| builtin:tech.oracleDb.pgi.io.bytesWritten | Физически записанные байты | Байт | autovalue |
| builtin:tech.oracleDb.pgi.io.wait | Суммарное время ожидания | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.memory.pga.size.allocated | Выделено PGA | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.pga.size.pgaAggregateLimit | Агрегированный лимит PGA | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.pga.size.pgaAggregateTarget | Агрегированная цель PGA | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.pga.usedForWorkAreas | PGA, используемый для рабочих областей | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.sga.cacheBuffer.sharedPoolFree | Свободный shared pool | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.memory.sga.redoBuffer.redoLogSpaceWaitTime | Время ожидания пространства redo log | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.memory.sga.redoBuffer.redoSizeIncrease | Прирост размера redo | Количество | autovalue |
| builtin:tech.oracleDb.pgi.memory.sga.redoBuffer.redoWriteTime | Время записи redo | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.queries.connMgmt | Время на управление соединениями | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.queries.other | Время на прочие операции | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.queries.plSqlExec | Затраченное время выполнения PL SQL | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.queries.sqlExec | Время выполнения SQL | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.queries.sqlParse | Время на разбор SQL | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.sessions.active | Активные сессии | Количество | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.sessions.all | Все сессии | Количество | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.sessions.userCalls | Количество вызовов пользователя | Количество | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.application | Время ожидания приложения | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.cluster | Время ожидания кластера | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.concurrency | Время ожидания конкурентного доступа | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.cpu | Время CPU | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.elapsed | Затраченное время | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.slow.time.userIo | Время ожидания пользовательского ввода-вывода | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.slow.bufferGets | Обращения к буферу | Количество | autovalue |
| builtin:tech.oracleDb.pgi.slow.directWrites | Прямые записи | Количество | autovalue |
| builtin:tech.oracleDb.pgi.slow.diskReads | Чтения с диска | Количество | autovalue |
| builtin:tech.oracleDb.pgi.slow.executions | Выполнения | Количество | autovalue |
| builtin:tech.oracleDb.pgi.slow.parseCalls | Вызовы разбора | Количество | autovalue |
| builtin:tech.oracleDb.pgi.slow.rowsProcessed | Обработано строк | Количество | autovalue |
| builtin:tech.oracleDb.pgi.tablespaces.totalSpace | Общее пространство | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.tablespaces.usedSpace | Использованное пространство | Байт | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.wait.count | Количество событий ожидания | Количество | autovalue |
| builtin:tech.oracleDb.pgi.wait.time | Суммарное время ожидания | Микросекунда | autovalue |
| builtin:tech.oracleDb.pgi.bufferCacheHit | Попадания в кэш буфера | Процент (%) | autoavgmaxmin |
| builtin:tech.oracleDb.pgi.sortsInMemory | Сортировки в памяти | Процент (%) | autoavgmaxmin |

### PHP

| Ключ метрики | Название и описание | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.php.phpGc.collectedCount | Количество собранных объектов PHP GC | Количество | autoavgcountmaxminsum |
| builtin:tech.php.phpGc.durationMs | Длительность сборки мусора PHP GC | Миллисекунда | autoavgcountmaxminsum |
| builtin:tech.php.phpGc.effectiveness | Эффективность PHP GC | Процент (%) | autoavgcountmaxminsum |
| builtin:tech.php.phpOpcache.jit.bufferFree | Свободный буфер PHP OPCache JIT | Байт | autoavgmaxmin |
| builtin:tech.php.phpOpcache.jit.bufferSize | Размер буфера PHP OPCache JIT | Байт | autoavgmaxmin |
| builtin:tech.php.phpOpcache.memory.free | Свободная память PHP OPCache | Байт | autoavgmaxmin |
| builtin:tech.php.phpOpcache.memory.used | Используемая память PHP OPCache | Байт | autoavgmaxmin |
| builtin:tech.php.phpOpcache.memory.wasted | Потерянная память PHP OPCache | Байт | autoavgmaxmin |
| builtin:tech.php.phpOpcache.restarts.hash | Перезапуски PHP OPCache из-за нехватки ключей | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.restarts.manual | Ручные перезапуски PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.restarts.outOfMemory | Перезапуски PHP OPCache из-за нехватки памяти | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.blocklistMisses | Промахи по blocklist PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.cachedKeys | Количество кешированных ключей PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.cachedScripts | Количество кешированных скриптов PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.hits | Попадания в кеш PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.maxCachedCachedKeys | Максимальное количество ключей PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.statistics.misses | Промахи кеша PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.strings.bufferSize | Размер буфера интернированных строк PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.strings.numberOfStrings | Количество интернированных строк PHP OPCache | Количество | autoavgmaxmin |
| builtin:tech.php.phpOpcache.strings.usedMemory | Использование памяти для интернированных строк PHP OPCache | Байт | autoavgmaxmin |
| builtin:tech.php.threads.avgNumOfActiveThreads | Среднее количество активных потоков PHP | Количество | autoavgmaxmin |
| builtin:tech.php.threads.avgNumOfInactiveThreads | Среднее количество неактивных потоков PHP | Количество | autoavgmaxmin |

### Python

| Ключ метрики | Название и описание | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.python.gc.collected.gen0 | Собранные объекты Python GC из поколения 0 | Количество | autoavgmaxmin |
| builtin:tech.python.gc.collected.gen1 | Собранные объекты Python GC из поколения 1 | Количество | autoavgmaxmin |
| builtin:tech.python.gc.collected.gen2 | Собранные объекты Python GC из поколения 2 | Количество | autoavgmaxmin |
| builtin:tech.python.gc.collection.gen0 | Количество сборок мусора Python GC в поколении 0 | Количество | autoavgmaxmin |
| builtin:tech.python.gc.collection.gen1 | Количество сборок мусора Python GC в поколении 1 | Количество | autoavgmaxmin |
| builtin:tech.python.gc.collection.gen2 | Количество сборок мусора Python GC в поколении 2 | Количество | autoavgmaxmin |
| builtin:tech.python.gc.collectionTime.gen0 | Время сборки мусора Python GC в поколении 0 | Микросекунда | autoavgmaxmin |
| builtin:tech.python.gc.collectionTime.gen1 | Время сборки мусора Python GC в поколении 1 | Микросекунда | autoavgmaxmin |
| builtin:tech.python.gc.collectionTime.gen2 | Время сборки мусора Python GC в поколении 2 | Микросекунда | autoavgmaxmin |
| builtin:tech.python.gc.uncollectable.gen0 | Несобираемые объекты Python GC в поколении 0 | Количество | autoavgmaxmin |
| builtin:tech.python.gc.uncollectable.gen1 | Несобираемые объекты Python GC в поколении 1 | Количество | autoavgmaxmin |
| builtin:tech.python.gc.uncollectable.gen2 | Несобираемые объекты Python GC в поколении 2 | Количество | autoavgmaxmin |
| builtin:tech.python.heap.allocatedBlocks | Количество блоков памяти, выделенных Python | Количество | autoavgmaxmin |
| builtin:tech.python.activeThreads | Количество активных потоков Python | Количество | autoavgmaxmin |

### RabbitMQ

| Ключ метрики | Название и описание | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.rabbitmq.cluster\_channels | каналы кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_connections | подключения кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_consumers | потребители кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_exchanges | exchanges кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_ack | подтверждённые сообщения кластера | В секунду | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_deliver\_get | доставленные и полученные сообщения кластера | В секунду | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_publish | опубликованные сообщения кластера | В секунду | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_ready | готовые к обработке сообщения кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_redeliver | повторно доставленные сообщения кластера | В секунду | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_return\_unroutable | недоставляемые сообщения кластера | В секунду | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_messages\_unacknowledged | неподтверждённые сообщения кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_nodes\_failed | сбойные узлы кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_nodes\_ok | работающие узлы кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_crashed | аварийные очереди кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_down | недоступные очереди кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_flow | очереди кластера в режиме flow | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_idle | простаивающие очереди кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.cluster\_queues\_running | активные очереди кластера | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_ack | топ N: подтверждения | В секунду | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_consumers | топ N: потребители | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_deliver\_get | топ N: доставка/получение | В секунду | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_messages\_ready | топ N: готовые сообщения | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_messages\_unacknowledged | топ N: неподтверждённые сообщения | Количество | autoavgcountmaxminsum |
| builtin:tech.rabbitmq.topN\_queue\_publish | топ N: публикации | В секунду | autoavgcountmaxminsum |

### Ruby

| Ключ метрики | Название и описание | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.ruby.gc.collectionCount | Количество сборок мусора Ruby GC | Количество | autovalue |
| builtin:tech.ruby.gc.collectionTime | Время сборки мусора Ruby GC | Миллисекунда | autovalue |
| builtin:tech.ruby.heap.allocated | Размер выделенной кучи Ruby MRI | Байт | autoavgmaxmin |
| builtin:tech.ruby.heap.freeSlots | Свободные слоты кучи Ruby MRI | Количество | autoavgmaxmin |
| builtin:tech.ruby.heap.liveSlots | Активные слоты кучи Ruby MRI | Количество | autoavgmaxmin |
| builtin:tech.ruby.memoryPool.committed | Зафиксированная память Ruby JVM | Байт | autoavgmaxmin |
| builtin:tech.ruby.memoryPool.max | Максимальная память Ruby JVM | Байт | autoavgmaxmin |
| builtin:tech.ruby.memoryPool.used | Используемая память Ruby JVM | Байт | autoavgmaxmin |
| builtin:tech.ruby.managedThreads | Количество управляемых потоков Ruby | Количество | autoavgmaxmin |

### Varnish

| Ключ метрики | Название и описание | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.varnish.cache.hitRatio | Доля попаданий в кеш | Процент (%) | autoavgmaxmin |
| builtin:tech.varnish.cache.hitpasses | Попадания в кеш для passes | В секунду | autoavgmaxmin |
| builtin:tech.varnish.cache.hits | Попадания в кеш | В секунду | autoavgmaxmin |
| builtin:tech.varnish.cache.misses | Промахи кеша | В секунду | autoavgmaxmin |
| builtin:tech.varnish.cache.passes | Пропуски кеша | В секунду | autoavgmaxmin |
| builtin:tech.varnish.connections.backend | Подключения к бэкенду | В секунду | autoavgmaxmin |
| builtin:tech.varnish.connections.failed | Неудачные подключения к бэкенду | В секунду | autoavgmaxmin |
| builtin:tech.varnish.connections.reused | Повторно используемые подключения к бэкенду | В секунду | autoavgmaxmin |
| builtin:tech.varnish.sessions.accepted | Принятые сессии | В секунду | autoavgmaxmin |
| builtin:tech.varnish.sessions.dropped | Отброшенные сессии | В секунду | autoavgmaxmin |
| builtin:tech.varnish.sessions.queued | Сессии в очереди | В секунду | autoavgmaxmin |
| builtin:tech.varnish.threads.failed | Сбойные потоки | В секунду | autoavgmaxmin |
| builtin:tech.varnish.threads.max | Максимальное количество потоков | Количество | autoavgmaxmin |
| builtin:tech.varnish.threads.min | Минимальное количество потоков | Количество | autoavgmaxmin |
| builtin:tech.varnish.threads.total | Общее количество потоков | Количество | autoavgmaxmin |
| builtin:tech.varnish.requests | Запросы | В секунду | autoavgmaxmin |
| builtin:tech.varnish.traffic | Трафик | Байт/с | autoavgmaxmin |

### Web server

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:tech.webserver.connections.dropped` | Dropped connections  Количество разорванных соединений | Per second | autoavgmaxmin |
| `builtin:tech.webserver.connections.handled` | Handled connections  Количество успешно завершённых и закрытых запросов | Per second | autoavgmaxmin |
| `builtin:tech.webserver.connections.reading` | Reading connections  Количество соединений, получающих данные от клиента | Count | autoavgmaxmin |
| `builtin:tech.webserver.connections.socketWaitingTime` | Socket backlog waiting time  Среднее время постановки в очередь и обработки входящих соединений | Microsecond | autovalue |
| `builtin:tech.webserver.connections.waiting` | Waiting connections  Количество соединений без активных запросов | Count | autoavgmaxmin |
| `builtin:tech.webserver.connections.writing` | Writing connections  Количество соединений, передающих данные клиенту | Count | autoavgmaxmin |
| `builtin:tech.webserver.threads.active` | Active worker threads  Количество активных рабочих потоков | Count | autoavgmaxmin |
| `builtin:tech.webserver.threads.idle` | Idle worker threads  Количество простаивающих рабочих потоков | Count | autoavgmaxmin |
| `builtin:tech.webserver.threads.max` | Maximum worker threads  Максимальное количество рабочих потоков | Count | autoavgmaxmin |
| `builtin:tech.webserver.requests` | Requests  Количество запросов | Per second | autoavgmaxmin |
| `builtin:tech.webserver.traffic` | Traffic  Объём переданных данных | Byte/second | autoavgmaxmin |

### WebSphere

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:tech.websphere.connectionPool.connectionPoolModule.FreePoolSize` | Free pool size | Count | autoavgcountmaxminsum |
| `builtin:tech.websphere.connectionPool.connectionPoolModule.PercentUsed` | Percent used | Percent (%) | autoavgcountmaxminsum |
| `builtin:tech.websphere.connectionPool.connectionPoolModule.PoolSize` | Pool size | Count | autoavgcountmaxminsum |
| `builtin:tech.websphere.connectionPool.connectionPoolModule.UseTime` | In use time | Millisecond | autoavgcountmaxminsum |
| `builtin:tech.websphere.connectionPool.connectionPoolModule.WaitTime` | Wait time | Millisecond | autoavgcountmaxminsum |
| `builtin:tech.websphere.connectionPool.connectionPoolModule.WaitingThreadCount` | Number of waiting threads | Count | autoavgcountmaxminsum |
| `builtin:tech.websphere.servletSessionsModule.LiveCount` | Live sessions | Count | autoavgcountmaxminsum |
| `builtin:tech.websphere.threadPoolModule.ActiveCount` | Active threads | Count | autoavgcountmaxminsum |
| `builtin:tech.websphere.threadPoolModule.PoolSize` | Pool size | Count | autoavgcountmaxminsum |
| `builtin:tech.websphere.webAppModule.RequestCountV2` | Number of requests | Per second | autoavgcountmaxminsum |

### z/OS

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| `builtin:tech.zos.db2.cpu_usage` | z/OS DB2 CPU usage  Процент использования CPU в z/OS DB2 | Percent (%) | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.cpu_usage_dbm1` | z/OS DB2 DBM1 CPU usage  Процент использования CPU в z/OS DB2 DBM1 | Percent (%) | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.cpu_usage_mstr` | z/OS DB2 MSTR CPU usage  Процент использования CPU в z/OS DB2 MSTR | Percent (%) | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.latch_suspension_time` | z/OS DB2 latch suspension time  Время приостановки защёлки DB2 за одноминутный интервал | Microsecond | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_active_connections` | z/OS DB2 active connections  Расчётное количество активных соединений z/OS DB2 | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_active_inbound_connections` | z/OS DB2 active inbound connections  Расчётное количество активных входящих соединений z/OS DB2 | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_active_outbound_connections` | z/OS DB2 active outbound connections  Расчётное количество активных исходящих соединений z/OS DB2 | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_cache_hits` | z/OS DB2 cache hits  Расчётное количество вставок и запросов в кэш динамических операторов | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_closes` | z/OS DB2 SQL close  Количество операторов SQL close в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_deadlocks` | z/OS DB2 deadlock  Количество взаимоблокировок в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_deletes` | z/OS DB2 SQL delete  Количество операторов SQL delete в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_edm_pool_requests` | z/OS DB2 EDM pool requests  Расчётное количество запросов к пулам Environmental Descriptor Manager (EDM) в z/OS DB2 | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_failed_connections` | z/OS DB2 failed connections  Расчётное количество неудачных попыток подключения к z/OS DB2 | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_fetches` | z/OS DB2 SQL fetch  Количество операторов SQL fetch в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_inserts` | z/OS DB2 SQL insert  Количество операторов SQL insert в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_opens` | z/OS DB2 SQL open  Количество операторов SQL open в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_selects` | z/OS DB2 SQL select  Количество операторов SQL select в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_timedout_deadlocks` | z/OS DB2 deadlock timeout  Количество таймаутов взаимоблокировок в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.num_updates` | z/OS DB2 SQL update  Количество операторов SQL update в z/OS DB2 за одноминутный интервал | Count | autoavgcountmaxminsum |
| `builtin:tech.zos.db2.ziip_time` | z/OS DB2 ZIIP time  Время, затраченное z/OS DB2 на процессоре z Integrated Information Processor (zIIP) для оптимизации использования CPU | Second | autoavgcountmaxminsum |
| `builtin:tech.zos.consumed_service_units` | z/OS Consumed Service Units per minute  Расчётное количество потреблённых сервисных единиц в минуту | Count | autoavgcountmaxminsum |