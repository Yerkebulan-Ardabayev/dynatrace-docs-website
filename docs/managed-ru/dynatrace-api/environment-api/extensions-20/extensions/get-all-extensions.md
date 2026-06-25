---
title: Extensions 2.0 API - GET все extensions
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/extensions/get-all-extensions
scraped: 2026-05-12T11:56:40.472100
---

# Extensions 2.0 API - GET все extensions

# Extensions 2.0 API - GET все extensions

* Справочник
* Опубликовано 22 января 2021 г.

Список всех Extensions 2.0 extensions, доступных в вашем Dynatrace-окружении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensions.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Если параметр запроса **nextPageKey** не указан, всегда возвращается первая страница.  Когда **nextPageKey** задан для получения последующих страниц, все остальные параметры запроса нужно опустить. | query | Необязательный |
| pageSize | integer | Количество extensions в одном payload ответа.  Максимально допустимый размер страницы, 100.  Если не задано, используется 20. | query | Необязательный |
| name | string | Фильтрует результирующий набор extensions 2.0 по имени. Можно указать частичное имя. В этом случае используется оператор CONTAINS. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionList](#openapi-definition-ExtensionList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ExtensionList`

| Элемент | Тип | Описание |
| --- | --- | --- |
| extensions | [MinimalExtension[]](#openapi-definition-MinimalExtension) | Список extensions. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в параметре запроса **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `MinimalExtension`

Список extensions.

| Элемент | Тип | Описание |
| --- | --- | --- |
| extensionName | string | Имя extension |
| version | string | Версия extension |

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
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"extensions": [



{



"extensionName": "string",



"version": "1.2.3"



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

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")