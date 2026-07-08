---
title: Credential vault API - DELETE a set of credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/credential-vault/del-credentials
---

# Credential vault API - DELETE a set of credentials

# Credential vault API - DELETE a set of credentials

* Reference
* Published Oct 14, 2019

This API is deprecated. Use the [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.") from the Environment API instead.

Deletes the specified set of credentials for [synthetic monitors](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.").

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/credentials/{id}` |

## Authentication

To execute this request, you need an access token with `credentialVault.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the credentials set to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Success. The credentials set has been deleted. Response doesn't have a body. |

## Example

In this example, the request updates the set of credentials created in the [POST request example](/managed/dynatrace-api/configuration-api/credential-vault/post-credentials#example "Create a credentials configuration via Dynatrace API."). The response code of **204** indicates that the deletion was successful.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/CREDENTIALS_VAULT-1E6EA5075AF7E85D \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/credentials/CREDENTIALS_VAULT-1E6EA5075AF7E85D
```

#### Response code

204

## Related topics

* [Configure browser monitors in Classic](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Learn about configuring browser monitors and clickpaths.")
* [Configure HTTP monitors in Classic](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Learn about configuring HTTP monitors.")