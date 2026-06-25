---
title: Deployment API - Download BOSH tarballs of specific version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/bosh/download-bosh-version
scraped: 2026-05-12T11:55:21.380072
---

# Deployment API - Download BOSH tarballs of specific version

# Deployment API - Download BOSH tarballs of specific version

* Справочник
* Опубликовано 28 августа 2019 г.

Скачивает тарболлы BOSH release указанной версии, OneAgent включён. Список доступных версий можно получить вызовом [GET available versions of BOSH tarballs](/managed/dynatrace-api/environment-api/deployment/bosh/get-available-version "Список доступных версий тарболлов OneAgent BOSH через Dynatrace API.").

Для SaaS вызов выполняется на Environment ActiveGate. Обязательно используйте базовый адрес ActiveGate, **не** окружения.

|  |  |
| --- | --- |
| GET | * Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/deployment/boshrelease/agent/{osType}/version/{version} * Dynatrace SaaS https://{your-environment-activegate}:9999/e/{your-environment-id}/api/v1/deployment/boshrelease/agent/{osType}/version/{version} |

## Аутентификация

Для выполнения запроса нужен **PaaS token** (`InstallerDownload`) вашего окружения. О том, как получить и использовать его, смотрите [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции access-токена и его scope.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| osType | string | Операционная система инсталлятора. Поле может принимать значения: * `windows` * `unix` | path | Обязательный |
| version | string | Требуемая версия OneAgent в формате `1.155.275.20181112-084458`.  Список доступных версий можно получить вызовом [**GET available versions of BOSH tarballs**](https://dt-url.net/j703kdn). | path | Обязательный |
| skipMetadata | boolean | Установите `true`, чтобы исключить сведения о подключении OneAgent из инсталлятора.  Если не задано, используется `false`. | query | Необязательный |
| networkZone | string | Сетевая зона, с которой должен быть сконфигурирован результат. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | string | Успех. Payload содержит файл тарболла BOSH release. |
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