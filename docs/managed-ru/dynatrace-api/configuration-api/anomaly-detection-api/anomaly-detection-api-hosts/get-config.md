---
title: Host anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/get-config
scraped: 2026-05-12T11:19:26.420443
---

# Host anomaly detection API - GET configuration

# Host anomaly detection API - GET configuration

* Reference
* Published Aug 28, 2019

Возвращает конфигурацию обнаружения аномалий для хостов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostsAnomalyDetectionConfig](#openapi-definition-HostsAnomalyDetectionConfig) | Успех |

### Объекты тела ответа

#### Объект `HostsAnomalyDetectionConfig`

Конфигурация обнаружения аномалий для хостов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| connectionLostDetection | [ConnectionLostDetectionConfig](#openapi-definition-ConnectionLostDetectionConfig) | Конфигурация обнаружения потери подключения. |
| diskLowInodesDetection | [DiskLowInodesDetectionConfig](#openapi-definition-DiskLowInodesDetectionConfig) | Конфигурация обнаружения малого числа inode на диске. |
| diskLowSpaceDetection | [DiskLowSpaceDetectionConfig](#openapi-definition-DiskLowSpaceDetectionConfig) | Конфигурация обнаружения нехватки места на диске. |
| diskSlowWritesAndReadsDetection | [DiskSlowWritesAndReadsDetectionConfig](#openapi-definition-DiskSlowWritesAndReadsDetectionConfig) | Конфигурация обнаружения медленных дисков. |
| highCpuSaturationDetection | [HighCpuSaturationDetectionConfig](#openapi-definition-HighCpuSaturationDetectionConfig) | Конфигурация обнаружения высокой загрузки CPU |
| highGcActivityDetection | [HighGcActivityDetectionConfig](#openapi-definition-HighGcActivityDetectionConfig) | Конфигурация обнаружения высокой активности сборщика мусора. |
| highMemoryDetection | [HighMemoryDetectionConfig](#openapi-definition-HighMemoryDetectionConfig) | Конфигурация обнаружения высокого потребления памяти. |
| highNetworkDetection | [HighNetworkDetectionConfig](#openapi-definition-HighNetworkDetectionConfig) | Конфигурация обнаружения высокой загрузки сети. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| networkDroppedPacketsDetection | [NetworkDroppedPacketsDetectionConfig](#openapi-definition-NetworkDroppedPacketsDetectionConfig) | Конфигурация обнаружения большого числа отброшенных пакетов. |
| networkErrorsDetection | [NetworkErrorsDetectionConfig](#openapi-definition-NetworkErrorsDetectionConfig) | Конфигурация обнаружения большого числа сетевых ошибок. |
| networkHighRetransmissionDetection | [NetworkHighRetransmissionDetectionConfig](#openapi-definition-NetworkHighRetransmissionDetectionConfig) | Конфигурация обнаружения высокой частоты повторных передач. |
| networkTcpProblemsDetection | [NetworkTcpProblemsDetectionConfig](#openapi-definition-NetworkTcpProblemsDetectionConfig) | Конфигурация обнаружения проблем TCP-связности. |
| outOfMemoryDetection | [OutOfMemoryDetectionConfig](#openapi-definition-OutOfMemoryDetectionConfig) | Конфигурация обнаружения проблем нехватки памяти Java. |
| outOfThreadsDetection | [OutOfThreadsDetectionConfig](#openapi-definition-OutOfThreadsDetectionConfig) | Конфигурация обнаружения проблем нехватки потоков Java. |

#### Объект `ConnectionLostDetectionConfig`

Конфигурация обнаружения потери подключения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |
| enabledOnGracefulShutdowns | boolean | Оповещать (`true`) при штатных остановках хоста. |

#### Объект `DiskLowInodesDetectionConfig`

Конфигурация обнаружения малого числа inode на диске.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [DiskLowInodesThresholds](#openapi-definition-DiskLowInodesThresholds) | Пользовательские пороги для малого числа inode на диске. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `DiskLowInodesThresholds`

Пользовательские пороги для малого числа inode на диске. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| freeInodesPercentage | integer | Оповещать, если процент доступных inode ниже *X*% в 3 из 5 замеров. |

#### Объект `DiskLowSpaceDetectionConfig`

Конфигурация обнаружения нехватки места на диске.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [DiskLowSpaceThresholds](#openapi-definition-DiskLowSpaceThresholds) | Пользовательские пороги для нехватки места на диске. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `DiskLowSpaceThresholds`

Пользовательские пороги для нехватки места на диске. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| freeSpacePercentage | integer | Оповещать, если свободное место на диске ниже *X*% в 3 из 5 замеров. |

#### Объект `DiskSlowWritesAndReadsDetectionConfig`

Конфигурация обнаружения медленных дисков.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [DiskSlowWriteAndReadsThresholds](#openapi-definition-DiskSlowWriteAndReadsThresholds) | Пользовательские пороги для медленных дисков. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `DiskSlowWriteAndReadsThresholds`

Пользовательские пороги для медленных дисков. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| writeAndReadTime | integer | Оповещать, если время чтения/записи диска выше *X* миллисекунд в 3 из 5 замеров. |

#### Объект `HighCpuSaturationDetectionConfig`

Конфигурация обнаружения высокой загрузки CPU

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [HighCpuSaturationThresholds](#openapi-definition-HighCpuSaturationThresholds) | Пользовательские пороги для высокой загрузки CPU. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `HighCpuSaturationThresholds`

Пользовательские пороги для высокой загрузки CPU. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| cpuSaturation | integer | Оповещать, если загрузка CPU выше *X*% в 3 из 5 замеров. |

#### Объект `HighGcActivityDetectionConfig`

Конфигурация обнаружения высокой активности сборщика мусора.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [HighGcActivityThresholds](#openapi-definition-HighGcActivityThresholds) | Пользовательские пороги для высокой активности GC. Если не заданы, используется автоматический режим.  Выполнение **любого** из этих условий вызывает оповещение. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `HighGcActivityThresholds`

Пользовательские пороги для высокой активности GC. Если не заданы, используется автоматический режим.

Выполнение **любого** из этих условий вызывает оповещение.

| Элемент | Тип | Описание |
| --- | --- | --- |
| gcSuspensionPercentage | integer | Приостановка GC выше *X*% в 3 из 5 замеров. |
| gcTimePercentage | integer | Время GC выше *X*% в 3 из 5 замеров. |

#### Объект `HighMemoryDetectionConfig`

Конфигурация обнаружения высокого потребления памяти.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [HighMemoryThresholds](#openapi-definition-HighMemoryThresholds) | Пользовательские пороги для высокого потребления памяти. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **оба** условия. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `HighMemoryThresholds`

Пользовательские пороги для высокого потребления памяти. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **оба** условия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| pageFaultsPerSecondNonWindows | integer | Частота страничных промахов памяти выше *X* промахов в секунду на Linux. |
| pageFaultsPerSecondWindows | integer | Частота страничных промахов памяти выше *X* промахов в секунду на Windows. |
| usedMemoryPercentageNonWindows | integer | Использование памяти выше *X*% на Linux. |
| usedMemoryPercentageWindows | integer | Использование памяти выше *X*% на Windows. |

#### Объект `HighNetworkDetectionConfig`

Конфигурация обнаружения высокой загрузки сети.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [HighNetworkThresholds](#openapi-definition-HighNetworkThresholds) | Пользовательские пороги для высокой загрузки сети. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `HighNetworkThresholds`

Пользовательские пороги для высокой загрузки сети. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| utilizationPercentage | integer | Оповещать, если загрузка отправленного/полученного трафика выше *X*% в 3 из 5 замеров. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `NetworkDroppedPacketsDetectionConfig`

Конфигурация обнаружения большого числа отброшенных пакетов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [NetworkDroppedPacketsThresholds](#openapi-definition-NetworkDroppedPacketsThresholds) | Пользовательские пороги для отброшенных пакетов. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** эти условия. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `NetworkDroppedPacketsThresholds`

Пользовательские пороги для отброшенных пакетов. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** эти условия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| droppedPacketsPercentage | integer | Процент отброшенных принятых/переданных пакетов выше *X*% в 3 из 5 замеров. |
| totalPacketsRate | integer | Суммарная частота принятых/переданных пакетов выше *X* пакетов в секунду в 3 из 5 замеров. |

#### Объект `NetworkErrorsDetectionConfig`

Конфигурация обнаружения большого числа сетевых ошибок.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [NetworkErrorsThresholds](#openapi-definition-NetworkErrorsThresholds) | Пользовательские пороги для сетевых ошибок. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** эти условия. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `NetworkErrorsThresholds`

Пользовательские пороги для сетевых ошибок. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** эти условия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| errorsPercentage | integer | Процент ошибочных принятых/переданных пакетов выше *X*% в 3 из 5 замеров. |
| totalPacketsRate | integer | Суммарная частота принятых/переданных пакетов выше *X* пакетов в секунду в 3 из 5 замеров. |

#### Объект `NetworkHighRetransmissionDetectionConfig`

Конфигурация обнаружения высокой частоты повторных передач.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [NetworkHighRetransmissionThresholds](#openapi-definition-NetworkHighRetransmissionThresholds) | Пользовательские пороги для высокой частоты повторных передач. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** эти условия. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `NetworkHighRetransmissionThresholds`

Пользовательские пороги для высокой частоты повторных передач. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** эти условия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| retransmissionRatePercentage | integer | Частота повторных передач выше *X*% в 3 из 5 замеров. |
| retransmittedPacketsNumberPerMinute | integer | Число повторно переданных пакетов выше *X* пакетов в минуту в 3 из 5 замеров. |

#### Объект `NetworkTcpProblemsDetectionConfig`

Конфигурация обнаружения проблем TCP-связности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [NetworkTcpProblemsThresholds](#openapi-definition-NetworkTcpProblemsThresholds) | Пользовательские пороги для проблем TCP-подключений. Если не заданы, используется автоматический режим.  Для срабатывания оповещения должны выполняться **все** эти условия. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `NetworkTcpProblemsThresholds`

Пользовательские пороги для проблем TCP-подключений. Если не заданы, используется автоматический режим.

Для срабатывания оповещения должны выполняться **все** эти условия.

| Элемент | Тип | Описание |
| --- | --- | --- |
| failedConnectionsNumberPerMinute | integer | Число неуспешных подключений выше *X* подключений в минуту в 3 из 5 замеров. |
| newConnectionFailuresPercentage | integer | Процент неуспешных новых подключений выше *X*% в 3 из 5 замеров. |

#### Объект `OutOfMemoryDetectionConfig`

Конфигурация обнаружения проблем нехватки памяти Java.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [OutOfMemoryThresholds](#openapi-definition-OutOfMemoryThresholds) | Пользовательские пороги для нехватки памяти Java. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `OutOfMemoryThresholds`

Пользовательские пороги для нехватки памяти Java. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| outOfMemoryExceptionsNumber | integer | Оповещать, если число исключений нехватки памяти Java составляет *X* в минуту или выше. |

#### Объект `OutOfThreadsDetectionConfig`

Конфигурация обнаружения проблем нехватки потоков Java.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customThresholds | [OutOfThreadsThresholds](#openapi-definition-OutOfThreadsThresholds) | Пользовательские пороги для обнаружения нехватки потоков Java. Если не заданы, используется автоматический режим. |
| enabled | boolean | Обнаружение включено (`true`) или отключено (`false`). |

#### Объект `OutOfThreadsThresholds`

Пользовательские пороги для обнаружения нехватки потоков Java. Если не заданы, используется автоматический режим.

| Элемент | Тип | Описание |
| --- | --- | --- |
| outOfThreadsExceptionsNumber | integer | Оповещать, если число исключений нехватки потоков Java составляет *X* в минуту или выше. |

### JSON-модели тела ответа

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

## Пример

В этом примере запрос возвращает текущую конфигурацию обнаружения аномалий для хостов.

API-токен передаётся в заголовке **Authorization**.

Конфигурация имеет следующие настройки:

![Anomaly detection config - hosts](https://dt-cdn.net/images/anomaly-detectoin-hosts-623-66c432a5ee.png)

Anomaly detection config - hosts

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/hosts \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/hosts
```

#### Тело ответа

```
{



"metadata": {



"clusterVersion": "1.163.5.20190201-130834",



"configurationVersions": [



91



]



},



"connectionLostDetection": {



"enabled": true,



"enabledOnGracefulShutdowns": false



},



"highCpuSaturationDetection": {



"enabled": true



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

200

## Связанные темы

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Настройка чувствительности обнаружения проблем для инфраструктуры.")
* [Davis® AI](/managed/dynatrace-intelligence "Познакомьтесь с возможностями Davis AI.")