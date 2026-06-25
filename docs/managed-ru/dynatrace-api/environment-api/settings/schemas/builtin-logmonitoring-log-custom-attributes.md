---
title: Settings API - Log custom attributes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-custom-attributes
scraped: 2026-05-12T11:41:28.629265
---

# Settings API - Log custom attributes schema table

# Settings API - Log custom attributes schema table

* Published Dec 05, 2023

### Пользовательские атрибуты логов (`builtin:logmonitoring.log-custom-attributes)`

Мониторинг логов Dynatrace позволяет задавать пользовательские атрибуты для загружаемых логов.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:logmonitoring.log-custom-attributes` | * `group:log-monitoring.analysis` * `group:log-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-custom-attributes` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:logmonitoring.log-custom-attributes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:logmonitoring.log-custom-attributes` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Ключ `key` | text | Ключ атрибута чувствителен к регистру при приёме данных логов. | Required |
| Показывать значения атрибутов в боковой панели `aggregableAttribute` | boolean | В случае Log Monitoring Classic изменение применяется к новым принятым событиям логов. Этот атрибут не будет искать события логов, принятые до включения этой опции. В случае Logs on Grail состояние переключателя игнорируется. | Required |