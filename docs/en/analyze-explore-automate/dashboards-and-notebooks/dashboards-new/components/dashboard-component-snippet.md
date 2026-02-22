---
title: Add a snippet to a dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-snippet
scraped: 2026-02-22T21:08:59.839649
---

# Add a snippet to a dashboard

# Add a snippet to a dashboard

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Jul 08, 2022

Several data and code snippets are available out of the box. Use our predefined DQL or code snippets to quickly start your data analytics journey.

## Select a snippet

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

## Examples

### Fetch logs

1. In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, select  **Dashboard** to create a new dashboard.
2. In the upper-right of the dashboard, select  **Add** to open the add menu.

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)
3. In the menu, scroll down to the **Start with a snippet** section of the menu and select  **Fetch logs**.

That's it. You have created a dashboard with a DQL tile that fetches the 100 latest logs and displays them starting with the most recent.

![Example snippet: Fetch logs](https://dt-cdn.net/images/example-snippet-fetch-logs-1335-7f23a8343c.png)

The DQL behind your tile is the snippet you selected with  **Fetch logs**:

```
fetch logs



| sort timestamp desc



| limit 100
```

The DQL commands are run in order:

1. `fetch logs` gets the log data
2. `sort timestamp desc` sorts the data by timestamp in descending order
3. `limit 100` limits the results to the 100.

### Pie (Top 5 events by kind)

1. In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, select  **Dashboard** to create a new dashboard.
2. In the upper-right of the dashboard, select  **Add** to open the add menu.

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)
3. In the menu, scroll down to the **Start with a snippet** section of the menu and select  **Pie (Top 5 events by kind)**.

This one creates a tile based on the following DQL:

```
fetch events



| summarize `event count`=count(), by:{event.kind}



| limit 5
```

The results are displayed as a pie chart.

![Example snippet: Pie (Top 5 events by kind)](https://dt-cdn.net/images/example-snippet-pie-top-five-events-1004-a42b6a2b21.png)

## What's next

The list of available snippets is long and growing. Create a new dashboard and try them out.

When you find something interesting:

* Inspect it to see how it works
* See if you can tweak and adapt it to your own purposes