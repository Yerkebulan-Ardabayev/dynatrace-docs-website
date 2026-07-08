---
title: GET cluster license and billed usage
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-license/get-cluster-license-usage
---

# GET cluster license and billed usage

# GET cluster license and billed usage

* Reference
* Updated on Mar 06, 2026

Dynatrace Managed version 1.326+

Get cluster license details and billed usage.

* This API is only compatible with Dynatrace classic licensing.
* Returned billed data only contains usage from the current contact.
* Billed usage is delayed by about 2 hours compared to current usage.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/clusterLicense`

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ClusterLicense](#openapi-definition-ClusterLicense) | Successful operation. |

### Response body objects

#### The `ClusterLicense` object

| Element | Type | Description |
| --- | --- | --- |
| accountName | string | Account name |
| clusterId | string | Cluster ID |
| contactEmailAddress | string | Contact email address |
| lastBillingTime | string | Last time when billing data was refreshed |
| licenseExpirationTime | string | License expiration date |
| licenseKey | string | License key |
| licenseName | string | License name |
| licenseStatus | string | License status |
| licenseType | string | License type |
| productVersion | string | Current version |
| usageOfDduUnits | [LicenseUsageOfUnit](#openapi-definition-LicenseUsageOfUnit) | Cluster license usage of Davis data units (DDU) |
| usageOfDemUnits | [LicenseUsageOfUnit](#openapi-definition-LicenseUsageOfUnit) | Cluster license usage of Davis data units (DDU) |
| usageOfHostUnits | [LicenseUsageOfUnit](#openapi-definition-LicenseUsageOfUnit) | Cluster license usage of Davis data units (DDU) |

#### The `LicenseUsageOfUnit` object

Cluster license usage of Davis data units (DDU)

| Element | Type | Description |
| --- | --- | --- |
| overageUsage | [OverageUsageOfUnit](#openapi-definition-OverageUsageOfUnit) | Overage usage if applicable |
| quota | integer | Cluster license quota |
| remaining | number | Remaining usage of quota |
| remainingPercent | number | Remaining usage of quota as percentage |
| usage | number | Current usage of quota |
| usagePercent | number | Current usage of quota as percentage |
| usageStatus | string | Current status of license usage The element can hold these values * `OVERAGE_QUOTA_REACHED` * `QUOTA_REACHED` * `USING_OVERAGE` * `USING_QUOTA` |

#### The `OverageUsageOfUnit` object

Overage usage if applicable

| Element | Type | Description |
| --- | --- | --- |
| overageQuota | integer | Overage quota if set, null if not |
| overageUsage | number | Overage used |
| overageUsagePercent | number | Overage used as percentage (filled only if overage limit is set) |
| remainingOverage | number | Remaining overage (filled only if overage limit is set) |
| remainingOveragePercent | number | Remaining overage as percentage (filled only if overage limit is set) |

### Response body JSON models

```
{



"accountName": "string",



"clusterId": "string",



"contactEmailAddress": "string",



"lastBillingTime": "string",



"licenseExpirationTime": "string",



"licenseKey": "string",



"licenseName": "string",



"licenseStatus": "string",



"licenseType": "string",



"productVersion": "string",



"usageOfDduUnits": {



"overageUsage": {



"overageQuota": 1,



"overageUsage": 1,



"overageUsagePercent": 1,



"remainingOverage": 1,



"remainingOveragePercent": 1



},



"quota": 1,



"remaining": 1,



"remainingPercent": 1,



"usage": 1,



"usagePercent": 1,



"usageStatus": "OVERAGE_QUOTA_REACHED"



},



"usageOfDemUnits": {},



"usageOfHostUnits": {}



}
```