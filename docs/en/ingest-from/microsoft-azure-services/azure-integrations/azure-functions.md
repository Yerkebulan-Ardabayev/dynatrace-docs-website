---
title: Monitor Azure Functions using Azure App Service (built-in)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions
scraped: 2026-03-06T21:18:25.804495
---

# Monitor Azure Functions using Azure App Service (built-in)


* Latest Dynatrace
* How-to guide
* 1-min read
* Published Apr 20, 2022

Azure Functions offers a wide range of options to address various Azure Functions [scenarios and use-casesï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview#scenarios):

* Use your preferred language
* Automate deployment
* Take advantage of flexible [hostingï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-scale)

## Distributed Tracing

With the different options for hosting your functions, Dynatrace provides you with the best options to enable distributed tracing.

* Dynatrace offers an easy integration for **Azure Functions running on Appservice- (Dedicated) plan** using a site extension.
* Tracing Azure Functions on a **Consumption- or Premium-Plan** comes with additional restrictions by the nature of a serverless service, such as using instrumentation agents to fully automatically instrument your code at runtime.

Dynatrace provides distributed tracing for these sandboxed environments based on [OpenTelemetryï»¿](https://opentelemetry.io/). If you already use OpenTelemetry to instrument your functions, you can ingest the trace data using Dynatrace Trace Ingest API, but we recommend that you use the Dynatrace exporter, which adds additional benefits to fully leverage the automatic AI-based analysis capabilities of Dynatrace.

To make using OpenTelemetry easier, Dynatrace provides library packages for Azure Functions to reduce necessary OpenTelemetry boiler-plate code for trace-propagation, applying resource attributes and initialization code as well as aligning with semantic conventions.

By using advanced concepts such as [aspect-oriented programming (AOP)ï»¿](https://en.wikipedia.org/wiki/Aspect-oriented_programming), it is even possible to add fully automatic instrumentation without changing a single line of code, as demonstrated within this community github-project for [Azure Functions .NETï»¿](https://github.com/dtPaTh/Azure.Functions.Tracing).

## Additional visibility using logs and platform metrics

To enhance visibility for monitoring your Azure Functions health, we recommend that you enable capturing service metrics from Azure Monitor as well as ingesting logs.

![Azure Function Service](https://dt-cdn.net/images/azure-function-service-1397-ee1fed5f77.png)

## Related topics

* Serverless monitoring