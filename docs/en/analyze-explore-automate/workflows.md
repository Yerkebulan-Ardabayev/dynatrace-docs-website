---
title: Workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows
scraped: 2026-02-26T21:16:13.055479
---

# Workflows

# Workflows

* Latest Dynatrace
* App
* 4-min read
* Updated on Nov 18, 2024

![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** is a powerful tool that lets you automatically act on monitoring data.

A workflow is not intended for mass data ingestion or mass data export. For large-scale data processing, consider using [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") or building custom solutions with [Dynatrace Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.").

For more information, see the [quickstart example](/docs/analyze-explore-automate/workflows/quickstart "Build and run your first workflow.").

Prerequisites

### Permissions

The following table describes the required permissions.

hub:catalog:read

Read access to Hub apps.

document:documents:read

Read documents for workflow templates.

app-engine:apps:run

Enables listing all apps and reading the app bundles.

app-engine:functions:run

Enables usage of the function-executor.

automation:calendars:read

Read access to business calendars.

automation:calendars:write

Write access to business calendars.

automation:rules:read

Read access to scheduling rules.

automation:rules:write

Write access to scheduling rules.

automation:workflows:admin

Admin access to workflows and executions.

automation:workflows:read

Read access to workflows.

You might need additional permissions to run certain tasks in ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.

For a complete list of permissions needed to use ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, go to **Hub**, find and select **Workflows**, and go to the **Technical information** tab.

For more information about ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** security, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security "Guide on security aspects of workflow automation in Dynatrace Workflows").

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Concepts

Use cases

![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** is your entry point to manage and monitor workflows. The app interacts with the automation service via its REST API. The automation service is responsible for processing your workflows and keeping track of the executions.

### Workflow

A workflow specifies a repeatable process by assembling a series of tasks.

* The sequence of tasks is defined by their transitions, which allow for execution in series, in parallel, and with conditional paths.
* Workflows can be edited and monitored in a visual graph.

### Simple workflow

A simple workflow specifies a repeatable process with only one task.

* Reduced functionality workflow with only one task, limited logging for executions, limited task options and conditions, and no JavaScript tasks allowed.
* No additional costs for creating the workflow, as simple workflows don't consume workflow hours.

### Task

Each step in a workflow is called a task.

* A workflow keeps track of tasks and their order.
* A task defines a unit of work (for example, `Create Incident`, `Notify Ops in Slack`, or `Get error log count`), including the conditions, retry behavior, timeouts and, most importantly, the input configuration required to achieve the work and provide a result to be used by subsequent tasks.

### Action

An action is a generic, reusable function configured and triggered by tasks. For example, an action could be `Create Jira Issue`, while a task would execute the action with a specific configuration to `Create Bug in Sample project`.

* Actions are the tools to be assembled in your workflows to fit your custom process.
* Actions are provided out of the box by Dynatrace and partners and can be installed via Dynatrace Hub.

### Execution

Workflows, tasks, and actions all define how work should be done. An execution represents a specific instance of running through that process.

* An execution is triggered either by a schedule, by events, or manually via ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** or the REST API.
* Each execution of the same workflow might be different, depending on its parameters, inputs, and context.
* Each run of a workflow can be found as an individual entry in the **Executions** table.

To list past and ongoing executions

To list all executions in your environment, select **Executions** in the Workflows app header.

* To filter the table, you can specify a combination of

  + **Keyword**: a search string
  + **Workflow**: the name of the workflow as displayed in the UI
  + **Execution state**: `Success`, `Running`, `Error`, or `Waiting`
  + **Trigger type**: `Manual`, `Schedule`, or `Event`
  + **Timeframe**: a relative timeframe such as `Last 2 hours` or a custom timeframe with selectable From and To settings
* To list executions of a particular workflow, find the workflow in the table and select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > **View execution history** in the **Action** column.

To list executions of the workflow you are editing, select **Executions** in the editor.

## EdgeConnect

EdgeConnect allows you to reach your non-public services in workflow tasks. HTTP requests happening within any type of action or platform function can be proxied via EdgeConnect into the target network.

Any HTTP request (from your custom app, workflow, or an ad-hoc JavaScript code) that matches a defined host pattern is handled by an EdgeConnect instance you specify in the platform configuration. For more information, see [Configure and deploy EdgeConnect](/docs/ingest-from/edgeconnect "Use EdgeConnect to control how your apps and workflows interact with your internal systems.").

## Use cases

Workflows allows you to:

* Create **[agentic workflowsï»¿](http://https://www.dynatrace.com/hub/detail/agentic-workflows)**
* Automatically react to Dynatrace Intelligence events or security problems.
* Schedule reports in line with holidays and work hours.
* Orchestrate IT processes across your entire IT landscape.
* Connect to both cloud and locally-gated services.
* Combine out-of-the-box integrations with custom code.
* Visualize automated processes in a graphical workflow interface.
* Get live monitoring and a full audit trail for all automation executions.
* Define flow logic with custom conditions, automatic retries, loops, and parallel processing.

## Learning modules

The following learning modules show how you can use ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** to automatically act on monitoring data.

[01Workflows quick start guide

* How-to guide
* Build and run your first workflow.](/docs/analyze-explore-automate/workflows/quickstart)[02Create workflows in Dynatrace Workflows

* How-to guide
* Create and edit workflows in Dynatrace Workflows.](/docs/analyze-explore-automate/workflows/building)[03Create a simple workflow in Dynatrace Workflows

* How-to guide
* Build and run a simple workflow.](/docs/analyze-explore-automate/workflows/simple-workflow)[04Workflow triggers

* Overview
* Introduction to workflow automation triggers for workflows.](/docs/analyze-explore-automate/workflows/trigger)[05Run and monitor workflows created in Dynatrace Workflows

* How-to guide
* Run and monitor workflows created in Dynatrace Workflows.](/docs/analyze-explore-automate/workflows/running)[06User permissions for workflows

* Reference
* Guide on security aspects of workflow automation in Dynatrace Workflows](/docs/analyze-explore-automate/workflows/security)[07Workflows actions

* Overview
* Use Dynatrace ready-made actions for your workflows.](/docs/analyze-explore-automate/workflows/default-workflow-actions)[08Workflows Connectors

* Overview
* Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.](/docs/analyze-explore-automate/workflows/actions)[09Manage workflows

* Overview
* Manage your workflows](/docs/analyze-explore-automate/workflows/manage-workflows)[10Expression reference

* Reference
* Get to know the workflows expression](/docs/analyze-explore-automate/workflows/reference)[11Workflows use cases

* Overview
* Explore common Workflows use cases in Dynatrace deployments.](/docs/analyze-explore-automate/workflows/use-cases)

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Automate tasks in your IT landscape, remediate problems, and visualize processes.](https://www.dynatrace.com/hub/detail/automations?internal_source=doc&internal_medium=link&internal_campaign=cross)