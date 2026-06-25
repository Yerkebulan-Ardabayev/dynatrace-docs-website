---
title: Settings API - Allowed URL pattern rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dashboards-image-allowlist
scraped: 2026-05-12T11:46:40.140552
---

# Settings API - Allowed URL pattern rules schema table

# Settings API - Allowed URL pattern rules schema table

* Published Dec 05, 2023

### Правила разрешённых URL-шаблонов (`builtin:dashboards.image.allowlist)`

Настройте разрешённые URL-шаблоны для загрузки внешних ресурсов, таких как изображения. Чтобы изображение было загружено, настроенный URL должен соответствовать одному из указанных шаблонов.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dashboards.image.allowlist` | * `group:dashboards` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.image.allowlist` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dashboards.image.allowlist` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.image.allowlist` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Список URL-сопоставителей `allowlist` | Set<[URLPattern](#URLPattern)> | - | Required |

##### Объект `URLPattern`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Правило `rule` | enum | Возможные значения: * `startsWith` * `equals` | Required |
| Шаблон `template` | text | - | Required |