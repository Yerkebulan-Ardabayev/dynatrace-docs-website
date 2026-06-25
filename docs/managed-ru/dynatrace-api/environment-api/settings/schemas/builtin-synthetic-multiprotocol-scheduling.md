---
title: Settings API - Frequency and locations schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-scheduling
scraped: 2026-05-12T11:48:22.568821
---

# Settings API - Frequency and locations schema table

# Settings API - Frequency and locations schema table

* Published Jul 31, 2024

### Частота и расположения (`builtin:synthetic.multiprotocol.scheduling)`

Выберите, как часто этот монитор должен выполняться в каждом включённом расположении.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.multiprotocol.scheduling` | - | `MULTIPROTOCOL_MONITOR` - Network availability monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.scheduling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.multiprotocol.scheduling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.scheduling` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Частота `frequency` | integer | Как часто выполняется монитор. Поддерживаемые значения: 1, 2, 5, 10, 15, 30 и 60 минут | Required |
| Расположения `locations` | Set<[Location](#Location)> | - | Required |

##### The `Location` object

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Расположение `location` | text | - | Optional |