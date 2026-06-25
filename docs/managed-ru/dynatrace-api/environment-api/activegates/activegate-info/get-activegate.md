---
title: ActiveGate API - GET an ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/activegate-info/get-activegate
scraped: 2026-05-12T11:55:45.610208
---

# ActiveGate API - GET an ActiveGate

# ActiveGate API - GET an ActiveGate

* Reference
* Published Jul 02, 2020

Возвращает информацию об указанном ActiveGate.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| agId | string | ID требуемого ActiveGate. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGate](#openapi-definition-ActiveGate) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не найдено. Подробности в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

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

В этом примере запрос выводит параметры ActiveGate с ID **876651882**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -L -X GET 'https://mySampleEnv/api/v2/activeGates/876651882' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv/api/v2/activeGates/876651882
```

#### Response body

```
{



"id": "876651882",



"networkAddresses": [



"orange-13.easytravel.com",



"228.245.125.39"



],



"osType": "LINUX",



"autoUpdateStatus": "UPDATE_IN_PROGRESS",



"offlineSince": null,



"version": "1.198.0.20200630-163221",



"type": "ENVIRONMENT",



"hostname": "orange-13.easytravel.com",



"mainEnvironment": null,



"environments": [



"mySampleEnv"



],



"networkZone": "easytravel.europe.austria.05"



}
```

#### Response code

200

## Связанные темы

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.")