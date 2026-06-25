---
title: Settings API - IBM MQ IMS bridges schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ibmmq-ims-bridges
scraped: 2026-05-12T11:42:58.860388
---

# Settings API - IBM MQ IMS bridges schema table

# Settings API - IBM MQ IMS bridges schema table

* Published Dec 05, 2023

### Мосты IBM MQ IMS (`builtin:ibmmq.ims-bridges)`

IMS-мост: компонент IBM MQ для z/OS, обеспечивающий прямой доступ к системе IMS. Dynatrace должен знать, какие менеджеры очередей и очереди относятся к какому IMS-мосту для сквозной трассировки на z/OS.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ibmmq.ims-bridges` | * `group:mainframe` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.ims-bridges` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ibmmq.ims-bridges` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.ims-bridges` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя IMS-моста `name` | text | - | Required |
| Менеджеры очередей `queueManagers` | Set<[QueueManager](#QueueManager)> | - | Required |

##### The `QueueManager` object

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя менеджера очередей `name` | text | - | Required |
| Очереди `queueManagerQueue` | set | - | Required |