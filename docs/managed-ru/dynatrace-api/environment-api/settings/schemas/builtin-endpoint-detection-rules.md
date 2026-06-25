---
title: Settings API - Endpoint detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-endpoint-detection-rules
scraped: 2026-05-12T11:44:40.360963
---

# Settings API - Endpoint detection schema table

# Settings API - Endpoint detection schema table

* Published Aug 25, 2025

### Обнаружение endpoint'ов (`builtin:endpoint-detection-rules)`

Задайте правила обнаружения запросов на endpoint'ах на основе атрибутов span, определённых в [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields), и пользовательских атрибутов. Правила вычисляются по порядку, применяется первое совпавшее правило.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:endpoint-detection-rules` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:endpoint-detection-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:endpoint-detection-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:endpoint-detection-rules` |

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
| Условие сопоставления `condition` | text | Ограничивает область правила обнаружения endpoint через условия [DQL matcher](https://dt-url.net/l603wby) на атрибутах span и ресурсов.  Правило применяется только если условие совпало, иначе вычисление набора правил продолжается.  Если поле пустое, условие всегда совпадает. | Optional |
| Если условие совпало `ifConditionMatches` | enum | Возможные значения: * `DETECT_REQUEST_ON_ENDPOINT` * `SUPPRESS_REQUEST` | Required |
| Шаблон имени endpoint `endpointNameTemplate` | text | Укажите placeholder'ы атрибутов в фигурных скобках, например {http.route} или {rpc.method}.  Placeholder'ы значений атрибутов следует указывать в фигурных скобках, например {http.route}, {rpc.method}. Все атрибуты, использованные в placeholder, обязательны для применения правила. Если хотя бы один отсутствует, правило не применяется, и вычисление набора правил продолжается.  Если разрешённое имя endpoint на данном span пустое, запрос игнорируется. | Required |