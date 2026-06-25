---
title: Dashboards API - GET all dashboards
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/get-all
scraped: 2026-05-12T11:14:58.562006
---

# Dashboards API - GET all dashboards

# Dashboards API - GET all dashboards

* Reference
* Published Aug 30, 2019

Возвращает список всех дашбордов вашего окружения Dynatrace независимо от прав доступа в UI.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| owner | string | Владелец дашборда. | query | Optional |
| tags | string[] | Список тегов, применённых к дашборду.  Дашборд должен соответствовать **всем** указанным тегам. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DashboardList](#openapi-definition-DashboardList) | Успех |

### Объекты тела ответа

#### Объект `DashboardList`

Список кратких представлений дашбордов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dashboards | [DashboardStub[]](#openapi-definition-DashboardStub) | Список кратких представлений дашбордов. |

#### Объект `DashboardStub`

Краткое представление дашборда.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID дашборда. |
| name | string | Имя дашборда. |
| owner | string | Владелец дашборда. |

### JSON-модели тела ответа

```
{



"dashboards": [



{



"id": "d6740373-ff26-4681-b95f-fd5b858c97f7",



"name": "Home dashboard",



"owner": "admin"



},



{



"id": "54b34dbb-2ae7-4c27-9dbc-90a4f4c68b10",



"name": "Databases",



"owner": "viewer"



},



{



"id": "8525b0bf-e33c-4a92-a534-9dedc1391e10",



"name": "Business value",



"owner": "rocks"



}



]



}
```

## Пример

В этом примере запрос возвращает список всех дашбордов окружения **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards
```

#### Тело ответа

```
{



"dashboards": [



{



"id": "891f3203-9953-4796-aacd-886c0f59dddf",



"name": "Home",



"owner": "admin.user"



},



{



"id": "2768e6ca-e199-4433-9e0d-2922aec2099b",



"name": "Sample dashboard",



"owner": "john.smith"



},



{



"id": "1d7d34c6-0eb1-4131-8d29-9022f8e7f530",



"name": "Kubernetes metrics",



"owner": "jane.brown"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Дашборды](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать дашборды Dynatrace Dashboards Classic, управлять ими и использовать их.")