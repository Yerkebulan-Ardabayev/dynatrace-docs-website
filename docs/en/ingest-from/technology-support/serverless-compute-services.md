---
title: Serverless compute support matrix
source: https://www.dynatrace.com/docs/ingest-from/technology-support/serverless-compute-services
scraped: 2026-02-17T04:52:10.147142
---

# Serverless compute support matrix

# Serverless compute support matrix

* Latest Dynatrace
* 13-min read
* Published Jan 27, 2022

This page describes which features and capabilities are available across the various flavors of serverless compute services for functions (FaaS).

Key to columns and cells

#### Columns

| Heading | Description |
| --- | --- |
| Cloud platform metrics and metadata | Dynatrace has an integration with the cloud provider to capture platform-level metrics and metadata. |
| Logs | Dynatrace captures resource and/or application logs. |
| Distributed tracing | Dynatrace supports distributed tracing for these services, either providing a dedicated integration or via OpenTelemetry. |
| Automatic tracing | Dynatrace provides automatic out-of-the-box tracing without code changes. |
| OpenTelemetry/Extend tracing | Dynatrace provides the ability to enhance tracing via [OpenTelemetry](/docs/ingest-from/extend-dynatrace/extend-tracing/opentracing "Learn how to integrate OpenTracing with Dynatrace."), its own [SDKs](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available."), and [custom services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols."). |
| Custom metrics | Dynatrace provides the ability to add custom metrics via [API](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."), [OpenTelemetry](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."), [Spring Micrometerï»¿](https://micrometer.io/docs/registry/dynatrace), and many other means. |
| Automatic RUM | Dynatrace provides out-of-the-box real user monitoring with no code changes required. |
| Agentless RUM | Dynatrace provides an [agentless integration](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") for real user monitoring. |

#### Cells

| Icon | Release | Description |
| --- | --- | --- |
| GA | **GA** | Generally available and fully supported. |
|  | **Preview** | These features are in the final stages of development and are ready to be previewed. Preview features aren't production-ready and they aren't officially supported. |
| Future | **Future** | A feature or technology support that is either on the roadmap or may be considered on-demand. |
| Not planned | **Not planned** | A feature or technology support that Dynatrace does not currently plan to pursue. |
| n/a |  | Not applicable |

### AWS Lambda

#### Classic deployment

Both 64-bit ARM (AWS Graviton2 processors) and 64-bit x86 architectures are supported

Language

[Cloud platform metrics and metadata](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.")

[Logs](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")

Distributed tracing

Automatic tracing

OpenTelemetry  
Extend tracing

Custom metrics

Automatic RUM

Agentless RUM

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

n/a

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

n/a

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

n/a

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[3](#fn-1-3-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[3](#fn-1-3-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

GoLang

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

#### Container images

Both 64-bit ARM (AWS Graviton2 processors) and 64-bit x86 architectures are supported

Language

[Cloud platform metrics and metadata](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.")

[Logs](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")

Distributed tracing

Automatic tracing

OpenTelemetry  
Extend tracing

Custom metrics

Automatic RUM

Agentless RUM

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

n/a

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

n/a

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

n/a

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[3](#fn-1-3-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[3](#fn-1-3-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

GoLang

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

[Requires integration of Dynatrace extension via Dynatrace Lambda Layer](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java."). To learn which runtimes are supported, see [Support lifecycle](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "AWS Lambda capabilities and integration options").

2

[Requires integration of Dynatrace extension on container image](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images "Deploy Dynatrace Lambda Layers when deployed via a container image.")

3

[Trace AWS Lambda .Net Core](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native "Learn how to use OpenTelemetry to trace AWS Lambda .NET Core functions.")

### Azure Functions

#### Windows-based AppService plan or App Service Environment

Language

[Cloud platform metrics and metadata](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")

[Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

Distributed tracing

Automatic tracing

OpenTelemetry  
extend tracing

Custom metrics

Automatic RUM

Agentless RUM

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-2-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

Requires integration of OneAgent via [Dynatrace Site-Extension for Azure App Services](/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace")

#### Linux-based App Service plan or App Service Environment

Language

[Cloud platform metrics and metadata](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")

[Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

Distributed tracing

Automatic tracing

OpenTelemetry  
extend tracing

Custom metrics

Automatic RUM

Agentless RUM

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-3-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

Requires integration of [OneAgent on AppServices for Linux and Containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")

#### Consumption or Premium plan

Language

[Cloud platform metrics and metadata](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")

[Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

Distributed tracing

Automatic tracing

OpenTelemetry  
extend tracing

Custom metrics

Automatic RUM

Agentless RUM

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-4-1-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

[Trace Azure Functions on Azure Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans")

### Runtime v1

Language

Distributed tracing

Automatic tracing

All languages

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Not planned](https://dt-cdn.net/images/icon-not-planned-172a321f5d.svg "Not planned")

### Runtime v2

Language

Distributed tracing

Automatic tracing

.NET Core[1](#fn-5-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-5-2-def)

Other languages

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

1

Functions written in [C# (class libaries), C# script (.csx) and F# (.fsx)ï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details) which are executed in the [in-process modelï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Limited to functions deployed on on AppService-Plan / Appservice-Environment or Kubernetes

### Runtime v3-v4

Language

Distributed tracing

Automatic tracing

.NET Core[1](#fn-6-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-6-2-def)

[.Net Core, Isolated-Processï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

Other languages

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

1

Functions written in [C# (class libaries), C# script (.csx) and F# (.fsx)ï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details) which are executed in the [in-process modelï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Limited to functions deployed on on AppService-Plan / Appservice-Environment or Kubernetes

### Frameworks

#### Durable Functions

Language

Distributed tracing

Automatic tracing

.NET Core

[1](#fn-7-1-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

Other languages

n/a[1](#fn-7-1-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

1

Durable Functions SDK has [preview support for distributed tracingï»¿](https://dt-url.net/qj03vf2) for .NET Core using Application-Insights.

### Google Cloud Functions

Language

[Cloud platform metrics and metadata](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")

[Logs](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")

[Distributed tracing](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Set up monitoring for Google Cloud Functions.")

Automatic tracing

OpenTelemetry  
Extend tracing

Custom metrics

Automatic RUM

Agentless RUM

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

GoLang

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-8-1-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

[Trace Google Functions written in Node.js](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace.")

## Related topics

* [Serverless monitoring](/docs/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [Known solutions and workarounds](/docs/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.")