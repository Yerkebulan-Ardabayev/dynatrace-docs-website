---
title: Account configuration for Monaco account management
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/configuration/account-configuration
scraped: 2026-02-15T21:23:25.755060
---

# Account configuration for Monaco account management

# Account configuration for Monaco account management

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Jan 15, 2026

To define the accounts for which Monaco will configure the account management resources, you need to create an `accounts` section in a [manifest file](/docs/deliver/configuration-as-code/monaco/configuration#manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.").

In the following example, we define a single account object containing account-related information. The **name** property specifies the account name (in this example, `my-account`) that can be referenced using the Monaco CLI commands `--account` flag.

```
accounts:



- name: my-account



accountUUID: 12345678-1234-5678-1234-123456789012



oAuth:



clientId:



name: OAUTH_CLIENT_ID



clientSecret:



name: OAUTH_CLIENT_SECRET
```

Account management requires OAuth credentials.
Platform tokens and API tokens are not supported.
The OAuth client must have the appropriate scopes configured for the account resources you want to manage.
Ensure your OAuth credentials include the required permissions for users, groups, policies, boundaries, or service users before deploying configurations.

Other than the `accounts` section, a `manifest.yaml` defined for account resources is the same as for environment configurations, requiring [`projects`](/docs/deliver/configuration-as-code/monaco/configuration#project-definitions "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") of account resource configuration files.

## Account resources

Using Monaco, you can define [users](/docs/manage/identity-access-management/user-and-group-management/access-user-management "User management"), [service users](/docs/manage/identity-access-management/user-and-group-management/access-service-users "Service users"), [groups](/docs/manage/identity-access-management/user-and-group-management/access-group-management "Manage Dynatrace groups and their permissions."), [policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies"), and [boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") as dedicated types in YAML configuration files.

Unlike the usual environment-level configurations, no JSON template files are needed. Monaco builds the required API data directly from your YAML configuration.

### Example account management resources representation

This example shows how Monaco represents account management resources locally, with examples defining users, service users, groups, policies, and boundaries.

The following sections will describe each configuration in detail.

```
users:



- email: monaco@dynatrace.com



groups:



- Log viewer



- type: reference



id: my-group



serviceUsers:



- name: Monaco service user



description: Description of service user



groups:



- Log viewer



- type: reference



id: my-group



groups:



- name: My Group



id: my-group



description: This is my group



account:



permissions:



- account-viewer



policies:



- policy: Environment role - Access environment



environments:



- environment: abc12345



permissions:



- tenant-viewer



policies:



- policy: Environment role - Replay session data without masking



- policy:



type: reference



id: my-policy



boundaries:



- type: reference



id: workflow-simple-boundary



- MyExistingBoundary # If you want to reference by name directly



managementZones:



- environment: abc12345



managementZone: Management Zone 2000



permissions:



- tenant-viewer



policies:



- name: My Policy



id: my-policy



level:



type: account



description: My policy description.



policy: |-



ALLOW automation:workflows:read;



boundaries:



- id: workflow-simple-boundary



name: Workflow Simple boundary



query: automation:workflow-type = "SIMPLE";
```

While this sample shows users, service users, groups, policies, and boundaries defined in a single file, you can define them in individual files and structure your account resource projects and files as needed.

### Users

```
users:



- email: my-user@example.com



groups:



- Log viewer



- type: reference



id: my-group
```

In this example, we define these objects.

* **users** define one or more users bound to different groups.

  + **email** address
  + **groups** specifies the groups to which the user belongs. In the example, the user belongs to the default `Log viewer` group.

    - **type**
    - **id** specifies a custom group, for example, `my-group`. This **id** must match a group defined under the **groups** field.

### Service users

Dynatrace Monaco CLI version 2.23.0+

```
serviceUsers:



- name: Monaco service user



description: Description of the service user.



originObjectId: 123e4567-e89b-12d3-a456-426614174000



groups:



- Log viewer



- type: reference



id: my-group
```

In this example, we define these objects.

* **serviceUsers** define one or more service users bound to different groups.

  + **name** is the name of the service user. If not unique within an account, an **originObjectId** must be provided.
  + **description** is an optional description of the service user.
  + **originObjectId** is an optional Dynatrace ID of an existing service user to update, used to differentiate between service users if more than one has the same name.
  + **groups** specifies the groups to which the service user belongs. In the example, the service user belongs to the default `Log viewer` group and to `my-group` defined under the **groups** field. As the latter is a reference, **type** must be set to `reference` and **id** must match that of a group defined under the **groups** field.

### Groups

```
groups:



- name: My Group



id: my-group



description: This is my group



account:



permissions:



- account-viewer



policies:



- policy: Environment role - Access environment



environments:



- environment: abc12345



permissions:



- tenant-viewer



policies:



- policy: Environment role - Replay session data without masking



- policy:



type: reference



id: my-policy



boundaries:



- type: reference



id: my-boundary



- MyExistingBoundary # If you want to reference by name directly



managementZones:



- environment: abc12345



managementZone: Management Zone 2000



permissions:



- tenant-viewer
```

In this example, we define these objects.

* **groups** defines one or more groups that are bound to different policies or permissions.

  + **name**: The name of the group.
  + **id**: A monaco-internal unique identifier for the group, which users and service users can reference.
  + **description**: A description of the group.
  + **account** specifies permissions and policies to which the group is bound on the account level.
  + **environments** specify the permissions and policies to which the group is bound on the environment level.

    - **name**: The environment-id.
    - **permissions**: A list of permissions assigned to the group for this environment.
    - **policies**
    - **policy** can be referenced by name if a default policy is available.

      * **type** must be set to `reference` when referencing a custom policy.
      * **id** references a custom policy. The **id** must match a policy defined in the **policies**.
    - **boundaries** can be referenced by name if it's available.

      * **id** references a custom boundary. The **id** must match a boundary defined in the **boundaries**.
      * **type** must be set to `reference` when referencing a custom boundary.
  + **managementZones**: specifies the permissions assigned to the group on the management zone level.

    - **environment**: The environment-id.
    - **managementZone**: The name of the environment zone, for example, `Management Zone 2000`.
    - **permissions**: A list of permissions assigned to the group for this management zone.

### Policies

```
policies:



- name: My policy



id: my-policy



level:



type: account



description: My policy is defined for the account.



policy: |-



ALLOW automation:workflows:read;



- name: My other policy.



id: my-other-policy



level:



type: environment



environment: abc12345



description: My policy is defined for a specific environment.



policy: |-



ALLOW automation:workflows:read;
```

In this example, we define these objects.

* **policies** defines one or more policies.

  + **name**: The name of the policy.
  + **id**: A monaco-internal unique identifier for the policy, which can be referenced by groups.
  + **level**: Specifies the level of the policy.

    - **type**: This can be `account` or `environment`.
    - **environment**: If the type is `environment`, specify the environment ID for which this policy applies.
  + **description**: A description of the policy.
  + **policy** contains any policy rules of this particular policy.

### Boundaries

```
boundaries:



- id: workflow-simple-boundary



name: Workflow Simple boundary



query: automation:workflow-type = "SIMPLE";
```

In this example, we define these objects.

* **boundaries** defines one or more boundaries.

  + **id**
  + **name**
  + **query** contains one or more policy statements separated by `;`.

## Commands



Because account-level configuration is usually distinct from environment-level configuration and changes less frequently, existing commands like `monaco deploy` ignore any account configuration that may be defined in a manifest file.

Dedicated commands exist for account resources: [Account](/docs/deliver/configuration-as-code/monaco/reference/commands-saas#account "How to use the Monaco CLI application, including arguments and options.").