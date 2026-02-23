---
title: Kong Gateway monitoring
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nginx/kong-gateway
scraped: 2026-02-23T21:23:53.582312
---

# Kong Gateway monitoring

# Kong Gateway monitoring

* Latest Dynatrace
* 4-min read
* Updated on Sep 04, 2024

To enable Kong Observability in Dynatrace, you have the following options.

* Recommended Enable OneAgent for Gateway logs, traces, and process monitoring. This should be combined with Dynatrace Prometheus scraping to monitor Kong Gateway metrics.
* Monitor Kong using a combination of OpenTelemetry for traces and Prometheus for Kong Gateway metrics.

OneAgent

OpenTelemetry

## Kong Gateway process and logs

OneAgent automatically monitors the Kong Gateway process and logs.

### Prerequisites

* Kong Gateway version 2.8+
* OneAgent or Dynatrace Operator is installed and available for monitoring your Kong Gateway.

The required installation depends on your application:

| If your application is running | See the instruction for |
| --- | --- |
| on a virtual machine or bare-metal | [OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation "Install OneAgent on a server for the very first time.") |
| as workload in Kubernetes or OpenShift | [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") |

## Application traces

In addition to process and logs, OneAgent also provides Kong Gateway application traces. See [Manual runtime instrumentation](/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.") for NGINX.

## Step 1 Configure Kong Gateway

### Prerequisites

* Kong Gateway version 3.8+

Kong Gateway requires the configuration of two settings.

* `tracing_instrumentations = all`
* `tracing_sampling_rate = 1.0`

For further details and option, see the [Kong Gateway documentationï»¿](https://dt-url.net/2m03q66).

## Step 2 Configure OpenTelemetry plugin

1. Evaluate support for logging and tracing according to the [OpenTelemetry plugin versionï»¿](https://dt-url.net/1423wjw) installed in your environment.
2. Send the following POST request (example assumes Kong Gateway 3.8+) by replacing `{HOST}`, `{PLUGIN-INSTANCE_NAME}` and `{OPENTELEMETRY_COLLECTOR}` with proper values:

```
curl -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "opentelemetry",



"instance_name": "{PLUGIN-INSTANCE_NAME}",



"config": {



"traces_endpoint": "http://{OPENTELEMETRY_COLLECTOR}:4318/v1/traces",



"logs_endpoint": "http://{OPENTELEMETRY_COLLECTOR}:4318/v1/logs",



"resource_attributes": {



"service.name": "kong-dev"



}



}



}'
```

## Step 3 Configure OpenTelemetry Collector

Configure your OpenTelemetry Collector to send data to your Dynatrace environment. The example below shows how to export traces and logs.

```
receivers:



otlp:



protocols:



http:



endpoint: 0.0.0.0:4318



exporters:



otlp_http:



endpoint: "${env:DT_BASEURL}/api/v2/otlp"



headers:



"Authorization": "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http]
```

## Step 3 Export Application Span Metrics

To include span metrics for application traces, configure the collector exporters section of the OpenTelemetry Collector configuration.

```
connectors:



spanmetrics:



dimensions:



- name: http.method



default: GET



- name: http.status_code



- name: http.route



exclude_dimensions:



- status.code



metrics_flush_interval: 15s



histogram:



disable: false



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [spanmetrics]



metrics:



receivers: [spanmetrics]



processors: []



exporters: [otlp_http]
```

## Metrics

Kongâs Prometheus plugin is a convenient way to collect Kong Gateway metrics. Dynatrace can collect these metrics directly from the Gateway produced by the Kong plugin. The default port and endpoint is `8001/metrics`.

For more information and a list of available metrics, see the [Kong Prometheus plugin documentationï»¿](https://dt-url.net/gp23qq7).

## Step 1 Enable Kong Prometheus plugin

### Basic configuration

To enable basic configuration of the Kong Prometheus plugin send a POST request replacing `{HOST}` with the host name value.

```
curl -s -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "prometheus"



}'
```

### Additional plugin metrics

To enable additional metrics produced by the Kong Gateway Prometheus plugin, send a POST request replacing `{HOST}` and `{PLUGIN-INSTANCE_NAME}` with proper values:

```
curl -s -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "prometheus",



"instance_name": "{PLUGIN-INSTANCE_NAME}",



"config": {



"per_consumer": true,



"status_code_metrics": true,



"latency_metrics": true,



"bandwidth_metrics": true,



"upstream_health_metrics": true



}



}'
```

To check available Kong metrics, query the `/metrics` endpoint:

```
curl -i http://{HOST}:8001/metrics
```

## Step 2 Collect Prometheus metrics

After configuring [Kong Gateway's Prometheus pluginï»¿](https://dt-url.net/gp23qq7), metrics can be collected using the Dynatrace ActiveGate (recommended) or the OpenTelemetry Collector.

ActiveGate

OpenTelemetry Collector

### Scrape metrics using ActiveGate

In Kubernetes, Dynatrace supports scraping of Prometheus endpoints using special annotations.

To learn how to collect Prometheus metrics in Kubernetes, see [Monitor Prometheus metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

### Scrape metrics using OpenTelemetry Collector

You can also use the OpenTelemetry Collectorâs Prometheus receiver to collect metrics from the Kong Gateway. To learn how to scrape Prometheus data using an OpenTelemetry collector, see [Scrape Promethus metrics with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.").

If you're running on Kubernetes, you can enrich traces, metrics, and logs using the Collector's Kubernetes attribute processor. This allows Dynatrace to map the telemetry data to the correct toplogy. To learn how to enable enrichment in the OpenTelemetry Collector, see [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.").