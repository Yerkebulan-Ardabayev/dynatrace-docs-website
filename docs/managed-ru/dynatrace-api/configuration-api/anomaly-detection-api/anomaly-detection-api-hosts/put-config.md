---
title: Host anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/put-config
scraped: 2026-05-12T11:19:29.147958
---

# Host anomaly detection API - PUT configuration

# Host anomaly detection API - PUT configuration

* Reference
* Published Jan 23, 2019

Обновляет конфигурацию обнаружения аномалий для хостов.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [HostsAnomalyDetectionConfig](#openapi-definition-HostsAnomalyDetectionConfig) | JSON-тело запроса. Содержит параметры конфигурации обнаружения аномалий для хостов. | body | Optional |

### Объекты тела запроса

#### Объект `HostsAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для хостов.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| connectionLostDetection | [ConnectionLostDetectionConfig](#openapi-definition-ConnectionLostDetectionConfig) | Конфигурация обнаружения потери подключения. | Required |
| diskLowInodesDetection | [DiskLowInodesDetectionConfig](#openapi-definition-DiskLowInodesDetectionConfig) | Конфигурация обнаружения малого числа inode на диске. | Required |
| diskLowSpaceDetection | [DiskLowSpaceDetectionConfig](#openapi-definition-DiskLowSpaceDetectionConfig) | Конфигурация обнаружения нехватки места на диске. | Required |
| diskSlowWritesAndReadsDetection | [DiskSlowWritesAndReadsDetectionConfig](#openapi-definition-DiskSlowWritesAndReadsDetectionConfig) | Конфигурация обнаружения медленных дисков. | Required |
| highCpuSaturationDetection | [HighCpuSaturationDetectionConfig](#openapi-definition-HighCpuSaturationDetectionConfig) | Конфигурация обнаружения высокой загрузки CPU | Required |
| highGcActivityDetection | [HighGcActivityDetectionConfig](#openapi-definition-HighGcActivityDetectionConfig) | Конфигурация обнаружения высокой активности сборщика мусора. | Required |
| highMemoryDetection | [HighMemoryDetectionConfig](#openapi-definition-HighMemoryDetectionConfig) | Конфигурация обнаружения высокого потребления памяти. | Required |
| highNetworkDetection | [HighNetworkDetectionConfig](#openapi-definition-HighNetworkDetectionConfig) | Конфигурация обнаружения высокой загрузки сети. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Optional |
| networkDroppedPacketsDetection | [NetworkDroppedPacketsDetectionConfig](#openapi-definition-NetworkDroppedPacketsDetectionConfig) | Конфигурация обнаружения большого числа отброшенных пакетов. | Required |
| networkErrorsDetection | [NetworkErrorsDetectionConfig](#openapi-definition-NetworkErrorsDetectionConfig) | Конфигурация обнаружения большого числа сетевых ошибок. | Required |
| networkHighRetransmissionDetection | [NetworkHighRetransmissionDetectionConfig](#openapi-definition-NetworkHighRetransmissionDetectionConfig) | Конфигурация обнаружения высокой частоты повторных передач. | Required |
| networkTcpProblemsDetection | [NetworkTcpProblemsDetectionConfig](#openapi-definition-NetworkTcpProblemsDetectionConfig) | Конфигурация обнаружения проблем TCP-связности. | Required |
| outOfMemoryDetection | [OutOfMemoryDetectionConfig](#openapi-definition-OutOfMemoryDetectionConfig) | Конфигурация обнаружения проблем нехватки памяти Java. | Required |
| outOfThreadsDetection | [OutOfThreadsDetectionConfig](#openapi-definition-OutOfThreadsDetectionConfig) | Конфигурация обнаружения проблем нехватки потоков Java. | Required |

#### Объект `ConnectionLostDetectionConfig`

Конфигурация обнаружения потери подключения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |
| enabledOnGracefulShutdowns | boolean | Оповещать (`true`) при штатных остановках хоста. | Required |

#### Объект `DiskLowInodesDetectionConfig`

Конфигурация обнаружения малого числа inode на диске.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [DiskLowInodesThresholds](#openapi-definition-DiskLowInodesThresholds) | Пользовательские пороги для малого числа inode на диске. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `DiskLowInodesThresholds`

Пользовательские пороги для малого числа inode на диске. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| freeInodesPercentage | integer | Оповещать, если процент доступных inode ниже *X*% в 3 из 5 замеров. | Required |

#### Объект `DiskLowSpaceDetectionConfig`

Конфигурация обнаружения нехватки места на диске.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [DiskLowSpaceThresholds](#openapi-definition-DiskLowSpaceThresholds) | Пользовательские пороги для нехватки места на диске. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `DiskLowSpaceThresholds`

Пользовательские пороги для нехватки места на диске. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| freeSpacePercentage | integer | Оповещать, если свободное место на диске ниже *X*% в 3 из 5 замеров. | Required |

#### Объект `DiskSlowWritesAndReadsDetectionConfig`

Конфигурация обнаружения медленных дисков.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [DiskSlowWriteAndReadsThresholds](#openapi-definition-DiskSlowWriteAndReadsThresholds) | Пользовательские пороги для медленных дисков. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `DiskSlowWriteAndReadsThresholds`

Пользовательские пороги для медленных дисков. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| writeAndReadTime | integer | Оповещать, если время чтения/записи диска выше *X* миллисекунд в 3 из 5 замеров. | Required |

#### Объект `HighCpuSaturationDetectionConfig`

Конфигурация обнаружения высокой загрузки CPU

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [HighCpuSaturationThresholds](#openapi-definition-HighCpuSaturationThresholds) | Пользовательские пороги для высокой загрузки CPU. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `HighCpuSaturationThresholds`

Пользовательские пороги для высокой загрузки CPU. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| cpuSaturation | integer | Оповещать, если загрузка CPU выше *X*% в 3 из 5 замеров. | Required |

#### Объект `HighGcActivityDetectionConfig`

Конфигурация обнаружения высокой активности сборщика мусора.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [HighGcActivityThresholds](#openapi-definition-HighGcActivityThresholds) | Пользовательские пороги для высокой активности GC. Если не заданы, используется автоматический режим.  Выполнение **любого** из этих условий вызывает оповещение. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `HighGcActivityThresholds`

Пользовательские пороги для высокой активности GC. Если не заданы, используется автоматический режим.

Выполнение **любого** из этих условий вызывает оповещение.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| gcSuspensionPercentage | integer | Приостановка GC выше *X*% в 3 из 5 замеров. | Required |
| gcTimePercentage | integer | Время GC выше *X*% в 3 из 5 замеров. | Required |

#### Объект `HighMemoryDetectionConfig`

Конфигурация обнаружения высокого потребления памяти.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [HighMemoryThresholds](#openapi-definition-HighMemoryThresholds) | Пользовательские пороги для высокого потребления памяти. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **оба** условия. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `HighMemoryThresholds`

Пользовательские пороги для высокого потребления памяти. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **оба** условия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| pageFaultsPerSecondNonWindows | integer | Частота страничных промахов памяти выше *X* промахов в секунду на Linux. | Required |
| pageFaultsPerSecondWindows | integer | Частота страничных промахов памяти выше *X* промахов в секунду на Windows. | Required |
| usedMemoryPercentageNonWindows | integer | Использование памяти выше *X*% на Linux. | Required |
| usedMemoryPercentageWindows | integer | Использование памяти выше *X*% на Windows. | Required |

#### Объект `HighNetworkDetectionConfig`

Конфигурация обнаружения высокой загрузки сети.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [HighNetworkThresholds](#openapi-definition-HighNetworkThresholds) | Пользовательские пороги для высокой загрузки сети. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `HighNetworkThresholds`

Пользовательские пороги для высокой загрузки сети. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| utilizationPercentage | integer | Оповещать, если загрузка отправленного/полученного трафика выше *X*% в 3 из 5 замеров. | Required |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `NetworkDroppedPacketsDetectionConfig`

Конфигурация обнаружения большого числа отброшенных пакетов.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [NetworkDroppedPacketsThresholds](#openapi-definition-NetworkDroppedPacketsThresholds) | Пользовательские пороги для отброшенных пакетов. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** эти условия. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `NetworkDroppedPacketsThresholds`

Пользовательские пороги для отброшенных пакетов. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** эти условия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| droppedPacketsPercentage | integer | Процент отброшенных принятых/переданных пакетов выше *X*% в 3 из 5 замеров. | Required |
| totalPacketsRate | integer | Суммарная частота принятых/переданных пакетов выше *X* пакетов в секунду в 3 из 5 замеров. | Required |

#### Объект `NetworkErrorsDetectionConfig`

Конфигурация обнаружения большого числа сетевых ошибок.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [NetworkErrorsThresholds](#openapi-definition-NetworkErrorsThresholds) | Пользовательские пороги для сетевых ошибок. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** эти условия. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `NetworkErrorsThresholds`

Пользовательские пороги для сетевых ошибок. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** эти условия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| errorsPercentage | integer | Процент ошибочных принятых/переданных пакетов выше *X*% в 3 из 5 замеров. | Required |
| totalPacketsRate | integer | Суммарная частота принятых/переданных пакетов выше *X* пакетов в секунду в 3 из 5 замеров. | Required |

#### Объект `NetworkHighRetransmissionDetectionConfig`

Конфигурация обнаружения высокой частоты повторных передач.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [NetworkHighRetransmissionThresholds](#openapi-definition-NetworkHighRetransmissionThresholds) | Пользовательские пороги для высокой частоты повторных передач. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** эти условия. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `NetworkHighRetransmissionThresholds`

Пользовательские пороги для высокой частоты повторных передач. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** эти условия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| retransmissionRatePercentage | integer | Частота повторных передач выше *X*% в 3 из 5 замеров. | Required |
| retransmittedPacketsNumberPerMinute | integer | Число повторно переданных пакетов выше *X* пакетов в минуту в 3 из 5 замеров. | Required |

#### Объект `NetworkTcpProblemsDetectionConfig`

Конфигурация обнаружения проблем TCP-связности.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [NetworkTcpProblemsThresholds](#openapi-definition-NetworkTcpProblemsThresholds) | Пользовательские пороги для проблем TCP-подключений. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** эти условия. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `NetworkTcpProblemsThresholds`

Пользовательские пороги для проблем TCP-подключений. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** эти условия.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| failedConnectionsNumberPerMinute | integer | Число неуспешных подключений выше *X* подключений в минуту в 3 из 5 замеров. | Required |
| newConnectionFailuresPercentage | integer | Процент неуспешных новых подключений выше *X*% в 3 из 5 замеров. | Required |

#### Объект `OutOfMemoryDetectionConfig`

Конфигурация обнаружения проблем нехватки памяти Java.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [OutOfMemoryThresholds](#openapi-definition-OutOfMemoryThresholds) | Пользовательские пороги для нехватки памяти Java. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `OutOfMemoryThresholds`

Пользовательские пороги для нехватки памяти Java. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| outOfMemoryExceptionsNumber | integer | Оповещать, если число исключений нехватки памяти Java составляет *X* в минуту или выше. | Required |

#### Объект `OutOfThreadsDetectionConfig`

Конфигурация обнаружения проблем нехватки потоков Java.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customThresholds | [OutOfThreadsThresholds](#openapi-definition-OutOfThreadsThresholds) | Пользовательские пороги для обнаружения нехватки потоков Java. Если не заданы, используется автоматический режим. | Optional |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). | Required |

#### Объект `OutOfThreadsThresholds`

Пользовательские пороги для обнаружения нехватки потоков Java. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| outOfThreadsExceptionsNumber | integer | Оповещать, если число исключений нехватки потоков Java составляет *X* в минуту или выше. | Required |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"connectionLostDetection": {



"enabled": true,



"enabledOnGracefulShutdowns": true



},



"diskLowInodesDetection": {



"customThresholds": {



"freeInodesPercentage": 10



},



"enabled": true



},



"diskLowSpaceDetection": {



"customThresholds": {



"freeSpacePercentage": 10



},



"enabled": true



},



"diskSlowWritesAndReadsDetection": {



"customThresholds": {



"writeAndReadTime": 300



},



"enabled": true



},



"highCpuSaturationDetection": {



"customThresholds": {



"cpuSaturation": 90



},



"enabled": true



},



"highGcActivityDetection": {



"customThresholds": {



"gcSuspensionPercentage": 20,



"gcTimePercentage": 35



},



"enabled": true



},



"highMemoryDetection": {



"customThresholds": {



"pageFaultsPerSecondNonWindows": 10,



"pageFaultsPerSecondWindows": 50,



"usedMemoryPercentageNonWindows": 85,



"usedMemoryPercentageWindows": 85



},



"enabled": true



},



"highNetworkDetection": {



"customThresholds": {



"utilizationPercentage": 88



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



"networkDroppedPacketsDetection": {



"customThresholds": {



"droppedPacketsPercentage": 8,



"totalPacketsRate": 8



},



"enabled": true



},



"networkErrorsDetection": {



"customThresholds": {



"errorsPercentage": 9,



"totalPacketsRate": 9



},



"enabled": true



},



"networkHighRetransmissionDetection": {



"customThresholds": {



"retransmissionRatePercentage": 15,



"retransmittedPacketsNumberPerMinute": 15



},



"enabled": true



},



"networkTcpProblemsDetection": {



"customThresholds": {



"failedConnectionsNumberPerMinute": 5,



"newConnectionFailuresPercentage": 5



},



"enabled": true



},



"outOfMemoryDetection": {



"customThresholds": {



"outOfMemoryExceptionsNumber": 2



},



"enabled": true



},



"outOfThreadsDetection": {



"customThresholds": {



"outOfThreadsExceptionsNumber": 2



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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts/validator` |

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

В этом примере запрос обновляет конфигурацию обнаружения аномалий для сервисов баз данных из примера [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/get-config#example "Просмотр конфигурации обнаружения аномалий для хостов через Dynatrace API."). Он активирует функцию **Alert on graceful host shutdowns**. Он также переключает режим **Detect CPU saturation on host** в **based on custom settings** и задаёт следующий порог:

* Оповещать, если загрузка CPU выше **90**% в 3 из 5 замеров.

API-токен передаётся в заголовке **Authorization**.

Вы можете скачать или скопировать пример тела запроса, чтобы попробовать его самостоятельно. Сначала обязательно создайте резервную копию текущей конфигурации вызовом **GET host anomaly detection configuration**.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/hosts \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section below>}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/hosts
```

#### Тело запроса

```
{



"connectionLostDetection": {



"enabled": true,



"enabledOnGracefulShutdowns": true



},



"highCpuSaturationDetection": {



"enabled": true,



"customThresholds": {



"cpuSaturation": 90



}



},



"highMemoryDetection": {



"enabled": true



},



"highGcActivityDetection": {



"enabled": true



},



"outOfMemoryDetection": {



"enabled": true



},



"outOfThreadsDetection": {



"enabled": true



},



"networkDroppedPacketsDetection": {



"enabled": true



},



"networkErrorsDetection": {



"enabled": true



},



"highNetworkDetection": {



"enabled": true



},



"networkTcpProblemsDetection": {



"enabled": true



},



"networkHighRetransmissionDetection": {



"enabled": true



},



"diskLowSpaceDetection": {



"enabled": true



},



"diskSlowWritesAndReadsDetection": {



"enabled": true



},



"diskLowInodesDetection": {



"enabled": true



}



}
```

#### Код ответа

204

#### Результат

Обновлённая конфигурация имеет следующие параметры:

![Anomaly detection config - hosts - updated](https://dt-cdn.net/images/anomaly-detectoin-hosts-upd-630-085b6a0ba6.png)

Anomaly detection config - hosts - updated

## Связанные темы

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Настройка чувствительности обнаружения проблем для инфраструктуры.")
* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")