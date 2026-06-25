---
title: Deployment API - Скачать ActiveGate конкретной версии
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-version
scraped: 2026-05-12T11:56:44.310299
---

# Deployment API - Скачать ActiveGate конкретной версии

# Deployment API - Скачать ActiveGate конкретной версии

* Справочник
* Опубликовано 28 августа 2019 г.

Скачивает инсталлятор ActiveGate указанной версии. Список доступных версий ActiveGate можно получить вызовом [GET available versions of ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-versions "Список доступных версий ActiveGate через Dynatrace API.").

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/{osType}/version/{version}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/{osType}/version/{version}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| If-None-Match | string | ETag предыдущего запроса. Не скачивайте, если он совпадает с ETag инсталлятора. | header | Необязательный |
| osType | string | Операционная система инсталлятора. Поле может принимать значения: * `windows` * `unix` | path | Обязательный |
| version | string | Требуемая версия инсталлятора ActiveGate в формате `1.155.275.20181112-084458`.  Список доступных версий можно получить вызовом [**GET available versions of ActiveGate**](https://dt-url.net/kh43rha). | path | Обязательный |
| networkZone | string | Сетевая зона, с которой должен быть сконфигурирован результат. Указанная сетевая зона должна существовать, иначе запрос завершится ошибкой. Требуется ActiveGate версии не ниже 1.247. | query | Необязательный |
| arch | string | Архитектура вашей ОС:  * `all`: по умолчанию `amd64`. * `amd64`: архитектура amd64. * `s390`: архитектура S/390, поддерживается только для Linux. * `arm64`: архитектура arm64, поддерживается только для Linux. Поле может принимать значения: * `all` * `amd64` * `arm64` * `s390` | query | Необязательный |

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