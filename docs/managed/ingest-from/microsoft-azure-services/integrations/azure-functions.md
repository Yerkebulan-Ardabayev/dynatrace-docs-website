---
title: Monitor Azure Functions
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/integrations/azure-functions
---

# Monitor Azure Functions

# Monitor Azure Functions

* Overview
* 1-min read
* Published Apr 20, 2022

Azure Functions offers a wide range of options to address various Azure Functions [scenarios and use-cases﻿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview#scenarios):

* Use your preferred language
* Automate deployment
* Take advantage of flexible [hosting﻿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale)

## Capabilities

The Dynatrace platform provides extensive monitoring capabilities:

* Automatic instrumentation for Azure Functions in Python, Node.js, and Java
* End-to-end tracing including Function triggers for HTTP, webhooks, and Azure services such as [Service Bus](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-bus-builtin "Monitor Azure Service Bus and view available metrics."), [Event Hubs](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-hubs "Monitor Azure Event Hubs Clusters and view available metrics.").
* Broad distributed tracing for many frameworks, including Azure SDK.
* Automatic enrichment of application logs for logs in context of traces.
* Capturing platform metrics and logs (Azure Cloud Platform Monitoring).

For more details, refer to [supported triggers](/managed/ingest-from/technology-support/serverless-compute-services "Learn which features and capabilities Dynatrace supports for serverless compute services for functions (FaaS).") and [framework support](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## OneAgent modes by hosting plan

OneAgent adapts its operating mode to your Azure Functions hosting plan.

### Serverless plans

On Consumption, Flex Consumption, and Premium plans, OneAgent uses an optimized, low-overhead mode purpose-built for short-lived, stateless, consumption-based environments. It offers fast startup, is scale-to-zero compatible, and is licensed to match serverless usage patterns.

Because serverless instances are ephemeral and don't expose persistent process or container infrastructure, some full-stack capabilities don't apply in serverless mode:

* Remote configuration from the Dynatrace UI (for example, feature flags)
* Infrastructure monitoring at the process and container level
* Profiling, LiveDebugging, Application Security, and BizEvents

### Dedicated plan

OneAgent runs in full-stack mode.

## Enable monitoring

How you integrate OneAgent depends on the operating system of your Function App.

### Windows

Azure Functions provides a native Site Extension mechanism. Install the [Dynatrace OneAgent site extension](/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") to start monitoring. No changes to your function code are required.

### Linux

Azure Functions on Linux has no native extension point. Instead, OneAgent ships as a runtime-specific deployment package (PyPI for Python, npm for Node.js, NuGet for .NET) that you add as a dependency to your function project. OneAgent is deployed alongside your function automatically. No changes to your function code are required.

Choose a guide that matches your setup:

[#### Monitor Azure Functions on Plans for Windows

Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.

* How-to guide

Read this guide](/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/integrate-oneagent-on-azure-functions)[#### Monitor Azure Functions on Linux plans

Learn how to enable OneAgent monitoring for Azure Functions on Linux hosting plans, including runtime setup, environment variables, and package deployment.

* How-to guide

Read this guide](/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/azure-function-linux)

## Related topics

* [Serverless monitoring](/managed/discover-dynatrace/get-started/serverless-monitoring "Monitor serverless cloud services across AWS, Azure, and Google Cloud with Dynatrace for end-to-end visibility and AI-powered analysis.")