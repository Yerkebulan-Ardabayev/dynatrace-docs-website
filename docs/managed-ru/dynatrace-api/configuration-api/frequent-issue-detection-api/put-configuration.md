---
title: Frequent issue detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/frequent-issue-detection-api/put-configuration
---

# Frequent issue detection API - PUT configuration

# Frequent issue detection API - PUT configuration

* Справочник
* Опубликовано 28 июня 2019 г.

Этот API устарел. Используй [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") вместо него. Ищи схему **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`).

Обновляет конфигурацию обнаружения частых проблем.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать его, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [FrequentIssueDetectionConfig](#openapi-definition-FrequentIssueDetectionConfig) | Тело JSON запроса, содержащее параметры конфигурации обнаружения частых проблем | body | Необязательный |

### Объекты тела запроса

#### Объект `FrequentIssueDetectionConfig`

Параметры обнаружения частых проблем. Подробнее об этом см. в разделе [Detection of frequent issues﻿](https://dt-url.net/4da3kdg?dt=m) в документации Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| frequentIssueDetectionApplicationEnabled | boolean | Обнаружение для приложений включено (`true`) или отключено (`false`). | Обязательный |
| frequentIssueDetectionEnvironmentEnabled | boolean | Обнаружение для окружения включено (`true`) или отключено (`false`). | Необязательный |
| frequentIssueDetectionInfrastructureEnabled | boolean | Обнаружение для инфраструктуры включено (`true`) или отключено (`false`). | Обязательный |
| frequentIssueDetectionServiceEnabled | boolean | Обнаружение для сервисов включено (`true`) или отключено (`false`). | Обязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Необязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Необязательный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Необязательный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Необязательный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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
| **204** | - | Успешно. Конфигурация обновлена. Ответ не содержит тела |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недопустимы |

### Объекты тела ответа

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

## Проверка полезной нагрузки

Рекомендуется проверить полезную нагрузку перед отправкой её в составе реального запроса. Код ответа **204** означает, что полезная нагрузка валидна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать его, см. в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация валидна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Введённые данные недопустимы |

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

#### Модели тела JSON ответа

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

В этом примере запрос обновляет конфигурацию обнаружения аномалий для приложений из примера [GET-запроса](/managed/dynatrace-api/configuration-api/frequent-issue-detection-api/get-configuration#example "Read frequent issue configuration via the Dynatrace API."). Он активирует **обнаружение частых проблем для приложений**.

Токен API передаётся в заголовке **Authorization**.

Пример тела запроса можно скачать или скопировать, чтобы опробовать самостоятельно. Обязательно создай резервную копию текущей конфигурации с помощью GET-запроса.

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

Anomaly detection configuration - updated

## Связанные темы

* [Detection of frequent issues](/managed/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues "Understand how Dynatrace detects and manages recurring problem patterns as frequent issues.")