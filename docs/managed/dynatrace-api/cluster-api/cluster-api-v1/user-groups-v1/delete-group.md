---
title: Delete user group
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/delete-group
scraped: 2026-05-12T12:12:43.956219
---

# Delete user group

# Delete user group

* Published Sep 13, 2021

This API call deletes a cluster user group.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| groupId | string | Group ID path parameter. Missing or empty values will return a 'Bad Request'. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [GroupConfig](#openapi-definition-GroupConfig) | Successfully deleted |
| **400** | - | Not Found |

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

In this example, you'll delete the `salesgroup` user group. If the user group is deleted, you'll receive details of the deleted user group. If the user group was removed previously, you'd receive an empty response payload with code `200`.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/v1.0/onpremise/groups/salesgroup" -H  "accept: application/json" -H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP'
```

#### Request URL

```
https://mymanaged.cluster.com/api/v1.0/onpremise/users/salesgroup
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