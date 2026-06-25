---
title: Settings API - General settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-dashboards-general
scraped: 2026-05-12T11:42:41.955173
---

# Settings API - General settings schema table

# Settings API - General settings schema table

* Published Dec 05, 2023

### Общие настройки (`builtin:dashboards.general)`

Настройте параметры анонимного доступа и домашнего дашборда.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:dashboards.general` | * `group:dashboards` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.general` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:dashboards.general` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:dashboards.general` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Разрешить анонимный доступ `enablePublicSharing` | boolean | Разрешить пользователям предоставлять анонимный доступ к дашбордам. Для просмотра таких дашбордов в режиме только чтения вход не потребуется. | Required |
| Домашние дашборды `defaultDashboardList` | [UserGroups](#UserGroups)[] | Настройте домашний дашборд для выбранной группы пользователей. Выбранная предустановка дашборда будет загружаться как стартовая страница окружения по умолчанию. | Required |

##### Объект `UserGroups`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Группа пользователей `UserGroup` | text | Показывать выбранный дашборд по умолчанию для этой группы пользователей | Required |
| Домашний дашборд `Dashboard` | text | Предустановка дашборда для отображения в качестве стартовой страницы по умолчанию | Required |