# Dynatrace Documentation: analyze-explore-automate/dashboards-classic

Generated: 2026-02-17

Files combined: 9

---


## Source: available-tiles.md


---
title: Available tiles
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/available-tiles
scraped: 2026-02-17T21:27:21.422138
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


---


## Source: pin-tiles-to-your-dashboard.md


---
title: Pin tiles to your dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard
scraped: 2026-02-17T21:25:42.907432
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


---


## Source: dashboard-json.md


---
title: Edit Dynatrace dashboard JSON
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json
scraped: 2026-02-17T21:28:06.840072
---

# Edit Dynatrace dashboard JSON

# Edit Dynatrace dashboard JSON

* How-to guide
* 3-min read
* Published Sep 24, 2020

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

You can edit the JSON definition of your dashboard offline or, for small changes, edit the JSON directly in Dynatrace.

API alternative

To manage dashboard JSON at scale, you need the [Dashboards API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.").

## Edit offline

Use this procedure to download a dashboard's JSON definition, edit it offline, and upload it back to Dynatrace.

When you upload a dashboard using this procedure, you overwrite the dashboard whose definition you originally downloaded. If you want to upload a dashboard definition to a new dashboard, see [Import dashboard](#import-dashboard) below.

1. Display the dashboard.
2. Select **Edit**.
3. Switch to the **Settings** tab and then select **Configure more**.
4. Select **Dashboard JSON**.
5. On the **Dashboard JSON** page, select **Download**.  
   A JSON file with the dashboard's name is downloaded to your local machine.
6. Edit the JSON in your preferred development environment.  
   For JSON syntax details, see the [Dashboards API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.") Documentation.
7. On the **Dashboard JSON** page, select **Upload**, browse for the edited JSON file, and upload it to Dynatrace.  
   The uploaded JSON is displayed on the **Dashboard JSON** page.
8. Select **Save changes** to replace the old JSON with your edited JSON.
9. Display the dashboard to verify your changes.

## Edit in Dynatrace

1. Display the dashboard.
2. Select **Edit**.
3. Switch to the **Settings** tab and then select **Configure more**.
4. Select **Dashboard JSON**.
5. On the **Dashboard JSON** page, the dashboard JSON is displayed in an edit window.
6. Click in the displayed JSON and start editing.

   * You can work directly in the edit window or copy and paste back and forth from another editor.
   * The **You have unsaved changes** message in the lower left of the page will remind you that you have work in progress. Be sure to save before you navigate away from the page.
   * Syntax is checked each time you save. You can work incrementally and use **Save changes** to verify that it still parses.
   * For JSON syntax details, see the [Dashboards API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.") Documentation.
7. When you are finished, display the dashboard to verify your changes.

## Import dashboard

Use this procedure to import a dashboard definition as a new dashboard.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Export the dashboard**](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json#step-1 "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Edit the dashboard JSON file**](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json#step-2 "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Import the dashboard**](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json#step-3 "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.")

When you import a dashboard using this procedure, you add a new dashboard to Dynatrace. If you want to overwrite an existing dashboard, see [Edit offline](#edit-offline) above.

### Step 1 Export the dashboard

If you want to start from an existing dashboard definition

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. In the table of dashboards, select **More** (**â¦**) > **Export** for the dashboard you want to export.  
   The dashboard definition is exported as a JSON file to your computer.

### Step 2 Edit the dashboard JSON file

Edit the dashboard JSON in your preferred development environment. For JSON syntax details, see the [Dashboards API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.") Documentation.

### Step 3 Import the dashboard

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select **Import dashboard**.
3. Select the JSON file for the dashboard you want to import.  
   The imported dashboard opens in edit mode.


---


## Source: dashboard-timeframe.md


---
title: Dynatrace dashboard timeframe and management zone settings
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe
scraped: 2026-02-17T04:49:59.221556
---

# Dynatrace dashboard timeframe and management zone settings

# Dynatrace dashboard timeframe and management zone settings

* How-to guide
* 2-min read
* Published Jul 19, 2017

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

The global selectors for timeframe and management zone are available for use across all pages and views. You'll find them in the upper-right corner.

![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

* Select the filter button to select a new management zone
* Select the timeframe to select a new timeframe
  Timeframe selector controls

  The global timeframe selector serves as a time filter that, in most cases, enables you to select a specific analysis timeframe that persists across all product pages and views as you navigate through your analysis.

  ![Timeframe selector: presets](https://dt-cdn.net/images/timeframe-selector-basic-355-f0a835da1e.png)

  + The **Presets** tab lists all standard timeframes available. Select one to change your timeframe to that preset.
  + The **Custom** tab displays a calendar. Click a start day, click an end day, and then click **Apply** to select that range of days as your timeframe.

    - Selected calendar intervals are set to end on start of the next day (with the time set to `00:00`). For example, if you select September 3 to September 4 on the calendar, the timeframe starts on September 3 at time `00:00` and ends on September **5** at time `00:00`, so you never miss the last minute of the time range. You can edit these displayed times.
  + The **Recent** tab displays recently used timeframes. Select one to revert to that timeframe.
  + The **<** and **>** controls shift the timerange forward or backward in time. The increment is the length of the original timerange. For example, if the current timerange is `Last 2 hours` (the two-hour range ending now), click **<** to shift the timerange two hours back, to `-4h to -2h` (the two-hour range ending two hours ago).
  + Hover over the timeframe to see the start time, duration, and end time.

    ![Timeframe selector: hover](https://dt-cdn.net/images/timeframe-selector-hover-168-cfb13dc777.png)

  Timeframe selector expressions

  If you select the current timeframe in the menu bar, an editable timeframe expression is displayed.

  + Reading from left to right, a timeframe expression has a start time, a `to` operator, and an end time.
  + If there is no explicit end time, the `to` and `now` are implied. For example, `-2h` is the same `-2h to now`.
  + Supported units: `s`, `m`, `h`, `d`, `w`, `M`, `q`, `y` (you can also use whole words such as `minutes` and `quarter`)

  **Example timeframe expressions**

  **Meaning**

  `today`

  From the beginning of today to the beginning of tomorrow.

  `yesterday`

  From the beginning of yesterday to the beginning of today. Like `-1d/d to today`.

  `yesterday to now`

  From the beginning of yesterday to the current time today.

  `previous week`

  The previous seven whole days. If today is Monday, you get the previous Monday through the previous Sunday (yesterday).

  `this year`

  The current calendar year, from January 1 of this year at `00:00` through January 1 of next year at `00:00`.

  `last 6 weeks`

  The last 42 days (6 weeks \* 7 days) ending now. Equivalent to `-6w to now`.

  `-2h`

  From 2 hours (120 minutes) ago to the current time (`now` is implied). Equivalent to `Last 2 hours` and `-2h to now`.

  `-4d to -1h30m`

  From 4 days (96 hours) ago to 1.5 hours ago.

  `-1w`

  The last 7 days (168 hours), from this time 7 days ago to the current time (`now`). Equivalent to `-7d` and `-168h`.

  `-1w/w`

  From the beginning of the previous calendar week to the current time (now).

  + If you used `-1w/w` on a Friday afternoon at 3:00, you would get a range of 11 days 15 hours, starting with the beginning of the previous week's Monday, because `/w` rounds down to the beginning of the week.
  + If you used `-1w` without `/w` on a Friday afternoon at 3:00, the start time would be exactly 7 days (168 hours) earlier: the previous Friday at 3:00 in the afternoon.

  In general, `/` used in combination with a unit (such as `/d`, `/w`, `/M`, and `/y`) means to round down the date or time to the beginning of the specified time unit. For example, `-3d` means exactly 72 hours ago, whereas `-3d/d` means three days ago rounded down to the nearest day (starting at time `00:00`, the beginning of the day). Use `now/d` to mean the start of today.

  `-1w/w + 8h`

  Starting from the beginning of last week plus 8 hours (8:00 AM Monday).

  + Note that you can use the `+` and `-` operators with units, timestamps, and `now`.

  `-1d/d+9h00m to -1d/d+17h00m`

  Business hours yesterday, from 09:00 - 17:00 (9 AM to 5 PM).

  `2020-08-16 21:28 to 2020-08-19 10:02`

  An absolute range consisting of absolute start and end dates and times in `YYYY-MM-DD hh:mm` format.

  + If you provide a date but omit the time (for example, just `2020-08-16`), the time is assumed to be the beginning of day (`00:00`)
  + If you provide a time but omit the date (for example, just `21:28`), the date is assumed to be today

  `1598545932346 to 1598837052346`

  Unix epoch millisecond timestamps.

## Timeframe and management zone preservation

Timeframe and management zone selections are stickyâthey're propagated to all pages you visit. For example, after changing the timeframe and management zone on your dashboard, the selections are preserved as you drill down from the **Applications** tile to individual application pages.

The exception is opening a new dashboard or getting back to the current dashboard by selecting **Dashboard** in the upper-left corner of the page. In that case, the timeframe and management zone are reset to the dashboard's [defaults](#default).

The timeframe selector remembers up to 10 recently used timeframes.

## Default timeframe and management zone

You can set a default timeframe and management zone for each dashboard; these are selected every time you open the dashboard. They're also used when you [share](/docs/analyze-explore-automate/dashboards-classic/dashboards/share-dashboards "Learn how to share your Dynatrace dashboards with others.") the dashboard.

You can also specify a default timeframe and management zone for each tile.

### Dashboard-specific timeframe

To set a dashboard timeframe that overrides the global timeframe

1. Switch to the **Settings** tab.
2. Turn on **Default timeframe**.
3. Select the timeframe you want to be the default for this dashboard.

### Dashboard-specific management zone

To set a dashboard management zone that overrides the global management zone

1. Switch to the **Settings** tab.
2. Turn on **Default management zone**.
3. Select the management zone you want to be the default for this dashboard.

### Tile-specific timeframe

To set a tile timeframe that overrides the dashboard timeframe

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile you want to configure.
5. Turn on **Custom timeframe**.
6. Select the timeframe you want to be the default for this tile.
7. **Done**.  
   When you set a tile-specific timeframe, a filter is displayed in the upper-right of the tile. Hover over the filter to see the setting.

### Tile-specific management zone

To set a tile management zone that overrides the dashboard management zone

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile you want to configure.
5. Turn on **Custom management zone**.
6. Select the management zone you want to be the default for this tile.
7. **Done**.  
   When you set a tile-specific management zone, a filter is displayed in the upper-right of the tile. Hover over the filter to see the setting.


---


## Source: dashboards-multi-environment.md


---
title: Create remote/multi-environment Dynatrace dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment
scraped: 2026-02-17T04:52:26.111216
---

# Create remote/multi-environment Dynatrace dashboards

# Create remote/multi-environment Dynatrace dashboards

* How-to guide
* 8-min read
* Updated on Jun 04, 2024

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

A Dynatrace dashboard can include monitoring artifacts (such as metrics, logs, events, user sessions, and server-side traces) from multiple Dynatrace environments and can even support remote management zones (for tiles that support custom management zones).

## Overview

### Advantages

Dynatrace dashboards serve as a single pane of glass for monitoring artifacts such as metrics, logs, events, and user sessions. With multi-environment dashboards, your dashboards can combine these monitoring artifacts from separate Dynatrace environments.

After you configure the remote connection in your local Dynatrace environment, [you can quickly point dashboard tiles to the remote environment](#tile).

![Example: select remote environment for tile](https://dt-cdn.net/images/select-tile-environment-example-317-72348cc81f.png)

For tiles that allow a custom management zone (look for the **Custom management zone** setting in the configuration panel for the tile), you can specify another management zone.

Because the remote-environment capabilities of dashboard tiles allow you to build a common overview of problems and other data, dashboards can essentially serve as a hub for deeper analysis. A single click on any given dashboard tile displaying remote information takes you straight into a dedicated view of the remote environment where you can continue your analysis.

### Limitations

* A remote environment tile is backward compatible for up to five versions.

  + A remote environment tile running in a Dynatrace version *x* environment will work correctly with Dynatrace version *x*-5 or later deployed in the remote environment.

    When there's a difference of more than five versions between the local and remote versions, the tile may still work but that configuration is not supported.
  + A remote environment tile displays data based on the features included in the remote environment's cluster version.

    For example, if a remote environment tile depends on a feature that was added in Dynatrace version *x*, and that version is deployed locally, but the remote environment is still running Dynatrace version *x*-1, the feature won't be displayed in the local dashboard because the remote environment doesn't support it.

    If a remote environment tile depends on a feature that is not supported in the remote environment, the tile displays an error message explaining the discrepancy between the local and remote environments.
  + To maintain maximum compatibility between local and remote environments, keep your Dynatrace environments on the same version.
* Remote-environment connections donât pass user context and permissions over environment boundaries.

  For this reason, the best practice is to use management zones to segment/limit dashboard tiles when viewing remote information.

  Because of the above consideration, remote-environment dashboards can be configured only by environment administrators. Regular users can still view and interact with remote-environment dashboards without limitation.
* The world map dashboard tile isnât suited for (and therefore doesnât support) remote-environment scenarios.

## Configuration

To create a dashboard tile that queries data from a remote environment:

* In the remote Dynatrace environment, [create an access token](#token) that permits you to query data from that environment
* In the local Dynatrace environment, [add the remote environment](#link) to the table of remote environments
* In the local Dynatrace environment, [create one or more tiles that display remote data](#tile) queried from the remote environment

API equivalents

The procedures that follow use the Dynatrace web UI. To carry out the equivalent tasks via API, see:

* [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.")âto create a token in the remote environment
* [Remote environments API](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")âto create a link to the remote environment from the local environment
* [Dashboards Classic API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")âto configure a dashboard with tiles that query the remote environment

### Create an access token

With this procedure, you get an access token from the remote environment that you need in the other steps.

To create an access token for the remote Dynatrace environment

1. Sign in to the remote environment.

   * This is the environment from which you pull data.
   * If you can't sign in to the remote environment, someone with access to the remote environment can do this procedure for you.
2. Go to **Access Tokens**.
3. Select **Generate new token**.
4. Enter a token name.
5. Find the **Fetch data from a remote environment** scope (`RestRequestForwarding`) and select its checkbox.
6. Select **Generate token**.  
   This generates a token that gives your local environment permission to pull data from this remote environment.
7. Select **Copy** and then paste the token to a secure location.  
   It's a long string that you need to copy and paste back into Dynatrace later.

### Add the remote environment

To add the remote Dynatrace environment to your list of available remote environments

1. Sign in to your local Dynatrace environment.
2. Go to **Settings**.
3. Select **Integration** > **Remote environments**.
4. Select **Connect environment**.
5. Define the remote environment from which your local environment pulls data, and then select **Save changes**.

   * **Name** is the name under which this environment will be listed in your local Dynatrace environment when you configure a tile to query this remote environment. This is freeform text. It doesn't affect the remote environment.
   * **Remote environment URI**

     + For Dynatrace SaaS, it needs to be in the following format:

       `https://<ENVIRONMENTID>.live.dynatrace.com/`

       Replace `<ENVIRONMENTID>` with your actual environment ID.
     + For Dynatrace Managed, any URI is allowed.
     + To connect a Dynatrace (SaaS deployment) environment to a Dynatrace Managed deployment via a URI that is outside the `dynatrace-managed.com` domain, contact a Dynatrace product expert via live chat within your Dynatrace environment.
   * **Network scope**

     + `External`: The remote environment is located in another network. Globally configured proxy settings are used if present. This is the default scope.
     + `Internal`: The remote environment is located in the same network. Globally configured proxy settings are not used.
     + `Cluster`: The remote environment is located in the same cluster. The request is made to `localhost`.

     Dynatrace SaaS can only use the `External` network scope.
   * **Token** is the token you generated in the previous procedure. It needs to include the **Fetch data from a remote environment** scope (`RestRequestForwarding`).
   * **Test connection** checks the connection from your local environment to the remote environment.

     Be sure to get a `connection successfully established` message before continuing.

Now that you have established a link to the remote environment, you can create dashboard tiles that query that environment.

### Create a tile that displays remote data

To create a tile that pulls data from the remote environment

1. Display the dashboard that will display the tile.
2. Select **Edit**.
3. Select or add a tile on which you want to display data from the remote environment.  
   The **Environment** section of the tile settings pane displays the name of the environment from which that tile pulls monitoring data.

   * **Default (local)** configures the tile to pull its data from the local Dynatrace environment.
   * All other listed environments are remote environments for which a connection has been established.
4. Select the remote environment that you want the selected tile to query.  
   If you named the remote environment `Boston` when you added the remote environment in the previous procedure, `Boston` should be on this list.

   ![Example: select remote environment for tile](https://dt-cdn.net/images/select-tile-environment-example-317-72348cc81f.png)
5. Select **Done** to display the finished dashboard.
6. Hover over the tile filter icon to see the environment selection.

   ![Example: display tile filters to see remote environment selection](https://dt-cdn.net/images/tile-remote-environment-tooltip-example-495-96be8d3ec4.png)

## Examples

### Same tiles, different environments

In this example, we create a dashboard that shows the host health and network status for the local environment and a remote environment side by side. We assume that you have already added the remote environment to your local environment.

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**, select **Create dashboard**, give it a name, and select **Create**.
2. Drag two **Header** tiles to the dashboard (or drag one and then clone it).
3. Edit one header to say **Local** and the other to say **Remote**.
4. Drag two **Host health** tiles to the dashboard (or drag one and then clone it).  
   Position one under the **Local** header and the other under the **Remote** header.
5. Drag two **Network status** tiles to the dashboard (or drag one and then clone it).  
   Position one under the **Local** header and the other under the **Remote** header.

   At this point, all of the tiles query the local environment, so you have two identical **Host health** tiles and two identical **Network status** tiles.

   ![Same tiles, same environments](https://dt-cdn.net/images/same-tiles-same-environments-595-51063546a9.png)
6. Under the **Remote** header, edit the **Host health** and **Network status** tiles so that both of them query the remote environment (`Boston` in this example).

   ![Example: select remote environment for tile](https://dt-cdn.net/images/select-tile-environment-example-317-72348cc81f.png)
7. Select **Done** to display the dashboard.

   * The tiles under **Local** still display local host and network information.
   * The tiles under **Remote** now query the remote environment:

     + The remote tiles display the host health and network status for the remote environment, not the default local environment.
     + The remote tiles each display a filter icon. Hover over the icon to see the environment name.

   ![Same tiles, different environments](https://dt-cdn.net/images/same-tiles-different-environments-595-d747473897.png)

You can of course add other tile types and point to additional remote environments.

## Troubleshooting

[`Verification failed, please check your settings: Constraints violated.` message displayed when adding a remote environmentï»¿](https://dt-url.net/t903mr6)

## Related topics

* [Dashboards Classic API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")
* [Remote environments API](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")
* [What is a monitoring environment?](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")


---


## Source: dashboards-preset.md


---
title: Preset Dynatrace dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-preset
scraped: 2026-02-17T05:07:03.066884
---

# Preset Dynatrace dashboards

# Preset Dynatrace dashboards

* How-to guide
* 4-min read
* Published Feb 04, 2021

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

Preset dashboards are visible to all users by default.

* On the **Dashboards** page, the name of each preset dashboard is followed by the `Preset` tag.
* To display only preset dashboards, set the `Preset` filter to `Yes`.

Dynatrace offers several domain-specific out-of-the-box preset dashboards. Use them as inspiration for your own dashboards and clone them to create your own customized versions.

* You can create your own preset dashboards.
* You can set any preset dashboard as the home dashboard for a user group.

## Manage global settings

Preset dashboards are visible to all users by default. You can use the global settings to turn them off entirely or to limit visibility to certain user groups.

### Enable presets

Use **Enable presets** to turn preset dashboards on or off globally. If you turn it off, dashboards marked as presets will no longer appear on **Dashboard** tables for any users.

### Limit preset visibility

Use preset rules to ensure that specific preset dashboards are visible only to specific user groups and not to all users in the environment.

1. Go to **Settings** and select **Dashboards** > **Preset settings**.
2. In the **Limit preset visibility** section, **Add item**.

   * Set **Preset dashboard** to the preset dashboard for which you want to manage group access.
   * Set **User group** to the user group that should have access to the selected preset dashboard.
3. Select **Save changes**.

## List all preset dashboards

To list all preset dashboards

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Set a filter using one of these methods:

   * Under **Preset** in the left column, select `Yes`
   * On the **Filter by** line, select `Preset: Yes`
3. Select the name of any preset dashboard to display it.

## Out-of-the-box preset dashboards

You can't edit out-of-the-box preset dashboards, but you can clone them and edit the clones.

### To clone an out-of-the-box preset dashboard

Use **Clone** to create your personal, editable copy of a dashboard with `-cloned` appended to the dashboard name.

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Find the out-of-the-box preset dashboard you want to clone.
3. Use one of these methods to clone the dashboard:

   * Select **More** (**â¦**) > **Clone** for the dashboard you want to clone.
   * Open the dashboard, select **More** (**â¦**) in the upper-right of the dashboard, and select **Clone**.

To clone a dashboard you are currently displaying, select **More** (**â¦**) > **Clone**.

### To inspect and edit the clone

Now that you have a copy of the dashboard, you can experiment with it.

1. Select **Edit** to inspect and edit the dashboard components.

   * **Name**âSelect  after the dashboard name to personalize the name of your clone.
   * **Tags**âUnder the dashboard name, add and delete tags as needed.
   * **Markdown** and **Header** tilesâSelect them to see how to use text and headers on your dashboard to label and explain elements of the dashboard.
   * Other tilesâselect tiles to see the settings in the tile-specific pane on the right. See [Available tiles](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/available-tiles "Find out how to configure your dashboard to track business-critical user-actions and conversion goals.") for tile-specific help.
2. Select **Done** to save any changes and display the working dashboard.
3. Try drilldowns from the tiles to see where they go.

   * Open a tile's menu to see menu options.
   * Select tile elements to see available actions.

## Create a preset dashboard

You can create and modify your own preset dashboards.

* Preset dashboards are automatically shared to all users
* Preset dashboards appear on the **Dashboards** table for all users

You need one of the following permissions:

* Environment-wide permission **Change monitoring settings**
* Role `ALLOW environment:roles:manage-settings`

To designate a dashboard as a preset dashboard

1. [Create a dashboard](/docs/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.") or display an existing dashboard for which you have editing rights.
2. Select **Edit**.
3. Switch to the **Settings** tab and then select **Configure more**.
4. On the **Manage access** tab, turn on **Publish as preset**.
5. **Save changes**.

To verify the change

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Filter by `Preset: Yes`.
3. Make sure the dashboard is displayed in the table.  
   Also, each preset dashboard has a `Preset` tag after its name in the table.

## Assign a home dashboard

If you have admin privileges, you can assign a preset dashboard as the home dashboard for a user group. The selected dashboard will become that group's default landing page.

1. Go to **Settings** > **Dashboards** > **General settings**.
2. Select **Configure home dashboard**.
3. Set **User group** to the group whose home dashboard you want to set.
4. Set **Home dashboard** to one of the preset dashboards on the list.  
   If your dashboard isn't listed, make sure it's set as a preset dashboard.
5. Select **Save changes**.


---


## Source: dashboards-settings.md


---
title: Global Dynatrace dashboard settings
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-settings
scraped: 2026-02-17T21:28:55.364554
---

# Global Dynatrace dashboard settings

# Global Dynatrace dashboard settings

* How-to guide
* 2-min read
* Published Mar 05, 2021

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

Use the **Global dashboard settings** page to configure dashboard global settings and global settings for dashboard sharing and preset dashboards.

## General settings

### Allow anonymous access

With public sharing, even users who don't have access to the related Dynatrace environment or any Dynatrace access at all can view (but not change) your dashboard.

1. Go to **Settings** and select **Dashboards** > **General settings**.
2. Turn **Allow anonymous access** on or off to determine at the global (account) level whether dashboards can be shared publicly.
3. Select **Save changes**.

### Home dashboards

You can assign a preset dashboard as the home dashboard for any user group. The selected dashboard will become that group's default landing page.

1. Go to **Settings** and select **Dashboards** > **General settings**.
2. Select **Configure home dashboard**.
3. Select **User group**.
4. Select a preset dashboard from the **Home dashboard** list.  
   If your dashboard isn't listed, make sure it's a [preset dashboard](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-preset "Learn about out-of-the-box Dynatrace dashboards and how to create your own preset dashboards.").
5. Select **Save changes**.

## Preset settings

Use this page to configure preset dashboard settings at the global level.

Preset dashboards are visible to all users by default. You can use the global settings to turn them off entirely or to limit visibility to certain user groups.

### Enable presets

Use **Enable preset** to turn preset dashboards on or off globally. If you turn it off, any dashboard marked as a preset will no longer be displayed on other users' **Dashboard** tables.

### Limit preset visibility

Use preset rules to ensure that specific preset dashboards are visible only to specific user groups and not to all users in the environment.

1. Go to **Settings** and select **Dashboards** > **Preset settings**.
2. In the **Limit preset visibility** section, **Add item**.

   * Set **Preset dashboard** to the preset dashboard for which you want to manage group access.
   * Set **User group** to the user group that should have access to the selected preset dashboard.
3. Select **Save changes**.

For more on preset dashboards, see [Preset dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-preset "Learn about out-of-the-box Dynatrace dashboards and how to create your own preset dashboards.").

## Allowed URL pattern rules

To add an image to your dashboard via URL, you first need to add a URL rule to the allowlist.

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

Then you can add a dashboard image via URL.

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Drag an **Image** tile into position.
5. On the **Image** panel, select the **Add image URL** tab.
6. Enter the URL of the image file you want to display in the tile. It needs to match one of the rules on the allowlist.
7. Size and position the tile as needed.


---


## Source: share-dashboards.md


---
title: Share Dynatrace dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/share-dashboards
scraped: 2026-02-17T21:33:15.228037
---

# Share Dynatrace dashboards

# Share Dynatrace dashboards

* How-to guide
* 7-min read
* Published Jul 19, 2017

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

You can share your dashboards with anyone, even if they don't have their own accounts within the same Dynatrace environment.

Limitations

* It is not possible to use an anonymous dashboard link to access Grail data.

## Quick start

To share a dashboard

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.
4. Turn on **Share dashboard** and specify the sharing details as described below.

   * [Grant access to a specific user](#access-user)
   * [Grant access to a specific group](#access-group)
   * [Grant access to any user with the link](#access-all-authenticated)
   * [Grant anonymous access](#access-anonymous)

   You can combine these options. For example, you might grant `Edit` access to dashboard developers and grant `View` access to other users or groups in your organization.
5. Select **Save changes**.

To stop sharing a dashboard

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. In the pop-up, turn off **Share this dashboard**.

Any share settings you made previously are preserved and will be reactivated if you turn **Share this dashboard** back on.

## Configure global dashboard sharing settings

With public sharing, even users who don't have access to the related Dynatrace environment or any Dynatrace access at all can view (but not change) your dashboard.

1. Go to **Settings** and select **Dashboards** > **General settings**.
2. Turn **Allow anonymous access** on or off to determine at the global (account) level whether dashboards can be shared publicly.
3. Select **Save changes**.

## Grant access to a specific user

To grant access to an authenticated Dynatrace user

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

1. Turn on **Share dashboard**.
2. Under **Access permissions**, select **Grant access permission**.
3. From the **Who to grant access to** list, select **Specific user**.
4. From the **User** list, select the user to whom you want to grant access.
5. From the **What they should be able to do with the dashboard**, select `Edit` or `View`.
6. Select **Save changes**.  
   The specified user is added to the list under **Grant access permission**.

   * When **Share dashboard** is turned on, the selected user has access to your dashboard as you specified above (`Edit` or `View`).
   * To change the access type (`Edit` or `View`), select **Details** for that user and change **What they should be able to do with the dashboard**.
   * To revoke this access, select **Delete** for that user.

   Users assigned the `Edit` permission can edit shared dashboards. Be careful about sharing `Edit` permission:

   * Changes someone else makes to a dashboard will affect all users who share the dashboard.
   * When two users edit the same dashboard at the same time, the most recently saved changes take precedence over earlier changes. If you attempt to edit a dashboard that is currently being edited by another user, you'll see a notification.

## Grant access to a specific group

To grant access to everyone in a Dynatrace user group

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

1. Turn on **Share dashboard**.
2. Under **Access permissions**, select **Grant access permission**.
3. Under **Who to grant access to**, select **Specific group**.
4. Under **User group**, select the group to whom you want to grant access to your dashboard.
5. From the **What they should be able to do with the dashboard**, select `Edit` or `View`.
6. Select **Save changes**.  
   The specified user group is added to the list under **Grant access permission**.

   * When **Share dashboard** is turned on, everyone in the selected user group has access to your dashboard as you specified above (`Edit` or `View`).
   * To change the access type (`Edit` or `View`), select **Details** for that user group and change **What they should be able to do with the dashboard**.
   * To revoke this access, select **Delete** for that user group.

   Users assigned the `Edit` permission can edit shared dashboards. Be careful about sharing `Edit` permission:

   * Changes someone else makes to a dashboard will affect all users who share the dashboard.
   * When two users edit the same dashboard at the same time, the most recently saved changes take precedence over earlier changes. If you attempt to edit a dashboard that is currently being edited by another user, you'll see a notification.

## Grant access to any user with the link

To grant access to any authenticated Dynatrace user who has a copy of the shared link

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

1. Turn on **Share dashboard**.
2. Under **Access permissions**, select **Grant access permission**.
3. Under **Who to grant access to**, select **Any user with the link**.
4. Select **Copy link** to get the link you need to share the dashboard.
5. Select **Save changes**.  
   **Any user with the link has permission** is added to the list of permissions under the **Grant access permission** button.
6. Share the link (address) with users who should view the dashboard.

   * When **Share dashboard** is turned on, any user who has a copy of the link can use it to view the dashboard.
   * The dashboard will not be visible on the user's **Dashboards** table in Dynatrace until they use the link for the first time.
   * To revoke this access, select **Delete** in the **Any user with the link has permission** row.

## Grant anonymous access

You can grant **anonymous access** to your dashboard based on distributable links to the dashboard:

* Anonymous access grants view permission only
* You can specify links per management zone
* To enable or disable anonymous access for your environment, see **Settings** > **Dashboards** > **General settings**.

* It is not possible to use an anonymous dashboard link to access Grail data.

### Create a shareable link to your dashboard

To create a shareable link to your dashboard that can be used by anyone (with no authentication)

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

1. Turn on **Share dashboard**.
2. Under **Anonymous access**, select **Add anonymous access link**.
3. From **Management Zone for anonymous access link**, select a management zone or leave it set to `default`.

   * Which management zones are available depends on your permissions when you create the link.
4. Select **Save changes**.  
   A shareable link is added to the list displayed under **Add anonymous access link**.
5. Expand the list entry (**Details**) and select **Copy link** to copy the link to your clipboard. Paste the link to any message you send referring to the dashboard.

Repeat this procedure to create multiple anonymous links.

* If a [default timeframe and management zone](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe#default "Learn about Dynatrace dashboard timeframe and management zone settings.") are set for the dashboard, the link is shared with those settings. Otherwise, the link is shared with the timeframe of **last 2 hours** and **All** management zone.
* If the dashboard is shared with the **All** management zone, a recipient of the link has access to the management zones that you had access to when you created the link.

### Revoke a shareable link to your dashboard

To revoke a shareable link to your dashboard that can be used by anyone (with no authentication)

1. Under **Anonymous access**, locate the link.
2. Select **X** in the **Delete** column for that row and then select **Save changes**.

### Caution on shared links

A shared link has the creator's permissions, not the recipient's permissions.

* Anyone using a link you create can see everything you see through that link (such as management zones).
* If you lose permissions, people using your link also lose those permissions.

To maintain stricter control over who can see your dashboard, use the authenticated options per user, group, or environment.


---


## Source: metrics-browser.md


---
title: Metrics browser
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/metrics-browser
scraped: 2026-02-15T09:08:57.807077
---

# Metrics browser

# Metrics browser

* How-to guide
* 5-min read
* Updated on Aug 01, 2022

Early Adopter

Go to **Metrics** to open the **Metrics** browser, which is a cool tool for browsing all metrics available in your monitoring environment and making a quick metric-specific visualization.

* [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards."): You can pin the visualization to a classic dashboard.

## Filter and sort the table

* By default, the table of metrics is filtered to show only those metrics that were last reported after the start of the selected timeframe (for example, `Last 2 hours`). Turn off **Only show metrics reported after the start of the selected timeframe** to see all metrics regardless of when they were last reported.
* Set **Favorites** to `Any`, `Yes`, or `No` to filter the table by metrics that you have favorited.

  + To favorite a metric, select the star in the **Favorite** column of the table. Favorited metrics sort to the top of the table by default.
  + To unfavorite a metric, select the star again.
* The filter bar (**Filtered by**) has the following options.

  + `Text`âSelect `Text`, enter a filter string, and then press **Enter** to list metrics that include the string in **Metric name**, **Metric key**, or **Description**.
  + `Tag`âSelect `Tag`, enter a filter string, and then select a matching tag to list metrics that include the tag in **Tags**.
  + `Unit`âSelect `Unit`, enter a filter string, and then select a matching metric unit (for example, `Percent`) to list metrics that have the selected **Unit**.
  + `Favorites`âSelect `Favorites` and then select `Yes` (to list only favorited metrics) or `No` (to list only metrics that are not favorited).
  + `Dimension`âSelect `Dimension`, enter a filter string, and then select a matching metric dimension (for example, `Host`) to list metrics that have the selected dimension.

    If you combine filters, they are ANDed together. For example, if you set `Dimension` to `Host` and set `Text` to `usage`, the metrics browser lists all metrics with the `Host` dimension that also include the string `usage` in the **Metric name**, **Metric key**, or **Description** field.
* Select column header **Favorite**, **Name**, or **Key** to sort by the selected column.
* Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column to display metric details.

## Review metric details

Expand **Details** for any metric (row) in the table to see metric details and a visualization of the metric over the selected timeframe.

Metric details available in the 'Metrics browser'

Field

Description

Metric name

The name of the metric in the user interface.

Metric key

The fully qualified key of the metric. If a transformation has been used, it is reflected in the metric key.

Entity type

Entity type for this metric.

Description

A short description of the metric.

Tags

Tags allow further grouping of metrics.

Created

The timestamp when the metric was created.

Last written

The timestamp when the metric was last written.

DDU billing

Whether the metric is subject to [Davis data unit (DDU) consumption](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

Unit

The unit of the metric.

Minimum value

The known lower boundary value for the metric.

Maximum value

The known upper boundary value for the metric.

Default aggregation

The default aggregation for this metric.

Aggregations

The list of allowed aggregations for this metric.

Dimensions

The fine metric division (for example, process group and process ID for a process-related metric).

Transformations

Possible transform operators.

## Order-of-magnitude notation

In this example, you can see values displayed in millions. This is order-of-magnitude notation (`7.5M` means "about 7.5 million" and not "exactly 7.5 million").

The order of magnitude here is selected automatically based on the size of the values. For example, the same metric measured over a shorter timeframe might be displayed in `k` values instead of `M`.

![Example order-of-magnitude values in the metrics browser.](https://dt-cdn.net/images/magnitude-metrics-browser-1284-02225955bf.png)

Examples of order-of-magnitude notation in Dynatrace:

Notation

Factor

Meaning

k

10^3

kilo, thousand

M

10^6

mega, million

G

10^9

giga, billion

T

10^12

tera, trillion

For details, see [Order-of-magnitude notation](/docs/discover-dynatrace/get-started/dynatrace-ui/order-of-magnitude-notation "Dynatrace order-of-magnitude notation for displaying metric values").

## Add metric to dashboard

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

To add a metric to a classic dashboard

1. Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column to display metric details.
2. Select **Create chart** to open the metric in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").
3. Adjust the query and visualization settings as needed. For details, see [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or [Data Explorer quick start](/docs/analyze-explore-automate/explorer/explorer-quick-start "Using Data Explorer, create your first query, select a visualization, and pin the results to a dashboard.").
4. Select **Pin to dashboard**.
5. Specify the target dashboard and metric title.
6. Select **Pin**.

## Metadata for custom metrics

To provide contextual information for custom metrics (for example, to define the unit of measurement, or to provide display names or descriptions or even information such as lower and upper value ranges or Davis-relevant information), you can create metric metadata per metric key.

Once this information is provided, it becomes part of the metrics descriptor and can be queried via the API and used in the Metrics Browser and Data Explorer.

* Providing metadata via Settings 2.0 is available only for custom/schemaless metrics, not for built-in/code-registered metrics.
* The metadata provided for a specific metric key exists side-by-side with the metric time series itself. You can even create the metric metadata before you ingest datapoints for the first time.

### Configuration via API

Metric metadata is fully configurable via API. For details, see [Custom metric metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.").

### Configuration via web UI

To configure metric metadata for custom metrics via the web UI

1. Go to **Metrics**.
2. Select ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column to display metric details.
3. Select **Edit metadata**.  
   If you don't see an **Edit metadata** button in the expanded row, you haven't selected a custom metric.
4. On the **Metric metadata** page, edit the metadata for the selected metric.  
   If the page displays a lock, you don't have the necessary write permissions to edit the selected metric's metadata.

   * **Display name**âEnter a human-friendly name for the metric.
   * **Description**âEnter a free-form description of the metric: how it is measured, etc.
   * **Unit**âSelect a unit from the list.
   * **Metric properties**

     + **Minimum value**âThe lower boundary of the metric.
     + **Maximum value**âThe upper boundary of the metric.
     + **Root cause relevant**âA root-cause relevant metric represents a strong indicator for a faulty component.
     + **Impact relevant**âAn impact-relevant metric is highly dependent on other metrics and changes because an underlying root-cause metric has changed.
     + **Value type**âThe type of the metric's value. You have these options:

       - `score`: A score metric is a metric where high values indicate a good situation, while low values indicate trouble. An example of such a metric is a success rate.
       - `error`: An error metric is a metric where high values indicate trouble, while low values indicate a good situation. An example of such a metric is an error count.
     + **Latency**âThe latency of the metric, in minutes. It indicates how long it takes before an ingested new metric data point is available in Dynatrace.
   * **Metric dimensions**âTo add a dimension, select **Add dimension** and enter the **Dimension key** and **Display name** for the dimension.
   * **Tags**âTo add a tag, select **Add tag** and enter the tag.
   * **Source entity type**âTo configure the entity type of the metric. Only editable if the metric is ingested via an API endpoint.
5. Select **Save changes** to save your edits.


---
