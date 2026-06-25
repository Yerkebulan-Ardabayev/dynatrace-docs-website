---
title: Extensions 2.0 API - PUT конфигурацию окружения
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/environment-configurations/put-environment-configuration
scraped: 2026-05-12T11:56:28.995158
---

# Extensions 2.0 API - PUT конфигурацию окружения

# Extensions 2.0 API - PUT конфигурацию окружения

* Справочник
* Опубликовано 22 января 2021 г.

Активирует указанную версию Extensions 2.0 extension.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/environmentConfiguration` |
| PUT | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/environmentConfiguration` |

## Аутентификация

Для выполнения запроса нужен access-токен с одним из следующих scope:

* `extensionEnvironment.write`
* `extensions.write`

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| extensionName | string | Имя требуемого extension 2.0. | path | Обязательный |
| body | [ExtensionEnvironmentConfigurationVersion](#openapi-definition-ExtensionEnvironmentConfigurationVersion) | Версия требуемой конфигурации окружения. | body | Обязательный |

### Объекты тела запроса

#### Объект `ExtensionEnvironmentConfigurationVersion`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| version | string | Версия extension | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"version": "1.2.3"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionEnvironmentConfigurationVersion](#openapi-definition-ExtensionEnvironmentConfigurationVersion) | Успех. Конфигурация окружения обновлена. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ExtensionEnvironmentConfigurationVersion`

| Элемент | Тип | Описание |
| --- | --- | --- |
| version | string | Версия extension |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
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



"version": "1.2.3"



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

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")