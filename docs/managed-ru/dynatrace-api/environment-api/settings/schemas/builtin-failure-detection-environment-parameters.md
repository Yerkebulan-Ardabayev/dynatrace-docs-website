---
title: Settings API - Failure detection parameters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-environment-parameters
scraped: 2026-05-12T11:46:07.390247
---

# Settings API - Failure detection parameters schema table

# Settings API - Failure detection parameters schema table

* Published Dec 05, 2023

### Параметры failure detection (`builtin:failure-detection.environment.parameters)`

Параметры failure detection, определяющие, считается ли вызов сервиса успешным или провалившимся. Используйте failure detection rules (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.rules`), чтобы задать, к каким сервисам применяются эти параметры.

Эти настройки не применяются к [Unified services](https://dt-url.net/gy03cmt).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection.environment.parameters` | * `group:service-monitoring` * `group:failure-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.environment.parameters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection.environment.parameters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.environment.parameters` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя `name` | text | - | Required |
| Описание `description` | text | - | Optional |
| HTTP response codes `httpResponseCodes` | [httpResponseCodes](#httpResponseCodes) | - | Required |
| HTTP 404 (broken links) `brokenLinks` | [brokenLinks](#brokenLinks) | HTTP-коды 404 возвращаются, когда web-сервер не может найти определённую страницу. 404 классифицируются как broken links на стороне клиента и поэтому не считаются service failures. Включив этот параметр, можно трактовать 404 как server-side service failures. | Required |
| Настроить failure detection для конкретных исключений и ошибок `exceptionRules` | [exceptionRules](#exceptionRules) | - | Required |

##### Объект `httpResponseCodes`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| HTTP response codes, означающие ошибку на стороне сервера `serverSideErrors` | text | - | Required |
| Считать отсутствующий HTTP response code ошибкой на стороне сервера `failOnMissingResponseCodeServerSide` | boolean | - | Required |
| HTTP response codes, означающие ошибки на стороне клиента `clientSideErrors` | text | - | Required |
| Считать отсутствующий HTTP response code ошибкой на стороне клиента `failOnMissingResponseCodeClientSide` | boolean | - | Required |

##### Объект `brokenLinks`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Считать HTTP-код 404 отказом `http404NotFoundFailures` | boolean | - | Required |
| Правила для broken links на связанные домены `brokenLinkDomains` | set | Если ваше приложение зависит от других хостов на других доменах, добавьте сюда соответствующие имена доменов. После настройки Dynatrace будет считать 404 от хостов на этих доменах service failures, связанными с вашим приложением. | Required |

##### Объект `exceptionRules`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Игнорировать все исключения `ignoreAllExceptions` | boolean | - | Required |
| Исключения, форсирующие успех `successForcingExceptions` | Set<[exception](#exception)> | Задайте исключения, означающие, что весь вызов сервиса не должен считаться провалившимся. Например, исключение о том, что клиент прервал операцию. Если на **entry node** сервиса возникает исключение, совпадающее с одним из заданных шаблонов, вызов считается успешным. В отличие от ignored exceptions, запрос считается успешным даже при появлении других исключений в этом же запросе. | Required |
| Игнорируемые исключения `ignoredExceptions` | Set<[exception](#exception)> | Некоторые исключения, выбрасываемые legacy- или 3rd-party-кодом, означают конкретный ответ, а не ошибку. Используйте этот параметр, чтобы Dynatrace трактовал такие исключения как непровалившиеся запросы. Если на **entry node** сервиса возникает исключение, совпадающее с одним из заданных шаблонов, оно не считается failure. Прочие исключения в этом же запросе всё равно могут пометить запрос как провалившийся. | Required |
| Пользовательские обработанные исключения `customHandledExceptions` | Set<[exception](#exception)> | Возможны ситуации, когда код вашего приложения корректно обрабатывает исключения так, что Dynatrace не обнаруживает эти отказы. Используйте этот параметр, чтобы задать конкретные gracefully-обрабатываемые исключения, которые должны трактоваться как service failures. | Required |
| Пользовательские правила ошибок `customErrorRules` | Set<[customErrorRule](#customErrorRule)> | Некоторые пользовательские ошибочные ситуации можно обнаружить только через возвращаемое значение или иными способами. Для таких случаев [задайте request attribute](https://dt-url.net/ys5k0p4y), захватывающий нужные данные. Затем задайте custom error rule, определяющее по значению request attribute, провалился ли запрос. | Required |
| Игнорировать span failure detection `ignoreSpanFailureDetection` | boolean | - | Required |

##### Объект `exception`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Шаблон класса `classPattern` | text | Шаблон совпадает, если он содержится в фактическом имени класса. | Optional |
| Шаблон сообщения исключения `messagePattern` | text | При желании задайте шаблон сообщения исключения. Шаблон совпадает, если фактическое сообщение исключения содержит шаблон. | Optional |

##### Объект `customErrorRule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Request attribute `requestAttribute` | text | - | Required |
| Условие request attribute `condition` | [compareOperation](#compareOperation) | - | Required |

##### Объект `compareOperation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Применять это сравнение `compareOperationType` | text | - | Required |
| Значение `textValue` | text | - | Required |
| Чувствительно к регистру `caseSensitive` | boolean | - | Required |
| Значение `intValue` | integer | - | Required |
| Значение `doubleValue` | float | - | Required |