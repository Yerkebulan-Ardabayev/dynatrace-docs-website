---
title: OpenTelemetry
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started/opentelemetry
scraped: 2026-02-24T21:20:10.679379
---

# OpenTelemetry

# OpenTelemetry

* Latest Dynatrace
* Explanation
* 5-min read
* Published Feb 02, 2026

OpenTelemetry provides a vendor-neutral standard for collecting traces, metrics, and logs from AI applications. With the [GenAI semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/), OpenTelemetry defines a consistent way to capture AI-specific attributes such as model names, token counts, latency, and cost metrics across different LLM providers.

Dynatrace fully supports OpenTelemetry, allowing you to send AI observability data directly to your Dynatrace environment using the [OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). This approach gives you flexibility to use any OpenTelemetry-compatible instrumentation library or build custom instrumentation.

## Instrument your AI application

You can use Python or Node.js to instrument your AI application directly with the OpenTelemetry SDK.

Python

Node.js

Install the required packages:

```
pip install opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
```

The Dynatrace backend works exclusively with delta values and [requires the respective aggregation temporality](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."). Set the `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` environment variable to `DELTA`.

Configure the OpenTelemetry SDK:

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

Add GenAI attributes to your spans:

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

Install the required packages:

```
npm install @opentelemetry/sdk-node @opentelemetry/api @opentelemetry/exporter-trace-otlp-proto
```

Configure the OpenTelemetry SDK:

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

Add GenAI attributes to your spans:

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

## GenAI semantic conventions

The [OpenTelemetry GenAI semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/) standardize the attributes captured for generative AI operations.

### Common attributes

| Attribute | Description | Example |
| --- | --- | --- |
| `gen_ai.operation.name` | The name of the operation being performed | `chat`, `embeddings`, `invoke_agent` |
| `gen_ai.provider.name` | The GenAI provider | `openai`, `anthropic`, `aws.bedrock` |
| `gen_ai.request.model` | The model used for the request | `gpt-5.2` |
| `gen_ai.response.model` | The model that generated the response | `gpt-5.2-0613` |
| `gen_ai.usage.input_tokens` | Number of tokens in the prompt | `100` |
| `gen_ai.usage.output_tokens` | Number of tokens in the completion | `180` |
| `gen_ai.request.max_tokens` | Maximum tokens requested | `100` |
| `gen_ai.response.id` | The unique identifier for the completion | `chatcmpl-123` |
| `gen_ai.response.finish_reasons` | Reasons the model stopped generating | `["stop"]` |
| `gen_ai.conversation.id` | Unique identifier for the conversation | `conv_5j66UpCpwteGg4YSxUnt7lPY` |
| `gen_ai.request.temperature` | Temperature parameter for the request | `0.7` |
| `gen_ai.request.top_p` | The top\_p sampling setting | `1.0` |

### Metrics

OpenTelemetry defines standard metrics for GenAI operations:

| Metric | Description |
| --- | --- |
| `gen_ai.client.token.usage` | Token usage by input/output type |
| `gen_ai.client.operation.duration` | Duration of GenAI operations |

These conventions ensure consistent data across different AI providers, making it easier to compare performance and costs.

### Agent span attributes

For AI agents, additional attributes are available. See [GenAI agent spansï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/) for the full specification.

| Attribute | Description | Example |
| --- | --- | --- |
| `gen_ai.agent.id` | The unique identifier of the agent | `assist_agent_5j66UpCpwteGg4YSxUnt7lPY` |
| `gen_ai.agent.name` | Human-readable name of the agent | `Supervisor`, `FAQ Agent` |
| `gen_ai.agent.description` | Free-form description of the agent | `Orchestrates agents for flight details` |
| `gen_ai.data_source.id` | The data source identifier for RAG | `H7STPQYOND` |
| `gen_ai.output.type` | The content type requested | `text`, `json`, `image` |
| `gen_ai.system_instructions` | System message or instructions | JSON array of instructions |
| `gen_ai.tool.definitions` | Tool definitions available to the agent | JSON array of tools |
| `gen_ai.input.messages` | Chat history provided to the model | JSON array of messages |
| `gen_ai.output.messages` | Messages returned by the model | JSON array of responses |

### OpenAI-specific attributes

When using OpenAI, set `gen_ai.provider.name` to `openai`. See [OpenAI semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/openai/) for details.

| Attribute | Description | Example |
| --- | --- | --- |
| `openai.request.service_tier` | The service tier requested | `auto`, `default` |
| `openai.response.service_tier` | The service tier used for the response | `scale`, `default` |
| `openai.response.system_fingerprint` | Fingerprint to track environment changes | `fp_44709d6fcb` |

### AWS Bedrock and AgentCore specific attributes

When using AWS Bedrock, set `gen_ai.provider.name` to `aws.bedrock`. See [AWS Bedrock semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/aws-bedrock/) for details.

| Attribute | Description | Example |
| --- | --- | --- |
| `aws.bedrock.guardrail.id` | The unique identifier of the AWS Bedrock Guardrail. A guardrail helps safeguard and prevent unwanted behavior from model responses | `sgi5gkybzqak` |
| `aws.bedrock.knowledge_base.id` | The unique identifier of the AWS Bedrock Knowledge base used for RAG | `XFWUPB9PAW` |

### Azure AI Foundry and Inference-specific attributes

When using Azure AI Inference, set `gen_ai.provider.name` to `azure.ai.inference`. See [Azure AI Inference semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/azure-ai-inference/) for details.

| Attribute | Description | Example |
| --- | --- | --- |
| `azure.resource_provider.namespace` | Azure Resource Provider Namespace as recognized by the client | `Microsoft.CognitiveServices` |

## Next steps

* Explore the [AI Observability app](/docs/observe/dynatrace-for-ai-observability/ai-observability-app "Use the new AI Observability app to monitor all your AI workloads.") to visualize your AI workloads
* Check out the [sample applicationsï»¿](https://github.com/dynatrace-oss/dynatrace-ai-agent-instrumentation-examples) for more examples