---
title: Deployment API - Просмотр последней версии OneAgent для AWS Lambda Classic
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-latest-version-lambda-classic
scraped: 2026-03-06T21:28:44.533912
---

Этот API предназначен для использования с реализацией AWS Lambda Classic. Подробности см. в разделе [AWS Lambda](../../../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration.md "AWS Lambda capabilities and integration options").

Получает названия последних версий кодовых модулей OneAgent для сред выполнения AWS Lambda Java, Node.js и Python, включая названия слоёв в комбинации с коллектором логов, а также названия автономного слоя коллектора логов.

Запрос возвращает полезную нагрузку типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/lambda/agent/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/lambda/agent/latest` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `InstallerDownload`.

Чтобы узнать, как получить и использовать его, см. [Tokens and authentication](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [LatestLambdaLayerNames](#openapi-definition-LatestLambdaLayerNames) | Успешно. Полезная нагрузка содержит доступные версии. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `LatestLambdaLayerNames`

Названия последних доступных версий OneAgent lambda

| Элемент | Тип | Описание |
| --- | --- | --- |
| collector | string | - |
| java | string | - |
| java\_with\_collector | string | - |
| nodejs | string | - |
| nodejs\_with\_collector | string | - |
| python | string | - |
| python\_with\_collector | string | - |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{


"collector": "string",


"java": "string",


"java_with_collector": "string",


"nodejs": "string",


"nodejs_with_collector": "string",


"python": "string",


"python_with_collector": "string"


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
