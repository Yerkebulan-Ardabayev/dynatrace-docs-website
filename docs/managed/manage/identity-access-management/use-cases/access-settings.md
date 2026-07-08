---
title: Grant access to Settings
source: https://docs.dynatrace.com/managed/manage/identity-access-management/use-cases/access-settings
---

# Grant access to Settings

# Grant access to Settings

* Tutorial
* 11-min read
* Updated on Oct 31, 2025

This article shows you how to control your user access to Dynatrace settings globally or at an individual settings schema level.

All examples here are based on the [`Settings 2.0`](/managed/manage/settings/settings-20 "Introduction to the Settings 2.0 framework") service. For a complete list of services supporting policy-based authorization, see [IAM policy reference](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Who this is for

This is for Dynatrace account administrators who need to grant user access to Dynatrace settings. It also helps new Dynatrace users looking to understand group-based permissions.

## What you will learn

In this article, you'll learn how to:

* Verify built-in policies for account administrators.
* Access IAM features via REST API using an OAuth2 client.
* Handle read and write permission and allow access to a particular schema.

## Before you begin

Prior knowledge

* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")
* [Dynatrace settings framework](/managed/manage/settings/settings-20 "Introduction to the Settings 2.0 framework")

Prerequisites

* A Dynatrace account with administrative privileges.
* Set up the required users, federations, and user groups in advance.

Key terms

Settings 2.0
:   Unified framework for managing configurations through settings objects defined by Dynatrace-managed schemas.

Settings Schema
:   A specific configuration structure in Settings 2.0; permissions can be granted per schema for reading or writing.

Policy Administration Point (PAP) REST API
:   An API used to manage IAM policies, including creating and binding policies to groups.

Verify available policies for administrators

For every account, administrators have two built-in policies available for `Settings 2.0` services:

* `Settings Reader`: grants permission to read Dynatrace settings
* `Settings Writer`: grants permission to write Dynatrace settings

To verify that you have these policies

1. In the Cluster Management Console, go to **User authentication** > **Policy management**.
2. Find `Settings Reader` and `Settings Writer` in the table.

Authenticate REST API request

You can access all IAM features via the REST API. Here, we cover the aspects of API request authentication.

Dynatrace Managed deployments use token-based authentication for the PAP REST API.

To generate the token

1. In the Cluster Management Console, go to **Settings** > **API tokens**.
2. In the **Cluster tokens** section, select **Generate token**.

   * Give the token any name you want
   * Turn on the **Service provider API**
3. Select **Save**.
4. Select **Copy** to copy the token.
5. Add an `Authorization` header to your request with the value `Api-Token [generated token goes here]`.

## Example scenarios

### Example 1: read and write permission

Suppose you have the following teams in your organization:

* `IT` team: is responsible for configuring the Dynatrace environment and making sure everything works.
* `Sales` team: only needs to read the settings and never modify them.

The IT team needs read and write access, while the sales team needs only read access.

#### Create two Dynatrace user groups

The policies in the examples presented on this page showcase the mechanics of the policy framework and only give access to the settings service. They enable API access to the settings service, but they don't provide access to the Dynatrace Web UI.

First, create a group named `IT` with the policies `Settings Writer` and `Settings Reader`.

To create a group

1. In the Cluster Management Console, go to **User authentication** > **User groups**.
2. Select **Add new group**.
3. Enter the **Group name** (`IT` in this example) and **Group description**, then select **Save**.

To bind policies to the group

1. In the Cluster Management Console, go to **User authentication** > **User groups**.
2. Find the `IT` group and select the pencil icon in the **Edit** column to edit that group.  
   The edit view includes an **Environment permissions** section listing all environments you're managing.
3. Expand the environment you want to change and select the **Policies** tab.
4. In the **Select policies to bind** filter box:

   * Find and select the `Settings Writer` policy
   * Find and select the `Settings Reader` policy
5. Select the **Bind policies** button on the right to bind the policies.
6. Select **Save**.

Now repeat the above procedure to create a `Sales` group with read-only access.

1. Set the group name to `Sales`.
2. Bind only the `Settings Reader` policy to the sales team, as they don't need write access to Dynatrace settings.

#### Bind policies via the web UI

To bind policies to the group

1. In the Cluster Management Console, go to **User authentication** > **User groups**.
2. Find the `IT` group and select the pencil icon in the **Edit** column to edit that group.  
   The edit view includes an **Environment permissions** section listing all environments you're managing.
3. Expand the environment you want to change and select the **Policies** tab.
4. In the **Select policies to bind** filter box:

   * Find and select the `Settings Writer` policy
   * Find and select the `Settings Reader` policy
5. Select the **Bind policies** button on the right to bind the policies.
6. Select **Save**.

### Example 2: allow access to a particular schema

You can add a condition to a policy to achieve more control.

If the built-in policies are not granular enough for your needs, you can manage permissions at the setting level.

Assume that you have a particular `Settings 2.0` schema, say `settings.apm.my-super-secret-schema`, the only one you want to keep open for the `Sales` and `IT` groups.

You want to allow access to the following:

* Allow reading of schema `settings.apm.my-super-secret-schema`
* Allow reading and writing of objects belonging to the schema `settings.apm.my-super-secret-schema`

There are two methods to allow access to a schema.

1. Create a policy via Dynatrace web UI.
2. Create a policy via REST API.

#### Create a policy via Dynatrace web UI

This procedure uses the Dynatrace web UI. To use the REST API, see [Create a policy via REST API](#create-policy-rest-api).

To create a policy:

1. In the Cluster Management Console, go to **User authentication** > **Policy management**.
2. Select **Add policy**.
3. Describe the policy:

   * **Policy name**  
     Add a relevant name.
   * **Policy description**  
     Add a useful description.
   * **Policy statements**  
     Copy the following statement to the **Policy statements** box.

     ```
     ALLOW settings:schemas:read WHERE settings:schemaId = "builtin:container.monitoring-rule";



     ALLOW settings:objects:read WHERE settings:schemaId = "builtin:container.monitoring-rule";



     ALLOW settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
     ```

     Note that since one can use multiple permissions in one statement, it is possible to merge the first two statements from the above into a single one:

     ```
     ALLOW settings:schemas:read, settings:objects:read WHERE settings:schemaId = "builtin:container.monitoring-rule";



     ALLOW settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
     ```
4. Select **Save**.

The policy is added to your table of policies that you can bind to groups.

#### Create a policy via REST API

This procedure uses the REST API to perform the same tasks we did in [Create a policy via Dynatrace web UI](#create-policy-web-ui).

To create a policy using the API, we will use the `/repo/{level-type}/{level-id}/policies` endpoint and use a POST method to add a policy.

Assume that the policy name we want to add is `my_policy_name` and the description is `My policy description`. As before, assume that we want this policy to apply only on the environment level for the environment `my_tenant_id`.

The request body should be the following:

```
{



"name":"my_policy_name",



"description":"My policy description",



"tags":[



],



"statementQuery": "ALLOW settings:schemas:read WHERE settings:schemaId = \"builtin:container.monitoring-rule\"; ALLOW settings:objects:read WHERE settings:schemaId = \"builtin:container.monitoring-rule\"; ALLOW settings:objects:write WHERE settings:schemaId = \"builtin:container.monitoring-rule\";"



}
```

Equivalently, using multiple permissions in a single statement, the request body should be the following:

```
{



"name":"my_policy_name",



"description":"My policy description",



"tags":[



],



"statementQuery": "ALLOW settings:schemas:read, settings:objects:read WHERE settings:schemaId = \"builtin:container.monitoring-rule\"; ALLOW settings:objects:write WHERE settings:schemaId = \"builtin:container.monitoring-rule\";"



}
```

### Enforce the policy

**Important:** Remember that a policy does not take effect until you bind it to a group. You need to bind this example to the `IT` and `Sales` groups. See [Bind policies via Dynatrace web UI](#bind-web-ui) or [Bind policies via REST API](#bind-api) for details.

## Related topics

* [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.")
* [Dynatrace settings framework](/managed/manage/settings/settings-20 "Introduction to the Settings 2.0 framework")
* [IAM policy statement syntax and examples](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")