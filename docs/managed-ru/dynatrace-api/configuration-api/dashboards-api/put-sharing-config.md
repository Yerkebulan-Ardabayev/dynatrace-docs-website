---
title: Dashboards API - PUT sharing configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/put-sharing-config
---

# Dashboards API - PUT sharing configuration

# Dashboards API - PUT sharing configuration

* Справочник
* Опубликовано 29 марта 2021 г.

Обновляет конфигурацию совместного доступа для указанного дашборда.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного дашборда. | путь | Обязательный |
| body | [DashboardSharing](#openapi-definition-DashboardSharing) | Тело JSON запроса. Содержит обновлённые параметры совместного доступа к дашборду. | тело | Опциональный |

### Объекты тела запроса

#### Объект `DashboardSharing`

Конфигурация совместного доступа к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Дашборд общедоступный (`true`) или приватный (`false`). | Опциональный |
| id | string | ID сущности Dynatrace для дашборда. | Обязательный |
| permissions | [DashboardSharePermissions](#openapi-definition-DashboardSharePermissions)[] | Список разрешений на доступ к дашборду. | Обязательный |
| preset | boolean | Если `true`, дашборд будет отмечен как preset. | Опциональный |
| publicAccess | [DashboardAnonymousAccess](#openapi-definition-DashboardAnonymousAccess) | Конфигурация [анонимного доступа﻿](https://dt-url.net/ov03sf1?dt=m) к дашборду. | Обязательный |

#### Объект `DashboardSharePermissions`

Разрешения на доступ к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | ID пользователя или группы, которым предоставляется разрешение.  Не применяется, если **type** установлен в `ALL`. | Опциональный |
| permission | string | Уровень разрешения:  * `VIEW`: дашборд предоставлен в общий доступ с разрешением на чтение. * `EDIT`: дашборд предоставлен в общий доступ с разрешением на редактирование. Элемент может принимать следующие значения * `EDIT` * `VIEW` | Обязательный |
| type | string | Тип разрешения:  * `USER`: дашборд предоставлен в общий доступ указанному пользователю. * `GROUP`: дашборд предоставлен в общий доступ всем пользователям указанной группы. * `ALL`: дашборд предоставлен в общий доступ по ссылке. Любой аутентифицированный пользователь с этой ссылкой может просматривать дашборд. Элемент может принимать следующие значения * `ALL` * `GROUP` * `USER` | Обязательный |

#### Объект `DashboardAnonymousAccess`

Конфигурация [анонимного доступа﻿](https://dt-url.net/ov03sf1?dt=m) к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZoneIds | string[] | Список management zones, которые могут отображать данные на публично доступном дашборде.  Здесь нужно указать ID management zone. Для каждой указанной management zone Dynatrace генерирует ссылку доступа. Их можно найти в списке **urls**.  Чтобы открыть общий доступ к дашборду с его management zone по умолчанию, использовать значение `default`. | Обязательный |
| urls | object | Список URL для анонимного доступа к дашборду.  Каждая ссылка предоставляет доступ к данным конкретной management zone, указанной в списке **managementZoneIds**.  Эти ссылки автоматически генерируются Dynatrace, изменить их нельзя. | Опциональный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные некорректны. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела JSON ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Проверить полезную нагрузку

Рекомендуется проверить полезную нагрузку перед отправкой в реальном запросе. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация совместного доступа к дашборду корректна. Ответ не содержит тела |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные некорректны |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела JSON ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Похожие темы

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")