---
title: Monitor Azure Functions on Consumption Plans
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans
scraped: 2026-02-19T21:22:23.579410
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

[Trace Azure Functions written in .NET](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace.")

[Trace Azure Functions written in Node.js](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Monitor Azure Functions with OpenTelemetry for Node.js and Dynatrace.")

[Trace Azure Functions written in Python](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Monitor Azure Functions with OpenTelemetry for Python and Dynatrace.")

## Monitoring Consumption

For Azure Functions, monitoring consumption is based on Davis data units. See [Serverless monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated.") for details.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")