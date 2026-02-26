---
title: Serverless compute support matrix
source: https://www.dynatrace.com/docs/ingest-from/technology-support/serverless-compute-services
scraped: 2026-02-26T21:29:37.762851
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

#### Container images

Both 64-bit ARM (AWS Graviton2 processors) and 64-bit x86 architectures are supported

1

[Requires integration of Dynatrace extension via Dynatrace Lambda Layer](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java."). To learn which runtimes are supported, see [Support lifecycle](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "AWS Lambda capabilities and integration options").

2

[Requires integration of Dynatrace extension on container image](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images "Deploy Dynatrace Lambda Layers when deployed via a container image.")

3

[Trace AWS Lambda .Net Core](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native "Learn how to use OpenTelemetry to trace AWS Lambda .NET Core functions.")

### Azure Functions

#### Windows-based AppService plan or App Service Environment

1

Requires integration of OneAgent via [Dynatrace Site-Extension for Azure App Services](/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace")

#### Linux-based App Service plan or App Service Environment

1

Requires integration of [OneAgent on AppServices for Linux and Containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")

#### Consumption or Premium plan

1

[Trace Azure Functions on Azure Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans")

### Runtime v1

### Runtime v2

1

Functions written in [C# (class libaries), C# script (.csx) and F# (.fsx)ï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details) which are executed in the [in-process modelï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Limited to functions deployed on on AppService-Plan / Appservice-Environment or Kubernetes

### Runtime v3-v4

1

Functions written in [C# (class libaries), C# script (.csx) and F# (.fsx)ï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details) which are executed in the [in-process modelï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Limited to functions deployed on on AppService-Plan / Appservice-Environment or Kubernetes

### Frameworks

#### Durable Functions

1

Durable Functions SDK has [preview support for distributed tracingï»¿](https://dt-url.net/qj03vf2) for .NET Core using Application-Insights.

### Google Cloud Functions

1

[Trace Google Functions written in Node.js](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace.")

## Related topics

* [Serverless monitoring](/docs/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [Known solutions and workarounds](/docs/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.")