---
title: OpenTelemetry metrics ingest API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/opentelemetry/post-metrics
scraped: 2026-05-12T12:10:36.394933
---

# OpenTelemetry metrics ingest API

# OpenTelemetry metrics ingest API

* Reference
* Published Sep 12, 2022

Загружает метрики OpenTelemetry в Dynatrace. Используйте этот endpoint как target для экспортёров OpenTelemetry. Подробнее смотрите [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API endpoints, которые ваше приложение использует для экспорта OpenTelemetry-данных в Dynatrace.").

Запрос принимает payload `application/x-protobuf`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/metrics` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/metrics` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `metrics.ingest`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | byte[] | Сообщение [ExportMetricsServiceRequest](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.2.0/opentelemetry/proto/collector/metrics/v1/metrics_service.proto) в бинарном формате protobuf. | body | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Запрос получен и будет обработан. |
| **400** | - | Запрос не может быть обработан. Может произойти, если сообщение некорректно. |
| **413** | - | Сообщение OTLP превысило лимит размера payload. |
| **415** | - | Запрос отправлен с неподдерживаемым content type. Этот API поддерживает запросы в бинарном формате protobuf с content type application/x-protobuf. |
| **500** | - | Запрос не может быть обработан из-за внутренней ошибки сервера. |
| **503** | - | Сервис временно недоступен. Может произойти, если модуль приостановлен. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

## Связанные темы

* [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API endpoints, которые ваше приложение использует для экспорта OpenTelemetry-данных в Dynatrace.")