---
title: Settings API - Frequency and locations schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-browser-scheduling
scraped: 2026-05-12T11:44:24.889743
---

# Settings API - Frequency and locations schema table

# Settings API - Frequency and locations schema table

* Published Dec 05, 2023

### Частота и расположения (`builtin:synthetic.browser.scheduling)`

Выберите, как часто этот монитор должен выполняться в каждом включённом расположении. Подробнее см. [how do I create a browser monitor?](https://dt-url.net/qj1p0p2b)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.browser.scheduling` | - | `SYNTHETIC_TEST` - Synthetic monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.scheduling` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.browser.scheduling` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.scheduling` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Частота `frequency` | integer | Как часто выполняется монитор. Поддерживаемые значения: 5, 10, 15, 30, 60, 120 и 240 минут | Required |
| Расположения `locations` | Set<[Location](#Location)> | - | Required |

##### Объект `Location`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Расположение `location` | text | - | Required |