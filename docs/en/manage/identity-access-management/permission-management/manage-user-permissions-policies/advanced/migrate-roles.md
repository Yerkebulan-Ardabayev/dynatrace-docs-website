---
title: Upgrade role-based permissions to Dynatrace IAM policies
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles
scraped: 2026-02-27T21:27:41.670823
---

# Upgrade role-based permissions to Dynatrace IAM policies

# Upgrade role-based permissions to Dynatrace IAM policies

* Latest Dynatrace
* 11-min read
* Updated on Aug 20, 2025

Dynatrace version 1.266+

This guide defines and compares role-based access control (RBAC) and attribute-based access control (ABAC), and provides guidelines and recommendations to consider when planning your upgrade from RBAC to ABAC. Upgrade in this context means expressing classic RBAC permissions targeting the previous Dynatrace as statements within IAM policies. As is explained later, upgrading offers you multiple benefits.

The guide is primarily intended for use by account administrators wanting to take advantage of the power of the ABAC framework within the previous Dynatrace.

## What is ABAC?

ABAC is the preferred industry-wide access management framework because of its business-oriented and modern approach to defining security policies through logical, plain language.

It defines access to secure resources based on a combination of user, resource, action, and contextual attributes. It uses security policies as a mechanism to define access rules for resources.

### Understanding the Difference: RBAC vs ABAC

RBAC roles are typically created to map work functions, such as department, seniority, or work assignment. RBAC permissions typically grant all-or-nothing access to resources based on pre-defined static roles.

For example, assigning "View Logs" permission to a group in Dynatrace grants users in that group the ability to view all captured logs. There is no ability to further refine their access to the logs.

* Various user, resource, and contextual information is not considered in classic RBAC.
* RBAC roles do not adapt well to changing access permission requirements and the dynamic nature of the attributes of the resources being secured.

ABAC, on the other hand, determines user access by evaluating resource, data, user, and contextual attributes, along with the specific user action being requested. This provides for a flexible permissions framework that handles changes in access requirements in a more dynamic way, rather than relying on static RBAC roles. Furthermore, the access control granularity offered makes it possible to design common or complex access requirements.

