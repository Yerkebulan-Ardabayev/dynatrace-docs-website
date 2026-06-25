---
title: Settings API - Span context propagation schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-span-context-propagation
scraped: 2026-05-12T11:49:49.829771
---

# Settings API - Span context propagation schema table

# Settings API - Span context propagation schema table

* Published Dec 05, 2023

### Распространение контекста span (`builtin:span-context-propagation)`

Распространение контекста позволяет соединять PurePath'ы через OpenTelemetry. Задайте правила, чтобы включить распространение контекста для определённых span внутри OneAgent.

Примечание: эта конфигурация не применяется к Trace ingest.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:span-context-propagation` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-context-propagation` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:span-context-propagation` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-context-propagation` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Правило распространения контекста `contextPropagationRule` | [SpanContextPropagationRule](#SpanContextPropagationRule) | - | Required |

##### Объект `SpanContextPropagationRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя правила `ruleName` | text | - | Required |
| Действие правила `ruleAction` | enum | Возможные значения: * `PROPAGATE` * `DONT_PROPAGATE` | Required |
| Сопоставители `matchers` | [SpanMatcher](#SpanMatcher)[] | - | Required |

##### Объект `SpanMatcher`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Источник `source` | enum | Возможные значения: * `SPAN_NAME` * `SPAN_KIND` * `ATTRIBUTE` * `INSTRUMENTATION_SCOPE_NAME` * `INSTRUMENTATION_SCOPE_VERSION` | Required |
| Ключ `sourceKey` | text | - | Required |
| Тип сравнения `type` | enum | влияет на значение Возможные значения: * `EQUALS` * `CONTAINS` * `STARTS_WITH` * `ENDS_WITH` * `DOES_NOT_EQUAL` * `DOES_NOT_CONTAIN` * `DOES_NOT_START_WITH` * `DOES_NOT_END_WITH` | Required |
| Значение `value` | text | вычисляется при инжекции контекста | Required |
| Значение `spanKindValue` | enum | Возможные значения: * `INTERNAL` * `SERVER` * `CLIENT` * `PRODUCER` * `CONSUMER` | Required |
| С учётом регистра `caseSensitive` | boolean | влияет на значение и ключ | Required |