---
title: Settings API - ServiceNow Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-servicenow-connection
scraped: 2026-05-12T11:48:47.054050
---

# Settings API - ServiceNow Connections schema table

# Settings API - ServiceNow Connections schema table

* Published Feb 26, 2024

### Подключения ServiceNow (`app:dynatrace.servicenow:connection)`

Подключения позволяют интегрироваться с ServiceNow.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.servicenow:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.servicenow:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.servicenow:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.servicenow:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Уникальное и однозначно идентифицируемое имя подключения к вашему инстансу ServiceNow. | Required |
| URL инстанса ServiceNow `url` | text | URL инстанса ServiceNow. | Required |
| Тип `type` | enum | Тип используемого метода аутентификации. Возможные значения: * `basic` * `client-credentials` | Required |
| Пользователь `user` | text | Имя пользователя или адрес электронной почты. | Required |
| Пароль `password` | secret | Пароль пользователя ServiceNow. | Required |
| ID клиента `clientId` | text | ID клиента OAuth-сервера ServiceNow | Required |
| Секрет клиента `clientSecret` | secret | Секрет клиента OAuth-сервера ServiceNow | Required |