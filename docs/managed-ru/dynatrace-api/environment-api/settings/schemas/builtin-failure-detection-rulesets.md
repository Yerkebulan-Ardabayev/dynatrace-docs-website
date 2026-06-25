---
title: Settings API - Failure detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-rulesets
scraped: 2026-05-12T11:39:10.783530
---

# Settings API - Failure detection schema table

# Settings API - Failure detection schema table

* Опубликовано 30 июня 2025 г.

### Обнаружение сбоев (`builtin:failure-detection-rulesets)`

Определите rulesets для обнаружения сбоев на основе атрибутов span, описанных в [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/model/trace), и пользовательских атрибутов. Rulesets оцениваются по порядку, и первый совпавший определяет результат обнаружения сбоя.

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:failure-detection-rulesets` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection-rulesets` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection-rulesets` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection-rulesets` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если включено, ruleset будет оцениваться. | Required |
| Ruleset `ruleset` | [Ruleset](#Ruleset) | - | Required |

##### Объект `Ruleset`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя ruleset `rulesetName` | text | - | Required |
| Описание `description` | text | - | Optional |
| Условие совпадения `condition` | text | Ограничивает scope ruleset с помощью условий [DQL matcher](https://dt-url.net/l603wby) на атрибутах span и resource.  Ruleset применяется только при совпадении условия, иначе оценка продолжается.  Если пусто, условие всегда совпадает. | Optional |
| HTTP status codes `failOnHttpResponseStatusCodes` | [failOnHttpResponseStatusCodes](#failOnHttpResponseStatusCodes) | Оцениваемый атрибут: `http.response.status_code`  Результат обнаружения сбоя: `reason="http_code"`, `verdict="failure"` | Required |
| gRPC status codes `failOnGrpcStatusCodes` | [failOnGrpcStatusCodes](#failOnGrpcStatusCodes) | Оцениваемый атрибут: `rpc.grpc.status_code`  Результат обнаружения сбоя: `reason="grpc_code"`, `verdict="failure"` | Required |
| Span status code `failOnSpanStatusError` | [failOnSpanStatusError](#failOnSpanStatusError) | Оцениваемый атрибут: `span.status_code`  Результат обнаружения сбоя: `reason="span_status"`, `verdict="failure"` | Required |
| Exceptions `failOnExceptions` | [failOnExceptions](#failOnExceptions) | Оцениваемое выражение: `iAny(`span.events`[][`span\_event.name`] == "exception" and` span.events`[][`exception.escaped`] != false)`  Результат обнаружения сбоя: `reason="exception"`, `verdict="failure"`, `exception_ids` | Required |
| Custom-правила сбоев `failOnCustomRules` | Set<[customRule](#customRule)> | Задайте причины сбоев на основе атрибутов span и request.  Результат обнаружения сбоя: `reason="custom_rule"`, `verdict="failure"`, `custom_rule_name` | Required |
| `overrides` | [overrides](#overrides) | - | Required |

##### Объект `failOnHttpResponseStatusCodes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Status codes, указывающие на сбой на стороне сервера `statusCodes` | text | - | Required |

##### Объект `failOnGrpcStatusCodes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Status codes, указывающие на сбой на стороне сервера `statusCodes` | text | - | Required |

##### Объект `failOnSpanStatusError`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Считать сбоем при span status "error" `enabled` | boolean | - | Required |

##### Объект `failOnExceptions`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Считать сбоем при exceptions `enabled` | boolean | - | Required |
| `ignoredExceptions` | Set<[singleException](#singleException)> | - | Required |

##### Объект `customRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя правила `ruleName` | text | - | Required |
| DQL-условие `dqlCondition` | text | Custom-правило на основе атрибутов span с использованием [DQL matcher](https://dt-url.net/l603wby). | Required |

##### Объект `overrides`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| HTTP status codes `forceSuccessOnHttpResponseStatusCodes` | [forceSuccessOnHttpResponseStatusCodes](#forceSuccessOnHttpResponseStatusCodes) | Оцениваемый атрибут: `http.response.status_code`  Результат обнаружения сбоя: `reason="http_code"`, `verdict="success"` | Required |
| gRPC status codes `forceSuccessOnGrpcResponseStatusCodes` | [forceSuccessOnGrpcResponseStatusCodes](#forceSuccessOnGrpcResponseStatusCodes) | Оцениваемый атрибут: `rpc.grpc.status_code`  Результат обнаружения сбоя: `reason="grpc_code"`, `verdict="success"` | Required |
| Span status code `forceSuccessOnSpanStatusOk` | [forceSuccessOnSpanStatusOk](#forceSuccessOnSpanStatusOk) | Оцениваемый атрибут: `span.status_code`  Результат обнаружения сбоя: `reason="span_status"`, `verdict="success"` | Required |
| Принудительно success для определённых exceptions `forceSuccessOnExceptions` | Set<[singleException](#singleException)> | Задайте escaped exceptions, которые должны принудительно давать success.  Оцениваемое выражение: `iAny(`span.events`[][`span\_event.name`] == "exception" and` span.events`[][`exception.escaped`] != false)`  Результат обнаружения сбоя: `reason="exception"`, `verdict="success"`, `exception_ids` | Required |
| Custom-правила принудительного success `forceSuccessWithCustomRules` | Set<[customRule](#customRule)> | Переопределить сбои по условиям на атрибутах span и request.  Результат обнаружения сбоя: `reason="custom_rule"`, `verdict="success"`, `custom_rule_name` | Required |

##### Объект `singleException`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Тип exception содержит `type` | text | Оцениваемый атрибут: `span.events[][exception.type]` | Optional |
| Сообщение exception содержит `message` | text | Оцениваемый атрибут: `span.events[][exception.message]` | Optional |

##### Объект `forceSuccessOnHttpResponseStatusCodes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Status codes, принудительно дающие success на стороне сервера `statusCodes` | text | - | Optional |

##### Объект `forceSuccessOnGrpcResponseStatusCodes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Status codes, принудительно дающие success на стороне сервера `statusCodes` | text | - | Optional |

##### Объект `forceSuccessOnSpanStatusOk`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Принудительно success при span status "ok" `enabled` | boolean | - | Required |