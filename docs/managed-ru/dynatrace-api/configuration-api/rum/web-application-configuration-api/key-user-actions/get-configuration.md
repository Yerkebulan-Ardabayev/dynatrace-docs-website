---
title: Web application configuration API - GET key user actions
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/get-configuration
scraped: 2026-05-12T11:17:04.697696
---

# Web application configuration API - GET key user actions

# Web application configuration API - GET key user actions

* Reference
* Published Sep 24, 2020

Возвращает список ключевых пользовательских действий в указанном приложении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/keyUserActions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/{id}/keyUserActions` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного веб-приложения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [KeyUserActionList](#openapi-definition-KeyUserActionList) | Успех |

### Объекты тела ответа

#### Объект `KeyUserActionList`

Список ключевых пользовательских действий в веб-приложении

| Элемент | Тип | Описание |
| --- | --- | --- |
| keyUserActionList | [KeyUserAction[]](#openapi-definition-KeyUserAction) | - |

#### Объект `KeyUserAction`

Конфигурация ключевого пользовательского действия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| actionType | string | Тип действия. Возможные значения: * `Custom` * `Load` * `Xhr` |
| domain | string | Домен, в котором выполняется действие. |
| meIdentifier | string | ID сущности Dynatrace для действия. |
| name | string | Имя действия. |

### JSON-модели тела ответа

```
{



"keyUserActionList": [



{



"actionType": "Load",



"domain": "test.com",



"meIdentifier": "APPLICATION_METHOD-1234",



"name": "Loading of page /example"



}



]



}
```

## Связанные темы

* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с вашим приложением.")