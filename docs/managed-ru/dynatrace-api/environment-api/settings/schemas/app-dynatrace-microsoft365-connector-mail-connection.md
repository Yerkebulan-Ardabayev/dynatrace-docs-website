---
title: Settings API - Microsoft 365 Email Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-microsoft365-connector-mail-connection
scraped: 2026-05-12T11:44:01.988138
---

# Settings API - Microsoft 365 Email Connections schema table

# Settings API - Microsoft 365 Email Connections schema table

* Published Oct 14, 2024

### Подключения электронной почты Microsoft 365 (`app:dynatrace.microsoft365.connector:mail.connection)`

Подключения Microsoft 365 для отправки электронной почты

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.microsoft365.connector:mail.connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.microsoft365.connector:mail.connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.microsoft365.connector:mail.connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.microsoft365.connector:mail.connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Уникальное имя для подключения электронной почты Microsoft 365  Это имя должно быть уникальным, оно будет отображаться и доступно для выбора в поле подключения действия workflow Microsoft 365 send-email | Required |
| ID каталога (тенанта) `tenant_id` | text | ID каталога (тенанта) вашего Azure Active Directory  ID каталога (тенанта) можно найти в Microsoft Azure Portal через сервис Azure Active Directory. | Required |
| ID приложения (клиента) `client_id` | text | ID приложения (клиента) вашего приложения, зарегистрированного в Microsoft Azure App registrations  ID приложения (клиента) можно найти в Microsoft Azure Portal через сервис App registrations. | Required |
| "From" адрес электронной почты `from_address` | text | Адрес электронной почты, с которого будут отправляться сообщения  Укажите корректный адрес электронной почты, с которого будут отправляться сообщения. Пример: service.user@company.com | Required |
| Тип `type` | enum | Тип используемого метода аутентификации Возможные значения: * `client_secret` | Required |
| Секрет клиента `client_secret` | secret | Секрет клиента вашего приложения, зарегистрированного в Microsoft Azure App registrations  Секрет клиента можно найти в Microsoft Azure Portal через сервис App registrations. | Required |