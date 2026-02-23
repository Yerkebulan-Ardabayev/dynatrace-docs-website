---
title: Policy boundaries
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries
scraped: 2026-02-23T21:40:15.904559
---

# Policy boundaries

# Policy boundaries

* Latest Dynatrace
* 6-min read
* Published Sep 01, 2024

With policy boundaries, you can assign permissions with fine-granular restrictions on the data level.

Policy boundaries enable to restrict user permissions on the record and resource level and are intended to work very well with the Dynatrace default policies.

## What are policy boundaries?

Policy boundaries allow you to bundle restrictions on the record and/or resource level together for usage in your permission assignments. This allows for easier management of partitions on the data level and enables re-usability. Boundaries alone don't restrict anything, they are always used together with policies in the process of assigning policies to your user groups.

Whenever a boundary is selected in combination with a security policy, it further restricts the existing policy, which can also result in no access for the user.

Policy boundaries support all conditions that are available in the [IAM reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Boundaries and default policies

**Use case**:

As an account admin I would like to restrict the **Read logs** default policy for 20 user groups to logs from K8s development namespace.

**Solution**:

1. Create a boundary **K8s DEV** with the following content:

   * `storage:k8s.namespace.name = "DEVELOPMENT";`
2. Select the boundary when you assign the **Read Logs** default policy to your user groups.

   * The boundary is automatically applied to all permissions where it fits and therefore restricts log access.

If you ever want to adopt the boundary because your access requirements have changed, for example you introduce another stage in your development process, you just need to change the boundary like so:

`storage:k8s.namespace.name IN ("DEVELOPMENT","HARDENING");`

### Technical details about boundaries

Boundaries allow you to decouple the "What" and "Where" of a policy.

In other words, enable you to externalize the conditions to a separate object for easier management and re-usability.

`ALLOW <permissions> WHERE <conditions>`

* **What** being the permissions part of the policy that defines which APIs you are allowed to use
* **Where** being the service related fine granular permissions on record/resource-level expressed by the policy conditions.

This mechanism is extremely useful in combination with the [default policies](/docs/manage/identity-access-management/permission-management/default-policies#default-policies "Dynatrace default policies reference").

The default policies define a set of permissions to access features and data. As they are generic, they don't restrict the access to a specific records and resources.

**Example**:

The `storage:k8s.namespace.name IN ("DEV","PREPROD")` is a recurring pattern in your policies and can be externalized into a policy boundary.

```
ALLOW storage:logs:read WHERE storage:k8s.namespace.name IN ("DEV","PREPROD");



ALLOW storage:metrics:read WHERE storage:k8s.namespace.name IN ("DEV","PREPROD");
```

Boundary **K8s-dev-preprod**:

`storage:k8s.namespace.name IN ("DEV","PREPROD");`

Of course, this is a basic example and your boundary could consist of more statements that exactly define to what records and resources your users have access.

## Working with policy boundaries

The boundary management operations listed below are all performed using the **Account Management** pages.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.

   This opens `https://myaccount.dynatrace.com/`, which you can bookmark for easy access to Account Management.
2. Go to **Identity & access management** > **Policy management**.
3. On the policy management screen you find two tabs for **Policies** and **Boundaries** on top.
4. Select **Boundaries** to open the boundary management screen.

### Create a new policy boundary

1. Select  **Boundary** and specify:

   * **Boundary Name**
   * **Boundary query**

     + Here you provide your conditions in textual format. One line per condition, no logical operators allowed.
2. Select **Save** to create your boundary.

### Edit a policy boundary

1. Find the policy boundary that you want to edit in the list overview.
2. In the Actions column, select  > **Edit boundary**.
3. Adopt the boundary to your requirements and click **Save**.

   * A change in the boundary will have an immediate effect on the user permissions that are assigned with this boundary.

### Delete a policy boundary

1. Find the policy boundary that you want to edit in the list overview.
2. In Actions column, select  > **Delete boundary**.
3. In the Confirmation dialog click **Cancel** to abort or **Delete** to confirm.

Deletion of used boundaries

A boundary that is used in policy bindings can not be deleted. Before you can delete the boundary you have to adjust or remove all bindings where the boundary is used.

### Assignment of a policy boundaries during permission assignment

1. To assign a boundary please configure your group permissions as described in [Group management](/docs/manage/identity-access-management/user-and-group-management/access-group-management#manage-group-permissions "Manage Dynatrace groups and their permissions.").
2. Select one or multiple boundaries that should be applied to your permission assignment.

   * To learn about how boundaries are applied to your policy permissions, see the [How are policy boundaries applied?](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries#apply-boundary "Restrict security policies with policy boundaries to provide tailored access to your users.") section below.

Boundaries assignment

Policy boundaries can only be assigned to policies, they are not compatible with role-based permissions.

## How are policy boundaries applied?

Boundaries work for all services that are covered with the security policies and which are documented in the [IAM Policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

When a policy binding contains boundaries the effective policy is calculated according to the following rules:

* Only conditions added to service configuration will be applied to relative permissions. This rule doesn't apply to global conditions. Global conditions will be applied to all permissions
* When a boundary contains repeated condition names, then each policy statement is multiplied by such conditions. Each of the repeated conditions appears separately in each applicable statement.
* When more than one boundary applies to a policy, then effective statements are calculated for each boundary separately

In certain configurations this may cause unintended unconditional access. For example when this policy:

```
"ALLOW storage:logs:read, storage:entities:read;"
```

is bound to boundary one:

```
storage:host.name="myHost"
```

and boundary two:

```
storage:dt.security_context="mySC"
```

will produce:

```
ALLOW storage:entities:read;



ALLOW storage:entities:read WHERE storage:dt.security_context = "mySC";



ALLOW storage:logs:read WHERE storage:host.name = "myHost";



ALLOW storage:logs:read WHERE storage:dt.security_context = "mySC" `
```

which would effectively grant unconditional read access to storage entities, as boundary one's condition of `storage:host.name="myHost"`does not apply to permission `storage:entities:read`.

* When a policy statement contains multiple permissions, then such a statement will be split into single permission statements
* Boundaries are applied to policy statements without evaluating the statement's condition. Boundary will be applied no matter if the statement already contains the same condition
* Boundaries don't apply to `DENY` statements

## Expressing management zones inside of policy boundaries

To use your management zones inside of boundaries you just need to reference them as a condition in your policy boundary.

Boundary **Kubernetes**:

```
environment:management-zone startsWith "[Kubernetes]";



storage:k8s.namespace.name IN ("DEV","PREPROD");
```

This boundary includes all management zones that start with `[Kubernetes]`, as well as all the records stored in Grail for the `DEV` and `PREPROD` K8s namespaces.

Be aware that the management zones referenced in your boundaries only apply to policy statements that support management zones.

Grail does not support management zones but uses the `storage:` fields for record level access control. For more details see [What is the difference between management zones and new IAM policies?](/docs/platform/upgrade#access-control "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.")

## Restrictions and limits of policy boundaries



* Only 10 restrictions per boundary, to keep them manageable. If you need more restrictions for your use case, create more boundaries and [assign multiple boundaries](/docs/manage/identity-access-management/iam-limits "IAM limits for Dynatrace SaaS") to the policy.
* Boundaries are only compatible with security policies. No role-based support.
* Boundaries don't support the AND operator, every line of a boundary can only consist of one condition.

  + If you need logical operators and also want to re-use your policy definitions please take a look into [policy templating](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating "Policy templating").