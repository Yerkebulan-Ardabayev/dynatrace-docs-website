---
title: Hub capabilities API - POST расширения 2.0 в окружение
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/post-extension-20-to-evironment
scraped: 2026-05-12T11:54:55.190531
---

# Hub capabilities API - POST расширения 2.0 в окружение

# Hub capabilities API - POST расширения 2.0 в окружение

* Reference
* Published Feb 07, 2023

Регистрирует расширение 2.0 в вашем окружении. Если версия не указана, используется рекомендованная версия.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/actions/addToEnvironment` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/actions/addToEnvironment` |

## Аутентификация

Для выполнения запроса необходим access token со scope `hub.install`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| extensionName | string | Полное имя (FQN) расширения | path | Обязательный |
| extensionVersion | string | Версия расширения. Откат к вычисленной рекомендованной версии, если версия не указана | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [RegisteredExtensionResultDto](#openapi-definition-RegisteredExtensionResultDto) | OK |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Некорректный запрос |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не найдено |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Недоступно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `RegisteredExtensionResultDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| extensionName | string | FQN расширения, зарегистрированного в тенанте. |
| extensionVersion | string | Номер версии расширения. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"extensionName": "string",



"extensionVersion": "string"



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