---
title: Request attributes API - DELETE a request attribute
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-attributes-api/del-request-attribute
scraped: 2026-05-12T11:20:37.572797
---

# Request attributes API - DELETE a request attribute

# Request attributes API - DELETE a request attribute

* Reference
* Published Sep 03, 2019

Удаляет указанный атрибут запроса.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/requestAttributes/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `CaptureRequestData`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID атрибута запроса, который нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Связанные темы

* [Атрибуты запросов](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов, и как использовать их на всех уровнях всех представлений анализа сервисов.")