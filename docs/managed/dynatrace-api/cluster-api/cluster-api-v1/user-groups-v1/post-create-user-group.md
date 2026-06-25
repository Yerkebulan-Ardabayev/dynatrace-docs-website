---
title: Create user group
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/post-create-user-group
scraped: 2026-05-12T12:12:49.149039
---

# Create user group

# Create user group

* Published Sep 13, 2021

This API call creates a cluster user group.

## Authentication

The `ServiceProviderAPI` (Service Provider API) Api-Token scope is required to get the default realm password policy configuration using the Dynatrace API. With this API method, you can preset user's password by passing `passwordClearText` value. This is allowed only if a specific Feature Flag is enabled. To do this, Please contact a Dynatrace product expert via live chat within your environment..

## Endpoint

`/api/v1.0/onpremise/groups`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [GroupConfig](#openapi-definition-GroupConfig) | Request body used for creating new user group. For creating user group leave 'id' empty, setting 'id' will return 'Bad Request'. Trying to create group with name that already exists will return 'Not Acceptable'. 'isAccessAccount' value is ignored when 'Dynatrace Platform Subscription' is not in use. | body | Optional |

### Request body objects

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
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [GroupConfig](#openapi-definition-GroupConfig) | Successfully updated |
| **400** | - | Operation failed. The input is invalid. Possible reasons:  * No group information received for the request to create a group * Group ID cannot be set * Group name cannot be null or empty * At least one of the specified environments doesn't exist |
| **406** | - | Not acceptable. Group already exists |

### Response body objects

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
```

## Example

In this example, you create the `Sales Group` user group that only maps to `sales` LDAP group membership. This group will allow access Cluster Management Console and Account Management full rights. As a response, you'll receive back the entity's current state and newly generated ID.

#### Curl

```
curl -X 'POST' \



'https://myManaged.cluster.com/api/v1.0/onpremise/groups' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP' \



-H 'Content-Type: application/json' \



-d '{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"id": "",



"name": "Sales Group",



"ldapGroupNames": [



"sales"



]



}



}'
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/groups
```

#### Response body

```
{



"isClusterAdminGroup": true,



"isAccessAccount": true,



"isManageAccount": true,



"id": "salesgroup",



"name": "Sales Group",



"ldapGroupNames": [



"sales"



]



}
```

#### Response code

`200`