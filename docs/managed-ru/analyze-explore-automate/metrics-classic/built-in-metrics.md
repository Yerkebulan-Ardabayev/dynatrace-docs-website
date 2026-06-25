---
title: Встроенные метрики
source: https://docs.dynatrace.com/managed/analyze-explore-automate/metrics-classic/built-in-metrics
scraped: 2026-05-12T11:07:07.924139
---

# Встроенные метрики

# Встроенные метрики

* Справочник
* Чтение: 3 мин
* Опубликовано 03 сентября 2020 г.

Каждая поддерживаемая Dynatrace технология предоставляет несколько «встроенных» метрик. Встроенные метрики входят в продукт из коробки, в ряде случаев — в составе встроенных расширений.

Метрики, основанные на расширениях OneAgent или ActiveGate (префикс `ext:`), и вычисляемые метрики (префикс `calc:`) — это пользовательские метрики, а не встроенные; [потребление DDU](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Узнайте, как рассчитать потребление Davis Data Units и затраты, связанные с отслеживаемыми метриками.") для этих метрик может значительно варьироваться в зависимости от того, как вы используете Dynatrace.

Префикс `ext:` используется метриками [расширений OneAgent](/managed/ingest-from/extensions/develop-your-extensions "Разрабатывайте собственные расширения в Dynatrace.") и [расширений ActiveGate](/managed/ingest-from/extensions/develop-your-extensions "Разрабатывайте собственные расширения в Dynatrace."), а также [классическими метриками для интеграции с AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Интегрируйте метрики из Amazon CloudWatch.").

Несмотря на схожесть названий, метрики интеграции AWS **не** основаны на расширениях.

Чтобы просмотреть все метрики, доступные в **вашей** среде, используйте API-вызов [GET metrics](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics "Список всех метрик, доступных в вашей среде мониторинга, через Metrics v2 API."). Рекомендуемые параметры запроса:

* `pageSize=500` — для получения максимально возможного количества метрик в одном ответе.
* `fields=displayName,unit,aggregationTypes,dduBillable` — для получения того же набора полей, что отображается в таблицах.
* В зависимости от того, какие метрики нужно запросить, одно из следующих значений параметра **metricSelector**:

  + `metricSelector=ext:*` — для получения всех метрик из расширений.
  + `metricSelector=calc:*` — для получения всех вычисляемых метрик.
  + Не указывайте параметр, чтобы получить **все** метрики вашей среды.

В разделах ниже описаны несоответствия или ограничения, выявленные для встроенных метрик Dynatrace.

Метрики приложений и биллинга для мобильных и пользовательских приложений

Раздел [Метрики других приложений](#other-applications-metrics) содержит метрики, собираемые для мобильных и пользовательских приложений. Эти метрики, начинающиеся с `builtin:apps.other`, захватываются без указания типа приложения — мобильное или пользовательское. Однако «биллинговые» метрики приложений, начинающиеся с `builtin:billing.apps`, разделены по этим типам:

* Мобильные приложения:

  + `builtin:billing.apps.mobile.sessionsWithoutReplayByApplication`
  + `builtin:billing.apps.mobile.sessionsWithReplayByApplication`
  + `builtin:billing.apps.mobile.userActionPropertiesByMobileApplication`
* Пользовательские приложения:

  + `builtin:billing.apps.custom.sessionsWithoutReplayByApplication`
  + `builtin:billing.apps.custom.userActionPropertiesByDeviceApplication`

Биллинговые метрики учитывают как оплачиваемые, так и неоплачиваемые сессии

Следующие «биллинговые» метрики количества сессий фактически представляют собой сумму **оплачиваемых и неоплачиваемых** пользовательских сессий.

* `builtin:billing.apps.custom.sessionsWithoutReplayByApplication`
* `builtin:billing.apps.mobile.sessionsWithReplayByApplication`
* `builtin:billing.apps.mobile.sessionsWithoutReplayByApplication`
* `builtin:billing.apps.web.sessionsWithReplayByApplication`
* `builtin:billing.apps.web.sessionsWithoutReplayByApplication`

Чтобы получить только количество оплачиваемых сессий, установите фильтр **Type** в значение **Billed**.

Различные единицы измерения для метрик длительности запросов

Для аналогичных метрик длительности запросов для мобильных и пользовательских приложений используются разные единицы измерения.

`builtin:apps.other.keyUserActions.requestDuration.os` измеряется в микросекундах, тогда как другие метрики длительности запросов (`builtin:apps.other.requestTimes.osAndVersion` и `builtin:apps.other.requestTimes.osAndProvider`) измеряются в миллисекундах.

Пользовательские и встроенные метрики

Пользовательские метрики определяются или устанавливаются пользователем, тогда как встроенные метрики по умолчанию входят в состав продукта. Некоторые встроенные метрики по умолчанию отключены и при активации потребляют [DDU](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе Davis Data Units (DDU)."). Эти метрики охватывают широкий спектр поддерживаемых технологий, включая Apache Tomcat, NGINX, Couchbase, RabbitMQ, Cassandra, Jetty и многие другие.

Пользовательская метрика — это новый тип метрики с предоставленными пользователем идентификатором и единицей измерения. Семантика пользовательских метрик определяется самим пользователем и не входит в установку OneAgent по умолчанию. Пользовательские метрики отправляются в Dynatrace через [различные интерфейсы](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace."). После определения пользовательской метрики она может передаваться для нескольких отслеживаемых компонентов — каждый из них создаёт отдельный временной ряд.

Например, если определить новую пользовательскую метрику `Files count` для подсчёта вновь созданных файлов в директории, она может собираться либо для одного хоста, либо для двух отдельных хостов. Сбор одной метрики для двух хостов даёт два временных ряда одного типа пользовательской метрики, как показано на примере ниже:

![Пользовательские метрики](https://dt-cdn.net/images/custommetrics2-1329-59422c6592.png)

Пользовательские метрики

В целях [расчёта потребления мониторинга](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Узнайте, как рассчитать потребление Davis Data Units и затраты, связанные с отслеживаемыми метриками.") сбор одной и той же пользовательской метрики для двух хостов считается двумя отдельными пользовательскими метриками.

## Applications

### Custom

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:apps.custom.reportedErrorCount | Reported error count (by OS, app version) [custom]  The number of all reported errors. | Count | autovalue |
| builtin:apps.custom.sessionCount | Session count (by OS, app version) [custom]  The number of captured user sessions. | Count | autovalue |

### Mobile

| Metric key | Name and description | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:apps.mobile.sessionCount | Session count (by OS, app version, crash replay feature status) [mobile]  The number of captured user sessions. | Count | autovalue |
| builtin:apps.mobile.sessionCount.sessionReplayStatus | Session count (by OS, app version, full replay feature status) [mobile]  The number of captured user sessions. | Count | autovalue |
| builtin:apps.mobile.reportedErrorCount | Reported error count (by OS, app version) [mobile]  The number of all reported errors. | Count | autovalue |

*Примечание: полный справочник метрик содержит тысячи записей. Для просмотра всех доступных метрик используйте [Metric browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser) или [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics).*