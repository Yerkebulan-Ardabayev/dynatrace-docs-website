---
title: AWS anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/put-config
scraped: 2026-05-12T11:16:39.773820
---

# AWS anomaly detection API - PUT configuration

# AWS anomaly detection API - PUT configuration

* Reference
* Published Aug 28, 2019

Обновляет конфигурацию обнаружения аномалий для AWS.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [AwsAnomalyDetectionConfig](#openapi-definition-AwsAnomalyDetectionConfig) | JSON-тело запроса. Содержит параметры конфигурации обнаружения аномалий для AWS. | body | Optional |

### Объекты тела запроса

#### Объект `AwsAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для AWS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ec2CandidateCpuSaturationDetection | [Ec2CandidateCpuSaturationDetectionConfig](#openapi-definition-Ec2CandidateCpuSaturationDetectionConfig) | Конфигурация обнаружения высокой загрузки CPU на EC2 без установленного агента (кандидат на мониторинг). Если null, эта конфигурация не изменяется. | Optional |
| elbHighConnectionErrorsDetection | [ElbHighConnectionErrorsDetectionConfig](#openapi-definition-ElbHighConnectionErrorsDetectionConfig) | Конфигурация обнаружения большого числа ошибок подключения к бэкенду на ELB. | Required |
| lambdaHighErrorRateDetection | [LambdaHighErrorRateDetectionConfig](#openapi-definition-LambdaHighErrorRateDetectionConfig) | Конфигурация обнаружения высокой частоты ошибок AWS Lambda. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Optional |
| rdsHighCpuDetection | [RdsHighCpuDetectionConfig](#openapi-definition-RdsHighCpuDetectionConfig) | Конфигурация обнаружения высокой загрузки CPU на RDS. | Required |
| rdsHighMemoryDetection | [RdsHighMemoryDetectionConfig](#openapi-definition-RdsHighMemoryDetectionConfig) | Конфигурация обнаружения нехватки памяти на RDS. | Required |
| rdsHighWriteReadLatencyDetection | [RdsHighWriteReadLatencyDetectionConfig](#openapi-definition-RdsHighWriteReadLatencyDetectionConfig) | Конфигурация обнаружения высокой задержки записи/чтения RDS. | Required |
| rdsLowStorageDetection | [RdsLowStorageDetectionConfig](#openapi-definition-RdsLowStorageDetectionConfig) | Конфигурация обнаружения нехватки свободного места в хранилище на RDS. | Required |
| rdsRestartsSequenceDetection | [RdsRestartsSequenceDetectionConfig](#openapi-definition-RdsRestartsSequenceDetectionConfig) | Конфигурация обнаружения последовательности перезапусков на RDS. | Required |

#### Объект `Ec2CandidateCpuSaturationDetectionConfig`

Конфигурация обнаружения высокой загрузки CPU на EC2 без установленного агента (кандидат на мониторинг). Если null, эта конфигурация не изменяется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [Ec2CandidateCpuSaturationThresholds](#openapi-definition-Ec2CandidateCpuSaturationThresholds) | Пользовательские пороги для высокой загрузки CPU на кандидате EC2 на мониторинг. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `Ec2CandidateCpuSaturationThresholds`

Пользовательские пороги для высокой загрузки CPU на кандидате EC2 на мониторинг. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| cpuUsagePercentage | integer | Оповещать, если загрузка CPU выше *X*% в 3 из 5 замеров. | Required |

#### Объект `ElbHighConnectionErrorsDetectionConfig`

Конфигурация обнаружения большого числа ошибок подключения к бэкенду на ELB.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [ElbHighConnectionErrorsThresholds](#openapi-definition-ElbHighConnectionErrorsThresholds) | Пользовательские пороги для большого числа ошибок подключения к бэкенду на ELB. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `ElbHighConnectionErrorsThresholds`

Пользовательские пороги для большого числа ошибок подключения к бэкенду на ELB. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| connectionErrorsPerMinute | integer | Оповещать, если число ошибок подключения к бэкенду выше *X* в минуту в 3 из 5 замеров. | Required |

#### Объект `LambdaHighErrorRateDetectionConfig`

Конфигурация обнаружения высокой частоты ошибок AWS Lambda.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [LambdaHighErrorRateThresholds](#openapi-definition-LambdaHighErrorRateThresholds) | Пользовательские пороги для высокой частоты ошибок AWS Lambda. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `LambdaHighErrorRateThresholds`

Пользовательские пороги для высокой частоты ошибок AWS Lambda. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| failedInvocationsRate | integer | Оповещать, если частота неуспешных вызовов выше *X*% в 3 из 5 замеров. | Required |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `RdsHighCpuDetectionConfig`

Конфигурация обнаружения высокой загрузки CPU на RDS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [RdsHighCpuThresholds](#openapi-definition-RdsHighCpuThresholds) | Пользовательские пороги для высокой загрузки CPU на RDS. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `RdsHighCpuThresholds`

Пользовательские пороги для высокой загрузки CPU на RDS. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| cpuUsagePercentage | integer | Оповещать, если загрузка CPU выше *X*% в 3 из 5 замеров. | Required |

#### Объект `RdsHighMemoryDetectionConfig`

Конфигурация обнаружения нехватки памяти на RDS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [RdsHighMemoryThresholds](#openapi-definition-RdsHighMemoryThresholds) | Пользовательские пороги для нехватки памяти на RDS. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** условия. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `RdsHighMemoryThresholds`

Пользовательские пороги для нехватки памяти на RDS. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** условия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| freeMemory | number | Свободная память меньше *X* мегабайт в 3 из 5 замеров. | Required |
| swapUsage | number | Использование swap выше *X* гигабайт в 3 из 5 замеров. | Required |

#### Объект `RdsHighWriteReadLatencyDetectionConfig`

Конфигурация обнаружения высокой задержки записи/чтения RDS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [RdsHighLatencyThresholds](#openapi-definition-RdsHighLatencyThresholds) | Пользовательские пороги для высокой задержки записи/чтения RDS. Если не заданы, используется автоматический режим | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `RdsHighLatencyThresholds`

Пользовательские пороги для высокой задержки записи/чтения RDS. Если не заданы, используется автоматический режим

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| writeReadLatency | integer | Оповещать, если задержка чтения/записи выше *X* миллисекунд в 3 из 5 замеров. | Required |

#### Объект `RdsLowStorageDetectionConfig`

Конфигурация обнаружения нехватки свободного места в хранилище на RDS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [RdsLowStorageThresholds](#openapi-definition-RdsLowStorageThresholds) | Пользовательские пороги для нехватки свободного места в хранилище на RDS. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `RdsLowStorageThresholds`

Пользовательские пороги для нехватки свободного места в хранилище на RDS. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| freeStoragePercentage | integer | Оповещать, если свободное место в хранилище, делённое на выделенное хранилище, ниже *X*% в 3 из 5 замеров. | Required |

#### Объект `RdsRestartsSequenceDetectionConfig`

Конфигурация обнаружения последовательности перезапусков на RDS.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [RdsRestartsThresholds](#openapi-definition-RdsRestartsThresholds) | Пользовательские пороги для последовательности перезапусков на RDS. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `RdsRestartsThresholds`

Пользовательские пороги для последовательности перезапусков на RDS. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| restartsPerMinute | integer | Оповещать, если число перезапусков составляет *X* в минуту или выше в 3 из 20 замеров. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"ec2CandidateCpuSaturationDetection": {



"customThresholds": {



"cpuUsagePercentage": 98



},



"enabled": true



},



"elbHighConnectionErrorsDetection": {



"customThresholds": {



"connectionErrorsPerMinute": 4



},



"enabled": true



},



"lambdaHighErrorRateDetection": {



"customThresholds": {



"failedInvocationsRate": 2



},



"enabled": true



},



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



},



"rdsHighCpuDetection": {



"customThresholds": {



"cpuUsagePercentage": 99



},



"enabled": true



},



"rdsHighMemoryDetection": {



"customThresholds": {



"freeMemory": 96.99,



"swapUsage": 5.5



},



"enabled": true



},



"rdsHighWriteReadLatencyDetection": {



"customThresholds": {



"writeReadLatency": 800



},



"enabled": true



},



"rdsLowStorageDetection": {



"customThresholds": {



"freeStoragePercentage": 7



},



"enabled": true



},



"rdsRestartsSequenceDetection": {



"customThresholds": {



"restartsPerMinute": 3



},



"enabled": true



}



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws/validator` |

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

## Пример

В этом примере запрос обновляет конфигурацию обнаружения аномалий для AWS из примера [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/get-config#example "Просмотр конфигурации обнаружения аномалий для AWS через Dynatrace API."). Он переключает **high CPU utilization on RDS detection** в режим **custom threshold** и задаёт порог **90**%. Он также отключает **RDS running out of memory detection**.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Обязательно создайте резервную копию текущей конфигурации вызовом **GET AWS anomaly detection configuration**.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/aws \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"rdsHighCpuDetection": {



"enabled": true,



"customThresholds": {



"cpuUsagePercentage": 90



}



},



"rdsHighWriteReadLatencyDetection": {



"enabled": true



},



"rdsLowStorageDetection": {



"enabled": true



},



"rdsHighMemoryDetection": {



"enabled": false



},



"elbHighConnectionErrorsDetection": {



"enabled": true



},



"rdsRestartsSequenceDetection": {



"enabled": true



},



"lambdaHighErrorRateDetection": {



"enabled": true



}



}



'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/aws
```

#### Тело запроса

```
{



"rdsHighCpuDetection": {



"enabled": true,



"customThresholds": {



"cpuUsagePercentage": 90



}



},



"rdsHighWriteReadLatencyDetection": {



"enabled": true



},



"rdsLowStorageDetection": {



"enabled": true



},



"rdsHighMemoryDetection": {



"enabled": false



},



"elbHighConnectionErrorsDetection": {



"enabled": true



},



"rdsRestartsSequenceDetection": {



"enabled": true



},



"lambdaHighErrorRateDetection": {



"enabled": true



}



}
```

#### Код ответа

204

#### Результат

Обновлённая конфигурация имеет следующие параметры:

![Anomaly detection config - AWS - updated](https://dt-cdn.net/images/anomaly-detecion-aws-upd-688-f0ba72cfb8.png)

Anomaly detection config - AWS - updated

## Связанные темы

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Настройка чувствительности обнаружения проблем для инфраструктуры.")
* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")