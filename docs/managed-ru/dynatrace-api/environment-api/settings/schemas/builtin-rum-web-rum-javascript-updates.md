---
title: Settings API - RUM JavaScript updates schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-rum-javascript-updates
scraped: 2026-05-12T11:44:45.450668
---

# Settings API - RUM JavaScript updates schema table

# Settings API - RUM JavaScript updates schema table

* Published Dec 05, 2023

### Обновления JavaScript-кода RUM (`builtin:rum.web.rum-javascript-updates)`

Задайте версию RUM JavaScript, которая будет использоваться глобально (в общих настройках) или для конкретного веб-приложения (в настройках приложения). Чтобы получать преимущества от обновлений RUM JavaScript, рекомендуется выбирать динамическую версию, например **Latest stable** или **Previous stable**. Если динамические версии не подходят, выберите **Custom**. Этот вариант ссылается на статическую версию, заданную в настройках окружения Custom RUM JavaScript version (`<your-dynatrace-url>//ui/settings/builtin:rum.web.custom-rum-javascript-version`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.rum-javascript-updates` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` * `group:rum-injection` | `APPLICATION` - Web application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.rum-javascript-updates` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.rum-javascript-updates` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.rum-javascript-updates` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Выбор версии `JavascriptVersion` | enum | Возможные значения: * `LATEST_STABLE` * `PREVIOUS_STABLE` * `LATEST_IE7_10_SUPPORTED` * `LATEST_IE11_SUPPORTED` * `CUSTOM` | Required |