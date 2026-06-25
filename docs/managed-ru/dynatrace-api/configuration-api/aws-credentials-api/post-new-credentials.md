---
title: AWS credentials API - POST new credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/post-new-credentials
scraped: 2026-05-12T11:15:08.851216
---

# AWS credentials API - POST new credentials

# AWS credentials API - POST new credentials

* Reference
* Published Jun 27, 2019

Создаёт новую конфигурацию AWS credentials. Проверьте статус подключения для этих credentials через 10 минут запросом [GET credentials](/managed/dynatrace-api/configuration-api/aws-credentials-api/get-credentials "Просмотр конфигурации AWS credentials через Dynatrace API.").

В теле не должно быть ID. Dynatrace Server назначает ID автоматически.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [AwsCredentialsConfig](#openapi-definition-AwsCredentialsConfig) | JSON-тело запроса. Содержит параметры новой конфигурации AWS credentials. | body | Optional |

### Объекты тела запроса

#### Объект `AwsCredentialsConfig`

Конфигурация AWS credentials.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| authenticationData | [AwsAuthenticationData](#openapi-definition-AwsAuthenticationData) | Credentials для AWS-аутентификации. | Required |
| connectionStatus | string | Статус подключения к AWS-окружению.  * `CONNECTED`: было подключение в течение последних 10 минут. * `DISCONNECTED`: возникла проблема при установке подключения с этими credentials. Проверьте корректность данных. * `UNINITIALIZED`: успешное подключение для этих credentials никогда не устанавливалось. Возможные значения: * `CONNECTED` * `DISCONNECTED` * `UNINITIALIZED` | Optional |
| credentialsEnabled | boolean | Включить мониторинг credentials. | Optional |
| id | string | Уникальный ID credentials. | Optional |
| label | string | Имя credentials. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| partitionType | string | Тип AWS-partition. Возможные значения: * `AWS_CN` * `AWS_DEFAULT` * `AWS_US_GOV` | Required |
| supportingServicesToMonitor | [AwsSupportingServiceConfig[]](#openapi-definition-AwsSupportingServiceConfig) | **Устарело**. Для управления сервисами используйте операцию [/aws/credentials/{id}/services](https://dt-url.net/l022s6v). Встроенные сервисы здесь не поддерживаются.  Список AWS-сервисов для мониторинга. Доступные сервисы перечислены операцией [/aws/supportedServices](https://dt-url.net/me02sh2).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации](https://dt-url.net/r12v0pkl).  Список метрик можно пропустить (задать null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. | Optional |
| taggedOnly | boolean | Мониторить только ресурсы с указанными AWS-тегами (`true`) или все ресурсы (`false`). | Optional |
| tagsToMonitor | [AwsConfigTag[]](#openapi-definition-AwsConfigTag) | Список AWS-тегов для мониторинга.  Можно указать до 10 тегов.  Применяется только когда параметр **taggedOnly** установлен в `true`. | Optional |

#### Объект `AwsAuthenticationData`

Credentials для AWS-аутентификации.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| keyBasedAuthentication | [KeyBasedAuthentication](#openapi-definition-KeyBasedAuthentication) | **Устарело**. Credentials для аутентификации по ключу. | Optional |
| roleBasedAuthentication | [RoleBasedAuthentication](#openapi-definition-RoleBasedAuthentication) | Credentials для аутентификации по роли. | Optional |
| type | string | Тип аутентификации: по роли или по ключу. Возможные значения: * `KEYS` * `ROLE` | Required |

#### Объект `KeyBasedAuthentication`

**Устарело**. Credentials для аутентификации по ключу.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| accessKey | string | ID access key. | Required |
| secretKey | string | Secret access key. | Required |

#### Объект `RoleBasedAuthentication`

Credentials для аутентификации по роли.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| accountId | string | ID аккаунта Amazon. | Required |
| externalId | string | Токен external ID для настройки IAM-роли.  Его можно получить запросом `GET /aws/iamExternalId`. | Optional |
| iamRole | string | IAM-роль, используемая Dynatrace для получения данных мониторинга. | Required |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `AwsSupportingServiceConfig`

Сервис для мониторинга.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric[]](#openapi-definition-AwsSupportingServiceMetric) | Список метрик для мониторинга этого сервиса. Если список null, мониторится рекомендуемый список метрик для этого сервиса. | Optional |
| name | string | Имя сервиса. Допустимые имена поддерживаемых сервисов можно узнать через restAPI /aws/supportedServices | Required |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса для мониторинга.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. | Required |
| name | string | Имя метрики сервиса. | Required |
| statistic | string | Статистика (агрегация), используемая для метрики. Значение AVG\_MIN\_MAX это 3 статистики сразу: AVERAGE, MINIMUM и MAXIMUM Возможные значения: * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` | Required |

#### Объект `AwsConfigTag`

AWS-тег ресурса для мониторинга.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| name | string | Ключ AWS-тега. | Required |
| value | string | Значение AWS-тега. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новая конфигурация AWS credentials создана. Тело ответа содержит ID конфигурации.  Проверьте статус подключения для этих credentials через 10 минут запросом `GET /aws/credentials/{id}`. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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

## Получение токена external ID

Возвращает токен external ID для настройки IAM-роли.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/iamExternalId` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/iamExternalId` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsIamToken](#openapi-definition-AwsIamToken) | Успех |

### Объекты тела ответа

#### Объект `AwsIamToken`

Токен external ID для настройки IAM-роли в AWS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| token | string | Токен external ID для настройки IAM-роли в AWS. |

### JSON-модели тела ответа

```
{



"token": "string"



}
```

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
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