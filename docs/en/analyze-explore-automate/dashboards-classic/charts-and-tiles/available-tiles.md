---
title: Available tiles
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/available-tiles
scraped: 2026-02-21T21:25:05.525634
---

# Available tiles

# Available tiles

* Reference
* 33-min read
* Updated on May 16, 2022

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

Tiles you can add to your dashboards are described below.

Editing tips

* To make multiple similar **tiles**, start with one good tile, clone it, and then edit the cloned tiles.

  Clone a tile to the current dashboard

  1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
  2. Select the name of a dashboard to display that dashboard.
  3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

     + If you don't see an **Edit** option, you don't have permission to edit that dashboard.
  4. Select the tile that you want to clone (add a copy of the tile to the current dashboard) and then select **Clone**.

     + To clone multiple tiles to the current dashboard, drag a selection rectangle around the *x* tiles you want to clone and then select **Clone x tiles**.
  5. Edit the cloned tiles as needed.

  Clone a tile to another dashboard

  1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
  2. Select the name of a dashboard to display that dashboard.
  3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

     + If you don't see an **Edit** option, you don't have permission to edit that dashboard.
  4. Select the tile you want to clone to another dashboard and then select **Clone to**.

     + To clone multiple tiles to another dashboard, drag a selection rectangle around the *x* tiles you want to clone and then select **Clone x to**.
  5. In the **Where do you want to pin to?** pop-up window, select an existing dashboard or **Create new dashboard**.
  6. Select **Pin** to add the selected tiles to the dashboard.
  7. Edit the cloned tiles as needed.
* To make multiple similar **dashboards**, each with the same tiles, start with one good dashboard, clone it, and then edit the cloned dashboards/tiles.

  Clone an existing dashboard

  1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
  2. In the table of dashboards, select **More** (**â¦**) > **Clone** for the dashboard you want to copy.

     + The copy opens in edit mode.
     + The original dashboard is unaffected.

## Visualizations

Use visualization tiles to create visual representations of [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") queries that you can pin to your dashboards.

### Visualization types

Dynatrace offers the following visualization types:

* [Graph](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-graph "Configure and use a graph visualization in Data Explorer and pin it to your dashboards as a graph tile.")
* [Stacked column](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-stacked-column "Configure and use a stacked column visualization in Data Explorer and display it on your dashboards.")
* [Stacked area](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-stacked-area "Configure and use a stacked area visualization in Data Explorer and display it on your dashboards.")
* [Pie](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-pie "Configure and use a pie/doughnut visualization in Data Explorer and display it on your dashboards.")
* [Single value](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-single-value "Configure and use a single-value visualization in Data Explorer and display it on your dashboards.")
* [Table](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-table "Configure and use a table visualization in Data Explorer and display it on your dashboards.")
* [Top list](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-top-list "Configure a top-list visualization in Data Explorer and display it on your dashboards.")
* [Heatmap](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-heatmap "Configure and use a heatmap visualization in Data Explorer and pin it to your dashboards as a heatmap tile.")
* [Honeycomb](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-honeycomb "Configure and use a honeycomb visualization in Data Explorer and display it on your dashboards.")

#### Interactivity

Interactivity of visualization tiles varies according to the type of visualization, but they generally share common capabilities.

* Hover over an element (such as a line or a slice of pie) to see details in a tooltip.
* Select (click) an element and then select a button in the tooltip to drill down for details. For example, in a visualization showing a line for each host, select an interesting point on a line and then select the **View host** button to drill down to the selected host page.
* The legend is active: select a legend entry to show or hide the corresponding element on the visualization.
* All tiles have a tile menu in the upper-right corner:

  + **Configure tile in Data Explorer** opens the tile in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), where you can configure the query and visualization.
  + **Edit tile** (if you have edit rights) opens the dashboard in edit mode with the current tile selected.

#### Configuration

To configure a visualization tile from the dashboard editor

1. Display your dashboard and select **Edit**.
2. Drag a visualization tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard.
3. Select **Configure tile** to open your tile in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").
4. Configure the query for the tile. You don't have to create the final version all at once; you can build your query iteratively.

   * Select **Run query** after you make a query change to see the results of the change.
   * Optional Select a different visualization type and see what works best for your query.
   * The selection of visual settings available depends on the query and visualization type.
5. After you have defined the query:

   * To save your changes to the tile and dashboard you started from, select **Save changes to dashboard**.
   * To save your changes to a different tile, even a different dashboard, select **Pin to dashboard** and choose the destination dashboard and tile title.
6. Select **Open dashboard**.
7. Optional Change the tile title.
8. Optional Select a custom timeframe.
9. Optional Select a custom management zone.
10. Optional Select an environment.

To configure a visualization tile from the 'Data Explorer'

