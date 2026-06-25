---
title: Process groups API - POST tags
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/topology-and-smartscape/process-groups-api/post-tags
scraped: 2026-05-12T12:02:13.257801
---

# Process groups API - POST tags

# Process groups API - POST tags

* Reference
* Updated on Mar 22, 2023
* Deprecated

Назначает [пользовательские теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") указанной [группе процессов](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов."). Нужно указать только значение тега. Context `CONTEXTLESS` будет назначен автоматически.

Использование этого API ограничено тегами только со значением. Чтобы назначить теги key:value, используйте [Custom tags API](/managed/dynatrace-api/environment-api/custom-tags/post-tags "Назначение пользовательских тегов отслеживаемым сущностям через Dynatrace API.").

Запрос возвращает данные в формате `application/json`

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/entity/infrastructure/process-groups/{meIdentifier}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `DataExport`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | ID сущности Dynatrace для группы процессов, которую нужно обновить. | path | Required |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | JSON-тело запроса. Содержит теги, которые нужно добавить к группе процессов. | body | Optional |

### Объекты тела запроса

#### Объект `UpdateEntity`

Список тегов для назначения сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| tags | string[] | Список тегов для назначения сущности Dynatrace. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **204** | - | Успех. Параметры группы процессов обновлены. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
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

В этом примере запрос назначает тег **PHP** группе процессов **PHP-FPM**, у которой ID **PROCESS\_GROUP-E5C3CC7EC1F80B5B**.

API-токен передаётся в заголовке **Authorization**.

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

* [Process groups](/managed/observe/infrastructure-observability/process-groups "Анализируйте группы процессов и настраивайте именование, обнаружение и мониторинг групп процессов.")