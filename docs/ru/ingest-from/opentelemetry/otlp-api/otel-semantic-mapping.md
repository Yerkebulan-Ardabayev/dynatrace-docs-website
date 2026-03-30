---
title: Семантическое сопоставление OpenTelemetry и Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/otel-semantic-mapping
scraped: 2026-03-06T21:35:37.469462
---

Dynatrace автоматически сопоставляет семантические соглашения OpenTelemetry со Словарём семантики Dynatrace.

Это сопоставление обеспечивает единообразную интерпретацию данных во всём стеке наблюдаемости и позволяет приложениям, аналитике и функциям визуализации Dynatrace работать с инструментацией OpenTelemetry.

## Операции с сообщениями

Dynatrace сопоставляет атрибуты сообщений OpenTelemetry с семантической моделью Dynatrace.

| Атрибут OpenTelemetry | Атрибут Dynatrace |
| --- | --- |
| `messaging.operation` | `messaging.operation.type` |

Для [`messaging.operation.type`](../../../semantic-dictionary/fields.md#messaging "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") значение `send` нормализуется до `publish`.

## Разбор URL

Dynatrace автоматически разбирает [`url.full`](../../../semantic-dictionary/fields.md#url "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") на составные компоненты:

| Производный атрибут | Описание |
| --- | --- |
| `url.path` | Компонент пути URL |
| `url.scheme` | Схема протокола (например, `https`) |
| `url.fragment` | Идентификатор фрагмента |
| `url.query` | Строка запроса |
| `server.address` | Адрес хоста |
| `server.port` | Номер порта |

### Устаревшие атрибуты

Dynatrace сопоставляет устаревшие HTTP-атрибуты OpenTelemetry с их актуальными эквивалентами:

| Устаревший атрибут | Актуальный атрибут |
| --- | --- |
| `http.url` | `url.full` |
| `http.method` | `http.request.method` |
| `http.status_code` | `http.response.status_code` |

## Атрибуты облачных провайдеров

Dynatrace создаёт атрибуты, специфичные для провайдеров, на основе стандартных облачных атрибутов OpenTelemetry.

### Идентификаторы аккаунтов и проектов

Dynatrace создаёт атрибуты аккаунтов, специфичные для провайдеров, на основе стандартного атрибута [`cloud.account.id`](../../../semantic-dictionary/fields.md#cloud "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types."):

| Облачный провайдер | Атрибут OpenTelemetry | Создаваемый атрибут |
| --- | --- | --- |
| AWS | `cloud.account.id` | `aws.account.id` |
| Azure | `cloud.account.id` | `azure.subscription` |
| Google Cloud | `cloud.account.id` | `gcp.project.id` |

### Региональные атрибуты

Dynatrace создаёт региональные атрибуты, специфичные для провайдеров, на основе стандартных атрибутов [`cloud.region`](../../../semantic-dictionary/fields.md#cloud "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") и связанных с ними:

| Облачный провайдер | Атрибуты OpenTelemetry | Создаваемый атрибут |
| --- | --- | --- |
| AWS | `cloud.region` | `aws.region` |
| Azure | `cloud.region` | `azure.location` |
| Google Cloud | `gcp.location` `gcp.zone` `cloud.region` `cloud.availability_zone` | `gcp.region` |

Для Google Cloud при наличии нескольких исходных атрибутов они оцениваются в порядке, указанном выше.

## Использование стандартных соглашений OpenTelemetry

В вашей инструментации поддерживаются стандартные [семантические соглашения OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/). Dynatrace автоматически выполняет преобразование. Это позволяет стандартным семантическим соглашениям OpenTelemetry работать с семантическим анализом Dynatrace.
