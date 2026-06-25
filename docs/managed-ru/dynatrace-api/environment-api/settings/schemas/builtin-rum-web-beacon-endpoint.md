---
title: Settings API - Beacon endpoint settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-beacon-endpoint
scraped: 2026-05-12T11:40:14.837782
---

# Settings API - Beacon endpoint settings schema table

# Settings API - Beacon endpoint settings schema table

* Published Apr 03, 2024

### Настройки эндпоинта beacon (`builtin:rum.web.beacon-endpoint)`

Задайте, куда OneAgent должен отправлять данные мониторинга веб-приложения.
Подробнее о том, как [configure the beacon endpoint](https://dt-url.net/yp036lb).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.beacon-endpoint` | * `group:rum-settings` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.beacon-endpoint` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.beacon-endpoint` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.beacon-endpoint` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип `type` | enum | Возможные значения: * `DEFAULT_CONFIG` * `ACTIVEGATE` * `ONEAGENT` | Required |
| URL `url` | text | Можно указать либо сегменты пути, либо абсолютный URL. | Required |
| Отправлять данные beacon через CORS `useCors` | boolean | Подробнее о [sending beacon data via CORS](https://dt-url.net/r7038sa) | Required |