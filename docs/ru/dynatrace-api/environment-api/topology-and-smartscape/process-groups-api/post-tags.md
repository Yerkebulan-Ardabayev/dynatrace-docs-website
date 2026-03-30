---
title: Process groups API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags
scraped: 2026-03-05T21:26:46.189276
---

# API групп процессов — POST tags


* Устарело

Назначает пользовательские теги указанной группе процессов. Достаточно указать только значение тега. Контекст `CONTEXTLESS` будет назначен автоматически.

Использование этого API ограничено тегами, содержащими только значение. Для назначения тегов в формате ключ:значение используйте API пользовательских тегов.

Запрос возвращает `application/json`

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью `DataExport`.

Чтобы узнать, как получить и использовать токен, см. Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательно |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace группы процессов, которую нужно обновить. | path | Обязательно |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | Тело запроса в формате JSON. Содержит теги, которые нужно добавить к группе процессов. | body | Необязательно |

### Объекты тела запроса

#### Объект `UpdateEntity`

Список тегов, назначаемых сущности Dynatrace.

| Элемент | Тип | Описание | Обязательно |
| --- | --- | --- | --- |
| tags | string[] | Список тегов, назначаемых сущности Dynatrace. | Обязательно |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Она должна быть адаптирована для использования в реальном запросе.

```
{


"tags": [


"office-linz",


"office-klagenfurt"


]


}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Параметры группы процессов были обновлены. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |
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
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | — Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

В этом примере запрос назначает тег **PHP** группе процессов **PHP-FPM** с идентификатором **PROCESS\_GROUP-E5C3CC7EC1F80B5B**.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \


https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \


-H 'Content-Type: application/json' \


-d '{


"tags": [


"PHP"


]


}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/process-groups/PROCESS_GROUP-E5C3CC7EC1F80B5B
```

#### Тело запроса

```
{


"tags": [


"PHP"


]


}
```

#### Код ответа

204

## Связанные темы

* Группы процессов
