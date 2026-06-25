---
title: Allowed beacon domains API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors/put-configuration
scraped: 2026-05-12T11:19:46.665462
---

# Allowed beacon domains API - PUT configuration

# Allowed beacon domains API - PUT configuration

* Reference
* Published Sep 23, 2020

Обновляет конфигурацию разрешённых beacon origins для запросов Cross Origin Resource Sharing (CORS).

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/allowedBeaconOriginsForCors` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/allowedBeaconOriginsForCors` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [AllowedBeaconOrigins](#openapi-definition-AllowedBeaconOrigins) | JSON-тело запроса. Содержит конфигурацию разрешённых beacon origins для запросов CORS. | body | Optional |

### Объекты тела запроса

#### Объект `AllowedBeaconOrigins`

Конфигурация разрешённых beacon origins для запросов CORS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| allowedBeaconOrigins | [BeaconDomainPattern[]](#openapi-definition-BeaconDomainPattern) | Список разрешённых beacon origins для запросов CORS. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| rejectBeaconsWithoutOriginHeader | boolean | Отбрасывать (`true`) или сохранять (`false`) beacon'ы без HTTP-заголовка **Origin** на BeaconForwarder.  Если не задано, используется `false`. | Optional |

#### Объект `BeaconDomainPattern`

Разрешённый beacon origin для запросов CORS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| domainNameMatcher | string | Операция сопоставления для **domainNamePattern**. Возможные значения: * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Required |
| domainNamePattern | string | Шаблон разрешённого доменного имени. | Required |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"allowedBeaconOrigins": [



{



"domainNameMatcher": "EQUALS",



"domainNamePattern": "dynatrace.com"



}



],



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

### Объекты тела ответа

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Validate payload

Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/allowedBeaconOriginsForCors/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/allowedBeaconOriginsForCors/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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