---
title: Ingest NetFlow records into Dynatrace
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/networks/ingest-netflow-records
scraped: 2026-02-24T21:20:20.254013
---

# Ingest NetFlow records into Dynatrace

# Ingest NetFlow records into Dynatrace

* How-to guide
* 2-min read
* Updated on Jan 19, 2026

Network observability provides the necessary visibility to understand how applications interact with the underlying network. It allows teams to identify and address issues more effectively by starting with device health monitoring and extending to flow data collectionâsuch as NetFlowâto track network usage. This approach actively supports performance optimization, enhances security, and streamlines troubleshooting efforts.

This guide shows you how to ingest NetFlow records into Dynatrace by setting up the collector and using ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** to analyze flow data.

## Why monitor network flow with Dynatrace?

Ingesting network flows into Dynatrace immediately puts this data in context. The data contained in the network flows complements supported network use cases by linking flow volume and directions to devices and interfaces. The network flow data can be compared with process-to-process data to help solve network-induced application problems.

## How does Dynatrace as a platform support NetFlow ingestion?

Dynatrace supports network flow protocols such as NetFlow, sFlow, and IPFIX through a fully supported version of the [OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector."). A dedicated network flow receiver enables seamless ingestion of flow data into the Dynatrace platform for analysis and visualization.

## Prerequisites

* A [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.") distribution with [NetFlow receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver).
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the **Ingest logs** (`logs.ingest`) and **Ingest metrics** (`metrics.ingest`) scopes. For details, see [OpenTelemetry Collector self-monitoring](/docs/ingest-from/opentelemetry/collector/self-monitoring "How to monitor OpenTelemetry Collectors with Dynatrace dashboards.").

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Steps

In this example, we deploy using Docker to keep the demonstration simple. For production use cases, we recommend deploying as a gateway on a Kubernetes cluster. For details, see [Configure OpenTelemetry Collector for Kubernetes monitoring](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-monitoring "Configure the OpenTelemetry Collector to monitor your Kubernetes clusters.").

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

   Check the [NetFlow receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.136.0/receiver/netflowreceiver#netflow-receiver) documentation for the available configuration options.
2. Create an `.env` file to add the `DT_ENDPOINT` and `DT_API_TOKEN` variables.

   * `DT_ENDPOINT` is the Dynatrace API server endpoint. It contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). For example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`. For more details, see [Integrate OneAgent on Azure App Service for Linux and containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.").
   * `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

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

## Data visualization and analysis

### Log analysis

NetFlow data is ingested as log records, which can be queried and visualized using DQL. You can use [![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**ï»¿](https://www.dynatrace.com/hub/detail/logs/) to look for container logs captured by OneAgent for the Collector:

![OpenTelemetry errors displayed in the Logs app](https://dt-cdn.net/images/open-telemetry-errors-2163-955bbf8cf3.png)

Similarly, ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** can help you see that traffic is indeed flowing:

![Traffic flow with NetFlow in the Logs app](https://dt-cdn.net/images/logs-netflow-trafic-flow-2022-d387c3206a.png)

### Dashboards

![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** provides a ready-made **NetFlow Overview** dashboard as an entry point to explore and visualize NetFlow data. It includes pre-configured charts and metrics to analyze network traffic, such as top sources, destinations, conversations, and port usage.

![Dashboards NetFlow Overview](https://dt-cdn.net/images/dashboards-netflow-overview-1619-1e3c5ca7d8.png)

The dashboard can be used as a base for further customizations. You can also create custom dashboards to visualize NetFlow data using various chart types.

### Notebooks

![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** allows you to run queries and visualize NetFlow data interactively. You can open a new notebook from ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** by going to **Open with** and selecting ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

DQL query example

Using this DQL query, you can get a summary of the bytes by destination IP and port:

```
fetch logs



| filter matchesValue(flow.type, "netflow_v9")



| summarize {totalBytes= sum(toLong(flow.io.bytes)),totalPackets=sum(toLong(flow.io.packets))}, by: {destination.address,destination.port}



| sort totalBytes desc



| limit 10
```

![Summary of bytes by destination IP and port in Notebooks](https://dt-cdn.net/images/notebooks-netflow-bytes-by-dest-id-and-port-1310-aa7ceb24fe.png)

## Related topics

* [Ingest NetFlow with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/netflow "Configure the OpenTelemetry Collector to ingest NetFlow data.")