---
title: Ollama
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/ollama
scraped: 2026-02-22T21:19:46.501531
---

# Ollama

# Ollama

* Latest Dynatrace
* Explanation
* 1-min read
* Published Oct 22, 2024

Ollama is a platform that allows users to run and manage AI models locally on their own machines. It provides tools for deploying, interacting with, and fine-tuning various AI models, particularly those related to natural language processing.

Monitoring your Ollama models via Dynatrace, you can get prompt and completion recording, error tracking, performance metrics of your AI services, and more.

![Ollama Observability](https://dt-cdn.net/images/ollama-1600-47c2844bfa.png)

[Explore the sample dashboard on the Dynatrace Playground.ï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/43d1aa93-b926-4245-9970-6eaca5e26e76)

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
| `gen_ai.usage.completion_tokens` | integer | The number of tokens used in the GenAI response (completion). |
| `gen_ai.usage.prompt_tokens` | integer | The number of tokens used in the GenAI input (prompt). |
| `llm.request.type` | string | The type of the operation being performed. |

## Related topics

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Observability of Retrieval-Augmented Generation pipelines](/docs/observe/dynatrace-for-ai-observability/sample-use-cases/self-service-ai-observability-tutorial "Learn how to use Dynatrace to have deep insights into your RAG pipelines.")