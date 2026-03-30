---
title: DDUs for custom traces (Trace API)
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/custom-traces
scraped: 2026-03-06T21:37:37.198226
---

# DDUs for custom traces (Trace API)


* Classic
* 2-min read
* Published Mar 30, 2021

While there are no additional costs or licensing involved in the integration of OpenTracing and OpenTelemetry span data into Dynatrace via OneAgent, you have the option to configure the Dynatrace Trace API to ingest OpenTelemetry and OpenTracing spans; these are known as "custom traces." This approach is useful for seamlessly integrating OpenTelemetry trace data that's emitted by third-party services. Ingestion of spans via the Trace API endpoint consumes Davis data units.") because this approach requires more processing and analytical power than ingestion via OneAgent.

For details on OneAgent-based ingestion of OpenTelemetry and OpenTracing spans, which does not consume DDUs, see OneAgent OpenTracing and OpenTelemetry support.

## DDU consumption for custom trace ingestion

While a trace may contain spans captured with OneAgent and the Dynatrace Trace API, only spans that are ingested via the Dynatrace Trace API consume DDUs. For an API service that is instrumented with OpenTelemetry and spans are captured via OneAgent, no DDUs are consumed. Custom traces ingested via the Dynatrace Trace API are licensed on the basis of ingestion of spans (each span equates to a single operation within a trace).

### DDU consumption example

To calculate the DDU consumption for custom traces, multiply the total number of invocations by the total number of spans times the DDU weight, for the measured time period. Consider an API service that's instrumented with OpenTelemetry that ingests on average 10 spans per API call via the Dynatrace Trace API. If the average number of API calls per month is 1 million, the monthly DDU consumption is 7,000 DDUs (`1,000,000 invocations Ã 10 spans Ã .0007 DDUs = 7,000 DDUs`), with an annual equivalent of 84,000 DDUs (`7,000 DDUs Ã 12 months = 84,000 DDUs`).

Davis data unit pools

Davis data units pools for traces.") allow you to set hard limits on your DDU consumption for traces. Go to **Settings** > **Consumption** > **Davis data units pools** and turn on **Enable limit** in the **Traces** section to set an annual or monthly limit.

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)
* License Dynatrace, the licensing model for all Dynatrace capabilities.")
* Extending Dynatrace (Davis data units).")
* DDUs for metrics
* Extend metric observability