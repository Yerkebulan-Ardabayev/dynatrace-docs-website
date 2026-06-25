---
title: Extensions API - DELETE an extension instance
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/del-instance
scraped: 2026-05-12T11:19:49.238867
---

# Extensions API - DELETE an extension instance

# Extensions API - DELETE an extension instance

* Reference
* Published Mar 06, 2020

Удаляет указанный экземпляр указанного расширения. Запрос не удаляет бинарный (.zip) файл расширения.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID расширения, в котором вы хотите удалить конфигурацию. | path | Required |
| configurationId | string | ID конфигурации, которую нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")