---
title: Settings API - Connections to Azure environments schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-hyperscaler-authentication-connections-azure
scraped: 2026-05-12T11:41:34.393766
---

# Settings API - Connections to Azure environments schema table

# Settings API - Connections to Azure environments schema table

* Published Sep 25, 2025

### Подключения к Azure-окружениям (`builtin:hyperscaler-authentication.connections.azure)`

Подключения к Azure для интеграций Dynatrace

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:hyperscaler-authentication.connections.azure` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.azure` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.azure` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.azure` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | Имя подключения | Required |
| Тип подключения `type` | enum | Механизм аутентификации Azure, используемый подключением Возможные значения: * `clientSecret` * `federatedIdentityCredential` | Required |
| `clientSecret` | [ClientSecretConfig](#ClientSecretConfig) | - | Required |
| `federatedIdentityCredential` | [FederatedIdentityCredential](#FederatedIdentityCredential) | - | Required |

##### Объект `ClientSecretConfig`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID каталога (tenant) `directoryId` | text | Directory (tenant) ID Microsoft Entra ID | Required |
| ID приложения (client) `applicationId` | text | Application (client) ID вашего приложения, зарегистрированного в Microsoft Azure App registrations | Required |
| Client secret `clientSecret` | secret | Client secret вашего приложения, зарегистрированного в Microsoft Azure App registrations | Required |
| Потребители `consumers` | [ConsumersOfClientSecret](#ConsumersOfClientSecret)[] | Интеграции Dynatrace, которые могут использовать это подключение Возможные значения: * `DA` * `SVC:com.dynatrace.da` * `NONE` | Required |

##### Объект `FederatedIdentityCredential`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ID каталога (tenant) `directoryId` | text | Directory (tenant) ID Microsoft Entra ID | Optional |
| ID приложения (client) `applicationId` | text | Application (client) ID вашего приложения, зарегистрированного в Microsoft Azure App registrations | Optional |
| Потребители `consumers` | [ConsumersOfFederatedIdentityCredential](#ConsumersOfFederatedIdentityCredential)[] | Потребители, которые могут использовать это подключение Возможные значения: * `DA` * `SVC:com.dynatrace.da` * `APP:dynatrace.microsoft.azure.connector` * `SVC:com.dynatrace.openpipeline` * `SVC:com.dynatrace.grail` * `SVC:com.dynatrace.bo` * `NONE` | Required |