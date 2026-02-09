---
title: "Get cluster user sessions configuration"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions-configuration
updated: 2026-02-09
---

# Get cluster user sessions configuration

# Get cluster user sessions configuration

* Published Apr 02, 2020

This API call gets a cluster user sessions configuration.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/clusterConfig/userSessions`

## Parameters

No parameters are required for this API call.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UserSessionsConfig](#openapi-definition-UserSessionsConfig) | Successful |

### Response body objects

#### The `UserSessionsConfig` object

The configuration of user sessions - concurrent sessions policy and automatic logout.

| Element | Type | Description |
| --- | --- | --- |
| automaticLogoutDto | [AutomaticLogoutConfiguration](#openapi-definition-AutomaticLogoutConfiguration) | Configuration of automatic logout. |
| concurrentSessionPolicyDto | [ConcurrentSessionPolicy](#openapi-definition-ConcurrentSessionPolicy) | The configuration of the concurrent sessions policy. Set '0' to disable session limitation. |

#### The `AutomaticLogoutConfiguration` object

Configuration of automatic logout.

| Element | Type | Description |
| --- | --- | --- |
| logoutInactiveUsersEnabled | boolean | True if automatic logout is enabled |
| userInactivityTimeout | integer | User inactivity timeout |

#### The `ConcurrentSessionPolicy` object

The configuration of the concurrent sessions policy. Set '0' to disable session limitation.

| Element | Type | Description |
| --- | --- | --- |
| adminLimit | integer | Session limit for admin users (0 = no limit) |
| userLimit | integer | Session limit for regular users (0 = no limit) |

### Response body JSON models

```
{



"automaticLogoutDto": {



"logoutInactiveUsersEnabled": true,



"userInactivityTimeout": 900



},



"concurrentSessionPolicyDto": {



"adminLimit": 1,



"userLimit": 1



}



}
```

## Example

In this example, the request queries the cluster for the current user sessions configuration. The cluster then returns information about the current session policy for concurrent sign-ins and user inactivity. The response indicates that the concurrent sign-in limit for users is `2`. For cluster admins accounts, the limit is `5`. Also, the inactivity sign-out policy is in effect and is set to `900` seconds.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/clusterConfig/userSessions" -H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/clusterConfig/userSessions
```

#### Response body

```
{



"concurrentSessionPolicyDto": {



"userLimit": 2,



"adminLimit": 5



},



"automaticLogoutDto": {



"logoutInactiveUsersEnabled": true,



"userInactivityTimeout": 900



}



}
```

#### Response code

`204`
