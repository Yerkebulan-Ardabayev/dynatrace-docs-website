---
title: AWS credentials API - GET credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/get-credentials
scraped: 2026-05-12T11:15:11.908751
---

# AWS credentials API - GET credentials

# AWS credentials API - GET credentials

* Reference
* Published Jun 27, 2019

Возвращает конфигурацию указанных AWS credentials.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID указанной конфигурации AWS credentials. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsCredentialsConfig](#openapi-definition-AwsCredentialsConfig) | Успех |

### Объекты тела ответа

#### Объект `AwsCredentialsConfig`

Конфигурация AWS credentials.

| Элемент | Тип | Описание |
| --- | --- | --- |
| authenticationData | [AwsAuthenticationData](#openapi-definition-AwsAuthenticationData) | Credentials для AWS-аутентификации. |
| connectionStatus | string | Статус подключения к AWS-окружению.  * `CONNECTED`: было подключение в течение последних 10 минут. * `DISCONNECTED`: возникла проблема при установке подключения с этими credentials. Проверьте корректность данных. * `UNINITIALIZED`: успешное подключение для этих credentials никогда не устанавливалось. Возможные значения: * `CONNECTED` * `DISCONNECTED` * `UNINITIALIZED` |
| credentialsEnabled | boolean | Включить мониторинг credentials. |
| id | string | Уникальный ID credentials. |
| label | string | Имя credentials. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| partitionType | string | Тип AWS-partition. Возможные значения: * `AWS_CN` * `AWS_DEFAULT` * `AWS_US_GOV` |
| supportingServicesToMonitor | [AwsSupportingServiceConfig[]](#openapi-definition-AwsSupportingServiceConfig) | **Устарело**. Для управления сервисами используйте операцию [/aws/credentials/{id}/services](https://dt-url.net/l022s6v). Встроенные сервисы здесь не поддерживаются.  Список AWS-сервисов для мониторинга. Доступные сервисы перечислены операцией [/aws/supportedServices](https://dt-url.net/me02sh2).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации](https://dt-url.net/r12v0pkl).  Список метрик можно пропустить (задать null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. |
| taggedOnly | boolean | Мониторить только ресурсы с указанными AWS-тегами (`true`) или все ресурсы (`false`). |
| tagsToMonitor | [AwsConfigTag[]](#openapi-definition-AwsConfigTag) | Список AWS-тегов для мониторинга.  Можно указать до 10 тегов.  Применяется только когда параметр **taggedOnly** установлен в `true`. |

#### Объект `AwsAuthenticationData`

Credentials для AWS-аутентификации.

| Элемент | Тип | Описание |
| --- | --- | --- |
| keyBasedAuthentication | [KeyBasedAuthentication](#openapi-definition-KeyBasedAuthentication) | **Устарело**. Credentials для аутентификации по ключу. |
| roleBasedAuthentication | [RoleBasedAuthentication](#openapi-definition-RoleBasedAuthentication) | Credentials для аутентификации по роли. |
| type | string | Тип аутентификации: по роли или по ключу. Возможные значения: * `KEYS` * `ROLE` |

#### Объект `KeyBasedAuthentication`

**Устарело**. Credentials для аутентификации по ключу.

| Элемент | Тип | Описание |
| --- | --- | --- |
| accessKey | string | ID access key. |
| secretKey | string | Secret access key. |

#### Объект `RoleBasedAuthentication`

Credentials для аутентификации по роли.

| Элемент | Тип | Описание |
| --- | --- | --- |
| accountId | string | ID аккаунта Amazon. |
| externalId | string | Токен external ID для настройки IAM-роли.  Его можно получить запросом `GET /aws/iamExternalId`. |
| iamRole | string | IAM-роль, используемая Dynatrace для получения данных мониторинга. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AwsSupportingServiceConfig`

Сервис для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric[]](#openapi-definition-AwsSupportingServiceMetric) | Список метрик для мониторинга этого сервиса. Если список null, мониторится рекомендуемый список метрик для этого сервиса. |
| name | string | Имя сервиса. Допустимые имена поддерживаемых сервисов можно узнать через restAPI /aws/supportedServices |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список имён измерений метрики. |
| name | string | Имя метрики сервиса. |
| statistic | string | Статистика (агрегация), используемая для метрики. Значение AVG\_MIN\_MAX это 3 статистики сразу: AVERAGE, MINIMUM и MAXIMUM Возможные значения: * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` |

#### Объект `AwsConfigTag`

AWS-тег ресурса для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Ключ AWS-тега. |
| value | string | Значение AWS-тега. |

### JSON-модели тела ответа

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