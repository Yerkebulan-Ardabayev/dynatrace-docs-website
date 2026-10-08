---
title: Dashboard settings
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/dashboard-settings
---

# Dashboard settings

# Dashboard settings

* Reference
* 3-min read
* Updated on Oct 05, 2026

Dashboards have global settings that apply to your whole environment and settings that apply to one dashboard, grouped here by the page where you find them.

## General settings

Go to **Settings** > **Dashboards** > **General settings**.

| Name | Type | Description |
| --- | --- | --- |
| **Allow anonymous access** | Switch | Global (account-level) setting that determines whether dashboards can be shared publicly. When off, anonymous access to a dashboard report returns a `403` error. See [Share a dashboard](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") |
| **Configure home dashboard** | User group and preset dashboard | Assigns a preset dashboard as the default landing page for a user group, chosen from the preset dashboards. See [Publish a preset dashboard](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.") |

## Preset settings

Go to **Settings** > **Dashboards** > **Preset settings**.

| Name | Type | Description |
| --- | --- | --- |
| **Enable presets** | Switch | Turns preset dashboards on or off globally. When off, dashboards marked as presets no longer appear in dashboard tables for any user. Default: on. See [Publish a preset dashboard](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.") |
| **Limit preset visibility** | List of rules, each with **Preset dashboard** and **User group** | Makes a preset dashboard visible only to the selected user group. Default: no rules, so presets are visible to all users. See [Publish a preset dashboard](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.") |

## Allowed URL pattern rules

Go to **Settings** > **Dashboards** > **Allowed URL pattern rules**. An **Image** tile can display an image by URL only when the URL matches a rule on this allowlist.

| Name | Type | Description |
| --- | --- | --- |
| **Rule** | `Starts with` or `Exact` | How the entry matches: `Starts with` allows any image URL that starts with **Pattern**, and `Exact` allows only the image URL that matches **Pattern** exactly |
| **Pattern** | URL string | URL start or full image URL to match, such as `https://example.com/images/` |

## Dashboard settings tab

Edit the dashboard and, on the **Edit dashboard** pane, select the **Settings** tab. See [Create a dashboard](/managed/analyze-explore-automate/dashboards/create-a-dashboard "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.").

| Name | Type | Description |
| --- | --- | --- |
| **Default timeframe** | Switch and timeframe | Timeframe selected every time the dashboard opens, overriding the global timeframe and also used for shared links. See [How dashboards scope and refresh data](/managed/analyze-explore-automate/dashboards/how-dashboards-scope-and-refresh-data "Learn how timeframe, management zone, and dynamic filter settings decide which data dashboard tiles show, and how often each tile refreshes.") |
| **Default management zone** | Switch and management zone | Management zone selected every time the dashboard opens, overriding the global management zone and also used for shared links. See [How dashboards scope and refresh data](/managed/analyze-explore-automate/dashboards/how-dashboards-scope-and-refresh-data "Learn how timeframe, management zone, and dynamic filter settings decide which data dashboard tiles show, and how often each tile refreshes.") |
| **Enable reports** | Switch | Lets users with access to the dashboard subscribe to weekly or monthly reports and view them without signing in. Default: off. See [Share a dashboard](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") |
| Title size | `small`, `medium`, or `large` | Title size for all tiles on the dashboard |
| **Consistent entity colors** | Switch | Shows the same entity in the same color across tiles created with Data Explorer |

## Configure more tabs

On the dashboard **Settings** tab, select **Configure more** to open **Dashboard settings**.

| Name | Type | Description |
| --- | --- | --- |
| **Manage access** > **Share dashboard** | Switch, with users, user groups, and `Edit` or `View` permission | Shares the dashboard with selected users, user groups, or anyone who has the link. See [Share a dashboard](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") |
| **Manage access** > **Publish as preset** | Switch | Publishes the dashboard as a preset dashboard. See [Publish a preset dashboard](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.") |
| **Manage access** > **Anonymous access** | List of links, each with a management zone | View-only links for anonymous access, which require **Share dashboard** and **Allow anonymous access**. Without a default timeframe and management zone, a link uses the last two hours and the **All** management zone. Default: management zone `default` for a new link. See [Share a dashboard](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") |
| **Dynamic filters** | List of filters | Filters that appear in the dashboard filter bar. See [Add dynamic filters to a dashboard](/managed/analyze-explore-automate/dashboards/add-dynamic-filters-to-a-dashboard "Add dynamic filters to a dashboard, such as operating system, tag key, or custom dimension filters, and then use the filter bar to filter all tiles on it.") |
| **Dashboard JSON** | JSON | JSON definition of the dashboard, which you can edit directly, download, or upload. See [Create a dashboard](/managed/analyze-explore-automate/dashboards/create-a-dashboard "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.") |