---
title: Settings API - Monitor name schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-browser-name
scraped: 2026-05-12T11:40:58.787262
---

# Settings API - Monitor name schema table

# Settings API - Monitor name schema table

* Published Dec 05, 2023

### Имя монитора (`builtin:synthetic.browser.name)`

Задайте отображаемое имя браузерного монитора

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.browser.name` | * `group:synthetic.browser` | `SYNTHETIC_TEST` - Synthetic monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.browser.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.browser.name` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя монитора `name` | text | - | Required |
| Описание монитора `description` | text | - | Optional |