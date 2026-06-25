---
title: OpenTelemetry logs ingest API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/opentelemetry/post-logs
scraped: 2026-05-12T12:10:16.914455
---

# OpenTelemetry logs ingest API

# OpenTelemetry logs ingest API

* Reference
* Published Nov 09, 2023

Загружает логи OpenTelemetry в Dynatrace. Используйте этот endpoint как target для экспортёров OpenTelemetry. Подробнее смотрите [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API endpoints, которые ваше приложение использует для экспорта OpenTelemetry-данных в Dynatrace.").

Запрос принимает payload `application/x-protobuf`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/logs` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `logs.ingest`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

При использовании log processing с пользовательским pipeline'ом обработки (OpenPipeline) ingest поддерживает все JSON-типы данных для значений атрибутов. Это требует SaaS версии 1.295+ при использовании SaaS API endpoint или ActiveGate версии 1.295+ при использовании ActiveGate API endpoint. Во всех остальных случаях все загружаемые значения конвертируются в тип string.

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| structure | string | (Опционально) Модель данных, используемая для структурирования входных данных в записи логов. Допустимые значения: `raw`, `flattened`. Подробнее в [documentation](https://dt-url.net/6y235qc). Элемент может принимать значения * `raw` * `flattened` | query | Optional |
| X-Dynatrace-Attr | string | (Опционально) Содержит разделённые амперсандом пары ключâзначение, представляющие дополнительные атрибуты лога, добавляемые к каждой загружаемой записи. Если один и тот же ключ встречается несколько раз, все значения сохраняются как multiâvalue атрибут. Query-параметры имеют приоритет над значениями, переданными в этом заголовке. | header | Optional |
| X-Dynatrace-Options | string | (Опционально) Содержит разделённые амперсандом Dynatrace-специфичные параметры. Поддерживаемые опции: (только SaaS) `structure` (значения: `raw`, `flattened`) определяет, как входные данные структурируются в записи логов. Query-параметры имеют приоритет над значениями заголовка. Подробнее в [documentation](https://dt-url.net/6y235qc). | header | Optional |
| body | [ExportLogsServiceRequest](#openapi-definition-ExportLogsServiceRequest) | Сообщение ExportLogsServiceRequest в бинарном формате protobuf. | body | Required |

### Объекты тела запроса

#### Объект `ExportLogsServiceRequest`

Запрос protobuf [ExportLogsServiceRequest](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.2.0/opentelemetry/proto/collector/logs/v1/logs_service.proto),
определённый в официальной спецификации OpenTelemetry, служит входным типом для LogsService/Export RPC.

Хотя протокол определяет wire-формат, следующие свойства являются частью Log Data Model, которая представляет структуру записей логов при обработке в Dynatrace:

* Timestamp: Время возникновения события.
* ObservedTimestamp: Время наблюдения события.
* TraceId: ID трейса запроса.
* SpanId: ID спана запроса.
* TraceFlags: W3C trace flag.
* SeverityText: Текст уровня (также известен как log level).
* SeverityNumber: Числовое значение уровня.
* Body: Тело записи лога.
* Resource: Описывает источник лога.
* InstrumentationScope: Описывает scope, который сгенерировал лог.
* Attributes: Дополнительная информация о событии.
* EventName: Имя, идентифицирующее класс/тип события.

Записи логов отображаются в записи логов Dynatrace, содержащие три специальных атрибута: timestamp, loglevel и content, а также map других атрибутов. Подробнее в [documentation](https://dt-url.net/6y235qc).

(Только SaaS) Обработка атрибутов зависит от модели данных, используемой для обработки входных данных. Эффективная модель данных для конкретного запроса зависит от параметра `structure` или модели данных tenant по умолчанию, которая определяется конфигурацией tenant. Подробнее в [documentation](https://dt-url.net/6y235qc).

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Запрос успешно принят или принят частично (т.е. когда сервер принимает только часть данных, а остальное отклоняет). |
| **400** | - | Запрос не может быть обработан. Может произойти, если сообщение некорректно. |
| **413** | - | Сообщение OTLP превысило лимит размера payload. Можно повторять с экспоненциальным backoff. |
| **500** | - | Запрос не может быть обработан из-за внутренней ошибки сервера. |
| **502** | - | Ошибка. Bad Gateway. Может произойти, когда промежуточная система (например, ActiveGate или прокси) сталкивается с проблемой при пересылке запроса. Можно повторять с экспоненциальным backoff. |
| **503** | - | Сервис временно недоступен. Можно повторять с экспоненциальным backoff. |
| **504** | - | Ошибка. Gateway Timeout. Может произойти из-за проблем в нижележащей инфраструктуре, вызывающих задержку обработки запроса. Можно повторять с экспоненциальным backoff. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

## Связанные темы

* [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API endpoints, которые ваше приложение использует для экспорта OpenTelemetry-данных в Dynatrace.")