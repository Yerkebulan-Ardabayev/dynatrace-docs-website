---
title: Settings API - Span capturing schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-span-capturing
scraped: 2026-05-12T11:43:10.319873
---

# Settings API - Span capturing schema table

# Settings API - Span capturing schema table

* Published Dec 05, 2023

### Захват span'ов (`builtin:span-capturing)`

Span'ы OpenTelemetry захватываются по умолчанию. Задайте правила для исключения конкретных span'ов.

Примечание: эта конфигурация не применяется к Trace ingest.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:span-capturing` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-capturing` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:span-capturing` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-capturing` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Правило захвата span `spanCaptureRule` | [SpanCaptureRule](#SpanCaptureRule) | - | Required |

##### Объект `SpanCaptureRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя правила `ruleName` | text | - | Required |
| Действие правила `ruleAction` | enum | Возможные значения: * `CAPTURE` * `IGNORE` | Required |
| Сопоставители `matchers` | [SpanMatcher](#SpanMatcher)[] | - | Required |

##### Объект `SpanMatcher`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Источник `source` | enum | Возможные значения: * `SPAN_NAME` * `SPAN_KIND` * `ATTRIBUTE` * `INSTRUMENTATION_SCOPE_NAME` * `INSTRUMENTATION_SCOPE_VERSION` | Required |
| Ключ `sourceKey` | text | - | Required |
| Тип сравнения `type` | enum | влияет на значение Возможные значения: * `EQUALS` * `CONTAINS` * `STARTS_WITH` * `ENDS_WITH` * `DOES_NOT_EQUAL` * `DOES_NOT_CONTAIN` * `DOES_NOT_START_WITH` * `DOES_NOT_END_WITH` | Required |
| Значение `value` | text | вычисляется в начале span | Required |
| Значение `spanKindValue` | enum | Возможные значения: * `INTERNAL` * `SERVER` * `CLIENT` * `PRODUCER` * `CONSUMER` | Required |
| С учётом регистра `caseSensitive` | boolean | влияет на значение и ключ | Required |