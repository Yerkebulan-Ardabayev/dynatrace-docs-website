---
title: Extensions API - GET extension .zip file
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-extension-file
scraped: 2026-05-12T11:20:03.285625
---

# Extensions API - GET extension .zip file

# Extensions API - GET extension .zip file

* Reference
* Published Mar 06, 2020

Скачивает бинарный (.zip) файл указанного расширения.

Запрос возвращает payload `application/octet-stream`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/binary` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/binary` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID расширения, которое вы хотите скачать. | path | Required |

## Ответ

Успешный запрос скачивает .zip-файл требуемого расширения.

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")