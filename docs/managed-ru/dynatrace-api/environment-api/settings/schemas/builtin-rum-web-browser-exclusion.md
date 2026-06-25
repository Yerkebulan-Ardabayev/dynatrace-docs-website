---
title: Settings API - Exclude/Include browsers from monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-browser-exclusion
scraped: 2026-05-12T11:42:26.347131
---

# Settings API - Exclude/Include browsers from monitoring schema table

# Settings API - Exclude/Include browsers from monitoring schema table

* Published Dec 05, 2023

### Исключение/включение браузеров из мониторинга (`builtin:rum.web.browser-exclusion)`

Чтобы исключить определённые устаревшие типы браузеров из списка мониторимых, создайте правила [browser exclusion](https://dt-url.net/0e2z0pp0) для тех браузеров, которые нужно исключить.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.browser-exclusion` | * `group:capturing` * `group:capturing.exclusions` | `APPLICATION` - Web application |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.browser-exclusion` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.browser-exclusion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.browser-exclusion` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Список исключений браузеров `browserExclusionList` | [BrowserExclusionListObject](#BrowserExclusionListObject)[] | - | Required |
| Только эти браузеры должны мониториться `browserExclusionInclude` | boolean | - | Required |

##### Объект `BrowserExclusionListObject`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Браузер `browserName` | enum | Возможные значения: * `ANDROID_WEBKIT` * `CHROME` * `CHROME_HEADLESS` * `FIREFOX` * `INTERNET_EXPLORER` * `OPERA` * `SAFARI` * `EDGE` * `BOTS_AND_SPIDERS` | Required |
| Компаратор версии браузера `versionComparator` | enum | Возможные значения: * `GREATER_OR_EQUAL` * `EQUALS` * `LESS_OR_EQUAL` | Required |
| Версия `version` | integer | - | Required |
| Платформа `platform` | enum | Возможные значения: * `ALL` * `MOBILE` * `DESKTOP` | Required |