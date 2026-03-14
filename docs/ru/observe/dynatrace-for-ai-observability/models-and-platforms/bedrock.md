---
title: Amazon Bedrock
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/bedrock
scraped: 2026-03-06T21:14:20.458987
---

# Amazon Bedrock


* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Jan 28, 2026

Amazon Bedrock — это полностью управляемый сервис, предоставляющий единый API для доступа к различным высокопроизводительным базовым моделям (FM) от ведущих AI-компаний и их использования. Он предлагает широкий набор возможностей для создания генеративных AI-приложений с соблюдением требований безопасности, конфиденциальности и принципов ответственного использования AI.

Мониторинг ваших моделей Bedrock через Dynatrace позволяет получить анализ затрат и прогнозную оценку с помощью Dynatrace Intelligence, запись промптов и ответов, отслеживание ошибок, метрики производительности ваших AI-сервисов и многое другое.

![Bedrock Observability](https://dt-cdn.net/images/bedrock-dashboard-4108-e3504d724e.png)

[Ознакомьтесь с примером дашборда на Dynatrace Playground.](https://wkf10640.apps.dynatrace.com/ui/document/dynatrace.genai.observability.bedrock)

## Спаны

Для GenAI-спанов доступны следующие атрибуты.

| Атрибут | Тип | Описание |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | Полный ответ, полученный от GenAI-модели. |
| `gen_ai.completion.0.finish_reason` | string | Причина остановки генерации токенов моделью для каждого полученного ответа. |
| `gen_ai.completion.0.role` | string | Роль, используемая GenAI-моделью. |
| `gen_ai.prompt.0.content` | string | Полный промпт, отправленный в GenAI-модель. |
| `gen_ai.prompt.0.role` | string | Настройка роли для GenAI-запроса. |
| `gen_ai.request.max_tokens` | integer | Максимальное количество токенов, которое модель генерирует для запроса. |
| `gen_ai.request.model` | string | Название GenAI-модели, к которой выполняется запрос. |
| `gen_ai.request.temperature` | double | Настройка температуры для GenAI-запроса. |
| `gen_ai.response.model` | string | Название модели, сгенерировавшей ответ. |
| `gen_ai.system` | string | GenAI-продукт, идентифицированный инструментарием клиента или сервера. |
| `gen_ai.usage.completion_tokens` | integer | Количество токенов, использованных в ответе GenAI-модели (completion). |
| `gen_ai.usage.prompt_tokens` | integer | Количество токенов, использованных во входных данных GenAI (промпт). |
| `llm.request.type` | string | Тип выполняемой операции. |

## Метрики

| Метрика | Тип | Единица | Описание |
| --- | --- | --- | --- |
| `gen_ai.client.operation.duration` | histogram | `s` | Длительность операции GenAI. |
| `gen_ai.client.token.usage` | histogram | `none` | Количество использованных входных и выходных токенов. |

## Связанные темы

* [Конечные точки Dynatrace OTLP API](../../../ingest-from/opentelemetry/otlp-api.md "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [О приёме метрик OTLP](../../../ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest.md "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
