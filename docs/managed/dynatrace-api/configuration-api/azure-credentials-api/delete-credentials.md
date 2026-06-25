---
title: Azure credentials API - DELETE credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/delete-credentials
scraped: 2026-05-12T11:16:36.595837
---

# Azure credentials API - DELETE credentials

# Azure credentials API - DELETE credentials

* Reference
* Published Feb 25, 2020

Deletes the specified Azure credentials configuration. You can't undo a deletion.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required Azure credentials configuration. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AzureCredentials](#openapi-definition-AzureCredentials) | Success |

### Response body objects

#### The `AzureCredentials` object

Configuration of Azure app-level credentials.

| Element | Type | Description |
| --- | --- | --- |
| active | boolean | The monitoring is enabled (`true`) or disabled (`false`).  If not set on creation, the `true` value is used.  If the field is omitted during an update, the old value remains unaffected. |
| appId | string | The application ID (also referred to as client ID).  The field is **required** when creating a new credentials configuration.  The field is ignored during an update, the old value remains unaffected. |
| autoTagging | boolean | The automatic capture of Azure tags is on (`true`) or off (`false`). |
| directoryId | string | The directory ID (also referred to as tenant ID).  The field is **required** when creating a new credentials configuration.  The field is ignored during an update, the old value remains unaffected. |
| id | string | The Dynatrace entity ID of the Azure credentials configuration. |
| key | string | The secret key associated with the application ID.  For security reasons, GET requests return this field as `null`.  Submit your key on creation or update of the configuration.  The field is **required** when creating a new credentials configuration. If the field is omitted during an update, the old value remains unaffected. |
| label | string | The unique name of the Azure credentials configuration.  Allowed characters are letters, numbers, and spaces. Also the special characters `.+-_` are allowed. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| monitorOnlyExcludingTagPairs | [CloudTag[]](#openapi-definition-CloudTag) | A list of Azure tags to be excluded from monitoring.  You can specify up to 20 tags. A resource tagged with *any* of the specified tags will not be monitored.  Only applicable when the **monitorOnlyTaggedEntities** parameter is set to `true`. |
| monitorOnlyTagPairs | [CloudTag[]](#openapi-definition-CloudTag) | A list of Azure tags to be monitored.  You can specify up to 20 tags. A resource tagged with *any* of the specified tags is monitored.  Only applicable when the **monitorOnlyTaggedEntities** parameter is set to `true`. |
| monitorOnlyTaggedEntities | boolean | Monitor only resources that have specified Azure tags (`true`) or all resources (`false`). |
| supportingServices | [AzureSupportingService[]](#openapi-definition-AzureSupportingService) | **Deprecated**. To manage services use [/azure/credentials/{id}/servicesï»¿](https://dt-url.net/1w62s27) operation. Built-in services are not supported here.  A list of Azure services to be monitored. Available services are listed by [/azure/supportedServicesï»¿](https://dt-url.net/wt42sdq) operation.  For each service, a list of metrics and dimensions can be specified. A list of supported metrics and dimensions for a given service can be checked in [documentationï»¿](https://dt-url.net/kx2351b).  List of metrics can be skipped (set to null), resulting in recommended (default) set of metrics and dimensions being chosen for monitoring. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `CloudTag` object

A cloud tag.

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the tag. |
| value | string | The value of the tag.  If set to `null` or `""`, then resources with any value of the tag are monitored. |

#### The `AzureSupportingService` object

A service to be monitored.

| Element | Type | Description |
| --- | --- | --- |
| monitoredMetrics | [AzureMonitoredMetric[]](#openapi-definition-AzureMonitoredMetric) | A list of metrics to be monitored for this service. It must include all the recommended metrics. If the list is null then recommended list of metrics for this service will be monitored. |
| name | string | The name of the service. Valid supported service names can be discovered using /azure/supportedServices restAPI |

#### The `AzureMonitoredMetric` object

A metric of service to be monitored.

| Element | Type | Description |
| --- | --- | --- |
| dimensions | string[] | A list of metric's dimensions names. It must include all the recommended dimensions. |
| name | string | The name of the metric of the service. |

### Response body JSON models

```
{



"active": true,



"appId": "string",



"autoTagging": true,



"directoryId": "string",



"id": "string",



"key": "string",



"label": "string",



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



"monitorOnlyExcludingTagPairs": [



{



"name": "string",



"value": "string"



}



],



"monitorOnlyTagPairs": [



{}



],



"monitorOnlyTaggedEntities": true,



"supportingServices": [



{



"monitoredMetrics": [



{



"dimensions": [



"string"



],



"name": "string"



}



],



"name": "string"



}



]



}
```

## Example

In this example, the request deletes Azure app-level credentials from the [POST request example](/managed/dynatrace-api/configuration-api/azure-credentials-api/post-new-credentials#example "Create an Azure credentials configuration via the Dynatrace API."). The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/azure/credentials/AZURE_CREDENTIALS-357FDA338DAAF338
```

#### Response code

204

## Related topics

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")