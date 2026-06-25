---
title: Settings API - Monitor name schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-http-name
scraped: 2026-05-12T11:39:26.602996
---

# Settings API - Monitor name schema table

# Settings API - Monitor name schema table

* Published Dec 05, 2023

### Имя монитора (`builtin:synthetic.http.name)`

Задайте отображаемое имя HTTP-монитора

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.http.name` | * `group:synthetic.http` | `HTTP_CHECK` - HTTP monitor |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.http.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.http.name` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя монитора `name` | text | - | Required |
| Описание монитора `description` | text | - | Optional |