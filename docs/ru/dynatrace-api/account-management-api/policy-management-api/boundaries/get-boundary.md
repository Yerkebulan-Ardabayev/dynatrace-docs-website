---
title: Policy management API - GET a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/get-boundary
scraped: 2026-03-03T21:29:45.609196
---

# API управления политиками — GET граница политики


Возвращает границу политики в рамках уровня.

Запрос возвращает полезную нагрузку типа `application/json`.

## Аутентификация

Для выполнения этого запроса необходимо разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`), назначенное вашему токену. Чтобы узнать, как его получить и использовать, см. раздел OAuth clients.

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | Идентификатор требуемой границы. | path | Обязательный |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID учётной записи. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Успешный ответ — граница политики |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Ошибка. Указанный ресурс не найден. |

### Объекты тела ответа

#### Объект `PolicyBoundaryOverview`

| Элемент | Тип | Описание |
| --- | --- | --- |
| uuid | string | - |
| levelType | string | - |
| levelId | string | - |
| name | string | Отображаемое имя границы политики. |
| boundaryQuery | string | Запрос границы политики. |
| boundaryConditions | [Condition[]](#openapi-definition-Condition) | - |
| metadata | [Map](#openapi-definition-Map) | Метаданные границы политики. |

#### Объект `Condition`

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Имя условия. Указывает, какая часть **служб** проверяется условием. |
| operator | string | Оператор условия. |
| values | string[] | Список эталонных значений условия. |

#### Объект `Map`

#### Объект `ErrorDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | number | Код ошибки. |
| message | string | Краткое описание ошибки. |
| errorsMap | object | - |

### JSON-модели тела ответа

```
{


"uuid": "string",


"levelType": "string",


"levelId": "string",


"name": "string",


"boundaryQuery": "string",


"boundaryConditions": [


{


"name": "string",


"operator": "string",


"values": [


"string"


]


}


],


"metadata": {}


}
```

```
{


"code": 1,


"message": "string",


"errorsMap": {}


}
```

## Пример

В данном примере запрос получает сведения о границе политики с UUID **9a7b6c54-3d2e-4f10-a8b2-7cde9012f345** для учётной записи с `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request GET \


--url 'https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345' \


--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### URL запроса

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345
```

#### Тело ответа

```
{


"uuid": "9a7b6c54-3d2e-4f10-a8b2-7cde9012f345",


"levelType": "account",


"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",


"name": "bndry_teamA",


"boundaryQuery": "storage:dt.security_context = \"TEAM-AB\";",


"boundaryConditions": [


{


"name": "storage:dt.security_context",


"operator": "EQ",


"values": [


"TEAM-A"


]


}


],


"metadata": {}


}
```

#### Код ответа

200 — Успешный ответ — граница политики.
