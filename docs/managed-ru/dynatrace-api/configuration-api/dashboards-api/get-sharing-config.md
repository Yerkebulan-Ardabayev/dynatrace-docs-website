---
title: Dashboards API - GET sharing configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/get-sharing-config
scraped: 2026-05-12T11:14:44.121591
---

# Dashboards API - GET sharing configuration

# Dashboards API - GET sharing configuration

* Reference
* Published Mar 29, 2021

Возвращает конфигурацию совместного доступа указанного дашборда.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного дашборда. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DashboardSharing](#openapi-definition-DashboardSharing) | Успех |

### Объекты тела ответа

#### Объект `DashboardSharing`

Конфигурация совместного доступа дашборда.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Дашборд общий (`true`) или приватный (`false`). |
| id | string | ID сущности Dynatrace для дашборда. |
| permissions | [DashboardSharePermissions[]](#openapi-definition-DashboardSharePermissions) | Список разрешений на доступ к дашборду. |
| preset | boolean | Если `true`, дашборд будет помечен как предустановленный. |
| publicAccess | [DashboardAnonymousAccess](#openapi-definition-DashboardAnonymousAccess) | Конфигурация [anonymous access](https://dt-url.net/ov03sf1) к дашборду. |

#### Объект `DashboardSharePermissions`

Разрешения на доступ к дашборду.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID пользователя или группы, которым предоставлено разрешение.  Не применимо, если **type** имеет значение `ALL`. |
| permission | string | Уровень разрешения:  * `VIEW`: дашборд предоставлен с разрешением на чтение. * `EDIT`: дашборд предоставлен с разрешением на редактирование. Возможные значения: * `EDIT` * `VIEW` |
| type | string | Тип разрешения:  * `USER`: дашборд предоставлен указанному пользователю. * `GROUP`: дашборд предоставлен всем пользователям указанной группы. * `ALL`: дашборд предоставлен по ссылке. Любой аутентифицированный пользователь со ссылкой может просматривать дашборд. Возможные значения: * `ALL` * `GROUP` * `USER` |

#### Объект `DashboardAnonymousAccess`

Конфигурация [anonymous access](https://dt-url.net/ov03sf1) к дашборду.

| Элемент | Тип | Описание |
| --- | --- | --- |
| managementZoneIds | string[] | Список зон управления, данные которых могут отображаться на публично доступном дашборде.  Укажите здесь ID зон управления. Для каждой указанной зоны управления Dynatrace генерирует ссылку доступа. Их можно получить в списке **urls**.  Чтобы предоставить дашборд с его зоной управления по умолчанию, используйте значение `default`. |
| urls | object | Список URL для анонимного доступа к дашборду.  Каждая ссылка даёт доступ к данным конкретной зоны управления, указанной в списке **managementZoneIds**.  Эти ссылки автоматически генерируются Dynatrace, изменить их нельзя. |

### JSON-модели тела ответа

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

## Связанные темы

* [Дашборды](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать дашборды Dynatrace Dashboards Classic, управлять ими и использовать их.")