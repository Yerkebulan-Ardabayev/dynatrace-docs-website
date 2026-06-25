---
title: Extensions 2.0 API - GET все файлы
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/schemas/get-all-files
scraped: 2026-05-12T11:56:27.083655
---

# Extensions 2.0 API - GET все файлы

# Extensions 2.0 API - GET все файлы

* Справочник
* Опубликовано 22 января 2021 г.

Список всех файлов в указанной версии schema Extensions 2.0 extension.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/schemas/{schemaVersion}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/schemas/{schemaVersion}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensions.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| schemaVersion | string | Версия schema. | path | Обязательный |
| Accept | string | Заголовок Accept. Указывает часть extension 2.0, которая будет возвращена:  * application/json; charset=utf-8 - возвращает метаданные extension 2.0 в JSON * application/octet-stream - возвращает zip-пакет extension 2.0, хранящийся на сервере. | header | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SchemaFiles](#openapi-definition-SchemaFiles) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SchemaFiles`

| Элемент | Тип | Описание |
| --- | --- | --- |
| files | string[] | Список файлов schema. |

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



"files": [



"string"



]



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