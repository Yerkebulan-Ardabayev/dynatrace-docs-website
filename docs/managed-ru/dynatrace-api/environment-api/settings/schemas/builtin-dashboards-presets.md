---
title: Settings API - Preset settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dashboards-presets
scraped: 2026-05-12T11:43:36.889533
---

# Settings API - Preset settings schema table

# Settings API - Preset settings schema table

* Published Dec 05, 2023

### Настройки предустановок (`builtin:dashboards.presets)`

Настройте параметры предустановок дашбордов.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dashboards.presets` | * `group:dashboards` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.presets` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dashboards.presets` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.presets` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включить предустановки `enableDashboardPresets` | boolean | Предустановки дашбордов по умолчанию видны всем пользователям. Для чистого окружения их можно полностью отключить или вручную ограничить видимость определёнными группами пользователей. | Required |
| Ограничить видимость предустановок `dashboardPresetsList` | [DashboardPresets](#DashboardPresets)[] | Показывать выбранную предустановку только соответствующей группе пользователей. | Required |

##### Объект `DashboardPresets`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Предустановка дашборда `DashboardPreset` | text | Предустановка дашборда, для которой ограничивается видимость | Required |
| Группа пользователей `UserGroup` | text | Группа пользователей, которой показывается выбранная предустановка дашборда | Required |