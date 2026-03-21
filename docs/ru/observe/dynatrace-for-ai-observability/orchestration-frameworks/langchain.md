---
title: LangChain
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/orchestration-frameworks/langchain
scraped: 2026-03-06T21:14:13.335634
---

* Latest Dynatrace
* How-to guide
* 2-min read

LangChain — это фреймворк, предназначенный для создания приложений, использующих большие языковые модели (LLM). Он предоставляет набор инструментов и компонентов, упрощающих интеграцию LLM в различные приложения и позволяющих разработчикам создавать сложные рабочие процессы и функциональные возможности.

С помощью Dynatrace вы можете получить видимость на каждом шаге рабочих процессов, отслеживая сообщения запросов и ответов, ошибки, метрики производительности и многое другое.

![trace-agentic-pipeline](https://dt-cdn.net/images/trace-agentic-pipeline-1708-3a40424e8a.png)

## Spans

Для спанов GenAI доступны следующие атрибуты.

| Атрибут | Тип | Описание |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | Полный ответ, полученный от модели GenAI. |
| `gen_ai.completion.0.role` | string | Роль, используемая моделью GenAI. |
| `gen_ai.prompt.0.content` | string | Полный запрос, отправленный в модель GenAI. |
| `gen_ai.prompt.0.role` | string | Настройка роли для запроса GenAI. |
| `gen_ai.request.model` | string | Название модели GenAI, к которой выполняется запрос. |
| `gen_ai.response.model` | string | Название модели, сгенерировавшей ответ. |
| `gen_ai.system` | string | Продукт GenAI, идентифицированный клиентской или серверной инструментацией. |
| `llm.request.type` | string | Тип выполняемой операции. |
| `traceloop.entity.name` | string | Название действия в цепочке. |
| `traceloop.span.kind` | string | Тип действия в цепочке. |
| `traceloop.workflow.name` | string | Название цепочки. |

## Метрики

| Метрика | Тип | Единица | Описание |
| --- | --- | --- | --- |
| `http.client.duration` | histogram | `ms` | Длительность исходящего HTTP-запроса. |

## Связанные темы

* [Dynatrace OTLP API endpoints](../../../ingest-from/opentelemetry/otlp-api.md "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](../../../ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest.md "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Observability of Retrieval-Augmented Generation pipelines](../sample-use-cases/self-service-ai-observability-tutorial.md "Learn how to use Dynatrace to have deep insights into your RAG pipelines.")
