---
title: Settings API - Launcher schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-launcher-home-launchpad
scraped: 2026-05-12T11:49:22.082489
---

# Settings API - Launcher schema table

# Settings API - Launcher schema table

* Published May 05, 2025

### Launcher (`app:dynatrace.launcher:home.launchpad)`

Настройте домашние launchpad-ы ваших команд, чтобы упорядочить рабочий процесс и повысить продуктивность. Настройте до 100 пользовательских домашних launchpad-ов в этом окружении под ваши конкретные нужды.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.launcher:home.launchpad` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.launcher:home.launchpad` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.launcher:home.launchpad` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.launcher:home.launchpad` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Домашний launchpad `groupLaunchpads` | [GroupLaunchpadItem](#GroupLaunchpadItem)[] | Задайте домашние launchpad-ы для групп пользователей. Пользователю группы будет показан launchpad с наивысшим рангом. | Required |

##### Объект `GroupLaunchpadItem`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Launchpad `launchpadId` | text | - | Required |
| Группа пользователей `userGroupId` | text | - | Required |
| Состояние `isEnabled` | boolean | - | Required |