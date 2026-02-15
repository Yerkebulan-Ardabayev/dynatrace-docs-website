---
title: Pin tiles to your dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard
scraped: 2026-02-15T09:10:58.493758
---

# Pin tiles to your dashboard

# Pin tiles to your dashboard

* How-to guide
* 5-min read
* Updated on May 16, 2022

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

You can automatically create a new dashboard tile from any Dynatrace page that includes a **Pin to dashboard** button. All you need is [edit permission](/docs/analyze-explore-automate/dashboards-classic/dashboards/share-dashboards "Learn how to share your Dynatrace dashboards with others.") for the dashboard. In this example, we create a new dashboard, so you are guaranteed to have edit permission.

## Create a dashboard

We start by creating an empty dashboard.

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select **Create dashboard**, enter a **Dashboard name** (in this example, use `Filtered Dashboard`), and select **Create**.  
   This creates the dashboard and opens it in edit mode.
3. Select **Done**.  
   Now we have an empty dashboard named `Filtered Dashboard`.

## Create a filtered tile

Now we create a tile based on a filtered view of the **Hosts** page and pin the tile to the empty dashboard.

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Set a filter on the list. In this example, we set `Data center: GdaÅsk, Poland`.

   ![Resulting filter](https://dt-cdn.net/images/filter-03-379-52198a4b6b.png)

   How to set a filter

   1. On the **Filtered by** line, start typing to select a filter

      ![Select a filter](https://dt-cdn.net/images/filter-01-325-2fe63fb62a.png)
   2. Select or type a value

      ![Select a value](https://dt-cdn.net/images/filter-02-404-32504bda2e.png)

   For more common filters, you can select a filter directly from the **Quick filters** column of the **Hosts** page.
3. Select **Pin to dashboard**.

   Dynatrace displays a preview of the tile and asks you to select the dashboard to which you want to pin it. The list of dashboards is searchable: select in the list and start typing to filter the list, and then select the dashboard from the filtered list.

   ![Filter tiles: pin](https://dt-cdn.net/images/filtered-tile-01-382-0dbefb8cc5.png)
4. Select a dashboard (in this example, `Filtered Dashboard`) and select **Pin**. This creates the tile and pins it to that dashboard.

   ![Filter tiles: open dashboard](https://dt-cdn.net/images/filtered-tile-02-380-4c83bb3eb7.png)
5. Select **Open dashboard**.  
   The formerly empty dashboard now opens in edit mode with the new tile selected for editing. You can make optional settings to this tile before saving it. For a **Host health** tile, you have the following options:

   * Optional Select whether to show a visualization on the tile
   * Optional Select a custom timeframe
   * Optional Select a custom management zone
   * Optional Select an environment

   ![Filter tiles: tile edit mode](https://dt-cdn.net/images/filtered-tile-03-1187-acc59a36d4.png)
6. Select **Done**.  
   The dashboard is displayed with the new tile representing hosts in GdaÅsk, Poland.

   ![Filter tiles: display mode](https://dt-cdn.net/images/filtered-tile-05-1186-285827111d.png)

Now we have a tile that's specific to the hosts in the GdaÅsk, Poland, data center.

* The filter is fully dynamic. If hosts are added or removed, or if their statuses change, the tile updates automatically.
* To view the filtered **Hosts** page from which we created the tile, open the menu in the tile's upper-right corner and select **View details**.

## Add a header to your tile

Optional

To add a meaningful label to your tile

1. Select **Edit** to edit your dashboard.
2. Drag a **Header** tile from the **Edit dashboard** pane to your dashboard.  
   This will be the title of your tile.
3. Edit the header text. In this example, we use **Gdansk hosts**.
4. Drag your **Header** tile into position above your **Hosts** tile.  
   Depending on the position of your **Hosts** tile on the dashboard, you may need to drag both tiles to new positions so you can fit the **Header** tile over the **Hosts** tile.

   ![Header tile - edit dashboard](https://dt-cdn.net/images/filtered-tile-08-399-4d36db7eb2.png)
5. Select **Done**.

   ![Header tile](https://dt-cdn.net/images/filtered-tile-07-401-f9f22ea2e9.png)

## Update a filtered tile

To change the filters on your tile

1. On your dashboard, select the tile to display the **Hosts** table with your filter applied.
2. Add or delete filters.

   In this example, we keep `Data center: GdaÅsk, Poland` and add `Operating system: Linux`. Because we have changed the filters, the **Update dashboard tile** button is enabled so you can save changes.

   ![Filter tiles: additional filter](https://dt-cdn.net/images/filtered-tile-06-1431-274639b9a2.png)
3. Select **Update dashboard tile**.  
   The new filter settings are saved to the tile. In this example, the tile on your dashboard displays the health of hosts matching `Data center: GdaÅsk, Poland` and `Operating system: Linux`, and it opens the **Hosts** page with those filters.
4. To return to the dashboard, select the dashboard button in the upper-left corner of Dynatrace.

   ![Dashboard button](https://dt-cdn.net/images/dashboardbutton-28-e3cbad6cfe.png)

## Pin as new tile

Instead of updating a tile, you might want to save a new copy of the tile. For example, you might want multiple similar tiles but with each tile filtered for a different operating system.

1. On the same example dashboard, open the tile menu (in the upper-right of the tile) and select **View details**.  
   The **Hosts** page opens with the same filters set.
2. Select **More** (**â¦**) > **Pin as new tile**.

   * Select a different dashboard to have copies of the same tile on two different dashboards.
   * Select the same dashboard to have two copies of the tile on the same dashboard, which might seem pointless. However:

     + You can edit each copy of the tile to have a different management zone, timerange, and environment
     + You can set different filters on each copy of the tile

## Clone tiles

Tile cloning can save you a lot of work. For example, suppose you want your dashboard to display three visualizations that are identical except that they each query a different host. The easiest solution is to create the first visualization, experiment with the visualization settings until it's perfect, and then clone it twice. After that, you just need to edit the clones to query the other two hosts.

### Clone a tile to the current dashboard

To pin the cloned tiles to the same dashboard

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile that you want to clone (add a copy of the tile to the current dashboard) and then select **Clone**.

   * To clone multiple tiles to the current dashboard, drag a selection rectangle around the *x* tiles you want to clone and then select **Clone x tiles**.
5. Edit the cloned tiles as needed.

### Clone a tile to another dashboard

To pin the cloned tiles to another existing dashboard, or to create another dashboard and pin the clones to it

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile you want to clone to another dashboard and then select **Clone to**.

   * To clone multiple tiles to another dashboard, drag a selection rectangle around the *x* tiles you want to clone and then select **Clone x to**.
5. In the **Where do you want to pin to?** pop-up window, select an existing dashboard or **Create new dashboard**.
6. Select **Pin** to add the selected tiles to the dashboard.
7. Edit the cloned tiles as needed.