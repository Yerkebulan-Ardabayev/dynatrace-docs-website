---
title: LangChain
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/orchestration-frameworks/langchain
scraped: 2026-02-17T21:20:16.892274
---

# LangChain

# LangChain

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Oct 22, 2024

LangChain is a framework designed for building applications that utilize large language models (LLMs). It provides a set of tools and components that make it easier to integrate LLMs into various applications, enabling developers to create complex workflows and functionalities.

With Dynatrace, you can get visibility into each step of the workflows monitoring prompt and completion messages, error tracking, performance metrics, and more.

![trace-agentic-pipeline](https://dt-cdn.net/images/trace-agentic-pipeline-1708-3a40424e8a.png)

## Spans

The following attributes are available for GenAI Spans.

| Attribute | Type | Description |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | The full response received from the GenAI model. |
| `gen_ai.completion.0.role` | string | The role used by the GenAI model. |
| `gen_ai.prompt.0.content` | string | The full prompt sent to the GenAI model. |
| `gen_ai.prompt.0.role` | string | The role setting for the GenAI request. |
| `gen_ai.request.model` | string | The name of the GenAI model a request is being made to. |
| `gen_ai.response.model` | string | The name of the model that generated the response. |
| `gen_ai.system` | string | The GenAI product as identified by the client or server instrumentation. |
| `llm.request.type` | string | The type of the operation being performed. |
| `traceloop.entity.name` | string | The name of the action in the chain. |
| `traceloop.span.kind` | string | The type of action in the chain. |
| `traceloop.workflow.name` | string | The name of the chain. |

## Metrics

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `http.client.duration` | histogram | `ms` | The duration of the outbound HTTP request. |

## Related topics

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Observability of Retrieval-Augmented Generation pipelines](/docs/observe/dynatrace-for-ai-observability/get-started/sample-use-cases/self-service-ai-observability-tutorial "Learn how to use Dynatrace to have deep insights into your RAG pipelines.")