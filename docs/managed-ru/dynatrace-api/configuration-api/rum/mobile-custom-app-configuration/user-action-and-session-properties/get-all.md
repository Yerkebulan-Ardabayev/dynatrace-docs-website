---
title: Mobile and custom app API - GET all user session properties
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/user-action-and-session-properties/get-all
scraped: 2026-05-12T11:15:35.461976
---

# Mobile and custom app API - GET all user session properties

# Mobile and custom app API - GET all user session properties

* Reference
* Published Nov 05, 2020

Перечисляет все свойства пользовательских сессий и пользовательских действий из указанного мобильного или пользовательского приложения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/userActionAndSessionProperties` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [MobileSessionUserActionPropertyList](#openapi-definition-MobileSessionUserActionPropertyList) | Успех |

### Объекты тела ответа

#### Объект `MobileSessionUserActionPropertyList`

Содержит списки кратких представлений свойств мобильных сессий и свойств мобильных пользовательских действий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| sessionProperties | [MobileSessionUserActionPropertyShort[]](#openapi-definition-MobileSessionUserActionPropertyShort) | Список кратких представлений свойств мобильных сессий. |
| userActionProperties | [MobileSessionUserActionPropertyShort[]](#openapi-definition-MobileSessionUserActionPropertyShort) | Список кратких представлений свойств мобильных пользовательских действий. |

#### Объект `MobileSessionUserActionPropertyShort`

Краткое представление свойства мобильной сессии или пользовательского действия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| displayName | string | Отображаемое имя свойства сессии или пользовательского действия. |
| key | string | Ключ свойства сессии или пользовательского действия. |

### JSON-модели тела ответа

```
{



"sessionProperties": [



{



"displayName": "string",



"key": "string"



}



],



"userActionProperties": [



{}



]



}
```