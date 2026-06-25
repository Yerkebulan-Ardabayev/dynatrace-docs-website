---
title: Hub capabilities API - GET элементов
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/get-items
scraped: 2026-05-12T11:54:47.112052
---

# Hub capabilities API - GET элементов

# Hub capabilities API - GET элементов

* Reference
* Published Feb 07, 2023

Выводит список всех доступных элементов Hub.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/items` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/items` |

## Аутентификация

Для выполнения запроса необходим access token со scope `hub.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если параметр запроса **nextPageKey** не указан.  Когда **nextPageKey** задан для получения последующих страниц, все остальные query-параметры должны быть пропущены. | query | Опциональный |
| pageSize | integer | Количество элементов Hub в одном теле ответа.  Максимально допустимый размер страницы 100.  Если не задано, используется 20. | query | Опциональный |
| itemType | string | Если указан, отфильтрует результаты по заданному типу элемента. Элемент может принимать значения * `EXTENSION1` * `EXTENSION2` * `TECHNOLOGY` | query | Опциональный |
| query | string | Фильтрует результаты по элементам, соответствующим строке запроса в id, name, author, description или любом теге.  * Без учёта регистра * Пробелы в строке запроса приводят к пересечению результатов каждого термина | query | Опциональный |
| installed | boolean | Если указан, ограничит результат до Extensions 2.0 с соответствующим состоянием установки.  * Применяется только если фильтр itemType не задан или равен EXTENSION2 | query | Опциональный |
| categoryId | string | Если указан, отфильтрует элементы, принадлежащие заданной категории.  * Переопределяет фильтры itemType или installed * Список ID категорий см. /categories * Возвращает элементы в порядке категории | query | Опциональный |
| offset | string | Если указан, пропустит заданное количество результатов, что позволяет реализовать пагинацию в сочетании с размером страницы | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ItemList](#openapi-definition-ItemList) | OK |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Недоступно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ItemList`

| Элемент | Тип | Описание |
| --- | --- | --- |
| items | [ItemOverview[]](#openapi-definition-ItemOverview) | Список доступных элементов. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в параметре запроса **nextPageKey**, чтобы получить последующие страницы результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `ItemOverview`

Обзор элемента.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activationLink | string | Ссылка активации для технологии |
| artifactId | string | Уникальный ID, используемый артефактами в релизах. |
| authorLogo | string | URL логотипа автора. |
| authorName | string | Имя автора элемента. |
| clusterCompatible | boolean | Проверяет, совместим ли элемент с версией кластера. |
| comingSoon | boolean | Запланирован ли элемент к выпуску в ближайшее время |
| description | string | Описание элемента. |
| documentationLink | string | Абсолютная ссылка на страницу документации этого элемента. |
| hasDescriptionBlocks | boolean | Содержит ли вызов details блоки описания. |
| itemId | string | Уникальный ID элемента. |
| logo | string | Логотип элемента. Может быть URL или Base64-кодировкой. Предназначен для html-тегов |
| marketingLink | string | Абсолютная ссылка на маркетинговую страницу этого элемента. |
| name | string | Имя элемента. |
| notCompatibleReason | string | Причина, по которой элемент несовместим с версией кластера. |
| tags | string[] | Группировка элементов по ключевым словам. |
| type | string | Представляет тип элемента. Может быть TECHNOLOGY, EXTENSION1 или EXTENSION2. Элемент может принимать значения * `EXTENSION1` * `EXTENSION2` * `TECHNOLOGY` |

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
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"items": [



{



"activationLink": "string",



"artifactId": "snmp-extension.dynatrace.com",



"authorLogo": "string",



"authorName": "string",



"clusterCompatible": true,



"comingSoon": true,



"description": "string",



"documentationLink": "string",



"hasDescriptionBlocks": true,



"itemId": "string",



"logo": "string",



"marketingLink": "string",



"name": "string",



"notCompatibleReason": "string",



"tags": [



"string"



],



"type": "EXTENSION1"



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