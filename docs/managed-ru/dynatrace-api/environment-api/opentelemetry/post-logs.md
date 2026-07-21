---
title: OpenTelemetry logs ingest API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/opentelemetry/post-logs
---

# OpenTelemetry logs ingest API

# OpenTelemetry logs ingest API

* Справочник
* Опубликовано 09 ноя 2023

Отправляет OpenTelemetry-логи в Dynatrace. Использовать эту конечную точку как цель для экспортёров OpenTelemetry. Подробнее см. [конечные точки OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

Запрос принимает полезную нагрузку `application/x-protobuf`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/logs` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `logs.ingest`.

О том, как получить и использовать его, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

При использовании обработки логов с помощью пользовательского конвейера обработки (OpenPipeline) ingest поддерживает все типы данных JSON для значений атрибутов. Для этого требуется SaaS версии 1.295+ при использовании SaaS-конечной точки API или ActiveGate версии 1.295+ при использовании конечной точки API ActiveGate. Во всех остальных случаях все принятые значения преобразуются в строковый тип.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| structure | string | (Необязательно) Модель данных, используемая для структурирования входных данных в записи логов. Допустимые значения: `raw`, `flattened`. Подробнее см. [документацию﻿](https://dt-url.net/6y235qc?dt=m). Элемент может принимать следующие значения * `raw` * `flattened` | query | Необязательный |
| X-Dynatrace-Attr | string | (Необязательно) Содержит разделённые амперсандом пары ключ-значение, представляющие дополнительные атрибуты лога, которые нужно добавить к каждой принятой записи лога. Если один и тот же ключ встречается несколько раз, все значения фиксируются как атрибут с несколькими значениями. Параметры запроса имеют приоритет над значениями, указанными в этом заголовке. Подробнее см. [документацию﻿](https://dt-url.net/vj639p4?dt=m). | header | Необязательный |
| X-Dynatrace-Options | string | (Необязательно) Содержит разделённые амперсандом параметры, специфичные для Dynatrace. Поддерживаемые опции: (только SaaS) `structure` (значения: `raw`, `flattened`) определяет, как входные данные структурируются в записи логов. Параметры запроса имеют приоритет над значениями заголовка. Подробнее см. [документацию﻿](https://dt-url.net/6y235qc?dt=m). | header | Необязательный |
| body | [ExportLogsServiceRequest](#openapi-definition-ExportLogsServiceRequest) | Сообщение ExportLogsServiceRequest в бинарном формате protobuf. | body | Обязательный |

### Объекты тела запроса

#### Объект `ExportLogsServiceRequest`

Protobuf-запрос [ExportLogsServiceRequest﻿](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.2.0/opentelemetry/proto/collector/logs/v1/logs_service.proto),
определённый в официальной спецификации OpenTelemetry, служит входным типом для RPC LogsService/Export.

Хотя протокол определяет формат передачи данных, следующие свойства являются частью модели данных логов, которая представляет структуру записей логов при обработке в Dynatrace:

* Timestamp: время, когда произошло событие.
* ObservedTimestamp: время, когда событие было зафиксировано.
* TraceId: ID трассировки запроса.
* SpanId: ID спана запроса.
* TraceFlags: флаг трассировки W3C.
* SeverityText: текст уровня серьёзности (также известен как уровень лога).
* SeverityNumber: числовое значение уровня серьёзности.
* Body: тело записи лога.
* Resource: описывает источник лога.
* InstrumentationScope: описывает область, из которой был отправлен лог.
* Attributes: дополнительная информация о событии.
* EventName: имя, идентифицирующее класс/тип события.

Записи логов сопоставляются с записями логов Dynatrace, содержащими три специальных атрибута: timestamp, loglevel и content, а также карту прочих атрибутов. Подробнее см. [документацию﻿](https://dt-url.net/6y235qc?dt=m).

(Только SaaS) Обработка атрибутов зависит от модели данных, используемой для обработки входных данных. Действующая модель данных для конкретного запроса зависит от параметра `structure` или от модели данных тенанта по умолчанию, которая определяется конфигурацией тенанта. Подробнее см. в [документации﻿](https://dt-url.net/6y235qc?dt=m).

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Запрос успешно принят или принят частично (то есть когда сервер принимает только часть данных и отклоняет остальное). |
| **400** | - | Запрос не может быть обработан. Это может произойти, если сообщение имеет неверный формат. |
| **413** | - | Сообщение OTLP превысило ограничение размера полезной нагрузки. Можно повторить с экспоненциальной задержкой. |
| **500** | - | Запрос не может быть обработан из-за внутренней ошибки сервера. |
| **502** | - | Ошибка. Bad Gateway. Это может произойти, если промежуточная система (например, ActiveGate или прокси) сталкивается с проблемой при пересылке запроса. Можно повторить с экспоненциальной задержкой. |
| **503** | - | Сервис в данный момент недоступен. Можно повторить с экспоненциальной задержкой. |
| **504** | - | Ошибка. Gateway Timeout. Это может произойти из-за проблемы в базовой инфраструктуре, вызвавшей задержку в обработке запроса. Можно повторить с экспоненциальной задержкой. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

## Смежные темы

* [конечные точки OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")