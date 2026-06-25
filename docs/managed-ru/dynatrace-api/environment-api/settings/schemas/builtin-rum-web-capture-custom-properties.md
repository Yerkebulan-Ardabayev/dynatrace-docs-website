---
title: Settings API - Custom Properties Capture Restrictions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-capture-custom-properties
scraped: 2026-05-12T11:43:38.062964
---

# Settings API - Custom Properties Capture Restrictions schema table

# Settings API - Custom Properties Capture Restrictions schema table

* Published May 05, 2025

### Ограничения захвата пользовательских свойств (`builtin:rum.web.capture-custom-properties)`

Задайте конкретные свойства для ограничения захвата событий и сессий: можно разрешать по имени свойства или разрешить все свойства.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.capture-custom-properties` | - | `APPLICATION` - Web application  `MOBILE_APPLICATION` - Mobile App |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.capture-custom-properties` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.capture-custom-properties` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.capture-custom-properties` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Список разрешённых пользовательских свойств события `customEventPropertiesAllowList` | [CustomProperty](#CustomProperty)[] | - | Required |
| Список разрешённых пользовательских свойств сессии `customSessionPropertiesAllowList` | [CustomProperty](#CustomProperty)[] | - | Required |

##### Объект `CustomProperty`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя поля `fieldName` | text | - | Required |
| Валидация имени поля должна быть нечувствительной к регистру `caseInsensitiveNamingEnabled` | boolean | - | Required |
| Тип данных `fieldDataType` | enum | Возможные значения: * `STRING` * `NUMBER` * `BOOLEAN` | Required |