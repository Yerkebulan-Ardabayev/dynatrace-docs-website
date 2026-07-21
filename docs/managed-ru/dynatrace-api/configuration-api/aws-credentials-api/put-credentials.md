---
title: AWS credentials API - PUT credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/put-credentials
---

# AWS credentials API - PUT credentials

# AWS credentials API - PUT credentials

* Справка
* Опубликовано 27 июня 2019 г.

Обновляет существующую конфигурацию учётных данных AWS. Статус подключения этих учётных данных нужно проверять через 10 минут запросом [GET credentials](/managed/dynatrace-api/configuration-api/aws-credentials-api/get-credentials "View an AWS credentials configuration via the Dynatrace API.").

Если конфигурация учётных данных с указанным ID не существует, создаётся новая конфигурация.

Запрос принимает и возвращает содержимое в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace для Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |

## Авторизация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Токены и авторизация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID конфигурации учётных данных AWS, которую нужно обновить. | path | Обязательный |
| body | [AwsCredentialsConfig](#openapi-definition-AwsCredentialsConfig) | Тело запроса JSON. Содержит обновлённые параметры конфигурации учётных данных AWS. | body | Опциональный |

### Объекты тела запроса

#### Объект `AwsCredentialsConfig`

Конфигурация учётных данных AWS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| authenticationData | [AwsAuthenticationData](#openapi-definition-AwsAuthenticationData) | Учётные данные для аутентификации AWS. | Обязательный |
| connectionStatus | string | Статус подключения к среде AWS.  * `CONNECTED`: подключение было в течение последних 10 минут. * `DISCONNECTED`: возникла проблема с установлением подключения по этим учётным данным. Нужно проверить корректность данных. * `UNINITIALIZED`: успешное подключение с этими учётными данными ни разу не устанавливалось. Элемент может принимать следующие значения * `CONNECTED` * `DISCONNECTED` * `UNINITIALIZED` | Опциональный |
| credentialsEnabled | boolean | Включить мониторинг учётных данных. | Опциональный |
| id | string | Уникальный ID учётных данных. | Опциональный |
| label | string | Имя учётных данных. | Обязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| partitionType | string | Тип раздела AWS. Элемент может принимать следующие значения * `AWS_CN` * `AWS_DEFAULT` * `AWS_US_GOV` | Обязательный |
| supportingServicesToMonitor | [AwsSupportingServiceConfig](#openapi-definition-AwsSupportingServiceConfig)[] | **Устарело**. Для управления сервисами нужно использовать операцию [/aws/credentials/{id}/services﻿](https://dt-url.net/l022s6v?dt=m). Встроенные сервисы здесь не поддерживаются.  Список сервисов AWS, которые нужно отслеживать. Доступные сервисы перечисляются операцией [/aws/supportedServices﻿](https://dt-url.net/me02sh2?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно проверить в [документации﻿](https://dt-url.net/r12v0pkl?dt=m).  Список метрик можно пропустить (установить в null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. | Опциональный |
| taggedOnly | boolean | Отслеживать только ресурсы с указанными тегами AWS (`true`) или все ресурсы (`false`). | Опциональный |
| tagsToMonitor | [AwsConfigTag](#openapi-definition-AwsConfigTag)[] | Список тегов AWS, которые нужно отслеживать.  Можно указать до 10 тегов.  Применимо только если параметр **taggedOnly** установлен в `true`. | Опциональный |

#### Объект `AwsAuthenticationData`

Учётные данные для аутентификации AWS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| keyBasedAuthentication | [KeyBasedAuthentication](#openapi-definition-KeyBasedAuthentication) | **Устарело**. Учётные данные для аутентификации на основе ключей. | Опциональный |
| roleBasedAuthentication | [RoleBasedAuthentication](#openapi-definition-RoleBasedAuthentication) | Учётные данные для аутентификации на основе роли. | Опциональный |
| type | string | Тип аутентификации: на основе роли или на основе ключей. Элемент может принимать следующие значения * `KEYS` * `ROLE` | Обязательный |

#### Объект `KeyBasedAuthentication`

**Устарело**. Учётные данные для аутентификации на основе ключей.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| accessKey | string | ID ключа доступа. | Обязательный |
| secretKey | string | Секретный ключ доступа. | Обязательный |

#### Объект `RoleBasedAuthentication`

Учётные данные для аутентификации на основе роли.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| accountId | string | ID аккаунта Amazon. | Обязательный |
| externalId | string | Внешний ID-токен для настройки IAM-роли.  Его можно получить запросом `GET /aws/iamExternalId`. | Опциональный |
| iamRole | string | IAM-роль, которую Dynatrace использует для получения данных мониторинга. | Обязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

#### Объект `AwsSupportingServiceConfig`

Сервис, который нужно отслеживать.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric](#openapi-definition-AwsSupportingServiceMetric)[] | Список метрик, которые нужно отслеживать для этого сервиса. Если список равен null, для этого сервиса будет отслеживаться рекомендуемый список метрик. | Опциональный |
| name | string | Имя сервиса. Действительные поддерживаемые имена сервисов можно узнать с помощью restAPI /aws/supportedServices | Обязательный |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса, которую нужно отслеживать.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. | Обязательный |
| name | string | Имя метрики сервиса. | Обязательный |
| statistic | string | Статистика (агрегация), которая будет использоваться для метрики. Значение AVG\_MIN\_MAX означает сразу 3 статистики: AVERAGE, MINIMUM и MAXIMUM Элемент может принимать следующие значения * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` | Обязательный |

#### Объект `AwsConfigTag`

Тег AWS ресурса, который нужно отслеживать.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Ключ тега AWS. | Обязательный |
| value | string | Значение тега AWS. | Обязательный |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать перед использованием в реальном запросе.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Создана новая конфигурация учётных данных AWS. Тело ответа содержит ID конфигурации.  Статус подключения этих учётных данных нужно проверять через 10 минут запросом `GET /aws/credentials/{id}`. |
| **204** | - | Успех. Конфигурация учётных данных AWS обновлена. Ответ не содержит тела.  Статус подключения этих учётных данных нужно проверять через 10 минут запросом `GET /aws/credentials/{id}`. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недействительны. |

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

### Модели тела ответа JSON

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## GET внешнего ID-токена

Получает внешний ID-токен для настройки роли IAM.

Запрос выдаёт полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/iamExternalId` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/iamExternalId` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Подробнее о том, как его получить и использовать, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsIamToken](#openapi-definition-AwsIamToken) | Успех |

### Объекты тела ответа

#### Объект `AwsIamToken`

Внешний ID-токен для настройки роли IAM в AWS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| token | string | Внешний ID-токен для настройки роли IAM в AWS. |

### Модели тела ответа JSON

```
{



"token": "string"



}
```

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой её с реальным запросом. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как его получить и использовать, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

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