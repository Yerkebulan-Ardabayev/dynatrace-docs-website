---
title: Settings API - OpenTelemetry metrics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-opentelemetry-metrics
scraped: 2026-05-12T11:47:59.082555
---

# Settings API - OpenTelemetry metrics schema table

# Settings API - OpenTelemetry metrics schema table

* Published Dec 05, 2023

### OpenTelemetry-метрики (`builtin:opentelemetry-metrics)`

Настройте, как OpenTelemetry-метрики поступают в Dynatrace через OTLP-эндпоинт.

**Примечания:**

* Изменения этих параметров применяются только к новым ingested data points. Уже сохранённые в Dynatrace data points не изменятся.
* Изменения могут повлиять на существующие дашборды, события и оповещения, использующие настроенные здесь dimensions. В этом случае их нужно обновить вручную.
* Параметры с пометкой `(Metrics Classic)` не действуют в Metrics powered by Grail. Для Metrics powered by Grail все атрибуты (resource, scope и metric) принимаются по умолчанию. Используйте block-list, если хотите исключить ingest определённых атрибутов.
* Параметры OpenTelemetry trace/span находятся в: **Settings** > **Server-side service monitoring**.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:opentelemetry-metrics` | * `group:metrics` | `environment`  `environment-default` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:opentelemetry-metrics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:opentelemetry-metrics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:opentelemetry-metrics` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Добавить имя и версию Meter как dimensions метрики (Metrics Classic) `meterNameToDimensionEnabled` | boolean | Если включено, имя Meter (также называемое InstrumentationScope или InstrumentationLibrary в OpenTelemetry SDK) и версия будут добавлены как dimensions (`otel.scope.name` и `otel.scope.version`) к ingested OTLP-метрикам. | Required |
| Расширенные OTLP-dimensions метрики `enableMintV2Ingest` | boolean | Включить расширенные возможности OpenTelemetry-метрик с Grail: обогащение primary field, гибкие dimensions, улучшенный routing, распределение затрат и поддержку запросов с high-cardinality. Подробнее об этом и о влиянии на обогащение dimension `dt.entity.service` см. [этот пост](https://dt-url.net/otlp-metrics-advanced). | Optional |
| Добавить настроенные ниже атрибуты resource и scope как dimensions (Metrics Classic) `additionalAttributesToDimensionEnabled` | boolean | - | Required |
| `additionalAttributes` | Set<[AdditionalAttributeItem](#AdditionalAttributeItem)> | Если включено, атрибуты из списка ниже будут добавлены как dimensions к ingested OTLP-метрикам, если они присутствуют в OpenTelemetry resource или в instrumentation scope.  **Примечания:**  * Атрибуты **обязательно** добавлять в **исходном формате**, в каком они экспортируются в Dynatrace источником телеметрии. Например, если атрибут в `PascalCase`, тот же регистр нужно использовать при добавлении в список. * Dynatrace не рекомендует менять или удалять атрибуты, начинающиеся с "dt.". Dynatrace использует их для [Enrich metrics](https://www.dynatrace.com/support/help/extend-dynatrace/extend-metrics/reference/enrich-metrics). | Required |
| `toDropAttributes` | Set<[DropAttributeItem](#DropAttributeItem)> | Атрибуты из списка ниже будут отбрасываться из всех ingested OTLP-метрик.  **Примечания:**  * Атрибуты **обязательно** добавлять в **исходном формате**, в каком они экспортируются в Dynatrace источником телеметрии. Например, если атрибут в `PascalCase`, тот же регистр нужно использовать при добавлении в список. * Wildcards поддерживаются только в Metrics powered by Grail. * Dynatrace не рекомендует включать в deny list атрибуты, начинающиеся с "dt.". Dynatrace использует их для [Enrich metrics](https://www.dynatrace.com/support/help/extend-dynatrace/extend-metrics/reference/enrich-metrics). | Required |

##### Объект `AdditionalAttributeItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если включено, атрибут будет добавлен как dimension к ingested-метрикам, если присутствует в OpenTelemetry resource или в instrumentation scope. | Required |
| Ключ атрибута `attributeKey` | text | - | Required |

##### Объект `DropAttributeItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если включено, атрибут будет отбрасываться у всех ingested-метрик. | Required |
| Ключ атрибута `attributeKey` | text | - | Required |