---
title: Settings API - Service splitting schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-splitting-rules
scraped: 2026-05-12T11:43:39.949574
---

# Settings API - Service splitting schema table

# Settings API - Service splitting schema table

* Published Jun 30, 2025

### Разделение сервисов (`builtin:service-splitting-rules)`

Задайте правила разделения сервисов на основе атрибутов ресурсов из [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields) и пользовательских атрибутов. Правила вычисляются по порядку, применяется первое совпавшее.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:service-splitting-rules` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-splitting-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-splitting-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-splitting-rules` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Если включено, правило будет вычисляться. | Required |
| Правило `rule` | [Rule](#Rule) | - | Required |

##### Объект `Rule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя правила `ruleName` | text | - | Required |
| Описание `description` | text | - | Optional |
| Условие сопоставления `condition` | text | Ограничивает область правила разделения сервисов через условия [DQL matcher](https://dt-url.net/l603wby) на атрибутах ресурсов.  Правило применяется только если условие совпало, иначе вычисление набора правил продолжается.  Если поле пустое, условие всегда совпадает. | Optional |
| Разделять сервисы по атрибутам ресурсов `serviceSplittingAttributes` | Set<[splitBy](#splitBy)> | Задайте полный набор атрибутов ресурсов, по которым следует разделять сервисы в области сопоставления.  Каждый существующий атрибут вносит вклад в финальный ID сервиса. | Required |

##### Объект `splitBy`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ атрибута `key` | text | - | Required |