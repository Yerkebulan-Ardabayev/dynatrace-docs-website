---
title: Settings API - Cloud Development Environments schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-app-engine-registry-cloud-development-environments
scraped: 2026-05-12T11:41:39.995395
---

# Settings API - Cloud Development Environments schema table

# Settings API - Cloud Development Environments schema table

* Published Nov 04, 2024

### Cloud Development Environments (`builtin:app-engine-registry.cloud-development-environments)`

Чтобы включить Cloud Development Environment (CDE) для разработки приложений, здесь нужно настроить соответствующие домены.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:app-engine-registry.cloud-development-environments` | * `group:dt-apps-development` * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-engine-registry.cloud-development-environments` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:app-engine-registry.cloud-development-environments` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-engine-registry.cloud-development-environments` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Cloud Development Environments `cloudDevelopmentEnvironments` | set | URL, с которого разрешена разработка приложений. Например `https://*.my-company.my-cde-provider.com`. | Required |