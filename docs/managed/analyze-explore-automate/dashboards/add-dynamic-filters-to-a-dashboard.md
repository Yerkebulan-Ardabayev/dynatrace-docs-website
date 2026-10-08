---
title: Add dynamic filters to a dashboard
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/add-dynamic-filters-to-a-dashboard
---

# Add dynamic filters to a dashboard

# Add dynamic filters to a dashboard

* How-to guide
* 4-min read
* Updated on Oct 05, 2026

To give a dashboard a filter bar that filters all its tiles, follow the steps below.

You can add multiple dynamic filters to a dashboard. They're all displayed as filter options in the dashboard filter bar. For how several filters combine, see [Filter evaluation](/managed/analyze-explore-automate/dashboards/how-dashboards-scope-and-refresh-data#filter-evaluation "Learn how timeframe, management zone, and dynamic filter settings decide which data dashboard tiles show, and how often each tile refreshes.").

If a metric has multiple entity types, management-zone filtering isn't applied. The limitation affects metrics with the dimensions `dt.entity.monitored_entity` or `dt.entity.device_application`. For details, see [Filter metrics by management zone](/managed/analyze-explore-automate/metrics-classic/metrics-mz "How to filter metrics by management zone and related security considerations").

## Step 1 Open the Dynamic filters tab

The **Dynamic filters** tab of the **Dashboard settings** page is where you define and manage filters for a dashboard. You can open it from the **Dashboards** table or from the dashboard itself.

### From the Dashboards table

1. Go to **Dashboards**.
2. In the **Dashboards** table, find the dashboard you want to edit.
3. Select **More** (**…**) > **Configure** to open **Dashboard settings** for that dashboard.  
   If you don't see a **Configure** entry in the menu, you don't have edit rights for the selected dashboard.
4. Select the **Dynamic filters** tab.

### From the dashboard

If the dashboard has no filters yet, it displays the notice "No dynamic filters have been defined for this dashboard. Add dynamic filters or learn more." Select **Add dynamic filters** to go directly to the **Dynamic filters** tab.

If the dashboard already has filters, there's no such notice.

1. Select **Edit** in the upper-right corner of the dashboard.  
   If you don't see an **Edit** button, you don't have edit rights for the selected dashboard.
2. Select the **Settings** tab.
3. Select **Configure more**.
4. Select **Dynamic filters**.

![The Dynamic filters tab of a dashboard](https://dt-cdn.net/images/empty-dynamic-filters-tab-1072-a5cc3d3c6e.png)

The Dynamic filters tab of a dashboard

## Step 2 Add filters

Custom dimension filters and generic tag filters apply only to tiles that you create in [Data Explorer](/managed/analyze-explore-automate/explorer "Explore Data Explorer topics, from creating and editing metric queries to learning advanced query syntax and resolving common issues.") and pin to the dashboard. They don't apply to standard tiles that you drag to the dashboard from the **Tiles** pane in the dashboard editor, or that you pin to the dashboard from another page such as **Hosts**.

1. On the **Dynamic filters** tab, select **Add filter**.
2. Select a filter from the **Filter criteria** list.  
   Some filters require an additional value. When you make a selection in the **Filter criteria** list, Dynatrace displays an additional entry field. The sections below describe the values for each such filter.
3. Repeat these steps for each filter you want to add to the dashboard.

### Filter by operating system

Select `OS type` from the **Filter criteria** list. The operating system filter requires no additional value.

### Filter by application tag key

To filter a dashboard by tags, first tag the components in your environment to which your dashboard applies, such as applications, hosts, services, process groups, or process group instances.

1. Go to **Settings** and select **Tags** > **Manually applied tags**.
2. Enter key/value pairs and apply them to each application to which your dashboard applies, for example, the key `demo-key-01` with the values `demo-value-01`, `demo-value-02`, and `demo-value-03`.

   Show me

   ![Dashboard filtering: apply demo-key-01/demo-value-01](https://dt-cdn.net/images/dashboard-filter-tag-demo-value-01-829-16ff5993a9.png)

   Dashboard filtering: apply demo-key-01/demo-value-01

   ![Dashboard filtering: apply demo-key-01/demo-value-02](https://dt-cdn.net/images/dashboard-filter-tag-demo-value-02-824-aba96ce516.png)

   Dashboard filtering: apply demo-key-01/demo-value-02

   ![Dashboard filtering: apply demo-key-01/demo-value-03](https://dt-cdn.net/images/3ashboard-filter-tag-demo-value-03-827-2650767241.png)

   Dashboard filtering: apply demo-key-01/demo-value-03
3. On the **Dynamic filters** tab, select **Add filter**.
4. From the **Filter criteria** list, select `Application tag key`.
5. In **Tag key**, enter the key you applied to your applications, for example, `demo-key-01`.

![Dashboard filtering: add application tag to dashboard](https://dt-cdn.net/images/dashboard-filter-add-app-tag-1134-64e29654e7.png)

Dashboard filtering: add application tag to dashboard

### Filter by custom dimension

1. From the **Filter criteria** list, select `Custom dimension`.  
   Dynatrace displays the **Dimension key** list.
2. Select or enter a value for **Dimension key**.

### Filter by generic tag key

1. From the **Filter criteria** list, select `Generic tag key`.
2. Set **Display name** to a unique name that identifies this generic filter, for example, `Application name`.
3. Set **Tag key**, for example, `appName`.
4. Set **Get suggestions from** to define where to get tag suggestions, for example, `Host`.
5. Under **Entity types affected by tag**, select **Add entity type** once for each kind of entity that this tag affects.

## Step 3 Save and apply the filters

1. Select **Save changes**.
2. Display the dashboard.  
   The dashboard displays a filter bar under its name. With no filter set, the tiles display data for your whole environment.
3. In the filter bar, select a filter, and then select a value.  
   For an application tag filter, select the filter, the tag key, and then a value. You can add other key/value pairs to the same filter, and you can apply a generic tag filter more than once under the same generic tag.

   ![Dashboard filtering: select application tag value in dashboard](https://dt-cdn.net/images/select-value-635-7f55e8621b.png)

   Dashboard filtering: select application tag value in dashboard

Your selection filters the dashboard tiles. For example, an operating system filter set to `Windows` makes the **Host health** tile display only the Windows hosts in the environment. If you drill down from a tile, the target page, such as **Applications**, opens with the selected filter applied.

To check which filters are applied to a tile, hover over the filter icon in the upper-right corner of the tile. The tooltip lists the applied filters, such as `Operating system: Windows`.

![Dashboard filter tooltip](https://dt-cdn.net/images/file-filter-hover-237-031a080875.png)

Dashboard filter tooltip

## What's next

* Learn how dashboard filters combine with each other and with Data Explorer filters in [How dashboards scope and refresh data](/managed/analyze-explore-automate/dashboards/how-dashboards-scope-and-refresh-data "Learn how timeframe, management zone, and dynamic filter settings decide which data dashboard tiles show, and how often each tile refreshes.").
* [Organize dashboards](/managed/analyze-explore-automate/dashboards/organize-dashboards "Filter the Dashboards table, mark favorites, add tags, hide dashboards you don't need, and find little-used dashboards to clean up by popularity.") with tags, favorites, and management zones.