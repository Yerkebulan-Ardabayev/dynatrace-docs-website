---
title: ActiveGate API - GET all ActiveGates
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/activegate-info/get-all
scraped: 2026-05-12T11:55:47.945294
---

# ActiveGate API - GET all ActiveGates

# ActiveGate API - GET all ActiveGates

* Reference
* Published Jul 02, 2020

Возвращает список всех ActiveGate, в данный момент подключённых к окружению или подключавшихся в течение последних 2 часов.

Вы можете сузить вывод, указав параметры фильтрации в запросе.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| hostname | string | Фильтрует результирующий набор ActiveGate по имени хоста, на котором работает.  Можно указать частичное имя. В этом случае используется оператор `CONTAINS`. | query | Опциональный |
| osType | string | Фильтрует результирующий набор ActiveGate по типу ОС хоста, на котором работает. Элемент может принимать значения * `LINUX` * `WINDOWS` | query | Опциональный |
| osArchitecture | string | Фильтрует результирующий набор ActiveGate по архитектуре ОС хоста, на котором работает. Элемент может принимать значения * `X86` * `S390` * `ARM` * `PPCLE` | query | Опциональный |
| networkAddress | string | Фильтрует результирующий набор ActiveGate по сетевому адресу.  Можно указать частичный адрес. В этом случае используется оператор `CONTAINS`. | query | Опциональный |
| loadBalancerAddress | string | Фильтрует результирующий набор ActiveGate по адресу балансировщика нагрузки.  Можно указать частичный адрес. В этом случае используется оператор `CONTAINS`. | query | Опциональный |
| type | string | Фильтрует результирующий набор ActiveGate по типу ActiveGate. Элемент может принимать значения * `ENVIRONMENT` * `ENVIRONMENT_MULTI` | query | Опциональный |
| networkZone | string | Фильтрует результирующий набор ActiveGate по network zone.  Можно указать частичное имя. В этом случае используется оператор `CONTAINS`. | query | Опциональный |
| updateStatus | string | Фильтрует результирующий набор ActiveGate по статусу авто-обновления. Элемент может принимать значения * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` | query | Опциональный |
| versionCompareType | string | Фильтрует результирующий набор ActiveGate по указанной версии.  Здесь указывается оператор сравнения. Элемент может принимать значения * `EQUAL` * `GREATER` * `GREATER_EQUAL` * `LOWER` * `LOWER_EQUAL` | query | Опциональный |
| version | string | Фильтрует результирующий набор ActiveGate по указанной версии.  Здесь указывается версия в формате `<major>.<minor>.<revision>` (например, `1.195.0`). | query | Опциональный |
| autoUpdate | string | Фильтрует результирующий набор ActiveGate по фактическому состоянию авто-обновления. Элемент может принимать значения * `DISABLED` * `ENABLED` | query | Опциональный |
| group | string | Фильтрует результирующий набор ActiveGate по группе.  Можно указать частичное имя. В этом случае используется оператор `CONTAINS`. | query | Опциональный |
| online | boolean | Фильтрует результирующий набор ActiveGate по статусу связи. | query | Опциональный |
| enabledModule | string[] | Фильтрует результирующий набор ActiveGate по включённым модулям. Элемент может принимать значения * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` | query | Опциональный |
| disabledModule | string[] | Фильтрует результирующий набор ActiveGate по отключённым модулям. Элемент может принимать значения * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` | query | Опциональный |
| containerized | boolean | Фильтрует результирующий набор ActiveGate по тем, которые работают в контейнере (`true`) или нет (`false`). | query | Опциональный |
| tokenState | string | Фильтрует результирующий набор ActiveGate по тем, у которых токен авторизации в указанном состоянии. Элемент может принимать значения * `ABSENT` * `EXPIRING` * `INVALID` * `UNKNOWN` * `UNSUPPORTED` * `VALID` | query | Опциональный |
| tokenExpirationSet | boolean | Фильтрует результирующий набор ActiveGate по тем, у которых задана дата истечения для токена авторизации. | query | Опциональный |
| fipsMode | boolean | Фильтрует результирующий набор ActiveGate по тем, которые работают в режиме FIPS (`true`) или нет (`false`). | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateList](#openapi-definition-ActiveGateList) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `ActiveGateList`

Список ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGates | [ActiveGate[]](#openapi-definition-ActiveGate) | Список ActiveGate. |

#### Объект `ActiveGate`

Параметры ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGateTokens | [ActiveGateTokenInfoDto[]](#openapi-definition-ActiveGateTokenInfoDto) | Список токенов ActiveGate. |
| autoUpdateSettings | [ActiveGateAutoUpdateConfig](#openapi-definition-ActiveGateAutoUpdateConfig) | Конфигурация авто-обновлений ActiveGate. |
| autoUpdateStatus | string | Текущий статус авто-обновлений ActiveGate. Элемент может принимать значения * `INCOMPATIBLE` * `OUTDATED` * `SCHEDULED` * `SUPPRESSED` * `UNKNOWN` * `UP2DATE` * `UPDATE_IN_PROGRESS` * `UPDATE_PENDING` * `UPDATE_PROBLEM` |
| connectedHosts | [ActiveGateConnectedHosts](#openapi-definition-ActiveGateConnectedHosts) | Информация о хостах, в данный момент подключённых к ActiveGate. |
| containerized | boolean | ActiveGate развёрнут в контейнере (`true`) или нет (`false`). |
| environments | string[] | Список окружений (заданных по ID), к которым может подключаться ActiveGate. |
| fipsMode | boolean | ActiveGate работает в режиме совместимости FIPS (`true`) или нет (`false`). |
| group | string | Группа ActiveGate. |
| hostname | string | Имя хоста, на котором работает ActiveGate. |
| id | string | ID ActiveGate. |
| loadBalancerAddresses | string[] | Список адресов балансировщика нагрузки ActiveGate. |
| mainEnvironment | string | ID основного окружения для multi-environment ActiveGate. |
| modules | [ActiveGateModule[]](#openapi-definition-ActiveGateModule) | Список модулей ActiveGate. |
| networkAddresses | string[] | Список сетевых адресов ActiveGate. |
| networkZone | string | Network zone ActiveGate. |
| offlineSince | integer | Временная метка, с которой ActiveGate находится в офлайне.  Значение `null` означает, что ActiveGate в онлайне. |
| osArchitecture | string | Архитектура ОС, на которой работает ActiveGate. Элемент может принимать значения * `S390` * `X86` * `ARM` * `PPCLE` |
| osBitness | string | Разрядность ОС, на которой работает ActiveGate. Элемент может принимать значения * `64` |
| osType | string | Тип ОС, на которой работает ActiveGate. Элемент может принимать значения * `LINUX` * `WINDOWS` |
| type | string | Тип ActiveGate. Элемент может принимать значения * `CLUSTER` * `ENVIRONMENT` * `ENVIRONMENT_MULTI` |
| version | string | Текущая версия ActiveGate в формате `<major>.<minor>.<revision>.<timestamp>`. |

#### Объект `ActiveGateTokenInfoDto`

Информация о токене ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| environmentId | string | ID окружения, к которому относится токен.  Доступен, только если поддерживается более одного окружения. |
| id | string | Идентификатор токена ActiveGate, состоящий из [префикса и публичной части](https://dt-url.net/rn00tjg) токена. |
| state | string | Состояние токена ActiveGate. Элемент может принимать значения * `ABSENT` * `EXPIRING` * `INVALID` * `UNKNOWN` * `UNSUPPORTED` * `VALID` |

#### Объект `ActiveGateAutoUpdateConfig`

Конфигурация авто-обновлений ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние авто-обновления ActiveGate.  Применимо, только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из родительской настройки. Иначе это просто дубликат значения **setting**. Элемент может принимать значения * `ENABLED` * `DISABLED` |
| setting | string | Состояние авто-обновления ActiveGate: enabled, disabled или inherited.  Если установлено в `INHERITED`, настройка наследуется из глобальной конфигурации, заданной на уровне окружения или кластера Managed. Элемент может принимать значения * `DISABLED` * `ENABLED` * `INHERITED` |

#### Объект `ActiveGateConnectedHosts`

Информация о хостах, в данный момент подключённых к ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| number | integer | Количество хостов, в данный момент подключённых к ActiveGate. |

#### Объект `ActiveGateModule`

Информация о модуле ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| attributes | object | Атрибуты модуля ActiveGate. |
| enabled | boolean | Модуль включён (`true`) или отключён (`false`). |
| misconfigured | boolean | Модуль неправильно настроен (`true`) или нет (`false`). |
| type | string | Тип модуля ActiveGate. Элемент может принимать значения * `AWS` * `AZURE` * `BEACON_FORWARDER` * `CLOUD_FOUNDRY` * `DB_INSIGHT` * `DEBUGGING` * `EXTENSIONS_V1` * `EXTENSIONS_V2` * `KUBERNETES` * `LOGS` * `MEMORY_DUMPS` * `METRIC_API` * `ONE_AGENT_ROUTING` * `OTLP_INGEST` * `REST_API` * `SYNTHETIC` * `VMWARE` * `Z_OS` |
| version | string | Версия модуля ActiveGate. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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



"setting": "INHERITED"



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

В этом примере запрос выводит все ActiveGate, доступные для окружения **mySampleEnv**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до двух записей.

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/activeGates' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/activeGates
```

#### Response body

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

#### Response code

200

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.")