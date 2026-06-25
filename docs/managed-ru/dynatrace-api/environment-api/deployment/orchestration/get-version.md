---
title: Deployment API - Download an orchestration tarball
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/orchestration/get-version
scraped: 2026-05-12T11:58:12.153920
---

# Deployment API - Download an orchestration tarball

# Deployment API - Download an orchestration tarball

* Справочник
* Опубликовано 29 июня 2021 г.

Скачивает конкретную версию orchestration-тарболла развёртывания OneAgent.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/orchestration/agent/{orchestrationType}/version/{version}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/orchestration/agent/{orchestrationType}/version/{version}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| orchestrationType | string | Orchestration Type скрипта развёртывания orchestration. Поле может принимать значения: * `ansible` * `puppet` | path | Обязательный |
| version | string | Запрошенная версия orchestration-тарболла развёртывания OneAgent в формате `0.1.0.20200925-120822`. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | string | Успех. Payload содержит файл инсталлятора. |
| **304** | - | Не изменено. У вас уже есть последняя версия инсталлятора. Ответ не содержит payload. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

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