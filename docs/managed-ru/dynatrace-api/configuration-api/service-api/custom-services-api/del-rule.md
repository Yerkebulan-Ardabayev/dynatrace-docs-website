---
title: Custom services API - DELETE a custom service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/custom-services-api/del-rule
scraped: 2026-05-12T11:18:05.455528
---

# Custom services API - DELETE a custom service rule

# Custom services API - DELETE a custom service rule

* Reference
* Published Sep 02, 2019

Удаляет указанное правило пользовательского сервиса.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| technology | string | Технология пользовательского сервиса, который нужно удалить. Возможные значения: * `dotNet` * `go` * `java` * `nodeJS` * `php` | path | Required |
| id | string | ID пользовательского сервиса, который нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Связанные темы

* [Define custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Определите точки входа (метод, класс или интерфейс) для пользовательских сервисов, не использующих стандартные протоколы.")