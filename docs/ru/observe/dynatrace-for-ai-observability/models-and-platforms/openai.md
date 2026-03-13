---
title: OpenAI
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/openai
scraped: 2026-03-06T21:14:15.056939
---

# OpenAI

# OpenAI

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Jan 28, 2026

Мониторинг ваших запросов OpenAI через Dynatrace позволяет получить анализ затрат и оценку прогноза через Dynatrace Intelligence, запись промптов и ответов (completions), отслеживание ошибок, метрики производительности ваших AI-сервисов и многое другое.

![OpenAI Observability](https://dt-cdn.net/images/openai-dashboard-4102-e844fa80f9.png)

[Explore the sample dashboard on the Dynatrace Playground.ï»¿](https://wkf10640.apps.dynatrace.com/ui/document/dynatrace.genai.observability.openai)

## Спаны

Для GenAI Spans доступны следующие атрибуты.

| Атрибут | Тип | Описание |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | Полный ответ, полученный от модели GenAI. |
| `gen_ai.completion.0.content_filter_results` | string | Результаты фильтрации ответа, полученного от модели GenAI. |
| `gen_ai.completion.0.finish_reason` | string | Причина, по которой модель GenAI прекратила генерацию токенов. |
| `gen_ai.completion.0.role` | string | Роль, используемая моделью GenAI. |
| `gen_ai.openai.api_base` | string | Адрес сервера GenAI. |
| `gen_ai.openai.api_version` | string | Версия GenAI API. |
| `gen_ai.openai.system_fingerprint` | string | Отпечаток ответа, сгенерированного моделью GenAI. |
| `gen_ai.prompt.0.content` | string | Полный промпт, отправленный модели GenAI. |
| `gen_ai.prompt.0.role` | string | Настройка роли для запроса к GenAI. |
| `gen_ai.prompt.prompt_filter_results` | string | Результаты фильтрации промпта, отправленного модели GenAI. |
| `gen_ai.request.max_tokens` | integer | Максимальное количество токенов, генерируемых моделью для запроса. |
| `gen_ai.request.model` | string | Название модели GenAI, к которой выполняется запрос. |
| `gen_ai.request.temperature` | double | Настройка температуры для запроса к GenAI. |
| `gen_ai.request.top_p` | double | Настройка выборки top\_p для запроса к GenAI. |
| `gen_ai.response.model` | string | Название модели, сгенерировавшей ответ. |
| `gen_ai.system` | string | Продукт GenAI, определённый инструментированием клиента или сервера. |
| `gen_ai.usage.completion_tokens` | integer | Количество токенов, использованных в ответе GenAI (completion). |
| `gen_ai.usage.prompt_tokens` | integer | Количество токенов, использованных во входных данных GenAI (промпте). |
| `llm.request.type` | string | Тип выполняемой операции. |

## Метрики

| Метрика | Тип | Единица | Описание |
| --- | --- | --- | --- |
| `gen_ai.client.generation.choices` | counter | `none` | Количество вариантов ответа, возвращённых вызовом chat completions. |
| `gen_ai.client.operation.duration` | histogram | `s` | Длительность операции GenAI. |
| `gen_ai.client.token.usage` | histogram | `none` | Количество использованных входных и выходных токенов. |
| `llm.openai.embeddings.vector_size` | counter | `none` | Размер возвращённого вектора. |

## Связанные темы

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
