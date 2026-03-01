---
title: Problems app
source: https://www.dynatrace.com/docs/dynatrace-intelligence/davis-problems-app
scraped: 2026-03-01T21:07:19.795467
---

# Problems app

# Problems app

* Latest Dynatrace
* App
* 15-min read
* Updated on Feb 17, 2026

Quickly triaging, investigating, and remediating incoming incidents is the core challenge for operations teams. ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** supports them by automatically analyzing complex incidents, collecting all the context, and presenting the root cause and impact within a consistent view.

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, backed by data from Grail and Dynatrace Intelligence analysis, helps operational and site reliability teams reduce the mean time to repair (MTTR) by presenting every aspect of the incident.

Prerequisites

### Permissions

The following table describes the required permissions.

business-analytics:business-flows:read

Read evaluation of affected Business Flows

davis-copilot:conversations:execute

Execute copilot conversations

davis-copilot:document-search:execute

Execute copilot document search

davis:analyzers:execute

Execute problem details analyzer

document:documents:read

Read documents from Doc workflow

document:documents:write

Write documents in Doc workflow

document:documents:delete

Delete documents from Doc workflow

notification:notifications:read

Read notifications for alerting on saved filters

notification:notifications:write

Save notifications for alerting on saved filters

settings:objects:read

Read settings objects from Environment API

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Use cases

## Aim and context

This page shows you how to use ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** to triage detected problems and investigate their root cause and impact.

## Target audience

This page is written for:

* Operations engineers
* Pipeline engineers
* Systems engineers
* Site reliability engineers (SREs)
* Build automation engineers

## Summary

**Problems** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") streamlines triage, analysis, and remediation of active incidents by reducing the MTTR. It allows you to focus on AI-detected problems and quickly navigate to their root cause.

* The data provided by Grail and DQL makes it possible to slice and dice all problem-related information for huge amounts of problems and events.
* Integration with context-specific Dynatrace apps allows you to analyze problems without the need to switch the context.

## Investigate and remediate active problems

### Set focus and triage

By default, ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** shows:

* A feed of all problems in the last 2 hours. To help operation teams spot open problems regardless of which filter is set, open problems remain on top of the feed no matter how long they are open.
* A problem chart at the top visualizes any abnormality with a high number of problems in the past. Select a peak on the chart to drill into it and investigate further.

