---
title: Settings API - Sensitive data masking schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-sensitive-data-masking-settings
scraped: 2026-05-12T11:47:08.412206
---

# Settings API - Sensitive data masking schema table

# Settings API - Sensitive data masking schema table

* Published Dec 05, 2023

### Маскирование чувствительных данных (`builtin:logmonitoring.sensitive-data-masking-settings)`

Создавайте правила маскирования любой информации, которую считаете чувствительной. Маскирование выполняется на OneAgent, никакие персональные данные не отправляются и не хранятся на сервере Dynatrace.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.sensitive-data-masking-settings` | * `group:log-monitoring` * `group:log-monitoring.ingest-and-processing` | `HOST` - Host  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.sensitive-data-masking-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.sensitive-data-masking-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.sensitive-data-masking-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активно `enabled` | boolean | - | Required |
| Имя `config-item-title` | text | - | Required |
| `masking` | [Masking](#Masking) | - | Required |
| `matchers` | Set<[Matcher](#Matcher)> | - | Required |

##### Объект `Masking`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Поисковое выражение `expression` | text | Допускается максимум одна capture-группа. Если она не задана, всё выражение трактуется как capture-группа. | Required |
| Тип маскирования `type` | enum | Возможные значения: * `STRING` * `SHA1` * `SHA256` | Required |
| Замена `replacement` | text | - | Required |

##### Объект `Matcher`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Атрибут `attribute` | enum | Возможные значения: * `dt.entity.process_group` * `log.source` * `log.source.origin` * `host.tag` * `k8s.container.name` * `k8s.namespace.name` * `k8s.deployment.name` * `k8s.pod.annotation` * `k8s.pod.label` * `k8s.workload.name` * `k8s.workload.kind` * `container.name` * `dt.entity.container_group` * `process.technology` | Required |
| Оператор `operator` | enum | Возможные значения: * `MATCHES` | Required |
| `values` | set | - | Required |