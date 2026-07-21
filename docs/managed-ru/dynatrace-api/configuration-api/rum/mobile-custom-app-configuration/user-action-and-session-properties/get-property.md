---
title: Mobile and custom app API - GET user session property
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-property
---

# Mobile and custom app API - GET user session property

# Mobile and custom app API - GET user session property

* Справочник
* Опубликовано 05 нояб. 2020 г.

Получает параметры указанного свойства пользовательской сессии приложения.

Запрос формирует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать его, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или кастомного приложения. Его можно найти в Instrumentation Wizard приложения. | путь | Обязательный |
| key | string | Ключ нужного свойства мобильной сессии или пользовательского действия. | путь | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MobileSessionUserActionProperty](#openapi-definition-MobileSessionUserActionProperty) | Успешно |
| **404** | - | Ошибка. Указанная сущность не существует. |

### Объекты тела ответа

#### Объект `MobileSessionUserActionProperty`

Конфигурация свойства мобильной сессии или пользовательского действия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства. Элемент может принимать следующие значения * `AVERAGE` * `FIRST` * `LAST` * `MAX` * `MIN` * `SUM` |
| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажи в нём [регулярное выражение﻿](https://dt-url.net/k9e0iaq?dt=m) для нужных данных. |
| displayName | string | Отображаемое имя свойства. |
| key | string | Уникальный ключ свойства мобильной сессии или пользовательского действия. |
| name | string | Имя передаваемого значения.  Применимо только если **origin** установлено в `API`. |
| origin | string | Источник свойства Элемент может принимать следующие значения * `API` * `SERVER_SIDE_REQUEST_ATTRIBUTE` |
| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только если **origin** установлено в `SERVER_SIDE_REQUEST_ATTRIBUTE`. |
| storeAsSessionProperty | boolean | Если `true`, свойство сохраняется как свойство сессии |
| storeAsUserActionProperty | boolean | Если `true`, свойство сохраняется как свойство пользовательского действия |
| type | string | Тип данных свойства. Элемент может принимать следующие значения * `DOUBLE` * `LONG` * `STRING` |

### Модели тела ответа JSON

```
{



"aggregation": "AVERAGE",



"cleanupRule": "string",



"displayName": "string",



"key": "string",



"name": "string",



"origin": "API",



"serverSideRequestAttribute": "string",



"storeAsSessionProperty": true,



"storeAsUserActionProperty": true,



"type": "DOUBLE"



}
```