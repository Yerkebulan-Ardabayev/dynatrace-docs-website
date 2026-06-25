---
title: Deployment API - View ActiveGate endpoints for OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-activegate-endpoints
scraped: 2026-05-12T11:58:15.850316
---

# Deployment API - View ActiveGate endpoints for OneAgent

# Deployment API - View ActiveGate endpoints for OneAgent

* Справочник
* Опубликовано 03 июня 2020 г.

Возвращает упорядоченный список endpoints ActiveGate, которые будут использоваться OneAgent в указанной сетевой зоне. Если сетевая зона не указана, перечисляются endpoints зоны **default**.

Запрос возвращает payload `text/plain`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/connectioninfo/endpoints` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/connectioninfo/endpoints` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| networkZone | string | - | query | Необязательный |
| defaultZoneFallback | boolean | Установите `true`, чтобы выполнить откат к сетевой зоне по умолчанию, если указанная сетевая зона не существует. | query | Необязательный |

## Ответ

Ответ это payload в виде обычного текста, где ActiveGate разделены точкой с запятой, endpoints с более высоким приоритетом идут первыми.