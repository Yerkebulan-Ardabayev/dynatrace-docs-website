---
title: Mobile and custom app API - GET user session property
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-property
scraped: 2026-05-12T11:15:23.703299
---

# Mobile and custom app API - GET user session property

# Mobile and custom app API - GET user session property

* Reference
* Published Nov 05, 2020

Возвращает параметры указанного свойства пользовательской сессии приложения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties/{key}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |
| key | string | Ключ нужного свойства мобильной сессии или пользовательского действия. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MobileSessionUserActionProperty](#openapi-definition-MobileSessionUserActionProperty) | Успех |
| **404** | - | Сбой. Указанная сущность не существует. |

### Объекты тела ответа

#### Объект `MobileSessionUserActionProperty`

Конфигурация свойства мобильной сессии или пользовательского действия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregation | string | Тип агрегации свойства.  Определяет, как агрегируются несколько значений свойства. Возможные значения: * `AVERAGE` * `FIRST` * `LAST` * `MAX` * `MIN` * `SUM` |
| cleanupRule | string | Правило очистки свойства.  Определяет, как извлечь нужные данные из строкового значения. Укажите [регулярное выражение](https://dt-url.net/k9e0iaq) для нужных вам данных. |
| displayName | string | Отображаемое имя свойства. |
| key | string | Уникальный ключ свойства мобильной сессии или пользовательского действия. |
| name | string | Имя передаваемого значения.  Применимо только когда **origin** установлен в `API`. |
| origin | string | Источник свойства Возможные значения: * `API` * `SERVER_SIDE_REQUEST_ATTRIBUTE` |
| serverSideRequestAttribute | string | ID атрибута запроса.  Применимо только когда **origin** установлен в `SERVER_SIDE_REQUEST_ATTRIBUTE`. |
| storeAsSessionProperty | boolean | Если `true`, свойство хранится как свойство сессии |
| storeAsUserActionProperty | boolean | Если `true`, свойство хранится как свойство пользовательского действия |
| type | string | Тип данных свойства. Возможные значения: * `DOUBLE` * `LONG` * `STRING` |

### JSON-модели тела ответа

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