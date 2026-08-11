---
title: Configure OpenTelemetry tracing with Envoy
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/integrations/envoy
---

# Configure OpenTelemetry tracing with Envoy

# Configure OpenTelemetry tracing with Envoy

* How-to guide
* 4-min read
* Updated on Jul 30, 2026

Support statement

This integration is based on open source code governed by the respective communities and is not covered under the Dynatrace support policy. While we strive to assist, issues and feature requests should be reported directly to the respective project. Dynatrace cannot ensure fixes/features due to the independent nature of OSS projects.

Always use the most recent release version to ensure you have the latest patches and fixes deployed.

This page describes how to configure your Envoy version 1.30+ instance to export traces to Dynatrace. This lets you monitor traffic flowing through your Envoy proxy directly in Dynatrace.

## Prerequisites

* Envoy 1.30+
* The [OTLP traces URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") for the export.
* The OneAgent Envoy code module is disabled for your environment or host.
  To do this:

  1. Go to the applicable configuration page:

     + For the entire environment:

       - In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **Monitored technologies**.
       - In Dynatrace Classic, go to **Settings** > **Monitoring** > **Monitored technologies**.
     + For a particular host, go to **Your host** > **Host settings** > **General**.
  2. Find **Envoy** in the list of monitored technologies and select  **Edit**.
  3. Select the **Monitor Envoy** toggle, as appropriate, to turn off the OneAgent Envoy code module.

## Configure Envoy tracing

### 1. Create a Dynatrace access token

1. In Dynatrace, select `Ctrl+K` and search for **Access tokens**.
2. Select **Generate new token**.
3. Give the token a name and add the following scopes:

   * **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`)
   * **Read sampling configuration for Adaptive Traffic Management** (`adaptiveTrafficManagement.read`)
4. Select **Generate token** and copy the token value.

For more information, see [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

### 2. Add the Dynatrace cluster entry

Add the following [cluster﻿](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/intro/terminology) entry under the top-level `clusters` key in your Envoy configuration file.

```
- name: dynatrace-otel



type: LOGICAL_DNS



dns_lookup_family: V4_ONLY



lb_policy: ROUND_ROBIN



load_assignment:



cluster_name: dynatrace-otel



endpoints:



- lb_endpoints:



- endpoint:



address:



socket_address:



address: "<your-environment-id>.live.dynatrace.com"



port_value: 443



transport_socket:



name: envoy.transport_sockets.tls



typed_config:



"@type": type.googleapis.com/envoy.extensions.transport_sockets.tls.v3.UpstreamTlsContext
```

### 3. Configure the OpenTelemetry tracer

Add the following entry to the [http\_connection\_manager filters﻿](https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/configuration-static?ut=e#listeners) section of your Envoy configuration file.

```
tracing:



random_sampling:



value: 100



provider:



name: envoy.tracers.opentelemetry



typed_config:



"@type": type.googleapis.com/envoy.config.trace.v3.OpenTelemetryConfig



service_name: <your-service-name>



http_service:



http_uri:



uri: "<your-environment-id>.live.dynatrace.com/api/v2/otlp/v1/traces"



cluster: dynatrace-otel



timeout: 10s



request_headers_to_add:



- header:



key: "Authorization"



value: "Api-Token <API_TOKEN>"



resource_detectors:



- name: envoy.tracers.opentelemetry.resource_detectors.dynatrace



typed_config:



"@type": type.googleapis.com/envoy.extensions.tracers.opentelemetry.resource_detectors.v3.DynatraceResourceDetectorConfig



sampler:



name: envoy.tracers.opentelemetry.samplers.dynatrace



typed_config:



"@type": type.googleapis.com/envoy.extensions.tracers.opentelemetry.samplers.v3.DynatraceSamplerConfig



cluster_id: <cluster-id>



tenant: <your-tenant-id>



http_service:



http_uri:



cluster: "dynatrace-otel"



uri: "<your-environment-id>.live.dynatrace.com/api/v2/samplingConfiguration"



timeout: 10s



request_headers_to_add:



- header:



key: "authorization"



value: "Api-Token <API_TOKEN>"
```

Replace the following placeholders with the appropriate values:

* `<your-service-name>`: Your service's name.
* `<your-environment-id>`: Your Dynatrace environment ID. See [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") to find yours.
* `<API_TOKEN>`: The access token you created.
* `<cluster-id>`: The numeric ID of your Dynatrace cluster.
* `<your-tenant-id>`: The same value as `<your-environment-id>`.

If you're setting up the integration through the Dynatrace Hub (search for `Envoy` > select the Hub entry > **Set up**), the `<cluster-id>` value is pre-filled in the provided snippet. If you don't have access to this wizard, retrieve the value by sending a `GET` request to `https://<your-environment-id>.live.dynatrace.com/api/v1/config/clusterid` with an access token that has the **Data Export** (`DataExport`) scope.

For more information, see [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

### 4. Verify the setup

After the setup is complete and you have ingested your first data, you can verify if the traces show up in Dynatrace.

![OpenTelemetry traces visible in Distributed Tracing](https://dt-cdn.net/images/screenshot-1863-979a8a5284.png)

OpenTelemetry traces visible in Distributed Tracing

## Next steps

To also trace Istio-managed traffic, see [Configure OpenTelemetry tracing with Istio](/managed/ingest-from/opentelemetry/integrations/istio "Configure Istio to export OpenTelemetry traces to Dynatrace using the Istio OpenTelemetry extension provider, in a standalone deployment or with Dynatrace Operator.").

## Related topics

* [Prometheus](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Learn how to extend observability in Dynatrace with Prometheus metrics.")
* [Istio/Envoy proxy metrics](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Istio metric ingestion and topology detection")