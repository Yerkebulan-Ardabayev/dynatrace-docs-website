---
title: Settings API - IBM MQ filters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-mainframe-mqfilters
scraped: 2026-05-12T11:41:19.274971
---

# Settings API - IBM MQ filters schema table

# Settings API - IBM MQ filters schema table

* Published Dec 05, 2023

### Фильтры IBM MQ (`builtin:mainframe.mqfilters)`

Dynatrace автоматически трассирует транзакции CICS и IMS, исходящие из очередей IBM MQ. Чтобы ограничить трассировку определёнными очередями, укажите их имена в списках включения. Чтобы исключить очереди из трассировки, укажите их имена в списках исключения. Для IMS эти списки применяются к регионам обработки сообщений.

Чтобы трассировать только определённые транзакции, отправленные через IMS bridge, укажите их идентификаторы транзакций в списке включения или исключения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:mainframe.mqfilters` | * `group:mainframe` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.mqfilters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:mainframe.mqfilters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.mqfilters` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| CICS: включённые очереди MQ `cicsMqQueueIdIncludes` | set | - | Required |
| CICS: исключённые очереди MQ `cicsMqQueueIdExcludes` | set | - | Required |
| IMS: включённые очереди MQ `imsMqQueueIdIncludes` | set | - | Required |
| IMS: исключённые очереди MQ `imsMqQueueIdExcludes` | set | - | Required |
| IMS bridge: включённые ID транзакций `imsCrTrnIdIncludes` | set | Когда вы добавляете ID транзакции в список включения, все остальные транзакции игнорируются. | Required |
| IMS bridge: исключённые ID транзакций `imsCrTrnIdExcludes` | set | Когда вы добавляете ID транзакции в список исключения, остальные транзакции продолжают мониториться. | Required |