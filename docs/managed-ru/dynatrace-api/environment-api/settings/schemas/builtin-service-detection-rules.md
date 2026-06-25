---
title: Settings API - Service detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-rules
scraped: 2026-05-12T11:44:50.609980
---

# Settings API - Service detection schema table

# Settings API - Service detection schema table

* Published Jun 30, 2025

### Обнаружение сервисов (`builtin:service-detection-rules)`

Задайте правила обнаружения и именования сервисов на основе атрибутов ресурсов, определённых в [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields), и пользовательских атрибутов. Правила вычисляются по порядку, применяется первое совпавшее правило.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:service-detection-rules` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-detection-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-rules` |

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
| Условие сопоставления `condition` | text | Ограничивает область правила обнаружения сервиса через условия [DQL matcher](https://dt-url.net/l603wby) на атрибутах ресурсов.  Правило применяется только если условие совпало, иначе вычисление набора правил продолжается.  Если поле пустое, условие всегда совпадает. | Optional |
| Шаблон имени сервиса `serviceNameTemplate` | text | Укажите placeholder'ы атрибутов ресурсов в фигурных скобках, например {service.name} или {k8s.workload.name}.  Все атрибуты, использованные в placeholder, обязательны для применения правила. Если хотя бы один отсутствует, правило не применяется, и вычисление набора правил продолжается.  Все разрешённые значения атрибутов вносят вклад в финальный ID сервиса. | Required |
| Дополнительные атрибуты обнаружения сервиса `additionalRequiredAttributes` | set | Добавьте ключи атрибутов ресурсов (например service.namespace или k8s.workload.kind), которые также обнаруживают уникальные сервисы, но не включаются в отображаемое имя сервиса.  Указанные здесь атрибуты обязательны для применения правила. Если хотя бы один отсутствует, правило не применяется, и вычисление набора правил продолжается.  Все значения атрибутов вносят вклад в финальный ID сервиса. | Required |