---
title: Dashboards API - DELETE a dashboard
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/del-dashboard
scraped: 2026-05-12T11:14:57.205468
---

# Dashboards API - DELETE a dashboard

# Dashboards API - DELETE a dashboard

* Reference
* Published Aug 30, 2019

Удаляет указанный дашборд.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого дашборда. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Дашборд удалён. Ответ без тела. |

## Пример

В этом примере запрос удаляет дашборд, созданный в примере [POST request](/managed/dynatrace-api/configuration-api/dashboards-api/del-dashboard#example "Удаление дашборда через Dynatrace Classic API."). Код ответа **204** означает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/7dd386fe-f91d-42e3-a2ec-0c88070933f4 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
DELETE https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards/7dd386fe-f91d-42e3-a2ec-0c88070933f4
```

#### Код ответа

204

## Связанные темы

* [Дашборды](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать дашборды Dynatrace Dashboards Classic, управлять ими и использовать их.")