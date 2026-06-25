---
title: Settings API - IBM MQ queue managers schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ibmmq-queue-managers
scraped: 2026-05-12T11:49:34.739855
---

# Settings API - IBM MQ queue managers schema table

# Settings API - IBM MQ queue managers schema table

* Published Dec 05, 2023

### Менеджеры очередей IBM MQ (`builtin:ibmmq.queue-managers)`

Dynatrace нужно знать определения IBM MQ для alias-очередей, удалённых очередей и cluster-очередей для end-to-end-трассировки. Без этой информации Dynatrace по-прежнему трассирует все запросы, но producer- и consumer-сервисы не будут сшиты вместе.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ibmmq.queue-managers` | * `group:mainframe` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.queue-managers` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ibmmq.queue-managers` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.queue-managers` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя менеджера очередей `name` | text | - | Required |
| Кластеры `clusters` | set | Имя кластера/кластеров, в который входит этот менеджер очередей | Required |
| Alias-очереди `aliasQueues` | Set<[AliasQueue](#AliasQueue)> | - | Required |
| Удалённые очереди `remoteQueues` | Set<[RemoteQueue](#RemoteQueue)> | - | Required |
| Cluster-очереди `clusterQueues` | Set<[ClusterQueue](#ClusterQueue)> | - | Required |

##### Объект `AliasQueue`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя alias-очереди `aliasQueue` | text | - | Required |
| Имя базовой очереди `baseQueue` | text | - | Required |
| Видимость в кластере `clusterVisibility` | set | Имя кластера/кластеров, в которых должен быть виден этот alias | Required |

##### Объект `RemoteQueue`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя локальной очереди `localQueue` | text | - | Required |
| Имя удалённой очереди `remoteQueue` | text | - | Required |
| Имя удалённого менеджера очередей `remoteQueueManager` | text | - | Required |
| Видимость в кластере `clusterVisibility` | set | Имя кластера/кластеров, в которых должно быть видно это локальное определение удалённой очереди | Required |

##### Объект `ClusterQueue`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя локальной очереди `localQueue` | text | - | Required |
| Видимости в кластерах `clusterVisibility` | set | Имя кластера/кластеров, в которых должна быть видна эта локальная очередь | Required |