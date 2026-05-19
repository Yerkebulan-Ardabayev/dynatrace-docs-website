---
title: Settings API - Microsoft Entra ID schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-azure-connector-microsoft-entra-identity-developer-connection
scraped: 2026-05-12T11:45:04.750869
---

# Settings API - Microsoft Entra ID schema table

# Settings API - Microsoft Entra ID schema table

* Published Jul 31, 2024

### Microsoft Entra ID (`app:dynatrace.azure.connector:microsoft-entra-identity-developer-connection)`

Настройки аутентификации для Microsoft Entra ID.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.azure.connector:microsoft-entra-identity-developer-connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.azure.connector:microsoft-entra-identity-developer-connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.azure.connector:microsoft-entra-identity-developer-connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.azure.connector:microsoft-entra-identity-developer-connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Имя подключения Microsoft Entra ID | Required |
| Описание `description` | text | - | Optional |
| ID каталога (тенанта) `directoryId` | secret | ID каталога (тенанта) Microsoft Entra ID | Required |
| ID приложения (клиента) `applicationId` | secret | ID приложения (клиента) вашего приложения, зарегистрированного в Microsoft Azure App registrations | Required |
| Секрет клиента `clientSecret` | secret | Секрет клиента вашего приложения, зарегистрированного в Microsoft Azure App registrations | Required |