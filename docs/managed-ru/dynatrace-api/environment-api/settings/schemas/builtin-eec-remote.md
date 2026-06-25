---
title: Settings API - Extension Execution Controller schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-eec-remote
scraped: 2026-05-12T11:40:40.434650
---

# Settings API - Extension Execution Controller schema table

# Settings API - Extension Execution Controller schema table

* Published Dec 05, 2023

### Extension Execution Controller (`builtin:eec.remote)`

Конфигурация Extension Execution Controller для развёртывания ActiveGate

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:eec.remote` | - | `ENVIRONMENT_ACTIVE_GATE` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eec.remote` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:eec.remote` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eec.remote` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Профиль производительности `performanceProfile` | enum | Select performance profile for Extension Execution Controller [Documentation](https://www.dynatrace.com/support/help/shortlink/extensions-concepts#resource-consumption "More about performance profiles") Возможные значения: * `DEFAULT` * `HIGH` * `DEDICATED` | Required |