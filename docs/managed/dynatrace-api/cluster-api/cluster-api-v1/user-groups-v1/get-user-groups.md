---
title: Get user groups
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-user-groups
---

# Get user groups

# Get user groups

* Published Sep 13, 2021

This API call retrieves information on a specific cluster user groups.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups`

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [GroupConfig](#openapi-definition-GroupConfig)[] | Success |

### Response body objects

#### The `ResponseBody` object

#### The `GroupConfig` object

The configuration of the group.

| Element | Type | Description |
| --- | --- | --- |
| accessRight | object | Access rights |
| id | string | Group ID. Leave empty if creating group. Set if updating group. |
| isAccessAccount | boolean | (only applicable for Dynatrace Platform Subscription license model) If true, then the group has the "Access account" rights. Users assigned to a group with this permission can access account.dynatrace.com service to see Dynatrace Platform Subscription utilization and manage license quotas. |
| isClusterAdminGroup | boolean | If true, then the group has the "cluster administrator" rights. Users assigned to a group with this permission are automatically given administrator access rights for all environments. They have access to Cluster Management Console and can manage your monitoring environments and Dynatrace Server. Users assigned to groups with this permission can also: Add new Dynatrace Server nodes, update Dynatrace Server, manage Dynatrace Managed users and user groups, install Dynatrace OneAgent into any monitoring environment, configure monitoring settings for any monitoring environment. |
| isManageAccount | boolean | If true, then the group has "Edit billing & account info" rights. Users assigned to a group with this permission can access myaccount.dynatrace.com service to see product usage statistics, license utilization and account information. |
| ldapGroupNames | string[] | LDAP group names |
| name | string | Group name |
| ssoGroupNames | string[] | SSO group names. If defined it's used to map SSO group name to Dynatrace group name, otherwise mapping is done by group name |

### Response body JSON models

```
[



{



"accessRight": {},



"id": "string",



"isAccessAccount": true,



"isClusterAdminGroup": true,



"isManageAccount": true,



"ldapGroupNames": [



"string"



],



"name": "string",



"ssoGroupNames": [



"string"



]



}



]
```

## Example

In this example, you retrieve user groups with details.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/groups' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP'
```

#### Request URL

```
https://mymanaged.cluster.com/api/v1.0/onpremise/onpremise/groups
```

#### Response body

```
[



{



"isClusterAdminGroup": true,



"isManageAccount": true,



"isAccessAccount": true,



"id": "owners",



"name": "Owners",



"ldapGroupNames": [



"LDAPM_ClusterBasicAccess"



],



"ssoGroupNames": [],



"accessRight": {}



},



{



"isClusterAdminGroup": false,



"isManageAccount": false,



"isAccessAccount": false,



"id": "mobile",



"name": "TeamPh",



"ldapGroupNames": [



"TeamPh"



],



"ssoGroupNames": [],



"accessRight": {



"VIEWER": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"MANAGE_SETTINGS": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"AGENT_INSTALL": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"LOG_VIEWER": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"VIEW_SENSITIVE_REQUEST_DATA": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"CONFIGURE_REQUEST_CAPTURE_DATA": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



],



"REPLAY_SESSION_DATA": [



"3d211429-1ebd-40a2-49ff-d2c40e605ff4",



"c69c1533-18c1-ed0e-fa15-9132f3a1a18b"



]



}



}



]
```

#### Response code

`200`