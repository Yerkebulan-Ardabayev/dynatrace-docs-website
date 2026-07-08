---
title: Timeframe selector
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/dynatrace-ui/ui-timeframe-selector
---

# Timeframe selector

# Timeframe selector

* Explanation
* 3-min read
* Updated on May 15, 2026

The timeframe selector lets you filter and analyze data by timeframes. You can use custom time values or presets.

## Presets

Presets are common, useful timeframe selections, such as `Last 2 hours` or `Today`.

## Custom timeframes

Custom timeframes consist of `from` and `to` values. To define a custom timeframe, enter the `from` and `to` values in the input fields and select **Apply**.

`From` and `to` can be either [absolute time](#absolute-time) or [relative time](#relative-time).

### Absolute time

Use the calendar to select one or more days. When you select inside the timeframe field, you can use the up `↑` and down `↓` arrow keys on your keyboard to increase and decrease the highlighted numbers.

The date and time format follows your Dynatrace user settings. The time precision depends on the data context and the app. Common time precisions are `hh:mm` (hour:minute) and `hh:mm:ss` (hour:minute:second).

### Relative time

Relative time is always calculated relative to `now`. It follows the format `-[number][unit]` for past dates, and `+[number][unit]` for future dates.

Supported units are `s` (seconds), `m` (minutes), `h` (hours), `d` (days), `w` (weeks), `M` (months), `q` (quarters), `y` (years).

The timeframe selector doesn't support combinations of different units (for example, `-1d3h30m`) or calculations with brackets (for example, `(now-1d)@d`).

| Example | Description |
| --- | --- |
| `-2h` | Exactly 2 hours ago |
| `-7d` | Exactly 7 days ago |
| `-1w` | Exactly 1 week ago |

The timeframe selector automatically simplifies the time format. For example, instead of writing `now-5m`, write `-5m`. The selector removes the `now` prefix.

### Rounded time

Rounded time expressions let you filter timeframes such as "today" (`@d`), "yesterday" (`-1d@d`), or "last week" (`-1w@w`). For example, `@d` to `now` filters for everything between 00:00:00 this morning and now.

The simplest form of rounded time is `@[unit]`. More complex variations are possible too. For example, you can combine rounded time with time offsets, such as `-[number][unit]@[unit]` and `+[number][unit]@[unit]`.

As with relative time, rounded time is relative to `now` and follows your Dynatrace user settings.

| Example | Description |
| --- | --- |
| `@d` | Beginning of today |
| `-2M@M` | Beginning of the month before last month |
| `@y` | Beginning of this year |

## Timeframe selector settings

The timeframe selector adapts to your Dynatrace user settings. These settings control the time zone and the regional date/time format.

### Time zone settings

The **Time zone settings** in the Dynatrace user settings control the time zone in the timeframe selector.

* **Specific time zone**: You can select a time zone in your Dynatrace user settings.
* **Use browser default**: Alternatively, choose **Time zone - use browser default**. The timeframe selector then uses your browser's time zone.

### Format settings

The **Region settings** in the Dynatrace user settings control the date and time format in the timeframe selector.

* **Date format**: The order and separators (for example, DD.MM.YYYY vs. MM/DD/YYYY) follow the standard for the selected region.
* **Time format**: The region also controls whether the timeframe selector uses a 12-hour clock or a 24-hour clock.

For example, **English - United States** renders dates and times as MM/DD/YYYY with a 12-hour clock, and **German - Germany** renders them as DD.MM.YYYY with a 24-hour clock.