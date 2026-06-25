---
title: Settings API - Privacy settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-privacy
scraped: 2026-05-12T11:48:59.353844
---

# Settings API - Privacy settings schema table

# Settings API - Privacy settings schema table

* Published Dec 05, 2023

### Настройки приватности (`builtin:rum.mobile.privacy)`

Включите режим opt-in, чтобы ваши пользователи могли решать, какие типы данных они готовы предоставить. Подробнее см. [Opt-in mode](https://dt-url.net/9602z8z)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.privacy` | * `group:rum-general` * `group:privacy-settings` | `MOBILE_APPLICATION` - Mobile App |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.privacy` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.privacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.privacy` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить режим opt-in пользователя `optInModeEnabled` | boolean | - | Required |