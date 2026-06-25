---
title: Hub capabilities API - PUT release notes расширения 2.0
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/hub/put-extension-20-release-notes
scraped: 2026-05-12T11:54:57.120943
---

# Hub capabilities API - PUT release notes расширения 2.0

# Hub capabilities API - PUT release notes расширения 2.0

* Reference
* Published Feb 07, 2023

Устанавливает release notes для релиза расширения 2.0. Любые ранее существовавшие заметки перезаписываются.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/releases/{version}/releaseNotes` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/hub/extensions2/{extensionName}/releases/{version}/releaseNotes` |

## Аутентификация

Для выполнения запроса необходим access token со scope `hub.write`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| extensionName | string | Полное имя (FQN) расширения | path | Обязательный |
| version | string | Версия релиза расширения | path | Обязательный |
| body | [ExtensionReleaseNotes](#openapi-definition-ExtensionReleaseNotes) | JSON-тело запроса. Содержит markdown для release notes | body | Опциональный |

### Объекты тела запроса

#### Объект `ExtensionReleaseNotes`

| Элемент | Тип | Описание | Обязательность |
| --- | --- | --- | --- |
| markdown | string | Release notes в формате markdown | Опциональный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её необходимо адаптировать для использования в реальном запросе.

```
{



"markdown": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Release notes расширения обновлены |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Некорректный запрос |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не найдено |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Недоступно |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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