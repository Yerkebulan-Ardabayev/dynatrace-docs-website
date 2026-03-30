---
title: Источники загрузки данных в OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/reference/api-ingestion-reference
scraped: 2026-03-06T21:16:01.329825
---

В этой статье вы найдете справочные материалы по источникам загрузки данных в OpenPipeline, разделенные по каждой области конфигурации. Включены:

* Доступные источники загрузки данных и связанный `dt.openpipeline.source`
* Спецификация API загрузки данных, такая как URL-адрес конечной точки и метод аутентификации
* Предварительные знания, такие как концепции, совместимость лицензирования и настройка

Параметры запроса

Каждый параметр запроса становится атрибутом верхнего уровня записи. Если в полезной нагрузке уже существует атрибут с тем же именем, атрибут из параметра запроса переопределяет существующее значение атрибута. Переопределенное исходное значение сохраняется в новом поле с синтаксисом имени `overwritten<index>.<original field name>`, например, `overwritten1.myField`.

Бизнес-события

### Предварительные знания

* Как захватывать бизнес-события
* [Этап извлечения данных OpenPipeline](../concepts/processing.md#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* DDU для бизнес-событий

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
| Аутентификация | [OAuth](../../../observe/business-observability/bo-api-ingest.md#oauth "Set up authentication for and ingest business events via API.") [Токен доступа](../../../observe/business-observability/bo-api-ingest.md#access-token "Set up authentication for and ingest business events via API.") с областью действия токена **Ingest bizevents** (`bizevents.ingest`) |
| Полезная нагрузка | `application/json` `application/cloudevent+json` `application/cloudevent-batch+json` |

Подробнее см. Загрузка бизнес-событий через API.

Логи

### Предварительные знания

* Как загружать логи
* Потоковая передача логов через Amazon Data Firehose
* DDU для управления и аналитики логов или Аналитика логов (DPS)

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
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия **Ingest logs** (`logs.ingest`) |
| Полезная нагрузка | `text/plain` `application/json` |

Подробнее см. Log Monitoring API v2 — POST загрузка логов.

#### OpenTelemetry

Отправляет пользовательские логи в Dynatrace.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs` |
| Метод | POST |
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest logs** (`logs.ingest`) |
| Полезная нагрузка | `application/x-protobuf` |

Подробнее см. Загрузка логов OTLP.

События (общие события)

### Предварительные знания

* Обзор событий на базе Grail (DPS)

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
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Events** (`openpipeline.events`) |
| Полезная нагрузка | `application/json` |

Подробнее см. OpenPipeline Ingest API — POST встроенные общие события.

#### Пользовательский API

Настраивает пользовательские конечные точки для загрузки общих событий.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events` |
| Метод | POST |
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Events (Custom)** (`openpipeline.events.custom`) |
| Полезная нагрузка | `application/json` |

Подробнее см. OpenPipeline Ingest API — POST пользовательская конечная точка общих событий.

События — события Davis

### Предварительные знания

* События Davis
* [Этап извлечения данных OpenPipeline](../concepts/processing.md#stage "Learn the core concepts of Dynatrace OpenPipeline processing.")
* Обзор событий на базе Grail (DPS)

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
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest Events** (`events.ingest`) |
| Полезная нагрузка | `application/json` |

Подробнее см. Events API v2 — POST событие.

События — проблемы Davis

### Предварительные знания

* Проблемы Davis
* [Классический анализ первопричин](../../../dynatrace-intelligence/root-cause-analysis/concepts.md#root-cause-analysis "Get acquainted with root cause analysis concepts.")
* Обзор событий на базе Grail (DPS)

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| Классический анализ первопричин | *(нет)* | Встроенный |

События — события SDLC

### Предварительные знания

* Как загружать события SDLC events which you can then ingest to use to generate analytics.")
* Обзор событий на базе Grail (DPS)

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
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Events, Security Development Lifecycle** (`openpipeline.sdlc`) |
| Полезная нагрузка | `application/json` |

Подробнее см. OpenPipeline Ingest API — POST встроенные события SDLC.

#### Пользовательская конечная точка для событий жизненного цикла разработки ПО

Настраивает пользовательские конечные точки для загрузки событий SDLC.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.sdlc` |
| Метод | POST |
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Events, Security Development Lifecycle (Custom)** (`openpipeline.sdlc.custom`) |
| Полезная нагрузка | `application/json` |

Подробнее см. OpenPipeline Ingest API — POST пользовательская конечная точка событий SDLC.

События — события безопасности

Мигрируйте до декабря 2025 г.

Конечные точки `events.security` планируется объявить устаревшими. Перенесите свои конфигурации на конечные точки `security.events` до **конца декабря 2025 г.**. Предыдущие конечные точки останутся доступными **до завершения миграции**.

Полный обзор изменений и пошаговые инструкции по миграции см. в Руководстве по миграции таблиц безопасности Grail.

### Предварительные знания

* [Как загружать события безопасности](../../../secure/threat-observability/security-events-ingest.md#ingest "Ingest external security data into Grail.")
* Обзор событий на базе Grail (DPS)

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
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) |
| Полезная нагрузка | `application/json` |

Подробнее см. OpenPipeline Ingest API — POST встроенные события безопасности (устаревшие).

#### Пользовательский API событий безопасности (устаревший)

Настраивает пользовательские конечные точки для загрузки событий безопасности. Подробнее см. Загрузка пользовательских событий безопасности через API.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/events.security` |
| Метод | POST |
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) |
| Полезная нагрузка | `application/json` |

Подробнее см. OpenPipeline Ingest API — POST пользовательская конечная точка событий безопасности (устаревшая).

Метрики

### Предварительные знания

* Как загружать метрики
* Обзор метрик на базе Grail (DPS)

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
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest metrics** (`metrics.ingest`) |
| Полезная нагрузка | `text/plain` |

Подробнее см. Metrics API — POST загрузка точек данных.

#### OpenTelemetry

Загружает метрики OpenTelemetry в Dynatrace.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics` |
| Метод | POST |
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest metrics** (`metrics.ingest`) |
| Полезная нагрузка | `application/x-protobuf` |

Подробнее см. API загрузки метрик OpenTelemetry.

События безопасности (новые)

### Предварительные знания

* [Как загружать события безопасности](../../../secure/threat-observability/security-events-ingest.md#ingest "Ingest external security data into Grail.")
* Обзор событий на базе Grail (DPS)

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
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Security Events (Built-in)** (`openpipeline.events_security`) |
| Полезная нагрузка | `application/json` |

Подробнее см. OpenPipeline Ingest API — POST встроенные события безопасности (новые).

#### Пользовательский API событий безопасности (новый)

Настраивает пользовательские конечные точки для загрузки событий безопасности.

| Свойство | Спецификация |
| --- | --- |
| URL конечной точки | `https://{your-environment-id}.live.dynatrace.com/platform/ingest/custom/security.events` |
| Метод | POST |
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **OpenPipeline - Ingest Security Events (Custom)** (`openpipeline.events_security.custom`) |
| Полезная нагрузка | `application/json` |

Подробнее см. OpenPipeline Ingest API — POST пользовательская конечная точка событий безопасности (новая).

Спаны

### Предварительные знания

* Как загружать трассировки
* Обзор трассировок на базе Grail (DPS) model.")

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
| Аутентификация | [Токен доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью действия токена **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`) |
| Полезная нагрузка | `application/x-protobuf` |

Подробнее см. API загрузки трассировок OpenTelemetry.

Системные события

### Предварительные знания

* Модели системных событий
* Расширения
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

* Пользовательские события
* Пользовательские сессии
* Как захватывать пользовательские события и сессии на Android, iOS, Flutter или React Native
* Обзор мониторинга цифрового опыта (DEM) (DPS) consumption is calculated using the Dynatrace Platform Subscription model.")

### Источники загрузки данных

| Источник загрузки | dt.openpipeline.source | Тип |
| --- | --- | --- |
| RUM Agent | `rumagent` | Встроенный |

## Связанные темы

* Поток данных в OpenPipeline
* Как загружать данные (события)
