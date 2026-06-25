---
title: Mobile Symbolication API - GET storage info
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-storage-info
scraped: 2026-05-12T11:19:35.599213
---

# Mobile Symbolication API - GET storage info

# Mobile Symbolication API - GET storage info

* Reference
* Published Sep 03, 2019

Возвращает информацию о хранилище файлов символов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/info` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/info` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `DssFileManagement`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SymbolFileStorageInfo](#openapi-definition-SymbolFileStorageInfo) | Успех |

### Объекты тела ответа

#### Объект `SymbolFileStorageInfo`

| Элемент | Тип | Описание |
| --- | --- | --- |
| availableStorage | integer | Доступное пространство хранилища для файлов символов, в КБ. Имеет значение `-1` при неограниченной квоте. |
| fileCount | integer | - |
| storageQuota | integer | Общая квота хранилища для файлов символов, в КБ. Имеет значение `-1` при неограниченной квоте. |
| usedStorage | integer | Размер хранилища, используемого файлами символов, в КБ. |

### JSON-модели тела ответа

```
{



"availableStorage": 1,



"fileCount": 1,



"storageQuota": 1,



"usedStorage": 1



}
```

## Связанные темы

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Узнайте о деобфускации (Android) и символикации (iOS и tvOS) и о ваших возможностях по загрузке файлов символов и управлению ими в Dynatrace.")