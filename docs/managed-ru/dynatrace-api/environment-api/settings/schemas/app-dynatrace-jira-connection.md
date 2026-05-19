---
title: Settings API - Jira Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-jira-connection
scraped: 2026-05-12T11:49:01.133821
---

# Settings API - Jira Connections schema table

# Settings API - Jira Connections schema table

* Published Dec 05, 2023

### Подключения Jira (`app:dynatrace.jira:connection)`

Учётные данные для приложения Jira

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.jira:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.jira:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.jira:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.jira:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Имя подключения Jira | Required |
| URL Jira `url` | text | URL сервера Jira | Required |
| Тип `type` | enum | Тип используемого метода аутентификации Возможные значения: * `basic` * `pat` * `cloud-token` | Required |
| Пользователь `user` | text | Имя пользователя или адрес электронной почты | Required |
| Пароль `password` | secret | Пароль пользователя Jira | Required |
| Токен `token` | secret | Токен для выбранного типа аутентификации | Required |