---
title: Settings API - Advanced correlation schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-resource-timing-origins
scraped: 2026-05-12T11:44:11.937165
---

# Settings API - Advanced correlation schema table

# Settings API - Advanced correlation schema table

* Published Dec 05, 2023

### Расширенная корреляция (`builtin:rum.resource-timing-origins)`

OneAgent использует заголовок ответа `Server-Timing` для передачи данных корреляции RUM в RUM JavaScript. Для cross-origin запросов RUM JavaScript может получить доступ к значению заголовка `Server-Timing`, только если заголовок `Timing-Allow-Origin` разрешает источник запроса. Поэтому OneAgent автоматически добавляет заголовок `Timing-Allow-Origin` в ответ веб-приложения, если приложение его ещё не установило. Заголовок `Timing-Allow-Origin` управляет доступом не только к значению заголовка `Server-Timing`, но и к подробным данным resource timing.

По умолчанию доступ предоставляется всем источникам. Добавьте правила, чтобы ограничить доступ указанными источниками.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.resource-timing-origins` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.resource-timing-origins` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.resource-timing-origins` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.resource-timing-origins` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Сопоставитель `matcher` | enum | Возможные значения: * `EQUALS` * `STARTS_WITH` * `ENDS_WITH` * `CONTAINS` | Required |
| Шаблон `pattern` | text | - | Required |