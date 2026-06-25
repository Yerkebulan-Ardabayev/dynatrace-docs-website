---
title: Settings API - General failure detection parameters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-failure-detection-service-general-parameters
scraped: 2026-05-12T11:40:24.292429
---

# Settings API - General failure detection parameters schema table

# Settings API - General failure detection parameters schema table

* Published Dec 05, 2023

### Общие параметры failure detection (`builtin:failure-detection.service.general-parameters)`

Dynatrace failure detection автоматически обнаруживает подавляющее большинство ошибочных состояний в вашем окружении. Однако обнаруженные ошибки сервиса не обязательно означают, что нижележащие запросы провалились. Бывают случаи, когда настройки failure detection по умолчанию не подходят под ваши потребности. В таких случаях можно настроить приведённые ниже параметры. Учтите, что эти настройки не применимы к сервисам типа 'Span service'. Подробнее см. [configure service failure detection](https://dt-url.net/ys5k0p4y).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:failure-detection.service.general-parameters` | * `group:failure-detection` | `SERVICE` - Service |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.service.general-parameters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:failure-detection.service.general-parameters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:failure-detection.service.general-parameters` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Переопределить глобальные параметры failure detection `enabled` | boolean | - | Required |
| Настроить failure detection для конкретных исключений и ошибок `exceptionRules` | [exceptionRules](#exceptionRules) | - | Required |

##### Объект `exceptionRules`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Игнорировать все исключения `ignoreAllExceptions` | boolean | - | Required |
| Исключения, форсирующие успех `successForcingExceptions` | Set<[exception](#exception)> | Задайте исключения, означающие, что весь вызов сервиса не должен считаться провалившимся. Например, исключение о том, что клиент прервал операцию. Если на **entry node** сервиса возникает исключение, соответствующее любому из заданных шаблонов, вызов считается успешным. В отличие от игнорируемых исключений, запрос будет считаться успешным даже при других исключениях в том же запросе. | Required |
| Игнорируемые исключения `ignoredExceptions` | Set<[exception](#exception)> | Некоторые исключения, бросаемые legacy- или сторонним кодом, означают конкретный ответ, а не ошибку. Используйте этот параметр, чтобы Dynatrace трактовал такие исключения как непровалившиеся запросы. Если на **entry node** сервиса возникает исключение, соответствующее любому из заданных шаблонов, оно не считается failure. Другие исключения в том же запросе по-прежнему могут пометить запрос как провалившийся. | Required |
| Пользовательские обработанные исключения `customHandledExceptions` | Set<[exception](#exception)> | Бывают ситуации, когда код приложения корректно обрабатывает исключения так, что эти failures не обнаруживаются Dynatrace. Используйте этот параметр, чтобы задать конкретные изящно обработанные исключения, которые должны считаться отказами сервиса. | Required |
| Пользовательские правила ошибок `customErrorRules` | Set<[customErrorRule](#customErrorRule)> | Некоторые пользовательские ошибочные ситуации обнаруживаются только по возвращаемому значению или иным способом. Для таких случаев [задайте request attribute](https://dt-url.net/ys5k0p4y), захватывающий нужные данные. Затем задайте custom error rule, которое по значению request attribute определяет, провалился запрос или нет. | Required |
| Игнорировать span failure detection `ignoreSpanFailureDetection` | boolean | - | Required |

##### Объект `exception`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Шаблон класса `classPattern` | text | Шаблон совпадает, если он содержится внутри фактического имени класса. | Optional |
| Шаблон сообщения исключения `messagePattern` | text | По желанию задайте шаблон сообщения исключения. Шаблон совпадает, если фактическое сообщение исключения содержит этот шаблон. | Optional |

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