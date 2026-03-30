---
title: "Metrics"
source: https://docs.dynatrace.com/managed/analyze-explore-automate/metrics-classic
updated: 2026-02-09
---

* 2-min read

In Dynatrace, you have various types of metrics at your disposal:

* Built-in metrics provided by OneAgent. These have the `builtin:` prefix in the metric key.

* Extension metrics provided by OneAgent or ActiveGate extensions. These have the `ext:` prefix in the metric key.

  The `ext:` prefix is used by metrics from OneAgent extensions and ActiveGate extensions, and also by classic metrics for AWS integration.

  Despite the naming similarities, AWS integration metrics are **not** based on extensions.
* Calculated metrics you create. These have the `calc:` prefix in the metric key.
* USQL custom metrics you create: user session custom metrics (`uscm.` prefix) and user action custom metrics (`uacm.` prefix). These metrics are based on metadata extracted from user session and user action data.
* Custom metrics you can feed to Dynatrace via metric ingestion. These don't have any fixed prefix, as the ingestion protocol is completely flexible.

Metrics frequency

* Infrastructure metrics and other periodic metrics are captured every 10 seconds and stored as 1-minute aggregates. Typically, this includes a min/max/count/sum/average of the measured metric.
* Service and web request metrics do not have a frequency. Dynatrace captures the transactions and displays medians and 90th percentiles. RUM and service analysis pages are based on this data.
* For custom metrics ingestion, the standard resolution is 1 minute, but you can also get statistic summaries.

### Ingestion

Push custom data to Dynatrace.### Built-in metrics

Get an overview of metrics available out of the box.### Self-monitoring metrics

Get an overview of self-monitoring metrics available out of the box.### Metric browser

Get an overview of all metrics available in your environment.

### Calculated metrics

Log Monitoring

Service

Synthetic

RUM - web applications

RUM - mobile applications

RUM - custom applications

### USQL custom metrics

RUM - web applications

RUM - mobile applications

RUM - custom applications

### Metric sources

Metric open ingest

OpenTelemetry metrics into Dynatrace.")

AWS service metrics

Azure service metrics

Metrics for Dynatrace Runtime Vulnerability Analytics

Log metrics (Logs Classic)

### See also

Data Explorer

Metrics API v2

Calculated metrics API

Metric events for alerting
