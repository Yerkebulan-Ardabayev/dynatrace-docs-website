---
title: Dynatrace dashboard timeframe and management zone settings
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe
scraped: 2026-02-22T21:17:17.080630
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