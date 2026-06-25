---
title: Hosts API - DELETE tag
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/del-tags
scraped: 2026-05-12T12:03:12.579507
---

# Hosts API - DELETE tag

# Hosts API - DELETE tag

* Reference
* Updated on Mar 22, 2023
* Deprecated

Этот API устарел. Используйте [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Узнайте о Dynatrace Monitored entities API.") вместо него.

Удаляет указанный [пользовательский тег](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") с указанного хоста. Удаление нельзя отменить.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/infrastructure/hosts/{meIdentifier}/tags/{tag}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/infrastructure/hosts/{meIdentifier}/tags/{tag}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | ID сущности Dynatrace для хоста. | path | Required |
| tag | string | Тег, который нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Тег хоста удалён. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **404** | - | Сбой. Тег не найден. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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

## Пример

В этом примере запрос удаляет тег **Rack123** с хоста **tag009**, у которого ID **HOST-B7A6F9EE9F366CB5**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5/tags/Rack123 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5/tags/Rack123
```

#### Код ответа

204

## Связанные темы

* [Hosts](/managed/observe/infrastructure-observability/hosts "Узнайте, как начать работу с мониторингом хостов, какие показатели влияют на здоровье хоста, как настроить пользовательские имена хостов и многое другое.")