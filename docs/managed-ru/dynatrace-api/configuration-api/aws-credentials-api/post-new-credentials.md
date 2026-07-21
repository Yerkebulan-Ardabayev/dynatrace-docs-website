---
title: AWS credentials API - POST new credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/post-new-credentials
---

# AWS credentials API - POST new credentials

# AWS credentials API - POST new credentials

* Справка
* Опубликовано 27 июня 2019

Создаёт новую конфигурацию учётных данных AWS. Статус подключения для этих учётных данных нужно проверять через 10 минут с помощью запроса [GET credentials](/managed/dynatrace-api/configuration-api/aws-credentials-api/get-credentials "View an AWS credentials configuration via the Dynatrace API.").

Тело запроса не должно содержать ID. Сервер Dynatrace назначает ID автоматически.

Запрос принимает и возвращает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать токен, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [AwsCredentialsConfig](#openapi-definition-AwsCredentialsConfig) | Тело JSON запроса. Содержит параметры новой конфигурации учётных данных AWS. | body | Необязательный |

### Объекты тела запроса

#### Объект `AwsCredentialsConfig`

Конфигурация учётных данных AWS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| authenticationData | [AwsAuthenticationData](#openapi-definition-AwsAuthenticationData) | Учётные данные для аутентификации AWS. | Обязательный |
| connectionStatus | string | Статус подключения к окружению AWS.  * `CONNECTED`: подключение устанавливалось в течение последних 10 минут. * `DISCONNECTED`: возникла проблема при установке подключения с использованием этих учётных данных. Нужно проверить корректность данных. * `UNINITIALIZED`: успешное подключение для этих учётных данных никогда не устанавливалось. Элемент может принимать следующие значения * `CONNECTED` * `DISCONNECTED` * `UNINITIALIZED` | Необязательный |
| credentialsEnabled | boolean | Включить мониторинг учётных данных. | Необязательный |
| id | string | Уникальный ID учётных данных. | Необязательный |
| label | string | Имя учётных данных. | Обязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Необязательный |
| partitionType | string | Тип раздела AWS. Элемент может принимать следующие значения * `AWS_CN` * `AWS_DEFAULT` * `AWS_US_GOV` | Обязательный |
| supportingServicesToMonitor | [AwsSupportingServiceConfig](#openapi-definition-AwsSupportingServiceConfig)[] | **Устарело**. Для управления сервисами нужно использовать операцию [/aws/credentials/{id}/services﻿](https://dt-url.net/l022s6v?dt=m). Встроенные сервисы здесь не поддерживаются.  Список сервисов AWS, за которыми ведётся мониторинг. Доступные сервисы перечислены в операции [/aws/supportedServices﻿](https://dt-url.net/me02sh2?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации﻿](https://dt-url.net/r12v0pkl?dt=m).  Список метрик можно пропустить (задать значение null), в этом случае для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. | Необязательный |
| taggedOnly | boolean | Отслеживать только ресурсы с указанными тегами AWS (`true`) или все ресурсы (`false`). | Необязательный |
| tagsToMonitor | [AwsConfigTag](#openapi-definition-AwsConfigTag)[] | Список тегов AWS, за которыми ведётся мониторинг.  Можно указать до 10 тегов.  Применимо только если параметр **taggedOnly** установлен в `true`. | Необязательный |

#### Объект `AwsAuthenticationData`

Учётные данные для аутентификации AWS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| keyBasedAuthentication | [KeyBasedAuthentication](#openapi-definition-KeyBasedAuthentication) | **Устарело**. Учётные данные для аутентификации на основе ключа. | Необязательный |
| roleBasedAuthentication | [RoleBasedAuthentication](#openapi-definition-RoleBasedAuthentication) | Учётные данные для аутентификации на основе роли. | Необязательный |
| type | string | Тип аутентификации: на основе роли или на основе ключа. Элемент может принимать следующие значения * `KEYS` * `ROLE` | Обязательный |

#### Объект `KeyBasedAuthentication`

**Устарело**. Учётные данные для аутентификации на основе ключа.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| accessKey | string | ID ключа доступа. | Обязательный |
| secretKey | string | Секретный ключ доступа. | Обязательный |

#### Объект `RoleBasedAuthentication`

Учётные данные для аутентификации на основе роли.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| accountId | string | ID учётной записи Amazon. | Обязательный |
| externalId | string | Внешний ID-токен для настройки роли IAM.  Его можно получить с помощью запроса `GET /aws/iamExternalId`. | Необязательный |
| iamRole | string | Роль IAM, которую Dynatrace будет использовать для получения данных мониторинга. | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Необязательный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Необязательный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Необязательный |

#### Объект `AwsSupportingServiceConfig`

Сервис, за которым ведётся мониторинг.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric](#openapi-definition-AwsSupportingServiceMetric)[] | Список метрик, за которыми ведётся мониторинг для данного сервиса. Если список равен null, для мониторинга будет использован рекомендуемый список метрик для этого сервиса. | Необязательный |
| name | string | Имя сервиса. Допустимые имена поддерживаемых сервисов можно узнать с помощью restAPI /aws/supportedServices | Обязательный |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса, за которой ведётся мониторинг.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. | Обязательный |
| name | string | Имя метрики сервиса. | Обязательный |
| statistic | string | Статистика (агрегация), используемая для метрики. Значение AVG\_MIN\_MAX означает сразу 3 статистики: AVERAGE, MINIMUM и MAXIMUM Элемент может принимать следующие значения * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` | Обязательный |

#### Объект `AwsConfigTag`

Тег AWS ресурса, за которым ведётся мониторинг.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Ключ тега AWS. | Обязательный |
| value | string | Значение тега AWS. | Обязательный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"authenticationData": {



"keyBasedAuthentication": {



"accessKey": "string",



"secretKey": "string"



},



"roleBasedAuthentication": {



"accountId": "string",



"externalId": "string",



"iamRole": "string"



},



"type": "KEYS"



},



"connectionStatus": "CONNECTED",



"credentialsEnabled": true,



"id": "string",



"label": "string",



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



},



"partitionType": "AWS_CN",



"supportingServicesToMonitor": [



{



"monitoredMetrics": [



{



"dimensions": [



"string"



],



"name": "string",



"statistic": "AVERAGE"



}



],



"name": "string"



}



],



"taggedOnly": false,



"tagsToMonitor": [



{



"name": "string",



"value": "string"



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новая конфигурация учётных данных AWS создана. Тело ответа содержит ID конфигурации.  Статус подключения для этих учётных данных нужно проверять через 10 минут запросом `GET /aws/credentials/{id}`. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введены некорректные данные. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела JSON ответа

```
{



"description": "сущность Dynatrace для примера REST API",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "сущность Dynatrace"



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

## GET внешнего ID токена

Получает внешний ID токен для настройки роли IAM.

Запрос выдаёт полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/iamExternalId` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/iamExternalId` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Чтобы узнать, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsIamToken](#openapi-definition-AwsIamToken) | Успешно |

### Объекты тела ответа

#### Объект `AwsIamToken`

Внешний ID токен для настройки IAM Role в AWS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| token | string | Внешний ID токен для настройки IAM Role в AWS. |

### Модели тела ответа JSON

```
{



"token": "string"



}
```

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой её в составе реального запроса. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Чтобы узнать, как его получить и использовать, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела ответа JSON

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