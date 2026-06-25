---
title: Create user groups
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/post-create-users-groups
scraped: 2026-05-12T12:12:31.012772
---

# Create user groups

# Create user groups

* Published Sep 13, 2021

This API call creates multiple cluster user groups.

## Authentication

The `ServiceProviderAPI` (Service Provider API) Api-Token scope is required to get the default realm password policy configuration using the Dynatrace API. With this API method, you can preset user's password by passing `passwordClearText` value. This is allowed only if a specific Feature Flag is enabled. To do this, Please contact a Dynatrace product expert via live chat within your environment..

## Endpoint

`/api/v1.0/onpremise/groups/bulk`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [GroupConfig[]](#openapi-definition-GroupConfig) | - | body | Optional |

### Request body objects

#### The `RequestBody` object

#### The `GroupConfig` object

The configuration of the group.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| accessRight | object | Access rights | Optional |
| id | string | Group ID. Leave empty if creating group. Set if updating group. | Required |
| isAccessAccount | boolean | (only applicable for Dynatrace Platform Subscription license model) If true, then the group has the "Access account" rights. Users assigned to a group with this permission can access account.dynatrace.com service to see Dynatrace Platform Subscription utilization and manage license quotas. | Optional |
| isClusterAdminGroup | boolean | If true, then the group has the "cluster administrator" rights. Users assigned to a group with this permission are automatically given administrator access rights for all environments. They have access to Cluster Management Console and can manage your monitoring environments and Dynatrace Server. Users assigned to groups with this permission can also: Add new Dynatrace Server nodes, update Dynatrace Server, manage Dynatrace Managed users and user groups, install Dynatrace OneAgent into any monitoring environment, configure monitoring settings for any monitoring environment. | Required |
| isManageAccount | boolean | If true, then the group has "Edit billing & account info" rights. Users assigned to a group with this permission can access myaccount.dynatrace.com service to see product usage statistics, license utilization and account information. | Optional |
| ldapGroupNames | string[] | LDAP group names | Optional |
| name | string | Group name | Required |
| ssoGroupNames | string[] | SSO group names. If defined it's used to map SSO group name to Dynatrace group name, otherwise mapping is done by group name | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [GroupConfig[]](#openapi-definition-GroupConfig) | Success |
| **400** | - | No group information received for the create-group request |
| **406** | [GroupConfig[]](#openapi-definition-GroupConfig) | Unacceptable or incomplete request. Some groups were added. |

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

In this example, you add user groups `Sales Group` and `Developers` in a single request. This will set their data and assign environment permissions. As a response, you will receive back persisted state of the entities.

#### Curl

```
curl -X 'POST' \



'https://mymanaged.cluster.com/api/v1.0/onpremise/groups/bulk' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP' \



-H 'Content-Type: application/json' \



-d '[



{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"name": "Sales Group",



"ldapGroupNames": [



"sales-group"



],



"ssoGroupNames": [



"sales-group"



],



"accessRight": {



"VIEWER": [



"3fcc5d83-d9e5-4bf9-9e00-d997f9c4c63d"



],



"REPLAY_SESSION_DATA": [



"3fcc5d83-d9e5-4bf9-9e00-d997f9c4c63d"



]



}



},



{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"name": "Developers",



"ldapGroupNames": [



"dev-group"



],



"ssoGroupNames": [



"dev-group"



],



"accessRight": {



"VIEWER": [



"3fcc5d83-d9e5-4bf9-9e00-d997f9c4c63d"



]



}



}



]'
```

#### Request URL

```
https://mymanaged.cluster.com/api/v1.0/onpremise/groups/bulk
```

#### Response body

```
[



{



"isClusterAdminGroup": true,



"isManageAccount": true,



"isAccessAccount": true,



"id": "salesgroup",



"name": "Sales Group",



"ldapGroupNames": [



"sales-group"



],



"ssoGroupNames": [



"sales-group"



],



"accessRight": {}



},



{



"isClusterAdminGroup": true,



"isManageAccount": true,



"isAccessAccount": true,



"id": "developers",



"name": "Developers",



"ldapGroupNames": [



"dev-group"



],



"ssoGroupNames": [



"dev-group"



],



"accessRight": {}



}



]
```

#### Response code

`200`