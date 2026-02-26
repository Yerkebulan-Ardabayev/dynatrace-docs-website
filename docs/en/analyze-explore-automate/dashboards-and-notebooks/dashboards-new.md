---
title: Dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new
scraped: 2026-02-26T21:13:41.464018
---

# Dashboards

# Dashboards

* Latest Dynatrace
* App
* 10-min read
* Updated on Jan 28, 2026

Prerequisites

### Permissions

The following table describes the required permissions.

app-engine:functions:run

Allows the user to run functions

app-engine:apps:run

Allows the user to run functions

app-engine:edge-connects:read

Allows the user to read EdgeConnect configuration via functions

document:environment-shares:read

Allows the user to access shared dashboards

document:direct-shares:read

Allows the user to access shared dashboards

state:user-app-states:write

Allows the app to persist view settings like the selected timeframe or variable values

state:user-app-states:read

Allows the app to read view settings like the selected timeframe or variable values

state:user-app-states:delete

Allows the app to delete view settings like the selected timeframe or variable values

davis:analyzers:read

Allows the user to read configuration of Davis analyzers

davis:analyzers:execute

Allows the user to run Davis analyzers

Get started

Concepts

Use cases

With ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, you can create powerful, data-driven documents for custom analytics.

![Get real-time insights by transforming complex data into dynamic, interactive dashboards.](https://dt-cdn.net/hub/00_General.png)![Start fast using our ready-made dashboards, designed for your everyday needs.](https://dt-cdn.net/hub/01_Ready_made.png)![Build your dashboard effortlessly with only a few clicks.](https://dt-cdn.net/hub/02_Explore.png)![Customize any visualization with ease.](https://dt-cdn.net/hub/03_Customize.png)![Experience dynamic and interactive dashboards with versatile variable filtering.](https://dt-cdn.net/hub/04_Variables.png)![Share your insights with others in seconds.](https://dt-cdn.net/hub/05_Share.png)

1 of 6Get real-time insights by transforming complex data into dynamic, interactive dashboards.

## Dashboard tiles

In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, a dashboard can consist of multiple tiles:

* [Explore](#explore): explore data such as your logs, metrics, and business events with our point-and-click interface.
* [Query](#query): displays data queried via Grail.
* [Code](#code): display data returned by code executed via Dynatrace functions.
* [Markdown](#markdown): static content edited in markdown.

### Explore tile

You can use the Explore options to explore your logs, metrics, business events, and more with our point-and-click interface. With zero knowledge of DQL or coding, you can create and start using dashboard tiles in minutes.

For more information, we have a whole [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") page that shows you how to create Explore tiles.

### Query tile

The query tiles allow you to easily query data from Grail and [visualize](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") the result in different ways.

A query tile consists of a query input where you can write a DQL query. In the query input, use **Ctrl**+**Space** to trigger autocompletion at any time.

You can control the timeframe for the query via the timeframe dropdown list. If the timeframe is defined in the query itself, the dropdown list is disabled.

### Code tile

The code section enables you to fetch data for your dashboard using Dynatrace functions.

### Markdown tile

A markdown section can be anything from a minor note about something on the dashboard to a whole page of formatted information with links and pictures.

* Easy to edit
* Attractive to look at

To insert queries from your dashboard with autocomplete, use **Ctrl**+**Space**.

You can link to other places in your dashboard and elsewhere.

Markdown link syntax

A link in Markdown is a label and link of the form `[label](address)`, where:

* The `label` is freeform text to display on the link in your Markdown tile or section
* The `address` specifies what to open when someone selects the link, such as a website or a Dynatrace app

## Use cases

Dashboards enables you to:

* Use readymade dashboards to monitor your system status in real-time.
* Create custom dashboards effortlessly with an easy-to-use editor or Davis CoPilotâ¢.
* Drill down into your data through seamless integration with other Dynatrace Apps.
* Utilize the power of Davis AI for spotting anomalies and forecasting directly on your charts.
* Search for any data type across the platform and combine them even with external data in a single view.
* Configure variable filters to monitor different resources within a single dashboard.

These procedures describe the basics of using ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and get you started on the way to customizing and creating your own dashboards.

## Use dashboards

### Use shortcuts

Keyboard shortcuts help you work faster in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

To list keyboard shortcuts, in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, open the  menu and select  **Keyboard shortcuts** or use keyboard shortcut **Shift**+**?**

| Action | Keyboard shortcut |
| --- | --- |
| **General** |  |
| Multiselect tiles | Select a tile, press **Space** to get a double border around the tile, use arrow keys to go to another tile, and then press **Space** again to select multiple tiles |
| Select all tiles | **Ctrl**/**Cmd**+**A** |
| Delete selected tiles | **Del** |
| Copy selected tiles to clipboard | **Ctrl**/**Cmd**+**C** |
| Paste tiles from clipboard | **Ctrl**/**Cmd**+**V** |
| Add tile | **Ctrl**/**Cmd**+**Shift**+**Enter** |
|  |  |
| **Code tiles** |  |
| Add code | **Shift**+**C** |
| Execute code | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Data tiles** |  |
| Add query | **Shift**+**D** |
| Run query | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Markdown tiles** |  |
| Add markdown | **Shift**+**M** |
|  |  |
| **Service-Level Objective tiles** |  |
| Add Service-Level Objective | **Shift**+**S** |
|  |  |
| **Variables** |  |
| Add variable | **Shift**+**V** |

### List dashboards

#### List all dashboards

To list dashboards

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, the **Last opened by you** section lists recently accessed dashboards.
3. Hover over a dashboard name and select  for a menu of available commands for that dashboard. In this example, we would display the menu for a dashboard called `my dashboard 3`.

   ![Dashboards: Last opened by you: dashboard-specific menu](https://dt-cdn.net/images/dashboards-last-opened-by-you-dashboard-specific-menu-269-08e78a134c.png)

   The commands you see in the menu depend on your permissions for that dashboard. For example, you can't rename someone else's dashboard unless they have given you edit permissions for that dashboard. (But you *can* make a copy of a shared dashboard and then edit your copy.)

   * **Rename** enables editing for the dashboard name
   * **Duplicate** makes a copy of the dashboard
   * **Download** writes the dashboard to a JSON file that you can import
   * **Change owner** assigns dashboard ownership to a new owner
   * **Move to trash** moves the dashboard to the trash can

   This icon  after a dashboard name means someone shared that dashboard with you.
4. To display a table of all dashboards to which you have accessâyour own dashboards and all dashboards that people have shared with youâselect  **All dashboards**.

   * To sort the table, select the **Name**, **Created**, or **Last modified** header.
   * To filter the table:

     + You can enter a search string in the  filter bar at the top of the table.
     + You can select **Owned by anyone**, **Owned by me**, or **Shared with me** in the list at the top of the table.
   * To create a new dashboard, select  **Dashboard** in the upper-left corner.
   * To upload a dashboard, select  **Upload** in the upper-left corner.
   * To delete a dashboard, select  **Move to trash**. If there's no  icon for a dashboard, it means you have permission to view that shared dashboard but not to delete it.
   * To list deleted dashboards, select the **Deleted** tab of the **Dashboards** page.

     + To restore a deleted dashboard, select  **Restore**.
     + To permanently delete a dashboard, select  **Delete permanently**.

#### List my dashboards

To list all dashboards you own

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **All dashboards**.
3. At the top of the **Dashboards** table, select **Owned by me**.

#### List dashboards shared with me

To list all dashboards shared with you

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **All dashboards**.
3. At the top of the **Dashboards** table, select **Shared with me**.

#### List ready-made dashboards

To list all ready-made dashboards

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel, select  **Ready-made dashboards**.

Alternatively, you can select  **All dashboards** and then change the filter at the top of the table from **All dashboards** to **Ready-made**.

What's special about ready-made documents

* Created and automatically distributed by Dynatrace as examples and templates.
* Read-only: you can edit them for use during your session, and you can save a copy with your changes, but you can't save your changes to the original document.
* This icon  in a table of documents indicates that it's a ready-made document.

### Display a dashboard

To display a dashboard

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. Select the name of the dashboard. In this example, we open `my dashboard 2`.

   ![Open a dashboard](https://dt-cdn.net/images/open-my-dashboard-2-264-194755db23.png)

### Interact with a tile

If you see something on a dashboard that you want to zoom in on, you can maximize it and have a closer look, and then minimize it again when you're done.

When you maximize a tile, it is temporarily zoomed to the maximum size of the display so you can see the details of the selected tile.

To maximize a tile

1. Hover over the tile to display the tile-specific commands.
2. Select  **Maximize**.

To return to the normal dashboard view, select **Minimize** in the upper-right corner.

### Refresh a dashboard

When you open a dashboard for the first time, the refresh rate is set to `Off` (no automatic refresh).

#### Manual refresh

To refresh the current dashboard manually, in the upper-right corner of the dashboard, select  (in the   pair).

#### Automatic refresh

To refresh the current dashboard automatically, in the upper-right corner of the dashboard, select  (in the   pair) and select a refresh rate.

* `Off` turns off automatic refresh
* Other settings will refresh the dashboard at the specified interval

If you change the refresh rate, that rate is remembered the next time you open the dashboard.

A frequent refresh rate can keep you literally up to the minute, but a complex dashboard may take some time to recalculate each time it is refreshed. Choose a refresh rate that suits your needs and the complexity of the dashboard.

### Edit read-only dashboards

When you open a document (dashboard or notebook) for which you don't have write permission, you can still edit the document during your session. After you're finished, you have two options:

* Save your changes to a new document
* Discard your changes

Example:

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, list the ready-made dashboards, and select the **Getting started** dashboard.

   It says  **Ready-made** in the upper-left corner, next to the document name.
2. Select the Pie chart tile and then select  **Edit**.
3. Change the visualization from Pie to Donut.

   Now you are offered two buttons: **Save as new** and **Discard changes**.
4. Use the updated dashboard as needed. You have full edit access for this session.
5. When you're finished, select what to do with your changes:

   * **Save as new**âsaves your changes in a new copy of the edited dashboard.
   * **Discard changes**âdiscards your changes and returns you to the unedited read-only dashboard.

### Select the timeframe

To review or change settings that apply to an entire dashboard

1. Display the dashboard.
2. In the upper-right corner of the dashboard, select  **Settings**.

   The **Settings** panel is displayed.
3. Review or change settings as needed.

   Custom timeframe

   To set a default timeframe for a dashboard

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Custom timeframe**.
   4. Select the default timeframe for the selected dashboard.

      Changing this setting does not immediately update the timeframe of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about the dashboard timeframes, see [Select the timeframe](#dashboard-timeframe).

   Default segment

   To review or change the dashboard default segment

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Default segment**.
   4. Select the default segment for the selected dashboard.

      Changing this setting does not immediately update the segment of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about dashboard segments, see [Select segments](#segment).

   {$} Variables

   To review or change dashboard variables

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.

      The **Settings** panel is displayed.
   3. Select **Variables**.

   For details about dashboard variables, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").

The timeframe describes the *when* of the data on the dashboard.

* When you open a dashboard for the first time, the standard global timeframe (**Last 2 hours**) is applied.
* If you change the global timeframe setting for your dashboard, that timeframe is applied the next time you open the dashboard. However, there are exceptions as described below.
* You can [set a dashboard-specific default timeframe](#timeframe-dashboard) that is applied each subsequent time you open the dashboard.
* You can [set a tile-specific timeframe](#timeframe-tile). This setting overrides the global timeframe.
* When you open a dashboard via a link, if a timeframe is included in the link, the link timeframe is applied and the default dashboard timeframe is ignored.

#### Change global timeframe

To change the global timeframe

1. In the upper-right corner of the dashboard, open the timeframe selector menu (the default is **Last 2 hours** ).
2. Select a new timeframe.

   * To select a standard timeframe, choose one of the standard **Relative timeframes**
   * To define a custom timeframe, define the timeframe in the **Custom timeframe** panel and select **Apply**.

     + Use the calendar buttons ![Calendar](https://dt-cdn.net/images/dashboards-app-dashboard-timeframe-calendar-b05d935595.svg "Calendar") to select calendar dates
     + Edit the resulting **From** and **To** settings to fine-tune the range

When you change the global timeframe:

* The new timeframe is displayed in the upper-right corner of the dashboard.
* The dashboard contents are recalculated and displayed according to the new timeframe. This overrides the default dashboard timeframe.
* This does not affect any tile-specific timeframe overrides. Tile-specific timeframes take precedence over any global timeframe settings.

#### Default dashboard timeframe

To set a default timeframe for a dashboard

1. Display the dashboard.
2. In the upper-right corner of the dashboard, select  **Settings**.
3. Turn on **Custom timeframe**.
4. Select the default timeframe for the selected dashboard.

   Changing this setting does not immediately update the timeframe of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

#### Tile-specific timeframe override

To specify a custom timeframe in a dashboard tile

1. Edit the tile.
2. In the edit panel, turn on **Custom timeframe**.
3. Select the timeframe to apply to the selected tile.

   This timeframe overrides the dashboard timeframe set in the upper-right corner of the dashboard. Using this method, a dashboard can have multiple tiles, where each tile has its own timeframe.

You can also specify a custom timeframe in a data tile's DQL query. If you use this method (with a timeframe specified in the query), the above UI setting is disabled and the timeframe specified in the query is used.

Example timeframe specification in DQL:

```
fetch [recordtype], from:now() - 2h



| ....
```

For details on specifying a timeframe in DQL, see [Specify timeframe](/docs/platform/grail/dynatrace-query-language/dql-guide#specifytimeframe "Find out how DQL works and what are DQL key concepts.") in the DQL documentation.

### Select segments

To filter data, you can specify segments at two levels: dashboard and tile. Tile-level segment selections override dashboard-level segment selections.

Should I use segments or variables?

#### Segments

Use segments when you want to reuse them across dashboards. For example, use segments for recurring filters such as for your Kubernetes clusters, namespaces, workloads, or pods. Segments automatically apply on top of the queries of your tiles/sections, so you donât need to reference them within.

#### Variables

If you need more control over how a filter is applied, however, you might want to use variables.

* Variables allow you to fully control the underlying query or within your Explore section or tile, determining where and how they are applied. For example, you can specify how they connect with other filters applied (**AND**, **OR**) and you can control which operator is used for your filter (such as `equals`, `contains`, `startsWith`, and `endsWith`).
* Additionally, use variables when you need fine-grained control over how filters are interdependent.

* For details on segments, see [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.")
* For a ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**-specific segments use case, see [Analyze monitoring data with segments](/docs/manage/segments/getting-started/segments-getting-started-analyze-monitoring-data "Learn how to analyze monitoring data more efficiently by using segments in Dashboards.")

#### Dashboard-level segments

To select dashboard-level segments

1. Display the dashboard.
2. Open the segment selector  at the top of the dashboard and, in **Filter by segments**, select a segment.  
   If the segment requires an additional value selection, select it now.
3. To add another segment, select  **Segment**. Repeat this step for each segment you want to add.
4. Select **Apply** to apply the selection and filter data on the dashboard.

   * The segment selector  now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

#### Tile-level segments

To select tile-level segments

1. Display the dashboard.
2. Select the tile and then select  in the tile controls to edit the tile.
3. In the edit panel, turn on **Custom segments**.
4. In the **Custom segments** list, select a segment.  
   If the segment requires an additional value selection, select it now.
5. To add another segment, select  **Segment**. Repeat this step for each segment you want to add for the selected tile.
6. Select **Apply** to apply the selection and filter data on the tile.

   * The segment selector  now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

### Dashboard settings

To review or change settings that apply to an entire dashboard

1. Display the dashboard.
2. In the upper-right corner of the dashboard, select  **Settings**.

   The **Settings** panel is displayed.
3. Review or change settings as needed.

   Custom timeframe

   To set a default timeframe for a dashboard

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Custom timeframe**.
   4. Select the default timeframe for the selected dashboard.

      Changing this setting does not immediately update the timeframe of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about the dashboard timeframes, see [Select the timeframe](#dashboard-timeframe).

   Default segment

   To review or change the dashboard default segment

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.
   3. Turn on **Default segment**.
   4. Select the default segment for the selected dashboard.

      Changing this setting does not immediately update the segment of the current dashboard. The change is applied only to a new session with the dashboard (either for a different user, or for the same user returning to the dashboard for another session).

   For details about dashboard segments, see [Select segments](#segment).

   {$} Variables

   To review or change dashboard variables

   1. Display the dashboard.
   2. In the upper-right corner of the dashboard, select  **Settings**.

      The **Settings** panel is displayed.
   3. Select **Variables**.

   For details about dashboard variables, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").

### Run a code tile

When you open a document from another user, you may see the following message:

`This dashboard contains custom code. It is read-only until you review the code and select âAccept and runâ.`

When you run a code tile or section written by another person, Dynatrace executes the other person's JavaScript using your user account and your permissions. This is a powerful feature, but it needs to be used correctly and responsibly. The JavaScript code can access external APIs on your behalf (using your account and permissions).

To review code

1. Select **Review all code**.

   The **Review code** page displays each code tile's code in a separate box.
2. Review the code and decide whether you want to run it.

   If you want to run the code, you can approve it just this time or permanently.

   * To run the code just this time, select **Accept and run**. The next time you open this document, you will be asked once again to review the code before running it.
   * To permanently accept the code in this document, select **Always trust code in this document** and then select **Accept and run**.

### Download result

To download (export) the result of the current dashboard tile or notebook section to a local file

1. Select the tile or section.
2. On the command bar, open the  menu and select  **Download result** > [format].

   The format options available depend on the visualization.

   * **CSV**: The result is downloaded to a local comma-separated values (\*.csv) file. This option includes table formatting such as visible columns and unit formatting.
   * **CSV (raw)**: The result is downloaded to a local comma-separated values (\*.csv) file. This option includes the complete unformatted data.
   * **JSON**: The result is downloaded to a local JSON (\*.json) file.

   Some visualizations offer no option to download the result.

#### Possible issue with importing CSV into Excel

When you export results to a CSV fileâwhether **CSV** or **CSV (raw)**âwith line breaks in any result column/field, and then open the file with Microsoft Excel or try to convert the file into a table using Excel option **Data** > **Text to Columns**, you may encounter an issue in which the line breaks are incorrectly rendered in Excel. This is caused by an Excel limitation.

To avoid this issue, use Excel option **Data** > **From Text/CSV**.

## Manage dashboards

### Add dashboard to Dock

To add a dashboard to the Dock for easy access

1. Display the dashboard.
2. Open the  menu next to the dashboard name (in the upper-left corner of the dashboard).
3. Select  **Add to dock**.

   If you change the name of the dashboard, it's automatically updated on the Dock.

To remove a dashboard from the Dock

1. Hover over the dashboard name in the Dock.
2. Select  **Unpin from dock**.

### Rename a dashboard

To rename a dashboard from the **Dashboards** panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

   The **Last opened by you** section lists your most recently accessed dashboards.
2. Hover over the name of the dashboard you want to rename and select  >  **Rename**. If the rename option isn't available, you don't have edit rights to that dashboard.

### Duplicate a dashboard

To duplicate a dashboard from the **Dashboards** panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

   The **Last opened by you** section lists your most recently accessed dashboards.
2. Hover over the name of the dashboard you want to duplicate and select  >  **Make a copy**.

To make a copy of the current dashboard

1. At the top of the dashboard, open the dashboard menu  next to the dashboard name.
2. Select  **Duplicate** from the menu.

   A copy is created with the name **Copy of** + the name of the current dashboard. The copy is now listed in the **Dashboards** panel.

### Share a dashboard

If you own a dashboard or notebook, you can share it.

There are three ways to share a document with other Dynatrace users in your company:

* **Access for all (view-only)**: Give view-only access to everyone in your Dynatrace environment.
* **Share access**: Create and maintain a list of users and user groups with access the document.
* **Share links**: Create links (URLs) pointing to your document and distribute the links through the channels of your choice (email, for example).

These methods are not mutually exclusive. For example, you can maintain a focused list of users for ongoing access to the document (maybe everyone in a certain group edits the document regularly) and you can create and distribute view-only links for a wider audience as needed.

In any case, you control whether people can edit the document or only view it.

For details on sharing documents, see [Share documents](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

### Manage dashboard versions

Dashboard versions are saved automatically.

* You can access the 50 most recent versions of your dashboard.
* Each dashboard version is available for up to 30 days.

To view and manage dashboard versions

1. Display your dashboard.
2. In the upper-right corner of your dashboard, select ![History](https://dt-cdn.net/images/history-icon-dc67cc1e2c.svg "History").

   This displays a menu of the most recent versions of the current dashboard.

   * Date
   * Time
   * Name of the person who created that version
3. From any version entry in the **Versions** menu, you can select version-specific actions.

   * ![Preview](https://dt-cdn.net/images/icon-preview-1-138a2e67eb.svg "Preview") **Preview** displays a preview of the selected version.
   * **Restore** switches your dashboard to the selected version.
   * **Make a copy** creates a new dashboard from the selected version and displays the new dashboard. The original dashboard remains unchanged.
   * **Download** saves a JSON file of the selected version of the dashboard to your local machine.
   * **Preview in new tab** displays a preview of the selected version on a new browser tab.
   * **Delete this version** deletes the selected version.
4. To list and manage all versions of the dashboard in a separate window, go to the bottom of the **Versions** menu and select **Show all**.

For details, see [Manage document versions](/docs/analyze-explore-automate/dashboards-and-notebooks/document-version "View and manage versions of documents created in Dynatrace Notebooks and Dashboards.").

### Change dashboard owner

When you create a document (dashboard or notebook), you are the owner. To give ownership of the document to another Dynatrace user

1. Open the  document menu and select  **Change owner**.
2. Find and select a new owner, and then select **Change owner**.

   When you change the document owner, you immediately lose access to the document.

   * Be sure you are ready to transfer ownership before you select this command.
   * You can regain access to the document only if the new owner gives you permission.
3. After the transfer is complete, the new owner will receive email about the document ownership transfer.

### Download a dashboard

To download (export) the currently displayed dashboard as JSON

1. At the top of the dashboard, open the  menu to the right of the dashboard name.
2. Select  **Download** from the menu.

   The definition of the current dashboard is downloaded to a local JSON file.

To download (export) a dashboard from the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** side panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In **Last opened by you**, hover over the name of the dashboard you want to export and select  **Download** from the  menu. The dashboard is downloaded to a local JSON file that you can upload.

   If your dashboard isn't listed in **Last opened by you**, select  **All dashboards** to display a table of all dashboards that you can access (your dashboards or dashboards shared with you). From there, you can find the dashboard and select  **Download** from the  menu.

### Upload a dashboard

To upload (import) the JSON definition of a dashboard from the **Dashboards** side panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel on the left, select  **Upload**.
3. Find and open the dashboard JSON definition file.

To upload (import) the JSON definition of a dashboard from the **Dashboards** table

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel on the left, select  **All dashboards**.

   A **Dashboards** table displays all dashboards by **Name** and **Last modified** date.
3. In the upper-left corner of the page, select  **Upload**.
4. Find and open the dashboard JSON definition file.

An uploaded dashboard is:

* Opened in Dynatrace.

  If you see a message about running custom code when you upload a dashboard, see [Run code warnings](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code#run-code-warnings "Add code to your Dynatrace dashboards.") for more information.
* Added to your **Last opened by you** list.
* Added to the **Dashboards** page with **Last modified** set to the upload date and time.

### Delete a dashboard

To delete any dashboard on the **Dashboards** page

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In the **Dashboards** panel on the left, select  **All dashboards**.

   A table displays all dashboards by **Name** and **Last modified** date.
3. On the **Dashboards** page, select  **Move to trash** for the dashboard you want to delete.

### Dashboards via API: best practices

When creating or managing dashboards via API, these best practices can make your life easier.

* To get a solid start, create the dashboard in the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** app and then [download](#dashboards-download) the dashboard configuration file.
* To verify changes made via API, [upload](#dashboards-upload) the file to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. Does everything still look as expected?
* Be careful with layout changes, as empty vertical spaces cause tiles to shift upwards automatically on document load and cause the **Discard changes** button to appear.
* To examine changes in detail, select **Save as new** to download the document and compare it with the original version.
* Don't set the `version` property of the config to an arbitrary value. It's an internal property needed for migration purposes.

## Create and edit dashboards

### Create a dashboard

The fastest and easiest way to explore your data is with our new [Explore](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") tiles and sections. In a few seconds, you can find and analyze your logs, metrics, or business events. No DQL required!

To create a new dashboard

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. Select  **Dashboard**.

After you create an empty dashboard, you need to add tiles to it.

* Query Grail
* Add code
* Add Markdown
* Add a variable
* Add a snippet

### Query Grail

To Query Grail

1. In the upper-right of the dashboard, select  **Add** >  **DQL**.

   Keyboard shortcut: **Shift**+**D**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   A configuration side panel opens on the right to display two tabs:

   * **Data**
   * **Visual**
2. On the **Data** tab, use the [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") to define your query.
3. Select **Run** to execute the query.
4. On the **Visual** tab, choose a [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") format for your results.

   * means the visualization type is unavailable for your query.
5. Under the **Visualization** selector, expand the options sections to adjust visualization settings as needed.
6. Close the side panel when you're done.

   If you want to return to these settings, select your tile to display them.

For details, see [Add data to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-data "Add data to your Dynatrace dashboards.").

### Add code

To add code to a dashboard

1. In the upper-right of the dashboard, select  **Add** >  **Code**.

   Keyboard shortcut: **Shift**+**C**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   An empty tile is added to the dashboard and an **Options** side panel opens on the right.
2. Optional In **Tile title**, enter a title to display at the top of your tile.
3. In the numbered **Code** box, enter custom JavaScript to fetch external data from any available API. Use the [Fetch APIï»¿](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) to fetch data from external APIs.

   To make sure your requests aren't blocked, ask your administrator to allow your external data sources by adding them to the **External requests**.

   External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
   2. Select  **New host pattern**.
   3. Add the domain names.
   4. Select **Add**.

   This way you can granularly control the web services your functions can connect to.

   Don't include the address prefix. For example, if the address is `https://some.service.org`, just add `some.service.org`.

For details, see [Add code to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Add code to your Dynatrace dashboards.").

### Add markdown

To add a markdown tile to a dashboard

1. In the upper-right of the dashboard, open the  **Add** menu and select  **Add markdown**.

   Keyboard shortcut: **Shift**+**M**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   An **Options** side panel opens on the right.
2. In the **Options** side panel, enter your text.

   * Use Markdown to format your text and add links and images.
   * The tile is updated as you edit.
   * While you're editing text, press Ctrl+Space to see options.
3. Close the **Options** side panel when you're done.

For details, see [Add Markdown to dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-markdown "Add Markdown-formatted annotations to your Dynatrace dashboards.").

### Add variable

Use variables to filter your dashboards, to act as variable values in code tiles, and as placeholders in tile titles and Markdown tile text.

To add a variable to a dashboard

1. In the dashboard header, open the  menu and select  **Variables**.
   Keyboard shortcut: **Shift**+**V**

   Keyboard shortcut: **Shift**+**V**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   The **Variable** panel is displayed.
2. Define the variable.

   * **Name**: the name of the variable.

     + Only alpha-numerical values are allowed
     + Do not start a variable name with `dt_`
   * **Type**: can be one of the following:

     + **DQL**: the value is returned from a query you enter when you define the variable.

       - Select **Run** to test your query.
     + **Code**: the value is returned from code you enter when you define the variable.
     + **List**: a comma-separated values (CSV) list of values.

       - To define possible values, enter them (separated by commas) in the box under **Data**.
       - To define a default value, select one from the **Default value** list.
       - To allow multiple values to be selected at the same time, turn on **Multi-select**.
     + **Free Text**: free text. You can enter a **Default value**.
       Your changes are saved automatically.
3. Set **Display settings**.

   * If the variable dropdown should be displayed on the dashboard, turn on **Display as filter on dashboard**.  
     Turn it off when you want it hidden, such as when the variable is used as a static value across tiles but should not be displayed to the dashboard user.
   * If users should be able to select multiple values at the same time within the variable dropdown, turn on **Multi-select**.  
     Turn it off when you want to use only single values of the variable dropdown.
   * Select a **Default value** for the variable dropdown. If you don't enter anything in this field, the first available value is selected.
4. When you're finished, select **< Variable** at the top to go to the **Variables** panel, or select  to dismiss the **Variables** panel.

Variables in dashboards can be defined to depend on other variables.

* The value of a variable is recalculated if its definition refers to another variable and the other variable's value changes.

  For example, if the value of variable A changes, the value of any variable whose definition refers to variable A is recalculated.
* Loops are not allowed.

  For example, if the value of variable A depends on the value of variable B, the value of variable B can't depend on the value of variable A.

For details, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").

### Add snippet

To get started based on a snippet

1. In the upper-right of the dashboard, select  **Add** to open the **Add** menu.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Shift**+**Enter**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)
2. Scroll down to the **Start with a snippet** section and choose one of the snippets. In this example, we select the  **Fetch logs** snippet, which is displayed in a preview panel.

   ![Example: select the "Fetch logs" snippet.](https://dt-cdn.net/images/add-snippet-menu-example-fetch-logs-754-d4435c09eb.png)
3. After you select a snippet, the edit panel displays the snippet you added.

   ![Example: "Fetch logs" snippet added.](https://dt-cdn.net/images/add-snippet-menu-example-fetch-logs-result-1436-77cc9fa8f1.png)
4. Edit the query or code (depending on the snippet type you selected) and the visualization settings as needed.
5. Select **Run** to see results.
6. Close the side panel when you're done.

For details, see [Add a snippet to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-snippet "Start with a snippet").

### Analyze data with AI

To analyze data using Dynatrace Intelligence Data Analyzers

1. Explore a timeseries.

   Example

   In your document (dashboard or notebook)

   1. Select  to add a new section or tile, and then select **Metrics** to explore metrics.

      ![Example: select Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
   2. In **Select metric**, select **Infrastructure** > **CPU** > **CPU usage %**.

      ![Example: select metric "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
   3. Set **Split by** to `host.name`.

      ![Example: set "Split by" to host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
   4. Set **Limit** to the maximum number of series to analyze. Dynatrace Intelligence Data Analyzer currently supports analysis up to 1000 series.

   You should get something like this:

   ![Example: complete query](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
2. Run the query.
3. In the options panel on the right, scroll down and expand  **Davis AI**.

   Show me

   ![An example of selecting the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![The initial panel for the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
4. On the **Davis AI** panel, set **Analyzers** to the analyzer you want to use, and then configure the analyzer.

   * For an overview of anomaly detection, see [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
   * For details on anomaly detection settings, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.")

   * For details on forecast analyzer settings, [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")

   Anomaly Detection: Auto adaptive threshold anomaly detection

   * **Number of signal fluctuations**âhow many times the signal fluctuation is added to the baseline to produce the actual threshold for alerting.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above, below, or outside (above or below) the normal range.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Anomaly Detection: Seasonal baseline anomaly detection

   * **Tolerance**âthe higher the tolerance, the broader the confidence band, leading to fewer triggered events.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above, below, or outside (above or below) the normal range.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Anomaly Detection: Static threshold anomaly detection

   * **Threshold**âa hard limit that a metric should not violate.
   * **Unit**âthe unit of the value.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above or below the threshold value.
   * **Suggest threshold**âDavis AI can help you to find the right threshold based on historical data.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Prediction: Forecast

   * **Data points to predict**âthe total steps the time series is forecasted. More steps generally results in less reliable forecasts and longer analyzer runtimes.
   * **Forecast offset**âan offset for the start of the forecast. For example, if the offset is set to `2`, the last two data points are ignored and a forecast for these points is returned as well.

   For details, see [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.").

   Advanced settings (for anomaly detection)

   You can use the default values or turn on **Show advanced properties** to fine-tune these settings.

   * **Alert on missing data**âalert if no data is detected within the sliding window.
   * **Violating samples**ânumber of samples in the sliding window that must violate to trigger an event.
   * **Sliding window**ânumber of samples that form the sliding window.
   * **Dealerting samples**ânumber of samples in the sliding window that must go back to normal to close the event.
5. By default, the analyzer is not enabled. To enable it, turn on the switch at the top of the edit panel (switch from **AI data analysis is not active** to **AI data analysis is active**).
6. To view the results, select the **Davis AI analysis** visualization and expand the **Davis AI analysis chart** section to review or change the visualization-specific settings:

   Show me

   ![Example of selecting "AI analysis" visualization and displaying visualization-specific settings in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)

   The **Davis AI analysis** visualization has two sections: chart and visualization. You can use the **Visible sections** setting to display either or both of them.

   * **All**âshow a chart and a table. The chart reflects your table selections.
   * **Table**âshow only a table. You can sort columns that display a sort icon  in the header. Select the column header to toggle the sort order up  or down .
   * **Chart**âshow only a chart. Use the table to select entries you want to show on the chart.

#### Example: anomalous CPU usage percent

To detect when CPU usage percent exceeds 70 percent, in your document (dashboard or notebook)

1. Select  to add a new section or tile, and then select **Metrics** to explore metrics.

   Show me

   ![Example: select Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
2. In **Select metric**, select **Infrastructure** > **CPU** > **CPU usage %**.

   Show me

   ![Example: select metric "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
3. Set **Split by** to `host.name`.

   Show me

   ![Example: set "Split by" to host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
4. Set **Limit** to the maximum number of series to analyze. Davis analyzer currently supports analysis up to 1000 series.

   Show me

   ![Example: complete query](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
5. Select **Run**.
6. In the edit panel, expand  **Davis AI**.

   Show me

   ![An example of selecting the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![The initial panel for the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
7. In the **Analyzers** list, select **Static threshold anomaly detection**.

   Show me

   ![Selecting the "Static threshold anomaly detection" analyzer in the Analyze and alert settings of the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-select-static-threshold-anomaly-detection-752-45026264f0.png)
8. Set **Threshold** to `70` (enter a value) and **Alert condition** to **Alert if metric is above** (default).

   Show me

   ![Configuring settings for the "Static threshold anomaly detection" analyzer in the Dashboards app.](https://dt-cdn.net/images/dashboards-static-threshold-anomaly-detection-settings-748-4d20c8220e.png)
9. Activate the analyzer: at the top of the edit panel, switch from **AI data analysis is not active** to **AI data analysis is active**.
10. To view the results, select the **Davis AI analysis** visualization. Expand the **Davis AI analysis chart** section to see visualization-specifc settings.

    Show me

    ![Example of selecting "AI analysis" visualization and displaying visualization-specific settings in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)
11. In the **Davis AI analysis chart** section, set **Visible sections** to **All**.
12. Review the results.

    In this example, we selected the hosts that exceeded the threshold.

    * The chart shows a line for the selected metric (`CPU usage %`) for each selected host.
    * A red bar across the top of the visualization indicates where the threshold for that metric was exceeded.
    * The table under the chart has those hosts selected.

    ![Example analyzer results with "AI analysis" visualization in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-chart-1920-5ac0e1f854.png)

### Change variable values

If a dashboard has one or more variables, they are listed by name along the upper-left of the dashboard, under the dashboard name. When you change variable values, the dashboard contents are recalculated and displayed according to the new values.

To change the value of a variable

1. In the upper-left of the dashboard, locate the variable name.
2. Use the menu or edit box under the variable name to change the value.

   * If the variable allows just one selection (value) at a time, select the value that you want to apply to the dashboard.
   * If the variable allows multiple selections (values) at a time, select the checkbox for each value you want to apply to the dashboard. The menu name for that variable shows how many values are selected.
   * For a Free Text variable, you can edit the text in the box under the variable name.

### Copy to another document

You can copy a dashboard tile to another document (such as a different dashboard or a notebook).

For example, an easy way to start a new notebook is to copy reusable tiles from existing dashboards to a new notebook and then edit the copied sections as part of the new notebook.

To copy a dashboard tile to a notebook (as a notebook section)

1. In the dashboard, select the tile that you want to copy to a notebook.
2. Open the  menu and select ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Add to notebook**.
3. In **Select destination**:

   * If you want to create a new notebook with the selected dashboard tile as a section, select **New notebook**.
   * If you want to add the selected dashboard tile as another section in an existing notebook, select the existing notebook from the list and then select **Confirm**.

   The notebook opens with the selected tile copied into it as a notebook section.

To copy a dashboard tile to a different app (not ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**), open the  menu and select  **Open with**, and then select the target app.

For details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/drilldowns-and-navigation "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

### Edit a tile

To edit a tile

1. Select the tile to display the tile-specific commands.
2. Select  **Edit**.

   An **Options** panel opens on the right to display the tile or section configuration.
3. Select and drag the expander control left or right as needed to resize the **Options** panel for a better look at the code.

   ![Resize options panel](https://dt-cdn.net/images/options-panel-resize-155-a8c92d2683.png)

### Add or edit a tile title

You can add a title to any dashboard tile (except for a Markdown tile).

Regardless of the title setting, a title bar is automatically created as needed to display tile indicators such as for a warning or to indicate a custom tile timeframe.

1. Select the tile and  edit it.

   * The title is displayed in the box at the top of the tile edit panel.
   * If the tile has no title, the box displays `Untitled tile`.
2. Edit the title. Your edits are displayed as you type.

   A title can include emojis (such as ð and ð and â¤ï¸) and variables.

   **Example:**

   1. In your dashboard, define [variables](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.") called `Status` and `Emoji`.
   2. Set the title to `Current $Emoji status is $Status`.
   3. Set variable `Status` to `Good`.
   4. Set variable `Emoji` to `ð`.

   The title will be displayed as `Current ð status is Good`, and it will update automatically when the variable values change.

To remove a tile title, select the tile and  edit it, and then clear the title box.

### Configure a tile visualization

Each visualization has visualization-specific settings.

To edit a tile visualization, see the [visualization instructions](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").

## Layout

### Resize a tile

To resize a tile

1. Hover over the tile.
2. Select and drag  in the lower-right corner of the tile to change the dimensions of the tile.

   To help you select a specific size, the tile size is displayed on the tile command bar.

### Move a tile

You can move one tile at a time or select and move multiple tiles simultaneously.

To move a tile, drag the tile to a new position.

* If the tile has a title, select and drag  the title bar to move the tile.
* If the tile has no title, select the tile to display the tile-specific commands, and then select and drag  on the tile command bar to drag the selected tile to a new location.

  To help you align tiles, a background grid is displayed when you're moving a tile.

To move multiple tiles simultaneously

1. Select one tile.
2. Ctrl-click additional tiles that you want to move.

   * Each selected tile is highlighted.
   * The total number of selected tiles is displayed on the tile command bar.
3. Select and drag  **Move** to drag all of the selected tiles to a new location.

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

### Split tile space to insert new tile

When laying out a dashboard, you can split the space that a tile uses on the grid, and insert a second tile next to the first tile within the same space.

* The first tile is unaffected other than that it now uses half the width or height it used before you split the space.
* The second (new) tile uses the other half of that layout space.
* This is available only when you select a single tile that is big enough to split. It's not available when you select multiple tiles, or if the size of the selected tile is too small to split.

For example, let's select a tile and add another tile to its right, so that the two tiles share the space originally used by the first tile.

1. Select the tile.
2. Hover over the tile to see the  split controlsâleft, right, and bottomâto indicate where you split that space and insert a new tile.

   ![Split a dashboard tile to insert another tile within the same space](https://dt-cdn.net/images/split-tiles-01-1515-c796df2c96.png)
3. In this example, select the  control on the right. It opens a menu similar to the  menu you would otherwise use to add a tile to the dashboard.
4. Select the tile type you want to add.
5. Edit the definition of the new tile and close the edit panel to see the changed layout.

   * The original tile is unchanged except that it now uses only the left half of the space it used before.
   * The new tile uses the right half of that space.
   * You can still adjust the tile sizes and positions manually.

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