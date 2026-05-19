---
title: Settings API - Compliance Assistant schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-compliance-assistant-comp-ass-settings
scraped: 2026-05-12T11:46:02.280597
---

# Settings API - Compliance Assistant schema table

# Settings API - Compliance Assistant schema table

* Published Sep 25, 2025

### Compliance Assistant (`app:dynatrace.compliance.assistant:comp-ass-settings)`

Настройки для приложения Compliance Assistant

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.compliance.assistant:comp-ass-settings` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.compliance.assistant:comp-ass-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.compliance.assistant:comp-ass-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.compliance.assistant:comp-ass-settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Конфигурации фреймворков `frameworks` | [frameworks](#frameworks) | - | Optional |

##### Объект `frameworks`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| DORA `dora` | [frameworks.dora](#frameworks.dora) | - | Optional |

##### Объект `frameworks.dora`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Критические или важные функции (CIF) `cifs` | [frameworks.dora.cif](#frameworks.dora.cif)[] | - | Required |

##### Объект `frameworks.dora.cif`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID `ID` | text | - | Optional |
| Затраты `cost` | [frameworks.dora.cost](#frameworks.dora.cost) | - | Optional |
| Дата изменения `dateModified` | zoned\_date\_time | - | Optional |
| Кем изменено `userModified` | text | - | Optional |

##### Объект `frameworks.dora.cost`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Сумма `value` | float | - | Optional |
| Валюта `currency` | text | - | Optional |