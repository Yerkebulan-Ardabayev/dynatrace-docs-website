---
title: Dynatrace OTel Collector system requirements.
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/system-requirements
scraped: 2026-02-21T21:16:41.469770
---

# Dynatrace OTel Collector system requirements.

# Dynatrace OTel Collector system requirements.

* Latest Dynatrace
* Reference
* 2-min read
* Updated on Sep 04, 2025

This page describes system requirements for the Dynatrace OpenTelemetry Collector distribution for different use cases.

### Hardware used

The numbers below were gathered using an Azure virtual machine of type Dadsv5-series (AMD EPYC 7763v Genoa CPU) with 4 vCPUs and 16GB RAM.

### CPU and memory requirements for traces, metrics and logs (combined)

The requirements for the Dynatrace Collector are based on a load scenario with the following numbers per second:

* 1000 traces (~1.2 KB each)
* 1000 metrics (~1.2 KB each)
* 1 MB logs

The recommended resources for this combined scenario are:

* 500 MiB RAM
* 500 mCPU

If you need additional data processing (for example, filter or transform processors), system requirements will increase.

For specific scaling and infrastructure architecture considerations, see [Deploy Dynatrace OTel Collector](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [How to scale the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/scaling "How to scale the OpenTelemetry Collector.").

### Specific load scenarios

The Dynatrace Collector was also tested under heavier scenarios than above but only with single signal types.
The following table shows performance data based on the following base data sizes:

* Traces: ~1 KiB per trace
* Metrics: ~3 KiB per metric
* Logs: ~3 KiB per line

This table shows throughput scenarios based on the above data sizes with different amounts of load and different used protocols.

| Scenario (traces, metrics, logs per second) | CPU cores | RAM (MiB) |
| --- | --- | --- |
| OTLP-HTTP 10k traces | 0.25 | 100 |
| OTLP-HTTP 100k traces | 1.5 | 120 |
| OTLP-HTTP 10k metrics | 0.25 | 110 |
| OTLP-HTTP 100k metrics | 1 | 100 |
| Syslog 10k logs 1 per batch | 0.2 | 100 |
| Syslog 10k logs 100 per batch | 0.2 | 100 |
| Syslog 70k logs 1 per batch | 1 | 100 |
| Syslog 70k logs 100 per batch | 0.5 | 110 |

### Prometheus scrape performance

Additional metrics based load scenarios were done based on Prometheus scraping with the following base settings:

* 1s scrape interval
* Metrics data size: ~3 KiB per metric

This table shows the load results with different scenarios.

| Scenario | CPU cores | RAM (MiB) |
| --- | --- | --- |
| 1 endpoint (10k data points each) | 0.5 | 300 |
| 1 endpoint (1k data points each) | 0.1 | 140 |
| 5 endpoints (1k data points each) | 1.5 | 250 |
| 10 endpoints (1k data points each) | 2 | 500 |