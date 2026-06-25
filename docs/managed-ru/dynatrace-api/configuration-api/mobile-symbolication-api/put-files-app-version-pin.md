---
title: Mobile Symbolication API - PUT pin files
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version-pin
scraped: 2026-05-12T11:19:33.111055
---

# Mobile Symbolication API - PUT pin files

# Mobile Symbolication API - PUT pin files

* Reference
* Published Sep 03, 2019

Закрепляет или открепляет все файлы символов версии приложения. Закреплённый файл не удаляется автоматически, когда в хранилище файлов символов заканчивается место.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}/pinning` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}/pinning` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `DssFileManagement`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |
| packageName | string | CFBundleIdentifier (iOS) или имя пакета (Android) нужного мобильного приложения. | path | Required |
| os | string | Операционная система нужного приложения. Возможные значения: * `ANDROID` * `IOS` * `TVOS` | path | Required |
| versionCode | string | Код версии (Android) / CFBundleVersion (iOS) нужного приложения. | path | Required |
| versionName | string | Имя версии (Android) / CFBundleShortVersionString (iOS) нужного приложения. | path | Required |
| body | [SymbolFilePinning](#openapi-definition-SymbolFilePinning) | JSON-тело запроса. Содержит устанавливаемый статус закрепления. | body | Optional |

### Объекты тела запроса

#### Объект `SymbolFilePinning`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| pinned | boolean | Статус закрепления файла: `true` для закрепления файла, `false` для открепления файла. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"pinned": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Статус закрепления файла обновлён. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}/pinning/validator` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}/pinning/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `DssFileManagement`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданное тело валидно. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.")