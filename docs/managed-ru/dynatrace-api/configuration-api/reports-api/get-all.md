---
title: Reports API - GET all reports
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/get-all
scraped: 2026-05-12T11:15:39.595465
---

# Reports API - GET all reports

# Reports API - GET all reports

* Reference
* Published Jan 16, 2020

Выводит список всех доступных отчётов указанного типа.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| type | string | Тип отчёта. Возможные значения: * `DASHBOARD` | query | Optional |
| sourceId | string | Ссылка на исходную сущность отчёта (например, дашборд). | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ReportStubList](#openapi-definition-ReportStubList) | Успех |

### Объекты тела ответа

#### Объект `ReportStubList`

Список кратких представлений отчётов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | [DashboardReportStub[]](#openapi-definition-DashboardReportStub) | Список отчётов. |

#### Объект `DashboardReportStub`

Краткое представление отчёта.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dashboardId | string | ID связанного дашборда. |
| id | string | ID отчёта. |
| type | string | Тип отчёта. Возможные значения: * `DASHBOARD` |

### JSON-модели тела ответа

```
{



"values": [



{



"dashboardId": "9eee7ed6-a125-4d9d-bfa7-afdb3404cb36",



"id": "337d883e-98c3-4dac-b8f2-1a9cdbd05969",



"type": "DASHBOARD"



},



{



"dashboardId": "26ccd360-828c-4d83-a65e-040ddc31e8f6",



"id": "b059e372-0b35-4d44-869b-95c326748848",



"type": "DASHBOARD"



}



]



}
```

## Пример

В этом примере запрос запрашивает список всех конфигураций отчётов в окружении **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до трёх записей.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/ \



-H 'Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/
```

#### Тело ответа

```
{



"values": [



{



"id": "3ad7dece-98a4-4cc4-8805-34dcd19d4714",



"type": "DASHBOARD",



"dashboardId": "18d5b111-05ed-4efb-8cf1-e8dd0a9e5c47"



},



{



"id": "81c86de0-95d6-42d1-ad50-8578bb688b1c",



"type": "DASHBOARD",



"dashboardId": "bf0aad45-3785-444f-88d3-21e547eb78b1"



},



{



"id": "0b2e3121-4f8d-4b08-a879-3047e044ba4c",



"type": "DASHBOARD",



"dashboardId": "b6570e01-1d49-4bcc-a3bb-2fab2906512c"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Узнайте, как подписаться на отчёты, генерируемые из дашбордов Dynatrace.")