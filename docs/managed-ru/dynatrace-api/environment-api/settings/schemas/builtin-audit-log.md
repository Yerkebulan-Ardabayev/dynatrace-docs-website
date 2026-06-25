---
title: Settings API - Log audit events schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-audit-log
scraped: 2026-05-12T11:46:26.657308
---

# Settings API - Log audit events schema table

# Settings API - Log audit events schema table

* Published Dec 05, 2023

### События аудита логов (`builtin:audit-log)`

Если включено, Dynatrace логирует все события, связанные с аудитом, включая входы/выходы, изменения конфигурации и изменения API-токенов. Обратите внимание, что аудит-логи содержат персонально идентифицируемую информацию (PII), такую как email-адреса и IP-адреса пользователей Dynatrace. К событиям аудита можно обращаться через Dynatrace REST API.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:audit-log` | * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:audit-log` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:audit-log` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:audit-log` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Логировать все системные события, связанные с аудитом `enabled` | boolean | - | Required |