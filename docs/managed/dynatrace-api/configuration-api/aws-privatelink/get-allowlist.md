---
title: AWS PrivateLink API - GET allowlist
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-privatelink/get-allowlist
---

# AWS PrivateLink API - GET allowlist

# AWS PrivateLink API - GET allowlist

* Reference
* Published Nov 19, 2020

Lists the AWS accounts from the allowlist of AWS PrivateLink.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink/allowlistedAccounts` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink/allowlistedAccounts` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AllowlistedAwsAccountList](#openapi-definition-AllowlistedAwsAccountList) | Success. The list is provided in the response body. |

### Response body objects

#### The `AllowlistedAwsAccountList` object

| Element | Type | Description |
| --- | --- | --- |
| values | [AllowlistedAwsAccount](#openapi-definition-AllowlistedAwsAccount)[] | - |

#### The `AllowlistedAwsAccount` object

| Element | Type | Description |
| --- | --- | --- |
| id | string | The AWS account id to allowlist |

### Response body JSON models

```
{



"values": [



{



"id": "string"



}



]



}
```