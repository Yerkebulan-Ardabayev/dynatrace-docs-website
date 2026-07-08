---
title: AWS anomaly detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/get-config
---

# AWS anomaly detection API - GET configuration

# AWS anomaly detection API - GET configuration

* Reference
* Published Aug 28, 2019

Gets the configuration of anomaly detection for AWS.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AwsAnomalyDetectionConfig](#openapi-definition-AwsAnomalyDetectionConfig) | Success |

### Response body objects

#### The `AwsAnomalyDetectionConfig` object

The configuration of anomaly detection for AWS.

| Element | Type | Description |
| --- | --- | --- |
| ec2CandidateCpuSaturationDetection | [Ec2CandidateCpuSaturationDetectionConfig](#openapi-definition-Ec2CandidateCpuSaturationDetectionConfig) | The configuration of the high CPU saturation on EC2 without installed agent (monitoring candidate). If null, then this configuration won't be changed. |
| elbHighConnectionErrorsDetection | [ElbHighConnectionErrorsDetectionConfig](#openapi-definition-ElbHighConnectionErrorsDetectionConfig) | The configuration of the high number of backend connection errors on ELB detection. |
| lambdaHighErrorRateDetection | [LambdaHighErrorRateDetectionConfig](#openapi-definition-LambdaHighErrorRateDetectionConfig) | The configuration of the AWS Lambda high error rate detection. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| rdsHighCpuDetection | [RdsHighCpuDetectionConfig](#openapi-definition-RdsHighCpuDetectionConfig) | The configuration of the high CPU utilization on RDS detection. |
| rdsHighMemoryDetection | [RdsHighMemoryDetectionConfig](#openapi-definition-RdsHighMemoryDetectionConfig) | The configuration of RDS running out of memory detection. |
| rdsHighWriteReadLatencyDetection | [RdsHighWriteReadLatencyDetectionConfig](#openapi-definition-RdsHighWriteReadLatencyDetectionConfig) | The configuration of the high RDS write/read latency detection. |
| rdsLowStorageDetection | [RdsLowStorageDetectionConfig](#openapi-definition-RdsLowStorageDetectionConfig) | The configuration of the low free storage space on RDS detection. |
| rdsRestartsSequenceDetection | [RdsRestartsSequenceDetectionConfig](#openapi-definition-RdsRestartsSequenceDetectionConfig) | The configuration of the restarts sequence on RDS detection. |

#### The `Ec2CandidateCpuSaturationDetectionConfig` object

The configuration of the high CPU saturation on EC2 without installed agent (monitoring candidate). If null, then this configuration won't be changed.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [Ec2CandidateCpuSaturationThresholds](#openapi-definition-Ec2CandidateCpuSaturationThresholds) | Custom thresholds for high CPU saturation on EC2 monitoring candidate. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `Ec2CandidateCpuSaturationThresholds` object

Custom thresholds for high CPU saturation on EC2 monitoring candidate. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| cpuUsagePercentage | integer | Alert if CPU usage is higher than *X*% in 3 out of 5 samples. |

#### The `ElbHighConnectionErrorsDetectionConfig` object

The configuration of the high number of backend connection errors on ELB detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [ElbHighConnectionErrorsThresholds](#openapi-definition-ElbHighConnectionErrorsThresholds) | Custom thresholds for high number of backend connection errors on ELB. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `ElbHighConnectionErrorsThresholds` object

Custom thresholds for high number of backend connection errors on ELB. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| connectionErrorsPerMinute | integer | Alert if number of backend connection errors is higher than *X* per minute in 3 out of 5 samples. |

#### The `LambdaHighErrorRateDetectionConfig` object

The configuration of the AWS Lambda high error rate detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [LambdaHighErrorRateThresholds](#openapi-definition-LambdaHighErrorRateThresholds) | Custom thresholds for AWS Lambda high error rate. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `LambdaHighErrorRateThresholds` object

Custom thresholds for AWS Lambda high error rate. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| failedInvocationsRate | integer | Alert if failed invocations rate is higher than *X*% in 3 out of 5 samples. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `RdsHighCpuDetectionConfig` object

The configuration of the high CPU utilization on RDS detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [RdsHighCpuThresholds](#openapi-definition-RdsHighCpuThresholds) | Custom thresholds for high CPU utilization on RDS. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `RdsHighCpuThresholds` object

Custom thresholds for high CPU utilization on RDS. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| cpuUsagePercentage | integer | Alert if CPU usage is higher than *X*% in 3 out of 5 samples. |

#### The `RdsHighMemoryDetectionConfig` object

The configuration of RDS running out of memory detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [RdsHighMemoryThresholds](#openapi-definition-RdsHighMemoryThresholds) | Custom thresholds for RDS running out of memory. If not set, automatic mode is used.  **All** conditions must be fulfilled to trigger an alert. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `RdsHighMemoryThresholds` object

Custom thresholds for RDS running out of memory. If not set, automatic mode is used.

**All** conditions must be fulfilled to trigger an alert.

| Element | Type | Description |
| --- | --- | --- |
| freeMemory | number | Freeable memory is lower than *X* Megabytes in 3 out of 5 samples. |
| swapUsage | number | Swap usage is higher than *X* Gigabytes in 3 out of 5 samples. |

#### The `RdsHighWriteReadLatencyDetectionConfig` object

The configuration of the high RDS write/read latency detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [RdsHighLatencyThresholds](#openapi-definition-RdsHighLatencyThresholds) | Custom thresholds for high RDS write/read latency. If not set, automatic mode is used |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `RdsHighLatencyThresholds` object

Custom thresholds for high RDS write/read latency. If not set, automatic mode is used

| Element | Type | Description |
| --- | --- | --- |
| writeReadLatency | integer | Alert if read/write latency is higher than *X* milliseconds in 3 out of 5 samples. |

#### The `RdsLowStorageDetectionConfig` object

The configuration of the low free storage space on RDS detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [RdsLowStorageThresholds](#openapi-definition-RdsLowStorageThresholds) | Custom thresholds for low free storage space on RDS. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `RdsLowStorageThresholds` object

Custom thresholds for low free storage space on RDS. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| freeStoragePercentage | integer | Alert if free storage space divided by allocated storage is lower than *X*% in 3 out of 5 samples. |

#### The `RdsRestartsSequenceDetectionConfig` object

The configuration of the restarts sequence on RDS detection.

| Element | Type | Description |
| --- | --- | --- |
| customThresholds | [RdsRestartsThresholds](#openapi-definition-RdsRestartsThresholds) | Custom thresholds for restarts sequence on RDS. If not set, automatic mode is used. |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). |

#### The `RdsRestartsThresholds` object

Custom thresholds for restarts sequence on RDS. If not set, automatic mode is used.

| Element | Type | Description |
| --- | --- | --- |
| restartsPerMinute | integer | Alert if number of restarts is *X* per minute or higher in 3 out of 20 samples. |

### Response body JSON models

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

## Example

In this example, the request lists the current configuration of anomaly detection for AWS.

The API token is passed in the **Authorization** header.

The configuration has the following settings:

![Anomaly detection config - AWS](https://dt-cdn.net/images/anomaly-detecion-aws-573-880e8e55e6.png)

Anomaly detection config - AWS

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/aws \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/aws
```

#### Response body

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

#### Response code

200

## Related topics

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.")
* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")