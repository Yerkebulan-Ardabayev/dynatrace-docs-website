---
title: Synthetic for Workflows
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-for-workflows
scraped: 2026-02-21T21:20:01.916629
---

# Synthetic for Workflows

# Synthetic for Workflows

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 20, 2025

Synthetic for Workflows allows you to execute synthetic monitors on demand at selected locations within your workflows. Dynatrace can respond to any event and execute synthetic monitors within the workflows to assess its impact on user experience. Depending on the outcome, **Workflows** can notify the team by creating a Jira ticket, sending a Slack message, or initiating a remediation process.

With Synthetic for Workflows, you can choose which monitors you want to execute.

* A list of all available monitors.
* Monitors tagged with specific identifiers.
* Monitors assigned to particular frontend applications.

It is also possible to use [workflow expressions](/docs/analyze-explore-automate/workflows/reference#expressions "Get to know the workflows expression") to extract the list of monitors and locations from incoming events, which enables you to create reusable workflows.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install Synthetic for Workflows**](/docs/observe/digital-experience/synthetic-on-grail/synthetic-for-workflows#install "Enhance your automation capabilities with Synthetic Monitoring.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Grant permissions to Workflows**](/docs/observe/digital-experience/synthetic-on-grail/synthetic-for-workflows#permissions "Enhance your automation capabilities with Synthetic Monitoring.")

### Step 1 Install Synthetic for Workflows

To use Synthetic for Workflow actions, you first need to install **Synthetic for Workflows** from Dynatrace Hub.

1. In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), search for **Synthetic for Workflows**.
2. Select **Synthetic for Workflows** and select **Install**.

After installation, `synthetic_for_workflows` actions appear automatically in the **Choose action** section of [**Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").  
Before you begin, ensure that your monitors are properly defined. To create a new monitor, search for **Synthetic** in Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub").

### Step 2 Grant permissions to Workflows

The permission you need are listed in [Workflows](/docs/analyze-explore-automate/workflows#authorization "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."). Additionally, for executing **Synthetic for Workflows** you need the following permissions

```
environment:roles:manage-settings,



storage:buckets:read,



storage:events:read
```

Example policy:

```
ALLOW



app-engine:apps:run,



automation:workflows:read,



app-engine:functions:run,



automation:workflows:run,



automation:workflows:write,



environment:roles:manage-settings,



storage:buckets:read,



storage:events:read;
```

## Use `synthetic_for_workflows` action

### Select synthetic monitors

To select monitors from the list for Synthetic for Workflows, you need to specify the synthetic monitors that you want to execute when the workflow is triggered. You can choose the monitor from **Visual** or **From event**.
You can find the most relevant monitors by filtering the list by various criteria such as type, name, applications, and tags.

You can also

* Select **With specific tags** to browse through monitors with a particular tag.
* Choose **Assigned to frontend applications** to select monitors assigned to particular applications. You can find the available applications in the **Select frontend applications** list.

### Select a synthetic location

In **Select a synthetic location**

1. Select **Visual** or **From event**.
2. For **Visual** select a synthetic location from the dropdown list.
3. For **From event**, you can define the list of synthetic monitors you want to execute in the workflow based on the incoming event. To do this, you need to create an [expression](/docs/analyze-explore-automate/workflows/reference#expressions "Get to know the workflows expression") that enables the workflow to extract this information from the event and execute the selected monitors.

If you don't select any location, the monitor will be executed at the location defined in the monitor configuration.

### Add metadata

With the **Add metadata** section you can enrich your synthetic result with execution context, such as the application name, version, development stage, and build version.

To add metadata

1. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add")**Add metadata**.
2. Fill in **Key** and **Value** fields. In these fields, you can use [workflow expressions](/docs/analyze-explore-automate/workflows/reference#expressions "Get to know the workflows expression").
3. Your metadata saves automatically.

### Configure monitor execution

You can customize execution settings that will be applied to all executions within Workflows.

To do this switch on or off any of the following:

* Stop on problem
* Fail on performance issue
* Fail on SSL warning
* Take screenshots on success

### Configure workflow execution

You can configure workflow behavior if a Synthetic monitor batch execution fails.
This is done with the **Fail workflow task on failed batch execution** switch.

You can switch it on or off:

* On (  ): If monitor execution fails, the task fails.
  This can be combined with other configuration options, such as the **Retry on error** switch, to control workflow behavior according to the failing task.
* Off (  ): If monitor execution fails, the task completes successfully.
  The Synthetic for Workflows action generates results which can be used by the next task, for example [Site Reliability Guardian](/docs/observe/digital-experience/synthetic-on-grail/synthetic-for-workflows#synthetic-srg "Enhance your automation capabilities with Synthetic Monitoring.").

By default, this switch is off.

## Synthetic results in Grail

Note that Synthetic does **not** generate Grail events for non-DPS tenants. All processing will rely solely on API data. To learn more about DPS licensing, see [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

Results from synthetic monitors executed on-demand are stored as events in Grail.

There are three types of events:

* `batch_status` - contains the summary result of all the monitor executions within the batch
* `browser_monitor_execution` - contains detailed information for one browser monitor execution
* `http_monitor_execution` - contains detailed information for one HTTP monitor execution

## Integrate Synthetic for Workflows with Site Reliability Guardian

If you want to evaluate objectives based on the results from synthetic monitors, you can integrate [Site Reliability Guardian (SRG)](/docs/deliver/site-reliability-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") as the next action in your workflow.

To do this

1. Select the ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") on the `synthetic_for_workflows` task and then select **Site Reliability Guardian** from **Choose action**. This will trigger a `site_reliability_guardian_1` task.
2. Select the `site_reliability_guardian_1` task. In **Variables** provide the `batchId` parameter from the synthetic result and the `{{ result("synthetic_for_workflows_1")["event.id"] }}` value. You can replace `"synthetic_for_workflows_1_"` with any other task name.
3. In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), search for **Site **Reliability** Guardian**.
4. Select **+ Guardian** button.
5. In your guardian, select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") and select ![Summarize](https://dt-cdn.net/images/dashboards-app-menu-list-63d17138c9.svg "Summarize") **Variables**.
6. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Add variable**.
7. Type in `batchId` in the **Name** field. In the **Value** field, provide the default value. Select the **Add** button to save your changes.
8. On the right-hand side, fill in the **Guardian name**.
9. Select the ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Add new objective** and provide one of the following [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") queries.

Note that queries for synthetic events from outside the Synthetic application, such as those from Notebooks, Dashboards, and SRG, are **not** charged.

Use the following query to get the total duration of the whole batch.

```
fetch dt.synthetic.events



| filter event.id == $batchId



| fields batch_result.duration
```

Use the following query to check if the batch finished successfully.

```
fetch dt.synthetic.events



| filter event.id == $batchId



| filter batch.status == "Success"



| summarize count = count()
```

## Related topics

* [Updates to Synthetic attribute names](/docs/observe/digital-experience/synthetic-on-grail/synthetic-for-workflows/synthetic-event-formats "Required updates for Synthetic event attribute names in Workflows.")