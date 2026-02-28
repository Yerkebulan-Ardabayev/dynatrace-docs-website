---
title: Dynatrace dashboard timeframe and management zone settings
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe
scraped: 2026-02-28T21:15:24.237896
---

# Dynatrace dashboard timeframe and management zone settings

# Dynatrace dashboard timeframe and management zone settings

* How-to guide
* 2-min read
* Published Jul 19, 2017

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

This page refers to classic dashboards created using the ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** functionality integrated with Dynatrace Classic.

* If you're already using the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") for related documentation.
* If you're still using classic dashboards, we encourage you to [upgrade your dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") and benefit from all the latest dashboarding possibilities made available by the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** app in the latest Dynatrace.

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