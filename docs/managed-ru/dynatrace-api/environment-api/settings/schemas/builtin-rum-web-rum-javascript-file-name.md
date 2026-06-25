---
title: Settings API - RUM monitoring code filename schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-rum-javascript-file-name
scraped: 2026-05-12T11:39:31.371084
---

# Settings API - RUM monitoring code filename schema table

# Settings API - RUM monitoring code filename schema table

* Published Jun 09, 2025

### Имя файла кода мониторинга RUM (`builtin:rum.web.rum-javascript-file-name)`

Задайте пользовательский префикс имени файла, который будет использоваться вместо префикса по умолчанию в имени файла кода мониторинга RUM (ruxitagentjs или ruxitagent). Подробнее см. [Configure the Real User Monitoring code source](https://dt-url.net/wc03z4k).

**Примечание:** учтите, что после смены префикса имени файла кода мониторинга RUM возможно временное снижение объёма собираемых данных RUM. Поэтому эту настройку не следует менять часто.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.rum-javascript-file-name` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.rum-javascript-file-name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.rum-javascript-file-name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.rum-javascript-file-name` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Пользовательский префикс имени файла `filename` | text | - | Required |