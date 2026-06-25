---
title: Settings API - Custom RUM JavaScript version schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-custom-rum-javascript-version
scraped: 2026-05-12T11:43:29.550516
---

# Settings API - Custom RUM JavaScript version schema table

# Settings API - Custom RUM JavaScript version schema table

* Published Dec 05, 2023

### Пользовательская версия RUM JavaScript (`builtin:rum.web.custom-rum-javascript-version)`

Задайте пользовательскую версию RUM JavaScript для добавления в пул версий, из которых могут выбирать веб-приложения.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.custom-rum-javascript-version` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-rum-javascript-version` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.custom-rum-javascript-version` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-rum-javascript-version` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Выбрать пользовательскую версию `customJavaScriptVersion` | text | - | Optional |