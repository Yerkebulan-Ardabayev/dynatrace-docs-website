---
title: Settings API - IBM MQ queue sharing groups schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ibmmq-queue-sharing-group
scraped: 2026-05-12T11:39:36.771316
---

# Settings API - IBM MQ queue sharing groups schema table

# Settings API - IBM MQ queue sharing groups schema table

* Published Dec 05, 2023

### Группы совместного использования очередей IBM MQ (`builtin:ibmmq.queue-sharing-group)`

Группа совместного использования очередей определяет группу менеджеров очередей, которые могут обращаться к одним и тем же общим очередям на z/OS. Dynatrace должен знать, какие менеджеры очередей и общие очереди относятся к какой группе совместного использования очередей для сквозной трассировки на z/OS.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ibmmq.queue-sharing-group` | * `group:mainframe` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.queue-sharing-group` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ibmmq.queue-sharing-group` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.queue-sharing-group` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя группы совместного использования очередей `name` | text | - | Required |
| Менеджеры очередей `queueManagers` | set | - | Required |
| Общие очереди `sharedQueues` | set | - | Required |