---
title: Settings API - OneAgent features schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-oneagent-features
---

# Settings API - OneAgent features schema table

# Settings API - OneAgent features schema table

* Опубликовано 05 дек. 2023

### OneAgent features (`builtin:oneagent.features)`

Dynatrace OneAgent придерживается подхода zero-configuration. Поэтому при первом развёртывании OneAgent применяется набор функций по умолчанию. Когда с новыми версиями OneAgent появляются дополнительные функции, их можно активировать здесь, чтобы они стали доступны во всём окружении.

| Идентификатор схемы | Группы схем | Область применения |
| --- | --- | --- |
| `builtin:oneagent.features` | * `group:preferences` | `PROCESS_GROUP_INSTANCE` - Процесс  `PROCESS_GROUP` - Группа процессов  `CLOUD_APPLICATION` - Рабочая нагрузка Kubernetes  `CLOUD_APPLICATION_NAMESPACE` - Пространство имён Kubernetes  `KUBERNETES_CLUSTER` - Кластер Kubernetes  `environment` |

Получение схемы через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:oneagent.features` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.features` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью **Read settings** (`settings.read`). Как получить и использовать токен, описано в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Обязательно |
| Instrumentation enabled `instrumentation` | boolean | - | Необязательно |
| Activate this feature also in OneAgents only fulfilling the minimum Opt-In version `forcible` | boolean | - | Необязательно |
| Feature `key` | text | - | Обязательно |