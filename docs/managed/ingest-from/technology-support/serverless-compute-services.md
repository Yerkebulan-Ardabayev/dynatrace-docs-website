---
title: Serverless compute support matrix
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/serverless-compute-services
---

# Serverless compute support matrix

# Serverless compute support matrix

* 13-min read
* Updated on Jan 12, 2026

This page describes which features and capabilities are available across the various flavors of serverless compute services for functions (FaaS).

Key to columns and cells

#### Columns

| Heading | Description |
| --- | --- |
| Cloud platform metrics and metadata | Dynatrace has an integration with the cloud provider to capture platform-level metrics and metadata. |
| Logs | Dynatrace captures resource and/or application logs. |
| Distributed tracing | Dynatrace supports distributed tracing for these services, either providing a dedicated integration or via OpenTelemetry. |
| Automatic tracing | Dynatrace provides automatic out-of-the-box tracing without code changes. |
| OpenTelemetry/Extend tracing | Dynatrace provides the ability to enhance tracing via [OpenTelemetry](/managed/ingest-from/extend-dynatrace/extend-tracing/opentracing "Learn how to integrate OpenTracing with Dynatrace."), its own [SDKs](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available."), and [custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols."). |
| Custom metrics | Dynatrace provides the ability to add custom metrics via [API](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."), [OpenTelemetry](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."), [Spring Micrometer﻿](https://micrometer.io/docs/registry/dynatrace), and many other means. |
| Automatic RUM | Dynatrace provides out-of-the-box real user monitoring with no code changes required. |
| Agentless RUM | Dynatrace provides an [agentless integration](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") for real user monitoring. |

#### Cells

| Icon | Release | Description |
| --- | --- | --- |
| GA | **GA** | Generally available and fully supported. |
|  | **Preview** | These features are in the final stages of development and are ready to be previewed. Preview features aren't production-ready and they aren't officially supported. |
| Future | **Future** | A feature or technology support that is either on the roadmap or may be considered on-demand. |
| Not planned | **Not planned** | A feature or technology support that Dynatrace does not currently plan to pursue. |
| n/a |  | Not applicable |

## AWS Lambda

### Classic deployment

Both 64-bit ARM (AWS Graviton2 processors) and 64-bit x86 architectures are supported

| Language | [Cloud platform metrics and metadata](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.") | [Logs](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.") | Distributed tracing | Automatic tracing | OpenTelemetry Extend tracing | Custom metrics | Automatic RUM | Agentless RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python | GA | GA | GA | GA[1](#fn-1-1-def) | GA | GA | GA[1](#fn-1-1-def) | n/a |
| Java | GA | GA | GA | GA[2](#fn-1-2-def) | GA | GA | GA[1](#fn-1-1-def) | n/a |
| Node.js | GA | GA | GA | GA[1](#fn-1-1-def) | GA | GA | GA[1](#fn-1-1-def) | n/a |
| .NET Core | GA | GA | GA[3](#fn-1-3-def) | Future | GA[3](#fn-1-3-def) | GA | Future | GA |
| GoLang | GA | GA | GA | Future | GA | GA | Future | GA |

### Container images

Both 64-bit ARM (AWS Graviton2 processors) and 64-bit x86 architectures are supported

| Language | [Cloud platform metrics and metadata](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.") | [Logs](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.") | Distributed tracing | Automatic tracing | OpenTelemetry Extend tracing | Custom metrics | Automatic RUM | Agentless RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python | GA | GA | GA | GA[2](#fn-1-2-def) | GA | GA | GA[2](#fn-1-2-def) | n/a |
| Java | GA | GA | GA | GA[2](#fn-1-2-def) | GA | GA | GA[2](#fn-1-2-def) | n/a |
| Node.js | GA | GA | GA | GA[2](#fn-1-2-def) | GA | GA | GA[2](#fn-1-2-def) | n/a |
| .NET Core | GA | GA | GA[3](#fn-1-3-def) | Future | GA[3](#fn-1-3-def) | GA | Future | GA |
| GoLang | GA | GA | GA | Future | GA | GA | Future | GA |

1

[Requires integration of Dynatrace extension via Dynatrace Lambda Layer](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java."). To learn which runtimes are supported, see [Support lifecycle](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#supported-versions "AWS Lambda capabilities and integration options").

2

[Requires integration of Dynatrace extension on container image](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images "Deploy Dynatrace Lambda Layers when deployed via a container image.")

3

[Trace AWS Lambda .Net Core](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native "Learn how to use OpenTelemetry to trace AWS Lambda .NET Core functions.")

## Azure Functions

Durable Functions aren't supported.

### Windows-based

| Language | [Cloud platform metrics and metadata](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.") | [Logs](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.") | Distributed tracing | [Automatic tracing](/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") | OpenTelemetry extend tracing | Infrastructure monitoring | Custom metrics | Automatic RUM | Agentless RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .NET Core | GA | GA | GA | GA[1](#fn-2-1-def) | GA | n/a | GA | Future | GA |
| Java | GA | GA | GA | OneAgent version 1.343+ | GA | OneAgent version 1.343+[7](#fn-2-7-def) | GA | Future | GA |
| Node.js | GA | GA | GA | OneAgent version 1.343+ | GA | OneAgent version 1.343+[7](#fn-2-7-def) | GA | Future | GA |
| Python | GA | GA | GA | n/a | GA | n/a | GA | Future | GA |

### Linux-based

| Language | [Cloud platform metrics and metadata](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.") | [Logs](/managed/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.") | Distributed tracing | Automatic tracing | OpenTelemetry extend tracing | Infrastructure monitoring | Custom metrics | Automatic RUM | Agentless RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| .NET Core | GA | GA | GA | GA[5](#fn-2-5-def) | GA | n/a | GA | Future | GA |
| Java | GA | GA | GA | Future | GA | Future[7](#fn-2-7-def) | GA | Future | GA |
| Node.js | GA | GA | GA | Future | GA | Future[7](#fn-2-7-def) | GA | Future | GA |
| Python | GA | GA | GA | OneAgent version 1.343+[6](#fn-2-6-def) | GA | Future[7](#fn-2-7-def) | GA | Future | GA |

5

Requires integration of [OneAgent on AppServices for Linux and Containers](/managed/ingest-from/microsoft-azure-services/integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")

6

For Flex Consumption only.

7

For Dedicated plan only.

### Trigger support

For Azure Functions runtime v4, only the following triggers are supported.

Output bindings are only supported for HTTP triggers.

| Trigger | Java | Node.js | Python |
| --- | --- | --- | --- |
| [HTTP and webhooks﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook) | GA | GA | GA |
| [Service Bus﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus) | GA | GA | GA |
| [Event Hubs﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-hubs) | GA | GA | GA |
| [Timer﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer) | GA | GA | GA |
| [Blob Storage﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cextensionv5&pivots=programming-language-python) | Future | Future | GA |
| [Event Grid﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-trigger?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cextensionv3&pivots=programming-language-python) | Future | Future | GA |
| [Azure SQL﻿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-azure-sql-trigger?tabs=isolated-process%2Cpython-v2%2Cportal&pivots=programming-language-python) | Future | Future | GA |

## Google Cloud Functions

| Language | [Cloud platform metrics and metadata](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.") | [Logs](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.") | [Distributed tracing](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Set up monitoring for Google Cloud Functions.") | Automatic tracing | OpenTelemetry Extend tracing | Custom metrics | Automatic RUM | Agentless RUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python | GA | GA | GA | Future | GA | GA | Future | GA |
| GoLang | GA | GA | GA | Future | GA | GA | Future | GA |
| .NET Core | GA | GA | GA | Future | GA | GA | Future | GA |
| Java | GA | GA | GA | Future | GA | GA | Future | GA |
| Node.js | GA | GA | GA[1](#fn-3-1-def) | Future | GA | GA | Future | GA |

1

[Trace Google Functions written in Node.js](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace.")

## Related topics

* [Serverless monitoring](/managed/discover-dynatrace/get-started/serverless-monitoring "Monitor serverless cloud services across AWS, Azure, and Google Cloud with Dynatrace for end-to-end visibility and AI-powered analysis.")
* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Technology support](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [Known solutions and workarounds](/managed/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.")