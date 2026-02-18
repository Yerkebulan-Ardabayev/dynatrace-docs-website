---
title: Amazon Bedrock
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/bedrock
scraped: 2026-02-18T05:41:16.812675
---

# Amazon Bedrock

# Amazon Bedrock

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Jan 28, 2026

Amazon Bedrock is a fully managed service that provides a single API to access and utilize various high-performing foundation models (FMs) from leading AI companies. It offers a broad set of capabilities to build generative AI applications with security, privacy, and responsible AI practices.

Monitoring your Bedrock models via Dynatrace, you can get cost analysis and forecast estimation via Dynatrace Intelligence, prompt and completion recording, error tracking, performance metrics of your AI services, and more.

![Bedrock Observability](https://dt-cdn.net/images/bedrock-dashboard-4108-e3504d724e.png)

[Explore the sample dashboard on the Dynatrace Playground.ï»¿](https://wkf10640.apps.dynatrace.com/ui/document/dynatrace.genai.observability.bedrock)

## Spans

The following attributes are available for GenAI Spans.

| Attribute | Type | Description |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | The full response received from the GenAI model. |
| `gen_ai.completion.0.finish_reason` | string | The reason the model stopped generating tokens, corresponding to each generation received. |
| `gen_ai.completion.0.role` | string | The role used by the GenAI model. |
| `gen_ai.prompt.0.content` | string | The full prompt sent to the GenAI model. |
| `gen_ai.prompt.0.role` | string | The role setting for the GenAI request. |
| `gen_ai.request.max_tokens` | integer | The maximum number of tokens the model generates for a request. |
| `gen_ai.request.model` | string | The name of the GenAI model a request is being made to. |
| `gen_ai.request.temperature` | double | The temperature setting for the GenAI request. |
| `gen_ai.response.model` | string | The name of the model that generated the response. |
| `gen_ai.system` | string | The GenAI product as identified by the client or server instrumentation. |
| `gen_ai.usage.completion_tokens` | integer | The number of tokens used in the GenAI response (completion). |
| `gen_ai.usage.prompt_tokens` | integer | The number of tokens used in the GenAI input (prompt). |
| `llm.request.type` | string | The type of the operation being performed. |

## Metrics

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `gen_ai.client.operation.duration` | histogram | `s` | The GenAI operation duration. |
| `gen_ai.client.token.usage` | histogram | `none` | The number of input and output tokens used. |

## Related topics

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")