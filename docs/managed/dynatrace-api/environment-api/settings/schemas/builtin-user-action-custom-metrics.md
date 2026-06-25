---
title: Settings API - User action custom metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-user-action-custom-metrics
scraped: 2026-05-12T11:45:51.581289
---

# Settings API - User action custom metrics schema table

# Settings API - User action custom metrics schema table

* Published Dec 05, 2023

### User action custom metrics (`builtin:user-action-custom-metrics)`

With user action custom metrics (see [documentationï»¿](https://dt-url.net/3i03u3s)), you can extract business-level KPI metrics from user action data. Metrics can then be saved as timeseries and consumed (without interpolation) by your custom charts, alerting mechanisms or the Metrics REST API (`<your-dynatrace-url>//rest-api-doc/?urls.primaryName=Environment+API+v2#/Metrics`).

To explore collected metrics, go to Data explorer (`<your-dynatrace-url>//ui/data-explorer`).

To create a custom event based on a custom metric, go to Custom events for alerting (`<your-dynatrace-url>//#settings/anomalydetection/metricevents`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:user-action-custom-metrics` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.usql-custom-metrics` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:user-action-custom-metrics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:user-action-custom-metrics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:user-action-custom-metrics` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable custom metric `enabled` | boolean | - | Required |
| Metric key `metricKey` | text | - | Required |
| Value type to be extracted `value` | [MetricValue](#MetricValue) | Defines the type of value to be extracted from the user action. When using **user action counter**, the number of user actions is counted (similar to count(\*) when using USQL). When using **user action field value**, the value of a user action field is extracted. | Required |
| Add a dimension `dimensions` | list | Defines the fields that are used as dimensions. A dimension is a collection of reference information about a metric data point that is of interest to your business. Dimensions are parameters like "application", "type", "apdexCategory". For example, using "type" as a dimension allows you to split chart data based on the user action type. | Required |
| Add a filter `filters` | [Filter](#Filter)[] | Defines the filters for the user action. Filters apply at the moment of extracting the data and only sessions that satisfy the filtering criteria will be used to extract the custom metrics. You will not be able to modify these filters in the metric data explorer. For example, using "type equals Xhr" will give you only data from xhr actions, while forcing the rest of user actions of different types to be ignored. | Required |

##### The `MetricValue` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `type` | enum | The element has these enums * `COUNTER` * `FIELD` | Required |
| Field name `fieldName` | text | - | Required |

##### The `Filter` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Field name `fieldName` | text | - | Required |
| Operator `operator` | enum | The element has these enums * `EQUALS` * `NOT_EQUAL` * `IS_NULL` * `IS_NOT_NULL` * `LIKE` * `NOT_LIKE` * `LESS_THAN` * `LESS_THAN_OR_EQUAL_TO` * `GREATER_THAN` * `GREATER_THAN_OR_EQUAL_TO` * `IN` * `STARTS_WITH` | Required |
| Value `value` | text | - | Required |
| Values `valueIn` | list | - | Required |