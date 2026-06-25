---
title: Reports API - GET a report
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/get-report
scraped: 2026-05-12T11:15:46.763842
---

# Reports API - GET a report

# Reports API - GET a report

* Reference
* Published Jan 16, 2020

Возвращает свойства указанного отчёта.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужного отчёта. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DashboardReport](#openapi-definition-DashboardReport) | Успех. Тело ответа содержит параметры отчёта. |

### Объекты тела ответа

#### Объект `DashboardReport`

Конфигурация отчёта по дашборду.

Отчёт по дашборду предоставляет публичную ссылку на связанный дашборд с настраиваемым периодом отчёта: прошлая неделя для еженедельных подписчиков или прошлый месяц для ежемесячных подписчиков.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dashboardId | string | ID связанного дашборда. |
| enabled | boolean | Уведомления по электронной почте для отчёта по дашборду включены (`true`) или выключены (`false`). |
| id | string | ID отчёта. |
| subscriptions | [DashboardReportSubscription](#openapi-definition-DashboardReportSubscription) | Список подписчиков отчёта. |
| type | string | -Возможные значения: * `DASHBOARD` |

#### Объект `DashboardReportSubscription`

Список подписчиков отчёта.

| Элемент | Тип | Описание |
| --- | --- | --- |
| MONTH | string[] | Список ежемесячных подписчиков.  Ежемесячные подписчики получают отчёт в первый понедельник месяца в полночь.  Здесь можно указать адреса электронной почты или ID пользователей Dynatrace. |
| WEEK | string[] | Список еженедельных подписчиков.  Еженедельные подписчики получают отчёт каждый понедельник в полночь.  Здесь можно указать адреса электронной почты или ID пользователей Dynatrace. |

### JSON-модели тела ответа

```
{



"dashboardId": "8dd67562-8bf5-4a09-830d-4e0ca992abd6",



"enabled": "true",



"id": "337d883e-98c3-4dac-b8f2-1a9cdbd05969",



"subscriptions": {



"MONTH": [



"demo@email.com",



"demo2@email.com"



],



"WEEK": [



"demo@email.com"



]



},



"type": "DASHBOARD"



}
```

## Пример

В этом примере запрос запрашивает свойства отчёта с ID **0b2e3121-4f8d-4b08-a879-3047e044ba4c**.

Отчёт содержит данные дашборда с ID **b6570e01-1d49-4bcc-a3bb-2fab2906512c**. Он отправляется еженедельно пользователям Dynatrace **john.smith** и **ryan.white** и ежемесячно пользователю Dynatrace **jane.brown**, а также на адрес электронной почты **marketing.office@organization.com**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/0b2e3121-4f8d-4b08-a879-3047e044ba4c \



-H 'Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/0b2e3121-4f8d-4b08-a879-3047e044ba4c
```

#### Тело ответа

```
{



"id": "0b2e3121-4f8d-4b08-a879-3047e044ba4c",



"type": "DASHBOARD",



"dashboardId": "b6570e01-1d49-4bcc-a3bb-2fab2906512c",



"enabled": true,



"subscriptions": {



"WEEK": [



"john.smith",



"ryan.white"



],



"MONTH": [



"jane.brown",



"marketing.office@organization.com"



]



}



}
```

#### Код ответа

200

## Связанные темы

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Узнайте, как подписаться на отчёты, генерируемые из дашбордов Dynatrace.")