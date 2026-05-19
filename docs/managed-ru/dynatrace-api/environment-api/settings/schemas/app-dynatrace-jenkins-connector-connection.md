---
title: Settings API - Jenkins Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-jenkins-connector-connection
scraped: 2026-05-12T11:44:20.311726
---

# Settings API - Jenkins Connections schema table

# Settings API - Jenkins Connections schema table

* Published Mar 17, 2025

### Подключения Jenkins (`app:dynatrace.jenkins.connector:connection)`

Подключения содержат информацию доступа для приложения Jenkins. Это подключение можно использовать для подключения к инстансу Jenkins.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.jenkins.connector:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.jenkins.connector:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.jenkins.connector:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.jenkins.connector:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя подключения `name` | text | Имя подключения Jenkins | Required |
| URL Jenkins `url` | text | Базовый URL вашего инстанса Jenkins (например, https://[YOUR\_JENKINS\_DOMAIN]/) | Required |
| Имя пользователя `username` | text | Имя вашего пользователя Jenkins (например, jenkins) | Required |
| Пароль `password` | secret | Пароль пользователя или токен API, полученный из интерфейса Jenkins (Dashboard > User > Configure > API Token) | Required |