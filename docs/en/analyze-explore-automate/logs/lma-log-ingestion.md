---
title: Log ingestion
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion
scraped: 2026-02-18T05:35:40.932740
---

# Log ingestion

# Log ingestion

* Latest Dynatrace
* Overview
* 6-min read
* Updated on Oct 15, 2025

Log ingestion is the process of collecting log data from various sources within an infrastructure. The logs are stored in the Grail data lakehouse for analysis, automation, and monitoring. Dynatrace simplifies this process with OneAgent, which automatically discovers logs and offers central management options. In serverless environments or where OneAgent installation isn't possible, the Logs Ingestion API can be used.

Find below an overview of log ingest strategies that you can use with Dynatrace.

[### OneAgent

Recommended

Automatically ingest log data from a wide variety of sources.](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")[### Log ingestion API

Configure Log ingest API integration for your use cases.](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")[![Syslog](https://dt-cdn.net/images/syslog-c85e9ae419.svg "Syslog")

### Syslog ingestion via ActiveGate

Ingest syslog logs.](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.")

### Ingest Kubernetes logs

Dynatrace Log Monitoring enables the collection of logs from Kubernetes container orchestration systems through OneAgent. [Kubernetes logs ingestion via OneAgent](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace.") includes out-of-the-box sensitive data masking, entity linking and preservation of Kubernetes metadata.

You can centrally configure OneAgent ingestion rules across your entire Kubernetes environment. By applying centralized filtering rules, you can ensure that only logs relevant to your use case are ingested, reducing maintenance efforts.

* [Stream Kubernetes logs with OneAgent](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace.")
* [Stream Kubernetes logs with Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.")
* [Stream Kubernetes logs with Dynatrace OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Stream Kubernetes logs with Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.")
* [Stream Kubernetes logs with Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.")

### Export telemetry data with OpenTelemetry

The OpenTelemetry Protocol (OTLP) is the principal network protocol for the exchange of telemetry data between OpenTelemetry-backed services and applications.

Dynatrace provides native OTLP endpoints with the following services:

* The SaaS platform
* ActiveGate instances
* OneAgent setups

Additionally, you can deploy the Collector as intermediary service application, to batch requests and improve network performance or transform requests before forwarding them to Dynatrace (for example, mask sensitive data).

* [OpenTelemetry Export with OTLP](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Forward log data from cloud platforms

[Cloud log forwarding](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.") allows the streaming of log data from various cloud platforms directly into Dynatrace. The following integrations are available:

### AWS

Use Amazon Data Firehose integration, Amazon S3 forwarder, and direct AWS Lambda integration for cost-optimized flow logs setup with Dynatrace.

* [Stream logs via Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [Stream logs from AWS S3](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding#s3-log-ingestion "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.")
* [Collect logs from AWS Lambda functions](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector "Collect logs from AWS Lambda functions")

### Azure

Stream logs from Azure Event Hubs into Dynatrace through the Azure Function App instance. Azure resource logs and activity logs are supported. Dynatrace purchased via Azure Marketplace comes with deep Azure platform logs integration. It offers streamlined configuration via Azure Portal, and simplifies financial settlements.

* [Stream Azure logs from Azure Event Hubs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")
* [Logs via Azure Native Dynatrace Service](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")

### GCP

Create a Pub/Sub subscription to facilitate the ingestion of metrics, logs, dashboards, and alerts into Dynatrace. This provides a comprehensive view of your Google Cloud Platform health, including resource and audit logs.

* [Set up the Dynatrace GCP metric and log integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

### Stream log data with log shippers

A log shipper is a versatile component that can be seamlessly integrated into the API to collect logs from various sources and forward them to designated destinations. The links below illustrate supported configurations, showcasing how various log shippers can be tailored to meet different deployment needs.

* [Stream logs with Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace.")
* [Stream logs with Fluentd on Kubernetes](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.")
* [Stream logs with Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace.")

### Stream Logs with Cribl

You can send logs, metrics and traces to Dynatrace using Cribl Streamâ¢ via OpenTelemetry Protocol (OTLP) or only logs using Cribl Streamâ¢ via Dynatrace HTTP destination that integrates with Log ingestion API.

* [Stream logs with Cribl](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-cribl "How to send logs, metrics, and traces from Cribl Stream to Dynatrace using OTLP or HTTP integration.")

### Push logs with Cloudflare

Use Cloudflare Logpush to push logs directly to Dynatrace.
Configure Logpush either via the Clouflare dashboard or the API.

* [Push logs with Cloudflare](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-push-logs-with-cloudflare "How to use Cloudflare Logpush to push logs directly to Dynatrace.")

### Integrations via Dynatrace Hub

Dynatrace Hub is a marketplace for Dynatrace extensions, integrations, and add-ons. It provides a wide range of pre-built solutions to enhance your Dynatrace experience. You can find various log management and analytics integrations in the Dynatrace Hub.

* [Dynatrace Hub (Log Management and Analytics)ï»¿](https://www.dynatrace.com/hub/?filter=log-management-and-analytics)

### Ingest via Dynatrace Extensions

Logs are observability data that [Dynatrace Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") collect and forward to Grail together with other monitoring signals to deliver a holistic view of your technology. [Extensions](/docs/ingest-from/extend-dynatrace/extend-logs "Learn how to extend log observability in Dynatrace.") expand observability data and analytics capabilities, streamlining data configuration and integration with third-party systems.

![log-extensions](https://dt-cdn.net/images/log-extensions-1980-76d7fc4317.png)

You can use the local `http://localhost:<port>/v2/logs/ingest` API endpoint to push locally retrieved logs to Dynatrace over a secure and authenticated channel. Learn more by accessing the [Extensions](/docs/ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api "Use the Dynatrace API to push locally retrieved logs to Dynatrace.") page.

## Related topics

* [Log ingestion via OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")
* [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.")
* [OneAgent log ingest API](/docs/ingest-from/extend-dynatrace/extend-logs/oneagent-log-ingest-api "Use the Dynatrace API to push locally retrieved logs to Dynatrace.")
* [Explore Log Management and Analytics in Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?filter=log-management-and-analytics&internal_source=doc&internal_medium=link&internal_campaign=cross)
* [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.")