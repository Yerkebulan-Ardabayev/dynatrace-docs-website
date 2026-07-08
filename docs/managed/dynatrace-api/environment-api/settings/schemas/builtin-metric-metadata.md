---
title: Settings API - Metric metadata schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-metric-metadata
---

# Settings API - Metric metadata schema table

# Settings API - Metric metadata schema table

* Published Dec 05, 2023

### Metric metadata (`builtin:metric.metadata)`

[Custom metrics metadata﻿](https://dt-url.net/k603stq "Custom metrics metadata") allows you to provide additional information for your metric.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:metric.metadata` | * `group:metrics` | `metric` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:metric.metadata` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:metric.metadata` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:metric.metadata` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Display name `displayName` | text | - | Optional |
| Description `description` | text | - | Optional |
| Unit `unit` | text | - | Required |
| Unit display format `unitDisplayFormat` | enum | The raw value is stored in bits or bytes. The user interface can display it in these numeral systems:  Binary: 1 MiB = 1024 KiB = 1,048,576 bytes  Decimal: 1 MB = 1000 kB = 1,000,000 bytes  If not set, the decimal system is used. The element has these enums * `binary` * `decimal` | Optional |
| Metric properties `metricProperties` | [MetricProperties](#MetricProperties) | - | Optional |
| Metric dimensions `dimensions` | [Dimension](#Dimension)[] | Define metadata per metric dimension. | Required |
| Tags `tags` | list | - | Required |
| Source entity type `sourceEntityType` | text | Specifies which entity dimension should be used as the primary dimension. The property can only be configured for metrics ingested with the Metrics API. | Optional |

##### The `MetricProperties` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Minimum value `minValue` | float | The minimum allowed value of the metric. | Optional |
| Maximum value `maxValue` | float | The maximum allowed value of the metric. | Optional |
| Root cause relevant `rootCauseRelevant` | boolean | Whether (true or false) the metric is related to a root cause of a problem.  A root-cause relevant metric represents a strong indicator for a faulty component. | Optional |
| Impact relevant `impactRelevant` | boolean | Whether (true or false) the metric is relevant to a problem's impact.  An impact-relevant metric is highly dependent on other metrics and changes because an underlying root-cause metric has changed. | Optional |
| Value type `valueType` | enum | The type of the metric's value. You have these options:  score: A score metric is a metric where high values indicate a good situation, while low values indicate trouble. An example of such a metric is a success rate.  error: An error metric is a metric where high values indicate trouble, while low values indicate a good situation. An example of such a metric is an error count. The element has these enums * `error` * `score` * `unknown` | Required |
| Latency `latency` | integer | The latency of the metric, in minutes.  The latency is the expected reporting delay (for example, caused by constraints of cloud vendors or other third-party data sources) between the observation of a metric data point and its availability in Dynatrace.  The allowed value range is from 1 to 60 minutes. | Optional |

##### The `Dimension` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Dimension key `key` | text | - | Required |
| Display name `displayName` | text | - | Optional |