---
title: Deployment API - GET available versions of BOSH tarballs
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/bosh/get-available-version
scraped: 2026-05-12T11:55:19.477283
---

# Deployment API - GET available versions of BOSH tarballs

# Deployment API - GET available versions of BOSH tarballs

* Справочник
* Опубликовано 28 августа 2019 г.

Получает список доступных версий OneAgent для тарболлов BOSH release.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/boshrelease/versions/{osType}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/boshrelease/versions/{osType}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| osType | string | Операционная система инсталлятора. Поле может принимать значения: * `windows` * `unix` | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [BoshReleaseAvailableVersions](#openapi-definition-BoshReleaseAvailableVersions) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `BoshReleaseAvailableVersions`

Список доступных версий OneAgent для тарболлов BOSH release.

| Поле | Тип | Описание |
| --- | --- | --- |
| availableVersions | string[] | Список доступных версий OneAgent для тарболлов BOSH release. |

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



"availableVersions": [



"string"



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