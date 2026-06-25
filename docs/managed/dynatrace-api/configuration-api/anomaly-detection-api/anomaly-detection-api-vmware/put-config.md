---
title: VMware anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/put-config
scraped: 2026-05-12T11:19:09.799556
---

# VMware anomaly detection API - PUT configuration

# VMware anomaly detection API - PUT configuration

* Reference
* Published Jan 23, 2019

Updates the configuration of anomaly detection for VMware.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [VMwareAnomalyDetectionConfig](#openapi-definition-VMwareAnomalyDetectionConfig) | JSON body of the request, containing parameters of the VMware anomaly detection configuration. | body | Optional |

### Request body objects

#### The `VMwareAnomalyDetectionConfig` object

The configuration of the anomaly detection for VMware.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| droppedPacketsDetection | [DroppedPacketsDetectionConfig](#openapi-definition-DroppedPacketsDetectionConfig) | The configuration of the high number of dropped packets detection. | Required |
| esxiHighCpuSaturation | [EsxiHighCpuSaturationConfig](#openapi-definition-EsxiHighCpuSaturationConfig) | The configuration of the CPU saturation on ESXi host detection. | Required |
| esxiHighMemoryDetection | [EsxiHighMemoryDetectionConfig](#openapi-definition-EsxiHighMemoryDetectionConfig) | The configuration of the memory saturation on ESXi host detection. | Required |
| guestCpuLimitReached | [GuestCPULimitReachedConfig](#openapi-definition-GuestCPULimitReachedConfig) | The configuration of the guest CPU limit reached configuration detection. | Optional |
| lowDatastoreSpaceDetection | [LowDatastoreSpaceDetectionConfig](#openapi-definition-LowDatastoreSpaceDetectionConfig) | The configuraiton of the low datastore free space detection. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| overloadedStorageDetection | [OverloadedStorageDetectionConfig](#openapi-definition-OverloadedStorageDetectionConfig) | The cofiguration of the overloaded storage on physical storage device detection. | Required |
| slowPhysicalStorageDetection | [SlowPhysicalStorageDetectionConfig](#openapi-definition-SlowPhysicalStorageDetectionConfig) | The configuraiton of the physical storage device running slow detection. | Required |
| undersizedStorageDetection | [UndersizedStorageDetectionConfig](#openapi-definition-UndersizedStorageDetectionConfig) | Undersized storage device detection cofing | Required |

#### The `DroppedPacketsDetectionConfig` object

The configuration of the high number of dropped packets detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [DroppedPacketsThresholds](#openapi-definition-DroppedPacketsThresholds) | Custom thresholds for high number of dropped packets. If not set then the automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `DroppedPacketsThresholds` object

Custom thresholds for high number of dropped packets. If not set then the automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| droppedPacketsPerSecond | integer | Alert if receive/transmit dropped packets rate on NIC is higher than *X* packets per second in 3 out of 5 samples. | Required |

#### The `EsxiHighCpuSaturationConfig` object

The configuration of the CPU saturation on ESXi host detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [EsxiHighCpuThresholds](#openapi-definition-EsxiHighCpuThresholds) | Custom thresholds for CPU saturation detection on ESXi. If not set then the automatic mode is used.  **All** conditions must be fulfilled to trigger an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `EsxiHighCpuThresholds` object

Custom thresholds for CPU saturation detection on ESXi. If not set then the automatic mode is used.

**All** conditions must be fulfilled to trigger an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| cpuPeakPercentage | integer | At least one peak higher than *X*% occurred in 3 out of 5 samples. | Required |
| cpuUsagePercentage | integer | CPU usage is higher than *X*% in 3 out of 5 samples. | Required |
| vmCpuReadyPercentage | integer | VM CPU ready is higher than *X*% in 3 out of 5 samples. | Required |

#### The `EsxiHighMemoryDetectionConfig` object

The configuration of the memory saturation on ESXi host detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [EsxiHighMemoryThresholds](#openapi-definition-EsxiHighMemoryThresholds) | Custom thresholds for memory saturation on ESXi host. If not set then the automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `EsxiHighMemoryThresholds` object

Custom thresholds for memory saturation on ESXi host. If not set then the automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| compressionDecompressionRate | number | Alert if ESXi host swap IN/OUT or compression/decompression rate is higher *X* kilobytes per second in 3 out of 5 samples. | Required |

#### The `GuestCPULimitReachedConfig` object

The configuration of the guest CPU limit reached configuration detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [GuestCPULimitThresholds](#openapi-definition-GuestCPULimitThresholds) | Custom thresholds for guest CPU limit detection. If not set then the automatic mode is used.  **All** conditions must be fulfilled to trigger an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `GuestCPULimitThresholds` object

Custom thresholds for guest CPU limit detection. If not set then the automatic mode is used.

**All** conditions must be fulfilled to trigger an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| hostCpuUsageMinPercentage | integer | Hypervisor CPU usage is higher than *X*% in 3 out of 5 samples. | Required |
| vmCpuReadyMaxPercentage | integer | VM CPU ready is higher than *X*% occurred in 3 out of 5 samples. | Required |
| vmCpuUsageMaxPercentage | integer | VM CPU usage (VM CPU Usage Mhz / VM CPU limit in Mhz) is higher than *X*% in 3 out of 5 samples. | Required |

#### The `LowDatastoreSpaceDetectionConfig` object

The configuraiton of the low datastore free space detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [LowDatastoreSpaceThresholds](#openapi-definition-LowDatastoreSpaceThresholds) | Custom thresholds for low datastore free space. If not set then the automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `LowDatastoreSpaceThresholds` object

Custom thresholds for low datastore free space. If not set then the automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| freeSpacePercentage | integer | Alert if datastore free space is lower than *X*%. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `OverloadedStorageDetectionConfig` object

The cofiguration of the overloaded storage on physical storage device detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [OverloadedStorageThresholds](#openapi-definition-OverloadedStorageThresholds) | Custom thresholds for overloaded storage on physical storage device. If not set then the automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `OverloadedStorageThresholds` object

Custom thresholds for overloaded storage on physical storage device. If not set then the automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| commandAbortsNumber | integer | Alert if number of command aborts is higher than *X* in 3 out of 5 samples. | Required |

#### The `SlowPhysicalStorageDetectionConfig` object

The configuraiton of the physical storage device running slow detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [SlowPhysicalStorageThresholds](#openapi-definition-SlowPhysicalStorageThresholds) | Custom thresholds for slow running physical storage device. If not set then the automatic mode is used.  Fulfillment of **any** condition triggers an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `SlowPhysicalStorageThresholds` object

Custom thresholds for slow running physical storage device. If not set then the automatic mode is used.

Fulfillment of **any** condition triggers an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| avgReadWriteLatency | integer | Read/write latency is higher than *X* milliseconds in 4 out of 5 samples. | Required |
| peakReadWriteLatency | integer | Peak value for read/write latency is higher than *X* milliseconds in 4 out of 5 samples. | Required |

#### The `UndersizedStorageDetectionConfig` object

Undersized storage device detection cofing

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [UndersizedStorageThresholds](#openapi-definition-UndersizedStorageThresholds) | Custom thresholds for undersized storage device. If not set then the automatic mode is used.  Fulfillment of **any** condition triggers an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `UndersizedStorageThresholds` object

Custom thresholds for undersized storage device. If not set then the automatic mode is used.

Fulfillment of **any** condition triggers an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| averageQueueCommandLatency | integer | Average queue command latency is higher than *X* milliseconds in 3 out of 5 samples. | Required |
| peakQueueCommandLatency | integer | Peak queue command latency is higher than *X* milliseconds in 3 out of 5 samples. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"droppedPacketsDetection": {



"customThresholds": {



"droppedPacketsPerSecond": 4



},



"enabled": true



},



"esxiHighCpuSaturation": {



"customThresholds": {



"cpuPeakPercentage": 90,



"cpuUsagePercentage": 80,



"vmCpuReadyPercentage": 10



},



"enabled": true



},



"esxiHighMemoryDetection": {



"customThresholds": {



"compressionDecompressionRate": 120



},



"enabled": true



},



"lowDatastoreSpaceDetection": {



"customThresholds": {



"freeSpacePercentage": 5



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



"overloadedStorageDetection": {



"customThresholds": {



"commandAbortsNumber": 1



},



"enabled": true



},



"slowPhysicalStorageDetection": {



"customThresholds": {



"avgReadWriteLatency": 150,



"peakReadWriteLatency": 400



},



"enabled": true



},



"undersizedStorageDetection": {



"customThresholds": {



"averageQueueCommandLatency": 15,



"peakQueueCommandLatency": 160



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
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

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

In this example, the request updates the configuration of anomaly detection for VMware from the [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/get-config#example "Read the configuration of anomaly detection for VMware via the Dynatrace API.") example. It changes **Detect CPU saturation ESXi host** mode to **based on custom thresholds** and sets the following thresholds:

* Alert if CPU usage is higher than **90**%
* AND VM CPU ready is higher than **12**%
* AND at least one peak higher than **98**% occurred in **3** out of **5** samples.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to create a backup copy of your current configuration with the **GET VMware anomaly detection configuration** call.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/vmware \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"esxiHighCpuSaturation": {



"enabled": true,



"customThresholds": {



"cpuUsagePercentage": 90,



"vmCpuReadyPercentage": 12,



"cpuPeakPercentage": 98



}



},



"esxiHighMemoryDetection": {



"enabled": true



},



"overloadedStorageDetection": {



"enabled": true



},



"undersizedStorageDetection": {



"enabled": true



},



"slowPhysicalStorageDetection": {



"enabled": true



},



"droppedPacketsDetection": {



"enabled": true



},



"lowDatastoreSpaceDetection": {



"enabled": true



}



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/vmware
```

#### Request body

```
{



"esxiHighCpuSaturation": {



"enabled": true,



"customThresholds": {



"cpuUsagePercentage": 90,



"vmCpuReadyPercentage": 12,



"cpuPeakPercentage": 98



}



},



"esxiHighMemoryDetection": {



"enabled": true



},



"overloadedStorageDetection": {



"enabled": true



},



"undersizedStorageDetection": {



"enabled": true



},



"slowPhysicalStorageDetection": {



"enabled": true



},



"droppedPacketsDetection": {



"enabled": true



},



"lowDatastoreSpaceDetection": {



"enabled": true



}



}
```

#### Response code

204

#### Result

The updated configuration has the following parameters:

![Anomaly detection config - vmware - updated](https://dt-cdn.net/images/anomaly-detectoin-vmware-upd-635-ebbe59a210.png)

Anomaly detection config - vmware - updated

## Related topics

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.")
* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")