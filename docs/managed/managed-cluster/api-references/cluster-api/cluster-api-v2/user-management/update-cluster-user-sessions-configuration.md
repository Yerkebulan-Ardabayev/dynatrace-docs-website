---
title: "Update cluster user sessions configuration"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/update-cluster-user-sessions-configuration
updated: 2026-02-09
---

# Update cluster user sessions configuration

# Update cluster user sessions configuration

* Published Feb 12, 2020

This API call updates a cluster user sessions configuration. You can modify the user sessions configuration by specifying new concurrent user session limits for cluster admin accounts and regular users. Set limits to `0` for unlimited concurrent user sessions. If you choose to set any of the limits to `0`, the limit for the other account type also must be set to `0`.

You can use this request to update automatic logout policy. By default, there's no auto logout of users who stay on auto-refreshable page. Use below payload to turn automatic logout on and set the session timeout to `900` seconds (15 minutes).

```
"automaticLogoutDto": {



"logoutInactiveUsersEnabled": true,



"userInactivityTimeout": 900



}
```

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/clusterConfig/userSessions`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [UserSessionsConfig](#openapi-definition-UserSessionsConfig) | The configuration of user sessions - concurrent sessions policy and automatic logout. | body | Optional |

### Request body objects

#### The `UserSessionsConfig` object

The configuration of user sessions - concurrent sessions policy and automatic logout.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| automaticLogoutDto | [AutomaticLogoutConfiguration](#openapi-definition-AutomaticLogoutConfiguration) | Configuration of automatic logout. | Required |
| concurrentSessionPolicyDto | [ConcurrentSessionPolicy](#openapi-definition-ConcurrentSessionPolicy) | The configuration of the concurrent sessions policy. Set '0' to disable session limitation. | Required |

#### The `AutomaticLogoutConfiguration` object

Configuration of automatic logout.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| logoutInactiveUsersEnabled | boolean | True if automatic logout is enabled | Required |
| userInactivityTimeout | integer | User inactivity timeout | Required |

#### The `ConcurrentSessionPolicy` object

The configuration of the concurrent sessions policy. Set '0' to disable session limitation.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| adminLimit | integer | Session limit for admin users (0 = no limit) | Required |
| userLimit | integer | Session limit for regular users (0 = no limit) | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | Successful |
| **400** | Wrong parameters |
| **510** | Configuration update failed |

## Example

In this example, the request updates the cluster user sessions configuration. Cluster updates the current session policy for concurrent sign-ins and user inactivity. The request indicates that the concurrent sign-in limit for users is `3`. The limit for cluster admin accounts is `5`. Also, the inactivity sign-out policy is in effect and is set to `900` seconds.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/cluster/v2/clusterConfig/userSessions"



-H  "accept: */*"



-H  "Content-Type: */*"



-d "{\"concurrentSessionPolicyDto\":{\"userLimit\":0,\"adminLimit\":0},\"automaticLogoutDto\":{\"logoutInactiveUsersEnabled\":true,\"userInactivityTimeout\":900}}"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/clusterConfig/userSessions
```

#### Request body

```
{



"concurrentSessionPolicyDto": {



"userLimit": 3,



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
