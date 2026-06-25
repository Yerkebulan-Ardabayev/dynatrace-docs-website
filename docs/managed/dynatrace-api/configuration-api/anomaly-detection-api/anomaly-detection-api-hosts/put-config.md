---
title: Host anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/put-config
scraped: 2026-05-12T11:19:29.147958
---

# Host anomaly detection API - PUT configuration

# Host anomaly detection API - PUT configuration

* Reference
* Published Jan 23, 2019

Updates the configuration of anomaly detection for hosts.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [HostsAnomalyDetectionConfig](#openapi-definition-HostsAnomalyDetectionConfig) | The JSON body of the request. Contains parameters of the host anomaly detection configuration. | body | Optional |

### Request body objects

#### The `HostsAnomalyDetectionConfig` object

Configuration of anomaly detection for hosts.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| connectionLostDetection | [ConnectionLostDetectionConfig](#openapi-definition-ConnectionLostDetectionConfig) | Configuration of lost connection detection. | Required |
| diskLowInodesDetection | [DiskLowInodesDetectionConfig](#openapi-definition-DiskLowInodesDetectionConfig) | Configuration of low disk inodes number detection. | Required |
| diskLowSpaceDetection | [DiskLowSpaceDetectionConfig](#openapi-definition-DiskLowSpaceDetectionConfig) | Configuration of low disk space detection. | Required |
| diskSlowWritesAndReadsDetection | [DiskSlowWritesAndReadsDetectionConfig](#openapi-definition-DiskSlowWritesAndReadsDetectionConfig) | Configuration of slow running disks detection. | Required |
| highCpuSaturationDetection | [HighCpuSaturationDetectionConfig](#openapi-definition-HighCpuSaturationDetectionConfig) | Configuration of high CPU saturation detection | Required |
| highGcActivityDetection | [HighGcActivityDetectionConfig](#openapi-definition-HighGcActivityDetectionConfig) | Configuration of high Garbage Collector activity detection. | Required |
| highMemoryDetection | [HighMemoryDetectionConfig](#openapi-definition-HighMemoryDetectionConfig) | Configuration of high memory usage detection. | Required |
| highNetworkDetection | [HighNetworkDetectionConfig](#openapi-definition-HighNetworkDetectionConfig) | Configuration of high network utilization detection. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| networkDroppedPacketsDetection | [NetworkDroppedPacketsDetectionConfig](#openapi-definition-NetworkDroppedPacketsDetectionConfig) | Configuration of high number of dropped packets detection. | Required |
| networkErrorsDetection | [NetworkErrorsDetectionConfig](#openapi-definition-NetworkErrorsDetectionConfig) | Configuration of high number of network errors detection. | Required |
| networkHighRetransmissionDetection | [NetworkHighRetransmissionDetectionConfig](#openapi-definition-NetworkHighRetransmissionDetectionConfig) | Configuration of high retransmission rate detection. | Required |
| networkTcpProblemsDetection | [NetworkTcpProblemsDetectionConfig](#openapi-definition-NetworkTcpProblemsDetectionConfig) | Configuration of TCP connectivity problems detection. | Required |
| outOfMemoryDetection | [OutOfMemoryDetectionConfig](#openapi-definition-OutOfMemoryDetectionConfig) | Configuration of Java out of memory problems detection. | Required |
| outOfThreadsDetection | [OutOfThreadsDetectionConfig](#openapi-definition-OutOfThreadsDetectionConfig) | Configuration of Java out of threads problems detection. | Required |

#### The `ConnectionLostDetectionConfig` object

Configuration of lost connection detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |
| enabledOnGracefulShutdowns | boolean | Alert (`true`) on graceful host shutdowns. | Required |

#### The `DiskLowInodesDetectionConfig` object

Configuration of low disk inodes number detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [DiskLowInodesThresholds](#openapi-definition-DiskLowInodesThresholds) | Custom thresholds for low disk inodes number. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `DiskLowInodesThresholds` object

Custom thresholds for low disk inodes number. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| freeInodesPercentage | integer | Alert if percentage of available inodes is lower than *X*% in 3 out of 5 samples. | Required |

#### The `DiskLowSpaceDetectionConfig` object

Configuration of low disk space detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [DiskLowSpaceThresholds](#openapi-definition-DiskLowSpaceThresholds) | Custom thresholds for low disk space. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `DiskLowSpaceThresholds` object

Custom thresholds for low disk space. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| freeSpacePercentage | integer | Alert if free disk space is lower than *X*% in 3 out of 5 samples. | Required |

#### The `DiskSlowWritesAndReadsDetectionConfig` object

Configuration of slow running disks detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [DiskSlowWriteAndReadsThresholds](#openapi-definition-DiskSlowWriteAndReadsThresholds) | Custom thresholds for slow running disks. If not set, the automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `DiskSlowWriteAndReadsThresholds` object

Custom thresholds for slow running disks. If not set, the automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| writeAndReadTime | integer | Alert if disk read/write time is higher than *X* milliseconds in 3 out of 5 samples. | Required |

#### The `HighCpuSaturationDetectionConfig` object

Configuration of high CPU saturation detection

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [HighCpuSaturationThresholds](#openapi-definition-HighCpuSaturationThresholds) | Custom thresholds for high CPU saturation. If not set then the automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `HighCpuSaturationThresholds` object

Custom thresholds for high CPU saturation. If not set then the automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| cpuSaturation | integer | Alert if CPU usage is higher than *X*% in 3 out of 5 samples. | Required |

#### The `HighGcActivityDetectionConfig` object

Configuration of high Garbage Collector activity detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [HighGcActivityThresholds](#openapi-definition-HighGcActivityThresholds) | Custom thresholds for high GC activity. If not set, automatic mode is used.  Meeting **any** of these conditions triggers an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `HighGcActivityThresholds` object

Custom thresholds for high GC activity. If not set, automatic mode is used.

Meeting **any** of these conditions triggers an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| gcSuspensionPercentage | integer | GC suspension is higher than *X*% in 3 out of 5 samples. | Required |
| gcTimePercentage | integer | GC time is higher than *X*% in 3 out of 5 samples. | Required |

#### The `HighMemoryDetectionConfig` object

Configuration of high memory usage detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [HighMemoryThresholds](#openapi-definition-HighMemoryThresholds) | Custom thresholds for high memory usage. If not set then the automatic mode is used.  **Both** conditions must be met to trigger an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `HighMemoryThresholds` object

Custom thresholds for high memory usage. If not set then the automatic mode is used.

**Both** conditions must be met to trigger an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| pageFaultsPerSecondNonWindows | integer | Memory page fault rate is higher than *X* faults per second on Linux. | Required |
| pageFaultsPerSecondWindows | integer | Memory page fault rate is higher than *X* faults per second on Windows. | Required |
| usedMemoryPercentageNonWindows | integer | Memory usage is higher than *X*% on Linux. | Required |
| usedMemoryPercentageWindows | integer | Memory usage is higher than *X*% on Windows. | Required |

#### The `HighNetworkDetectionConfig` object

Configuration of high network utilization detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [HighNetworkThresholds](#openapi-definition-HighNetworkThresholds) | Custom thresholds for high network utilization. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `HighNetworkThresholds` object

Custom thresholds for high network utilization. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| utilizationPercentage | integer | Alert if sent/received traffic utilization is higher than *X*% in 3 out of 5 samples. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `NetworkDroppedPacketsDetectionConfig` object

Configuration of high number of dropped packets detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [NetworkDroppedPacketsThresholds](#openapi-definition-NetworkDroppedPacketsThresholds) | Custom thresholds for dropped packets. If not set, automatic mode is used.  **All** of these conditions must be met to trigger an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `NetworkDroppedPacketsThresholds` object

Custom thresholds for dropped packets. If not set, automatic mode is used.

**All** of these conditions must be met to trigger an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| droppedPacketsPercentage | integer | Receive/transmit dropped packet percentage is higher than *X*% in 3 out of 5 samples. | Required |
| totalPacketsRate | integer | Total receive/transmit packets rate is higher than *X* packets per second in 3 out of 5 samples. | Required |

#### The `NetworkErrorsDetectionConfig` object

Configuration of high number of network errors detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [NetworkErrorsThresholds](#openapi-definition-NetworkErrorsThresholds) | Custom thresholds for network errors. If not set, automatic mode is used.  **All** of these conditions must be met to trigger an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `NetworkErrorsThresholds` object

Custom thresholds for network errors. If not set, automatic mode is used.

**All** of these conditions must be met to trigger an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| errorsPercentage | integer | Receive/transmit error packet percentage is higher than *X*% in 3 out of 5 samples. | Required |
| totalPacketsRate | integer | Total receive/transmit packets rate is higher than *X* packets per second in 3 out of 5 samples. | Required |

#### The `NetworkHighRetransmissionDetectionConfig` object

Configuration of high retransmission rate detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [NetworkHighRetransmissionThresholds](#openapi-definition-NetworkHighRetransmissionThresholds) | Custom thresholds for high retransmission rate. If not set, automatic mode is used.  **All** of these conditions must be met to trigger an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `NetworkHighRetransmissionThresholds` object

Custom thresholds for high retransmission rate. If not set, automatic mode is used.

**All** of these conditions must be met to trigger an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| retransmissionRatePercentage | integer | Retransmission rate is higher than *X*% in 3 out of 5 samples. | Required |
| retransmittedPacketsNumberPerMinute | integer | Number of retransmitted packets is higher than *X* packets per minute in 3 out of 5 samples. | Required |

#### The `NetworkTcpProblemsDetectionConfig` object

Configuration of TCP connectivity problems detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [NetworkTcpProblemsThresholds](#openapi-definition-NetworkTcpProblemsThresholds) | Custom thresholds for TCP connection problems. If not set, automatic mode is used.  **All** of these conditions must be met to trigger an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `NetworkTcpProblemsThresholds` object

Custom thresholds for TCP connection problems. If not set, automatic mode is used.

**All** of these conditions must be met to trigger an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| failedConnectionsNumberPerMinute | integer | Number of failed connections is higher than *X* connections per minute in 3 out of 5 samples. | Required |
| newConnectionFailuresPercentage | integer | Percentage of new connection failures is higher than *X*% in 3 out of 5 samples. | Required |

#### The `OutOfMemoryDetectionConfig` object

Configuration of Java out of memory problems detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [OutOfMemoryThresholds](#openapi-definition-OutOfMemoryThresholds) | Custom thresholds for Java out of memory. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `OutOfMemoryThresholds` object

Custom thresholds for Java out of memory. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| outOfMemoryExceptionsNumber | integer | Alert if the number of Java out of memory exceptions is *X* per minute or higher. | Required |

#### The `OutOfThreadsDetectionConfig` object

Configuration of Java out of threads problems detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [OutOfThreadsThresholds](#openapi-definition-OutOfThreadsThresholds) | Custom thresholds for Java out of threads detection. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `OutOfThreadsThresholds` object

Custom thresholds for Java out of threads detection. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| outOfThreadsExceptionsNumber | integer | Alert if the number of Java out of threads exceptions is *X* per minute or higher. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

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

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/hosts/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

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

## Example

In this example, the request updates the configuration of anomaly detection for database services from the [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-hosts/get-config#example "Read the configuration of anomaly detection for hosts via the Dynatrace API.") example. It activates the **Alert on graceful host shutdowns** feature. It also changes **Detect CPU saturation on host** mode to **based on custom settings** and sets the following threshold:

* Alert if CPU usage is higher than **90**% in 3 out of 5 samples.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. First, be sure to create a backup copy of your current configuration with the **GET host anomaly detection configuration** call.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/hosts \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{<truncated - see the Request body section below>}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/hosts
```

#### Request body

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

#### Response code

204

#### Result

The updated configuration has the following parameters:

![Anomaly detection config - hosts - updated](https://dt-cdn.net/images/anomaly-detectoin-hosts-upd-630-085b6a0ba6.png)

Anomaly detection config - hosts - updated

## Related topics

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.")
* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")