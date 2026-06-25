---
title: Mobile and custom app API - GET key user actions
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/get-configuration
scraped: 2026-05-12T11:15:28.898822
---

# Mobile and custom app API - GET key user actions

# Mobile and custom app API - GET key user actions

* Reference
* Published Nov 05, 2020

Возвращает список ключевых пользовательских действий в указанном приложении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions` |

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
| **200** | [KeyUserActionMobileList](#openapi-definition-KeyUserActionMobileList) | Успех |
| **404** | - | Сбой. Указанная сущность не существует. |

### Объекты тела ответа

#### Объект `KeyUserActionMobileList`

Список ключевых действий в приложении.

| Элемент | Тип | Описание |
| --- | --- | --- |
| keyUserActions | [KeyUserActionMobile[]](#openapi-definition-KeyUserActionMobile) | Список ключевых действий в приложении. |

#### Объект `KeyUserActionMobile`

Ключевое пользовательское действие.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя ключевого пользовательского действия. |

### JSON-модели тела ответа

```
{



"keyUserActions": [



{



"name": "string"



}



]



}
```

## Связанные темы

* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с вашим приложением.")