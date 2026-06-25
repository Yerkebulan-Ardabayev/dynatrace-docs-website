---
title: Extensions API - GET all extensions
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-all-extensions
scraped: 2026-05-12T11:20:00.516123
---

# Extensions API - GET all extensions

# Extensions API - GET all extensions

* Reference
* Published Mar 06, 2020

Выводит список всех расширений, загруженных в ваше окружение Dynatrace.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| pageSize | integer | Количество результатов на страницу. Должно быть от 1 до 500 | query | Optional |
| nextPageKey | string | Курсор для следующей страницы результатов. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionListDto](#openapi-definition-ExtensionListDto) | Успех |

### Объекты тела ответа

#### Объект `ExtensionListDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| extensions | [ExtensionDto[]](#openapi-definition-ExtensionDto) | Список расширений. |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| totalResults | integer | Общее количество записей в результате. |

#### Объект `ExtensionDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | - |
| name | string | - |
| type | string | -Возможные значения: * `ACTIVEGATE` * `CODEMODULE` * `JMX` * `ONEAGENT` * `PMI` * `UNKNOWN` |

### JSON-модели тела ответа

```
{



"extensions": [



{



"id": "custom.python.connectionpool",



"name": "Connection Pool",



"type": "ONEAGENT"



}



],



"nextPageToken": "LlUdYmu5S2MfX/ppfCInR9M=",



"totalResults": 9



}
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")