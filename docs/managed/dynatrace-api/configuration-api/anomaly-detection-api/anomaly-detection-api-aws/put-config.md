---
title: AWS anomaly detection API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/put-config
scraped: 2026-05-12T11:16:39.773820
---

# AWS anomaly detection API - PUT configuration

# AWS anomaly detection API - PUT configuration

* Reference
* Published Aug 28, 2019

Updates the configuration of anomaly detection for AWS.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [AwsAnomalyDetectionConfig](#openapi-definition-AwsAnomalyDetectionConfig) | JSON body of the request, containing parameters of the AWS anomaly detection configuration. | body | Optional |

### Request body objects

#### The `AwsAnomalyDetectionConfig` object

The configuration of anomaly detection for AWS.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| ec2CandidateCpuSaturationDetection | [Ec2CandidateCpuSaturationDetectionConfig](#openapi-definition-Ec2CandidateCpuSaturationDetectionConfig) | The configuration of the high CPU saturation on EC2 without installed agent (monitoring candidate). If null, then this configuration won't be changed. | Optional |
| elbHighConnectionErrorsDetection | [ElbHighConnectionErrorsDetectionConfig](#openapi-definition-ElbHighConnectionErrorsDetectionConfig) | The configuration of the high number of backend connection errors on ELB detection. | Required |
| lambdaHighErrorRateDetection | [LambdaHighErrorRateDetectionConfig](#openapi-definition-LambdaHighErrorRateDetectionConfig) | The configuration of the AWS Lambda high error rate detection. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| rdsHighCpuDetection | [RdsHighCpuDetectionConfig](#openapi-definition-RdsHighCpuDetectionConfig) | The configuration of the high CPU utilization on RDS detection. | Required |
| rdsHighMemoryDetection | [RdsHighMemoryDetectionConfig](#openapi-definition-RdsHighMemoryDetectionConfig) | The configuration of RDS running out of memory detection. | Required |
| rdsHighWriteReadLatencyDetection | [RdsHighWriteReadLatencyDetectionConfig](#openapi-definition-RdsHighWriteReadLatencyDetectionConfig) | The configuration of the high RDS write/read latency detection. | Required |
| rdsLowStorageDetection | [RdsLowStorageDetectionConfig](#openapi-definition-RdsLowStorageDetectionConfig) | The configuration of the low free storage space on RDS detection. | Required |
| rdsRestartsSequenceDetection | [RdsRestartsSequenceDetectionConfig](#openapi-definition-RdsRestartsSequenceDetectionConfig) | The configuration of the restarts sequence on RDS detection. | Required |

#### The `Ec2CandidateCpuSaturationDetectionConfig` object

The configuration of the high CPU saturation on EC2 without installed agent (monitoring candidate). If null, then this configuration won't be changed.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [Ec2CandidateCpuSaturationThresholds](#openapi-definition-Ec2CandidateCpuSaturationThresholds) | Custom thresholds for high CPU saturation on EC2 monitoring candidate. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `Ec2CandidateCpuSaturationThresholds` object

Custom thresholds for high CPU saturation on EC2 monitoring candidate. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| cpuUsagePercentage | integer | Alert if CPU usage is higher than *X*% in 3 out of 5 samples. | Required |

#### The `ElbHighConnectionErrorsDetectionConfig` object

The configuration of the high number of backend connection errors on ELB detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [ElbHighConnectionErrorsThresholds](#openapi-definition-ElbHighConnectionErrorsThresholds) | Custom thresholds for high number of backend connection errors on ELB. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `ElbHighConnectionErrorsThresholds` object

Custom thresholds for high number of backend connection errors on ELB. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| connectionErrorsPerMinute | integer | Alert if number of backend connection errors is higher than *X* per minute in 3 out of 5 samples. | Required |

#### The `LambdaHighErrorRateDetectionConfig` object

The configuration of the AWS Lambda high error rate detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [LambdaHighErrorRateThresholds](#openapi-definition-LambdaHighErrorRateThresholds) | Custom thresholds for AWS Lambda high error rate. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `LambdaHighErrorRateThresholds` object

Custom thresholds for AWS Lambda high error rate. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| failedInvocationsRate | integer | Alert if failed invocations rate is higher than *X*% in 3 out of 5 samples. | Required |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `RdsHighCpuDetectionConfig` object

The configuration of the high CPU utilization on RDS detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [RdsHighCpuThresholds](#openapi-definition-RdsHighCpuThresholds) | Custom thresholds for high CPU utilization on RDS. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `RdsHighCpuThresholds` object

Custom thresholds for high CPU utilization on RDS. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| cpuUsagePercentage | integer | Alert if CPU usage is higher than *X*% in 3 out of 5 samples. | Required |

#### The `RdsHighMemoryDetectionConfig` object

The configuration of RDS running out of memory detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [RdsHighMemoryThresholds](#openapi-definition-RdsHighMemoryThresholds) | Custom thresholds for RDS running out of memory. If not set, automatic mode is used.  **All** conditions must be fulfilled to trigger an alert. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `RdsHighMemoryThresholds` object

Custom thresholds for RDS running out of memory. If not set, automatic mode is used.

**All** conditions must be fulfilled to trigger an alert.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| freeMemory | number | Freeable memory is lower than *X* Megabytes in 3 out of 5 samples. | Required |
| swapUsage | number | Swap usage is higher than *X* Gigabytes in 3 out of 5 samples. | Required |

#### The `RdsHighWriteReadLatencyDetectionConfig` object

The configuration of the high RDS write/read latency detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [RdsHighLatencyThresholds](#openapi-definition-RdsHighLatencyThresholds) | Custom thresholds for high RDS write/read latency. If not set, automatic mode is used | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `RdsHighLatencyThresholds` object

Custom thresholds for high RDS write/read latency. If not set, automatic mode is used

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| writeReadLatency | integer | Alert if read/write latency is higher than *X* milliseconds in 3 out of 5 samples. | Required |

#### The `RdsLowStorageDetectionConfig` object

The configuration of the low free storage space on RDS detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [RdsLowStorageThresholds](#openapi-definition-RdsLowStorageThresholds) | Custom thresholds for low free storage space on RDS. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `RdsLowStorageThresholds` object

Custom thresholds for low free storage space on RDS. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| freeStoragePercentage | integer | Alert if free storage space divided by allocated storage is lower than *X*% in 3 out of 5 samples. | Required |

#### The `RdsRestartsSequenceDetectionConfig` object

The configuration of the restarts sequence on RDS detection.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customThresholds | [RdsRestartsThresholds](#openapi-definition-RdsRestartsThresholds) | Custom thresholds for restarts sequence on RDS. If not set, automatic mode is used. | Optional |
| enabled | boolean | The detection is enabled (`true`) or disabled (`false`). | Required |

#### The `RdsRestartsThresholds` object

Custom thresholds for restarts sequence on RDS. If not set, automatic mode is used.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| restartsPerMinute | integer | Alert if number of restarts is *X* per minute or higher in 3 out of 20 samples. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/anomalyDetection/aws/validator` |

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

In this example, the request updates the configuration of anomaly detection for AWS from the [GET request](/managed/dynatrace-api/configuration-api/anomaly-detection-api/anomaly-detection-api-aws/get-config#example "Read the configuration of anomaly detection for AWS via the Dynatrace API.") example. It switches **high CPU utilization on RDS detection** to **custom threshold** mode and sets a threshold of **90**%. It also disables **RDS running out of memory detection**.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to create a backup copy of your current configuration with the **GET AWS anomaly detection configuration** call.

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

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/anomalyDetection/aws
```

#### Request body

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

#### Response code

204

#### Result

The updated configuration has the following parameters:

![Anomaly detection config - AWS - updated](https://dt-cdn.net/images/anomaly-detecion-aws-upd-688-f0ba72cfb8.png)

Anomaly detection config - AWS - updated

## Related topics

* [Adjust the sensitivity of anomaly detection for infrastructure](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-infastructure "Adjust problem detection sensitivity for infrastructure.")
* [DavisÂ® AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.")