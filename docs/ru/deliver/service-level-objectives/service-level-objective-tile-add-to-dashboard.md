---
title: Add a service-level objective (SLO) tile to a dashboard
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-tile-add-to-dashboard
scraped: 2026-02-15T21:24:11.149444
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