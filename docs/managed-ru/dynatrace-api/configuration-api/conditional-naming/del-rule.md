---
title: Conditional naming API - DELETE a naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/conditional-naming/del-rule
scraped: 2026-05-12T11:17:21.882545
---

# Conditional naming API - DELETE a naming rule

# Conditional naming API - DELETE a naming rule

* Reference
* Published Apr 23, 2020

Удаляет указанное правило условного именования. Удаление необратимо.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/conditionalNaming/{type}/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| type | string | Тип правила, определяемый типом сущностей Dynatrace, к которым применяется правило. Элемент может принимать значения * `processGroup` * `host` * `service` | path | Required |
| id | string | ID удаляемого правила именования. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Связанные темы

* [Process group naming](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Способы настройки именования process group.")