---
title: Serverless compute support matrix
source: https://www.dynatrace.com/docs/ingest-from/technology-support/serverless-compute-services
scraped: 2026-03-06T21:29:10.840259
---

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
| OpenTelemetry/Extend tracing | Dynatrace provides the ability to enhance tracing via OpenTelemetry, its own SDKs, and custom services for custom services that don't use standard protocols."). |
| Custom metrics | Dynatrace provides the ability to add custom metrics via API, OpenTelemetry into Dynatrace."), [Spring Micrometerï»¿](https://micrometer.io/docs/registry/dynatrace), and many other means. |
| Automatic RUM | Dynatrace provides out-of-the-box real user monitoring with no code changes required. |
| Agentless RUM | Dynatrace provides an agentless integration for real user monitoring. |

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

Requires integration of Dynatrace extension via Dynatrace Lambda Layer. To learn which runtimes are supported, see [Support lifecycle](../amazon-web-services/integrate-into-aws/aws-lambda-integration.md#support-lifecycle "AWS Lambda capabilities and integration options").

2

Requires integration of Dynatrace extension on container image

3

Trace AWS Lambda .Net Core

### Azure Functions

#### Windows-based AppService plan or App Service Environment

1

Requires integration of OneAgent via Dynatrace Site-Extension for Azure App Services

#### Linux-based App Service plan or App Service Environment

1

Requires integration of OneAgent on AppServices for Linux and Containers

#### Consumption or Premium plan

1

Trace Azure Functions on Azure Consumption Plan

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

Trace Google Functions written in Node.js

## Related topics

* Serverless monitoring
* OneAgent platform and capability support matrix
* Technology support
* Known solutions and workarounds