Dynatraceâs IAM permissions framework uses these core ABAC principles and further enhances them with features like [policy templating](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating "Policy templating"), [policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users."), and [default policies](/docs/manage/identity-access-management/permission-management/default-policies#default-policies "Dynatrace default policies reference") to make our implementation of ABAC more flexible and user friendly.

### ABAC implementation in your Dynatrace

The Dynatrace IAM permissions framework currently supports the classic RBAC as well as the newer, ABAC, which leverages security policies to define permissions. Security policies are stand-alone components of the ABAC framework that allow combining one or many policy statements to define conditional access to your Dynatrace resources.

The access permissions defined in a security policy take effect when that policy is bound to a group, thus directly controlling the permissions of the users of that group. For simplicity, we will refer to security policies as simply policies for the remainder of this guide.

The following diagram captures the relationship between users, groups, policies, and policy boundaries.

![Users-Groups-Policies-Boundaries](https://dt-cdn.net/images/user-group-policy-boundary-812-75ea55d16b.png)

[Policies](/docs/manage/identity-access-management/permission-management "Permission management") leverage user, resource, data, and contextual attribution to enable you to configure access to your Dynatrace secure resources. You can secure individual data resources, apps, and services while optionally specifying business-specific access control conditions through the expressiveness of the [policy statements syntax](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.").

One or many policy statements can be combined into one policy. The policy can then be bound to one or many user groups, ultimately granting the users of those group the resource access defined by the policy.

For example, the Dynatrace ABAC policy below grants the ability to install or delete (action) custom apps (resource) where (condition) app identifier (resource attribute) is prefixed with "custom" (attribute value):

```
ALLOW app-engine:apps:install, app-engine:apps:delete WHERE shared:app-id startsWith âcustomâ;
```

The next example leverages additional contextual information (the time of the day) to restrict the ability to run apps only within business working hours.

```
ALLOW app-engine:apps:run WHERE shared:app-id = "dynatrace.automations" and global:time-of-day > "09:00+01:00" AND global:time-of-day < "17:00+01:00";
```

Classic RBAC roles can also be expressed in policies. For example, the policy statement below grants environment access but only for a specific management zone.

```
ALLOW environment:roles:viewer WHERE environment:management-zone=âmgmt-euâ
```

The ability to include classic RBAC roles in your policy statements is a very important feature of ABAC policies to help you transition from RBAC.

The true power of the Dynatrace ABAC framework lies in its ability to dynamically target individual or groups of platform resources, while optionally combining available attributes to further narrow down access parameters using the expressive nature of policy statement syntax.

### Benefits of upgrading to ABAC

Dynatraceâs ABAC permissions framework offers the following advantages:

#### Security and compliance

* Policies enable admins to adopt the [principle of least privilegeï»¿](https://en.wikipedia.org/wiki/Principle_of_least_privilege)
* Policies provide a better framework to adhere to your IT compliance standards

#### Flexibility

* Policies are built to be adaptable to changes and future platform services
* [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") are managed by Dynatrace and automatically adapt to future platform changes
* Multiple policy statements can be combined to form one policy, allowing administrators to build policies that align with their access control business requirement

#### Scalability

* Policies allow for a concise expression of complex permissions
* Policy boundaries offer further policy optimization and generalization
* [Policy templating](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating "Policy templating") enables parameterization of policies through binding parameters

#### Granularity

* Each policy statement can target one or many platform resources
* `WHERE` conditions can be appended to statements to further limit access

#### Usability

[Policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") can be re-used in multiple policies.

* Default policies give a great starting point for common access scenarios

#### Futureproofing

* ABAC is here to stay and will continue to be developed and extended.

## RBAC to ABAC upgrade planning

The following upgrade guide recommends a strategy and best practices to consider when planning and executing your upgrade from RBAC to ABAC.

If you use management zones for access control, this guide offers examples of how to refer to management zones within policies so that you can remove the corresponding RBAC assignments. This guide does not cover how to migrate your use of management zones into Grail permissions.

### Upgrade guidelines

The upgrade strategy you choose will depend on your current Dynatrace configuration.

The general strategy is to:

1. Identify RBAC permissions that you have currently configured with your groups.
2. Define a mapping on how those RBAC permissions map to ABAC permissions that can be implemented in policies.

   * You can repeat doing this in batches until you cover all your groups.
   * Where appropriate, consider using [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") rather than building custom policies.

You can use these sample [Dynatrace Notebook or this PowerShellï»¿](https://community.dynatrace.com/t5/Dynatrace-tips/RBAC-to-ABAC-migration-helper-scripts-Notebook-and-PowerShell/m-p/257807#M1447) scripts to give you an initial assessment and some recommendations to get you started. We will use the script output from our sample Dynatrace environment to illustrate some important concepts and best practices you should consider as you plan your RBAC upgrade to ABAC.

Note that any automation scripts that you might have built that use RBAC permissions will also have to be reviewed for potential changes in the event that you transition to solely using ABAC for your access control.

### Your Dynatrace RBAC assessment

An upgrade plan should start with an assessment of your current RBAC configuration. This means identifying existing RBAC roles assigned to your groups. We are interested in RBAC role assignments that are scoped to target environments or management zones.

Consider the steps below to conduct an initial assessment. You can use the Account Management portal to complete the steps or [import](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and use the provided notebook to help you. Alternatively, you can also use the provided PowerShell script.

1. Create the required OAuth client in the [Account Management](/docs/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.") portal with permissions as instructed in the notebook.
2. Import the provided **RBAC Assessment** notebook into your Dynatrace or, if itâs more convenient for you, use the provided PowerShell script.
3. Run the script.
4. The output will be a table like the example below:

| permissionName | scope | scopeType | mgmtzone\_name | group\_name | abacRole | recommended\_policy |
| --- | --- | --- | --- | --- | --- | --- |
| tenant-replay-session-with-masking | xyz:mgmt\_na\_east | management-zone | mgmt\_na\_east | group\_na\_supp | `environment:roles:replay-sessions-with-masking` | Dynatrace Professional |
| tenant-replay-session-without-masking | xyz:mgmt\_na\_east | management-zone | mgmt\_na\_east | group\_na\_supp | `environment:roles:replay-sessions-without-masking` | Dynatrace Professional |
| tenant-manage-settings | xyz:mgmt\_na\_east | management-zone | mgmt\_na\_east | group\_na\_supp | `environment:roles:manage-settings` | Dynatrace Professional |
| â¦ | â¦ | â¦ | â¦ | â¦ | â¦ | â¦ |
| tenant-replay-session-with-masking | xyz:mgmt\_na\_west | management-zone | mgmt\_na\_west | group\_na\_supp | `environment:roles:replay-sessions-with-masking` | Dynatrace Professional |
| tenant-replay-session-without-masking | xyz:mgmt\_na\_west | management-zone | mgmt\_na\_west | group\_na\_supp | `environment:roles:replay-sessions-without-masking` | Dynatrace Professional |
| tenant-manage-settings | xyz:mgmt\_na\_west | management-zone | mgmt\_na\_west | group\_na\_supp | `environment:roles:manage-settings` | Dynatrace Professional |
| â¦ | â¦ | â¦ | â¦ | â¦ | â¦ | â¦ |

### Upgrade to ABAC

With the inventory of assigned RBAC permissions already created, you can now map RBAC permissions to ABAC ones. You should give priority to existing [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") whenever possible, as opposed to building your own custom policies.

We will use âgroup\_na\_suppâ to help us illustrate some key best practices you should consider for your ABAC configuration.

This group currently has the following RBAC permissions scoped to two management zones âmgmt\_na\_eastâ and âmgmt-na\_westâ:

| RBAC Role Name | ABAC role name |
| --- | --- |
| tenant-replay-session-with-masking | `environment:roles:replay-sessions-with-masking` |
| tenant-replay-session-without-masking | `environment:roles:replay-sessions-without-masking` |
| tenant-manage-settings | `environment:roles:manage-settings` |
| tenant-view-sensitive-request-data | `environment:roles:view-sensitive-request-data` |
| tenant-view-security-problems | `environment:roles:view-security-problems` |
| tenant-manage-security-problems | `environment:roles:manage-security-problems` |
| tenant-log-viewer | `environment:roles:logviewer` |

If we were to create a new custom policy to assign those permissions, we could write the following policy statement:

```
ALLOW  environment:roles:replay-sessions-with-masking, environment:roles:replay-sessions-without-masking, environment:roles:manage-settings, environment:roles:view-sensitive-request-data , environment:roles:manage-security-problems, environment:roles:logviewer



WHERE environment:management-zone startsWith "mgmt_na";
```

We could then bind this policy to the `group_na_supp` group and remove the old RBAC role assignment from the group. To further optimize our new ABAC permission, we could use **Dynatrace Professional** rather than building a custom policy. Because [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") are read-only, we would need a mechanism to append our `WHERE` condition above.

This is where [policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") come into play. We can store the condition `environment:management-zone startsWith "mgmt\_na";` in a policy boundary and then use it with our group, as we bind the group to the **Dynatrace Professional** policy, thus further restricting this permission assignment using the boundary we created.

First, letâs create the policy boundary. In [Account Management](/docs/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health."), under **Identity & Access management** > **Policy management**, we can create a policy boundary specific to North America management zones.

![Boundaries](https://dt-cdn.net/images/boundaries-468-08355e2a83.png)

Next, we assign the default policy **Dynatrace Professional** to the `group_na_supp` and apply the boundary we just created.

![Permission Assign](https://dt-cdn.net/images/permissionassign-936-e6e96537be.png)

As may be obvious from this example, policy boundaries make it possible to extract your business-specific access requirements out of the policy and into a standalone unit that can be re-applied over and over across multiple policies. Policy boundaries can be assigned to one or many group-to-policy bindings, making them reusable. The combination of default policies with policy boundaries has the potential to further simplify your permissions configuration.

Best practice

Make use of [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") whenever possible and define your business-specific access conditions in policy boundaries.

### When should you create custom policies

Rather than creating new custom policies, administrators are strongly encouraged to primarily leverage default policies, which are built and managed by Dynatrace and already encapsulate the necessary policy statements for typical access scenarios. When assigning these default policies to groups, you can then further restrict the permissions by using policy boundaries.

In cases where default policies do not meet your specific permission requirements, or when you might want to restrict them with some specific `DENY` statements, you can then build custom policies.

Best practice

Build your own custom policies only when provided default policies don't fit your requirements or when you want to further limit default policies.

### Testing and validation

We recommend mocking up groups and users and testing separately, ideally in a sandboxed environment if possible.

Also, Dynatraceâs Enterprise API could be used to provide useful permissions information for specific users or groups. For example, the following GET request to `https://api.dynatrace.com` will return current permissions for a specific user:

```
`https://api.dynatrace.com/iam/v1/resolutionaccount/:accountIdHere/effectivepermissions?entityType=user\&entityId=:userIdHere`
```

### Deployment

Deploy policies in a phased approach to minimize user access disruptions. You may choose to do these in batches of groups or some other way more appropriate to your setup.

Best practice

Consider deploying your changes in batches rather than all at once.

### Monitoring and tuning

Monitor your ABAC permissions over time to see if they have adversely affected user access and adjust accordingly.

### Upgrade support

Refer to our online documentation and Dynatrace Community forums for additional help during your upgrade from RBAC to ABAC. Additionally, make use of Dynatraceâs support channels for more targeted help.

### Final checklist

1. Compile your existing RBAC roles and group assignments

   * Identify and plan to replace any custom automation still relying on RBAC
2. Design your ABAC policies:

   * Use default policies whenever suitable
   * Create policy boundaries to capture your specific business logic
3. Decide on an upgrade strategy

   * Consider a phased rather than a big-bang approach by introducing changes in multiple batches
4. Test your upgrade

   * Use a sandbox environment if available to test the effects of your new ABAC-only configuration
   * Try upgrading a select set of groups first
5. Monitor the effects of your upgrade to catch and correct any misconfigurations

## Related topics

* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [IAM policy statement syntax and examples](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")