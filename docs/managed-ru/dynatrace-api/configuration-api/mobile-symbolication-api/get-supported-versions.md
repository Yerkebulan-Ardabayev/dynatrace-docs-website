---
title: Mobile Symbolication API - GET supported version
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-supported-versions
scraped: 2026-05-12T11:19:42.572610
---

# Mobile Symbolication API - GET supported version

# Mobile Symbolication API - GET supported version

* Reference
* Published Sep 03, 2019

Возвращает поддерживаемую версию формата файла для файлов символов iOS.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/ios/supportedversion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/ios/supportedversion` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `DssFileManagement`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SupportedVersion](#openapi-definition-SupportedVersion) | Успех |

### Объекты тела ответа

#### Объект `SupportedVersion`

| Элемент | Тип | Описание |
| --- | --- | --- |
| version | string | Поддерживаемая версия формата файла iOS. |

### JSON-модели тела ответа

```
{



"version": "string"



}
```

## Связанные темы

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.")