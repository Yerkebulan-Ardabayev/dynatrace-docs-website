---
title: Plugins API - GET plugin ZIP file
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-plugin-binary
scraped: 2026-05-12T11:21:05.640364
---

# Plugins API - GET plugin ZIP file

# Plugins API - GET plugin ZIP file

* Reference
* Published Jun 07, 2019

Скачивает ZIP-файл указанного плагина.

Запрос возвращает payload `application/octet-stream`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/binary` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/binary` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID плагина, который вы хотите скачать. | path | Required |

## Ответ

Успешный запрос скачивает ZIP-файл требуемого плагина.