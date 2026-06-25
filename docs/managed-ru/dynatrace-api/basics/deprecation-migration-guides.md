---
title: Руководства по миграции с устаревших API
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/deprecation-migration-guides
scraped: 2026-05-12T11:04:46.602075
---

# Руководства по миграции с устаревших API

# Руководства по миграции с устаревших API

* Reference
* Updated on Nov 20, 2025

Следующие API объявлены устаревшими. Для обратной совместимости endpoints продолжают работать до особого уведомления, но рекомендуется переходить на новые варианты.

Каждый устаревший endpoint в итоге достигает конца жизненного цикла (end of life, EOL) и отключается. После этого использовать его будет нельзя. Перед отключением мы даём достаточно времени для перехода на новый вариант. Даже если дата EOL не определена, лучше адаптировать ваши интеграции под новые варианты заранее.

## Устаревшие

| Устаревший API | Чем заменять | Версия объявления устаревшим | Версия конца жизненного цикла | Руководство по миграции |
| --- | --- | --- | --- | --- |
| Security context API | [Management zones API](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "Просмотр таблицы схемы настроек builtin:management-zones для вашего окружения мониторинга через Dynatrace API.") | [SaaS 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog Dynatrace API версии 1.316")  [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog Dynatrace API версии 1.316") | Managed: 1.322 |  |
| Monitored entities API v2 - Security context | [Management zones API](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "Просмотр таблицы схемы настроек builtin:management-zones для вашего окружения мониторинга через Dynatrace API.") | [SaaS 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog Dynatrace API версии 1.316")  [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog Dynatrace API версии 1.316") | Managed: 1.322 |  |
| Grail security context for monitored entities API | n/a | [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog Dynatrace API версии 1.316") | Managed: 1.322 |  |
| Log security context API | n/a | [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog Dynatrace API версии 1.316") | Managed: 1.322 |  |
| Business event security context API | n/a | [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog Dynatrace API версии 1.316") | Managed: 1.322 |  |
| [Timeseries API v1](/managed/dynatrace-api/environment-api/metric-v1 "Получение информации о метриках через Timeseries v1 API.") | [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API.") | [SaaS 1.305](/managed/whats-new/dynatrace-api/sprint-305#timeseries "Changelog Dynatrace API версии 1.305")  [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog Dynatrace API версии 1.316") | End of 2025 |  |
| Log Monitoring API v1 | Log Management and Analytics: [Grail Query API](https://developer.dynatrace.com/platform-services/services/storage/#grail-query-api)  Log Monitoring Classic: [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Возможности Log Monitoring API v2.")  Для **Calculated metrics - Log Monitoring** используйте endpoint [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API.") со schemaId `builtin:logmonitoring.schemaless-log-metric`. | SaaS 1.280  Managed 1.284 | SaaS 1.325  Managed 1.326 |  |

## Перенесено во фреймворк Settings 2.0

Следующие API перенесены во фреймворк Settings 2.0. Перенесённые конфигурации управляются через [Settings API](/managed/dynatrace-api/environment-api/settings "Возможности Dynatrace Settings API.") по соответствующей схеме.

| Устаревший API | Какую схему использовать вместо | Версия объявления устаревшим | Версия конца жизненного цикла | Руководство по миграции |
| --- | --- | --- | --- | --- |