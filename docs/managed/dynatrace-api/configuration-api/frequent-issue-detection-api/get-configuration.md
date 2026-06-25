---
title: Frequent issue detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/frequent-issue-detection-api/get-configuration
scraped: 2026-05-12T12:35:22.204661
---

# Frequent issue detection API - GET configuration

# Frequent issue detection API - GET configuration

* Reference
* Published Jun 28, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`) schema.

Gets the configuration of frequent issue detection. To learn more about it, see [Detection of frequent issues](/managed/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues "Understand how Dynatrace detects and manages recurring problem patterns as frequent issues.").

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [FrequentIssueDetectionConfig](#openapi-definition-FrequentIssueDetectionConfig) | Success |

### Response body objects

#### The `FrequentIssueDetectionConfig` object

Parameters of the frequent issue detection. To learn more about it, see [Detection of frequent issuesï»¿](https://dt-url.net/4da3kdg) in Dynatrace Documentation.

| Element | Type | Description |
| --- | --- | --- |
| frequentIssueDetectionApplicationEnabled | boolean | The detection for applications is enabled (`true`) or disabled (`false`). |
| frequentIssueDetectionEnvironmentEnabled | boolean | The detection for environment is enabled (`true`) or disabled (`false`). |
| frequentIssueDetectionInfrastructureEnabled | boolean | The detection for infrastructure is enabled (`true`) or disabled (`false`). |
| frequentIssueDetectionServiceEnabled | boolean | The detection for services is enabled (`true`) or disabled (`false`). |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

### Response body JSON models

```
{



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionEnvironmentEnabled": false,



"frequentIssueDetectionInfrastructureEnabled": true,



"frequentIssueDetectionServiceEnabled": true



}
```

## Example

In this example, the request lists the current configuration of frequent issue detection.

The API token is passed in the **Authorization** header.

The configuration has the following settings:

![Anomaly detection configuration](https://dt-cdn.net/images/get-frequent-issue-704-93f6d04ce3.png)

Anomaly detection configuration

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/config/v1/frequentIssueDetection' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/frequentIssueDetection
```

#### Response body

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.194.0.20200427-192742"



},



"frequentIssueDetectionApplicationEnabled": false,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": false



}
```

#### Response code

200

## Related topics

* [Detection of frequent issues](/managed/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues "Understand how Dynatrace detects and manages recurring problem patterns as frequent issues.")