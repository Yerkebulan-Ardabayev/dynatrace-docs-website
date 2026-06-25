---
title: VMware anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-vmware/get-config
scraped: 2026-05-12T11:19:07.321418
---

# VMware anomaly detection API - GET configuration

# VMware anomaly detection API - GET configuration

* Reference
* Published Aug 28, 2019

Gets the configuration of anomaly detection for VMware.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/vmware` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [VMwareAnomalyDetectionConfig](#openapi-definition-VMwareAnomalyDetectionConfig) | Success |

### Response body objects

#### The `VMwareAnomalyDetectionConfig` object

The configuration of the anomaly detection for VMware.

| Element | Type | Description |
| --- | --- | --- |
| droppedPacketsDetection | [DroppedPacketsDetectionConfig](#openapi-definition-DroppedPacketsDetectionConfig) | The configuration of the high number of dropped packets detection. |
| esxiHighCpuSaturation | [EsxiHighCpuSaturationConfig](#openapi-definition-EsxiHighCpuSaturationConfig) | The configuration of the CPU saturation on ESXi host detection. |
| esxiHighMemoryDetection | [EsxiHighMemoryDetectionConfig](#openapi-definition-EsxiHighMemoryDetectionConfig) | The configuration of the memory saturation on ESXi host detection. |
| guestCpuLimitReached | [GuestCPULimitReachedConfig](#openapi-definition-GuestCPULimitReachedConfig) | The configuration of the guest CPU limit reached configuration detection. |
| lowDatastoreSpaceDetection | [LowDatastoreSpaceDetectionConfig](#openapi-definition-LowDatastoreSpaceDetectionConfig) | The configuraiton of the low datastore free space detection. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| overloadedStorageDetection | [OverloadedStorageDetectionConfig](#openapi-definition-OverloadedStorageDetectionConfig) | The cofiguration of the overloaded storage on physical storage device detection. |
| slowPhysicalStorageDetection | [SlowPhysicalStorageDetectionConfig](#openapi-definition-SlowPhysicalStorageDetectionConfig) | The configuraiton of the physical storage device running slow detection. |
| undersizedStorageDetection | [UndersizedStorageDetectionConfig](#openapi-definition-UndersizedStorageDetectionConfig) | Undersized storage device detection cofing |

#### The `DroppedPacketsDetectionConfig` object

The configuration of the high number of dropped packets detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [DroppedPacketsThresholds](#openapi-definition-DroppedPacketsThresholds) | Custom thresholds for high number of dropped packets. If not set then the automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `DroppedPacketsThresholds` object

Custom thresholds for high number of dropped packets. If not set then the automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| droppedPacketsPerSecond | integer | Alert if receive/transmit dropped packets rate on NIC is higher than *X* packets per second in 3 out of 5 samples. |

#### The `EsxiHighCpuSaturationConfig` object

The configuration of the CPU saturation on ESXi host detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [EsxiHighCpuThresholds](#openapi-definition-EsxiHighCpuThresholds) | Custom thresholds for CPU saturation detection on ESXi. If not set then the automatic mode is used.  **All** conditions must be fulfilled to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `EsxiHighCpuThresholds` object

Custom thresholds for CPU saturation detection on ESXi. If not set then the automatic mode is used.

**All** conditions must be fulfilled to trigger an alert.

| Element | Type | Description |
| --- | --- | --- |
| cpuPeakPercentage | integer | At least one peak higher than *X*% occurred in 3 out of 5 samples. |
| cpuUsagePercentage | integer | CPU usage is higher than *X*% in 3 out of 5 samples. |
| vmCpuReadyPercentage | integer | VM CPU ready is higher than *X*% in 3 out of 5 samples. |

#### The `EsxiHighMemoryDetectionConfig` object

The configuration of the memory saturation on ESXi host detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [EsxiHighMemoryThresholds](#openapi-definition-EsxiHighMemoryThresholds) | Custom thresholds for memory saturation on ESXi host. If not set then the automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `EsxiHighMemoryThresholds` object

Custom thresholds for memory saturation on ESXi host. If not set then the automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| compressionDecompressionRate | number | Alert if ESXi host swap IN/OUT or compression/decompression rate is higher *X* kilobytes per second in 3 out of 5 samples. |

#### The `GuestCPULimitReachedConfig` object

The configuration of the guest CPU limit reached configuration detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [GuestCPULimitThresholds](#openapi-definition-GuestCPULimitThresholds) | Custom thresholds for guest CPU limit detection. If not set then the automatic mode is used.  **All** conditions must be fulfilled to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `GuestCPULimitThresholds` object

Custom thresholds for guest CPU limit detection. If not set then the automatic mode is used.

**All** conditions must be fulfilled to trigger an alert.

| Element | Type | Description |
| --- | --- | --- |
| hostCpuUsageMinPercentage | integer | Hypervisor CPU usage is higher than *X*% in 3 out of 5 samples. |
| vmCpuReadyMaxPercentage | integer | VM CPU ready is higher than *X*% occurred in 3 out of 5 samples. |
| vmCpuUsageMaxPercentage | integer | VM CPU usage (VM CPU Usage Mhz / VM CPU limit in Mhz) is higher than *X*% in 3 out of 5 samples. |

#### The `LowDatastoreSpaceDetectionConfig` object

The configuraiton of the low datastore free space detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [LowDatastoreSpaceThresholds](#openapi-definition-LowDatastoreSpaceThresholds) | Custom thresholds for low datastore free space. If not set then the automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `LowDatastoreSpaceThresholds` object

Custom thresholds for low datastore free space. If not set then the automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| freeSpacePercentage | integer | Alert if datastore free space is lower than *X*%. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `OverloadedStorageDetectionConfig` object

The cofiguration of the overloaded storage on physical storage device detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [OverloadedStorageThresholds](#openapi-definition-OverloadedStorageThresholds) | Custom thresholds for overloaded storage on physical storage device. If not set then the automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `OverloadedStorageThresholds` object

Custom thresholds for overloaded storage on physical storage device. If not set then the automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| commandAbortsNumber | integer | Alert if number of command aborts is higher than *X* in 3 out of 5 samples. |

#### The `SlowPhysicalStorageDetectionConfig` object

The configuraiton of the physical storage device running slow detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [SlowPhysicalStorageThresholds](#openapi-definition-SlowPhysicalStorageThresholds) | Custom thresholds for slow running physical storage device. If not set then the automatic mode is used.  Fulfillment of **any** condition triggers an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `SlowPhysicalStorageThresholds` object

Custom thresholds for slow running physical storage device. If not set then the automatic mode is used.

Fulfillment of **any** condition triggers an alert.

| Element | Type | Description |
| --- | --- | --- |
| avgReadWriteLatency | integer | Read/write latency is higher than *X* milliseconds in 4 out of 5 samples. |
| peakReadWriteLatency | integer | Peak value for read/write latency is higher than *X* milliseconds in 4 out of 5 samples. |

#### The `UndersizedStorageDetectionConfig` object

Undersized storage device detection cofing

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [UndersizedStorageThresholds](#openapi-definition-UndersizedStorageThresholds) | Custom thresholds for undersized storage device. If not set then the automatic mode is used.  Fulfillment of **any** condition triggers an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `UndersizedStorageThresholds` object

Custom thresholds for undersized storage device. If not set then the automatic mode is used.

Fulfillment of **any** condition triggers an alert.

| Element | Type | Description |
| --- | --- | --- |
| averageQueueCommandLatency | integer | Average queue command latency is higher than *X* milliseconds in 3 out of 5 samples. |
| peakQueueCommandLatency | integer | Peak queue command latency is higher than *X* milliseconds in 3 out of 5 samples. |

### Response body JSON models

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

## Example

In this example, the request lists the current configuration of anomaly detection for VMware.

The API token is passed in the **Authorization** header.

The configuration has the following settings:

![Anomaly detection config - vmware](https://dt-cdn.net/images/anomaly-detectoin-vmware-576-2d28cdf057.png)

Anomaly detection config - vmware

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/vmware \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/vmware
```

#### Response body

```
{



"metadata": {



"clusterVersion": "1.164.0.20190204-124711",



"configurationVersions": [



1



]



},



"esxiHighCpuSaturation": {



"enabled": true



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

200

## Related topics

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.")
* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")