---
title: Settings API - Transaction monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-mainframe-txmonitoring
scraped: 2026-05-12T11:40:01.635572
---

# Settings API - Transaction monitoring schema table

# Settings API - Transaction monitoring schema table

* Published Dec 05, 2023

### Мониторинг транзакций (`builtin:mainframe.txmonitoring)`

Задайте дополнительные параметры мониторинга для транзакций CICS и IMS.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:mainframe.txmonitoring` | * `group:mainframe` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.txmonitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:mainframe.txmonitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.txmonitoring` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Мониторить все входящие web-запросы `monitorAllIncomingWebRequests` | boolean | Dynatrace автоматически трассирует входящие web-запросы, когда их вызывают уже мониторимые сервисы. Включите этот параметр, чтобы мониторить все входящие web-запросы. Рекомендуем включать его только на короткое время. | Required |
| Мониторить все EXCI-запросы от CICS Transaction Gateway `monitorAllCtgProtocols` | boolean | Если включено, сенсор CICS Transaction Gateway будет трассировать все EXCI-запросы, в том числе использующие протокол TCP/IP или SNA. | Required |
| Группировать CICS-регионы из одного CICSPlex `groupCicsRegions` | boolean | Если включено, CICS-регионы из одного CICSPlex будут сгруппированы в одну process group. Если отключено, для каждого CICS-региона будет создана отдельная process group. | Required |
| Создавать CICS-сервисы на основе transaction ID `zosCicsServiceDetectionUsesTransactionId` | boolean | Если включено, для каждого мониторимого transaction ID внутри process group будет создан CICS-сервис. Если отключено, для каждого мониторимого CICS-региона внутри process group будет создан CICS-сервис. Рекомендуем включать только если CICS-регионы сгруппированы по CICSPlex. | Required |
| Группировать IMS-регионы из одной подсистемы `groupImsRegions` | boolean | Если включено, IMS-регионы из одной подсистемы будут сгруппированы в одну process group. Если отключено, для каждого IMS-региона будет создана отдельная process group. | Required |
| Создавать IMS-сервисы на основе transaction ID `zosImsServiceDetectionUsesTransactionId` | boolean | Если включено, для каждого мониторимого transaction ID внутри process group будет создан IMS-сервис. Если отключено, для каждого мониторимого IMS-региона внутри process group будет создан IMS-сервис. Рекомендуем включать только если IMS-регионы сгруппированы по подсистемам. | Required |
| Лимит узлов PurePath: максимальное число узлов на вызов CICS/IMS-программы `nodeLimit` | integer | Рекомендуем лимит по умолчанию 500 узлов. Значение 0 означает неограниченное число узлов. | Required |