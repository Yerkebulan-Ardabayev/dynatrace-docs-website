---
title: Configure OpenTelemetry tracing with Envoy
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/integrations/envoy
scraped: 2026-05-12T11:23:45.595247
---

# Configure OpenTelemetry tracing with Envoy

# Configure OpenTelemetry tracing with Envoy

* How-to guide
* 4-min read
* Updated on Apr 07, 2026

Support statement

This integration is based on open source code governed by the respective communities and is not covered under the Dynatrace support policy. While we strive to assist, issues and feature requests should be reported directly to the respective project. Dynatrace cannot ensure fixes/features due to the independent nature of OSS projects.

Always use the most recent release version to ensure you have the latest patches and fixes deployed.

This page describes how to configure your Envoy version 1.30+ instance to export traces to Dynatrace.

### Prerequisites

* The [OTLP traces URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") for the export.
* The OneAgent Envoy code module is disabled.
  To do this:

  1. Go to the applicable configuration page:

     + For the entire environment, go to **Settings** > **Monitoring** > **Monitored technologies**.
     + For a particular host, go to **Your host** > **Host settings** > **General**.
  2. Find **Envoy** in the list of monitored technologies and select  **Edit**.
  3. Select the **Monitor Envoy** toggle, as appropriate, to disable the OneAgent Envoy code module.

### Steps

1. Get configuration entries

1. In Dynatrace Hub, search for `Envoy`.
2. Select the Hub entry for Envoy.
3. Select **Set up**.
4. Configure the API token.
5. Proceed with the following steps and use (and adjust) the two provided configuration snippets where applicable.

2. Add Dynatrace cluster entry for OpenTelemetry export

For Envoy to send traces to Dynatrace, you first need to configure a [clusterï»¿](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/intro/terminology) entry for Dynatrace in the Envoy configuration file. For that, add the [cluster configuration entry as obtained in step 2](#snippets) under the top-level `clusters` key.

3. Dynatrace-specific configuration for the OpenTelemetry tracer

Next, you need to add the tracing provider to the [HTTP connection manager filterï»¿](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_connection_management#http-connection-management) in the [Envoy configuration fileï»¿](https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/configuration-static#listeners).

Use the [tracer configuration entry you obtained in step 2](#snippets), configure the [API token](#prerequisites) under `tracing` - `provider` - `typed_config` - `http_service` - `request_headers_to_add` - `header` - `value` (the correct syntax is `value: "Api-Token YOUR_API_TOKEN_HERE"`), and add the tracer configuration under aforementioned `filters` entry.

4. Verify the setup

Once the setup is complete and you have ingested your first data, you can verify if the traces show up in Dynatrace.

![trace](https://dt-cdn.net/images/screenshot-1863-979a8a5284.png)

trace

## Related topics

* [Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Learn how to extend observability in Dynatrace with Prometheus metrics.")
* [Istio/Envoy proxy metrics](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Istio metric ingestion and topology detection")