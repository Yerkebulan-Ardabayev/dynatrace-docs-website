---
title: Request naming API - DELETE a request naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-naming-api/delete-a-rule
scraped: 2026-05-12T11:17:41.146632
---

# Request naming API - DELETE a request naming rule

# Request naming API - DELETE a request naming rule

* Reference
* Published Jun 25, 2019

Удаляет указанное правило именования запросов. Удаление невозможно отменить.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestNaming/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID правила именования запросов, которое нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Успех. Правило удалено. Ответ без тела. |