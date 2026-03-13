---
title: Monitor Azure Functions on Consumption Plans
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans
scraped: 2026-03-06T21:26:24.559248
---

# Monitor Azure Functions on Consumption Plans

# Monitor Azure Functions on Consumption Plans

* Latest Dynatrace
* Overview
* 1-min read
* Published Apr 20, 2022

Azure Functions let you run code without provisioning or managing servers.
This deployment model is sometimes referred to as "serverless" or "Function as a Service" (FaaS).

* An Azure Function runs in an application on a container managed by Azure. This lets you focus on writing code without worrying about the underlying application or infrastructure.
* Azure Functions are ephemeral. This means that the underlying container can be suspended or recycled when thereâs no request pending.

## Integration

[Trace Azure Functions written in .NET](func-dynamic-plans/opentelemetry-on-azure-functions-dotnet.md "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace.")

[Trace Azure Functions written in Node.js](func-dynamic-plans/opentelemetry-on-azure-functions-nodejs.md "Monitor Azure Functions with OpenTelemetry for Node.js and Dynatrace.")

[Trace Azure Functions written in Python](func-dynamic-plans/opentelemetry-on-azure-functions-python.md "Monitor Azure Functions with OpenTelemetry for Python and Dynatrace.")

## Monitoring Consumption

For Azure Functions, monitoring consumption is based on Davis data units. See [Serverless monitoring](../../../../license/monitoring-consumption-classic/davis-data-units/serverless-monitoring.md "Understand how serverless monitoring consumption is calculated.") for details.

## Related topics

* [Set up Dynatrace on Microsoft Azure](../../../microsoft-azure-services.md "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](../../../technology-support/oneagent-platform-and-capability-support-matrix.md "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](func-dynamic-plans/opentelemetry-on-azure-functions.md "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")