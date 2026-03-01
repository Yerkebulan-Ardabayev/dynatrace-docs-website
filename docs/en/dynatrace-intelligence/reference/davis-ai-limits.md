---
title: Dynatrace Intelligence limits
source: https://www.dynatrace.com/docs/dynatrace-intelligence/reference/davis-ai-limits
scraped: 2026-03-01T21:22:45.697418
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

### Event maximum lifetime

The maximum lifetime for active events is 60 days. If the underlying anomaly doesn't disappear after 60 days, the respective event is closed and a new one is created.

### Problem merging timeframe

The maximum problem merging timeframe is 90 minutes. If the problem remains unresolved for more than 90 minutes, no new events will be merged into it after that.

This measure ensures that Dynatrace Intelligence avoids collecting unrelated information for long-lasting incidents.

## Anomaly Detection - new **Anomaly Detection**

### Custom alerts

### Metric events

#### General

#### Metric selector events

#### Metric key events

### Notebook & Dashboard Simulation

## Dynatrace Intelligence generative AI