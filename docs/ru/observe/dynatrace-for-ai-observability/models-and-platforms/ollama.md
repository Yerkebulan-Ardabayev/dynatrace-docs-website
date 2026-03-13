---
title: Ollama
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/ollama
scraped: 2026-03-06T21:14:16.809856
---

# Ollama

# Ollama

* Последняя версия Dynatrace
* Пояснение
* Чтение: 1 мин
* Опубликовано 22 окт. 2024 г.

Ollama — это платформа, позволяющая пользователям запускать AI-модели и управлять ими локально на собственных машинах. Она предоставляет инструменты для развёртывания, взаимодействия и тонкой настройки различных AI-моделей, в особенности связанных с обработкой естественного языка.

Отслеживая свои модели Ollama через Dynatrace, вы можете получить запись промптов и ответов, отслеживание ошибок, метрики производительности ваших AI-сервисов и многое другое.

![Ollama Observability](https://dt-cdn.net/images/ollama-1600-47c2844bfa.png)

[Изучите пример дашборда на Dynatrace Playground.](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/43d1aa93-b926-4245-9970-6eaca5e26e76)

## Спаны

Для GenAI-спанов доступны следующие атрибуты.

| Атрибут | Тип | Описание |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | Полный ответ, полученный от GenAI-модели. |
| `gen_ai.completion.0.role` | string | Роль, используемая GenAI-моделью. |
| `gen_ai.prompt.0.content` | string | Полный промпт, отправленный GenAI-модели. |
| `gen_ai.prompt.0.role` | string | Настройка роли для GenAI-запроса. |
| `gen_ai.request.model` | string | Название GenAI-модели, к которой выполняется запрос. |
| `gen_ai.response.model` | string | Название модели, сгенерировавшей ответ. |
| `gen_ai.system` | string | Продукт GenAI, идентифицированный клиентской или серверной инструментацией. |
| `gen_ai.usage.completion_tokens` | integer | Количество токенов, использованных в ответе GenAI (завершение). |
| `gen_ai.usage.prompt_tokens` | integer | Количество токенов, использованных во входных данных GenAI (промпт). |
| `llm.request.type` | string | Тип выполняемой операции. |

## Связанные темы

* [OTLP API-эндпоинты Dynatrace](../../../ingest-from/opentelemetry/otlp-api.md "Узнайте об OTLP API-эндпоинтах, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")
* [О приёме метрик OTLP](../../../ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest.md "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.")
* [Наблюдаемость конвейеров Retrieval-Augmented Generation](../sample-use-cases/self-service-ai-observability-tutorial.md "Узнайте, как использовать Dynatrace для получения глубокого понимания ваших RAG-конвейеров.")
