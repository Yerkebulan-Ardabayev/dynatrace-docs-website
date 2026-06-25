---
title: Data privacy API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/data-privacy-api/put-configuration
scraped: 2026-05-12T11:17:38.609425
---

# Data privacy API - PUT configuration

# Data privacy API - PUT configuration

* Reference
* Published Sep 02, 2019

Обновляет глобальную конфигурацию data privacy, влияющую на все ваши приложения.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `DataPrivacy`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [DataPrivacyAndSecurity](#openapi-definition-DataPrivacyAndSecurity) | Глобальная конфигурация data privacy и security. | body | Required |

### Объекты тела запроса

#### Объект `DataPrivacyAndSecurity`

Глобальная конфигурация data privacy и security.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| logAuditEvents | boolean | Audit logging включён (`true`) или выключен (`false`). | Optional |
| maskIpAddressesAndGpsCoordinates | boolean | Маскирование IP-адресов и GPS-координат включено (`true`) или выключено (`false`). | Required |
| maskPersonalDataInUris | boolean | Маскирование персональных данных в URI включено (`true`) или выключено (`false`). | Required |
| maskUserActionNames | boolean | Маскирование имён user actions включено (`true`) или выключено (`false`).  Это маскирование доступно только для web applications. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |

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



"logAuditEvents": true,



"maskIpAddressesAndGpsCoordinates": true,



"maskPersonalDataInUris": true,



"maskUserActionNames": true,



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



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

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `DataPrivacy`.

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

## Пример

В этом примере запрос обновляет конфигурацию data privacy из примера [GET request](/managed/dynatrace-api/configuration-api/data-privacy-api/get-configuration#example "Чтение конфигурации data privacy через Dynatrace API."). Активируются функции **Mask user actions** и **Mask personal data in URLs**.

API-токен передаётся в заголовке **Authorization**.

Можно скачать или скопировать пример тела запроса для своих экспериментов. Сначала обязательно сделайте backup-копию текущей конфигурации через **GET data privacy configuration**.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dataPrivacy \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - смотрите секцию Request body ниже>}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dataPrivacy
```

#### Тело запроса

```
{



"maskIpAddressesAndGpsCoordinates": true,



"maskUserActionNames": true,



"maskPersonalDataInUris": true,



"logAuditEvents": true



}
```

#### Код ответа

204

## Связанные темы

* [Data privacy and security](/managed/manage/data-privacy-and-security "Узнайте, как Dynatrace применяет меры безопасности для защиты приватных данных.")