---
title: Problems API v2 - GET все комментарии
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems-v2/comments/get-all
scraped: 2026-05-12T11:57:14.886361
---

# Problems API v2 - GET все комментарии

# Problems API v2 - GET все комментарии

* Справочник
* Опубликовано 12 октября 2020 г.

Возвращает список всех комментариев к указанной проблеме.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/problems/{problemId}/comments` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/problems/{problemId}/comments` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `problems.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| problemId | string | ID требуемой проблемы. | path | Обязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Находится в поле **nextPageKey** предыдущего ответа. Первая страница возвращается всегда, если query-параметр **nextPageKey** не указан. Когда **nextPageKey** задан для получения следующих страниц, все остальные query-параметры нужно опустить, кроме необязательного параметра **fields**. | query | Необязательный |
| pageSize | integer | Количество комментариев в одном payload ответа. Максимально допустимый размер страницы: 500. Если не задан, используется 10. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CommentsList](#openapi-definition-CommentsList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CommentsList`

Список комментариев.

| Поле | Тип | Описание |
| --- | --- | --- |
| comments | [Comment[]](#openapi-definition-Comment) | Записи результата. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`. Используйте его в query-параметре **nextPageKey** для получения следующих страниц результата. |
| pageSize | integer | Количество записей на страницу. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `Comment`

Комментарий к проблеме.

| Поле | Тип | Описание |
| --- | --- | --- |
| authorName | string | Пользователь, написавший комментарий. |
| content | string | Текст комментария. |
| context | string | Контекст комментария. |
| createdAtTimestamp | integer | Метка времени создания комментария, в UTC миллисекундах. |
| id | string | ID комментария. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"comments": [



{



"authorName": "string",



"content": "string",



"context": "string",



"createdAtTimestamp": 1,



"id": "string"



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



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

## Связанные темы

* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")