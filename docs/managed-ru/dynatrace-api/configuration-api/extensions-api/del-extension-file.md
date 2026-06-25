---
title: Extensions API - DELETE extension .zip file
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/del-extension-file
scraped: 2026-05-12T11:19:50.410764
---

# Extensions API - DELETE extension .zip file

# Extensions API - DELETE extension .zip file

* Reference
* Published Mar 06, 2020

Удаляет .zip-файл указанного расширения из Dynatrace.

Удаление файла расширения деинсталлирует расширение, делая его недоступным для использования.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID расширения, которое нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")