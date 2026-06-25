---
title: Dashboards API - PUT sharing configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/put-sharing-config
scraped: 2026-05-12T11:14:56.004397
---

# Dashboards API - PUT sharing configuration

# Dashboards API - PUT sharing configuration

* Reference
* Published Mar 29, 2021

Обновляет конфигурацию совместного доступа указанного дашборда.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного дашборда. | path | Required |
| body | [DashboardSharing](#openapi-definition-DashboardSharing) | JSON-тело запроса. Содержит обновлённые параметры совместного доступа дашборда. | body | Optional |

### Объекты тела запроса

#### Объект `DashboardSharing`

Конфигурация совместного доступа дашборда.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Дашборд общий (`true`) или приватный (`false`). | Optional |
| id | string | ID сущности Dynatrace для дашборда. | Required |
| permissions | [DashboardSharePermissions[]](#openapi-definition-DashboardSharePermissions) | Список разрешений на доступ к дашборду. | Required |
| preset | boolean | Если `true`, дашборд будет помечен как предустановленный. | Optional |
| publicAccess | [DashboardAnonymousAccess](#openapi-definition-DashboardAnonymousAccess) | Конфигурация [anonymous access](https://dt-url.net/ov03sf1) к дашборду. | Required |

#### Объект `DashboardSharePermissions`

Разрешения на доступ к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | ID пользователя или группы, которым предоставлено разрешение.  Не применимо, если **type** имеет значение `ALL`. | Optional |
| permission | string | Уровень разрешения:  * `VIEW`: дашборд предоставлен с разрешением на чтение. * `EDIT`: дашборд предоставлен с разрешением на редактирование. Возможные значения: * `EDIT` * `VIEW` | Required |
| type | string | Тип разрешения:  * `USER`: дашборд предоставлен указанному пользователю. * `GROUP`: дашборд предоставлен всем пользователям указанной группы. * `ALL`: дашборд предоставлен по ссылке. Любой аутентифицированный пользователь со ссылкой может просматривать дашборд. Возможные значения: * `ALL` * `GROUP` * `USER` | Required |

#### Объект `DashboardAnonymousAccess`

Конфигурация [anonymous access](https://dt-url.net/ov03sf1) к дашборду.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| managementZoneIds | string[] | Список зон управления, данные которых могут отображаться на публично доступном дашборде.  Укажите здесь ID зон управления. Для каждой указанной зоны управления Dynatrace генерирует ссылку доступа. Их можно получить в списке **urls**.  Чтобы предоставить дашборд с его зоной управления по умолчанию, используйте значение `default`. | Required |
| urls | object | Список URL для анонимного доступа к дашборду.  Каждая ссылка даёт доступ к данным конкретной зоны управления, указанной в списке **managementZoneIds**.  Эти ссылки автоматически генерируются Dynatrace, изменить их нельзя. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}/shareSettings/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная настройка совместного доступа дашборда валидна. Ответ без тела |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

## Связанные темы

* [Дашборды](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать дашборды Dynatrace Dashboards Classic, управлять ими и использовать их.")