![An example of the Problems app problem feed view](https://dt-cdn.net/images/problems-app-problem-feed-view-1920-f7f665e813.png)

#### Filtering

To focus on your domain and triage problems that affect it, set filters. The three most common filtersâ**Status**, **Category**, and **Impact**âhave selectable settings to the left of the table for quick access. Your selections there automatically add the corresponding filters to the  filter bar above the table.

To set other filters, enter them directly in the filter bar.

* **Status**âCan be `Active` or `Closed`.

  + If this is not set, all problems (active or closed) are listed.
  + If you select a status in the controls on the left, the corresponding filter is also displayed in the filter bar.
* **Category**âIndicates the nature of the incident, such as slowdowns, errors, resource-related issues, or availability incidents.

  + If you select one or more categories in the controls on the left, the corresponding filters are also displayed in the filter bar.
* **Impact**âIndicates the type of the impacted area, such as frontends, services, infrastructure, or environments.

  + If you select one or more impact areas in the controls on the left, the corresponding filters are also displayed in the filter bar.

Filtering with the filter bar allows you to focus your feed on problems based on multiple criteria, such as status, number of affected entities, root cause entity, and more. Place your cursor in the input field to see all the available options. By default, filtering criteria are combined by the **AND** logic. For each criterion, Dynatrace Intelligence provides a list of suggested values, based on your problem feed.

For example, to see problems that are raised due to an increase of JavaScript errors and that persist for longer than 1 hour, use the following filter criteria:

* `Status=ACTIVE`
* `Duration>1h`
* `Category=Error`
* `Name=JavaScript error rate increase`

By using the filter bar, you can also narrow your feed to focus on specific impact areas (such as `Frontend`, `Service`, or `Infrastructure`) with the `Impact` parameter, or use text search to find problems that contain a specific string. To use search, you can:

* Input any text in the filter bar and select **Search in all data**.
* Enter `* ~ <your_text>` in the filter bar and select **Update**.

Fields considered for text search

The following fields in the problem record are considered for the text search:

* `event.id`
* `event.name`
* `event.description`
* `event.status`
* `display_id`
* `labels.alerting_profile`
* `entity_tags`
* `root_cause_entity_name`

The problem filter bar supports Boolean logic filters. This allows you to combine **AND** and **OR** criteria and create complex filters using parentheses to group Boolean terms. You can see a Boolean logic filter statement within ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** app in the example below.

![Powerful Boolean Filters within the Problems Filter Bar.](https://dt-cdn.net/images/complex-problem-filters-1920-db9346a85b.png)

#### Leverage predefined Team Segments to increase operational productivity

Segments are predefined filters used for quickly filtering the data to include only the relevant entries. In the context of ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, you or your team can utilize a predefined set of team-specific segments  to filter your problem tables instead of having to create your own problem filters.

The following example shows how to use segments to filter problems connected to easyTravel.

![Filter by segments in the Problems app.](https://dt-cdn.net/images/problems-filter-by-segments-1920-c5610b610e.png)

In addition, using segments in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** allows you to:

* Create sets of filters that can be reused by you and shared to the whole team.
* Save time on recreating filters applied during the previous sessions.
* Increase productivity by quickly filtering relevant problems.
* Quickly check the status of your service by creating and applying service-specific segments.

Since problems are stored as events in Grail, segments created for filtering problems must define an event filter. For example, if you want to filter problems that were raised in a specific cloud region, you can create a segment with the following event filter:

```
cloud.region = "us-east-1c" AND event.kind = "DAVIS_PROBLEM"
```

Screenshot example of defining a segment for Problems filtering

![An example of defining a segment for filtering problems in the Problems app.](https://dt-cdn.net/images/problems-segment-definition-1512-4649153a97.png)

Segment filters are directly applied to the problem Grail records. Consequently, no entity filters are applied to the problem unless the entity ID is chosen as a primary field of the filtered problem.

For more information on segments and how they work, see [Segments](/docs/manage/segments "Use segments to logically structure and conveniently filter observability data across apps.") ![Segments](https://dt-cdn.net/images/segments-256-8e66310720.webp "Segments").

### Activate auto refresh

To make sure you always catch incoming problems, use the refresh settings ![Refresh](https://dt-cdn.net/images/dashboards-app-refresh-33a794c2f1.svg "Refresh") ![Expand menu](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Expand menu") in the upper-right corner of ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.

* To automatically refresh the problem feed, select ![Expand menu](https://dt-cdn.net/images/dashboards-app-menu-expand-3398af0cdf.svg "Expand menu") and choose a refresh rate (or select `Off` to turn off automatic refresh)
* To manually refresh the problem feed at any time, regardless of the automatic refresh setting, select ![Refresh](https://dt-cdn.net/images/dashboards-app-refresh-33a794c2f1.svg "Refresh")

### Investigate and compare problems

To see the details of a problem

1. In the table, select the problem ID in the **ID** column.
2. Review the details page.

The problems details page provides all available details about the problem, highlighting the root cause entity with a red mark, to guide your attention to the right things. The example below shows details of a problem with user action degradationâincluding the root cause entity (`easyTravelBusiness` service) and a chart of abnormal response time of that service.

![Example of the problem detail view in the Problems app.](https://dt-cdn.net/images/problems-details-view-page-1920-3d5f2bb781.png)

All entities affected by the problem are listed in the **Affected entities** section, along with information about entity type and the number of events, detected during the analysis.

* As a suggestion for the starting point of the investigation, Dynatrace Intelligence marks the entity that it determined to be the root cause of the problem.
* To review details about an affected entity, select it in the table.

#### Compare multiple problems

If all the filters are applied and you still have multiple problems to investigate, you can select and compare the details of multiple problems.

1. In the table, use the checkboxes to select two or more problems.
2. Select **Show details**.

   This preloads the details of all selected problems and adds controls to the upper-right corner of the problem details page so you can quickly switch between each selected problem.

### Read event properties for additional information

Dynatrace receives events from multiple event sources, such as OneAgent, Synthetic, extensions, and ingestion APIs. Dynatrace accepts and understands various properties (also referred to as fields) of those events that provide additional information about the event.

Event sources can be customized to provide the information you need to analyze and remediate problems caused by the events. For example, linking the configuration that detected the event (`dt.settings.schema_id` and `dt.settings.object_id`) helps you to quickly adapt the threshold or baseline if such action is necessary.

Another example is adjusting the sensitivity of the custom alert that triggered the event by modifying the detector's configuration in the settings.

Since available event properties depend on the event's source, events that are not generated by custom alerts don't contain links to relevant event settings. If you want an event to link to a settings object, you can do so by attaching a `dt.settings.object_id` property to events ingested via API and/or extensions.

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** displays all event properties for each collected event in a table and provides intent links, such as direct navigation to a custom alert's configuration, as shown below.

![Problems app offering a direct link to settings object.](https://dt-cdn.net/images/problems-app-settings-direct-link-1920-b7ded7d7d3.png)

Examples of powerful event properties include:

* Event description (`event.description`). The event description supports Markdown-formatted text, enabling you to include links to resources that can help to remediate the problem.
* DQL query (`dt.query`) allows you to rebuild the event's chart in a notebook or at a dashboard or to copy the raw value of a property.
* Related entities (`dt.entity.*`) allow you to directly navigate to entities through the `dt.entity.*` properties.
* Link to a settings object (`dt.settings.object_id`) and settings schema (`dt.settings.schema_id`).

To learn more about the semantics and syntax of event properties and how they can be used across Dynatrace, see [Semantic Dictionary](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

### Analyze problems with your own tools by exporting CSV

For cases when your software tools create integration gaps preventing you from effective usage of Dynatrace data, we provide the ability to export problem feed data in the CSV format. You can later use this data in various tools, including spreadsheet programs, databases, and data analysis tools.

As illustrated below, you can export problem related-data from the problem feed table. You can also export it from **Notebooks** and **Dashboards** within all table visualizations.

![Export selected problems as a CSV file.](https://dt-cdn.net/images/problems-app-csv-export-1920-c5d456c07a.png)

You can export all loaded problems (up to a limit of 1000) or use the multi-select feature to choose specific problems. Additionally, the filter bar above the table allows you to filter through larger subsets of problems. The **Select all** checkbox helps you to export all problems in the filtered set of entries.

### Check the root cause without leaving your context

Depending on your team's responsibility, you might want to focus your attention on Kubernetes clusters, cloud resources, and workloads of critical services. To minimize context switching, Dynatrace offers consistent root cause information across multiple apps. No matter where your investigation starts, you don't have to switch to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** to see the root cause.

In the example below, the **Kubernetes** app displays information about a problem affecting a workload.

![Problem information integrated into the Kubernetes app.](https://dt-cdn.net/images/dynatrace-intelligence-in-k8s-app-1920-2da55950a8.png)

### Investigate all problem relevant logs

A Davis-analyzed problem highlights the root cause of an incident and shows all the incident-relevant log lines across multiple entities in the problem details.

To access the log lines that were collected during the incident, select the **Logs** tab. Additionally, you're able to see their log level across all entities affected by the problem, allowing you to save time on manual investigations and filtering logs of relevant entities separately.

The **Logs** tab also includes references to the affected entities and information about all related entities, such as parent hosts. To verify which entities are affected by the problem event, you can refer to all the event properties that start with the `dt.entity.` prefix.

See how **Logs** tab summarizes all problem-relevant logs in the image below.

![Dynatrace Intelligence Problems app log count.](https://dt-cdn.net/images/problems-log-count-1920-330dd46337.png)

The image below illustrates the further sorting of the log lines with the help of a DQL query.

![Dynatrace Intelligence Problems app error log lines.](https://dt-cdn.net/images/problems-error-log-lines-1920-cb4599df02.png)

### Visually notify and automate to speed up remediation

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** features a global problem indicator that shows the number of active problems within the environment and is always visible in the Dock. When the Dock is collapsed, a red dot is displayed next to the app icon instead of a number.

To personalize the indicator and the number of the displayed active issues, select filters in **Category** and save the filter configuration by selecting the  icon. The saved filter will automatically apply to the global problem indicator, reducing the number of problems counted for the user, as shown below. Selecting the **Default filter** button restores the last saved configuration.

![Saving filter configuration in Problems app.](https://dt-cdn.net/images/problems-app-notifications-config-save-1920-af4147c3c1.png)

While a problem filter is active, the indicator number will only show active problems from your chosen categories. The indicator updates on a one-minute schedule, which means that after the filter is updated, it can take some time for the indicator to adapt.

You can also set up email notifications for filtered problems using your email address by selecting the  icon, as shown below:

![Turning on email notifications for the filters applied in the Problems app.](https://dt-cdn.net/images/problems-app-turn-on-notifications-1920-6806895778.png)

The email notification is your personal setting, so you can enable it without the need for configuration permissions or the risk of impacting other users within the same environment.

The email notification is directly triggered within OpenPipeline, meaning only simple filters can be applied. Workflows that query ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** through DQL can use the complete feature set of Grail queries, such as joining tables.

If you need to send out customized email messages or have more complex automation and integration needs, you should apply a complete workflow along with the problem trigger.

### Visualize affected deployments to gather additional insights

The **Deployment** perspective equips operations teams with deeper insight into the infrastructure and cloud resources impacted by large-scale incidents. The root cause analysis feature automatically collects and visualizes affected deployments and related resources.

The additional context provided by related resources allows you to:

* Quickly understand where an affected resource resides, for example, a specific cloud region or Kubernetes cluster.
* Gather additional insight for multicloud deployments by showing an app's deployment across clouds, regions, and technology boundaries.

**Deployment** view uses a diagram similar to a Unified Modeling Language (UML) deployment diagram and follows a top-down approach, starting with the largest container element at the top and becoming more detailed as you drill down. The deployment structure is visualized as collapsible cards with horizontally overlapping elements, for example, services running in multiple regions. In this case, cards representing such services are duplicated and shown in multiple deployment stacks.

The deployment containing the root cause is automatically expanded and tagged with a red root cause badge, while all other deployments are collapsed by default. The deployment hierarchy is focused on a maximum of 5 levels, starting with the hierarchy leaf nodes at the bottom of the diagram upwards, seen in the example below:

![Dynatrace Intelligence Problems Deployment view with highlighted root cause.](https://dt-cdn.net/images/problem-deployment-view-1920-e646972d40.png)

Interactivity is a crucial feature of the deployment view. On the right side, you can click on any element to visualize findings, such as events related to the problem, along with a direct link to the selected entity. This structured approach allows you and your operations team to reduce the time needed to respond to incidents by navigating a familiar visual representation.

Not all incident-relevant related elements may show information on the right. Some elements, like the cloud region, are displayed for better context but may not necessarily show problem-relevant events.

### Define custom problem fields

Dynatrace Intelligence causal AI root-cause detection identifies and reports issues triggered by one or more events within a Dynatrace environment, and saves the results in the form of a problem record in Grail.

The problem record includes an array of event IDs (`dt.davis.event_ids`) that represents all the events collected and merged during the root-cause analysis. Event-related **Problems** table fields such as category, name, description, status, start, and end are derived from these events, which allows you to efficiently filter and sort all incoming problem records.

By default, Dynatrace propagates a set of built-in problem fields along with record-level permission fields, such as `dt.host_group.id`, `k8s.namespace.name`, `k8s.cluster.name`, onto problems. For the full list of built-in problem fields, see [Record level permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

Other built-in and custom event fields are not automatically propagated to avoid an excessive number of problem records.

In Davis events, permission policies based on Grail record-level permissions work as expected because the fields contain single values. However, when multiple events are aggregated into a problem, the values of the same field are combined into an array. Due to the current implementation of Grail record-level permission filters, only `dt.security_context` supports filtering array values. Other permission fields can't be used with array-based filters in permission policies.

This behavior differs from the DQL filter functionality, where array filters on array fields are fully supported. While this limitation may impact the flexibility of permission filters, itâs important to consider when you're managing permission policies.

* Dynatrace doesn't allow you to define problem field names that repeat existing [Semantic Dictionary](/docs/semantic-dictionary/model/davis#davis-ai-events "Get to know the Semantic Dictionary models related to Davis AI.") event field names.
* You can only define problem fields for source fields with values of type `string`. Fields that contain values of other types aren't supported.

#### Custom problem fields modification

To view or change the fields automatically propagated from events to problems, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Root cause analysis** > **Problem fields**. By modifying these problem fields, you can:

* Subscribe to custom record fields to be automatically propagated from all single events to any detected problem.
* Rename existing problem fields.
* Remove problem fields.

Renaming existing problem fields and removing problem fields changes current and future Grail problem records and may break your DQL queries.

To learn more about custom problem fields use cases, see [Dynatrace Intelligence Problems use cases](/docs/dynatrace-intelligence/davis-problems-app/problems-app-custom-problem-field-examples "Explore scenarios of how you can use custom problem fields in Problems.").

### Create a troubleshooting guide

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** allows you to create troubleshooting guides using ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** to document your investigation and the steps taken to resolve the problem. The guide is based on a predefined template and contains two types of sections:

* Sections with information extracted directly from the problem.
* Template sections (such as `Initial Response & Detection`, `Troubleshooting`, and `Remediation steps`) that you can edit to describe the process and steps followed to resolve the problem.

To create a troubleshooting guide

1. Go to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and open the problem you need to resolve.
2. On the problem details page, select **Troubleshooting**.
3. Select  **New**.

   * Select  **Notebooks** to create a new document in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
   * Select  **Dashboards** to create a new document in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
4. Follow the instructions in the template to document the details for your troubleshooting guide.

If you share a troubleshooting guide with all users in your environment, and you have enabled document suggestions based on vector similarity, Dynatrace Intelligence generative AI will index your document and proactively suggest it to your team to help them remediate similar problems faster. To learn more about Dynatrace Intelligence generative AI document suggestions, see [Find relevant documents with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides "Learn how Dynatrace Intelligence generative AI can suggest troubleshooting guides for problem remediation.").

The ability to create and share troubleshooting guides allows DevOps teams to:

* Share and spread their domain knowledge about specific business logic, software implementation, and infrastructure.
* Enrich the Dynatrace AI in their environment with shared knowledge for a more streamlined, tailored experience during problem investigation and remediation.
* Enrich the Dynatrace AI in their environment.

### Resolve the cases of missing events

Dynatrace offers a wide range of tools suited for your needs, such as configuring user group permissions, Dynatrace Intelligence alerting rules, or OpenPipeline ingestion rules. Due to the rich customization options, however, there are cases that might lead to events not being visible in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and differences in the number of affected entities in the available tabs. The most common reasons for events "missing" from ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** are:

* Difference in bucket retention period: you can configure your bucket retention period for the monitored data to last longer, so that the events related to the problem will be visible regardless of how long the problem has been in the open state. To learn more about configuring bucket retention period for monitored data, see [Retain trace data for long periods](/docs/observe/application-observability/distributed-tracing/data-retention "Create and assign buckets with custom data retention for your trace data in Grail.").
* Missing permissions necessary for viewing the event: check with your Dynatrace support group and ensure that you have necessary permissions. Ask the administrator to adjust permissions, so the event becomes visible to you.
* OpenPipeline ingestion rules dropping records: you can adjust OpenPipeline ingestion rules to prevent it from dropping any records or broaden the rules to keep records that might be connected to the alerted problem. To learn more about configuring OpenPipeline ingestion rules, see [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.").

### Streamline problem resolution with problems-specific drill-down options

![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** provides drill-down options that are designed to guide you toward the most relevant actions for resolving detected problems and help you streamline problem resolution.

Drill-down options available to you are displayed within the problem details view and depend on the type of the affected entity (such as service, Kubernetes workload, host, or AWS availability zone).

Some of the available drill-down options are:

* Analyze failures: Perform a focused failure analysis to identify the root cause of failure rates, error patterns, or performance issues.
* View related logs: Investigate relevant log entries directly within ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
* View failed traces: Analyze failed traces in ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** to understand the root cause of failures.
* View `app`: Navigate to the associated app's details page. The exact name is specific to the affected entity (such as View service, View Kubernetes workload, or View host).

To access drill-down options

1. In **Dynatrace**, go to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
2. Select the problem you want to investigate from the ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** overview. This opens a problem details page.
3. Optional On the left side of the problem details page, select the affected entity or infrastructure you want to investigate further. Usually, when you open the problem details page, the affected entity is pre-selected for you.
4. From the affected entity details on the right, select the preferred option for further investigation.

   * Select  > **View related logs** to continue the investigation without leaving ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.
   * Select  > **View failed traces** to continue the investigation in the [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.").
   * Select  > **View** `app` to continue the investigation in one of the available Dynatrace apps.
   * Select  > **Open with** to see all available investigation options.

Drill-down options provide you with seamless navigation between ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and other Dynatrace apps to ensure focus and continuity in problem resolution.

### Review problem overview

The **Overview** is a concise, executive summary of a detected problem.

To view a problem overview

1. Go to ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** and open the problem you need to resolve.
2. On the problem details page, select **Overview**.

   **Example**:

   ![Example problem details Overview tab](https://dt-cdn.net/images/problems-screenshot-with-overview-1920-6c68de3f34.png)

The **Overview** has four sections:

Customize the layout

You can move these sections around to personalize your view of the **Overview**.

1. In the header of the section you want to move, select  and drag the section.
2. Drop the section where you want it to appear in the layout.

These changes are saved per user. Your layout changes don't affect how others see the overview.

### Impact

The **Impact** section displays all impacted [Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") entities (for example, services, processes, and hosts) along with brief issue details for each entity.

The **Impact** section is categorized by:

* **Frontends**
* **Services**
* **Infrastructure**
* **Synthetic monitoring**
* **Environment**

### Root cause

The **Root cause** section focuses on the root cause of the issue, including detailed information about the affected deployment stack. This may include:

* The process and host where the root-cause service is running.
* The Kubernetes workload serving the impacted service.

To ensure consistency, the root-cause entity is also listed in the **Impact** table.

### Visual resolution path

The **Visual resolution path** section graphically illustrates the relationships between frontends, services, and backends involved in the issue.

* Each node represents a [Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") entity (frontend, service, or backend) where a health issue was detected.
* Gray nodes indicate related entities used in the analysis but not directly impacted.

This graph helps explain how Dynatrace AI identified the root-cause backend service.

To maximize your view of the graph, select  **Maximize**.

### Automation and remediation

The **Automation and remediation** section lists all automation workflows triggered by the problem. These workflows may include:

* Alert notifications sent to response teams.
* Remediation flows and runbooks for auto-remediation.
* External AI agent triggers, such as cloud platform SRE agents, to gather further insights or resolve issues within cloud vendor infrastructure.

The table provides key details for each workflow, including:

* The last trigger time (as workflows may run multiple times during problem updates).
* The execution state (for example, success or failure).

Workflow execution details are based on standard workflow execution events, which can also be queried using DQL in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

**Note**:

* Only users with system event read permissions can view workflow executions. Without these permissions, the table is empty and a message indicates the missing access.
* Workflows not shared with your user are listed but shown in gray without direct links, indicating restricted access.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Explore in Dynatrace Hub

Triage, investigate, and remediate incidences directly in ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.](https://www.dynatrace.com/hub/detail/problems/)