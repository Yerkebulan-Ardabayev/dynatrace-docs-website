---
title: Service detection API - DELETE a full web request rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/del-a-rule
scraped: 2026-05-12T11:18:50.829672
---

# Service detection API - DELETE a full web request rule

# Service detection API - DELETE a full web request rule

* Reference
* Published Sep 06, 2019

Удаляет указанное правило обнаружения сервисов для полных веб-запросов.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_REQUEST/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/detectionRules/FULL_WEB_REQUEST/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID правила обнаружения сервисов, которое нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |
| **404** | Сбой. Правило с указанным ID не существует. |

## Связанные темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.")