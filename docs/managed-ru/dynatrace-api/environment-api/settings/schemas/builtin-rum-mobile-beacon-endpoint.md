---
title: Settings API - Beacon endpoint settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-beacon-endpoint
scraped: 2026-05-12T11:44:00.187174
---

# Settings API - Beacon endpoint settings schema table

# Settings API - Beacon endpoint settings schema table

* Published Dec 05, 2023

### Настройки эндпоинта beacon (`builtin:rum.mobile.beacon-endpoint)`

Задайте, куда OneAgent должен отправлять данные мониторинга iOS и Android.  
**Примечание:** чтобы использовать Environment ActiveGate как эндпоинт beacon, сначала включите пересылку beacon в конфигурации ActiveGate. Подробнее о настройке [Environment ActiveGate](https://dt-url.net/90r039v) или об использовании [OneAgent as a beacon endpoint](https://dt-url.net/hr4e0ijr).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.beacon-endpoint` | * `group:rum-general` | `MOBILE_APPLICATION` - Mobile App  `CUSTOM_APPLICATION` - Custom Application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.beacon-endpoint` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.beacon-endpoint` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.beacon-endpoint` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип `type` | enum | Возможные значения: * `CLUSTER_ACTIVEGATE` * `ENVIRONMENT_ACTIVEGATE` * `INSTRUMENTED_WEBSERVER` | Required |
| URL `url` | text | Должен быть валидным URL эндпоинта beacon.  URL должен начинаться с 'http://' или 'https://'. URL Environment ActiveGate должен заканчиваться на '/mbeacon/{{environment-id}}', URL Instrumented Web Server заканчивается на '/dtmb'. | Required |