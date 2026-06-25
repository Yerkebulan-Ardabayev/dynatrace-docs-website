---
title: OpenTelemetry trace ingest API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/opentelemetry/post-traces
scraped: 2026-05-12T12:10:38.334723
---

# OpenTelemetry trace ingest API

# OpenTelemetry trace ingest API

* Reference
* Published Feb 14, 2022

Загружает трейсы OpenTelemetry в Dynatrace. Используйте этот endpoint как target для экспортёров OpenTelemetry. Подробнее смотрите [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API endpoints, которые ваше приложение использует для экспорта OpenTelemetry-данных в Dynatrace.").

Запрос принимает payload `application/x-protobuf`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/otlp/v1/traces` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/traces` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `openTelemetryTrace.ingest`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | byte[] | Сообщение [ExportTraceServiceRequest](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.2.0/opentelemetry/proto/collector/trace/v1/trace_service.proto) в бинарном формате protobuf. | body | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Запрос получен и будет обработан. |
| **400** | - | Запрос не может быть обработан. Может произойти, если сообщение некорректно. |
| **413** | - | Сообщение OTLP превысило лимит размера payload. |
| **415** | - | Запрос отправлен с неподдерживаемым content type. Этот API поддерживает запросы в бинарном формате protobuf с content type application/x-protobuf. |
| **500** | - | Запрос не может быть обработан из-за внутренней ошибки сервера. |
| **503** | - | Сервис временно недоступен. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

## Ограничения

* Поиск трейсов/спанов по атрибутам OpenTelemetry resources ограничен **service.name**. Используйте фильтр **Service name** на странице **Distributed traces**.
* Поиск трейсов/спанов по атрибутам OpenTelemetry span ограничен именем спана. Используйте фильтр **Request** на странице **Distributed traces**.

## OneAgent endpoint

В дополнение к OpenTelemetry trace ingest API OneAgent предоставляет локальный OpenTelemetry endpoint для загрузки трейсов.

Адрес этого endpoint: `http://localhost:14499/otlp/v1/traces` на TCP-порте 14499 по умолчанию (настраивается через [`oneagentctl`](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#set-a-custom-ingestion-port "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки.")), требует `POST`-запрос.

### Включение endpoint'а

По умолчанию endpoint выключен.

Включить на уровне окружения

1. Перейдите в **Settings** и выберите **Preferences** > **Extension Execution Controller**.
2. Включите **Enable Extension Execution Controller**.
3. Включите **Enable local HTTP Metric, Log and Event Ingest API**.

Включить для host group

1. Перейдите в **Deployment Status** > **OneAgents**.
2. На странице **OneAgent deployment** выключите **Show new OneAgent deployments**.
3. В поле **Filter by** введите **Host group** и выберите host group, которую нужно настроить, из выпадающего списка.

   Список хостов теперь отфильтрован по выбранной host group. У каждого хоста в списке есть ссылка **Host group:** `<group name>`, где `<group name>` это имя host group, которую нужно настроить.

   Свойство **Host group** не отображается, когда выбранный хост не принадлежит ни одной host group.
4. Выберите имя host group в любой строке.

   Поскольку вы отфильтровали по host group, все отображаемые хосты относятся к одной и той же host group.

5. В настройках host group выберите **Extension Execution Controller**.
6. Включите **Enable Extension Execution Controller**.

Включить для одного хоста

1. Перейдите в **Hosts**.
2. Найдите и выберите хост, чтобы открыть страницу обзора хоста.
3. В правом верхнем углу страницы обзора хоста выберите **More** (**â¦**) > **Settings**.

4. В настройках хоста выберите **Extension Execution Controller**.
5. Включите **Enable Extension Execution Controller**.

## Сравнение ingestion API и OneAgent endpoint

| Ingestion API | OneAgent endpoint |
| --- | --- |
| * Поддерживает все сигналы OpenTelemetry (traces, metrics, logs) * Нет автоматического обогащения информации * SSL и аутентификация | * Автоматическое обогащение информации * Нет поддержки metrics и logs (только traces) * Нет аутентификации |

## Связанные темы

* [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об OTLP API endpoints, которые ваше приложение использует для экспорта OpenTelemetry-данных в Dynatrace.")