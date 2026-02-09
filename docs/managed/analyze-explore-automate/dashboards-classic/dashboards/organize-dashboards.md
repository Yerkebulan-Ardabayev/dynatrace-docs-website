---
title: "Organize Dynatrace dashboards"
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards-classic/dashboards/organize-dashboards
updated: 2026-02-09
---

# Organize Dynatrace dashboards

# Organize Dynatrace dashboards

* How-to guide
* 3-min read
* Published Jan 18, 2019

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

When you have a lot of dashboards, you need to manage them.

## Filters on the dashboards table

Depending on how many Dynatrace users you have and how many dashboards they create, the **Dashboards** page (go to **Dashboards**) may present you with a long table of dashboards. You need to know how to filter that table.

There are two ways to set filters on the **Dashboards** table:

* The collapsible pane to the left of the table has filters such as **Ownership** and **Favorite**. Any selection you make for one of those filters adds the equivalent filter to the filter bar above the table and applies the filter.
* You can add filters directly to the filter bar above the table: in the filter bar, select a filter, and then type or select the filter value. You need to use this method for filter values that require typing.

#### List my dashboards

To list just your own dashboards

1. Go to **Dashboards**.
2. Set a filter using one of these methods:

   * Under **Ownership** in the left column, select `Mine`
   * On the **Filter by** line, select `Ownership: Mine`

#### All dashboard table filters

You can apply the following filters to the **Dashboards** table:

* **Name**: Type any part of the dashboard name and press enter
* **Ownership**: Filters by ownership of the dashboard

  + `Mine`: All dashboards that you've created
  + `Shared with me`: All dashboards created by other users who have granted you read or edit permissions to their dashboards
* **Favorite**: Lists just the [favorited](#favorite) dashboards
* **Owner**: Filters by the name or user ID of the owner
* **Tag**: Filters by [dashboard tag](#tag)
* **Hidden**: Set to `Yes` to display your hidden dashboards
* **Preset**: Whether to list only [preset dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboards-preset "Learn about out-of-the-box Dynatrace dashboards and how to create your own preset dashboards.")

If you set more than one filter, only dashboards that match all of the filters are shown.

## Favorites

Favorited dashboards are sorted to the top of the **Dashboards** table by default, followed by the rest of the dashboards in the table.

### Favorite a dashboard

To favorite the dashboard you are viewing, select the star in the upper-right corner of the dashboard. The star toggles favoriting on and off.

![Favoriting the current dashboard](https://dt-cdn.net/images/favorite-current-dashboard-169-caf101b927.png)

To favorite multiple dashboards

1. Go to **Dashboards**.  
   By default, the table is sorted by the **Favorite** column, so your favorites should be listed at the top of the table.
2. In the **Favorite** column, select the star for each dashboard you want to favorite.

### Unfavorite a dashboard

To unfavorite the dashboard you are viewing, select the star in the upper-right corner of the dashboard. The star toggles favoriting on and off.

![Unfavoriting the current dashboard](https://dt-cdn.net/images/unfavorite-current-dashboard-169-97f319d05f.png)

To unfavorite multiple dashboards

1. Go to **Dashboards**.  
   By default, the table is sorted by the **Favorite** column, so your favorites should be listed at the top of the table.
2. Optional To list only your favorites, filter the table by `Favorite: Yes`.
3. In the **Favorite** column, select the star for each dashboard you want to unfavorite.

### List your favorite dashboards

1. Go to **Dashboards**.  
   By default, the table is sorted by the **Favorite** column, so your favorites should be listed at the top of the table, followed by the other dashboards you have permission to display.
2. Optional To list only your favorites, set a filter using one of these methods:

   * Under **Favorite** in the left column, select `Yes`
   * On the **Filter by** line, select `Favorite: Yes`

## Popularity

The **Popularity** column of the **Dashboards** table shows you which dashboards have been most viewed over the last 30 days. Each dashboard is given a popularity score between 1 (least popular) and 10 (most popular).

![Dashboard popularity](https://dt-cdn.net/images/relnotes-232-dashboard-popularity-347-ec0f08449a.png)

* If you're a Dynatrace user, sort by **Popularity** to find popular dashboards that you might want to use.
* If you manage a Dynatrace deployment, sort by **Popularity** to identify underused dashboards that could be candidates for cleanup.

## Tags

You can use tags to organize your dashboards into groups.

To apply dashboard tags

1. Display the dashboard.
2. Select **Edit**.  
   If you don't see an **Edit** option, you don't have permission to edit that dashboard.
3. Select **Add tag** under the name of the dashboard, type and select the tag, and then select **Add**.  
   Repeat this step as needed to add additional tags to this dashboard.
4. Select **Done** to save your changes.

You can filter the **Dashboards** list by **Tag**.

### Generic tag filter

1. Go to the **Dynamic filters** page of your dashboard settings.

   Show me

   1. Select **Edit** in the upper-right corner of the dashboard.

      If you don't see an **Edit** button, you don't have edit rights for the selected dashboard.
   2. Select the **Settings** tab.
   3. Select **Configure more**.
   4. Select **Dynamic filters**.

      ![The "Dynamic filters" tab of a dashboard](https://dt-cdn.net/images/empty-dynamic-filters-tab-1072-a5cc3d3c6e.png)
2. Select **Add filter**.
3. Set **Filter criteria** to `Generic tag key`.
4. Set **Display name** to a unique display name that identifies this generic filter (for example, `Application name`).
5. Set **Tag key** (for example, `appName`).
6. Set **Get suggestions from** to define where to get tag suggestions (for example, `Host`).
7. Under **Entity types affected by tag**, select **Add entity type** to add an entity type affected by this tag.

   You can do this multiple times.
8. Select **Save changes**.
9. Display the dashboard.
10. When you set a filter on the dashboard, you can apply the same type of filter more than once under the same generic tag.

## Management zones

[Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") are used to partition monitoring data based on team ownership and responsibility. Dashboard content is automatically filtered whenever a management zone is selected.

You can set a default timeframe and management zone for each dashboard; these are selected every time you open the dashboard. They're also used when you [share](/managed/analyze-explore-automate/dashboards-classic/dashboards/share-dashboards "Learn how to share your Dynatrace dashboards with others.") the dashboard.

To configure the default timeframe and management zone, edit the dashboard, switch to the **Settings** tab, and configure either or both settings:

* **Default timeframe**: turn it on and select a timeframe for the dashboard.
* **Default management zone**: turn it on and select a management zone for the dashboard.

Team members who view a zone-specific dashboard without having the required management zone permissions are presented with a dashboard that has no content. They must select a management zone that they have permission to view before data is displayed on the dashboard.

For more on dashboards and management zones, see [Dashboard timeframe and management zone](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.").

## More dashboard management procedures

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

Hide a dashboard

1. Go to **Dashboards**.
2. In the table of dashboards, select **More** (**â¦**) > **Hide** for the dashboard you want to hide.

Unhide a dashboard

1. Go to **Dashboards**.
2. Filter the table by `Hidden: Yes` to display all of your hidden dashboards.
3. In the table of dashboards, select **More** (**â¦**) > **Unhide** for the dashboard you want to unhide.

Delete a dashboard

1. Go to **Dashboards**.
2. In the table of dashboards, select **More** (**â¦**) > **Delete** for the dashboard you want to delete.

   * If you don't see a **Delete** option, you don't have permission to delete that dashboard.
3. Confirm the deletion to remove the dashboard.

## Related topics

* [Dashboards API](/managed/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")
