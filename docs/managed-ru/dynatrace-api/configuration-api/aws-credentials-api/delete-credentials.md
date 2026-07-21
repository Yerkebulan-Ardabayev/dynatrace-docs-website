---
title: AWS credentials API - DELETE credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/delete-credentials
---

# AWS credentials API - DELETE credentials

# AWS credentials API - DELETE credentials

* Справочник
* Опубликовано 27 июня 2019 г.

Удаляет указанную конфигурацию учётных данных AWS. Удаление отменить нельзя.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательность |
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
| connectionStatus | string | Статус соединения со средой AWS.  * `CONNECTED`: соединение устанавливалось в течение последних 10 минут. * `DISCONNECTED`: возникла проблема при установлении соединения с использованием этих учётных данных. Нужно проверить корректность данных. * `UNINITIALIZED`: успешное соединение с этими учётными данными ни разу не устанавливалось. Элемент может принимать следующие значения * `CONNECTED` * `DISCONNECTED` * `UNINITIALIZED` |
| credentialsEnabled | boolean | Включает мониторинг учётных данных. |
| id | string | Уникальный ID учётных данных. |
| label | string | Название учётных данных. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| partitionType | string | Тип раздела (partition) AWS. Элемент может принимать следующие значения * `AWS_CN` * `AWS_DEFAULT` * `AWS_US_GOV` |
| supportingServicesToMonitor | [AwsSupportingServiceConfig](#openapi-definition-AwsSupportingServiceConfig)[] | **Устарело**. Для управления сервисами нужно использовать операцию [/aws/credentials/{id}/services﻿](https://dt-url.net/l022s6v?dt=m). Встроенные сервисы здесь не поддерживаются.  Список сервисов AWS для мониторинга. Доступные сервисы перечисляются операцией [/aws/supportedServices﻿](https://dt-url.net/me02sh2?dt=m).  Для каждого сервиса можно указать список метрик и измерений (dimensions). Список поддерживаемых метрик и измерений для данного сервиса можно проверить в [документации﻿](https://dt-url.net/r12v0pkl?dt=m).  Список метрик можно пропустить (установить в null), тогда для мониторинга будет выбран рекомендуемый (по умолчанию) набор метрик и измерений. |
| taggedOnly | boolean | Мониторить только ресурсы с указанными тегами AWS (`true`) или все ресурсы (`false`). |
| tagsToMonitor | [AwsConfigTag](#openapi-definition-AwsConfigTag)[] | Список тегов AWS для мониторинга.  Можно указать до 10 тегов.  Применимо только если параметр **taggedOnly** установлен в `true`. |

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
| externalId | string | Токен внешнего ID для настройки роли IAM.  Его можно получить запросом `GET /aws/iamExternalId`. |
| iamRole | string | Роль IAM, которую Dynatrace будет использовать для получения данных мониторинга. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `AwsSupportingServiceConfig`

Сервис для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric](#openapi-definition-AwsSupportingServiceMetric)[] | Список метрик для мониторинга этого сервиса. Если список равен null, для этого сервиса будет использован рекомендуемый список метрик. |
| name | string | Название сервиса. Допустимые поддерживаемые названия сервисов можно узнать с помощью /aws/supportedServices restAPI |

#### Объект `AwsSupportingServiceMetric`

Метрика сервиса для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| dimensions | string[] | Список названий измерений (dimensions) метрики. |
| name | string | Название метрики сервиса. |
| statistic | string | Статистика (агрегация), используемая для метрики. Значение AVG\_MIN\_MAX означает сразу 3 статистики: AVERAGE, MINIMUM и MAXIMUM. Элемент может принимать следующие значения * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` |

#### Объект `AwsConfigTag`

Тег AWS ресурса для мониторинга.

| Элемент | Тип | Описание |
| --- | --- | --- |
| name | string | Ключ тега AWS. |
| value | string | Значение тега AWS. |

### Модели JSON тела ответа

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

## Формат ответа

Успешный запрос не возвращает содержимого.