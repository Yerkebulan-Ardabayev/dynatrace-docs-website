---
title: Settings API - Hub subscriptions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-hub-channel-subscriptions
scraped: 2026-05-12T11:42:28.130379
---

# Settings API - Hub subscriptions schema table

# Settings API - Hub subscriptions schema table

* Published Feb 26, 2024

### Подписки Hub (`builtin:hub-channel.subscriptions)`

Здесь можно управлять подписками для расширения списка доступных приложений или релизов в [Dynatrace Hub](https://www.dynatrace.com/support/help/manage/hub). Добавьте новый токен, чтобы зарегистрировать подписку.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:hub-channel.subscriptions` | * `group:preferences` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hub-channel.subscriptions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:hub-channel.subscriptions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hub-channel.subscriptions` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Подписки `tokenSubscriptions` | [TokenSubscription](#TokenSubscription)[] | - | Required |

##### Объект `TokenSubscription`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя подписки `name` | text | - | Required |
| Токен подписки `token` | text | - | Required |
| Описание `description` | text | - | Optional |