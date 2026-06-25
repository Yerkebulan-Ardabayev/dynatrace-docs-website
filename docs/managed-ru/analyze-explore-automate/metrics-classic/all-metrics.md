---
title: Встроенные метрики (полный список)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/metrics-classic/all-metrics
scraped: 2026-05-12T12:34:41.371407
---

# Встроенные метрики (полный список)

# Встроенные метрики (полный список)

* Справочник
* Чтение: 1 мин
* Опубликовано 10 сентября 2021 г.

Данная страница содержит полный справочник встроенных метрик Dynatrace с указанием ключей метрик, описаний, единиц измерения, агрегаций и типа потребления мониторинга.

Для просмотра всех метрик, доступных в **вашей** среде, используйте [Metric browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser) или [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics).

## Applications

### Custom

| Metric key | Name and description | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:apps.custom.reportedErrorCount | Reported error count (by OS, app version) [custom]  The number of all reported errors. | Count | autovalue | DEM units |
| builtin:apps.custom.sessionCount | Session count (by OS, app version) [custom]  The number of captured user sessions. | Count | autovalue | DEM units |

### Mobile

| Metric key | Name and description | Unit | Aggregations | Monitoring consumption |
| --- | --- | --- | --- | --- |
| builtin:apps.mobile.sessionCount | Session count (by OS, app version, crash replay feature status) [mobile]  The number of captured user sessions. | Count | autovalue | DEM units |
| builtin:apps.mobile.sessionCount.sessionReplayStatus | Session count (by OS, app version, full replay feature status) [mobile]  The number of captured user sessions. | Count | autovalue | DEM units |
| builtin:apps.mobile.reportedErrorCount | Reported error count (by OS, app version) [mobile]  The number of all reported errors. | Count | autovalue | DEM units |

*Примечание: полный справочник метрик содержит тысячи записей со всеми доступными встроенными метриками Dynatrace. Для просмотра полного списка метрик используйте [Metric browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser) или [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2/get-all-metrics).*