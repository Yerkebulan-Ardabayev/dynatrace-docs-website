---
title: Host anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/get-config
---

# Host anomaly detection API - GET configuration

# Host anomaly detection API - GET configuration

* Reference
* Published Aug 28, 2019

Gets the configuration of anomaly detection for hosts.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [HostsAnomalyDetectionConfig](#openapi-definition-HostsAnomalyDetectionConfig) | Success |

### Response body objects

#### The `HostsAnomalyDetectionConfig` object

Configuration of anomaly detection for hosts.

| Element | Type | Description |
| --- | --- | --- |
| connectionLostDetection | [ConnectionLostDetectionConfig](#openapi-definition-ConnectionLostDetectionConfig) | Configuration of lost connection detection. |
| diskLowInodesDetection | [DiskLowInodesDetectionConfig](#openapi-definition-DiskLowInodesDetectionConfig) | Configuration of low disk inodes number detection. |
| diskLowSpaceDetection | [DiskLowSpaceDetectionConfig](#openapi-definition-DiskLowSpaceDetectionConfig) | Configuration of low disk space detection. |
| diskSlowWritesAndReadsDetection | [DiskSlowWritesAndReadsDetectionConfig](#openapi-definition-DiskSlowWritesAndReadsDetectionConfig) | Configuration of slow running disks detection. |
| highCpuSaturationDetection | [HighCpuSaturationDetectionConfig](#openapi-definition-HighCpuSaturationDetectionConfig) | Configuration of high CPU saturation detection |
| highGcActivityDetection | [HighGcActivityDetectionConfig](#openapi-definition-HighGcActivityDetectionConfig) | Configuration of high Garbage Collector activity detection. |
| highMemoryDetection | [HighMemoryDetectionConfig](#openapi-definition-HighMemoryDetectionConfig) | Configuration of high memory usage detection. |
| highNetworkDetection | [HighNetworkDetectionConfig](#openapi-definition-HighNetworkDetectionConfig) | Configuration of high network utilization detection. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| networkDroppedPacketsDetection | [NetworkDroppedPacketsDetectionConfig](#openapi-definition-NetworkDroppedPacketsDetectionConfig) | Configuration of high number of dropped packets detection. |
| networkErrorsDetection | [NetworkErrorsDetectionConfig](#openapi-definition-NetworkErrorsDetectionConfig) | Configuration of high number of network errors detection. |
| networkHighRetransmissionDetection | [NetworkHighRetransmissionDetectionConfig](#openapi-definition-NetworkHighRetransmissionDetectionConfig) | Configuration of high retransmission rate detection. |
| networkTcpProblemsDetection | [NetworkTcpProblemsDetectionConfig](#openapi-definition-NetworkTcpProblemsDetectionConfig) | Configuration of TCP connectivity problems detection. |
| outOfMemoryDetection | [OutOfMemoryDetectionConfig](#openapi-definition-OutOfMemoryDetectionConfig) | Configuration of Java out of memory problems detection. |
| outOfThreadsDetection | [OutOfThreadsDetectionConfig](#openapi-definition-OutOfThreadsDetectionConfig) | Configuration of Java out of threads problems detection. |

#### The `ConnectionLostDetectionConfig` object

Configuration of lost connection detection.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |
| enabledOnGracefulShutdowns | boolean | Alert (`true`) on graceful host shutdowns. |

#### The `DiskLowInodesDetectionConfig` object

Configuration of low disk inodes number detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [DiskLowInodesThresholds](#openapi-definition-DiskLowInodesThresholds) | Custom thresholds for low disk inodes number. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `DiskLowInodesThresholds` object

Custom thresholds for low disk inodes number. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| freeInodesPercentage | integer | Alert if percentage of available inodes is lower than *X*% in 3 out of 5 samples. |

#### The `DiskLowSpaceDetectionConfig` object

Configuration of low disk space detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [DiskLowSpaceThresholds](#openapi-definition-DiskLowSpaceThresholds) | Custom thresholds for low disk space. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `DiskLowSpaceThresholds` object

Custom thresholds for low disk space. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| freeSpacePercentage | integer | Alert if free disk space is lower than *X*% in 3 out of 5 samples. |

#### The `DiskSlowWritesAndReadsDetectionConfig` object

Configuration of slow running disks detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [DiskSlowWriteAndReadsThresholds](#openapi-definition-DiskSlowWriteAndReadsThresholds) | Custom thresholds for slow running disks. If not set, the automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `DiskSlowWriteAndReadsThresholds` object

Custom thresholds for slow running disks. If not set, the automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| writeAndReadTime | integer | Alert if disk read/write time is higher than *X* milliseconds in 3 out of 5 samples. |

#### The `HighCpuSaturationDetectionConfig` object

Configuration of high CPU saturation detection

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [HighCpuSaturationThresholds](#openapi-definition-HighCpuSaturationThresholds) | Custom thresholds for high CPU saturation. If not set then the automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `HighCpuSaturationThresholds` object

Custom thresholds for high CPU saturation. If not set then the automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| cpuSaturation | integer | Alert if CPU usage is higher than *X*% in 3 out of 5 samples. |

#### The `HighGcActivityDetectionConfig` object

Configuration of high Garbage Collector activity detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [HighGcActivityThresholds](#openapi-definition-HighGcActivityThresholds) | Custom thresholds for high GC activity. If not set, automatic mode is used.  Meeting **any** of these conditions triggers an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `HighGcActivityThresholds` object

Custom thresholds for high GC activity. If not set, automatic mode is used.

Meeting **any** of these conditions triggers an alert.

| Element | Type | Description |
| --- | --- | --- |
| gcSuspensionPercentage | integer | GC suspension is higher than *X*% in 3 out of 5 samples. |
| gcTimePercentage | integer | GC time is higher than *X*% in 3 out of 5 samples. |

#### The `HighMemoryDetectionConfig` object

Configuration of high memory usage detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [HighMemoryThresholds](#openapi-definition-HighMemoryThresholds) | Custom thresholds for high memory usage. If not set then the automatic mode is used.  **Both** conditions must be met to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `HighMemoryThresholds` object

Custom thresholds for high memory usage. If not set then the automatic mode is used.

**Both** conditions must be met to trigger an alert.

| Element | Type | Description |
| --- | --- | --- |
| pageFaultsPerSecondNonWindows | integer | Memory page fault rate is higher than *X* faults per second on Linux. |
| pageFaultsPerSecondWindows | integer | Memory page fault rate is higher than *X* faults per second on Windows. |
| usedMemoryPercentageNonWindows | integer | Memory usage is higher than *X*% on Linux. |
| usedMemoryPercentageWindows | integer | Memory usage is higher than *X*% on Windows. |

#### The `HighNetworkDetectionConfig` object

Configuration of high network utilization detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [HighNetworkThresholds](#openapi-definition-HighNetworkThresholds) | Custom thresholds for high network utilization. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `HighNetworkThresholds` object

Custom thresholds for high network utilization. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| utilizationPercentage | integer | Alert if sent/received traffic utilization is higher than *X*% in 3 out of 5 samples. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `NetworkDroppedPacketsDetectionConfig` object

Configuration of high number of dropped packets detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [NetworkDroppedPacketsThresholds](#openapi-definition-NetworkDroppedPacketsThresholds) | Custom thresholds for dropped packets. If not set, automatic mode is used.  **All** of these conditions must be met to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `NetworkDroppedPacketsThresholds` object

Custom thresholds for dropped packets. If not set, automatic mode is used.

**All** of these conditions must be met to trigger an alert.

| Element | Type | Description |
| --- | --- | --- |
| droppedPacketsPercentage | integer | Receive/transmit dropped packet percentage is higher than *X*% in 3 out of 5 samples. |
| totalPacketsRate | integer | Total receive/transmit packets rate is higher than *X* packets per second in 3 out of 5 samples. |

#### The `NetworkErrorsDetectionConfig` object

Configuration of high number of network errors detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [NetworkErrorsThresholds](#openapi-definition-NetworkErrorsThresholds) | Custom thresholds for network errors. If not set, automatic mode is used.  **All** of these conditions must be met to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `NetworkErrorsThresholds` object

Custom thresholds for network errors. If not set, automatic mode is used.

**All** of these conditions must be met to trigger an alert.

| Element | Type | Description |
| --- | --- | --- |
| errorsPercentage | integer | Receive/transmit error packet percentage is higher than *X*% in 3 out of 5 samples. |
| totalPacketsRate | integer | Total receive/transmit packets rate is higher than *X* packets per second in 3 out of 5 samples. |

#### The `NetworkHighRetransmissionDetectionConfig` object

Configuration of high retransmission rate detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [NetworkHighRetransmissionThresholds](#openapi-definition-NetworkHighRetransmissionThresholds) | Custom thresholds for high retransmission rate. If not set, automatic mode is used.  **All** of these conditions must be met to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `NetworkHighRetransmissionThresholds` object

Custom thresholds for high retransmission rate. If not set, automatic mode is used.

**All** of these conditions must be met to trigger an alert.

| Element | Type | Description |
| --- | --- | --- |
| retransmissionRatePercentage | integer | Retransmission rate is higher than *X*% in 3 out of 5 samples. |
| retransmittedPacketsNumberPerMinute | integer | Number of retransmitted packets is higher than *X* packets per minute in 3 out of 5 samples. |

#### The `NetworkTcpProblemsDetectionConfig` object

Configuration of TCP connectivity problems detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [NetworkTcpProblemsThresholds](#openapi-definition-NetworkTcpProblemsThresholds) | Custom thresholds for TCP connection problems. If not set, automatic mode is used.  **All** of these conditions must be met to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `NetworkTcpProblemsThresholds` object

Custom thresholds for TCP connection problems. If not set, automatic mode is used.

**All** of these conditions must be met to trigger an alert.

| Element | Type | Description |
| --- | --- | --- |
| failedConnectionsNumberPerMinute | integer | Number of failed connections is higher than *X* connections per minute in 3 out of 5 samples. |
| newConnectionFailuresPercentage | integer | Percentage of new connection failures is higher than *X*% in 3 out of 5 samples. |

#### The `OutOfMemoryDetectionConfig` object

Configuration of Java out of memory problems detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [OutOfMemoryThresholds](#openapi-definition-OutOfMemoryThresholds) | Custom thresholds for Java out of memory. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `OutOfMemoryThresholds` object

Custom thresholds for Java out of memory. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| outOfMemoryExceptionsNumber | integer | Alert if the number of Java out of memory exceptions is *X* per minute or higher. |

#### The `OutOfThreadsDetectionConfig` object

Configuration of Java out of threads problems detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [OutOfThreadsThresholds](#openapi-definition-OutOfThreadsThresholds) | Custom thresholds for Java out of threads detection. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `OutOfThreadsThresholds` object

Custom thresholds for Java out of threads detection. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| outOfThreadsExceptionsNumber | integer | Alert if the number of Java out of threads exceptions is *X* per minute or higher. |

### Response body JSON models

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

## Example

In this example, the request lists the current configuration of anomaly detection for hosts.

The API token is passed in the **Authorization** header.

The configuration has the following settings:

![Anomaly detection config - hosts](https://dt-cdn.net/images/anomaly-detectoin-hosts-623-66c432a5ee.png)

Anomaly detection config - hosts

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/hosts \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/hosts
```

#### Response body

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

#### Response code

200

## Related topics

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.")
* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")