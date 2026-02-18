# Dynatrace Documentation: deliver/service-level-objectives

Generated: 2026-02-18

Files combined: 6

---


## Source: create-slo.md


---
title: Create service-level objectives
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/create-slo
scraped: 2026-02-16T21:32:10.969067
---

# Create service-level objectives

# Create service-level objectives

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Nov 05, 2024

With ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**, you can configure new service-level objectives (SLO)s from templates provided by Dynatrace.
You can also define your SLOs based on a custom [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") query.

## Steps

### Create an SLO from template

To create a new SLO with a predefined template

1. In **Dynatrace**, search for ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** and open it.
2. Select  **Service-level objective**.
3. In the SLO wizard, choose one of the following:

   * **Host CPU usage utilization**
   * **Service availability**
   * **Service performance**
   * **Kubernetes cluster CPU usage efficiency**
   * **Kubernetes cluster memory usage efficiency**
   * **Kubernetes namespace CPU usage efficiency**
   * **Kubernetes namespace memory usage efficiency**
4. Select **Create** for one of the above options.
5. Choose the entities that should meet your objective. If you're using the **Service performance** template, enter a value in milliseconds in **Requests should be faster than**.
6. Optional Select segments , choose the required segment(s), and select **Apply**. This reduces the number of filter results.

   ![Add segments filter to the SLO](https://dt-cdn.net/images/slo-level-segments-1313-399767711c.png)

   This is only an additional filter for the required entities. It does not apply to the SLO evaluation. To add the segment filter to the SLO evaluation, use step 5 in the [Create a custom SLO](/docs/deliver/service-level-objectives/create-slo#create-a-custom-slo "Create and configure service-level objectives (SLOs).") section.
7. Select **Next**.
8. Define the criteria of your SLO. Fill in the **Target** field and select the timeframe for the evaluation period by using the dropdown in the **Over the evaluation period** field.
9. Optional Turn on **Show warning** and enter the numeric percent in **Show warning at** field.
10. Select **Next**.
11. Enter a name for your SLO in **SLO Name**.
12. Optional Provide a meaningful description of what your SLO is about in **SLO description**.
13. Optional Provide tags for your SLO in the **Tags** section by filling in the **Key** and **Value** fields. Select **Add** to save the tags. Tags can be used to provide additional metadata for your SLOs, such as a responsible ownership team or additional information about the underlying entities or criticality of your SLO.
14. Select **Save**.

### Create a custom SLO

1. In **Dynatrace**, search for ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**.
2. In the overview of **Service-Level Objectives**, select  **Service-level objective**.
3. Select  **Custom SLO**.
4. Provide your DQL query. Your query has to include an "sli" field like in the following example, to ensure consistent visualization, transformation, and aggregation across your SLOs. The "sli" field needs to return an array of `double` type. The DQL query can be based on any data type in Grail, such as events or logs. Using the [makeTimeseries](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") provides the possibility to create an sli time series that can be used for calculating the SLO status.

```
timeseries { total=sum(dt.service.request.count) ,failures=sum(dt.service.request.failure_count) }



, by: { dt.entity.service }



, filter: { in (dt.entity.service, { services }) }



| fieldsAdd sli=(((total[]-failures[])/total[])*(100))
```

5. Optional Select segments , choose the required segment(s), and select **Apply**. This is an additional filter to the query.

   The selected segments are stored with the SLO definition. Those filters are effective with future segment modifications and new entity creations with the same DQL query.
6. Select **Next**.
7. Define the criteria of your SLO. Fill in the **Target** field and select the timeframe for the evaluation period by using the dropdown in the **over the evaluation period** field.
8. Optional Turn on **Show warning** and enter the percentage in **Show warning at**.
9. Select **Next**.
10. Provide the name for your SLO in the **SLO Name** field.
11. Optional Provide a meaningful description of what your SLO is about in the **SLO description** field.
12. Optional Provide tags for your SLO in the **Tags** section by filling in the **Key** and **Value** fields. Select the **Add** button to save the tags. Tags can be used to provide additional metadata to your SLOs, such as a responsible ownership team or additional information about the underlaying entities or criticality of your SLO.
13. Select the **Save** button to create your SLO.

## Create and manage SLOs via API

You can create, edit, list, delete, and evaluate your SLOs via API.

1. Go to Dynatrace.
2. In the [platform search](/docs/discover-dynatrace/get-started/dynatrace-ui#search "Navigate the latest Dynatrace"), type `API`. In the search results, see **Support resources** section and **Dynatrace API** below it.
3. Select **Dynatrace API** to access the Dynatrace API documentation. A new page opens with the Dynatrace API definitions.
4. In the upper right corner, go to **Select a definition**.
5. From the drop-down list, choose the endpoint.
6. Authenticate with your API token. For more details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").


---


## Source: service-level-objective-permissions.md


---
title: Permissions for service-level objective (SLO) tiles in a dashboard
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-permissions
scraped: 2026-02-17T21:28:59.049319
---

# Permissions for service-level objective (SLO) tiles in a dashboard

# Permissions for service-level objective (SLO) tiles in a dashboard

* Latest Dynatrace
* 1-min read
* Published Nov 24, 2024

You need the following permissions for service-level objective (SLO) tiles in a dashboard

For **Edit**

* `slo:slos:read` ârequired for reading all SLOs to show them in the dropdown selector
* `slo:slos:write` ârequired for showing the  **Service-level objective** button
* `slo:slos:write`, `slo:slos:read`, and the Grail permissions you need for your specific query. For more information, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

For SLO tile evaluation

* `slo:slos:read` and the Grail permissions you need for your specific query. For more information, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

For the SLO details view

* `slo:slos:read`, `slo:objective-templates:read`, and the Grail permissions you need for your specific query. For more information, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").


---


## Source: service-level-objective-tile-add-to-dashboard.md


---
title: Add a service-level objective (SLO) tile to a dashboard
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-tile-add-to-dashboard
scraped: 2026-02-18T05:56:48.158733
---

# Add a service-level objective (SLO) tile to a dashboard

# Add a service-level objective (SLO) tile to a dashboard

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Nov 19, 2024

With ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**, you can add your service-level objective (SLO) as a tile to a dashboard to visualize and monitor it.

## Steps

### Add an SLO from the SLO overview

1. In **Dynatrace**, search for ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**.
2. In the **Service-level objectives** table, find your SLO and, in the **Actions** column, select  >  **Add to Dashboard**.

   ![Add a Service-level objective](https://dt-cdn.net/images/chrome-83tpev8kjz-205-6d208f9a7d.png)
3. In the **Select destination** window, select your document and **Confirm** to add the tile to an existing dashboard, or select **New dashboard** to create a new dashboard for your SLO.

![Screenshot of Select destination dialog](https://dt-cdn.net/images/wtp95711-dev-apps-dynatracelabs-com-ui-apps-dynatrace-dashboards-intent-add-slo-to-dashboard-1-2445-1726e627fe.png)

An SLO tile showing the SLO status, error budget, and target is available on your dashboard.

### Add an SLO from your dashboard

Add and edit your SLO directly from ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and create a [new dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#create-dashboard "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or select an [existing dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboard-display "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
2. You can add an SLO using the Shift+S keyboard shortcut, or in the upper-right corner of the dashboard, select the plus sign .

   ![Add an SLO tile from your dashboard](https://dt-cdn.net/images/chrome-ftp3kxoqkt-736-3ea4751a06.png)
3. From the **Create new tile** drop-down list, choose  **Service-level Objective**.

   The **Service-level objective** panel is displayed.
4. In the edit panel for your SLO tile, select your SLO from the **Service-level objective** list. Alternatively, you can add a new SLO or edit an existing SLO using the **Add SLO** and **Edit SLO** options. You can perform these actions from the same window without leaving the Dashboard application.

The SLO name is used as the title of your dashboard tile. You can edit the tile title, in which your tile will have a different title from your SLO. (The SLO name won't be changed.)

![Screenshot of  Service-level objective panel with the Data tab link to the SLO list](https://dt-cdn.net/images/new-slo-in-dashboard-2907-a5f32f2b0c.png)

1. In the **Visual** tab, you can select or deselect the **Data mapping** **Columns** to display for your SLO which are **Status**, **Error budget**, **Target** and **Evaluation period**.
2. In the **Visual** tab, **Service-level objective options** section, you can toggle the **Show labels** option to display them. You can also toggle to **Apply status threshold color to** either the SLO **Value** or the **Background**.

   ![Screenshot of Service-level objective panel with the Visual tab](https://dt-cdn.net/images/wtp95711-dev-apps-dynatracelabs-com-ui-apps-dynatrace-dashboards-dashboard-f8f0ee42-e4a3-4b63-a3af-ca753060d7f7-3-2400-a36ac46dc8.png)

The tile won't be functional until you select an SLO. For more information, see [Edit a service-level objective (SLO) tile in a dashboard](/docs/deliver/service-level-objectives/service-level-objective-tile-edit-in-dashboard "Edit your service-level objective tiles directly in your dashboard.").

You added your new SLO tile to your dashboard.

Changing the dashboard's timeframe does not affect the SLO evaluation timeframe; it has no effect on the SLO status, which is always evaluated against its own evaluation period.

### Add segment filter to SLO in Dashboards

1. Add an SLO to the Dashboard according to the [Add an SLO from your dashboard](/docs/deliver/service-level-objectives/service-level-objective-tile-add-to-dashboard#tiles-add-from-dashboard "Visualize your service-level objectives by adding them to a dashboard.") section.
2. Select segments , choose the required segment(s), and select **Apply**.

   ![Add segments filter to Dashboard-level SLO](https://dt-cdn.net/images/dashboard-level-slo-segments-1971-8ef61073f5.png)
3. The SLO visualization automatically contains the dashboard-level segments in its evaluation.

Dashboards-level segments and SLO-level segments can be used at the same time. The final result will be an intersection of these two selections. Depending on the selected segments, the SLO evaluation contains:

1. A common result set for the Dashboard-level and the SLO-level.
2. No results if there are no intersections between the segments.

Example:

* Segment A: has entities S-1 and S-2
* Segment B: has entities S-2 and S-3

Due to the intersection, the result contains only the evaluations related to S-2.


---


## Source: service-level-objective-tile-edit-in-dashboard.md


---
title: Edit a service-level objective (SLO) tile in a dashboard
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-tile-edit-in-dashboard
scraped: 2026-02-17T21:25:57.015501
---

# Edit a service-level objective (SLO) tile in a dashboard

# Edit a service-level objective (SLO) tile in a dashboard

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Nov 24, 2024

You can configure and edit your service-level objective (SLO) tiles directly in **Dashboards** ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") to visualize them exactly how you want them.

## Steps

### Edit a tile

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. Select the dashboard with your SLO.
3. In your dashboard, hover over and click your SLO to display the SLO tile actions.

   ![Screenshot of Edit a service-level objective tile](https://dt-cdn.net/images/empty-slo-tile-2400-b7b459694a.png)
4. Select  **Edit**.
5. Edit the tile in the edit panel on the right.

   Changing the selected SLO will change the title to the selected SLO name.

   ![Screenshot of  Service-level objective panel with the Data tab link to the SLO list](https://dt-cdn.net/images/new-slo-in-dashboard-2907-a5f32f2b0c.png)

   1. In the **Visual** tab, you can select or deselect the **Data mapping** **Columns** to display for your SLO which are **Status**, **Error budget**, **Target** and **Evaluation period**.
   2. In the **Visual** tab, **Service-level objective options** section, you can toggle the **Show labels** option to display them. You can also toggle to **Apply status threshold color to** either the SLO **Value** or the **Background**.

      ![Screenshot of Service-level objective panel with the Visual tab](https://dt-cdn.net/images/wtp95711-dev-apps-dynatracelabs-com-ui-apps-dynatrace-dashboards-dashboard-f8f0ee42-e4a3-4b63-a3af-ca753060d7f7-3-2400-a36ac46dc8.png)

### Duplicate a tile

You can duplicate one tile at a time or duplicate multiple tiles simultaneously.

To duplicate one tile

1. Select the tile to display the tile-specific commands.
2. Select  **Duplicate**.

   A copy of the tile is created on the current dashboard.

To duplicate multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to duplicate.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Duplicate**.

   The selected tiles are duplicated on the current dashboard.

### Delete a tile

You can delete one tile at a time or select and delete multiple tiles simultaneously.

To delete one tile

1. Select the tile to display the tile-specific commands.
2. On the tile command bar, select  **More actions** >  **Delete**.
3. In the **Are you sure you want to delete this tile?** message, select **Cancel** or **Delete**.

To delete multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to delete.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Delete**.
4. In the **Are you sure you want to delete this tile?** message, select **Cancel** or **Delete**.

### Copy and paste a tile

You can copy and paste tiles to the same dashboard or another dashboard.

To copy and paste one tile

1. Select the tile to display the tile-specific commands.
2. On the tile command bar, select  **Copy to clipboard**.

   The selected tile is copied to your clipboard.
3. Paste the tile (Ctrl-V).

   * You can paste the copied tile to the current dashboard, in which case it's the equivalent of  **Duplicate**.
   * You can switch to another dashboard and paste the copied tile there.

To copy and paste multiple tiles simultaneously

1. Click one tile to select it.
2. Ctrl-click additional tiles that you want to copy and paste.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. On the tile command bar, select  **Copy to clipboard**.

   The selected tiles are copied to your clipboard.
4. Paste the tiles (Ctrl-V) to the same dashboard or switch to another dashboard and paste them there.


---


## Source: service-level-objective-tile-view.md


---
title: View the details of a service-level objective (SLO) tile in a dashboard
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-tile-view
scraped: 2026-02-18T05:45:37.896176
---

# View the details of a service-level objective (SLO) tile in a dashboard

# View the details of a service-level objective (SLO) tile in a dashboard

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Nov 24, 2024

You can view details of your SLO tile in your dashboard.

## Steps

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. Select the dashboard with your SLO.
3. In your dashboard, select your SLO tile to display the SLO tile actions.

   ![Service-level objective tile screenshot shows the open with option](https://dt-cdn.net/images/chrome-kntow83har-947-3eec6f8cb7.png)
4. Select  >  **Open with**.
5. Select **Dashboards** to add the SLO to a dashboard.
6. Or select **Service-level Objectives** to view the SLO details.


---


## Source: service-level-objective-upgrade-classic.md


---
title: Upgrade Classic SLOs
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-upgrade-classic
scraped: 2026-02-17T05:00:51.250654
---

# Upgrade Classic SLOs

# Upgrade Classic SLOs

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Nov 10, 2025

Upgrade Classic SLOs

We strongly recommend upgrading your Classic SLOs from ![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic** to ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** to maximize capabilities and benefit from the newest enhancements.

Dynatrace offers an improved ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** (SLOs) experience, allowing you to define tailored Service-Level Indicators (SLIs) using all available data points. This upgrade provides greater flexibility, customization, and integration with Grail.

Dynatrace provides two Service-Level Objectives application types:

* [![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**](/docs/deliver/service-level-objectives "Discover the functionalities of the new Service-Level Objectives powered by Grail.") is our latest, Grail-powered application offering enhanced flexibility and customization options.
* [![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic**](/docs/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic.") is the previous application with limited capabilities.

The following examples show an SLO in ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** and multiple SLOs in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

![SLO in Dashboards](https://dt-cdn.net/images/2025-06-18-12-55-59-2870-02bc549b90.png)![Service availability SLO](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-3-2705-04466642b4.png)![User-conversion rate SLO](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-4-2638-97d276e660.png)

1 of 3

## Why upgrade?

The table below highlights the new functionality and shows the many reasons you should upgrade. It compares the capabilities of SLOs in ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** and ![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic**.

| Capability | SLOs Classic **Service-Level Objectives Classic** | SLOs **Service-Level Objectives** | Business impact |
| --- | --- | --- | --- |
| Supported input for SLI definition | Limited to built-in or custom-calculated metrics | Supporting all data types in Grail, incl. biz-events, logs, spans, and time series | SLOs allow a finer granular configuration and tailored definition of the SLI. |
| Segmenting, data filtering for SLO evaluation | ManagementZones | [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") | [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") allow detailed filtering of the dataset used for the SLO evaluation. |
| Adding SLO tags | â | SLO tags | Add SLO tags (key-value pairs) and then use them to filter SLOs when querying them via the API. |
| Customized dashboard tiles | Classic dashboard tile | New [dashboard SLO tiles](/docs/deliver/service-level-objectives/service-level-objective-tile-view "View your service-level objective (SLO) tile details directly in your dashboard.") | New [dashboard SLO tiles](/docs/deliver/service-level-objectives/service-level-objective-tile-view "View your service-level objective (SLO) tile details directly in your dashboard.") allow more visual customization options, including what data should be shown and colorized. An additional SLO wizard overview allows for creating and editing SLOs in Dashboards **Dashboards**. |
| Integration with other Dynatrace apps | Integrated with classic Dynatrace Apps | Integrated with latest Dynatrace Apps |  |

### Difference between SLO and Classic SLO

The main difference between the SLO and the Classic SLO is that the SLI in the SLO is represented as a single DQL query.
The DQL query allows extensive customization possibilities, unlike metric and entity selectors in the Classic SLO.

The benefits of DQL-based SLOs are as follows:

* Use any telemetry data in Grail. For more information, see [Upgrading Metrics](/docs/analyze-explore-automate/metrics/upgrade "Upgrade classic metrics to metrics powered by Grail to continue using your data retrieved with metric selectors, but with the added power of Grail and DQL.").
* Apply custom filters and advanced options [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").
* Benefit from simplified ratio calculations for SLI.

#### How core SLO components are defined in SLO and Classic SLO

An SLO typically shows specific characteristics you can configure in many possible ways.

The core SLO components are:

* **Service-level indicator (SLI)**: Time series showing percentage values (100% = ideal)
* **SLO target**: Threshold for success
* **Evaluation period**: Typically from 1 to 4 weeks
* **SLO status**: Aggregated result over the evaluation period
* **Error budget**: Acceptable deviation (100% â SLO target)

It's possible to set the following parameters:

* SLI

  + What data types are needed?
  + What fraction of the data needs to be considered?
* Evaluation period
* SLO target (threshold)

In ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**, the SLI is represented as a [DQL (Dynatrace Query Language)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") query.
It's flexible and uses contextual data to represent the objectives.

### SLO Classic example using Metrics selectors

Below is an example of a Classic SLO using the classic metric selectors, similar to a DQL query.

![Screenshot of a Classic SLO](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-classic-settings-ui-settings-builtin-monitoring-slo-gtf-2h-gf-all-id-ce2ea422-2364-3dd2-bb04-46dba36f44bc-1-1847-1327f5cb0a.png)

### SLO example using DQL

An SLO has two major parts: the **Custom DQL** and the **Preview**. In **Custom DQL** you can define your DQL query. In **Preview** you visualize the SLO.

#### Custom DQL

The SLO DQL query is structured in a certain way to define the SLO and SLI. The SLO DQL example snippet defined in the **Critical services or entities** tab of the SLO has the following characteristics:

* Define the data points.

  ```
  timeseries {total=sum(dt.service.request.count), failures=sum(dt.service.request.failure_count)},
  ```
* Specify the entity scope.

  ```
  by: { dt.entity.service }
  ```
* Display the information needed by using DQL filters.

  ```
  | fieldsAdd name = entityName(dt.entity.service)



  | filter in(name, "astroshop-checkoutservice", "astroshop-cartservice", "astroshop-paymentservice", "astroshop-shippingservice", "astroshop-currencyservice", "astroshop-frontend", "astroshop-recommendationservice")
  ```
* Calculate the SLI.

  ```
  | fieldsAdd sli = (((total[] - failures[]) / total[]) * 100)



  | fields timeframe, interval, dt.entity.service, name, sli
  ```

#### Preview

Check in **Preview** the SLO and SLI statuses.

![Screenshot of Dynatrace UI showing an SLI and SLO.](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-6-2658-349ab1cff7.png)

## Upgrade Classic SLOs to SLOs

To upgrade a Classic SLO to SLO

1. Map your Classic SLO metric expression to Grail.

   1. Check the comprehensive list in [Upgrading Metrics](/docs/analyze-explore-automate/metrics/upgrade "Upgrade classic metrics to metrics powered by Grail to continue using your data retrieved with metric selectors, but with the added power of Grail and DQL.").
   2. Use the [Metric selector conversion guide](/docs/analyze-explore-automate/metrics/upgrade/metric-selector-conversion "Learn about the various metrics that Dynatrace offers.").

   For complex metric expressions, you might need to adapt the DQL queries manually.
2. Convert the entity selectors to the corresponding [DQL statement](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). For more information, see [DQL best practices](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Best practices for using Dynatrace Query Language.").

   The following table shows the typical entity selectors for Classic SLOs and their equivalent in DQL.

   Entity selector classic

   DQL representation

   `type("SERVICE")`

   `by: {dt.entity.service}`

   `tag("myTag")`

   ```
   | fieldsAdd tags=entityAttr(dt.entity.service, "tags")



   | filter in(tags, "myTag")
   ```

   `entityId("SERVICE-XY")`

   ```
   | filter in(dt.entity.service, "SERVICE-XY")
   ```

   `entityName.contains/equals/in/startsWith("ENTITY-NAME")`

   ```
   | fieldsAdd name = entityName(dt.entity.service)



   | filter in/contains/startsWith/endsWith(name, "ENTITY-NAME")
   ```

   `mzId` / `mzName`

   Use [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.").

   Segments aren't related to permissions or access control.

   `toRelationship` / `fromRelationship`

   See the relationship mapping table in Grail: [Query monitored entities in Grail](/docs/platform/grail/querying-monitored-entities#relationship-mapping-table "Find out how to query monitored entities in Grail.").

   If you use management zones for permissions and access control, see [Grant access to entities with security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").
3. Enhance your SLI definition.

   While you can upgrade most Classic SLOs to a one-to-one match in Grail, consider enhancing your SLI definitions by leveraging options that are not available with traditional metric expressions.

   Take advantage of the new options:

   * Business hours
   * Key requests/endpoints in DQL
   * Advanced math operations
   * Use bisiness events as leading indicators
   * Add SLO tags for filtering and grouping
   * Use segments for dynamic entity scope

## Upgrade API integration

To automate SLO management and evaluation, use the dedicated API endpoints. Reference the table below to upgrade your API integration for Classic SLO to SLO leveraging the SLO Service Public API.

![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic**

![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**

[Service-level Objectives API classic](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.")

[SLO Service Public API](/docs/dynatrace-api/environment-api/service-level-objectives "Discover the API functionalities of the new Service-Level Objectives powered by Grail.")

## Upgrade via Configuration as Code

For scalable SLO management and evaluation, use [Configuration as Code overview](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.") on top of the SLO Service Public API.

To access the SLO Service Public API on your tenant

1. Go to Dynatrace.
2. In the [platform search](/docs/discover-dynatrace/get-started/dynatrace-ui#search "Navigate the latest Dynatrace"), type `API`. In the search results, see **Support resources** section and **Dynatrace API** below it.
3. Select **Dynatrace API** to access the Dynatrace API documentation. A new page opens with the Dynatrace API definitions.
4. In the upper right corner, go to **Select a definition**.
5. From the drop-down list, choose the endpoint.

* [Configuration as Code via Terraform overview](/docs/deliver/configuration-as-code/terraform "Manage your Dynatrace environment using Dynatrace Configuration as Code via Terraform.") support the SLO Service Public API since v1.78.0 and the Dynatrace Terraform provider can be found `dynatrace-oss/dynatrace | Terraform Registry`.
* [Configuration as Code via Monaco overview](/docs/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco.") supports the SLO Service Public API since v2.22.

## Whatâs next?

An automated upgrade flow is under consideration; however, due to the highly customized nature of SLOs, a manual review is expected to deliver the best results.
Use this opportunity to reassess and improve your SLIs, rather than simply copying them one-to-one.

For further optimization and guidance, contact your Dynatrace support team to maximize business impact from your service-level objectives.

## Related topics

* [Discover Dynatrace](/docs/discover-dynatrace "Discover Dynatrace")
* [Service-level objective templates](/docs/deliver/service-level-objectives/service-level-objective-templates "Explore the out-of-the-box service-level objective templates.")
* [Service-level objective examples](/docs/deliver/service-level-objectives/service-level-objective-examples "Explore the out-of-the-box service-level objective definitions by way of examples.")


---
