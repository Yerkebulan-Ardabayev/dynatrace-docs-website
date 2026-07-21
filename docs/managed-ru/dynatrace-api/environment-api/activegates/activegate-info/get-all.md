---
title: ActiveGate API - GET all ActiveGates
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/activegate-info/get-all
---

# ActiveGate API - GET all ActiveGates

# ActiveGate API - GET all ActiveGates

* Справка
* Опубликовано 02 июля 2020 г.

Выводит список всех ActiveGateов, которые в настоящий момент подключены к environment или были подключены в течение последних 2 часов.

Можно сузить выдачу, указав параметры фильтрации в запросе.

Запрос формирует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `activeGates.read`.

О том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| hostname | string | Фильтрует результирующий набор ActiveGateов по имени хоста, на котором он запущен. Можно указать часть имени, в этом случае используется оператор `CONTAINS`. | query | Необязательный |
| osType | string | Фильтрует результирующий набор ActiveGateов по типу ОС хоста, на котором он запущен. Элемент может принимать следующие значения * `LINUX` * `WINDOWS` | query | Необязательный |
| osArchitecture | string | Фильтрует результирующий набор ActiveGateов по архитектуре ОС хоста, на котором он запущен. Элемент может принимать следующие значения * `X86` * `S390` * `ARM` * `PPCLE` | query | Необязательный |
| networkAddress | string | Фильтрует результирующий набор ActiveGateов по сетевому адресу. Можно указать часть адреса, в этом случае используется оператор `CONTAINS`. | query | Необязательный |
| loadBalancerAddress | string | Фильтрует результирующий набор ActiveGateов по адресу Load Balancer. Можно указать часть адреса, в этом случае используется оператор `CONTAINS`. | query | Необязательный |
| type | string | Фильтрует результирующий набор ActiveGateов по типу ActiveGate. Элемент может принимать следующие значения * `ENVIRONMENT` * `ENVIRONMENT_MULTI` | query | Необязательный |
| networkZone | string | Фильтрует результирующий набор ActiveGateов по сетевой зоне. Можно указать часть имени, в этом случае используется оператор `CONTAINS`. | query | Необязательный |
| updateStatus | string | Фильтрует результирующий набор ActiveGateов по статусу автообновления. Элемент может принимать следующие значения * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` | query | Необязательный |
| versionCompareType | string | Фильтрует результирующий набор ActiveGateов по указанной версии. Здесь указывается оператор сравнения. Элемент может принимать следующие значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Необязательный |
| version | string | Фильтрует результирующий набор ActiveGateов по указанной версии. Здесь указывается версия в формате `<major>.<minor>.<revision>` (например, `1.195.0`). | query | Необязательный |
| autoUpdate | string | Фильтрует результирующий набор ActiveGateов по фактическому состоянию автообновления. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` | query | Необязательный |
| group | string | Фильтрует результирующий набор ActiveGateов по группе. Можно указать часть имени, в этом случае используется оператор `CONTAINS`. | query | Необязательный |
| online | boolean | Фильтрует результирующий набор ActiveGateов по статусу соединения. | query | Необязательный |
| enabledModule | string[] | Фильтрует результирующий набор ActiveGateов по включённым модулям. Элемент может принимать следующие значения * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` | query | Необязательный |
| disabledModule | string[] | Фильтрует результирующий набор ActiveGateов по отключённым модулям. Элемент может принимать следующие значения * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` | query | Необязательный |
| containerized | boolean | Фильтрует результирующий набор ActiveGateов, оставляя те, что работают в контейнере (`true`) или нет (`false`). | query | Необязательный |
| tokenState | string | Фильтрует результирующий набор ActiveGateов, оставляя те, у которых токен авторизации находится в указанном состоянии. Элемент может принимать следующие значения * `ABSENT` * `EXPIRING` * `INVALID` * `UNKNOWN` * `UNSUPPORTED` * `VALID` | query | Необязательный |
| tokenExpirationSet | boolean | Фильтрует результирующий набор ActiveGateов, оставляя те, у которых задана дата истечения токена авторизации. | query | Необязательный |
| fipsMode | boolean | Фильтрует результирующий набор ActiveGateов, оставляя те, что работают в режиме FIPS (`true`) или нет (`false`). | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateList](#openapi-definition-ActiveGateList) | Успешно |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ActiveGateList`

Список ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGates | [ActiveGate](#openapi-definition-ActiveGate)[] | Список ActiveGate. |

#### Объект `ActiveGate`

Параметры ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGateTokens | [ActiveGateTokenInfoDto](#openapi-definition-ActiveGateTokenInfoDto)[] | Список токенов ActiveGate. |
| autoUpdateSettings | [ActiveGateAutoUpdateConfig](#openapi-definition-ActiveGateAutoUpdateConfig) | Конфигурация автообновлений ActiveGate. |
| autoUpdateStatus | string | Текущий статус автообновлений ActiveGate. Элемент может принимать следующие значения * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` |
| connectedHosts | [ActiveGateConnectedHosts](#openapi-definition-ActiveGateConnectedHosts) | Информация о хостах, в данный момент подключённых к ActiveGate |
| containerized | boolean | ActiveGate развёрнут в контейнере (`true`) или нет (`false`). |
| environments | string[] | Список сред (указанных по ID), к которым может подключаться ActiveGate. |
| fipsMode | boolean | ActiveGate работает в режиме, совместимом с FIPS (`true`), или нет (`false`). |
| group | string | Группа ActiveGate. |
| hostname | string | Имя хоста, на котором работает ActiveGate. |
| id | string | ID ActiveGate. |
| loadBalancerAddresses | string[] | Список адресов балансировщика нагрузки ActiveGate. |
| mainEnvironment | string | ID главной среды для мультисредового ActiveGate. |
| modules | [ActiveGateModule](#openapi-definition-ActiveGateModule)[] | Список модулей ActiveGate. |
| networkAddresses | string[] | Список сетевых адресов ActiveGate. |
| networkZone | string | Сетевая зона ActiveGate. |
| offlineSince | integer | Метка времени, с которой ActiveGate находится в офлайне. Значение `null` означает, что ActiveGate в онлайне. |
| osArchitecture | string | Архитектура ОС, на которой работает ActiveGate. Элемент может принимать следующие значения * `S390` * `X86` * `ARM` * `PPCLE` |
| osBitness | string | Разрядность ОС, на которой работает ActiveGate. Элемент может принимать следующие значения * `64` |
| osType | string | Тип ОС, на которой работает ActiveGate. Элемент может принимать следующие значения * `LINUX` * `WINDOWS` |
| type | string | Тип ActiveGate. Элемент может принимать следующие значения * `CLUSTER` * `ENVIRONMENT` * `ENVIRONMENT_MULTI` |
| version | string | Текущая версия ActiveGate в формате `<major>.<minor>.<revision>.<timestamp>`. |

#### Объект `ActiveGateTokenInfoDto`

Информация о токене ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| environmentId | string | ID среды, к которой относится токен. Доступно только если поддерживается больше одной среды. |
| id | string | Идентификатор токена ActiveGate, состоящий из [префикса и публичной части﻿](https://dt-url.net/rn00tjg?dt=m) токена. |
| state | string | Состояние токена ActiveGate. Элемент может принимать следующие значения * `ABSENT` * `EXPIRING` * `INVALID` * `UNKNOWN` * `UNSUPPORTED` * `VALID` |

#### Объект `ActiveGateAutoUpdateConfig`

Конфигурация автообновлений ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние автообновления ActiveGate. Применимо только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из родительской настройки. Иначе это просто дубликат значения **setting**. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` |
| setting | string | Состояние автообновления ActiveGate: включено, отключено или унаследовано. Если установлено значение `INHERITED`, настройка наследуется из глобальной конфигурации, заданной на уровне среды или Managed-кластера. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | Целевая версия ActiveGate. Версию нужно указывать в формате `<major>.<minor>` (например, `1.342`) либо `latest`, `previous` или `older`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Основная информация обо всех настроенных окнах обновления |

#### Объект `UpdateWindowsConfig`

Основная информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание |
| --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, в которые может начаться обновление OneAgent. Если значение отсутствует и обновление должно быть выполнено, оно начнётся при первой возможности. |

#### Объект `UpdateWindow`

Основная информация об одном окне обслуживания

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор окна обслуживания |
| name | string | Имя окна обслуживания |

#### Объект `ActiveGateConnectedHosts`

Информация о хостах, в данный момент подключённых к ActiveGate

| Элемент | Тип | Описание |
| --- | --- | --- |
| number | integer | Количество хостов, в данный момент подключённых к ActiveGate |

#### Объект `ActiveGateModule`

Информация о модуле ActiveGate

| Элемент | Тип | Описание |
| --- | --- | --- |
| attributes | object | Атрибуты модуля ActiveGate. |
| enabled | boolean | Модуль включён (`true`) или отключён (`false`). |
| misconfigured | boolean | Модуль настроен некорректно (`true`) или нет (`false`). |
| type | string | Тип модуля ActiveGate. Элемент может принимать следующие значения * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` |
| version | string | Версия модуля ActiveGate. |

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

### Примеры моделей тела ответа JSON

```
{



"activeGates": [



{



"activeGateTokens": [



{



"environmentId": "string",



"id": "dt0g02.4KWZO5EF",



"state": "ABSENT"



}



],



"autoUpdateSettings": {



"effectiveSetting": "ENABLED",



"setting": "INHERITED",



"targetVersion": "latest",



"updateWindows": {



"windows": [



{



"id": "vu9U3hXa3q0AAAABADdkeW5hdHJhY2Uuc2V0dGluZ3MuZGVwbG95bWVudC5tYW5h",



"name": "Daily maintenance window"



}



]



}



},



"autoUpdateStatus": "OUTDATED",



"connectedHosts": {



"number": 150



},



"containerized": true,



"environments": [



"string"



],



"fipsMode": true,



"group": "default",



"hostname": "exampleHostname",



"id": "0x3efdd091",



"loadBalancerAddresses": [



"string"



],



"mainEnvironment": "d1bf4a7e-666b-43af-9f45-718g98372e2f",



"modules": [



{



"attributes": {},



"enabled": true,



"misconfigured": true,



"type": "KUBERNETES",



"version": "string"



}



],



"networkAddresses": [



"string"



],



"networkZone": "exampleNetworkZone",



"offlineSince": 1582031917814,



"osArchitecture": "X86",



"osBitness": "64",



"osType": "WINDOWS",



"type": "ENVIRONMENT",



"version": "1.185.0.20200201-120000"



}



]



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

## Пример

В этом примере запрос выводит список всех ActiveGate, доступных для среды **mySampleEnv**.

Токен API передаётся в заголовке **Authorization**.

Результат сокращён до двух записей.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates
```

#### Тело ответа

```
{



"activeGates": [



{



"id": "1541791174",



"networkAddresses": [



"orange-15.easytravel.com",



"150.134.11.6"



],



"osType": "LINUX",



"autoUpdateStatus": "UP2DATE",



"offlineSince": null,



"version": "1.193.0.20200416-144858",



"type": "ENVIRONMENT",



"hostname": "orange-15.easytravel.com",



"mainEnvironment": null,



"environments": [



"mySampleEnv"



],



"networkZone": "default"



},



{



"id": "974977376",



"networkAddresses": [



"win-18.easytravel.com",



"66.165.59.105"



],



"osType": "WINDOWS",



"autoUpdateStatus": "OUTDATED",



"offlineSince": null,



"version": "1.198.0.20200629-221007",



"type": "ENVIRONMENT",



"hostname": "win-18.easytravel.com",



"mainEnvironment": null,



"environments": [



"mySampleEnv"



],



"networkZone": "default"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Понять базовые концепции, связанные с ActiveGate.")