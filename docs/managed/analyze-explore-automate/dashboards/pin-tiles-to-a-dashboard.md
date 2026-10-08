---
title: Pin tiles to a dashboard
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/pin-tiles-to-a-dashboard
---

# Pin tiles to a dashboard

# Pin tiles to a dashboard

* How-to guide
* 5-min read
* Updated on Oct 05, 2026

To put a view from another Dynatrace page, or a Data Explorer chart, on a dashboard as a tile, follow the steps below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Pin a filtered page**](/managed/analyze-explore-automate/dashboards/pin-tiles-to-a-dashboard#pin-filtered-page "Pin a filtered Dynatrace page or a Data Explorer chart to a dashboard as a tile, then update, copy, or clone that tile to other dashboards.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Pin a Data Explorer chart**](/managed/analyze-explore-automate/dashboards/pin-tiles-to-a-dashboard#pin-data-explorer-chart "Pin a filtered Dynatrace page or a Data Explorer chart to a dashboard as a tile, then update, copy, or clone that tile to other dashboards.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Update a filtered tile**](/managed/analyze-explore-automate/dashboards/pin-tiles-to-a-dashboard#update-filtered-tile "Pin a filtered Dynatrace page or a Data Explorer chart to a dashboard as a tile, then update, copy, or clone that tile to other dashboards.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Pin as new tile**](/managed/analyze-explore-automate/dashboards/pin-tiles-to-a-dashboard#pin-as-new-tile "Pin a filtered Dynatrace page or a Data Explorer chart to a dashboard as a tile, then update, copy, or clone that tile to other dashboards.")[![Step 5 optional](https://dt-cdn.net/images/dotted-step-5-52040ae237.svg "Step 5 optional")

**Clone tiles**](/managed/analyze-explore-automate/dashboards/pin-tiles-to-a-dashboard#clone-tiles "Pin a filtered Dynatrace page or a Data Explorer chart to a dashboard as a tile, then update, copy, or clone that tile to other dashboards.")

## Step 1 Pin a filtered page

You can create a dashboard tile from any Dynatrace page that includes a **Pin to dashboard** button.

You need [edit permission](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") for the target dashboard. If you don't have a dashboard yet, [create one](/managed/analyze-explore-automate/dashboards/create-a-dashboard "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.") first, which gives you edit permission for it.

This example pins a filtered view of the **Hosts** page.

1. Go to **Hosts**.
2. Set a filter on the list. In this example, set `Data center: Gdańsk, Poland`.

   ![Hosts page filtered to the hosts in the Gdańsk, Poland, data center](https://dt-cdn.net/images/filter-03-379-52198a4b6b.png)

   Hosts page filtered to the hosts in the Gdańsk, Poland, data center

   How to set a filter

   * For common filters, select a filter directly from the **Quick filters** column of the **Hosts** page. The quick filters are a subset of the available filters.
   * To specify any available filter, start typing on the **Filtered by** line to select a filter, and then select or enter a value.

     ![Filtered by line with the list of available host filters](https://dt-cdn.net/images/filter-01-325-2fe63fb62a.png)

     Filtered by line with the list of available host filters

     ![Filtered by line with the values for the selected filter](https://dt-cdn.net/images/filter-02-404-32504bda2e.png)

     Filtered by line with the values for the selected filter
3. Select **Pin to dashboard**.

   Dynatrace displays a preview of the tile and asks you to select the target dashboard. The list of dashboards is searchable: select the list, start typing to filter it, and then select the dashboard.

   ![Pin to dashboard dialog with a preview of the tile and the searchable dashboard list](https://dt-cdn.net/images/filtered-tile-01-382-0dbefb8cc5.png)

   Pin to dashboard dialog with a preview of the tile and the searchable dashboard list
4. Select a dashboard and select **Pin**.

   Dynatrace creates the tile and pins it to that dashboard.

   ![Confirmation that the tile is pinned, with the Open dashboard button](https://dt-cdn.net/images/filtered-tile-02-380-4c83bb3eb7.png)

   Confirmation that the tile is pinned, with the Open dashboard button
5. Select **Open dashboard**.

   The dashboard opens in edit mode with the new tile selected for editing. For a **Host health** tile, you can change these settings before you save it:

   * Optional Select whether to show a visualization on the tile.
   * Optional Select a custom timeframe.
   * Optional Select a custom management zone.
   * Optional Select an environment.

   ![New tile selected in edit mode, with its optional timeframe, management zone, and environment settings](https://dt-cdn.net/images/filtered-tile-03-1187-acc59a36d4.png)

   New tile selected in edit mode, with its optional timeframe, management zone, and environment settings
6. Select **Done**.

   The dashboard shows the new tile, which represents the hosts in the Gdańsk, Poland, data center.

   ![Dashboard showing the health of the hosts in the Gdańsk, Poland, data center](https://dt-cdn.net/images/filtered-tile-05-1186-285827111d.png)

   Dashboard showing the health of the hosts in the Gdańsk, Poland, data center

The filter is fully dynamic:

* When hosts join or leave the filtered set, or when their health changes, the tile updates automatically.
* Each hexagon on the tile represents a host. A green hexagon is a healthy host, and a red hexagon is a host with a problem. Hover over a red hexagon to see which host has the problem, or select it and then select **View host** to drill down to its details.
* To open the filtered **Hosts** page that you created the tile from, open the menu in the upper-right corner of the tile and select **View details**.

To put a bold label above the tile, add a **Header** tile. For details, see [Available tiles](/managed/analyze-explore-automate/dashboards/available-tiles "Look up every tile you can add to a dashboard, with what each tile displays, where it drills down to, and the settings it offers.").

## Step 2 optional Pin a Data Explorer chart

1. Go to **Data Explorer**.
2. Configure the query for the tile. You can build the query iteratively.

   * Select **Run query** after each query change to see its results.
   * Select different visualization types to see what works best for your query. The available visual settings depend on the query and the visualization you choose. For details, see [Visualization settings](/managed/analyze-explore-automate/explorer/visualization-settings "Look up each Data Explorer visualization, what it shows, its limits, its own settings, and the shared settings that carry over to dashboard tiles.").
3. Select **Pin to dashboard**, and then choose the destination dashboard and tile title.

   If you opened Data Explorer from a tile through **Configure tile**, you can instead select **Save changes to dashboard** to save your changes to the tile and dashboard you started from.
4. Select **Open dashboard** to see the tile on the dashboard.
5. Optional Change the tile title, or select a custom timeframe, a custom management zone, or an environment.

## Step 3 optional Update a filtered tile

1. On your dashboard, select the tile.

   The **Hosts** page opens with the tile's filter applied.
2. Add or delete filters.

   In this example, keep `Data center: Gdańsk, Poland` and add `Operating system: Linux`. When the filters change, the **Update dashboard tile** button is enabled.

   ![Hosts page with an added Linux filter and the Update dashboard tile button enabled](https://dt-cdn.net/images/filtered-tile-06-1431-274639b9a2.png)

   Hosts page with an added Linux filter and the Update dashboard tile button enabled
3. Select **Update dashboard tile**.

   Dynatrace saves the new filter settings to the tile. In this example, the tile shows the health of hosts that match `Data center: Gdańsk, Poland` and `Operating system: Linux`, and it opens the **Hosts** page with those filters.
4. To return to the dashboard, select the dashboard button in the upper-left corner of Dynatrace.

   ![Dashboard button that returns you to the current dashboard](https://dt-cdn.net/images/dashboardbutton-28-e3cbad6cfe.png)

   Dashboard button that returns you to the current dashboard

## Step 4 optional Pin as new tile

Instead of updating a tile, you can save a new copy of it. For example, you might want several similar tiles, each filtered for a different operating system.

1. Open the tile menu in the upper-right corner of the tile and select **View details**.

   The **Hosts** page opens with the same filters set.
2. Select **More** > **Pin as new tile**, and then select the target dashboard.

   * Select a different dashboard to have copies of the same tile on two dashboards.
   * Select the same dashboard to have two copies of the tile on one dashboard. You can then edit each copy to use a different management zone, timeframe, environment, or set of filters.

## Step 5 optional Clone tiles

Cloning saves work when you need several similar tiles. For example, to show three visualizations that differ only in the host they query, create the first visualization, refine its settings, and clone it twice. Then edit the clones to query the other two hosts.

1. Go to **Dashboards** and select the name of a dashboard to display it.
2. Select **Edit** in the upper-right corner of the dashboard.

   The dashboard opens in edit mode. If you don't see **Edit**, you don't have permission to edit that dashboard.
3. Select the tile you want to clone, or drag a selection rectangle around several tiles.
4. Clone the selection.

   * To add the copies to the current dashboard, select **Clone**, or **Clone x tiles** for several tiles.
   * To add the copies to another dashboard, select **Clone to**, or **Clone x to** for several tiles. In the **Where do you want to pin to?** window, select an existing dashboard or **Create new dashboard**, and then select **Pin**.
5. Edit the cloned tiles as needed.

   The cloned tiles appear on the dashboard you selected.

## What's next

* [Add dynamic filters to a dashboard](/managed/analyze-explore-automate/dashboards/add-dynamic-filters-to-a-dashboard "Add dynamic filters to a dashboard, such as operating system, tag key, or custom dimension filters, and then use the filter bar to filter all tiles on it.").
* [Share a dashboard](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") with the people who need its tiles.