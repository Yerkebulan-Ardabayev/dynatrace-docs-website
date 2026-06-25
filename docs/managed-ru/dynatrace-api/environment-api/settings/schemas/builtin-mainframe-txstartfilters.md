---
title: Settings API - Transaction start filters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-mainframe-txstartfilters
scraped: 2026-05-12T11:45:22.964327
---

# Settings API - Transaction start filters schema table

# Settings API - Transaction start filters schema table

* Published Dec 05, 2023

### Фильтры начала транзакций (`builtin:mainframe.txstartfilters)`

Dynatrace автоматически трассирует транзакции CICS и IMS, когда их вызывают мониторимые сервисы. Транзакции, исходящие с mainframe, с терминала или вызываемые немониторимыми сервисами, должны быть явно перечислены для мониторинга.

Добавьте транзакции CICS и IMS, исходящие с терминала (например, IBM 3270 green screen terminal), в фильтр начала терминальных транзакций. Остальные транзакции добавьте в фильтры начала транзакций.

Учтите: трассы, запущенные через фильтры транзакций, никогда не будут связаны с предыдущей трассой, независимо от способа инициации транзакции.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:mainframe.txstartfilters` | * `group:mainframe` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.txstartfilters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:mainframe.txstartfilters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.txstartfilters` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Фильтр начала терминальных транзакций CICS `includedCicsTerminalTransactionIds` | set | Можно использовать \* как wildcard. Например, A\* трассирует все ID транзакций, начинающиеся с A. | Required |
| Фильтр начала транзакций CICS `includedCicsTransactionIds` | set | Можно использовать \* как wildcard. Например, A\* трассирует все ID транзакций, начинающиеся с A. | Required |
| Фильтр начала терминальных транзакций IMS `includedImsTerminalTransactionIds` | set | Можно использовать \* как wildcard. Например, A\* трассирует все ID транзакций, начинающиеся с A. | Required |
| Фильтр начала транзакций IMS `includedImsTransactionIds` | set | Можно использовать \* как wildcard. Например, A\* трассирует все ID транзакций, начинающиеся с A. | Required |