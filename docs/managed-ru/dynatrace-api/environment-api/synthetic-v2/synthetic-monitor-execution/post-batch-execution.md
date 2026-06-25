---
title: Synthetic monitor executions API v2 - POST пакетное выполнение
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution/post-batch-execution
scraped: 2026-05-12T11:57:51.920653
---

# Synthetic monitor executions API v2 - POST пакетное выполнение

# Synthetic monitor executions API v2 - POST пакетное выполнение

* Справочник
* Опубликовано 27 июня 2022 г.

Запускает пакетное выполнение синтетических мониторов.

Запрос принимает и возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/executions/batch` |
| POST | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/executions/batch` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `syntheticExecutions.write`
* `ExternalSyntheticIntegration`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [SyntheticOnDemandExecutionRequest](#openapi-definition-SyntheticOnDemandExecutionRequest) | JSON-тело запроса. Содержит параметры инициируемого выполнения по требованию. | body | Обязательный |

### Объекты тела запроса

#### Объект `SyntheticOnDemandExecutionRequest`

Содержит параметры для выполнения по требованию мониторов, идентифицированных по тегам, приложениям или сервисам.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| failOnPerformanceIssue | boolean | Если true, выполнение завершится неудачно в случае проблемы с производительностью. | Необязательный |
| failOnSslWarning | boolean | Применяется только к HTTP-мониторам. Если true, выполнение завершится неудачно в случае предупреждения об истечении SSL-сертификата или если сертификат отсутствует. | Необязательный |
| group | [SyntheticOnDemandExecutionRequestGroup](#openapi-definition-SyntheticOnDemandExecutionRequestGroup) | Содержит параметры для выполнения по требованию мониторов, идентифицированных по тегам, приложениям или сервисам. | Необязательный |
| metadata | object | Карта строка-в-строку свойств метаданных для выполнения | Необязательный |
| monitors | [SyntheticOnDemandExecutionRequestMonitor[]](#openapi-definition-SyntheticOnDemandExecutionRequestMonitor) | Список мониторов для инициирования. | Необязательный |
| processingMode | string | Режим обработки выполнения Поле может принимать значения: * `STANDARD` * `DISABLE_PROBLEM_DETECTION` * `EXECUTIONS_DETAILS_ONLY` | Необязательный |
| stopOnProblem | boolean | Если true, выполнения не будут планироваться при возникновении проблемы. | Необязательный |
| takeScreenshotsOnSuccess | boolean | Если true, скриншоты будут делаться во время выполнения браузерного монитора. | Необязательный |

#### Объект `SyntheticOnDemandExecutionRequestGroup`

Содержит параметры для выполнения по требованию мониторов, идентифицированных по тегам, приложениям или сервисам.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| applications | string[] | Список идентификаторов приложений. Выполнятся только мониторы со всеми назначенными приложениями. | Необязательный |
| locations | string[] | Локации, с которых должны выполняться мониторы. | Необязательный |
| services | string[] | Список идентификаторов сервисов. Выполнятся только мониторы со всеми назначенными сервисами. | Необязательный |
| tags | string[] | Список тегов. Выполнятся только мониторы со всеми назначенными тегами. | Необязательный |

#### Объект `SyntheticOnDemandExecutionRequestMonitor`

Содержит мониторы, которые должны быть выполнены по требованию с указанных локаций.

| Поле | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customizedScript | object | Кастомизированные свойства скрипта для этого пакетного выполнения по требованию. | Необязательный |
| executionCount | integer | Количество раз, которое монитор должен быть выполнен на локацию; если не задано, монитор будет выполнен один раз. | Необязательный |
| locations | string[] | Локации, с которых должен выполняться монитор. | Необязательный |
| monitorId | string | Идентификатор монитора. | Обязательный |
| repeatMode | string | Режим повтора выполнения. Если не задан, режим SEQUENTIAL. Поле может принимать значения: * `SEQUENTIAL` * `PARALLEL` | Необязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные поля. Её нужно скорректировать для использования в реальном запросе.

```
{



"failOnPerformanceIssue": false,



"failOnSslWarning": true,



"group": {



"applications": [



"APPLICATION-CD4BEF05FA9DD044"



],



"services": [



"SERVICE-01C6C1282960638B",



"SERVICE-B18840B4E3115C1A"



],



"tags": [



"tag-production",



"another-tag"



]



},



"metadata": {



"key": "value",



"version": "1.255.20221022"



},



"monitors": [



{



"customizedScript": {



"requests": [



{



"sequenceId": "1",



"url": "https://www.somepage.org",



"validation": {



"rules": [



{



"passIfFound": "true",



"type": "httpStatusesList",



"value": "=201"



}



]



}



}



]



},



"executionCount": 3,



"locations": [



"SYNTHETIC_LOCATION-9BB04DAEBA71B8CA",



"SYNTHETIC_LOCATION-ACCA399FAA1194DD"



],



"monitorId": "HTTP_CHECK-6349B98E1CD87352",



"repeatMode": "SEQUENTIAL"



}



],



"processingMode": "EXECUTIONS_DETAILS_ONLY",



"stopOnProblem": true,



"takeScreenshotsOnSuccess": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [SyntheticOnDemandExecutionResult](#openapi-definition-SyntheticOnDemandExecutionResult) | Успех. Детали ответа на выполнение монитора |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Входные данные некорректны. |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Недоступно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SyntheticOnDemandExecutionResult`

Результат выполнения синтетического монитора по требованию.

| Поле | Тип | Описание |
| --- | --- | --- |
| batchId | string | Идентификатор пакета инициированных выполнений. |
| triggered | [SyntheticOnDemandTriggeredMonitor[]](#openapi-definition-SyntheticOnDemandTriggeredMonitor) | Мониторы, для которых были инициированы выполнения по требованию. |
| triggeredCount | integer | Общее количество инициированных выполнений в рамках пакета. |
| triggeringProblemsCount | integer | Общее количество проблем в рамках пакета. |
| triggeringProblemsDetails | [SyntheticOnDemandTriggeringProblemDetails[]](#openapi-definition-SyntheticOnDemandTriggeringProblemDetails) | Список с сущностями, для которых возникли проблемы инициирования. |

#### Объект `SyntheticOnDemandTriggeredMonitor`

Содержит список выполнений монитора по требованию.

| Поле | Тип | Описание |
| --- | --- | --- |
| executions | [SyntheticOnDemandTriggeredExecutionDetails[]](#openapi-definition-SyntheticOnDemandTriggeredExecutionDetails) | Список инициированных выполнений. |
| monitorId | string | Идентификатор монитора. |

#### Объект `SyntheticOnDemandTriggeredExecutionDetails`

Содержит детали инициированного выполнения по требованию.

| Поле | Тип | Описание |
| --- | --- | --- |
| executionId | string | Идентификатор выполнения. |
| locationId | string | Идентификатор локации, с которой должен выполняться монитор. |

#### Объект `SyntheticOnDemandTriggeringProblemDetails`

Содержит детали проблем, возникших при инициировании выполнений по требованию.

| Поле | Тип | Описание |
| --- | --- | --- |
| cause | string | Причина того, что сущность не была инициирована. |
| details | string | Детали проблемы инициирования. |
| entityId | string | Идентификатор сущности. |
| executionId | string | Идентификатор выполнения. |
| locationId | string | Идентификатор локации. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"batchId": "22396514015719218",



"triggered": [



{



"executions": [



{



"executionId": "1069999568093682590",



"locationId": "SYNTHETIC_LOCATION-9BB04DAE11123122"



}



],



"monitorId": "HTTP_CHECK-69A9B98E1CD87352"



}



],



"triggeredCount": 1,



"triggeringProblemsCount": 4,



"triggeringProblemsDetails": [



{



"cause": "Location not found",



"entityId": "HTTP_CHECK-6349B98E1CD87352",



"locationId": "SYNTHETIC_LOCAT-9BB04DAEBA71B8CA"



},



{



"cause": "Monitor not found",



"entityId": "HTTP_CHECK-6349B98E1CD85432"



},



{



"cause": "Incorrect monitor identifier format",



"entityId": "HTTP_HACK-AAAAAAA"



},



{



"cause": "Incorrect application identifier format",



"entityId": "APPLICATION-WRONG"



}



]



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")