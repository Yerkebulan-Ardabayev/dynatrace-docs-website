---
title: Mobile Symbolication API - GET files for an app version
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app-version
scraped: 2026-05-12T11:19:36.935412
---

# Mobile Symbolication API - GET files for an app version

# Mobile Symbolication API - GET files for an app version

* Reference
* Published Sep 03, 2019

Возвращает метаданные файла символов, относящегося к указанной версии приложения. Для каждой ОС и версии может существовать только один файл символов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}` |

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SymbolFile](#openapi-definition-SymbolFile) | Успех |

### Объекты тела ответа

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
```

## Связанные темы

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.")