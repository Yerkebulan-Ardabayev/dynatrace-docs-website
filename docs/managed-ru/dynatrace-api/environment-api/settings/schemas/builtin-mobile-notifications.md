---
title: Settings API - Dynatrace mobile app schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-mobile-notifications
scraped: 2026-05-12T11:39:35.004404
---

# Settings API - Dynatrace mobile app schema table

# Settings API - Dynatrace mobile app schema table

* Published Feb 26, 2024

### Мобильное приложение Dynatrace (`builtin:mobile.notifications)`

Мобильное приложение Dynatrace для iOS и Android позволяет пользователям получать настраиваемые push-уведомления на свои мобильные устройства. Смотрите инструкции ниже для настройки доступа мобильного приложения Dynatrace в этом окружении.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:mobile.notifications` | * `group:integration` | `environment`  `environment-default` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mobile.notifications` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:mobile.notifications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mobile.notifications` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | Включает мобильные push-уведомления для проблем DavisÂ®. В окружениях Dynatrace Managed дополнительно включает генерацию мобильного QR-кода. | Required |