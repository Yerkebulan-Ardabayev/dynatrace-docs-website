---
title: "Delete specific environment"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/delete-specific-managed-environment
updated: 2026-02-09
---

# Delete specific environment

# Delete specific environment

* Published Mar 09, 2021

This API call deletes the specified environment. An environment must be disabled before it can be deleted.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/environments`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the environment to be deleted. | path | Required |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | Deleted. Response does not have a body. |
| **400** | Failed. For example, if an environment is not disabled. |

## Example

Deletes the environment `19a963a7-b19f-4382-964a-4df674c8eb8e`.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/cluster/v2/environments/19a963a7-b19f-4382-964a-4df674c8eb8e" -H "accept: */*" -H "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/environments/19a963a7-b19f-4382-964a-4df674c8eb8e
```

#### Response body

Response does not have a body.

#### Response code

`204`
