---
title: Frequent issue detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/frequent-issue-detection-api/put-configuration
scraped: 2026-05-12T12:15:28.508429
---

# Frequent issue detection API - PUT configuration

# Frequent issue detection API - PUT configuration

* Reference
* Published Jun 28, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`).

Обновляет конфигурацию frequent issue detection.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [FrequentIssueDetectionConfig](#openapi-definition-FrequentIssueDetectionConfig) | JSON-тело запроса с параметрами конфигурации frequent issue detection | body | Optional |

### Объекты тела запроса

#### Объект `FrequentIssueDetectionConfig`

Параметры frequent issue detection. Подробнее смотрите [Detection of frequent issues](https://dt-url.net/4da3kdg) в документации Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| frequentIssueDetectionApplicationEnabled | boolean | Detection для applications включена (`true`) или выключена (`false`). | Required |
| frequentIssueDetectionEnvironmentEnabled | boolean | Detection для environment включена (`true`) или выключена (`false`). | Optional |
| frequentIssueDetectionInfrastructureEnabled | boolean | Detection для infrastructure включена (`true`) или выключена (`false`). | Required |
| frequentIssueDetectionServiceEnabled | boolean | Detection для services включена (`true`) или выключена (`false`). | Required |
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



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionEnvironmentEnabled": false,



"frequentIssueDetectionInfrastructureEnabled": true,



"frequentIssueDetectionServiceEnabled": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

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

В этом примере запрос обновляет конфигурацию anomaly detection для applications из примера [GET request](/managed/dynatrace-api/configuration-api/frequent-issue-detection-api/get-configuration#example "Чтение конфигурации frequent issue через Dynatrace API."). Активируется **frequent issue detection для applications**.

API-токен передаётся в заголовке **Authorization**.

Можно скачать или скопировать пример тела запроса для своих экспериментов. Обязательно сделайте backup-копию текущей конфигурации через GET request.

#### Curl

```
curl -L -X PUT 'https://mySampleEnv.live.dynatrace.com/api/config/v1/frequentIssueDetection' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": false



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/frequentIssueDetection
```

#### Тело запроса

```
{



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": false



}
```

#### Код ответа

204

#### Результат

Обновлённая конфигурация имеет следующие параметры:

![Anomaly detection configuration - updated](https://dt-cdn.net/images/put-frequent-issue-703-b57d1c1c38.png)

Конфигурация anomaly detection: обновлена

## Связанные темы

* [Detection of frequent issues](/managed/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues "Узнайте, как Dynatrace обнаруживает и управляет повторяющимися проблемными паттернами как frequent issues.")