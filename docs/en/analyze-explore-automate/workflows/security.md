---
title: User permissions for workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/security
scraped: 2026-02-20T21:18:01.290473
---

# User permissions for workflows

# User permissions for workflows

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Feb 17, 2025

## Workflows and AutomationEngine API permissions

The Workflows app, which is the frontend for the AutomationEngine, enables you to edit, manage, and run workflows in Dynatrace.

* To use Workflows, you need some general AppEngine permissions and some AutomationEngine-specific permissions.
* Permissions are configured in account administration and require account admin access.
* If you are missing any required permissions, reach out to your account administrator.

We recommend that administrators differentiate between regular users and administrators as follows.

### AutomationEngine authorization settings

If the required permission for a workflow task is missing, an attempt to execute this task results in a 403 Forbidden error.

Always make sure:

* You have the required permissions granted in [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.").
* You granted all required permissions for the workflows to run in the authorization settings.

To enable or edit the AutomationEngine authorization settings

1. In the **Workflows** app, go to **Settings** > **Authorization settings**.
2. Enable the required permissions from **Primary permissions** and **Secondary permissions** lists.

### Workflows user

A Workflows user creates, edits, runs, and monitors workflows.

To access the **Workflows** and view workflows, you need at least the following permissions.

Permission

Grants access to

`app-engine:apps:run`

List all apps and read the app bundles.

`automation:workflows:read`

View workflows.

`storage:system:read`

optional `storage:event.provider = "AUTOMATION_ENGINE"` [1](#fn-1-1-def)

`storage:buckets:read`

optional `storage:table-name = "dt.system.events"` [1](#fn-1-1-def)

View the execution history of workflows.

1

The conditions listed represent the most restrictive way to apply the permissions while still allowing access to the execution history. Any less restrictive application of these permissions will also provide the necessary access.

To write and execute workflows, the following additional permissions are required.

| Permission | Grants access to |
| --- | --- |
| `app-engine:functions:run` | Use the function executor. |
| `automation:workflows:run` | Run workflows manually via the user interface or API. |
| `automation:workflows:write` | Write workflows. It includes creating, updating, and deleting a workflow. It also includes the workflow configuration with active schedule or event trigger configurations. Thus, the workflow is run based on these configurations. |

You can grant users the `automation:workflows:write` permission where the `automation:workflow-type = "SIMPLE"` is specified. This means that they can create workflows with a single trigger and task. Since simple workflows don't consume workflow hours, this is a convenient way to give a broader user base access to workflows without the cost implication.

These permissions grant access to workflows themselves. To successfully run workflow tasks, the [actor](#workflow-actor) might need additional permissions.

### Workflows administrator

A Workflows administrator can:

* Access all workflows and executions in an environment.
* Manage workflows and executions where the owner is unavailable.
* Import or edit workflows, preserving the [actor](#workflow-actor) and [owner](#workflow-access) of the workflow, which is most of the time desired when transporting workflows between environments.

To administer workflows, you need the following permission on top of all [user permissions](#user-permission).

| Permission | Grants access to |
| --- | --- |
| `automation:workflows:admin` | Administer workflows. |

To turn on **Workflow admin** mode in Workflows

1. Verify that you have `automation:workflows:admin` permission in addition to all regular user permissions.
2. Select **Settings** in the upper-right corner of the **Workflows** app.
3. Turn on the **Workflow admin** mode.

To exit the **Workflow admin** mode and use Workflows as a regular user, turn off the **Workflow admin** toggle.

## Workflow owner

The initial owner of a workflow is the user who creates it. Right after a workflow is created, only the owner can view, manage, and execute the workflow. This is a private workflow.

To let others access a workflow, the owner has the following options:

* Make the workflow public. A public workflow is visible to every user with `automation:workflows:*` permissions.
* Transfer ownership to another user. For details, see [Change ownership of a workflow](/docs/analyze-explore-automate/workflows/manage-workflows/workflows-change-owner "Change ownership of your workflow.").
* Transfer ownership to a group, in which case all members of the group can access the workflow, depending on their permissions.

### Execution access and ownership

Access to an execution depends on the workflow ownership and private/public configuration when the execution was started.

* Execution access is always evaluated at the start of an execution.
* A change to workflow ownership or visibility doesn't impact past executions; it affects only future executions.

### Administrator

An administrator has access to all workflows and executions in an environment.

* An administrator can manage all workflows and executions.
* No restriction of visibility or ownership applies to an administrator.

## Workflow actor

Every execution of a workflow task is performed in the context of a user.

To figure out the actor of a workflow

1. Open a workflow in the workflow editor.
2. Select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **Settings**.
3. Check the details pane where you'll find the actor information.

* This user is called the actor.
* The actor is configured per workflow.
* By default, the actor is the creator of the workflow.

When you run a workflow in an environment for the first time, Dynatrace asks to allow the AutomationEngine to run workflows for you.

* You need to consent to the range of permissions the AutomationEngine might exercise when running workflows with you as the actor.
* These permissions are tied to the permissions you already have and can never exceed them.

### Actor updates

A user who updates a workflow is set as the actor automatically. This prevents exploits where a user changes a workflow to achieve something in another user's context.

* The actor remains unchanged if either the workflow update happens by a user in **Workflow admin** mode, or the actor is set to a service user.
* You can only use service users which are granted to you.

### Service users

By default, the workflow actor is the user who created the workflow. However, there is the option to select a non-interactive service user as the actor of a workflow. This makes the workflow independent of the status of the user who maintains it.

We highly recommend using service users as actors for all workflows that are worked on collaboratively and serve a production grade use case.

Service users and their permissions are managed by admins through [Identity and Access Management](/docs/manage/identity-access-management/user-and-group-management/access-service-users "Service users"). We highly recommend granting a service user only the permissions that are required for the intended usage scenario.

To set the workflow actor to a service user

1. Open the workflow in the workflow editor.
2. Select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **Settings**.
3. Select the service user from the **Actor** list.
4. Save your changes.

The user editing a workflow needs the `iam:service-users:use` permission to use a service user as an actor. You can create a policy as follows to allow specific service users.

```
ALLOW iam:service-users:use



WHERE iam:service-user-email IN ("<SERVICE_USER_1_EMAIL>", "<SERVICE_USER_2_EMAIL>");
```

For more information, see [Service users](/docs/manage/identity-access-management/user-and-group-management/access-service-users "Service users")