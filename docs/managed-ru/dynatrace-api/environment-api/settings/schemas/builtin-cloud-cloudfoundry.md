---
title: Settings API - Cloud Foundry schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-cloudfoundry
scraped: 2026-05-12T11:45:38.821268
---

# Settings API - Cloud Foundry schema table

# Settings API - Cloud Foundry schema table

* Published Dec 05, 2023

### Cloud Foundry (`builtin:cloud.cloudfoundry)`

Используйте эту страницу для подключения Cloud Foundry к Dynatrace для мониторинга. Подготовьте целевой URL Cloud Foundry API, endpoint аутентификации и имя пользователя и пароль Cloud Foundry.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:cloud.cloudfoundry` | * `group:cloud-and-virtualization` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.cloudfoundry` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:cloud.cloudfoundry` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.cloudfoundry` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя этого подключения `label` | text | - | Required |
| Целевой Cloud Foundry API `apiUrl` | text | - | Required |
| Endpoint аутентификации Cloud Foundry `loginUrl` | text | - | Required |
| Имя пользователя Cloud Foundry `username` | text | - | Required |
| Пароль Cloud Foundry `password` | secret | - | Required |
| Группа ActiveGate `activeGateGroup` | text | - | Optional |