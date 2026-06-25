---
title: Settings API - Anonymize End-User IP Addresses schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-preferences-ipaddressmasking
scraped: 2026-05-12T11:45:19.207167
---

# Settings API - Anonymize End-User IP Addresses schema table

# Settings API - Anonymize End-User IP Addresses schema table

* Published Dec 05, 2023

### Анонимизация IP-адресов конечных пользователей (`builtin:preferences.ipaddressmasking)`

Управляйте тем, какие данные захватывает Dynatrace. Dynatrace может захватывать IP-адреса и GPS-координаты конечных пользователей, чтобы определить место, откуда они обращаются к приложению. IP Address Masking усекает IP-адреса, захваченные из браузеров конечных пользователей и данных OneAgent, для эффективной деперсонализации.

Подробнее см. [Mask IPs and GPS coordinates](https://dt-url.net/mask-end-users-ip-addresses). О настройках приватности Dynatrace см. документацию [Data privacy and security](https://dt-url.net/zn03sq4).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:preferences.ipaddressmasking` | * `group:rum-general` * `group:preferences` * `group:rum-settings` * `group:privacy-settings` | `MOBILE_APPLICATION` - Mobile App  `CUSTOM_APPLICATION` - Custom Application  `APPLICATION` - Web application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:preferences.ipaddressmasking` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:preferences.ipaddressmasking` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:preferences.ipaddressmasking` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Маскировать IP-адреса и GPS-координаты конечных пользователей `enabled` | boolean | - | Required |
| `type` | enum | Возможные значения: * `all` * `public` | Required |