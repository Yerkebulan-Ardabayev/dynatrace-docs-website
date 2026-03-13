---
title: Get notified about workflow changes
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/manage-workflows/workflows-notifications
scraped: 2026-03-06T21:32:34.815912
---

# Get notified about workflow changes

# Get notified about workflow changes

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Oct 07, 2025

Get notifications about changes to your workflow, such as edits, deletions, execution failures, and throttle limits.

## Turn on notifications

Notifications are not turned on by default.

To turn on notifications for a workflow navigate to the relevant workflow.

1. Select .
2. Select **Turn on notifications**.

   ![Screenshot of a workflow with notification.](https://dt-cdn.net/images/umsaywsjuo-dev-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-send-email-1-view-draft-1968-27572da6b3.png)

## Details

When you turn on notifications, you receive email notifications for the following scenarios:

* Workflow edits or deletions
* Workflow failures
* Hourly execution throttle limit

### Workflow edits or deletions

Notifications are sent when a workflow is edited or deleted, provided the following conditions are met:

Notifications are sent when:

* Someone else edited a live workflow.
* Someone else deleted a workflow.

### Workflow failures

A notification is sent when a workflow execution fails if that workflow has already had at least one successful execution.

### Hourly execution throttle limit

A notification is sent when a workflow hits its hourly execution throttle limit.
This ensures awareness about potential interruptions in workflow execution.

## Turn off notifications

To turn off notifications for workflow, select  > **Turn off notifications**.

## Related topics

* [Workflows quick start guide](../quickstart.md "Build and run your first workflow.")
* [Create workflows in Dynatrace Workflows](../building.md "Create and edit workflows in Dynatrace Workflows.")
* [Manage workflows](../manage-workflows.md "Manage your workflows")
* [Upload a workflow or a workflow template](workflows-upload.md "Upload your workflow or your template.")
* [Download a workflow or template](workflows-download.md "Download your workflow or your existing workflow as a template for an easy backup, to use locally or to share it to upload on a different tenant.")
* [Change ownership of a workflow](workflows-change-owner.md "Change ownership of your workflow.")
* [Manage live or draft workflows](workflows-manage-live-mode.md "Undeploy your workflow or download as Workflow or as a template.")
* [Compare and restore versions of a workflow](workflows-versioning.md "Compare and restore every version of your workflow.")