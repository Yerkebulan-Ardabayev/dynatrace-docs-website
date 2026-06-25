---
title: Settings API - Custom units schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-custom-unit
scraped: 2026-05-12T11:48:18.775401
---

# Settings API - Custom units schema table

# Settings API - Custom units schema table

* Published Dec 05, 2023

### Пользовательские единицы (`builtin:custom-unit)`

Здесь вы можете создавать пользовательские единицы.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:custom-unit` | * `group:metrics` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:custom-unit` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:custom-unit` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:custom-unit` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя единицы `newUnitName` | text | Имя единицы должно быть уникальным и используется как идентификатор.  Например: Byte, Second, BytePerMinute | Required |
| Имя единицы во множественном числе `newUnitPluralName` | text | Имя во множественном числе представляет форму множественного числа имени единицы.  Например: Bytes, Seconds | Required |
| Символ единицы `newUnitSymbol` | text | Символ единицы должен быть уникальным.  Например: s, m/s, B/min, bit/s | Required |
| Описание единицы `newUnitDescription` | text | Описание единицы должно содержать дополнительную информацию о новой единице.  Например: Byte: 8 bits of information | Required |