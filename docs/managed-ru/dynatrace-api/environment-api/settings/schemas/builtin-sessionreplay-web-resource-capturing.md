---
title: Settings API - Resource capture for Session Replay schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-sessionreplay-web-resource-capturing
scraped: 2026-05-12T11:46:52.161254
---

# Settings API - Resource capture for Session Replay schema table

# Settings API - Resource capture for Session Replay schema table

* Published Dec 05, 2023

### Захват ресурсов для Session Replay (`builtin:sessionreplay.web.resource-capturing)`

Захват ресурсов позволяет захватывать и сохранять стили во время записи пользовательских сессий. Подробнее см. [Resource capturing](https://dt-url.net/sr-resource-capturing).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:sessionreplay.web.resource-capturing` | * `group:capturing` * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.capturing` | `APPLICATION` - Web application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:sessionreplay.web.resource-capturing` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:sessionreplay.web.resource-capturing` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:sessionreplay.web.resource-capturing` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить захват ресурсов `enableResourceCapturing` | boolean | Если включено, Dynatrace захватывает ресурсы для не более 0,1% сессий пользователей, записанных через Session Replay. Подробнее см. [Resource capture](https://dt-url.net/sr-resource-capturing). | Required |
| Исключение URL `resourceCaptureUrlExclusionPatternList` | set | Добавьте правила исключений, чтобы избежать захвата ресурсов с определённых страниц. | Required |