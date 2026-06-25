---
title: Settings API - End users' data privacy schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-preferences-privacy
scraped: 2026-05-12T11:47:36.529214
---

# Settings API - End users' data privacy schema table

# Settings API - End users' data privacy schema table

* Published Dec 05, 2023

### Приватность данных конечных пользователей (`builtin:preferences.privacy)`

Используйте параметры на этой странице, чтобы маскировать персональные данные конечных пользователей и обеспечивать соответствие вашей организации требованиям приватности, включая [GDPR](https://dt-url.net/8m3u0pxk).

Если не указано иное, все приведённые ниже параметры приватности применяются и к данным, захватываемым RUM JavaScript, и к данным, захватываемым OneAgent на стороне сервера. Эти параметры гарантируют, что персональные данные конечных пользователей не сохраняются в Dynatrace. Подробнее о защите приватности конечных пользователей см. [Data privacy and security](https://dt-url.net/zn03sq4) в Dynatrace Help.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:preferences.privacy` | * `group:preferences` * `group:rum-settings` * `group:privacy-settings` | `APPLICATION` - Web application  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:preferences.privacy` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:preferences.privacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:preferences.privacy` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `masking` | [Masking](#Masking) | - | Required |
| User tracking `userTracking` | [UserTracking](#UserTracking) | - | Required |
| Opt-in mode `dataCollection` | [DataCollection](#DataCollection) | Чтобы дать конечным пользователям возможность самим решать, нужно ли отслеживать их активность для измерения производительности и использования приложения, включите opt-in mode. | Required |
| Do Not Track `doNotTrack` | [DoNotTrack](#DoNotTrack) | У большинства современных web-браузеров есть функция приватности ["Do Not Track"](https://dt-url.net/sb3n0pnl), которую отдельные пользователи могут включить на своих устройствах. Настройте поведение Dynatrace при обнаружении этой настройки. | Required |

##### Объект `Masking`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Маскировать персональные данные в URI `personalDataUriMaskingEnabled` | boolean | Dynatrace захватывает URI и request-заголовки, отправляемые из desktop- и mobile-браузеров. Dynatrace также захватывает данные запросов на стороне сервера для детального анализа производительности приложений. Подробнее см. [Mask personal data in URIs](https://dt-url.net/mask-personal-data-in-URIs).  URI, query-строки, заголовки, сообщения об исключениях и данные, захватываемые для request attributes, могут содержать персональные данные. При включении этого параметра Dynatrace автоматически обнаруживает UUID, номера кредитных карт, email-адреса, IP-адреса и другие идентификаторы и заменяет их значения placeholder'ами. Затем персональные данные маскируются в PurePath analysis, error analysis, именовании user actions для RUM и в других местах Dynatrace. | Required |
| Маскировать user actions (только web-приложения) `userActionMaskingEnabled` | boolean | Когда Dynatrace обнаруживает user action, инициирующее загрузку страницы или AJAX/XHR-действие. Подробнее о маскировании user actions см. [Mask user actions](https://dt-url.net/mask-user-action).  Когда Dynatrace обнаруживает user action, инициирующее загрузку страницы или AJAX/XHR-действие, оно формирует имя user action на основе:  * Типа user-события (click on..., loading of page... или keypress on...) * Title, caption, label, value, ID, className или другого доступного свойства связанного HTML-элемента (например, image, button, checkbox или text input field).  В большинстве случаев подход по умолчанию к именованию user-action работает хорошо, и имена выглядят так:  * click on "Search" on page /search.html * keypress on "Feedback" on page /contact.html * touch on "Homescreen" of page /list.jsf  В редких случаях конфиденциальные данные (например, email-адреса, имена пользователей или номера счетов) могут непреднамеренно попасть в имена user actions, потому что сами эти данные содержатся в label, атрибуте или другом значении HTML-элемента (например, click on "my Account Number: 1231231"...). Если такие конфиденциальные данные появляются в именах user actions вашего приложения, включите параметр маскирования имён user actions. Этот параметр заменяет конкретные имена и значения HTML-элементов на generic-имена. С включённым маскированием имён user-actions перечисленные выше имена выглядят так:  * click on INPUT on page /search.html * keypress on TEXTAREA on page /contact.html * touch on DIV of page /list.jsf | Required |

##### Объект `UserTracking`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Использовать persistent cookies для user tracking `persistentCookieEnabled` | boolean | При включении Dynatrace размещает [persistent cookie](https://dt-url.net/313o0p4n) на всех устройствах конечных пользователей для идентификации возвращающихся пользователей. | Required |

##### Объект `DataCollection`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Data-collection и opt-in mode `optInModeEnabled` | boolean | При включённом [Data-collection и opt-in mode](https://dt-url.net/7l3p0p3h) данные Real User Monitoring не захватываются, пока для конкретных user-сессий не вызвано dtrum.enable(). | Required |

##### Объект `DoNotTrack`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Соблюдать настройки браузера "Do Not Track" `complyWithDoNotTrack` | boolean | - | Required |
| `doNotTrack` | enum | Возможные значения: * `anonymous` * `disable-rum` | Required |