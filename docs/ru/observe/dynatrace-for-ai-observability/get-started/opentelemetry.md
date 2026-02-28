---
title: Get started with OpenTelemetry and AI Observability
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started/opentelemetry
scraped: 2026-02-28T21:33:14.049265
---

# Get started with OpenTelemetry and AI Observability

# Get started with OpenTelemetry and AI Observability

* Latest Dynatrace
* Getting started guide
* 5-min read
* Updated on Feb 25, 2026

OpenTelemetry provides a vendor-neutral standard for collecting traces and metrics from AI applications. With the [GenAI semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/), OpenTelemetry defines a consistent way to capture AI-specific attributes such as model names, token counts, latency, and cost metrics across different LLM providers.

Dynatrace fully supports OpenTelemetry, allowing you to send AI observability data directly to your Dynatrace environment using the [OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). This approach gives you flexibility to use any OpenTelemetry-compatible instrumentation library or build custom instrumentation.

## Who is this for?

This getting started guide is for:

* AI engineering teams building agent and LLM powered applications and services.
* Site Reliability Engineers responsible for monitoring AI workloads on hyperscalers.
* Platform engineers integrating OTel data into Dynatrace.

## What will you learn?

By following this guide, you will learn:

* How to set up OpenTelemetry and get trace- and log-level visibility into your AI apps.
* How to configure and instrument your app with OTel.
* How to configure OTLP exports to Dynatrace.
* How to report attributes following GenAI semantic conventions.
* What traces and metrics can be sent to Dynatrace.
* How to achieve trace- and token-level visibility into Agent and LLM operations.

## Before you begin

### Prerequisites

In order for this to work, you need to have:

* A running AI app or AI demo app.
* Dynatrace SaaS with a [Dynatrace Platform Subscription (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") license that has [Traces powered by Grail](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model."), [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model."), and [Log Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.") enabled.
* OTLP ingestion enabled, see [OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").
* An OpenAPI platform API key.
* A Dynatrace API token the following scopes, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").

  + Ingest metrics (`metrics.ingest`)
  + Ingest logs (`logs.ingest`)
  + Ingest OpenTelemetry traces (`openTelemetryTrace.ingest`)

### Prior knowledge

It's helpful to have some basic knowledge of:

* Python or Node.js.
* OTel concepts like SDKs, spans, exporters, and collectors.
* Dynatrace permissions and data ingestion.

## Get started with AI and OpenTelemetry

### 1. Instrument your application for OpenTelemetry

You can use Python or Node.js to instrument your AI application directly with the OpenTelemetry SDK.

Python

Node.js

1. Install the OpenTelemetry SDK and Collector Exporter.
   Run the following command in your terminal.

   ```
   pip install opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
   ```
2. Optional You can also run the OpenTelemetry auto-instrumentation.

   ```
   pip install opentelemetry-distro opentelemetry-exporter-otlp



   opentelemetry-bootstrap -a install
   ```
3. Initialize the OpenTelemetry SDK.
   Add the following code at the beginning of your main file.

   ```
   from opentelemetry import trace



   from opentelemetry.sdk.resources import Resource



   from opentelemetry.sdk.trace import TracerProvider



   from opentelemetry.sdk.trace.export import BatchSpanProcessor



   from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter



   resource = Resource.create({"service.name": "<your-service>"})



   provider = TracerProvider(resource=resource)



   trace.set_tracer_provider(provider)



   exporter = OTLPSpanExporter(



   endpoint="https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp/v1/traces",



   headers={"Authorization": "Api-Token <YOUR_DT_API_TOKEN>"},



   )



   provider.add_span_processor(BatchSpanProcessor(exporter))



   tracer = trace.get_tracer(__name__)
   ```

1. Install the OpenTelemetry SDK, API, and Collector Exporter.
   Run the following command in your terminal.

   ```
   npm install @opentelemetry/sdk-node @opentelemetry/api @opentelemetry/exporter-trace-otlp-proto
   ```
2. Initialize the OpenTelemetry SDK.
   Add the following code at the beginning of your main file.

   ```
   import { NodeSDK } from '@opentelemetry/sdk-node';



   import { Resource } from '@opentelemetry/resources';



   import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-proto';



   import { trace } from '@opentelemetry/api';



   const sdk = new NodeSDK({



   resource: new Resource({ 'service.name': '<your-service>' }),



   traceExporter: new OTLPTraceExporter({



   url: 'https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp/v1/traces',



   headers: { Authorization: 'Api-Token <YOUR_DT_API_TOKEN>' },



   }),



   });



   sdk.start();



   const tracer = trace.getTracer('my-tracer');
   ```

### 2. Add GenAI attributes to your spans

The OpenTelemetry GenAI semantic conventions standardize the attributes captured for generative AI operations.
To make sure that your telemetry data follows these conventions, add the following code to your application.

For more information about semantic conventions, see [GenAI semantic conventions](/docs/observe/dynatrace-for-ai-observability/terms-and-concepts#semantic-conventions "Learn how to combine Dynatrace and Traceloop OpenLLMetry to observe an AI/ML model through OpenTelemetry.").

Python

Node.js

```
from opentelemetry.trace import SpanKind



with tracer.start_as_current_span("chat gpt-5", kind=SpanKind.CLIENT) as span:



span.set_attribute("gen_ai.operation.name", "chat")



span.set_attribute("gen_ai.provider.name", "openai")



span.set_attribute("gen_ai.request.model", "gpt-5.2")



span.set_attribute("gen_ai.request.temperature", 0.7)



response = openai_client.chat.completions.create(



model="gpt-4",



messages=messages,



temperature=0.7,



)



span.set_attribute("gen_ai.response.model", response.model)



span.set_attribute("gen_ai.response.id", response.id)



span.set_attribute("gen_ai.usage.input_tokens", response.usage.prompt_tokens)



span.set_attribute("gen_ai.usage.output_tokens", response.usage.completion_tokens)
```

```
import { SpanKind } from '@opentelemetry/api';



tracer.startActiveSpan('chat gpt-4', { kind: SpanKind.CLIENT }, async (span) => {



span.setAttribute('gen_ai.operation.name', 'chat');



span.setAttribute('gen_ai.provider.name', 'openai');



span.setAttribute('gen_ai.request.model', 'gpt-5.2');



span.setAttribute('gen_ai.request.temperature', 0.7);



const response = await openai.chat.completions.create({



model: 'gpt-4',



messages: messages,



temperature: 0.7,



});



span.setAttribute('gen_ai.response.model', response.model);



span.setAttribute('gen_ai.response.id', response.id);



span.setAttribute('gen_ai.usage.input_tokens', response.usage.prompt_tokens);



span.setAttribute('gen_ai.usage.output_tokens', response.usage.completion_tokens);



span.end();



});
```

## Congratulations!

Now that you've set up your AI app to send observability data directly to Dynatrace, you can:

* Explore the [AI Observability app](/docs/observe/dynatrace-for-ai-observability/ai-observability-app "Use the new AI Observability app to monitor all your AI workloads.") to visualize your AI workloads.
* Check out the [sample applicationsï»¿](https://github.com/dynatrace-oss/dynatrace-ai-agent-instrumentation-examples) for more examples.