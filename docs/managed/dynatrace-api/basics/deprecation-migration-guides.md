---
title: Migration guides for deprecated APIs
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/deprecation-migration-guides
scraped: 2026-05-12T11:04:46.602075
---

# Migration guides for deprecated APIs

# Migration guides for deprecated APIs

* Reference
* Updated on Nov 20, 2025

The following APIs have been deprecated. For backward compatibility, the endpoints remain functional until further notice, but we recommend that you use the new options instead.

Every deprecated endpoint will eventually reach end of life (EOL) and be disabled. You won't be able to use them afterward. We provide enough time to switch to the new option before shutting down the old one. Even if the EOL date is not defined, you still should adapt your integrations to the new options.

## Deprecated

| Deprecated API | What to use instead | Deprecated in version | End of life in version | Migration guide |
| --- | --- | --- | --- | --- |
| Security context API | [Management zones API](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "View builtin:management-zones settings schema table of your monitoring environment via the Dynatrace API.") | [SaaS 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")  [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316") | Managed: 1.322 |  |
| Monitored entities API v2 - Security context | [Management zones API](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "View builtin:management-zones settings schema table of your monitoring environment via the Dynatrace API.") | [SaaS 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316")  [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316") | Managed: 1.322 |  |
| Grail security context for monitored entities API | n/a | [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316") | Managed: 1.322 |  |
| Log security context API | n/a | [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316") | Managed: 1.322 |  |
| Business event security context API | n/a | [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316") | Managed: 1.322 |  |
| [Timeseries API v1](/managed/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.") | [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") | [SaaS 1.305](/managed/whats-new/dynatrace-api/sprint-305#timeseries "Changelog for Dynatrace API version 1.305")  [Managed 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316") | End of 2025 |  |
| Log Monitoring API v1 | Log Management and Analytics: [Grail Query APIï»¿](https://developer.dynatrace.com/platform-services/services/storage/#grail-query-api)  Log Monitoring Classic: [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")  For **Calculated metrics - Log Monitoring**, use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") endpoint with schemaId `builtin:logmonitoring.schemaless-log-metric`. | SaaS 1.280  Managed 1.284 | SaaS 1.325  Managed 1.326 |  |

## Migrated to Settings 2.0 framework

The following APIs have been migrated to the Settings 2.0 framework. Migrated configurations are handled via [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with a related schema.

| Deprecated API | Schema to use instead | Deprecated in version | End of life in version | Migration guide |
| --- | --- | --- | --- | --- |