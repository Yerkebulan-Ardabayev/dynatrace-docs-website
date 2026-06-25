---
title: Settings API - HTTP failure detection parameters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-service-http-parameters
scraped: 2026-05-12T11:45:17.410118
---

# Settings API - HTTP failure detection parameters schema table

# Settings API - HTTP failure detection parameters schema table

* Published Dec 05, 2023

### Параметры обнаружения HTTP-сбоев (`builtin:failure-detection.service.http-parameters)`

Dynatrace failure detection автоматически обнаруживает подавляющее большинство ошибок в окружении. Однако обнаруженные ошибки сервиса не обязательно означают, что соответствующие запросы провалились. Бывают случаи, когда параметры обнаружения сбоев сервиса по умолчанию не отвечают конкретным потребностям, в таких случаях можно настроить параметры ниже. Учтите: эти параметры не применяются к сервисам типа 'Span service'. Подробности см. [configure service failure detection](https://dt-url.net/ys5k0p4y).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection.service.http-parameters` | * `group:failure-detection` | `SERVICE` - Service |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.service.http-parameters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection.service.http-parameters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.service.http-parameters` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Переопределять глобальные параметры обнаружения сбоев `enabled` | boolean | - | Required |
| HTTP-коды ответа `httpResponseCodes` | [httpResponseCodes](#httpResponseCodes) | - | Required |
| HTTP 404 (битые ссылки) `brokenLinks` | [brokenLinks](#brokenLinks) | HTTP-коды ответа 404 возвращаются, когда web-сервер не находит определённую страницу. 404 классифицируются как битые ссылки на стороне клиента и поэтому не считаются сбоями сервиса. Включив этот параметр, можно трактовать 404 как сбои сервиса на стороне сервера. | Required |

##### Объект `httpResponseCodes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| HTTP-коды ответа, указывающие на ошибку на стороне сервера `serverSideErrors` | text | - | Required |
| Считать отсутствие HTTP-кода ответа ошибкой сервера `failOnMissingResponseCodeServerSide` | boolean | - | Required |
| HTTP-коды ответа, указывающие на ошибки клиента `clientSideErrors` | text | - | Required |
| Считать отсутствие HTTP-кода ответа ошибкой клиента `failOnMissingResponseCodeClientSide` | boolean | - | Required |

##### Объект `brokenLinks`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Считать HTTP-коды ответа 404 сбоями `http404NotFoundFailures` | boolean | - | Required |
| Правила для битых ссылок на связанные домены `brokenLinkDomains` | set | Если приложение зависит от других хостов на других доменах, добавьте сюда соответствующие доменные имена. После настройки Dynatrace будет считать 404, возвращаемые хостами на этих доменах, сбоями сервиса, связанными с вашим приложением. | Required |