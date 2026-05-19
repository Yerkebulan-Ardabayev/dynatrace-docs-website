---
title: Settings API - AbuseIPDB Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-abuseipdb-connections
scraped: 2026-05-12T11:49:43.777147
---

# Settings API - AbuseIPDB Connections schema table

# Settings API - AbuseIPDB Connections schema table

* Published Aug 04, 2025

### Подключения AbuseIPDB (`app:dynatrace.abuseipdb:connections)`

Подключения AbuseIPDB

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.abuseipdb:connections` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.abuseipdb:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.abuseipdb:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.abuseipdb:connections` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активировать подключение `enabled` | boolean | Включить или отключить подключение | Required |
| Имя подключения `name` | text | Введите уникальное отображаемое имя. | Required |
| Ключ API `api_key` | secret | Войдите в AbuseIPDB и создайте ключ API. Вставьте ключ в это поле. | Required |