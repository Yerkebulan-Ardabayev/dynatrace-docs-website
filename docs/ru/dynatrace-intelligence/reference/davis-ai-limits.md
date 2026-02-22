---
title: Dynatrace Intelligence limits
source: https://www.dynatrace.com/docs/dynatrace-intelligence/reference/davis-ai-limits
scraped: 2026-02-22T21:23:10.191139
---

# Dynatrace Intelligence limits

# Dynatrace Intelligence limits

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Feb 04, 2026

The following page lists the default limits of Dynatrace Intelligence components.

## Problems and events

Some of the problems and events limits apply per provider. The following providers are subject to limits:

* `AGENT_LOCAL_REST_API_INGEST`
* `AVAILABILITY`
* `BASELINING`
* `EVENTS_REST_API_INGEST`
* `KUBERNETES_ANOMALY_DETECTION`
* `KUBERNETES_EVENT`
* `LOG_EVENTS`
* `METRIC_EVENTS`
* `ONEAGENT`
* `OPENPIPELINE_DATA_EXTRACTION`
* `REAL_USER_MONITORING`
* `SYNTHETIC`

### Number of simultaneously active Davis problems

The maximum number of simultaneously active Davis problems within a single environment is 10,000.

### Number of simultaneously active Davis events

The maximum number of simultaneously active Davis events within a single environment, across all event providers, is 15,000.

### Number of simultaneously active Davis events per provider

The maximum number of simultaneously active Davis events per event provider is 4,000. Example of the event provider: `event.provider = "AVAILABILITY"`.

### Number of Davis events processed every hour

The maximum number of Davis events per event provider that can be processed within an hour is 100,000. This limit is replenished every hour.

Certain events override default limits. See the table below for more information.

Event provider

Maximum limit

`AVAILABILITY`

200,000 Davis events processed per hour.

`METRIC_EVENTS`

200,000 Davis events processed per hour.

* `AGENT_LOCAL_REST_API_INGEST`
* `BASELINING`
* `EVENTS_REST_API_INGEST`
* `KUBERNETES_ANOMALY_DETECTION`
* `KUBERNETES_EVENT`
* `LOG_EVENTS`
* `ONEAGENT`
* `OPENPIPELINE_DATA_EXTRACTION`
* `REAL_USER_MONITORING`
* `SYNTHETIC`

The default of 100,000 Davis events processed per hour applies.

### Event maximum lifetime

The maximum lifetime for active events is 60 days. If the underlying anomaly doesn't disappear after 60 days, the respective event is closed and a new one is created.

### Problem merging timeframe

The maximum problem merging timeframe is 90 minutes. If the problem remains unresolved for more than 90 minutes, no new events will be merged into it after that.

This measure ensures that Dynatrace Intelligence avoids collecting unrelated information for long-lasting incidents.

## Anomaly Detection - new **Anomaly Detection**

### Custom alerts

Item

Maximum limit

Description

Number of custom alert configurations

1,000 per environment

The maximum number of custom alerts that can be configured.

Grail query request timeout

10 seconds

The maximum time limit for the query execution.

Number of auto-adaptive threshold monitored dimensions

10,000 per configuration

The maximum number of auto-adaptive threshold monitored dimensions. Once the limit is reached, no additional dimensions will be monitored.

Number of seasonal baseline monitored dimensions

10,000 per configuration

The maximum number of seasonal baseline monitored dimensions. Once the limit is reached, no additional dimensions will be monitored.

### Metric events

#### General

Item

Maximum limit

Description

Number of metric events

10,000 per environment

The maximum number of metric events that can be configured.

#### Metric selector events

Item

Maximum limit

Description

Number of monitored dimensions

100,000

This limit applies across all customer-defined metric selector metric events.

Dynatrace also counts aggregated dimensions towards the limit. Once the limit is reached, no additional dimensions will be monitored.

Number of static threshold metric event configurations

100

The maximum number of static threshold model metric event configurations created with metric selector.

Number of static threshold monitored dimensions

1,000 per configuration

The maximum number of static threshold monitored dimensions. Once the limit is reached, no additional dimensions will be monitored.

Number of auto-adaptive threshold metric event configurations

100

The maximum number of metric event configurations that use the auto-adaptive threshold model.

Number of auto-adaptive threshold monitored dimensions

1,000 per configuration

The maximum number of auto-adaptive threshold monitored dimensions. Once the limit is reached, no additional dimensions will be monitored.

Number of seasonal baseline metric event configurations

100

The maximum number of metric event configurations that use the seasonal baseline model.

Number of seasonal baseline monitored dimensions

500 per configuration

The maximum number of seasonal baseline monitored dimensions. Once the limit is reached, no additional dimensions will be monitored.

Hard monitored dimension limit

10,000 per configuration

If the number of monitored dimensions exceeds the hard limit, the query will start failing.

#### Metric key events

Item

Maximum limit

Description

Number of simultaneously active alerts

200 per configuration

The maximum number of simultaneously active alerts per metric key-based configuration.

### Notebook & Dashboard Simulation

Item

Maximum limit

Description

Data records

1,000

The maximum number of timeseries data records that can be uniquely simulated per single data analyzer execution.

## Dynatrace Intelligence generative AI

Item

Maximum limit

Individual user requests

25 requests per 15 minutes

All user requests across the environment

60 requests per 15 minutes