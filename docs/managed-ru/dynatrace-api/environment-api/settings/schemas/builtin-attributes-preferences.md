---
title: Settings API - Preferences schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-attributes-preferences
scraped: 2026-05-12T11:40:33.794350
---

# Settings API - Preferences schema table

# Settings API - Preferences schema table

* Published Feb 26, 2024

### Настройки (`builtin:attributes-preferences)`

Задайте поведение сохранения атрибутов OpenTelemetry по умолчанию. Вы можете хранить все атрибуты, кроме определённых заблокированных, или хранить только явно разрешённые атрибуты.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:attributes-preferences` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attributes-preferences` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:attributes-preferences` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attributes-preferences` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `persistenceMode` | enum | Возможные значения: * `ALLOW_ALL_ATTRIBUTES` * `BLOCK_ALL_ATTRIBUTES` | Required |