1. Go to **Data Explorer**.
2. Configure the query for the tile. You don't have to create the final version all at once; you can build your query iteratively.

   * Select **Run query** after you make a query change to see the results of the change.
   * Select different visualization types to see what works best for your query.
   * The selection of visual settings available depends on the query and visualization type. For details:

     + [Graph](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-graph "Configure and use a graph visualization in Data Explorer and pin it to your dashboards as a graph tile.")
     + [Stacked column](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-stacked-column "Configure and use a stacked column visualization in Data Explorer and display it on your dashboards.")
     + [Stacked area](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-stacked-area "Configure and use a stacked area visualization in Data Explorer and display it on your dashboards.")
     + [Pie](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-pie "Configure and use a pie/doughnut visualization in Data Explorer and display it on your dashboards.")
     + [Single value](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-single-value "Configure and use a single-value visualization in Data Explorer and display it on your dashboards.")
     + [Table](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-table "Configure and use a table visualization in Data Explorer and display it on your dashboards.")
     + [Top list](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-top-list "Configure a top-list visualization in Data Explorer and display it on your dashboards.")
     + [Heatmap](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-heatmap "Configure and use a heatmap visualization in Data Explorer and pin it to your dashboards as a heatmap tile.")
     + [Honeycomb](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-honeycomb "Configure and use a honeycomb visualization in Data Explorer and display it on your dashboards.")
   * Some visualizations (for example, heatmaps) can display only one metric. To display a different metric in the visualization, select the letter next to the metric you want to visualize. In this example, we would change the selection from **A** (`CPU usage %`) to **B** (`Memory used %`).

     ![Change metric selection](https://dt-cdn.net/images/select-metric-379-6a5af28695.png)

     Other visualizations (for example, tables) can display more than one metric. To change the selection of metrics to visualize, select the letters next to the metric names. In the above example, we would change the selection from **A** (`CPU usage %` only) to both **A** and **B** (`CPU usage %` and `Memory used %`).
3. When you are satisfied with the results of your query, select **Pin to dashboard** and choose the destination dashboard and tile title.
4. Select **Open dashboard** to see the tile on the dashboard.
5. Optional Change the tile title.
6. Optional Select a custom timeframe.
7. Optional Select a custom management zone.
8. Optional Select an environment.

## Context

Use the context tiles (**Header**, **Markdown**, and **Image**) to explain your dashboard contents and add graphics such as company logos. This is particularly important if you're making dashboards to share with others.

### Header

Use a header tile to put a bold label over another tile.

### Markdown

Use one or more markdown tiles to customize and describe your dashboard: what it does, how to use it, and so on.

Limitations: 1,000 characters per markdown tile.

Markdown syntax

#### Headings

Markdown heading levels `#` - `######` are supported.

#### Horizontal lines

Use `***` or `___` or `---` alone on one line to add a horizontal line separating sections of your tile.

#### Line breaks

Leave two spaces at the end of a line to force a line break.

#### Emphasis

Use `**text**` or `__text__` to display bold **text**.

#### Lists

You can create numbered (`1.`) or bulleted (`*`) markdown lists, or a mix of the two, with nesting.

#### Links

If you have favorite Dynatrace pages and websites, you can add links to all of them from your dashboards.

A link consists of two parts:

* The link label in square brackets: `[` and `]`. This is free-form text between two square brackets, such as `[Dynatrace]`.
* The link target in parentheses: `(` and `)`. There are two ways to define a target:

  + An absolute URL. For example, to link to:

    ```
    https://www.example.com/
    ```

    put the whole URL in parentheses

    ```
    (https://www.example.com/)
    ```

    to get a link definition like:

    ```
    [Example](https://www.example.com/)
    ```
  + An anchor to a Dynatrace page (including other dashboards).  
    To get that anchor, navigate to the target page in Dynatrace and copy everything on the browser address line that follows the domain and slash.  
    If the full URL of the target page is:

    ```
    https://myenvironment.live.dynatrace.com/ui/deploymentstatus/oneagents?gtf=-2h&gf=all
    ```

    the anchor text is:

    ```
    ui/deploymentstatus/oneagents?gtf=-2h&gf=all
    ```

    and the full link specification is something like:

    ```
    [My link to deployment status](ui/deploymentstatus/oneagents?gtf=-2h&gf=all)
    ```

    Similarly, if you added this example to a markdown tile on one of your dashboards, the link would open the Dynatrace Hosts table:

    ```
    [Hosts](#newhosts;gtf=-2h;gf=all)
    ```

### Image

Add images to your dashboards to improve their appearance and customize them for presentations.

Supported image file types: JPG/JPEG, GIF, PNG, WEBP, TIFF, BMP, SVG

You can upload an image or point to it via URL.

Unlike other tile types, an image tile is not automatically refreshed. You need to refresh a dashboard manually to update the image tiles on that dashboard.

Upload an image

To upload an image and display it on your dashboard

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Drag an **Image** tile into position.
5. On the **Image** panel, select the **Upload an image** tab.
6. Select **Upload image**.
7. Browse for and select the image file you want to display in the tile.
8. Size and position the tile as needed.

Point to image via URL

To point to an image via URL and display it on your dashboard, you first need to add the URL to the allowlist, and then you can refer to that URL from an image tile.

**Add the URL to the allowlist**

1. Go to **Settings** and select **Dashboards** > **Allowed URL pattern rules**.
2. Select **Add item**.
3. Set **Rule**, which specifies how to process this allowlist entry.

   * **Starts with**âallow any image whose URL starts with the contents of **Pattern**.
   * **Exact**âallow the specific image whose URL matches the contents of **Pattern** exactly.
4. Set **Pattern**:

   * To specify a URL start, enter enough of the URL to make sure any matching image URLs will be suitable for your dashboards.  
     Example: enter `https://example.com/images/` to allow any image whose URL starts with `https://example.com/images/`, such as  
     `https://example.com/images/image-x.jpg` and
     `https://example.com/images/my-picture.svg`
   * To specify an exact URL, enter the entire URL of the image you want to allow.  
     Example: enter `https://example.com/images/my-image-file-name.jpg` to allow only that image
5. Select **Save changes** to add the specified rule to the allowlist.

**Add the image tile**

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Drag an **Image** tile into position.
5. On the **Image** panel, select the **Add image URL** tab.
6. Enter the URL of the image file you want to display in the tile. It needs to match one of the rules on the allowlist.
7. Size and position the tile as needed.

Example dashboard with images:

![Example dashboard with images](https://dt-cdn.net/images/dashboard-image-example-01-1286-031295613c.png)

## Infrastructure

### Host health

Displays the number of hosts (operating system instances, whether physical and virtual) in your environment compared to the number of hosts in your environment that are currently affected by problems. Each host instance equates to a Dynatrace OneAgent installed in your environment.

#### Drilldowns

Health tile drilldowns

* From a health tile (such as **Host health**, **Service health**, and **Application health**), where you see green and red elements (such as hosts, services, or applications), hover over any problematic (red) element to see the identity of the element.
* To drill down to a problematic (red) element, select the red hexagon and then select the **Viewâ¦** button. On this example **Synthetic monitor health** tile, we have selected a red element, which enabled the **View test** drilldown button for that element.

  ![Drill down to problematic entity from health tile](https://dt-cdn.net/images/tile-health-bad-drilldown-276-6265617519.png)
* You can't drill down from a healthy (green) element. From any tile, however, you can select the menu in the upper-right corner of the tile and then select **View details** to display the relevant Dynatrace page for the tile. For example, **View details** from a **Synthetic monitor health** tile displays the **Synthetic monitors** table.

  ![Select tile menu](https://dt-cdn.net/images/tile-health-menu-open-272-17a936feef.png)

  ![Select 'View details' from tile menu](https://dt-cdn.net/images/tile-health-menu-view-details-270-aaf4eae8ec.png)

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Host health** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select whether to show a visualization on the tile
3. Optional Select a custom timeframe
4. Optional Select a custom management zone
5. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Set filters in the **Filtered by** box.
3. Select **Pin to dashboard**, select a target dashboard, and select **Pin** to add a **Hosts** tile to the selected dashboard with the selected filters. You can then set any of the options described above.

   * The tile will reflect all filters and options you have set
   * The next time you select the tile on your dashboard, the **Hosts** page will open with the filters and options already applied

### Network metrics

Displays network health metrics for traffic flowing through your monitored hosts. Shows current traffic volume and quality of communication of both new (Connectivity) and established sessions (Retransmissions).

#### Drilldowns

* From the tile menu, select **View details** to open the **Host networking** page

#### Configuration

To configure this tile type from the dashboard editor

1. Optional Select a custom timeframe
2. Optional Select a custom management zone
3. Optional Select an environment

### Network status

Displays current network traffic flowing through your monitored hosts. Shows traffic volume, number of nodes (Talkers) exchanging network traffic, and number of nodes experiencing performance problems (Processes and Hosts).

#### Drilldowns

* From the tile menu, select **View details** to open the **Host networking** page

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Network status** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select whether to show a visualization on the tile
3. Optional Select a custom timeframe
4. Optional Select a custom management zone
5. Optional Select an environment

### Docker

Displays current number of Docker containers and images compared to last week, plus current number of Docker hosts.

#### Drilldowns

* From the tile menu, select **View details** to open the **Docker** page

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Docker** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select a custom timeframe
3. Optional Select a custom management zone
4. Optional Select an environment

### VMware

Displays current basic indicators related to the virtualized infrastructure in your environment, including the number of VMs, migration events, and the corresponding trends, as well as the number of ESXi hosts (standalone or managed by attached vCenter servers) against the number of ESXi hosts in your environment that are currently affected by problems. If there are multiple vCenter or ESXi hosts attached, all gathered data can be aggregated or presented for a selected entity.

#### Drilldowns

* From the tile menu, select **View details** to open the **VMware** page

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **VMware** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select a custom timeframe
3. Optional Select an environment

### AWS

Displays quick insights and health indicators of three services running under your AWS account:

* Elastic Compute Cloud (EC2) instances
* Elastic Block Storage (EBS)
* Classic Load Balancer (ELB)

#### Drilldowns

* From the tile menu, select **View details** to open the **AWS** page

#### Configuration

To configure this tile type from the dashboard editor

1. Drag an **AWS** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an AWS account
3. Optional Select a custom timeframe
4. Optional Select an environment

## Services

### Service health

Displays an overview of all services monitored by Dynatrace, including the number of services experiencing performance degradation. This high-level visualization provides an easily digestible view, which makes it a great fit for management dashboards.

Depending on the selected timeframe, the tile shows:

* For a *last X* timeframe: the most recent time slot of data.
* For other timeframe types: the average value within the timeframe.

#### Drilldowns

Health tile drilldowns

* From a health tile (such as **Host health**, **Service health**, and **Application health**), where you see green and red elements (such as hosts, services, or applications), hover over any problematic (red) element to see the identity of the element.
* To drill down to a problematic (red) element, select the red hexagon and then select the **Viewâ¦** button. On this example **Synthetic monitor health** tile, we have selected a red element, which enabled the **View test** drilldown button for that element.

  ![Drill down to problematic entity from health tile](https://dt-cdn.net/images/tile-health-bad-drilldown-276-6265617519.png)
* You can't drill down from a healthy (green) element. From any tile, however, you can select the menu in the upper-right corner of the tile and then select **View details** to display the relevant Dynatrace page for the tile. For example, **View details** from a **Synthetic monitor health** tile displays the **Synthetic monitors** table.

  ![Select tile menu](https://dt-cdn.net/images/tile-health-menu-open-272-17a936feef.png)

  ![Select 'View details' from tile menu](https://dt-cdn.net/images/tile-health-menu-view-details-270-aaf4eae8ec.png)

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Service health** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select whether to show a visualization on the tile
3. Optional Select a custom timeframe
4. Optional Select a custom management zone
5. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Set filters in the **Filtered by** box.
3. Select **Pin to dashboard** to add a **Services** tile to the selected dashboard with the selected filters. You can then set any of the options described above.

   * The tile will reflect all filters and options you have set
   * The next time you select the tile on your dashboard, the **Services** page will open with the filters and options already applied

### Service or request

Displays current key performance indicators related to the selected service or request (requests per minute, failure rate, and response time) in a resizable tile format.

#### Drilldowns

* From the tile menu, select **View details** to open the selected service or request details page

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Service or request** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select a service type
3. Select a service
4. Select a key request
5. Optional Select a custom timeframe
6. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Select a service.
3. From the service page, select **More** (**â¦**) > **Pin to dashboard**. You can then set any of the options described above.

   * The tile will reflect the options you have set
   * The next time you select the tile on your dashboard, the service page will open with the options already applied

## Applications

### Top web applications

Displays load details related to up to three web applications in your environment that have the highest user-action rate.

* Current values are compared against baseline measurements (when available)
* Performance threshold violations are color coded in red
* Optional Select a custom management zone

#### Drilldowns

* From the tile menu, select **View details** to open the **Applications** page filtered by web applications (and any other filters you set on the tile if you pinned it from the **Applications** page)

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Top web applications** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select a custom management zone

To pin this tile to your dashboard with filters set

1. Go to **Web**.
2. Set other filters as needed.
3. Select **Pin to dashboard**, select a target dashboard, and select **Pin**.

### Application health

Displays the total number of applications in your environment versus the number of applications that are currently affected by problems. Opens your Applications page.

#### Drilldowns

Health tile drilldowns

* From a health tile (such as **Host health**, **Service health**, and **Application health**), where you see green and red elements (such as hosts, services, or applications), hover over any problematic (red) element to see the identity of the element.
* To drill down to a problematic (red) element, select the red hexagon and then select the **Viewâ¦** button. On this example **Synthetic monitor health** tile, we have selected a red element, which enabled the **View test** drilldown button for that element.

  ![Drill down to problematic entity from health tile](https://dt-cdn.net/images/tile-health-bad-drilldown-276-6265617519.png)
* You can't drill down from a healthy (green) element. From any tile, however, you can select the menu in the upper-right corner of the tile and then select **View details** to display the relevant Dynatrace page for the tile. For example, **View details** from a **Synthetic monitor health** tile displays the **Synthetic monitors** table.

  ![Select tile menu](https://dt-cdn.net/images/tile-health-menu-open-272-17a936feef.png)

  ![Select 'View details' from tile menu](https://dt-cdn.net/images/tile-health-menu-view-details-270-aaf4eae8ec.png)

#### Configuration

To configure this tile type from the dashboard editor

1. Drag an **Application health** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select whether to show a visualization on the tile
3. Optional Select a custom timeframe
4. Optional Select a custom management zone
5. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Custom Applications**, **Frontend**, **Mobile**, or **Web**.
2. Set filters in the **Filtered by** box.
3. Select **Pin to dashboard** to add an **Application health** tile to the selected dashboard with the selected filters. You can then set any of the options described above.

   * The tile will reflect all filters and options you have set
   * The next time you select the tile on your dashboard, the **Applications** page will open with the filters and options already applied

### User behavior

Displays key user behavior indicators related to the selected application (active sessions per minute, actions per session, and session duration) over the timeframe.

#### Drilldowns

* From the tile menu, select **View details** to open the selected application's user behavior section

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **User behavior** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Custom Applications**, **Frontend**, **Mobile**, or **Web**, depending on the type of application you want to monitor.
2. Select the application you want to monitor with a tile.
3. Select the **User behavior** section of the infographic.
4. Select **Pin to dashboard**, select a target dashboard, and select **Pin**.  
   A **User behavior** tile for the selected application is pinned to the selected dashboard.

### User breakdown

Displays a user type breakdown (doughnut) by real users, robots, and monitors, and visualizes new users versus returning users over the timeframe.

#### Drilldowns

* From the tile menu, select **View details** to open the selected application's user behavior section

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **User breakdown** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application you want to monitor with a tile
3. Optional Select a custom timeframe
4. Optional Select an environment

### World map

Displays a geographic map of the selected metric for the selected application.

The timeframe of the world map tile is always **Last 2 hours**, regardless of the global or dashboard timeframe setting. If you need to see a different timeframe, drill down to the full world map and change the timeframe there.

#### Drilldowns

* To open the full-sized world map page for the selected metric and location, either select the tile or select **View details** from the tile menu

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **World map** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application (or `Most active application`) from the list
3. Select a geolocation
4. Select the metric you want to map. There are two categories. You can select only one item.

   **Performance metric based on user actions:**

   * [Apdex](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.")
   * [User actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")
   * [Load actions](/docs/observe/digital-experience/rum-concepts/user-actions#load-action "Learn what user actions are and how they help you understand what users do with your application.")
   * [XHR actions](/docs/observe/digital-experience/rum-concepts/user-actions#xhr-action "Learn what user actions are and how they help you understand what users do with your application.")
   * [Custom actions](/docs/observe/digital-experience/rum-concepts/user-actions#custom-action "Learn what user actions are and how they help you understand what users do with your application.")
   * Errors

   **Behavior metric based on sessions or users:**

   * Active sessions
   * Active users
   * Actions per session
   * Bounce rate
   * Session duration

To pin this tile to your dashboard with filters set

1. Go to **Custom Applications**, **Frontend**, **Mobile**, or **Web**, depending on the type of application you want to monitor.
2. Select an application.
3. On the infographic, select **View geolocation breakdown**.
4. In the **Geolocation breakdown** section that is now displayed under the infographic, select **View full world map**.
5. In the filter bar, set a `Location` filter to zoom that map to that location
6. Select a metric button (**Apdex**, **User actions**, **Load actions**, **XHR actions**, **Custom actions**, or **Errors**) to focus the map on that metric
7. Select **Pin to dashboard**, select the target dashboard, and select **Pin**.

**Troubleshooting:**

* If you don't see data on the world map, you might need to map your internal IP addresses to locations for your [web](/docs/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are."), [mobile](/docs/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are."), and [custom applications](/docs/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.").
* Remember that the timeframe of a world map tile is always **Last 2 hours**, regardless of how you set the global or dashboard timeframe.

### Key user action overview

Displays an overview of the selected application's key user actions and any corresponding open problems.

#### Drilldowns

* From the tile menu, select **View details** to open the user action analysis page for the selected application with a full list of key user actions.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Key user action overview** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

### Bounce rate

Displays a comparison of the current bounce rate with yesterday and the number of entry actions.

#### Drilldowns

* From the tile menu, select **View details** to open the selected application's bounce rate analysis.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Bounce rate** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

### Top conversion goals

Displays the overall conversion rate and your top 5 goals for the selected application. This tile also serves as a direct link to the selected application goals view.

#### Drilldowns

* From the tile menu, select **View details** to open the selected application's **Conversion** page.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Top conversion goals** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

### Conversion goal

Displays the overall conversion rate and completions for the selected goal. This tile also serves as a direct link to the selected application goals view.

#### Drilldowns

* From the tile menu, select **View details** to open the selected application's goals view.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Conversion goal** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Select a goal
4. Optional Select a custom timeframe
5. Optional Select an environment

### JavaScript errors

Displays JavaScript error indicators related to the selected application (JavaScript errors per minute, percent affected user actions).

#### Drilldowns

* From the tile menu, select **View details** to open **Compare JavaScript errors** for the selected application.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **JavaScript errors** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

### Resources

Displays load details for application-specific resources grouped by first-party, third-party, and CDN resources.

#### Drilldowns

* From the tile menu, select **View details** to open the application details page with **Resources** selected.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Resources** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Select a metric: `Count per minute` or `Load time`
4. Optional Select a custom timeframe
5. Optional Select an environment

### Most used 3rd parties

Displays load details related to the three third-party content providers that your application uses most frequently.

#### Drilldowns

* From the tile menu, select **View details** to open the application details page with **Resources** selected.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Most used 3rd parties** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Select a metric: `3rd party`, `CDN`, or `1st party`
4. Optional Select a custom timeframe
5. Optional Select an environment

### Mobile app

Displays key performance indicators related to the selected mobile app (users, crash-free user rate, and number of crashes).

#### Drilldowns

* From the tile menu, select **View details** to open the selected mobile app page.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Mobile map** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select a mobile app from the list.
3. Optional Select a custom timeframe.
4. Optional Select an environment.

To pin this tile to your dashboard with filters set

1. Go to **Mobile**.
2. Select the mobile application for which you want to create a dashboard tile.
3. On the application page, select **Pin to dashboard**, select the target dashboard, and select **Pin**.

### Custom application

Displays key performance indicators related to the selected custom application (users, crash free user rate, and number of crashes).

#### Drilldowns

* From the tile menu, select **View details** to open the selected custom application page.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Custom application** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select a custom application from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Custom Applications**.
2. Select the custom application you want to monitor with a dashboard tile.
3. On the application page, select **Pin to dashboard**, select the target dashboard, and select **Pin**.

### Live user activity

Displays the number of current live users overall as well as your applications with most live users.

#### Drilldowns

* From the tile menu, select **View details** to open **User sessions** filtered for `Live: Yes` and `User type: Real users`.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Live user activity** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select a custom timeframe
3. Optional Select a custom management zone
4. Optional Select an environment

### Web application

Displays key performance indicators related to the selected application: [Apdex rating](/docs/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance."), [user actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") per minute, and number of JavaScript errors per minute.

#### Drilldowns

* From the tile menu, select **View details** to open the selected application page.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Web application** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Web**.
2. Select the web application you want to monitor with this tile.
3. Display the **Performance analysis** section of the infographic.
4. Select **Pin to dashboard**.  
   A **Web application** tile for the selected application is pinned to the selected web dashboard.

### Key user action

Displays key performance indicators related to the selected application and key [user action](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application."): user action duration, user actions/min, and number of errors/min.

#### Drilldowns

* From the tile menu, select **View details** to open the selected key user action page for the selected application and key user action.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Key user action** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an application from the list
3. Select a key user action from the list
4. Optional Select a custom timeframe
5. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Custom Applications**, **Frontend**, **Mobile**, or **Web**, depending on the type of application you want to monitor.
2. Select the application you want to monitor with this tile.
3. In the **Top 3 user actions** section, select **View full details**.
4. Select a key user action.

   * If the user action has already been selected as a key user action, select it in the **Key user actions** list.
   * If the user action has not been selected as a key user action, select a user action from the **Top 100 user actions** tab, and then select **More** (**â¦**) > **Mark as key user action**.

   The **Pin to dashboard** button is now displayed.
5. Select **Pin to dashboard**, select a target dashboard, and select **Pin**.

### User Sessions Query

Create advanced queries on completed user sessions with user sessions query language.

#### Drilldowns

* From the tile menu, select **View details** to open the user sessions query page for this query.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **User Sessions Query** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select **Configure tile** in the **User Sessions Query** configuration pane
3. On the **User sessions query** page, [create a query](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") and select **Run query**
4. When you have a query that you want to link to your tile, select **Save changes to dashboard**
5. Optional Select a custom timeframe
6. Optional Select a custom management zone
7. Optional Select an environment

## Service-level objectives

### Service-level objective

Displays the following:

* **Title**
* **Status**: numeric value displayed in green (good), yellow (warning), red (bad), or gray (no data).
* **Error budget**: numeric value displayed in green (good), yellow (warning), red (bad), or gray (no data).
* **Target**: numeric value
* Problems indicator is optional
* Legend (colors) and metric names are optional
* Colorized based on status is optional
* **Tiles filters\*Environment**
* Optional Set **Title**

For more information, see [Configure and monitor service-level objectives with Dynatrace](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#slodashboardtile "Create, configure, and monitor service-level objectives with Dynatrace.").

#### Drilldowns

* From the tile menu, select **View details** to open the **Service-level objectives** page filtered to the selected SLO.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Service-level objective** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Set **Select a SLO** to one of the listed service-level objectives.
3. Adjust its configuration as needed.

   * Optional Set **Max shown decimals** to a different value.
   * Optional Turn **Show metric names** on or off.
   * Optional Turn **Show legend** on or off.
   * Optional Turn **Show problems indicator** on or off.
   * Optional Turn **Colorize based on status** on or off.
   * Optional Select a custom timeframe.
   * Optional Select an environment.
4. Select **Done**.

To pin this tile to your dashboard with filters set

1. Go to ![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic**.
2. Find the SLO you want to pin to the dashboard.
3. In the **Actions** column, select the pin icon for that SLO.
4. Select the dashboard to which you want to pin the tile.
5. Select **Pin**.
6. Select **Open dashboard** to open the dashboard in edit mode with the new tile selected.
7. Adjust its configuration as needed.

   * Optional Turn **Show legend** on or off.
   * Optional Turn **Show metric names** on or off.
   * Optional Turn **Show problems indicator** on or off.
   * Optional Set **Max shown decimals** to a different value.
   * Optional Select a custom timeframe.
   * Optional Select an environment.
8. Select **Done**.

## Synthetic

### Browser monitor

Displays key performance indicators related to the selected browser monitor (availability, duration, and location status).

#### Drilldowns

* From the tile menu, select **View details** to open the selected browser monitor page.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Browser monitor** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select a browser monitor from the list
3. Optional Exclude maintenance windows from availability calculations
4. Optional Select a custom timeframe
5. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Synthetic Classic**.  
   To filter the list, set **Type of synthetic monitor** to **Browser**.
2. Select the browser monitor for which you want to create a dashboard tile.
3. On the browser monitor page, select **Pin to dashboard**, select the target dashboard, and select **Pin**.

### Synthetic monitor health

Displays the number of active synthetic monitors in your environment against the number of synthetic monitors in your environment that are currently affected by problems.

#### Drilldowns

Health tile drilldowns

* From a health tile (such as **Host health**, **Service health**, and **Application health**), where you see green and red elements (such as hosts, services, or applications), hover over any problematic (red) element to see the identity of the element.
* To drill down to a problematic (red) element, select the red hexagon and then select the **Viewâ¦** button. On this example **Synthetic monitor health** tile, we have selected a red element, which enabled the **View test** drilldown button for that element.

  ![Drill down to problematic entity from health tile](https://dt-cdn.net/images/tile-health-bad-drilldown-276-6265617519.png)
* You can't drill down from a healthy (green) element. From any tile, however, you can select the menu in the upper-right corner of the tile and then select **View details** to display the relevant Dynatrace page for the tile. For example, **View details** from a **Synthetic monitor health** tile displays the **Synthetic monitors** table.

  ![Select tile menu](https://dt-cdn.net/images/tile-health-menu-open-272-17a936feef.png)

  ![Select 'View details' from tile menu](https://dt-cdn.net/images/tile-health-menu-view-details-270-aaf4eae8ec.png)

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Synthetic monitor health** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Show a visualization on the tile
3. Optional Select a custom timeframe
4. Optional Select a custom management zone
5. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Synthetic Classic**.
2. Set filters in the **Filtered by** box.
3. Select **Pin to dashboard** to add a **Hosts** tile to the selected dashboard with the selected filters. You can then set any of the options described above (timeframe, management zone, environment).

   * The tile will reflect all filters and options you have set
   * The next time you select the tile on your dashboard, the **Synthetic** page will open with the filters and options already applied

### Third-party monitor

Displays key performance indicators related to the selected third-party monitor (availability, duration, and location status).

#### Drilldowns

* From the tile menu, select **View details** to open the selected third-party monitor page.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Third-party monitor** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select a third-party monitor from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Synthetic Classic**.
2. In the **Filtered by** box, set **Type of synthetic monitor** to **Third-party**.
3. Select the third-party monitor for which you want to create a dashboard tile.
4. On the third-party monitor page, select **Pin to dashboard**, select the target dashboard, and select **Pin**.

### HTTP monitor

Displays key performance indicators related to the selected HTTP monitor (availability and duration).

#### Drilldowns

* From the tile menu, select **View details** to open the selected HTTP monitor page.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag an **HTTP monitor** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select an HTTP monitor from the list
3. Optional Select a custom timeframe
4. Optional Select an environment

To pin this tile to your dashboard with filters set

1. Go to **Synthetic Classic**.
2. In the **Filtered by** box, set **Type of synthetic monitor** to **HTTP**.
3. Select the HTTP monitor for which you want to create a dashboard tile.
4. On the HTTP monitor page, select **Pin to dashboard**, select the target dashboard, and select **Pin**.

## Databases

### Database health

Displays the number of databases in your environment against the number of databases that are currently affected by problems.

#### Drilldowns

Health tile drilldowns

* From a health tile (such as **Host health**, **Service health**, and **Application health**), where you see green and red elements (such as hosts, services, or applications), hover over any problematic (red) element to see the identity of the element.
* To drill down to a problematic (red) element, select the red hexagon and then select the **Viewâ¦** button. On this example **Synthetic monitor health** tile, we have selected a red element, which enabled the **View test** drilldown button for that element.

  ![Drill down to problematic entity from health tile](https://dt-cdn.net/images/tile-health-bad-drilldown-276-6265617519.png)
* You can't drill down from a healthy (green) element. From any tile, however, you can select the menu in the upper-right corner of the tile and then select **View details** to display the relevant Dynatrace page for the tile. For example, **View details** from a **Synthetic monitor health** tile displays the **Synthetic monitors** table.

  ![Select tile menu](https://dt-cdn.net/images/tile-health-menu-open-272-17a936feef.png)

  ![Select 'View details' from tile menu](https://dt-cdn.net/images/tile-health-menu-view-details-270-aaf4eae8ec.png)

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Database health** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Show a visualization on the tile
3. Optional Select a custom timeframe
4. Optional Select a custom management zone
5. Optional Select an environment

### Database performance

Displays key performance indicators related to the selected database service (commits per hour, statements per minute, and response time).

#### Drilldowns

* From the tile menu, select **View details** to open the selected Database service page.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Database performance** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Select a database service from the list.
3. Optional Select a custom timeframe
4. Optional Select an environment

## Integrations

### Data center service health

Displays the total number of data center services in your environment against the number of data center services that are currently affected by problems.

#### Drilldowns

Health tile drilldowns

* From a health tile (such as **Host health**, **Service health**, and **Application health**), where you see green and red elements (such as hosts, services, or applications), hover over any problematic (red) element to see the identity of the element.
* To drill down to a problematic (red) element, select the red hexagon and then select the **Viewâ¦** button. On this example **Synthetic monitor health** tile, we have selected a red element, which enabled the **View test** drilldown button for that element.

  ![Drill down to problematic entity from health tile](https://dt-cdn.net/images/tile-health-bad-drilldown-276-6265617519.png)
* You can't drill down from a healthy (green) element. From any tile, however, you can select the menu in the upper-right corner of the tile and then select **View details** to display the relevant Dynatrace page for the tile. For example, **View details** from a **Synthetic monitor health** tile displays the **Synthetic monitors** table.

  ![Select tile menu](https://dt-cdn.net/images/tile-health-menu-open-272-17a936feef.png)

  ![Select 'View details' from tile menu](https://dt-cdn.net/images/tile-health-menu-view-details-270-aaf4eae8ec.png)

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Data center service health** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select a custom timeframe
3. Optional Select a custom management zone
4. Optional Select an environment

## Analysis

### Problems

Displays the number of problems that are currently watched and active against the number of resolved problems in your environment. When a problem is active, the problem count is displayed in red.

#### Drilldowns

* From the tile menu, select **View details** to open your [Problems](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") feed.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Problems** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select a custom timeframe
3. Optional Select a custom management zone
4. Optional Select an environment

### Smartscape

Synthetically visualizes your environment components based on [Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") analysis. The tile display constantly cycles through the five Smartscape layers: applications, services, OS processes, hosts, and datacenters. For each layer, the tile shows the total number in your environment and, in red, the number currently affected by problems.

#### Drilldowns

* From the tile menu, select **View details** to open your [Smartscape](/docs/analyze-explore-automate/smartscape-classic#services "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") topology view to the Services layer.

#### Configuration

To configure this tile type from the dashboard editor

1. Drag a **Smartscape** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard
2. Optional Select a custom timeframe
3. Optional Select a custom management zone
4. Optional Select an environment

### Log query table

Displays log events matching the specific log data query. Only columns configured in the log viewer for that query are displayed in the table tile.

#### Configuration

To pin this tile type to your dashboard with filters set

1. Go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. In **Log Viewer**, enter the log query that you want the tile to reflect.
3. Optional Select **Table options** to specify which table columns to display.
4. Select **Pin to dashboard**, select the target dashboard, and then select **Pin**.
5. Select **Open dashboard** to see the new tile on the dashboard.

   * The tile displays the results of the query you specified in **Log Viewer**.
   * Only the columns you specified with **Table options** are displayed.

To configure this tile type from the dashboard editor

1. Drag a **Log query table** tile from the **Edit dashboard** pane, **Tiles** tab, to your dashboard.
2. Select **Configure tile** to display **Log Viewer**.
3. Enter a log query.
4. Optional Select **Table options** to specify which table columns to display.
5. Select **Save changes to dashboard** to return to editing the **Log query table** tile on the dashboard.
6. Optional Select a custom timeframe.
7. Optional Select a custom management zone.
8. Optional Select an environment.