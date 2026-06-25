---
title: Mobile Symbolication API - DELETE files for an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/del-files-app
scraped: 2026-05-12T11:19:41.355395
---

# Mobile Symbolication API - DELETE files for an app

# Mobile Symbolication API - DELETE files for an app

* Reference
* Published Sep 03, 2019

Удаляет все файлы символов (файлы Android mapping и файлы iOS/tvOS symbol extract) для мобильного приложения из хранилища файлов символов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}` |

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
| **204** | - | Успех. Все файлы, относящиеся к указанному мобильному приложению, успешно удалены. Ответ без тела. |
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

## Связанные темы

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.")