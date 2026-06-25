---
title: Azure credentials API - GET monitored services
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/azure-credentials-api/get-services
scraped: 2026-05-12T11:16:32.256513
---

# Azure credentials API - GET monitored services

# Azure credentials API - GET monitored services

* Reference
* Published Jul 28, 2022

Lists Azure services that are monitored by an Azure configuration.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/azure/credentials/{id}/services` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required Azure credentials configuration. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AzureMonitoredServicesDto](#openapi-definition-AzureMonitoredServicesDto) | Success |

### Response body objects

#### The `AzureMonitoredServicesDto` object

| Element | Type | Description |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| services | [AzureSupportingService[]](#openapi-definition-AzureSupportingService) | A list of Azure services to be monitored. Available services are listed by [/azure/supportedServicesï»¿](https://dt-url.net/wt42sdq) operation.  For each service, a list of metrics and dimensions can be specified. A list of supported metrics and dimensions for a given service can be checked in [documentationï»¿](https://dt-url.net/kx2351b).  List of metrics can be skipped (set to null), resulting in recommended (default) set of metrics and dimensions being chosen for monitoring. For built-in services, adjusting the list of metrics is not supported, therefore it needs to be null. |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

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



"name": "string"



}



],



"name": "string"



}



]



}
```

## Related topics

* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")