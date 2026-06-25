---
title: Mobile Symbolication API - GET files for an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app
scraped: 2026-05-12T11:19:30.450675
---

# Mobile Symbolication API - GET files for an app

# Mobile Symbolication API - GET files for an app

* Reference
* Published Sep 03, 2019

Возвращает метаданные всех файлов символов (файлов Android mapping и файлов iOS/tvOS symbol extract) для мобильного приложения из хранилища файлов символов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `DssFileManagement`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SymbolFileList](#openapi-definition-SymbolFileList) | Успех |

### Объекты тела ответа

#### Объект `SymbolFileList`

| Элемент | Тип | Описание |
| --- | --- | --- |
| symbolFiles | [SymbolFile[]](#openapi-definition-SymbolFile) | Список файлов символов. |

#### Объект `SymbolFile`

| Элемент | Тип | Описание |
| --- | --- | --- |
| appId | [AppIdentifier](#openapi-definition-AppIdentifier) | Идентификационная информация приложения, которому принадлежит файл. |
| applicationName | string | Имя приложения, которому принадлежит файл. |
| pinned | boolean | Закреплён ли файл и поэтому не может быть удалён. |
| size | integer | Размер файла, в КБ. |
| uploadTimestamp | integer | Временная метка загрузки файла, в миллисекундах UTC |

#### Объект `AppIdentifier`

Идентификационная информация приложения, которому принадлежит файл.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID мобильного приложения. |
| os | string | Операционная система, которой принадлежит файл. Возможные значения: * `ANDROID` * `IOS` * `TVOS` |
| packageName | string | bundleId (iOS) или имя пакета (Android), которому принадлежит файл. |
| versionCode | string | Код версии (Android) / версия бандла (iOS), которой принадлежит файл. |
| versionName | string | Имя версии (Android) / строка версии бандла (iOS), которой принадлежит файл. |

### JSON-модели тела ответа

```
{



"symbolFiles": [



{



"appId": {



"id": "string",



"os": "ANDROID",



"packageName": "string",



"versionCode": "string",



"versionName": "string"



},



"applicationName": "string",



"pinned": true,



"size": 1,



"uploadTimestamp": 1



}



]



}
```

## Связанные темы

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.")