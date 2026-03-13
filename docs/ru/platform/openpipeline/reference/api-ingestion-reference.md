---
title: Источники загрузки данных в OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/api-ingestion-reference
scraped: 2026-03-06T21:16:01.329825
---

# Источники загрузки данных в OpenPipeline

# Источники загрузки данных в OpenPipeline

* Последняя версия Dynatrace
* Справочник
* Чтение: 5 мин
* Обновлено 4 декабря 2025 г.

В этой статье вы найдете справочные материалы по источникам загрузки данных в OpenPipeline, разделенные по каждой области конфигурации. Включены:

* Доступные источники загрузки данных и связанный `dt.openpipeline.source`
* Спецификация API загрузки данных, такая как URL-адрес конечной точки и метод аутентификации
* Предварительные знания, такие как концепции, совместимость лицензирования и настройка

Параметры запроса

Каждый параметр запроса становится атрибутом верхнего уровня записи. Если в полезной нагрузке уже существует атрибут с тем же именем, атрибут из параметра запроса переопределяет существующее значение атрибута. Переопределенное исходное значение сохраняется в новом поле с синтаксисом имени `overwritten<index>.<original field name>`, например, `overwritten1.myField`.

Бизнес-события

### Предварительные знания

* [Как захватывать бизнес-события](/docs/observe/business-observability/bo-events-capturing "Capture business events for Dynatrace Business Observability.")
* [Этап извлечения данных OpenPipeline](/docs/platform/openpipeline/concepts/processing#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [DDU для бизнес-событий](/docs/license/monitoring-consumption-classic/davis-data-units/ddus-for-business-events "Understand how the volume of DDU consumption is calculated for business events.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| OneAgent | `oneagent` | Встроенный |
| RUM Agent | `rumagent` | Встроенный |
| Business Events API | `/api/v2/bizevents/ingest` | Встроенный |
| Извлечение данных | `data_extraction` | Встроенный |

#### Business Events API

Захватывает бизнес-события в Dynatrace.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/bizevents/ingest` |
| Метод | POST |
| Аутентификация | [OAuth](/docs/observe/business-observability/bo-api-ingest#oauth "Set up authentication for and ingest business events via API.") [Токен доступа](/docs/observe/business-observability/bo-api-ingest#access-token "Set up authentication for and ingest business events via API.") с областью действия токена **Ingest bizevents** (`bizevents.ingest`) |
| Полезная нагрузка | `application/json` `application/cloudevent+json` `application/cloudevent-batch+json` |

Подробнее см. [Загрузка бизнес-событий через API](/docs/observe/business-observability/bo-api-ingest "Set up authentication for and ingest business events via API.").

Логи

### Предварительные знания

* [Как загружать логи](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.")
* [Потоковая передача логов через Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [DDU для управления и аналитики логов](/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics "Understand how the volume of DDUs consumption is calculated for Dynatrace Log Management and Analytics.") или [Аналитика логов (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| Amazon Data Firehose | `/api/v2/logs/ingest/aws_firehose` | Встроенный |
| Расширения | `<extension>` | Готовый |
| Log ingest API | `/api/v2/logs/ingest` | Встроенный |
| OneAgent | `oneagent` | Встроенный |
| OpenTelemetry | `/api/v2/otlp/v1/logs` | Встроенный |

#### Log ingest API

Отправляет пользовательские логи в Dynatrace.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest` `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/logs/ingest` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия **Ingest logs** (`logs.ingest`) |
| Полезная нагрузка | `text/plain` `application/json` |

Подробнее см. [Log Monitoring API v2 — POST загрузка логов](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.").

#### OpenTelemetry

Отправляет пользовательские логи в Dynatrace.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest logs** (`logs.ingest`) |
| Полезная нагрузка | `application/x-protobuf` |

Подробнее см. [Загрузка логов OTLP](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.").

События (общие события)

### Предварительные знания

* [Обзор событий на базе Grail (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| API по умолчанию | `/platform/ingest/v1/events` | Встроенный |
| Пользовательский API | `/platform/ingest/custom/events/<custom-endpoint-name>` | Пользовательский |

#### API по умолчанию

Загружает общие события из встроенных конечных точек.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Events** (`openpipeline.events`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [OpenPipeline Ingest API — POST встроенные общие события](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-builtin "Ingest generic events from built-in endpoints via OpenPipeline Ingest API.").

#### Пользовательский API

Настраивает пользовательские конечные точки для загрузки общих событий.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Events (Custom)** (`openpipeline.events.custom`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [OpenPipeline Ingest API — POST пользовательская конечная точка общих событий](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-custom-endpoint "Configure a custom generic event endpoint via OpenPipeline Ingest API.").

События — события Davis

### Предварительные знания

* [События Davis](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.")
* [Этап извлечения данных OpenPipeline](/docs/platform/openpipeline/concepts/processing#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* [Обзор событий на базе Grail (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| OneAgent | `oneagent` | Встроенный |
| Классический API окружения | `events/ingest` | Встроенный |
| Извлечение данных | `data_extraction` | Встроенный |

#### Классический API окружения

Загружает пользовательское событие в Dynatrace.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/events/ingest` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest Events** (`events.ingest`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [Events API v2 — POST событие](/docs/dynatrace-api/environment-api/events-v2/post-event "Ingests an event via the Dynatrace API.").

События — проблемы Davis

### Предварительные знания

* [Проблемы Davis](/docs/semantic-dictionary/model/davis "Get to know the Semantic Dictionary models related to Davis AI.")
* [Классический анализ первопричин](/docs/dynatrace-intelligence/root-cause-analysis/concepts#root-cause-analysis "Get acquainted with root cause analysis concepts.")
* [Обзор событий на базе Grail (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| Классический анализ первопричин | *(нет)* | Встроенный |

События — события SDLC

### Предварительные знания

* [Как загружать события SDLC](/docs/deliver/pipeline-observability-sdlc-events/sdlc-events "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.")
* [Обзор событий на базе Grail (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| Конечная точка для событий жизненного цикла разработки ПО | `/platform/ingest/v1/events.SDLC` | Встроенный |
| Пользовательская конечная точка для событий жизненного цикла разработки ПО | `/platform/ingest/custom/events.SDLC/<custom-endpoint-name>` | Пользовательский |

#### Конечная точка для событий жизненного цикла разработки ПО

Загружает события SDLC из встроенных конечных точек.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events.sdlc` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Events, Security Development Lifecycle** (`openpipeline.sdlc`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [OpenPipeline Ingest API — POST встроенные события SDLC](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-builtin "Ingest SDLC events from built-in endpoints via OpenPipeline Ingest API.").

#### Пользовательская конечная точка для событий жизненного цикла разработки ПО

Настраивает пользовательские конечные точки для загрузки событий SDLC.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.sdlc` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Events, Security Development Lifecycle (Custom)** (`openpipeline.sdlc.custom`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [OpenPipeline Ingest API — POST пользовательская конечная точка событий SDLC](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-custom-endpoint "Configure a custom SDLC event endpoint via OpenPipeline Ingest API.").

События — события безопасности

Мигрируйте до декабря 2025 г.

Конечные точки `events.security` планируется объявить устаревшими. Перенесите свои конфигурации на конечные точки `security.events` до **конца декабря 2025 г.**. Предыдущие конечные точки останутся доступными **до завершения миграции**.

Полный обзор изменений и пошаговые инструкции по миграции см. в [Руководстве по миграции таблиц безопасности Grail](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

### Предварительные знания

* [Как загружать события безопасности](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail.")
* [Обзор событий на базе Grail (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| Конечная точка событий безопасности | `/platform/ingest/v1/events.security` | Встроенный |
| Пользовательский API событий безопасности | `/platform/ingest/custom/events.security/<custom-endpoint-name>` | Пользовательский |

#### Конечная точка событий безопасности (устаревшая)

Загружает события безопасности из встроенных конечных точек.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/events.security` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [OpenPipeline Ingest API — POST встроенные события безопасности (устаревшие)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.").

#### Пользовательский API событий безопасности (устаревший)

Настраивает пользовательские конечные точки для загрузки событий безопасности. Подробнее см. [Загрузка пользовательских событий безопасности через API](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data "Ingest security events from custom third-party products via API.").

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.security` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [OpenPipeline Ingest API — POST пользовательская конечная точка событий безопасности (устаревшая)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.").

Метрики

### Предварительные знания

* [Как загружать метрики](/docs/analyze-explore-automate/metrics "Metrics powered by Grail offer a comprehensive solution to manage your metrics data, in integration with logs, spans, and events, providing a unified approach to data analysis.")
* [Обзор метрик на базе Grail (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| OneAgent | `oneagent` | Встроенный |
| Классический API окружения | `/api/v2/metrics/ingest` | Встроенный |
| OpenTelemetry | `/api/v2/otlp/v1/metrics` | Встроенный |

#### Классический API окружения

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest metrics** (`metrics.ingest`) |
| Полезная нагрузка | `text/plain` |

Подробнее см. [Metrics API — POST загрузка точек данных](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").

#### OpenTelemetry

Загружает метрики OpenTelemetry в Dynatrace.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest metrics** (`metrics.ingest`) |
| Полезная нагрузка | `application/x-protobuf` |

Подробнее см. [API загрузки метрик OpenTelemetry](/docs/dynatrace-api/environment-api/opentelemetry/post-metrics "Send OpenTelemetry metrics to Dynatrace via API.").

События безопасности (новые)

### Предварительные знания

* [Как загружать события безопасности](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail.")
* [Обзор событий на базе Grail (DPS)](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| Конечная точка событий безопасности | `/platform/ingest/v1/security.events` | Встроенный |
| Пользовательский API событий безопасности | `/platform/ingest/custom/security.events/<custom-endpoint-name>` | Пользовательский |

#### Конечная точка событий безопасности (новая)

Загружает события безопасности из встроенных конечных точек.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/v1/security.events` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [OpenPipeline Ingest API — POST встроенные события безопасности (новые)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.").

#### Пользовательский API событий безопасности (новый)

Настраивает пользовательские конечные точки для загрузки событий безопасности.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/security.events` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) |
| Полезная нагрузка | `application/json` |

Подробнее см. [OpenPipeline Ingest API — POST пользовательская конечная точка событий безопасности (новая)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.").

Спаны

### Предварительные знания

* [Как загружать трассировки](/docs/observe/application-observability/distributed-tracing/ingest-traces "Instrument your applications with OneAgent or OpenTelemetry to start ingesting trace data into Dynatrace.")
* [Обзор трассировок на базе Grail (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| OneAgent | `oneagent` | Встроенный |
| OpenTelemetry | `/api/v2/otlp/v1/traces` | Встроенный |

#### OpenTelemetry

Загружает трассировки OpenTelemetry в Dynatrace.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/traces` |
| Метод | POST |
| Аутентификация | [Токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`) |
| Полезная нагрузка | `application/x-protobuf` |

Подробнее см. [API загрузки трассировок OpenTelemetry](/docs/dynatrace-api/environment-api/opentelemetry/post-traces "Send OpenTelemetry traces to Dynatrace via API..").

Системные события

### Предварительные знания

* [Модели системных событий](/docs/semantic-dictionary/model/dt-system-events "Get to know the Semantic Dictionary models related to system events.")
* [Расширения](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* Поддерживаемые системные события в OpenPipeline ограничены следующими:

  + Уведомления о жизненном цикле приложений

    `event.kind == "AUDIT_EVENT" AND event.provider == "APP_REGISTRY"`
  + События выполнения рабочих процессов

    `event.kind == "WORKFLOW_EVENT" AND event.provider == "AUTOMATION_ENGINE"`
  + События самомониторинга ECC

    `event.kind == "EXTENSIONS_EVENT"`

  Чтобы узнать путь и тип системных событий, обрабатываемых в вашем окружении:

  1. Перейдите в **Notebooks**.
  2. Создайте новый блокнот со следующим запросом:

     ```
     fetch dt.system.events



     | filter isNotNull(dt.openpipeline.pipelines)
     ```
  3. Выберите **Run**.

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| System Events API[1](#fn-1-1-def) | `system_events` | Встроенный |
| Расширения | `<extension>` | Готовый |

1

Генерируется внутренне

Пользовательские события и сессии

### Предварительные знания

* [Пользовательские события](/docs/observe/digital-experience/rum-concepts/user-and-error-events "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [Пользовательские сессии](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.")
* Как захватывать пользовательские события и сессии на [Android](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/android/id-09-user-and-session "Identify users across sessions and devices, manage session lifecycle, and attach properties that apply to all events in a session."), [iOS](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/ios/id-09-user-and-session "Identify users, manage sessions, and report session properties in your iOS application."), [Flutter](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/flutter/id-09-user-and-session "Learn how to identify users, manage sessions, and report session properties in your Flutter application.") или [React Native](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/react-native/id-09-user-and-session "Learn how to identify users, manage sessions, and report session properties in your React Native application.")
* [Обзор мониторинга цифрового опыта (DEM) (DPS)](/docs/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| RUM Agent | `rumagent` | Встроенный |

## Связанные темы

* [Поток данных в OpenPipeline](/docs/platform/openpipeline/concepts/data-flow "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.")
* [Как загружать данные (события)](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.")
