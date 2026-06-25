---
title: Mobile and custom app API - POST a key user action
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration/key-user-actions/post-configuration
scraped: 2026-05-12T11:15:30.099797
---

# Mobile and custom app API - POST a key user action

# Mobile and custom app API - POST a key user action

* Reference
* Published Nov 05, 2020

Добавляет пользовательское действие в список ключевых пользовательских действий в указанном приложении.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions/{actionName}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/mobile/{applicationId}/keyUserActions/{actionName}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| applicationId | string | UUID нужного мобильного или пользовательского приложения. Его можно найти в мастере инструментирования вашего приложения. | path | Required |
| actionName | string | Имя пользовательского действия, отмечаемого как ключевое пользовательское действие. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [KeyUserActionMobile](#openapi-definition-KeyUserActionMobile) | Успех. Действие отмечено как ключевое пользовательское действие. Ответ содержит его имя. |
| **404** | - | Сбой. Указанная сущность не существует. |
| **409** | - | Сбой. Достигнуто максимальное число ключевых пользовательских действий для приложения. |

### Объекты тела ответа

#### Объект `KeyUserActionMobile`

Ключевое пользовательское действие.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя ключевого пользовательского действия. |

### JSON-модели тела ответа

```
{



"name": "string"



}
```

## Связанные темы

* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с вашим приложением.")