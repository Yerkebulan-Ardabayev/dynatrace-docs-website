---
title: Extensions 2.0 API - POST файл extension
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/extensions/post-an-extension
scraped: 2026-05-12T11:56:23.057646
---

# Extensions 2.0 API - POST файл extension

# Extensions 2.0 API - POST файл extension

* Справочник
* Опубликовано 22 января 2021 г.

Загружает файл Extensions 2.0 extension в ваше Dynatrace-окружение.

Запрос принимает payload `application/octet-stream` и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `extensions.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| validateOnly | boolean | Проверить и сохранить (`false`) или только проверить (`true`) загруженный файл extension.  Если не задано, используется `false`. | query | Необязательный |

### Тело запроса

Файл пакета Extension 2.0 (`*.zip`) для загрузки.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionUploadResponseDto](#openapi-definition-ExtensionUploadResponseDto) | Extension корректен |
| **201** | [ExtensionUploadResponseDto](#openapi-definition-ExtensionUploadResponseDto) | Успех. Extension 2.0 загружен. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входной файл некорректен. |
| **409** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Загрузка пока невозможна, повторите попытку через несколько секунд. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ExtensionUploadResponseDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| assetsInfo | [AssetInfo[]](#openapi-definition-AssetInfo) | Информация о включённых ассетах extension |
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

#### Объект `AssetInfo`

Типы ассетов и их количество

| Элемент | Тип | Описание |
| --- | --- | --- |
| assetType | string | - |
| count | integer | - |

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



"assetsInfo": [



{



"assetType": "string",



"count": 1



}



],



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