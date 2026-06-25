---
title: Settings API - OneAgent features schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-oneagent-features
scraped: 2026-05-12T11:45:50.229793
---

# Settings API - OneAgent features schema table

# Settings API - OneAgent features schema table

* Published Dec 05, 2023

### Возможности OneAgent (`builtin:oneagent.features)`

Dynatrace OneAgent работает по принципу zero-configuration. Поэтому при первом развёртывании OneAgent применяется набор возможностей по умолчанию. Когда с новыми версиями OneAgent появляются дополнительные возможности, их можно активировать здесь, чтобы сделать доступными во всём окружении.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:oneagent.features` | * `group:preferences` | `PROCESS_GROUP_INSTANCE` - Process  `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Инструментирование включено (для изменения требуется перезапуск процесса) `instrumentation` | boolean | - | Optional |
| Активировать эту возможность также в OneAgent, удовлетворяющих только минимальной Opt-In версии `forcible` | boolean | - | Optional |
| Возможность `key` | text | - | Required |