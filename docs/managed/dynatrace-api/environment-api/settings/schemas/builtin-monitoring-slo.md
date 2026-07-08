---
title: Settings API - Service-level objective definitions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitoring-slo
---

# Settings API - Service-level objective definitions schema table

# Settings API - Service-level objective definitions schema table

* Published Dec 05, 2023

### Service-level objective definitions (`builtin:monitoring.slo)`

Define custom [Service-level objectives﻿](https://dt-url.net/slos) (SLOs) to assist in fulfilling your organization’s service-level agreements. Create up to 10000 custom SLOs for this Dynatrace environment.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitoring.slo` | * `group:cloud-automation.monitoring.slo` * `group:cloud-automation` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoring.slo` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitoring.slo` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitoring.slo` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| SLO name `name` | text | - | Required |
| Description `customDescription` | text | The description of the SLO | Optional |
| Metric name `metricName` | text | - | Required |
| Define the metric expression that measures the success rate of this SLO `metricExpression` | text | For details, see the Metrics page (`<your-dynatrace-url>//ui/metrics "Metrics page"`). | Required |
| Evaluation type `evaluationType` | enum | Select "Aggregate" to have the measurements of this success metric aggregated into a single percentage-rate metric. The element has these enums * `AGGREGATE` | Required |
| Entity selector `filter` | text | Set a filter parameter (entitySelector) on any GET call to evaluate this SLO against specific services only (for example, type("SERVICE")). For details, see the [Entity Selector documentation﻿](https://dt-url.net/entityselector). | Required |
| Timeframe during which the SLO is to be evaluated `evaluationWindow` | text | Define the timeframe during which the SLO is to be evaluated. For the timeframe you can enter expressions like -1h (last hour), -1w (last week) or complex expressions like -2d to now (last two days), -1d/d to now/d (beginning of yesterday to beginning of today). | Required |
| Target percentage `targetSuccess` | float | Set the target value of the SLO. A percentage below this value indicates a failure. | Required |
| Warning percentage `targetWarning` | float | Set the warning value of the SLO. At the warning state the SLO is fulfilled. However, it is getting close to a failure. | Required |
| `errorBudgetBurnRate` | [ErrorBudgetBurnRate](#ErrorBudgetBurnRate) | - | Required |

##### The `ErrorBudgetBurnRate` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Burn rate visualization enabled `burnRateVisualizationEnabled` | boolean | - | Required |
| Fast-burn threshold `fastBurnThreshold` | float | The threshold defines when a burn rate is marked as fast-burning (high-emergency). Burn rates lower than this threshold (and greater than 1) are highlighted as slow-burn (low-emergency). | Required |