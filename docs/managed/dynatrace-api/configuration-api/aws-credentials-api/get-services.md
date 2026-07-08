---
title: AWS credentials API - GET monitored services
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-credentials-api/get-services
---

# AWS credentials API - GET monitored services

# AWS credentials API - GET monitored services

* Reference
* Published Jul 28, 2022

Lists AWS services that are monitored by an AWS configuration.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/credentials/{id}/services` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the specified AWS credentials configuration. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AwsMonitoredServicesDto](#openapi-definition-AwsMonitoredServicesDto) | Success |

### Response body objects

#### The `AwsMonitoredServicesDto` object

| Element | Type | Description |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| services | [AwsSupportingServiceConfig](#openapi-definition-AwsSupportingServiceConfig)[] | A list of AWS services to be monitored. Available services are listed by [/aws/supportedServices﻿](https://dt-url.net/me02sh2) operation.  For each service, a list of metrics and dimensions can be specified. A list of supported metrics and dimensions for a given service can be checked in [documentation﻿](https://dt-url.net/r12v0pkl).  List of metrics can be skipped (set to null), resulting in recommended (default) set of metrics and dimensions being chosen for monitoring. For built-in services, adjusting the list of metrics is not supported, therefore it needs to be null. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `AwsSupportingServiceConfig` object

A service to be monitored.

| Element | Type | Description |
| --- | --- | --- |
| monitoredMetrics | [AwsSupportingServiceMetric](#openapi-definition-AwsSupportingServiceMetric)[] | A list of metrics to be monitored for this service. If the list is null then recommended list of metrics for this service will be monitored. |
| name | string | The name of the service. Valid supported service names can be discovered using /aws/supportedServices restAPI |

#### The `AwsSupportingServiceMetric` object

A metric of service to be monitored.

| Element | Type | Description |
| --- | --- | --- |
| dimensions | string[] | A list of metric's dimensions names. |
| name | string | The name of the metric of the service. |
| statistic | string | The statistic (aggregation) to be used for the metric. AVG\_MIN\_MAX value is 3 statistics at once: AVERAGE, MINIMUM and MAXIMUM The element can hold these values * `AVERAGE` * `AVG_MIN_MAX` * `MAXIMUM` * `MINIMUM` * `SAMPLE_COUNT` * `SUM` |

### Response body JSON models

```
{



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"services": [



{



"monitoredMetrics": [



{



"dimensions": [



"string"



],



"name": "string",



"statistic": "AVERAGE"



}



],



"name": "string"



}



]



}
```