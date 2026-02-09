---
title: "Dashboards"
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards-classic
updated: 2026-02-09
---

# Dashboards

# Dashboards

* Reference
* 7-min read
* Published Sep 25, 2018

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

Each dashboard consists of tiles and visualizations that can be selected, configured, and positioned to best meet your needs. Dynatrace provides many preconfigured tiles in addition to a number of configurable tiles that you can customize to visualize the metrics that are most relevant to the people using the dashboard. Select any dashboard tile that reports on monitored entities in your environment (hosts, processes, or services) to view the list of monitored entities.

Example dashboard

This simple example has four standard tiles.

* Everything's looking good: all green, no red, no problems.
* If you did have problems, you would see an indicator to warn you, and you could, for example, drill down from a problematic (red) host to investigate.

For more elaborate examples

1. Go to **Dashboards**.
2. Filter the table by `Owner: Dynatrace`.
3. Open some of our out-of-the-box preset dashboards.

![Dashboard general example](https://dt-cdn.net/images/dashboard-general-example3-778-3ecb2bdf91.png)

You can make different dashboards for specific people, roles, and teams, so everyone can focus on what's important to them.

Basic navigation

1. Go to **Dashboards**.
2. Select any dashboard on the list to open that dashboard.
3. When you open a dashboard, it becomes your *current dashboard*.

* From a health tile (such as **Host health**, **Service health**, and **Application health**), where you see green and red elements (such as hosts, services, or applications), hover over any problematic (red) element to see the identity of the element.
* To drill down to a problematic (red) element, select the red hexagon and then select the **Viewâ¦** button. On this example **Synthetic monitor health** tile, we have selected a red element, which enabled the **View test** drilldown button for that element.

  ![Drill down to problematic entity from health tile](https://dt-cdn.net/images/tile-health-bad-drilldown-276-6265617519.png)
* You can't drill down from a healthy (green) element. From any tile, however, you can select the menu in the upper-right corner of the tile and then select **View details** to display the relevant Dynatrace page for the tile. For example, **View details** from a **Synthetic monitor health** tile displays the **Synthetic monitors** table.

  ![Select tile menu](https://dt-cdn.net/images/tile-health-menu-open-272-17a936feef.png)

  ![Select 'View details' from tile menu](https://dt-cdn.net/images/tile-health-menu-view-details-270-aaf4eae8ec.png)

* If you drill down from a tile, you can always select the dashboard button

  ![Dashboard button](https://dt-cdn.net/images/home-icon-26-dd12d3ab04.png)

  in the upper-left corner of the Dynatrace web UI to return to your current dashboard. If you select the dashboard button while you're already on a dashboard, you instead go to the **Dashboards** page.
* You can open several dashboards at the same time in multiple browser tabs, one dashboard per browser tab.

Dashboard tile refresh rates

Every dashboard tile is refreshed automatically to update visualized data. Depending on the content shown in a tile and especially the applied timeframe, the refresh interval can vary.

| Dashboard timeframe | Refresh interval |
| --- | --- |
| Last 2 hours and less | 1 minute |
| Last 2 hours to last 6 hours | 5 minutes |
| Last 6 hours to last 24 hours | 15 minutes |
| Last 24 hours to last 72 hours | 30 minutes |
| Last 72 hours and more | 1 hour |

* For heavily used environments, Dynatrace may reduce the refresh rate to prevent Dynatrace server overload.
* Unlike other tile types, an image tile is not automatically refreshed. You need to refresh a dashboard manually to update the image tiles on that dashboard.

## Procedures

Use the following procedures to create and manage dashboards.

### Dashboards

Dashboards consist of tiles that can have their own settings for timeframe, management zone, and sharing.

Browse and display dashboards

1. Go to **Dashboards**.  
   This lists all dashboards you are permitted to view or edit.
2. To list only your dashboards, set the filter to `Ownership: Mine`.
3. To display a dashboard, select its name in the list of dashboards.

   * To open multiple copies of the same dashboard, right-click the dashboard title on the **Dashboards** page and open the link in a new tab or window. (Alternatively, you can copy and paste the address line from a dashboard page and paste it on the address line of a different browser tab or window.)

For details on using the **Dashboards** table, see [Organize dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/organize-dashboards "Learn how to organize your Dynatrace dashboards.").

List dashboards by popularity

1. Go to **Dashboards**.  
   This lists all dashboards you are permitted to view or edit.
2. Sort the table by the **Popularity** column.

List my dashboards

To list just your own dashboards

1. Go to **Dashboards**.
2. Set a filter using one of these methods:

   * Under **Ownership** in the left column, select `Mine`
   * On the **Filter by** line, select `Ownership: Mine`

Return to the current dashboard

![Dashboard button](https://dt-cdn.net/images/dashboardbutton-28-e3cbad6cfe.png)

The current dashboard is your most recently visited dashboard.

* When you drill down from a dashboard, select the dashboard button in the upper-left corner of Dynatrace to go back to the current dashboard.
* If you are already on a dashboard, the dashboard button takes you to the **Dashboards** explorer.

Create a new (empty) dashboard

1. Go to **Dashboards**.
2. Select **Create Dashboard**.
3. Enter a name for your dashboard and select **Create**. The new dashboard opens in edit mode.
4. Optional To add a tile, drag it from the **Tiles** pane to the dashboard, or [pin a tile to the dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").
5. Optional To configure dashboard-specific settings, select the **Settings** tile.
6. Select **Done**.  
   The new dashboard is displayed as it will appear to you and people with whom you [share](/managed/analyze-explore-automate/dashboards-classic/dashboards/share-dashboards "Learn how to share your Dynatrace dashboards with others.") it, though other people will not see the **Edit** button if you don't give them edit permission.

For details on creating dashboards, see [Create and edit Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.")

Clone an existing dashboard

1. Go to **Dashboards**.
2. In the table of dashboards, select **More** (**â¦**) > **Clone** for the dashboard you want to copy.

   * The copy opens in edit mode.
   * The original dashboard is unaffected.

For details on creating dashboards, see [Create and edit Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.")

Edit an existing dashboard

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.

Hide and unhide dashboards

To hide a dashboard

1. Go to **Dashboards**.
2. In the table of dashboards, select **More** (**â¦**) > **Hide** for the dashboard you want to hide.

To unhide a dashboard

1. Go to **Dashboards**.
2. Filter the table by `Hidden: Yes` to display all of your hidden dashboards.
3. In the table of dashboards, select **More** (**â¦**) > **Unhide** for the dashboard you want to unhide.

Delete a dashboard

1. Go to **Dashboards**.
2. In the table of dashboards, select **More** (**â¦**) > **Delete** for the dashboard you want to delete.

   * If you don't see a **Delete** option, you don't have permission to delete that dashboard.
3. Confirm the deletion to remove the dashboard.

Favorite a dashboard

To favorite the dashboard you are viewing, select the star in the upper-right corner of the dashboard. The star toggles favoriting on and off.

![Favoriting the current dashboard](https://dt-cdn.net/images/favorite-current-dashboard-169-caf101b927.png)

To favorite multiple dashboards

1. Go to **Dashboards**.  
   By default, the table is sorted by the **Favorite** column, so your favorites should be listed at the top of the table.
2. In the **Favorite** column, select the star for each dashboard you want to favorite.

For more on organizing dashboards, see [Organize dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/organize-dashboards "Learn how to organize your Dynatrace dashboards.").

Unfavorite a dashboard

To unfavorite the dashboard you are viewing, select the star in the upper-right corner of the dashboard. The star toggles favoriting on and off.

![Unfavoriting the current dashboard](https://dt-cdn.net/images/unfavorite-current-dashboard-169-97f319d05f.png)

To unfavorite multiple dashboards

1. Go to **Dashboards**.  
   By default, the table is sorted by the **Favorite** column, so your favorites should be listed at the top of the table.
2. Optional To list only your favorites, filter the table by `Favorite: Yes`.
3. In the **Favorite** column, select the star for each dashboard you want to unfavorite.

For more on organizing dashboards, see [Organize dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/organize-dashboards "Learn how to organize your Dynatrace dashboards.").

List my favorite dashboards

1. Go to **Dashboards**.  
   By default, the table is sorted by the **Favorite** column, so your favorites should be listed at the top of the table, followed by the other dashboards you have permission to display.
2. Optional To list only your favorites, set a filter using one of these methods:

   * Under **Favorite** in the left column, select `Yes`
   * On the **Filter by** line, select `Favorite: Yes`

For more on organizing dashboards, see [Organize dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/organize-dashboards "Learn how to organize your Dynatrace dashboards.").

Tag a dashboard

1. Display the dashboard.
2. Select **Edit**.  
   If you don't see an **Edit** option, you don't have permission to edit that dashboard.
3. Select **Add tag** under the name of the dashboard, type the tag, and select **Add**.  
   Repeat this step as needed to add additional tags to this dashboard.
4. Select **Done**.

For more on tagging dashboards, see [Organize dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/organize-dashboards "Learn how to organize your Dynatrace dashboards.").

Share a dashboard

1. Display the dashboard you want to share.

   * To display a dashboard, go to **Dashboards** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

For details on your dashboard sharing options, see [Share dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/share-dashboards "Learn how to share your Dynatrace dashboards with others.").

Subscribe to dashboard reports

1. Display the dashboard.
2. Select **More** (**â¦**) > **Subscribe** in the upper-right corner of the dashboard.

   * If you don't see a **Subscribe** option, the dashboard owners have not enabled reports for that dashboard.
   * If you see an **Enable reports** button, you have edit rights to that dashboard and you must enable reports if you want to receive reports from that dashboard.
3. Select how often you want to receive a dashboard report in email (turn on **Weekly** or **Monthly** or both).

For details on subscribing to dashboard reports, see [Subscribe to dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Learn how to subscribe to reports generated from Dynatrace dashboards.").

Set a dashboard-specific timeframe

1. Switch to the **Settings** tab.
2. Turn on **Default timeframe**.
3. Select the timeframe you want to be the default for this dashboard.

For an overview of timeframes and management zones on dashboards, see [Dynatrace dashboard timeframe and management zone settings](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

Set a dashboard-specific management zone

1. Switch to the **Settings** tab.
2. Turn on **Default management zone**.
3. Select the management zone you want to be the default for this dashboard.

* For an overview of timeframes and management zones on dashboards, see [Dynatrace dashboard timeframe and management zone settings](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.")
* For more on using management zones to organize your dashboards, see [Organize Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/organize-dashboards "Learn how to organize your Dynatrace dashboards.")

Configure advanced settings

1. Display **Dashboard settings**.

   * If you're starting from the **Dashboards** page, find the dashboard and select **More** (**â¦**) > **Configure**
   * If you're starting from the dashboard, select **Edit**, switch to the **Settings** tab, and then select **Configure more**.

Print a dashboard to a PDF file

Printing a dashboard to a PDF file is supported for Chromium-based browsers (Chrome, Edge, Opera) and Safari. Printing a dashboard to PDF from Firefox is not yet supported.

1. Display the dashboard that you want to print to a PDF file.

   * To display a dashboard, go to **Dashboards** and select the name of the dashboard.
2. Select  > **Print PDF** in the upper-right corner of the dashboard.
3. Adjust the settings as needed.

   * **Destination:** Select **Save as PDF**.
   * **Options:** Select **Background graphics**.
   * **Pages:** If an empty page is generated, set **Pages** to `Custom` and then enter `1` for the page range that you want to print to PDF.
4. Select **Save**.
5. Select a name and destination for the PDF file.

Export and import dashboards

To export a dashboard

1. Go to **Dashboards**.
2. In the table of dashboards, select **More** (**â¦**) > **Export** for the dashboard you want to export.  
   The dashboard definition is exported as a JSON file to your computer.

To import a dashboard

1. Go to **Dashboards**.
2. Select **Import dashboard**.
3. Select the JSON file for the dashboard you want to import.  
   The imported dashboard opens in edit mode.

For details, see [Edit Dynatrace dashboard JSON](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.").

### Tiles

Tiles are the components of dashboards.

List available tiles

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.

Now you can scroll down the **Tiles** pane to see all tile types available for your dashboard.

For details on available tiles, see [Available tiles](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/available-tiles "Find out how to configure your dashboard to track business-critical user-actions and conversion goals.").

Create a metric visualization tile

1. Go to **Data Explorer**.
2. Select metrics.
3. Select **Run query** to verify your query and see further display options.
4. Select chart settings.
5. Select **Pin to dashboard**.
6. Select a dashboard for which you have edit permission.
7. Select **Pin**.

For details, see [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

Add a tile

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Drag a tile type from the **Tiles** pane to your dashboard.  
   To see a description of a tile, drag it to your dashboard and then refer to the description on the tile configuration panel.

Add an uploaded image

To add an uploaded graphic to your dashboard

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Drag an **Image** tile into position.
5. On the **Image** panel, select the **Upload an image** tab.
6. Select **Upload image**.
7. Browse for and select the image file you want to display in the tile.
8. Size and position the tile as needed.

Add image URL to allowlist

To add an image to your dashboard via URL, you first need to add the image URL to the allowlist.

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

Add image via URL

You first need to add the image URL to the allowlist.

To add an image to your dashboard via URL

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Drag an **Image** tile into position.
5. On the **Image** panel, select the **Add image URL** tab.
6. Enter the URL of the image file you want to display in the tile. It needs to match one of the rules on the allowlist.
7. Size and position the tile as needed.

Pin as a tile

Some Dynatrace pages can be pinned as a tile to a dashboard. Those pages have a **Pin to dashboard** button.

**Example**

1. Go to **Hosts**.
2. Set some filters to display only the hosts of interest.
3. Select **Pin to dashboard**.
4. Select a dashboard for which you have edit permission.
5. Select **Pin**.

In this example, the new tile on your dashboard shows a graphic representation of your host selection. If there are ten hosts listed on the **Hosts** page, there are ten hosts (and their health) indicated on the tile. Select **View details** from that tile's menu to return to the **Hosts** table with the same filters set.

For details, see [Pin tiles to your dashboard](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

Clone a tile to the current dashboard

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile that you want to clone (add a copy of the tile to the current dashboard) and then select **Clone**.

   * To clone multiple tiles to the current dashboard, drag a selection rectangle around the *x* tiles you want to clone and then select **Clone x tiles**.
5. Edit the cloned tiles as needed.

Clone a tile to another dashboard

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile you want to clone to another dashboard and then select **Clone to**.

   * To clone multiple tiles to another dashboard, drag a selection rectangle around the *x* tiles you want to clone and then select **Clone x to**.
5. In the **Where do you want to pin to?** pop-up window, select an existing dashboard or **Create new dashboard**.
6. Select **Pin** to add the selected tiles to the dashboard.
7. Edit the cloned tiles as needed.

Edit a tile

1. Display the dashboard.
2. Hover over the tile, select the tile menu in the upper-right corner, and select **Edit tile**.  
   The tile configuration settings are displayed.
3. Change the configuration as needed.  
   To be sure you're making the changes you want, keep an eye on the tile while you change the configuration settings. Tile configuration changes (such as a custom timeframe) are reflected in real time as you make them.
4. When you're finished, select **Done**.

Set a tile-specific timeframe

To set a tile timeframe that overrides the dashboard timeframe

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile you want to configure.
5. Turn on **Custom timeframe**.
6. Select the timeframe you want to be the default for this tile.
7. **Done**.  
   When you set a tile-specific timeframe, a filter is displayed in the upper-right of the tile. Hover over the filter to see the setting.

For an overview of timeframes and management zones on dashboards, see [Dashboard timeframe and management zone](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

Set a tile-specific management zone

To set a tile management zone that overrides the dashboard management zone

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile you want to configure.
5. Turn on **Custom management zone**.
6. Select the management zone you want to be the default for this tile.
7. **Done**.  
   When you set a tile-specific management zone, a filter is displayed in the upper-right of the tile. Hover over the filter to see the setting.

For an overview of timeframes and management zones on dashboards, see [Dashboard timeframe and management zone](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

Set a tile-specific environment

To set a tile environment that overrides the dashboard environment

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile you want to configure.
5. Under **Environment**, select the environment for this tile.
6. **Done**.  
   When you set a tile-specific environment, a filter is displayed in the upper-right of the tile. Hover over the filter to see the setting.

For details on remote environments, see [Create remote/multi-environment Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment "Create dashboards that display data from multiple Dynatrace environments.").

Delete a tile

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the unwanted tile.
5. Select **Delete** and then confirm your action.

   * To delete multiple tiles, drag a selection rectangle around the unwanted tiles, select **Delete x tiles**, and then confirm your action.

Move a tile

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select and drag the tile to a new location.

   * To move multiple tiles, drag a selection rectangle around the tiles, and then select and drag the selected tiles together to a new location.

Change a tile title

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Select the tile you want to configure.
5. Under **Title**, edit the tile title.
6. **Done**.

Create a header

1. Go to **Dashboards**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Drag a **Header** tile into position. For example, create a header above three related tiles.
5. Select the edit control on the header tile.
6. Edit the header text.
7. Size the header tile.
8. Select the check mark on the header tile. The header tile remains independent. You can move and resize it to label more than one tile with a single header.

## API

You can also manage dashboards through the [Dashboards API](/managed/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API."):

* [GET all dashboards](/managed/dynatrace-api/configuration-api/dashboards-api/get-all "View all dashboards of your environment via the Dynatrace Classic API."): List all dashboards of your Dynatrace environment.
* [GET a dashboard](/managed/dynatrace-api/configuration-api/dashboards-api/get-dashboard "View a dashboard via the Dynatrace Classic API."): Get parameters of a specified dashboard.
* [POST a dashboard](/managed/dynatrace-api/configuration-api/dashboards-api/post-dashboard "Create a dashboard via the Dynatrace Classic API."): Create a new dashboard.
* [PUT a dashboard](/managed/dynatrace-api/configuration-api/dashboards-api/put-dashboard "Edit a dashboard via the Dynatrace Classic API."): Update a specified dashboard.
* [DELETE a dashboard](/managed/dynatrace-api/configuration-api/dashboards-api/del-dashboard "Delete a dashboard via the Dynatrace Classic API."): Delete a specified dashboard.
* [GET sharing configuration](/managed/dynatrace-api/configuration-api/dashboards-api/get-sharing-config "View the sharing configuration of a dashboard via the Dynatrace Classic API."): Get the sharing configuration of the specified dashboard.
* [PUT sharing configuration](/managed/dynatrace-api/configuration-api/dashboards-api/put-sharing-config "Update the sharing configuration of a dashboard via the Dynatrace Classic API."): Update the sharing configuration of the specified dashboard.
* [Tile JSON models](/managed/dynatrace-api/configuration-api/dashboards-api/dashboards-api-tile-models "Learn the variations of tile JSON models in the Dynatrace Dashboards Classic API."): JSON models of dashboard tiles vary greatly, depending on the type of a tile. Check this page to see JSON models for each tile type.
