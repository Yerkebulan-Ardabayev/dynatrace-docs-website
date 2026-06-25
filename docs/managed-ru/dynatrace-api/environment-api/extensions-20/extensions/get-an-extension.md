---
title: Extensions 2.0 API - GET extension
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/extensions/get-an-extension
scraped: 2026-05-12T11:56:13.145764
---

# Extensions 2.0 API - GET extension

# Extensions 2.0 API - GET extension

* Справочник
* Опубликовано 22 января 2021 г.

Возвращает свойства указанного Extensions 2.0 extension или скачивает ZIP-файл extension.

В зависимости от значения заголовка запроса **Accept** запрос возвращает один из следующих типов payload:

* `application/json`, JSON-payload, содержащий свойства extension.
* `application/octet-stream`, скачивание ZIP-файла extension.

Если заголовок **Accept** в запросе не указан, возвращается payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/{extensionVersion}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/{extensionVersion}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensions.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| extensionName | string | Имя требуемого extension 2.0. | path | Обязательный |
| extensionVersion | string | Версия требуемого extension 2.0 | path | Обязательный |
| Accept | string | Заголовок Accept. Указывает часть extension 2.0, которая будет возвращена:  * application/json; charset=utf-8 - возвращает метаданные extension 2.0 в JSON * application/octet-stream - возвращает zip-пакет extension 2.0, хранящийся на сервере. | header | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Extension](#openapi-definition-Extension) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `Extension`

| Элемент | Тип | Описание |
| --- | --- | --- |
| author | [AuthorDto](#openapi-definition-AuthorDto) | Автор extension |
| dataSources | string[] | Источники данных, которые extension использует для сбора данных |
| extensionName | string | Имя extension |
| featureSets | string[] | Доступные наборы возможностей |
| featureSetsDetails | object | Детали наборов возможностей |
| fileHash | string | SHA-256 хеш загруженного файла Extension |
| minDynatraceVersion | string | Минимальная версия Dynatrace, с которой работает extension |
| minEECVersion | string | Минимальная версия Extension Execution Controller, с которой работает extension |
| variables | string[] | Пользовательские переменные, используемые в конфигурации extension |
| version | string | Версия extension |

#### Объект `AuthorDto`

Автор extension

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя автора |

#### Объект `FeatureSetDetails`

Дополнительная информация о наборе возможностей

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Необязательное описание набора возможностей |
| displayName | string | Необязательное отображаемое имя набора возможностей |
| isRecommended | boolean | Помечает набор возможностей как рекомендуемый (выбран по умолчанию при активации) |
| metrics | [MetricDto[]](#openapi-definition-MetricDto) | Метрики набора возможностей |

#### Объект `MetricDto`

Метрика, собираемая extension

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ метрики |
| metadata | [MetricMetadataDto](#openapi-definition-MetricMetadataDto) | Метаданные метрики |

#### Объект `MetricMetadataDto`

Метаданные метрики

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание метрики |
| displayName | string | Имя метрики в интерфейсе пользователя |
| unit | string | Единица измерения метрики |

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



"author": {



"name": "string"



},



"dataSources": [



"string"



],



"extensionName": "string",



"featureSets": [



"string"



],



"featureSetsDetails": {},



"fileHash": "string",



"minDynatraceVersion": "string",



"minEECVersion": "string",



"variables": [



"string"



],



"version": "1.2.3"



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