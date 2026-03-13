---
title: Policy management API - GET all policy boundaries
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/get-all-boundaries
scraped: 2026-03-04T21:36:14.135297
---

# API управления политиками — GET все границы политик

# API управления политиками — GET все границы политик

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Возвращает список границ политик в рамках определённого уровня.

Запрос возвращает полезную нагрузку типа `application/json`.

## Аутентификация

Для выполнения этого запроса необходимо разрешение **Allow IAM policy configuration for environments** (`iam-policies-management`), назначенное вашему токену. Чтобы узнать, как получить и использовать его, см. [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| size | integer | - | query | Необязательный |
| page | integer | - | query | Необязательный |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID аккаунта. | path | Обязательный |

## Ответ

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| size | integer | - | query | Необязательный |
| page | integer | - | query | Необязательный |
| accountId | - | Идентификатор уровня границы политики. Используйте UUID аккаунта. | path | Обязательный |

## Пример

В этом примере запрос возвращает все границы политик, применимые к аккаунту с `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**. Возвращаются только первые три записи.

#### Curl

```
curl --request GET \



--url 'https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890' \



--header 'accept: application/json' \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### URL запроса

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890
```

#### Тело ответа

```
{



"pageSize": 100,



"pageNumber": 1,



"totalCount": 22,



"content": [



{



"uuid": "a13f7b92-4c8e-4d3a-a1f7-9e3b6c2d8f01",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "Bnd1",



"boundaryQuery": "storage:dt.security_context = '${bindParam:bucket-name-param}';",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"${bindParam:bucket-name-param}"



]



}



],



"metadata": {}



},



{



"uuid": "345a2b02-678e-45ff-92c1-4b4fd5er3b0f",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bnd101",



"boundaryQuery": "storage:gcp.project.id = \"123\";",



"boundaryConditions": [



{



"name": "storage:gcp.project.id",



"operator": "EQ",



"values": [



"123"



]



}



],



"metadata": {}



},



{



"uuid": "a567b345-2345-4ab5-b8d1-0e9a65ae678f",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bnd101_alpha",



"boundaryQuery": "storage:dt.security_context = 'alpha';\n//storage:bucket-name = 'alpha';",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"alpha"



]



}



],



"metadata": {}



},



]



}
```

#### Код ответа

Успешно (200) — успешный ответ — список границ политик
