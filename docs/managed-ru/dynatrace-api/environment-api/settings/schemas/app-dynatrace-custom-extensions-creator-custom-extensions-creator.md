---
title: Settings API - Extensions Creator schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-custom-extensions-creator-custom-extensions-creator
scraped: 2026-05-12T11:42:53.781170
---

# Settings API - Extensions Creator schema table

# Settings API - Extensions Creator schema table

* Published Aug 26, 2024

### Extensions Creator (`app:dynatrace.custom.extensions.creator:custom-extensions-creator)`

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.custom.extensions.creator:custom-extensions-creator` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.custom.extensions.creator:custom-extensions-creator` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.custom.extensions.creator:custom-extensions-creator` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.custom.extensions.creator:custom-extensions-creator` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | Понятное имя для этого окружения | Required |
| URL окружения `environmentUrl` | text | URL окружения, из которого извлекаются эндпоинты Custom DB Query V1  Используется только функцией миграции Custom DB Query этого приложения.  Не забудьте разрешить исходящие подключения к этому URL в Dynatrace, в разделе **Settings > Preferences > Limit outbound connections** | Required |
| Токен API `apiToken` | secret | Токен со scope **ReadConfig**  Это позволяет приложению выполнять GET-вызовы к Configuration V1 API | Required |