---
title: DDUs for custom traces (Trace API)
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/custom-traces
scraped: 2026-02-18T21:32:55.081102
---

# DDUs for custom traces (Trace API)

# DDUs for custom traces (Trace API)

* 2-min read
* Published Mar 30, 2021

While there are no additional costs or licensing involved in the integration of OpenTracing and OpenTelemetry span data into Dynatrace via OneAgent, you have the option to configure the Dynatrace Trace API to ingest OpenTelemetry and OpenTracing spans; these are known as "custom traces." This approach is useful for seamlessly integrating OpenTelemetry trace data that's emitted by third-party services. Ingestion of spans via the Trace API endpoint consumes [Davis data units](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") because this approach requires more processing and analytical power than ingestion via OneAgent.

For details on OneAgent-based ingestion of OpenTelemetry and OpenTracing spans, which does not consume DDUs, see [OneAgent OpenTracing and OpenTelemetry support](/docs/ingest-from/extend-dynatrace/extend-tracing/opentracing "Learn how to integrate OpenTracing with Dynatrace.").

## DDU consumption for custom trace ingestion

While a trace may contain spans captured with OneAgent and the Dynatrace Trace API, only spans that are ingested via the Dynatrace Trace API consume DDUs. For an API service that is instrumented with OpenTelemetry and spans are captured via OneAgent, no DDUs are consumed. Custom traces ingested via the Dynatrace Trace API are licensed on the basis of ingestion of spans (each span equates to a single operation within a trace).

### DDU consumption example

To calculate the DDU consumption for custom traces, multiply the total number of invocations by the total number of spans times the DDU weight, for the measured time period. Consider an API service that's instrumented with OpenTelemetry that ingests on average 10 spans per API call via the Dynatrace Trace API. If the average number of API calls per month is 1 million, the monthly DDU consumption is 7,000 DDUs (`1,000,000 invocations Ã 10 spans Ã .0007 DDUs = 7,000 DDUs`), with an annual equivalent of 84,000 DDUs (`7,000 DDUs Ã 12 months = 84,000 DDUs`).

Davis data unit pools

[Davis data units pools for traces](/docs/license/monitoring-consumption-classic/davis-data-units#ddu-pools "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") allow you to set hard limits on your DDU consumption for traces. Go to **Settings** > **Consumption** > **Davis data units pools** and turn on **Enable limit** in the **Traces** section to set an annual or monthly limit.

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [DDUs for metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.")
* [Extend metric observability](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")