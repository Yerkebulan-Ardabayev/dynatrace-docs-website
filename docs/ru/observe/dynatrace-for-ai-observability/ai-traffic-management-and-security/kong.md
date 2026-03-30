---
title: Шлюз Kong AI
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/ai-traffic-management-and-security/kong
scraped: 2026-03-05T21:32:10.458716
---

# Kong AI Gateway


* Latest Dynatrace
* Explanation
* 2-min read

**Kong AI Gateway** — это набор функций, построенных поверх Kong Gateway, предназначенных для помощи разработчикам и организациям в быстром и безопасном внедрении возможностей ИИ. Он предоставляет нормализованный слой API, который позволяет клиентам использовать несколько ИИ-сервисов из одной кодовой базы.

![Kong-dashboard](https://dt-cdn.net/images/kong-dashboard-1639-51c812bf99.png)

[Изучите пример дашборда на Dynatrace Playground.](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/dynatrace.genai.observability.kong)

## Включение мониторинга

Убедитесь, что [плагин Kong Prometheus](https://docs.konghq.com/hub/kong-inc/prometheus/#ai-llm-metrics) включён и предоставляет метрики AI LLM.

Kubernetes

OpenTelemetry Collector

Следуйте руководству Настройка Dynatrace в Kubernetes, чтобы настроить мониторинг вашего кластера.

После этого добавьте следующие аннотации к вашим Deployment-ресурсам Kong:

* `metrics.dynatrace.com/scrape: "true"`
* `metrics.dynatrace.com/port: "8100"`

Следуйте руководству по установке OpenTelemetry Collector для развёртывания коллектора.
С помощью следующей конфигурации коллектор будет собирать метрики AI LLM каждые 10 секунд с эндпоинта `kong-metrics.kong:8100`.

```
receivers:


prometheus:


config:


scrape_configs:


- job_name: kong


scrape_interval: 10s


honor_labels: false


static_configs:


- targets:


- kong-metrics.kong:8100


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

Рекомендуется установить параметр `max_staleness` процессора [cumulativetodelta](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) на значение, превышающее частоту получения метрик коллектором (например, частоту получения метрик через OTLP или длительность интервала сбора Prometheus). Это гарантирует, что ссылки на устаревшие потоки метрик не будут накапливаться в памяти с течением времени.

Kong не предоставляет сервис `kong-metrics` для сбора метрик по умолчанию, поэтому вам необходимо создать его с помощью следующего определения сервиса:

```
apiVersion: v1


kind: Service


metadata:


name: kong-metrics


namespace: kong


spec:


type: ClusterIP


ports:


- name: metrics


port: 8100


targetPort: 8100


protocol: TCP


selector:


app.kubernetes.io/name: kong


app.kubernetes.io/instance: kong
```

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
| `gen_ai.request.max_tokens` | integer | Максимальное количество токенов, генерируемых моделью для запроса. |
| `gen_ai.request.model` | string | Название модели GenAI, к которой выполняется запрос. |
| `gen_ai.request.temperature` | double | Настройка температуры для запроса GenAI. |
| `gen_ai.request.top_p` | double | Настройка сэмплирования top\_p для запроса GenAI. |
| `gen_ai.response.model` | string | Название модели, сгенерировавшей ответ. |
| `gen_ai.system` | string | Продукт GenAI, идентифицированный клиентской или серверной инструментацией. |
| `gen_ai.usage.completion_tokens` | integer | Количество токенов, использованных в ответе GenAI (completion). |
| `gen_ai.usage.prompt_tokens` | integer | Количество токенов, использованных во входных данных GenAI (prompt). |
| `llm.request.type` | string | Тип выполняемой операции. |

## Метрики

После выполнения описанных выше шагов будут доступны следующие метрики:

| Метрика | Тип | Единица | Описание |
| --- | --- | --- | --- |
| `ai_llm_requests_total` | counter | integer | Общее количество ИИ-запросов по ai\_provider в Kong |
| `ai_llm_cost_total` | counter | integer | Стоимость ИИ-запросов по ai\_provider/cache в Kong |
| `ai_llm_provider_latency_ms_bucket` | histogram | ms | Задержки ИИ по ai\_provider в Kong |
| `ai_llm_tokens_total` | counter | integer | Общее количество токенов ИИ по ai\_provider/cache в Kong |
| `ai_cache_fetch_latency` | histogram | ms | Задержки кэша ИИ по ai\_provider/database в Kong |
| `ai_cache_embeddings_latency` | histogram | ms | Задержки эмбеддингов кэша ИИ по ai\_provider/database в Kong |
| `ai_llm_provider_latency` | histogram | ms | Задержки провайдера ИИ по ai\_provider/database в Kong |

Кроме того, передаются следующие метрики.

| Метрика | Тип | Единица | Описание |
| --- | --- | --- | --- |
| `gen_ai.client.generation.choices` | counter | `none` | Количество вариантов, возвращённых вызовом chat completions. |
| `gen_ai.client.operation.duration` | histogram | `s` | Длительность операции GenAI. |
| `gen_ai.client.token.usage` | histogram | `none` | Количество использованных входных и выходных токенов. |
| `llm.openai.embeddings.vector_size` | counter | `none` | Размер возвращённого вектора. |
