---
title: Configure and monitor service-level objectives with Dynatrace
source: https://docs.dynatrace.com/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo
---

# Configure and monitor service-level objectives with Dynatrace

# Configure and monitor service-level objectives with Dynatrace

* How-to guide
* 15-min read
* Updated on Mar 25, 2024

## SLO overview

The list of defined service-level objectives (SLOs) within a Dynatrace monitoring environment on the **Service-level objectives** page shows important information such as current status, error budget and [burn rate](#burn-rate), target, warning, the [number of open problems out of the total number of problems](#problems) for the SLO entity selector, and the timeframe during which the SLO is to be evaluated.

### Analyze problems

If there are any open problems associated with an SLO, the value in the **Open/total problems** column for the SLO is marked with a red warning symbol. Select the value to display the **Problems** page filtered by the respective entity selector. For more information on how to analyze problems, see [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.").

### SLO details

Expand the **Details** of an SLO for more information, such as:

* The metric and entity selectors of the SLO
* A graph representing the SLO evaluation over time
* A table view of the latest 10 evaluated SLOs belonging to a certain entity type. Switch to the table view to find out, for example, the exact value that is negatively affecting the result of the aggregated SLO evaluation, and the entity associated with it. Additionally, you can:

  + Sort the table view by status in ascending or descending order
  + Select any of the entities for further details on the respective entity page

By default, each SLO is evaluated according to its defined timeframe, but for what-if analyses with different timeframes, or for a retrospective view, you can temporarily switch to the global timeframe.

## Configure a service-level objective

To configure a new service-level objective, use the [SLO wizard](#wizard) to select from a set of Dynatrace preconfigured templates for common use cases. Alternatively, you can [create your own SLO definitions](#new).

### Add an SLO using the wizard

In Dynatrace, go to **Service-Level Objectives**, select **Add new SLO**, and step through the **SLO wizard** as described below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Select your indicators**](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#step-1 "Create, configure, and monitor service-level objectives with Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Define a filter**](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#step-2 "Create, configure, and monitor service-level objectives with Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Add success criteria**](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#step-3 "Create, configure, and monitor service-level objectives with Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Evaluate**](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#step-4 "Create, configure, and monitor service-level objectives with Dynatrace.")

#### Step 1 Select your indicators

* Select the desired SLO:

  + **Service-level availability** SLO, where service-level availability is measured by dividing the number of successful service calls by the total number of service calls.
  + **Service-method availability** SLO, where the service-method availability is measured by dividing the number of successful key request service calls by the total number of key request service calls.
  + **Service performance** SLO, where the service performance ratio is measured by dividing the number of `good` minutes and `total` minutes, via a metric expression.

    `good` minutes count the number of minutes during which the response latency is below the defined threshold.
  + **User experience** SLO, which is based on the Apdex measurement, representing the percentage of users who are **SATISFIED** out of the total number of users who are using a web or mobile application.
  + **Mobile crash-free users** SLO, which measures the percentage of crash-free users within your mobile applications.
  + **Synthetic availability** SLO, which represents the percentage of successful synthetic monitor executions related to the total number of executions.

  For more information on the use cases, see [Configuration examples of service-level objective definitions](/managed/deliver/service-level-objectives-classic/slo-definition-configuration-examples "Explore the out-of-the-box service-level objective definitions by way of examples.").
* Enter an **SLO name**.
* Enter a **Metric name**, for example `my_new_slo`, which will be used to create metric keys:

  + SLO status, for example, `func:slo.my_new_slo`.
  + SLO error budget, for example, `func:slo.errorBudget.my_new_slo`.
  + SLO normalized error budget, for example, `func:slo.normalizedErrorBudget.my_new_slo`.
  + SLO error budget burn rate, for example, `func:slo.errorBudgetBurnRate.my_new_slo`.

  You can chart these metric keys on all pages that allow using metrics, such as [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

  After creating the SLO:

  + The metric keys cannot be changed.
  + You can view the metric keys in the SLO details.
* Optional Configure the SLI metrics you want to add to your SLO.

#### Step 2 Define a filter

In the timeframe selector, scroll down to select a timeframe value for your SLO.

* To choose one of the existing values, select **Presets**.
* To create your own timeframe value, select **Custom**.

The [entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") is consistent with the [Dynatrace REST API query syntax](/managed/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API."). You can use filters on management zone ID/name, tags, entity name/ID/type, health state, or a combination of these. For management zones, you can choose from the list of accessible management zones.

After entering the entity selectors you want, you can test whether there aren't any mistakes by selecting **Preview** next to the entity selector bar.

#### Step 3 Add success criteria

Set the target percentage (**Failure**) and the warning percentage (**Warning**).

The warning percentage has to be between 100% and your SLO target percentage in order to be effective. For example, if your SLO target percentage is 99.00%, you need to set your warning percentage between 99.00% and 100% to get an early warning (as indicated by a yellow state).

To see how fast a service consumes an error budget, relative to the SLO, make sure [**Error budget burn rate**](#burn-rate) is turned on, and set the threshold values for the **slow-burn** and **fast burn** rates.

#### Step 4 Evaluate

After entering the success criteria values, select **Evaluate** to evaluate the SLO based on the entered values.

If everything is correct and you get no errors, you can select **Create** to save your configuration and add your new SLO.

After you complete the setup, the newly created service-level objective appears on the **SLOs** page.

### Create your own SLO

To set up your own service-level objective, go to **Settings**, select **Cloud Automation** > **Definition**, and select **Add new SLO**.

### Edit SLOs

To edit an SLO, in Dynatrace, go to **Service-Level Objectives**, find your SLO, and select **More** (**…**) > **SLO definition** in the **Actions** column.

### Normalize error budget

To see a normalized error budget for all SLOs, go to **Settings** > **Cloud Automation** > **Setup**, and enable **Normalize error budget**.

Take, for example, an SLO target of 95% with a current SLO status of 96%. If the normalization is turned on, the remaining error budget left is (status − target) ÷ (100 − target) × 100, for example, (96% − 95%) ÷ (100 − 95%) × 100.

## Error budget burn rate

The error budget burn rate shows how fast a service consumes an error budget, relative to the SLO. For example,

* A burn rate of `1` indicates that the service consumed 100% of the error budget during your SLO timeframe.
* A burn rate of `2` indicates that the service consumed double the error budget during your SLO timeframe.

Burn rate is calculated either for the past hour (if you select the SLO timeframe) or for the global timeframe value (if no SLO timeframe is selected).

### Set up an error budget burn rate

For an indication of how fast a service consumes an error budget, you can enable the burn rate visualization either from the [wizard](#wizard) or [settings page](#new) while creating the SLO.

At any time, you can change the threshold value or disable the burn rate visualization from the **SLO definition** of your SLO.

### Visualize the error budget burn rate

After you set up the error budget burn rate, there are several places in your environment where you can view it:

* On the SLO overview page, in the error budget column:

  + A slow-burn yellow icon is displayed when the burn rate value is between `1` and the fast-burn threshold you entered while creating the SLO.
  + A fast-burn red icon is displayed when the burn rate is greater than or equal to the fast-burn threshold you entered while creating the SLO.

  If burn rate visualization is enabled, but no icon is displayed, the burn rate is below `1`.
* In the details of an SLO.
* In [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").
* On your dashboard, if you [pin your SLO to your dashboard](#dash).

## Set up alerts

You can set up two types of alerts:

* SLO alerts are sent when an SLO status goes below the target value.
* Burn rate alerts are sent when the error budget of an SLO decreases at a specific rate.

Alerts can only be created based on metric events within the last hour. If you set the threshold to `10` for a burn rate alert, an alert will be generated when the burn rate exceeds `10` during the last hour.

* To set up an SLO alert

1. Go to **Service-Level Objectives**, find your SLO, and select **More** (**…**) > **Create alert**.
2. For **Select alert type**, select `Status`.
3. Name your alert and set a threshold value. If you don't set a value, the threshold is populated with the existing SLO target value.
4. Select **Create alert**.

* To set up a burn rate alert

1. Go to **Service-Level Objectives**, find your SLO, and select **More** (**…**) > **Create alert**.
2. For **Select alert type**, select `Burn rate`.
3. Name your alert and set the burn rate threshold.
4. Select **Create alert**.

Your newly created SLO or burn rate alert will appear on the **Metric events** page, where you can configure it further. For details, see [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Add SLOs to management zones

SLOs that don't belong to any [management zone](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") are visible to all users. If you add an SLO to a management zone, only users who have access to that management zone can see it on the **Service-level objectives** overview page.

* To add an SLO to a management zone

1. Go to **Settings**.
2. Select **Cloud Automation** > **Definition**.
3. Select **Add new SLO**.
4. In the **Entity selector** field, add the management zone [name](/managed/dynatrace-api/environment-api/entity-v2/entity-selector#mzname "Configure the entity selector for Environment API endpoints.") or [ID](/managed/dynatrace-api/environment-api/entity-v2/entity-selector#mzid "Configure the entity selector for Environment API endpoints.").
5. After entering all SLO details, select **Save changes** to save your configuration.

* To add an existing SLO to a management zone, see [Edit SLOs](#edit).
* To view SLOs belonging to a specific management zone, select the management zone using the filter button in the menu bar.
* To view the global SLOs regardless of any other selected management zone filter, turn on **Show global SLOs**. Global SLOs are SLOs that are visible to all users, regardless of their management zone permissions.

For more information on how you can control access to the SLOs in your environment by setting permissions, see [View and edit SLOs based on permission levels](/managed/deliver/service-level-objectives-classic/slo-mz-permissions#slo "Permissions required at the environment and management-zone level to manage service-level objectives.").

## Pin SLOs to your dashboard

After you define your objectives, you can add the SLOs to your dashboard to visualize their current status along with the remaining error budgets.

1. In Dynatrace, go to **Service-Level Objectives**, find your SLO, and select **More** (**…**) > **Pin to your dashboard** in the **Actions** column.
2. From the list, select an existing dashboard or **Create new dashboard**, and then select **Pin**.
3. Select **Open dashboard** to open the dashboard in edit mode with the SLO tile selected.
4. Adjust the tile configuration as needed.
5. Select **Done**.

## SLO dashboard tile

By default, an SLO tile evaluates and filters ![Variable](https://dt-cdn.net/images/dashboards-app-dashboard-add-variable-821b40325c.svg "Variable") the SLO timeframe instead of the selected global timeframe. You can override the timeframe used in the tile configuration to compare the global and the SLO timeframe. For details, see [View and add SLO dashboard tiles based on permission levels](/managed/deliver/service-level-objectives-classic/slo-mz-permissions#dash "Permissions required at the environment and management-zone level to manage service-level objectives.").

An SLO dashboard tile displays the **Status**, the **Error budget**, and the **Target**.

* If [problems](#problems) are associated with the SLO,  a red exclamation mark is shown on the bottom left of the tile.
* If the [error budget burn rate](#burn-rate) is enabled and the burn rate is higher than one, a status indicator icon  is displayed before the error budget value. The color of the status indicator icon depends on the SLO threshold.

An SLO tile is refreshed automatically. The [refresh rate](/managed/analyze-explore-automate/dashboards-classic#dashboardrefreshrates "Learn how to create, manage, and use Dynatrace Dashboards Classic.") of the tile depends on the applied timeframe.

If you reduce the size, the SLO tile will display less information. Selecting an SLO tile forwards to the SLO overview, filtered by the selected SLO.

### Edit and view the SLO dashboard tile

Select **View details** from the menu in the upper-right corner of the tile to see the SLO details.

Select **Edit tile** from the menu in the upper-right corner of the tile.configuration settings in the **Service-level objective** panel.

* **Select an SLO:**: select the SLO to display in this tile.
* **Title**: the title to display at the top of the tile. By default, the title is taken from the name of the selected SLO. Use **Title Size** to adjust the font size.
* **Max shown decimals**: the maximum number of decimal places (0–10) to display. The decimals are cut off/truncated, not rounded. The number of decimal places displayed is automatically adjusted to fit the tile size.

The toggle options are

* **Show metric names**: whether to display **Status**, **Error budget**, and **Target** under the values in the tile.
* **Show legend**: whether to display a legend for status colors: green for **Good**, yellow for **Warning**, red for **Bad**, gray for **No Data**.
* **Show problems indicator**: whether to display the problems indicator (a red exclamation mark  ) in the tile.
* **Colorize based on status**: whether to color the entire tile background (instead of values) based on the status. When this is turned on, the legend is hidden.
* **Title Size**: set the font size of the **Title** text: **Inherit** (default), **Small**, **Medium**, or **Large**.

The information shown in a tile depends on the size.

* All information is shown if the tile size is 8x4 or larger.
* If the tile is smaller, **Open/total problems**, **Error budget**, error budget burn rate, and **Target** are hidden.
* If the width is less than 4, the title is hidden.

### SLO dashboard tile filters

You can use the following filters to override dashboard settings for the selected tile.

* **Custom timeframe**: it's **Last 1 week** by default.
* **Custom management zone**: it's **All** by default.

Both the **Custom timeframe** and **Custom management zone** can be set in the global selectors, inside the dashboard **Tile filters** in the sidebar, or in **Edit tile**. For more information, see [Dynatrace dashboard timeframe and management zone settings](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

You can set your tile to query a remote environment. For more information, see [Create remote/multi-environment Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment "Create dashboards that display data from multiple Dynatrace environments.").

If a tile has custom filters, a filter  icon is displayed. Hover over the icon to list the filters, which can include **Timeframe**, **Management zone**, and remote environment settings.

#### SLO Data Explorer tiles compared

SLO tiles and Data Explorer tiles might show different values.

* Data Explorer tile values are rounded
* SLO tile values are truncated

### SLO dashboard tile permissions

You can see global SLOs. A global SLO is visible to all users and doesn't belong to a management zone. For information, see [add SLOs to the management zone](#mz)

You can also see the SLOs you have permission to access.

* When you edit an SLO, if you don't have access to a given management zone, SLOs in that management zone are not displayed in the **Select an SLO** list.
* If you open an existing dashboard that contains SLOs to which you don't have access, the SLO tiles display a message saying that permission is denied.

If the dashboard has an [anonymous access link](/managed/analyze-explore-automate/dashboards-classic/dashboards/share-dashboards#access-anonymous "Learn how to share your Dynatrace dashboards with others."), the user who created the link sets the permissions. Anyone can see the linked dashboard the same way the creator of the link can.

## Visualize SLO status by color

After pinning an SLO to your dashboard, the SLO status is indicated in the tile by a combination of text and text color.

To optionally enable SLO background colorization to reflect the SLO status

1. In Dynatrace, go to **Dashboards** and open the dashboard.
2. Select **Edit**.
3. Select the SLO tile that you want to colorize.
4. In the **Service-level objective** pane on the right, turn on **Colorize based on status**.
5. Select **Done**.

The background color of the SLO tile (instead of the text) then changes automatically to reflect the SLO status:

| Tile color | Status |
| --- | --- |
| Green | Good |
| Yellow | Warning |
| Red | Bad |

## Clone an SLO

Cloning an SLO allows you to create a new SLO reusing the configuration of an existing SLO.

To clone an SLO

1. Go to **Service-Level Objectives**.
2. Select the SLO that you want to clone, and then select **Action** > **Clone**.  
   The **Add new SLO** page is prefilled with the cloned SLO's settings.
3. Adjust the new SLO's settings where necessary, and then select **Create**.

## Show metrics in Data Explorer

To query and chart metrics, go to the service-level objective you want and select **Actions** > **View in Data Explorer**. For more information, see [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

### Limitations

* Data Explorer shows metric keys; it doesn't show transformations or filters.

## Davis alerting

Dynatrace Davis® provides quick notifications on anomalies detected, along with actionable root causes. If your SLO has turned red, this is most likely because Davis has already raised a problem for the underlying metrics, showing you the root cause.

Davis doesn't provide alerts for SLO target breaches, but for underlying metrics and SLO entities.

## Troubleshooting

The following are solutions to problems some people have.

* [Service-level objective (SLO) list takes a lot of time to load﻿](https://dt-url.net/og238b6)
* [Service-level objective (SLO): One resulting value is required, but the SLO definition delivers more than one﻿](https://dt-url.net/us4383g)
* [Service-level objective (SLO): Timeframe starts before the metric was created﻿](https://dt-url.net/cg638yh)
* [Service-level objective (SLO): No management zone selected﻿](https://dt-url.net/e883882)