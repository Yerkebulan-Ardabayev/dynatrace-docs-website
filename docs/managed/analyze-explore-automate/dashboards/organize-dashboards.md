---
title: Organize dashboards
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/organize-dashboards
---

# Organize dashboards

# Organize dashboards

* How-to guide
* 4-min read
* Updated on Oct 05, 2026

To keep the **Dashboards** list manageable and find the dashboards you need, follow the steps below. Every step is optional, so perform only the ones you need.

[![Step 1 optional](https://dt-cdn.net/images/dotted-step-1-c1b92a267e.svg "Step 1 optional")

**Filter the Dashboards table**](/managed/analyze-explore-automate/dashboards/organize-dashboards#filter "Filter the Dashboards table, mark favorites, add tags, hide dashboards you don't need, and find little-used dashboards to clean up by popularity.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Favorite dashboards**](/managed/analyze-explore-automate/dashboards/organize-dashboards#favorite "Filter the Dashboards table, mark favorites, add tags, hide dashboards you don't need, and find little-used dashboards to clean up by popularity.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Tag dashboards**](/managed/analyze-explore-automate/dashboards/organize-dashboards#tag "Filter the Dashboards table, mark favorites, add tags, hide dashboards you don't need, and find little-used dashboards to clean up by popularity.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Hide dashboards**](/managed/analyze-explore-automate/dashboards/organize-dashboards#hide "Filter the Dashboards table, mark favorites, add tags, hide dashboards you don't need, and find little-used dashboards to clean up by popularity.")[![Step 5 optional](https://dt-cdn.net/images/dotted-step-5-52040ae237.svg "Step 5 optional")

**Clean up little-used dashboards**](/managed/analyze-explore-automate/dashboards/organize-dashboards#popularity "Filter the Dashboards table, mark favorites, add tags, hide dashboards you don't need, and find little-used dashboards to clean up by popularity.")

## Step 1 optional Filter the Dashboards table

Depending on how many users you have and how many dashboards they create, the **Dashboards** page can list a long table of dashboards. Filter the table to show only the dashboards you need.

1. Go to **Dashboards**.
2. Set one or more filters using either method:

   * In the collapsible pane to the left of the table, select a value for a filter such as **Ownership** or **Favorite**. Your selection adds the equivalent filter to the filter bar above the table and applies it.
   * In the filter bar above the table, select a filter, and then enter or select the filter value. Use this method for filter values that you need to enter.

   For example, to list only your own dashboards, select `Mine` under **Ownership** in the left pane, or select `Ownership: Mine` on the **Filter by** line.

   You can apply the following filters:

   * **Name**: Enter any part of the dashboard name.
   * **Ownership**: Filters by ownership of the dashboard.

     + `Mine`: All dashboards that you've created.
     + `Shared with me`: All dashboards created by other users who have granted you read or edit permissions to their dashboards.
   * **Favorite**: Lists only your [favorite](#favorite) dashboards.
   * **Owner**: Filters by the name or user ID of the owner.
   * **Tag**: Filters by [dashboard tag](#tag).
   * **Hidden**: Set to `Yes` to display your [hidden](#hide) dashboards.
   * **Preset**: Lists only [preset dashboards](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.").

   If you set more than one filter, the table shows only the dashboards that match all filters.

To filter the content of a dashboard rather than the list of dashboards, see [Add dynamic filters to a dashboard](/managed/analyze-explore-automate/dashboards/add-dynamic-filters-to-a-dashboard "Add dynamic filters to a dashboard, such as operating system, tag key, or custom dimension filters, and then use the filter bar to filter all tiles on it.").

## Step 2 optional Favorite dashboards

By default, the **Dashboards** table sorts by the **Favorite** column, so your favorite dashboards appear at the top, followed by the other dashboards you have permission to display.

1. Favorite or unfavorite dashboards using either method:

   * To favorite or unfavorite the dashboard you're viewing, select the star in the upper-right corner of the dashboard. The star toggles favoriting on and off.

     ![Favoriting the current dashboard](https://dt-cdn.net/images/favorite-current-dashboard-169-caf101b927.png)

     Favoriting the current dashboard
   * To favorite or unfavorite several dashboards, go to **Dashboards** and select the star in the **Favorite** column for each dashboard.
2. To list only your favorite dashboards, go to **Dashboards** and select `Yes` under **Favorite** in the left pane, or select `Favorite: Yes` on the **Filter by** line.

## Step 3 optional Tag dashboards

Use tags to organize your dashboards into groups.

1. Display the dashboard.
2. Select **Edit**.

   If you don't see an **Edit** option, you don't have permission to edit that dashboard.
3. Under the name of the dashboard, select **Add tag**. Enter the tag, select it in the list, and then select **Add**.

   Repeat this step to add more tags to the dashboard.
4. Select **Done** to save your changes. You can now filter the **Dashboards** table by **Tag**.

## Step 4 optional Hide dashboards

1. To hide a dashboard, go to **Dashboards** and select **More** (**…**) > **Hide** for the dashboard you want to hide.
2. To unhide a dashboard:

   1. Go to **Dashboards**.
   2. Filter the table by `Hidden: Yes` to display your hidden dashboards.
   3. Select **More** (**…**) > **Unhide** for the dashboard you want to unhide.

## Step 5 optional Clean up little-used dashboards

The **Popularity** column of the **Dashboards** table shows which dashboards users viewed most over the last 30 days. Each dashboard gets a popularity score between 1 (least popular) and 10 (most popular).

![Dashboards table sorted by the Popularity column, showing a popularity score for each dashboard](https://dt-cdn.net/images/relnotes-232-dashboard-popularity-347-ec0f08449a.png)

Dashboards table sorted by the Popularity column, showing a popularity score for each dashboard

1. Go to **Dashboards** and sort the table by the **Popularity** column.

   The table lists all dashboards you're permitted to view or edit. Popular dashboards are ones you might want to use, and underused dashboards are candidates for cleanup.
2. To delete an underused dashboard, select **More** (**…**) > **Delete** for that dashboard, and then confirm the deletion.

   If you don't see a **Delete** option, you don't have permission to delete that dashboard.

## What's next

* To set a default management zone for a dashboard, see [How dashboards scope and refresh data](/managed/analyze-explore-automate/dashboards/how-dashboards-scope-and-refresh-data "Learn how timeframe, management zone, and dynamic filter settings decide which data dashboard tiles show, and how often each tile refreshes.").
* To filter a dashboard by a generic tag, see [Add dynamic filters to a dashboard](/managed/analyze-explore-automate/dashboards/add-dynamic-filters-to-a-dashboard "Add dynamic filters to a dashboard, such as operating system, tag key, or custom dimension filters, and then use the filter bar to filter all tiles on it.").
* To give other users access to a dashboard, see [Share a dashboard](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.").

## Related topics

* [Dashboards API](/managed/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")