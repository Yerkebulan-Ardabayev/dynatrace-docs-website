---
title: Dashboards API - GET sharing configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/get-sharing-config
---

# Dashboards API - GET sharing configuration

# Dashboards API - GET sharing configuration

* Справка
* Опубликовано 29 марта 2021 г.

Получает конфигурацию совместного доступа к указанному dashboard.

Запрос формирует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Подробнее о том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного dashboard. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DashboardSharing](#openapi-definition-DashboardSharing) | Успешно |

### Объекты тела ответа

#### Объект `DashboardSharing`

Конфигурация совместного доступа к dashboard.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Dashboard является общим (`true`) или приватным (`false`). |
| id | string | Dynatrace ID сущности dashboard. |
| permissions | [DashboardSharePermissions](#openapi-definition-DashboardSharePermissions)[] | Список разрешений на доступ к dashboard. |
| preset | boolean | Если `true`, dashboard будет помечен как preset. |
| publicAccess | [DashboardAnonymousAccess](#openapi-definition-DashboardAnonymousAccess) | Конфигурация [анонимного доступа﻿](https://dt-url.net/ov03sf1?dt=m) к dashboard. |

#### Объект `DashboardSharePermissions`

Разрешения доступа к dashboard.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID пользователя или группы, которым предоставлено разрешение.  Не применимо, если параметр **type** установлен в значение `ALL`. |
| permission | string | Уровень разрешения:  * `VIEW`: dashboard передан в совместный доступ с разрешением на чтение. * `EDIT`: dashboard передан в совместный доступ с разрешением на редактирование. Элемент может содержать следующие значения * `EDIT` * `VIEW` |
| type | string | Тип разрешения:  * `USER`: dashboard передан в совместный доступ указанному пользователю. * `GROUP`: dashboard передан в совместный доступ всем пользователям указанной группы. * `ALL`: dashboard передан в совместный доступ по ссылке. Любой аутентифицированный пользователь, у которого есть ссылка, может просматривать dashboard. Элемент может содержать следующие значения * `ALL` * `GROUP` * `USER` |

#### Объект `DashboardAnonymousAccess`

Конфигурация [анонимного доступа﻿](https://dt-url.net/ov03sf1?dt=m) к dashboard.

| Элемент | Тип | Описание |
| --- | --- | --- |
| managementZoneIds | string[] | Список management zone, которые могут отображать данные на публично доступном dashboard.  Здесь нужно указать ID management zone. Для каждой указанной management zone Dynatrace генерирует ссылку доступа. Их можно найти в списке **urls**.  Чтобы предоставить общий доступ к dashboard с его management zone по умолчанию, используй значение `default`. |
| urls | object | Список URL для анонимного доступа к dashboard.  Каждая ссылка предоставляет доступ к данным конкретной management zone, указанной в списке **managementZoneIds**.  Эти ссылки автоматически генерируются Dynatrace, изменить их нельзя. |

### JSON модели тела ответа

```
{



"enabled": "true",



"id": "a5fca32f-d3ba-4749-b201-5d3cd70b9d22",



"permissions": [



{



"permission": "VIEW",



"type": "ALL"



},



{



"id": "userid",



"permission": "VIEW",



"type": "USER"



},



{



"id": "userid",



"permission": "EDIT",



"type": "USER"



},



{



"id": "groupid",



"permission": "VIEW",



"type": "GROUP"



},



{



"id": "groupid",



"permission": "EDIT",



"type": "GROUP"



}



],



"preset": "true",



"publicAccess": {



"managementZoneIds": [



"default",



"2899273953172250973"



],



"urls": {



"2899273953172250973": "https://mytenantid.live.dynatrace.com/e/1/dashboards/a5fca32f-d3ba-4749-b201-5d3cd70b9d22?auth=SL5wTvCbaM2lwpew23234",



"default": "https://mytenantid.live.dynatrace.com/e/1/dashboards/a5fca32f-d3ba-4749-b201-5d3cd70b9d22?auth=9yPpSI-M-3434Irz8yc8U"



}



}



}
```

## Похожие темы

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")