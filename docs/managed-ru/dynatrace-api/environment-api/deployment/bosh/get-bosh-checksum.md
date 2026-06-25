---
title: Deployment API - GET checksum of a BOSH tarball
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/bosh/get-bosh-checksum
scraped: 2026-05-12T11:55:23.339946
---

# Deployment API - GET checksum of a BOSH tarball

# Deployment API - GET checksum of a BOSH tarball

* Справочник
* Опубликовано 28 августа 2019 г.

Получает контрольную сумму указанного тарболла BOSH release. Контрольная сумма это SHA-256 хеш файла инсталлятора.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/boshrelease/agent/{osType}/version/{version}/checksum` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/boshrelease/agent/{osType}/version/{version}/checksum` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

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
| **200** | [BoshReleaseChecksum](#openapi-definition-BoshReleaseChecksum) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `BoshReleaseChecksum`

Контрольная сумма тарболла BOSH release.

| Поле | Тип | Описание |
| --- | --- | --- |
| sha256 | string | Контрольная сумма тарболла BOSH release.  Это sha256 хеш файла инсталлятора. |

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



"sha256": "string"



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