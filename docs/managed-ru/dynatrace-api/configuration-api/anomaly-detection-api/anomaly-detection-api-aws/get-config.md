---
title: AWS anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/get-config
scraped: 2026-05-12T11:16:41.435535
---

# AWS anomaly detection API - GET configuration

# AWS anomaly detection API - GET configuration

* Reference
* Published Aug 28, 2019

Возвращает конфигурацию обнаружения аномалий для AWS.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsAnomalyDetectionConfig](#openapi-definition-AwsAnomalyDetectionConfig) | Успех |

### Объекты тела ответа

#### Объект `AwsAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для AWS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ec2CandidateCpuSaturationDetection | [Ec2CandidateCpuSaturationDetectionConfig](#openapi-definition-Ec2CandidateCpuSaturationDetectionConfig) | Конфигурация обнаружения высокой загрузки CPU на EC2 без установленного агента (кандидат на мониторинг). Если null, эта конфигурация не изменяется. |
| elbHighConnectionErrorsDetection | [ElbHighConnectionErrorsDetectionConfig](#openapi-definition-ElbHighConnectionErrorsDetectionConfig) | Конфигурация обнаружения большого числа ошибок подключения к бэкенду на ELB. |
| lambdaHighErrorRateDetection | [LambdaHighErrorRateDetectionConfig](#openapi-definition-LambdaHighErrorRateDetectionConfig) | Конфигурация обнаружения высокой частоты ошибок AWS Lambda. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| rdsHighCpuDetection | [RdsHighCpuDetectionConfig](#openapi-definition-RdsHighCpuDetectionConfig) | Конфигурация обнаружения высокой загрузки CPU на RDS. |
| rdsHighMemoryDetection | [RdsHighMemoryDetectionConfig](#openapi-definition-RdsHighMemoryDetectionConfig) | Конфигурация обнаружения нехватки памяти на RDS. |
| rdsHighWriteReadLatencyDetection | [RdsHighWriteReadLatencyDetectionConfig](#openapi-definition-RdsHighWriteReadLatencyDetectionConfig) | Конфигурация обнаружения высокой задержки записи/чтения RDS. |
| rdsLowStorageDetection | [RdsLowStorageDetectionConfig](#openapi-definition-RdsLowStorageDetectionConfig) | Конфигурация обнаружения нехватки свободного места в хранилище на RDS. |
| rdsRestartsSequenceDetection | [RdsRestartsSequenceDetectionConfig](#openapi-definition-RdsRestartsSequenceDetectionConfig) | Конфигурация обнаружения последовательности перезапусков на RDS. |

#### Объект `Ec2CandidateCpuSaturationDetectionConfig`

Конфигурация обнаружения высокой загрузки CPU на EC2 без установленного агента (кандидат на мониторинг). Если null, эта конфигурация не изменяется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [Ec2CandidateCpuSaturationThresholds](#openapi-definition-Ec2CandidateCpuSaturationThresholds) | Пользовательские пороги для высокой загрузки CPU на кандидате EC2 на мониторинг. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `Ec2CandidateCpuSaturationThresholds`

Пользовательские пороги для высокой загрузки CPU на кандидате EC2 на мониторинг. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| cpuUsagePercentage | integer | Оповещать, если загрузка CPU выше *X*% в 3 из 5 замеров. |

#### Объект `ElbHighConnectionErrorsDetectionConfig`

Конфигурация обнаружения большого числа ошибок подключения к бэкенду на ELB.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [ElbHighConnectionErrorsThresholds](#openapi-definition-ElbHighConnectionErrorsThresholds) | Пользовательские пороги для большого числа ошибок подключения к бэкенду на ELB. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `ElbHighConnectionErrorsThresholds`

Пользовательские пороги для большого числа ошибок подключения к бэкенду на ELB. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| connectionErrorsPerMinute | integer | Оповещать, если число ошибок подключения к бэкенду выше *X* в минуту в 3 из 5 замеров. |

#### Объект `LambdaHighErrorRateDetectionConfig`

Конфигурация обнаружения высокой частоты ошибок AWS Lambda.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [LambdaHighErrorRateThresholds](#openapi-definition-LambdaHighErrorRateThresholds) | Пользовательские пороги для высокой частоты ошибок AWS Lambda. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `LambdaHighErrorRateThresholds`

Пользовательские пороги для высокой частоты ошибок AWS Lambda. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| failedInvocationsRate | integer | Оповещать, если частота неуспешных вызовов выше *X*% в 3 из 5 замеров. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `RdsHighCpuDetectionConfig`

Конфигурация обнаружения высокой загрузки CPU на RDS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [RdsHighCpuThresholds](#openapi-definition-RdsHighCpuThresholds) | Пользовательские пороги для высокой загрузки CPU на RDS. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `RdsHighCpuThresholds`

Пользовательские пороги для высокой загрузки CPU на RDS. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| cpuUsagePercentage | integer | Оповещать, если загрузка CPU выше *X*% в 3 из 5 замеров. |

#### Объект `RdsHighMemoryDetectionConfig`

Конфигурация обнаружения нехватки памяти на RDS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [RdsHighMemoryThresholds](#openapi-definition-RdsHighMemoryThresholds) | Пользовательские пороги для нехватки памяти на RDS. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** условия. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `RdsHighMemoryThresholds`

Пользовательские пороги для нехватки памяти на RDS. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** условия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| freeMemory | number | Свободная память меньше *X* мегабайт в 3 из 5 замеров. |
| swapUsage | number | Использование swap выше *X* гигабайт в 3 из 5 замеров. |

#### Объект `RdsHighWriteReadLatencyDetectionConfig`

Конфигурация обнаружения высокой задержки записи/чтения RDS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [RdsHighLatencyThresholds](#openapi-definition-RdsHighLatencyThresholds) | Пользовательские пороги для высокой задержки записи/чтения RDS. Если не заданы, используется автоматический режим |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `RdsHighLatencyThresholds`

Пользовательские пороги для высокой задержки записи/чтения RDS. Если не заданы, используется автоматический режим

| Элемент | Тип | Описание |
| --- | --- | --- |
| writeReadLatency | integer | Оповещать, если задержка чтения/записи выше *X* миллисекунд в 3 из 5 замеров. |

#### Объект `RdsLowStorageDetectionConfig`

Конфигурация обнаружения нехватки свободного места в хранилище на RDS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [RdsLowStorageThresholds](#openapi-definition-RdsLowStorageThresholds) | Пользовательские пороги для нехватки свободного места в хранилище на RDS. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `RdsLowStorageThresholds`

Пользовательские пороги для нехватки свободного места в хранилище на RDS. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| freeStoragePercentage | integer | Оповещать, если свободное место в хранилище, делённое на выделенное хранилище, ниже *X*% в 3 из 5 замеров. |

#### Объект `RdsRestartsSequenceDetectionConfig`

Конфигурация обнаружения последовательности перезапусков на RDS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [RdsRestartsThresholds](#openapi-definition-RdsRestartsThresholds) | Пользовательские пороги для последовательности перезапусков на RDS. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `RdsRestartsThresholds`

Пользовательские пороги для последовательности перезапусков на RDS. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| restartsPerMinute | integer | Оповещать, если число перезапусков составляет *X* в минуту или выше в 3 из 20 замеров. |

### JSON-модели тела ответа

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

## Пример

В этом примере запрос возвращает текущую конфигурацию обнаружения аномалий для AWS.

API-токен передаётся в заголовке **Authorization**.

Конфигурация имеет следующие настройки:

![Anomaly detection config - AWS](https://dt-cdn.net/images/anomaly-detecion-aws-573-880e8e55e6.png)

Anomaly detection config - AWS

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/aws \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/aws
```

#### Тело ответа

```
{



"metadata": {



"clusterVersion": "1.163.2.20190201-072431",



"configurationVersions": [



8,



2



]



},



"rdsHighCpuDetection": {



"enabled": true



},



"rdsHighWriteReadLatencyDetection": {



"enabled": true



},



"rdsLowStorageDetection": {



"enabled": true



},



"rdsHighMemoryDetection": {



"enabled": true



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

200

## Связанные темы

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Настройка чувствительности обнаружения проблем для инфраструктуры.")
* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")