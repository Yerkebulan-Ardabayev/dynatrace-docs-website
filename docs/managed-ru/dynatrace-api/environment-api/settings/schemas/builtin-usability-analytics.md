---
title: Settings API - Usability analytics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-usability-analytics
scraped: 2026-05-12T11:44:15.102734
---

# Settings API - Usability analytics schema table

# Settings API - Usability analytics schema table

* Published Dec 05, 2023

### Аналитика юзабилити (`builtin:usability-analytics)`

Анализируйте обнаруженные проблемы юзабилити в приложении.

К типам пользовательских действий, обычно отражающих фрустрацию пользователя, относятся мёртвые клики, rage-клики, rage-повороты и обновления страницы.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:usability-analytics` | * `group:web-and-mobile-monitoring` * `group:preferences` | `APPLICATION` - Web application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:usability-analytics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:usability-analytics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:usability-analytics` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Определять rage-клики `detectRageClicks` | boolean | Три или более быстрых клика в одной области веб-страницы считаются rage-кликами. Rage-клики обычно отражают медленно загружающиеся или сломанные ресурсы страницы. Счётчики rage-кликов формируются для каждой сессии и учитываются в [User Experience Score](https://dt-url.net/39034wt) . Если эта настройка включена, счётчик rage-кликов формируется для каждой отслеживаемой пользовательской сессии. | Required |