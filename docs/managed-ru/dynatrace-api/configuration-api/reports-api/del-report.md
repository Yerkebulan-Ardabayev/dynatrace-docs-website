---
title: Reports API - DELETE a report
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/del-report
scraped: 2026-05-12T11:15:43.870402
---

# Reports API - DELETE a report

# Reports API - DELETE a report

* Reference
* Published Jan 16, 2020

Удаляет указанный отчёт. Удаление нельзя отменить!

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемого отчёта. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Отчёт удалён. Ответ без тела. |

## Пример

В этом примере запрос удаляет отчёт из примера [POST request](/managed/dynatrace-api/configuration-api/reports-api/post-report#example "Создание конфигурации отчёта через Dynatrace API."). Код ответа **204** означает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73 \



-H 'Authorization: Api-token abcdefghij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73
```

#### Код ответа

204

## Связанные темы

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Узнайте, как подписаться на отчёты, генерируемые из дашбордов Dynatrace.")