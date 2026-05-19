---
title: Settings API - VirusTotal Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-virustotal-connections
scraped: 2026-05-12T11:46:47.830850
---

# Settings API - VirusTotal Connections schema table

# Settings API - VirusTotal Connections schema table

* Published Aug 04, 2025

### Подключения VirusTotal (`app:dynatrace.virustotal:connections)`

Подключения VirusTotal

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.virustotal:connections` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.virustotal:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.virustotal:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.virustotal:connections` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активировать подключение `enabled` | boolean | Включить или отключить подключение | Required |
| Имя подключения `name` | text | Введите уникальное отображаемое имя. | Required |
| Ключ API `api_key` | secret | Войдите в VirusTotal и создайте ключ API. Вставьте ключ в это поле. | Required |