---
title: Deployment API - View the latest OneAgent version for AWS Lambda Classic
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-latest-version-lambda-classic
scraped: 2026-05-12T11:58:29.735240
---

# Deployment API - View the latest OneAgent version for AWS Lambda Classic

# Deployment API - View the latest OneAgent version for AWS Lambda Classic

* Справочник
* Обновлено 20 августа 2025 г.

Этот API предназначен для использования с реализацией AWS Lambda Classic. Подробности смотрите в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности AWS Lambda и варианты интеграции").

Возвращает имена последних версий code modules OneAgent для сред выполнения AWS Lambda Java, Node.js и Python, включая также имена слоёв, объединённых с log collector, а также имя отдельного слоя log collector.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/lambda/agent/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/lambda/agent/latest` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [LatestLambdaLayerNames](#openapi-definition-LatestLambdaLayerNames) | Успех. Payload содержит доступные версии. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `LatestLambdaLayerNames`

Доступные имена последних версий lambda OneAgent

| Поле | Тип | Описание |
| --- | --- | --- |
| collector | string | - |
| java | string | - |
| java\_with\_collector | string | - |
| nodejs | string | - |
| nodejs\_with\_collector | string | - |
| python | string | - |
| python\_with\_collector | string | - |

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