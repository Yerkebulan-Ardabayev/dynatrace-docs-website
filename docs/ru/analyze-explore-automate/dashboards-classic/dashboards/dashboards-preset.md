---
title: Preset Dynatrace dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-preset
scraped: 2026-02-22T21:28:13.503196
---

# Preset Dynatrace dashboards

# Preset Dynatrace dashboards

* How-to guide
* 4-min read
* Published Feb 04, 2021

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

Preset dashboards are visible to all users by default.

* On the **Dashboards** page, the name of each preset dashboard is followed by the `Preset` tag.
* To display only preset dashboards, set the `Preset` filter to `Yes`.

Dynatrace offers several domain-specific out-of-the-box preset dashboards. Use them as inspiration for your own dashboards and clone them to create your own customized versions.

* You can create your own preset dashboards.
* You can set any preset dashboard as the home dashboard for a user group.

## Manage global settings

Preset dashboards are visible to all users by default. You can use the global settings to turn them off entirely or to limit visibility to certain user groups.

### Enable presets

Use **Enable presets** to turn preset dashboards on or off globally. If you turn it off, dashboards marked as presets will no longer appear on **Dashboard** tables for any users.

### Limit preset visibility

Use preset rules to ensure that specific preset dashboards are visible only to specific user groups and not to all users in the environment.

1. Go to **Settings** and select **Dashboards** > **Preset settings**.
2. In the **Limit preset visibility** section, **Add item**.

   * Set **Preset dashboard** to the preset dashboard for which you want to manage group access.
   * Set **User group** to the user group that should have access to the selected preset dashboard.
3. Select **Save changes**.

## List all preset dashboards

To list all preset dashboards

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Set a filter using one of these methods:

   * Under **Preset** in the left column, select `Yes`
   * On the **Filter by** line, select `Preset: Yes`
3. Select the name of any preset dashboard to display it.

## Out-of-the-box preset dashboards

You can't edit out-of-the-box preset dashboards, but you can clone them and edit the clones.

### To clone an out-of-the-box preset dashboard

Use **Clone** to create your personal, editable copy of a dashboard with `-cloned` appended to the dashboard name.

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Find the out-of-the-box preset dashboard you want to clone.
3. Use one of these methods to clone the dashboard:

   * Select **More** (**â¦**) > **Clone** for the dashboard you want to clone.
   * Open the dashboard, select **More** (**â¦**) in the upper-right of the dashboard, and select **Clone**.

To clone a dashboard you are currently displaying, select **More** (**â¦**) > **Clone**.

### To inspect and edit the clone

Now that you have a copy of the dashboard, you can experiment with it.

1. Select **Edit** to inspect and edit the dashboard components.

   * **Name**âSelect  after the dashboard name to personalize the name of your clone.
   * **Tags**âUnder the dashboard name, add and delete tags as needed.
   * **Markdown** and **Header** tilesâSelect them to see how to use text and headers on your dashboard to label and explain elements of the dashboard.
   * Other tilesâselect tiles to see the settings in the tile-specific pane on the right. See [Available tiles](/docs/analyze-explore-automate/dashboards-classic/charts-and-tiles/available-tiles "Find out how to configure your dashboard to track business-critical user-actions and conversion goals.") for tile-specific help.
2. Select **Done** to save any changes and display the working dashboard.
3. Try drilldowns from the tiles to see where they go.

   * Open a tile's menu to see menu options.
   * Select tile elements to see available actions.

## Create a preset dashboard

You can create and modify your own preset dashboards.

* Preset dashboards are automatically shared to all users
* Preset dashboards appear on the **Dashboards** table for all users

You need one of the following permissions:

* Environment-wide permission **Change monitoring settings**
* Role `ALLOW environment:roles:manage-settings`

To designate a dashboard as a preset dashboard

1. [Create a dashboard](/docs/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.") or display an existing dashboard for which you have editing rights.
2. Select **Edit**.
3. Switch to the **Settings** tab and then select **Configure more**.
4. On the **Manage access** tab, turn on **Publish as preset**.
5. **Save changes**.

To verify the change

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Filter by `Preset: Yes`.
3. Make sure the dashboard is displayed in the table.  
   Also, each preset dashboard has a `Preset` tag after its name in the table.

## Assign a home dashboard

If you have admin privileges, you can assign a preset dashboard as the home dashboard for a user group. The selected dashboard will become that group's default landing page.

1. Go to **Settings** > **Dashboards** > **General settings**.
2. Select **Configure home dashboard**.
3. Set **User group** to the group whose home dashboard you want to set.
4. Set **Home dashboard** to one of the preset dashboards on the list.  
   If your dashboard isn't listed, make sure it's set as a preset dashboard.
5. Select **Save changes**.