---
title: Settings API - Service Detection v2 for OneAgent schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-v2-for-oneagent
scraped: 2026-05-12T11:48:55.475559
---

# Settings API - Service Detection v2 for OneAgent schema table

# Settings API - Service Detection v2 for OneAgent schema table

* Published Sep 25, 2025

### Service Detection v2 для OneAgent (`builtin:service-detection-v2-for-oneagent)`

Включение SDv2 для OneAgent задействует те же attribute-based правила, что и OpenTelemetry, для обнаружения сервисов, эндпоинтов и failure. Подробнее см. в [SDv2 documentation](https://dt-url.net/5e0309z).

Это **Public Preview**-функция. До включения необходимо заполнить [access request form and agree to preview terms](https://dt-url.net/cb300tiz).

**Важно**

Сервисы, попадающие под ваши условия, получат новые ключи метрик, что сломает существующие API-запросы, дашборды и имена сервисов. Custom, opaque, third party, database и message queue-сервисы в SDv2 определяются иначе. Аналитические представления для операций service-to-database и message queue будут анонсированы в будущих релизах.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:service-detection-v2-for-oneagent` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection-v2-for-oneagent` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить Service Detection v2 для Kubernetes-workload `enableSDV2ForKubernetesWorkloads` | boolean | - | Required |
| Условие сопоставления для Kubernetes-workload `condition` | text | Ограничивает scope opt-in фильтрацией [DQL matcher](https://dt-url.net/l603wby)-условиями по выбранному набору атрибутов.  Service detection v2 применяется только если это условие совпало. Допустимые атрибуты: Resource attributes и custom attributes. Если поле пустое, условие всегда совпадает. | Required |
| Включить Service Detection v2 для FaaS `enableSDV2ForFaaS` | boolean | - | Optional |
| Условие сопоставления для FaaS `conditionForFaaS` | text | Ограничивает scope opt-in фильтрацией [DQL matcher](https://dt-url.net/l603wby)-условиями по выбранному набору атрибутов.  Service detection v2 применяется только если это условие совпало. Допустимые атрибуты: Resource attributes и custom attributes. Если поле пустое, условие всегда совпадает. | Required |
| Условие сопоставления для любого workload `conditionForAnyWorkload` | text | Ограничивает scope opt-in фильтрацией [DQL matcher](https://dt-url.net/l603wby)-условиями по выбранному набору атрибутов. Resource attributes должны присутствовать.  Service detection v2 применяется только если это условие совпало. Допустимые атрибуты: Resource attributes и custom attributes. Если поле пустое, условие всегда совпадает. Если набор resource attributes отсутствует или пуст, условие считается несовпавшим. | Required |