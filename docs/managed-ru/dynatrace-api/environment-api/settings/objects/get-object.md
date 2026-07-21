---
title: Settings API - GET an object
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/objects/get-object
scraped: 2026-05-12T11:35:54.090860
---

# Settings API - GET an object

# Settings API - GET an object

* Reference
* Published Feb 24, 2021

Возвращает указанный settings object.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/settings/objects/{objectId}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `settings.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| objectId | string | ID нужного settings object. | path | Required |
| adminAccess | boolean | Если установлено в true и у пользователя есть право settings:objects:admin, endpoint будет действовать так, как будто пользователь является владельцем всех объектов | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SettingsObjectByObjectIdResponse](#openapi-definition-SettingsObjectByObjectIdResponse) | Успех |
| **403** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Доступ запрещён. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Нет объекта для указанного objectId |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SettingsObjectByObjectIdResponse`

Ответ на запрос получения по objectId.

| Элемент | Тип | Описание |
| --- | --- | --- |
| author | string | Пользователь (идентифицированный по ID пользователя или ID публичного токена), который выполнил эту последнюю модификацию. |
| created | integer | Временная метка создания. |
| createdBy | string | Уникальный идентификатор пользователя, который создал settings object. |
| externalId | string | Внешний идентификатор settings object. |
| modified | integer | Временная метка последней модификации. |
| modifiedBy | string | Уникальный идентификатор пользователя, который выполнил последнюю модификацию. |
| objectId | string | ID settings object. |
| owner | [Identity](#openapi-definition-Identity) | Identity, описывающая пользователя, группу или группу all-users (применяемую ко всем пользователям). |
| resourceContext | [ResourceContext](#openapi-definition-ResourceContext) | Контекст ресурса, содержащий дополнительную информацию о правах на объект. |
| schemaId | string | Schema, на которой основан объект. |
| schemaVersion | string | Версия schema, на которой основан объект. |
| scope | string | Scope, на который нацелен объект. Подробнее см. [Dynatrace Documentation](https://dt-url.net/ky03459?dt=m). |
| searchSummary | string | Доступная для поиска строка-сводка значения настройки. Обычный текст без Markdown. |
| summary | string | Краткая сводка настроек. Может содержать Markdown и будет соответствующим образом экранирована. |
| updateToken | string | Update token объекта. Вы можете использовать его для обнаружения одновременных модификаций разными пользователями.  Он генерируется при получении (GET-запросы). Если задан при обновлении (PUT-запрос) или удалении, обновление/удаление будет разрешено только если между получением и обновлением не было изменений.  Если опущен при обновлении/удалении, операция переопределяет текущее значение или удаляет его без каких-либо проверок. |
| value | string | Значение настройки.  Оно определяет фактические значения параметров настроек.  Фактическое содержимое зависит от schema объекта. |

#### Объект `Identity`

Identity, описывающая пользователя, группу или группу all-users (применяемую ко всем пользователям).

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID пользователя или ID группы пользователей, если type равен 'user' или 'group', отсутствует, если type равен 'all-users'. |
| type | string | Тип идентичности. Возможные значения: * `all-users` * `group` * `user` |

#### Объект `ResourceContext`

Контекст ресурса, содержащий дополнительную информацию о правах на объект.

| Элемент | Тип | Описание |
| --- | --- | --- |
| modifications | [Modification](#openapi-definition-Modification) | Дополнительные сведения о модификации для этого settings object. |
| operations | string[] | Разрешённые операции над этим settings object. Возможные значения: * `delete` * `read` * `write` |

#### Объект `Modification`

Дополнительные сведения о модификации для этого settings object.

| Элемент | Тип | Описание |
| --- | --- | --- |
| first | boolean | Находится ли неперемещаемый settings object в первой группе неперемещаемых настроек или в последней (начало или конец списка). |
| modifiablePaths | string[] | Пути свойств, которые модифицируемы, независимо от того, разрешена ли операция `write`. |
| movable | boolean | Может ли settings object быть перемещён/переупорядочен. Применимо только для schema упорядоченного списка. |
| nonModifiablePaths | string[] | Пути свойств, которые не модифицируемы, даже если операция `write` разрешена. |

#### Объект `AnyValue`

Schema, представляющая произвольный тип значения.

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
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



"author": "john.doe@example.com",



"created": 1,



"createdBy": "fab17b7a-2eb2-4c95-b818-743d94be2c30",



"externalId": "string",



"modified": 1,



"modifiedBy": "fab17b7a-2eb2-4c95-b818-743d94be2c30",



"objectId": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"owner": {



"id": "string",



"type": "user"



},



"resourceContext": {



"modifications": {



"first": true,



"modifiablePaths": [



"string"



],



"movable": true,



"nonModifiablePaths": [



"string"



]



},



"operations": [



"delete"



]



},



"schemaId": "builtin:container.built-in-monitoring-rule",



"schemaVersion": "1.0.0",



"scope": "HOST-D3A3C5A146830A79",



"searchSummary": "string",



"summary": "string",



"updateToken": "Y2ktaGdyb3VwLTEyMythZjhjOThlOS0wN2I0LTMyMGEtOTQzNi02NTEyMmVlNWY4NGQ=",



"value": "string"



}
```

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