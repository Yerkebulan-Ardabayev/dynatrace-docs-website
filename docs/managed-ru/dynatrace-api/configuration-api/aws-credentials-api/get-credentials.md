---
title: AWS credentials API - GET credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/get-credentials
---

# AWS credentials API - GET credentials

# AWS credentials API - GET credentials

* Справка
* Опубликовано 27 июня 2019 г.

Получает конфигурацию указанных учётных данных AWS.

Запрос возвращает содержимое `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать токен, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID указанной конфигурации учётных данных AWS. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsCredentialsConfig](#openapi-definition-AwsCredentialsConfig) | Успешно |

### Объекты тела ответа

#### Объект `AwsCredentialsConfig`

Конфигурация учётных данных AWS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| authenticationData | [AwsAuthenticationData](#openapi-definition-AwsAuthenticationData) | Учётные данные для аутентификации AWS. |
| connectionStatus | string | Статус соединения со средой AWS.  * `CONNECTED`: соединение устанавливалось в течение последних 10 минут. * `DISCONNECTED`: возникла проблема при установлении соединения с использованием этих учётных данных. Нужно проверить корректность данных. * `UNINITIALIZED`: успешное соединение с этими учётными данными никогда не устанавливалось. Элемент может принимать следующие значения * `CONNECTED` * `DISCONNECTED` * `UNINITIALIZED` |
| credentialsEnabled | boolean | Включает мониторинг учётных данных. |
| id | string | Уникальный ID учётных данных. |
| label | string | Название учётных данных. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| partitionType | string | Тип раздела AWS. Элемент может принимать следующие значения * `AWS_CN` * `AWS_DEFAULT` * `AWS_US_GOV` |
| supportingServicesToMonitor | [AwsSupportingServiceConfig](#openapi-definition-AwsSupportingServiceConfig)[] | **Устарело**. Для управления сервисами используй операцию [/aws/credentials/{id}/services﻿](https://dt-url.net/l022s6v?dt=m). Встроенные сервисы здесь не поддерживаются.  Список сервисов AWS, подлежащих мониторингу. Доступные сервисы перечисляются операцией [/aws/supportedServices﻿](https://dt-url.net/me02sh2?dt=m).  Для каждого сервиса можно указать список метрик и измерений. Список поддерживаемых метрик и измерений для конкретного сервиса можно посмотреть в [документации﻿](https://dt-url.net/r12v0pkl?dt=m).  Список метрик можно пропустить (задать значение null), в этом случае для мониторинга будет выбран рекомендованный (по умолчанию) набор метрик и измерений. |
| taggedOnly | boolean | Мониторить только ресурсы с указанными тегами AWS (`true`) или все ресурсы (`false`). |
| tagsToMonitor | [AwsConfigTag](#openapi-definition-AwsConfigTag)[] | Список тегов AWS, подлежащих мониторингу.  Можно указать до 10 тегов.  Применимо только когда параметр **taggedOnly** установлен в `true`. |

#### Объект `AwsAuthenticationData`

Учётные данные для аутентификации AWS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| keyBasedAuthentication | [KeyBasedAuthentication](#openapi-definition-KeyBasedAuthentication) | **Устарело**. Учётные данные для аутентификации на основе ключей. |
| roleBasedAuthentication | [RoleBasedAuthentication](#openapi-definition-RoleBasedAuthentication) | Учётные данные для аутентификации на основе роли. |
| type | string | Тип аутентификации: на основе роли или на основе ключей. Элемент может принимать следующие значения * `KEYS` * `ROLE` |

#### Объект `KeyBasedAuthentication`

**Устарело**. Учётные данные для аутентификации на основе ключей.

| Элемент | Тип | Описание |
| --- | --- | --- |
| accessKey | string | ID ключа доступа. |
| secretKey | string | Секретный ключ доступа. |

#### Объект `RoleBasedAuthentication`

Учётные данные для аутентификации на основе роли.

| Элемент | Тип | Описание |
| --- | --- | --- |
| accountId | string | ID учётной записи Amazon. |
| externalId | string | Внешний ID-токен для настройки роли IAM.  Его можно получить запросом `GET /aws/iamExternalId`. |
| iamRole | string | Роль IAM, используемая Dynatrace для получения данных мониторинга. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AwsSupportingServiceConfig`

Сервис, подлежащий мониторингу.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric](#openapi-definition-AwsSupportingServiceMetric)[] | Список метрик, подлежащих мониторингу для этого сервиса. Если список равен null, для мониторинга будет использован рекомендованный список метрик для этого сервиса. |
| name | string | Название сервиса. Действительные поддерживаемые названия сервисов можно узнать с помощью /aws/supportedServices restAPI |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса, подлежащая мониторингу.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список названий измерений метрики. |
| name | string | Название метрики сервиса. |
| statistic | string | Статистика (агрегация), используемая для метрики. Значение AVG\_MIN\_MAX представляет собой сразу 3 статистики: AVERAGE, MINIMUM и MAXIMUM Элемент может принимать следующие значения * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` |

#### Объект `AwsConfigTag`

Тег AWS ресурса, подлежащего мониторингу.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Ключ тега AWS. |
| value | string | Значение тега AWS. |

### JSON моделей тела ответа

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