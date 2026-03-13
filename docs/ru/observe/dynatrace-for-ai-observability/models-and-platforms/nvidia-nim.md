---
title: NVIDIA NIM
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/nvidia-nim
scraped: 2026-03-06T21:14:25.595461
---

# NVIDIA NIM

# NVIDIA NIM

* Последняя версия Dynatrace
* Пояснение
* Чтение: 2 мин
* Обновлено 20 ноя 2025

NVIDIA NIM (NVIDIA Inference Microservices) — это набор микросервисов, которые ускоряют развертывание базовых моделей в любом облаке или центре обработки данных, оптимизируя инфраструктуру ИИ для повышения эффективности и экономичности при одновременном снижении затрат на оборудование и эксплуатацию.

![Панель управления NVIDIA NIM](https://dt-cdn.net/images/ai-observability-nvidia-nim-3580-bc02ba8523.png)

[Изучите пример панели управления на Dynatrace Playground.](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/cdf180cb-3153-447f-8f28-5bfb05bd3e93)

## Включение мониторинга

Kubernetes

OpenTelemetry Collector

Следуйте руководству [Настройка Dynatrace в Kubernetes](/docs/ingest-from/setup-on-k8s "Способы развертывания и настройки Dynatrace в Kubernetes") для мониторинга вашего кластера.

После этого добавьте следующие аннотации к вашим развертываниям NVIDIA NIM:

* `metrics.dynatrace.com/scrape: "true"`
* `metrics.dynatrace.com/port: "8000"`

Следуйте [руководству по установке OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/deployment "Как развернуть Dynatrace OTel Collector.") для развертывания коллектора.
С помощью следующей конфигурации коллектор будет собирать метрики ИИ каждые 10 секунд с конечной точки `<NIM-endpoint>:8000`.

```
receivers:



prometheus:



config:



scrape_configs:



- job_name: nim-metrics



scrape_interval: 10s



honor_labels: false



static_configs:



- targets:



- ["<NIM-endpoint>:8000"]



processors:



cumulativetodelta:



max_staleness: 25h



extensions:



health_check:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



extensions: [health_check]



metrics:



receivers: [prometheus]



processors: [cumulativetodelta]



exporters: [otlp_http]
```

Рекомендация по процессору cumulativetodelta

Рекомендуется установить параметр `max_staleness` процессора [cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) на значение, превышающее частоту получения метрик коллектором (например, частоту получения метрик через OTLP или длительность интервала сбора Prometheus). Это гарантирует, что ссылки на заброшенные потоки метрик не будут накапливаться в памяти со временем.

## Спаны

Следующие атрибуты доступны для спанов GenAI.

| Атрибут | Тип | Описание |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | Полный ответ, полученный от модели GenAI. |
| `gen_ai.completion.0.content_filter_results` | string | Результаты фильтрации ответа, полученного от модели GenAI. |
| `gen_ai.completion.0.finish_reason` | string | Причина, по которой модель GenAI прекратила генерацию токенов. |
| `gen_ai.completion.0.role` | string | Роль, используемая моделью GenAI. |
| `gen_ai.openai.api_base` | string | Адрес сервера GenAI. |
| `gen_ai.openai.api_version` | string | Версия API GenAI. |
| `gen_ai.openai.system_fingerprint` | string | Отпечаток ответа, сгенерированного моделью GenAI. |
| `gen_ai.prompt.0.content` | string | Полный промпт, отправленный модели GenAI. |
| `gen_ai.prompt.0.role` | string | Настройка роли для запроса GenAI. |
| `gen_ai.prompt.prompt_filter_results` | string | Результаты фильтрации промпта, отправленного модели GenAI. |
| `gen_ai.request.max_tokens` | integer | Максимальное количество токенов, которое модель генерирует для запроса. |
| `gen_ai.request.model` | string | Название модели GenAI, к которой выполняется запрос. |
| `gen_ai.request.temperature` | double | Настройка температуры для запроса GenAI. |
| `gen_ai.request.top_p` | double | Настройка top\_p для запроса GenAI. |
| `gen_ai.response.model` | string | Название модели, сгенерировавшей ответ. |
| `gen_ai.system` | string | Продукт GenAI, определенный клиентской или серверной инструментацией. |
| `gen_ai.usage.completion_tokens` | integer | Количество токенов, использованных в ответе GenAI (completion). |
| `gen_ai.usage.prompt_tokens` | integer | Количество токенов, использованных во входных данных GenAI (промпт). |
| `llm.request.type` | string | Тип выполняемой операции. |

## Метрики

Доступны следующие метрики:

| Метрика | Тип | Единица | Описание |
| --- | --- | --- | --- |
| `e2e_request_latency_seconds` | histoGrailm | s | Гистограмма задержки сквозного запроса в секундах |
| `generation_tokens_total` | counter | integer | Количество обработанных токенов генерации |
| `gpu_cache_usage_perc` | gauge | integer | Использование KV-кеша GPU. 1 означает 100-процентное использование |
| `num_request_max` | counter | integer | Максимальное количество одновременно выполняемых запросов |
| `num_requests_running` | counter | integer | Количество запросов, выполняемых в данный момент на GPU |
| `num_requests_waiting` | counter | integer | Количество запросов, ожидающих обработки |
| `prompt_tokens_total` | counter | integer | Количество обработанных токенов предзаполнения |
| `request_failure_total` | counter | integer | Количество неудавшихся запросов; учитываются запросы с другими причинами завершения |
| `request_finish_total` | counter | integer | Количество завершенных запросов с меткой, указывающей причину завершения |
| `request_generation_tokens` | histogram | integer | Гистограмма количества обработанных токенов генерации |
| `request_prompt_tokens` | histogram | integer | Гистограмма количества обработанных токенов предзаполнения |
| `request_success_total` | counter | integer | Количество успешных запросов; учитываются запросы с причиной завершения "stop" или "length" |
| `time_per_output_token_seconds` | histogram | s | Гистограмма времени на выходной токен в секундах |
| `time_to_first_token_seconds` | histogram | s | Гистограмма времени до первого токена в секундах |

Дополнительно передаются следующие метрики.

| Метрика | Тип | Единица | Описание |
| --- | --- | --- | --- |
| `gen_ai.client.generation.choices` | counter | `none` | Количество вариантов, возвращенных вызовом chat completions. |
| `gen_ai.client.operation.duration` | histogram | `s` | Длительность операции GenAI. |
| `gen_ai.client.token.usage` | histogram | `none` | Количество использованных входных и выходных токенов. |
| `llm.openai.embeddings.vector_size` | counter | `none` | Размер возвращенного вектора. |

## Связанные темы

* [Конечные точки Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.")
* [Об импорте метрик OTLP](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace импортирует метрики OpenTelemetry и какие ограничения применяются.")
