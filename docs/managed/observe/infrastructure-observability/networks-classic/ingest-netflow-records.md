---
title: Ingest NetFlow records into Dynatrace
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/networks-classic/ingest-netflow-records
---

# Ingest NetFlow records into Dynatrace

# Ingest NetFlow records into Dynatrace

* How-to guide
* 2-min read
* Updated on Jan 19, 2026

Network observability provides the necessary visibility to understand how applications interact with the underlying network. It allows teams to identify and address issues more effectively by starting with device health monitoring and extending to flow data collection—such as NetFlow—to track network usage. This approach actively supports performance optimization, enhances security, and streamlines troubleshooting efforts.

This guide shows how to ingest NetFlow records into Dynatrace by setting up the collector.

## Why monitor network flow with Dynatrace?

Ingesting network flows into Dynatrace immediately puts this data in context. The data contained in the network flows complements supported network use cases by linking flow volume and directions to devices and interfaces. The network flow data can be compared with process-to-process data to help solve network-induced application problems.

## How does Dynatrace as a platform support NetFlow ingestion?

Dynatrace supports network flow protocols such as NetFlow, sFlow, and IPFIX through a fully supported version of the [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."). A dedicated network flow receiver enables seamless ingestion of flow data into the Dynatrace platform for analysis and visualization.

## Prerequisites

* A [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") distribution with [NetFlow receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver).
* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the **Ingest logs** (`logs.ingest`) and **Ingest metrics** (`metrics.ingest`) scopes.

See [Collector Deployment](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") and [Collector Configuration](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Steps

In this example, we deploy using Docker to keep the demonstration simple. For production use cases, we recommend deploying as a gateway on a Kubernetes cluster. For details, see [Configure OpenTelemetry Collector for Kubernetes monitoring](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.").

1. To configure a Dynatrace Collector instance, create a file called `otel-collector-config.yaml` and add the following configuration:

   ```
   receivers:



   netflow:



   scheme: netflow



   port: 2055



   sockets: 16



   workers: 32



   netflow/sflow:



   scheme: sflow



   port: 6343



   sockets: 16



   workers: 32



   processors:



   batch:



   send_batch_size: 2000



   timeout: 30s



   exporters:



   otlp_http:



   endpoint: "${env:DT_ENDPOINT}"



   headers:



   Authorization: "Api-Token ${env:DT_API_TOKEN}"



   service:



   pipelines:



   logs:



   receivers: [netflow, netflow/sflow]



   processors: [batch]



   exporters: [otlp_http]



   telemetry:



   logs:



   level: debug
   ```

   Check the [NetFlow receiver﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver#netflow-receiver) documentation for the available configuration options.
2. Create an `.env` file to add the `DT_ENDPOINT` and `DT_API_TOKEN` variables.

   * `DT_ENDPOINT` is the Dynatrace API server endpoint. It contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). For example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`. For more details, see [Integrate OneAgent on Azure App Service for Linux and containers](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.").
   * `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

   Ensure your `.env` file is properly secured and not exposed to unauthorized access, as it contains sensitive information.
3. Create an access token by going to **Access Tokens** > **Generate new token** and selecting **Ingest logs** as a scope.
4. Run the Collector image in Docker using the following command:

   ```
   docker run -p 2055:2055 --env-file ./.dt_token.env -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.33.0 --config=/etc/otelcol/otel-collector-config.yaml
   ```

   Once the process is completed, you can start running and processing data.

   If you want the process to run in the background, you can kill it and run again with the `-d` option.
5. Direct your network devices to send NetFlow records to the Collector.

   The network device configuration is vendor-specific. It must indicate the Dynatrace endpoint's IP address and the matching UDP port.

You have successfully configured NetFlow ingestion. Your network flow data is now available in Dynatrace for analysis.

## Related topics

* [Ingest NetFlow with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/netflow "Configure the OpenTelemetry Collector to ingest NetFlow data.")