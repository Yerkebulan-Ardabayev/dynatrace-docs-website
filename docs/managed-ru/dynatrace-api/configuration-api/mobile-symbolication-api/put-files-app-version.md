---
title: Mobile Symbolication API - PUT upload file for an app version
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version
scraped: 2026-05-12T11:19:31.742052
---

# Mobile Symbolication API - PUT upload file for an app version

# Mobile Symbolication API - PUT upload file for an app version

* Reference
* Updated on Nov 12, 2025

Загружает файл символов (файл Android mapping и файл iOS/tvOS symbol extract) для указанной версии мобильного приложения.

* Для приложений iOS необходимо предварительно обработать файлы dSYM через DSSClient перед их передачей в Dynatrace. Подробнее смотрите [Upload symbol files via REST API](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#ios-api "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.").
* Вы можете загрузить файл символов в любом поддерживаемом формате (сжатом или несжатом). Обратите внимание на следующие ограничения:

  + Загружаемый файл не должен превышать 100 MiB.
  + Несжатый файл не должен превышать 500 MiB после распаковки (если он сжат).

  Если файл слишком большой, попробуйте сжать его, чтобы уложиться в лимит загрузки 100 MiB.

Запрос принимает один из следующих типов payload:

* `application/x-compressed`
* `application/x-zip-compressed`
* `application/zip`
* `text/plain`

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}` |

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
| content-type | string | - | header | Optional |
| body | string | Загружаемый файл: proguard-файл (\*.txt) для Android или zip-файл, созданный DTXDssClient, поставляемым с OneAgent для iOS. | body | Required |

### Объекты тела запроса

#### Объект `RequestBody`

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Файл загружен и сохранён. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |
| **413** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Квота хранилища файлов символов исчерпана. |

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

## Связанные темы

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.")