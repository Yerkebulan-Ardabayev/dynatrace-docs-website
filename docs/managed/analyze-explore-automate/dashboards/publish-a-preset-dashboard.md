---
title: Publish a preset dashboard
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard
---

# Publish a preset dashboard

# Publish a preset dashboard

* How-to guide
* 2-min read
* Updated on Oct 05, 2026

To make a dashboard available to all users as a preset dashboard, follow the steps below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Enable presets**](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard#global "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Publish the dashboard as a preset**](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard#publish "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Verify the preset dashboard**](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard#verify "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Limit preset visibility**](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard#limit-visibility "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.")[![Step 5 optional](https://dt-cdn.net/images/dotted-step-5-52040ae237.svg "Step 5 optional")

**Assign a home dashboard**](/managed/analyze-explore-automate/dashboards/publish-a-preset-dashboard#home-dashboard "Publish a dashboard as a preset so that it's shared with all users, then limit its visibility or assign it as a home dashboard for a user group.")

Dynatrace automatically shares a preset dashboard with all users, and it appears in the **Dashboards** table for all users. To customize one of the built-in preset dashboards instead, clone it as described in [Create a dashboard](/managed/analyze-explore-automate/dashboards/create-a-dashboard "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.").

## Step 1 Enable presets

Preset dashboards are visible to all users by default. If you turn off presets globally, dashboards marked as presets no longer appear in the **Dashboards** table for any users.

1. Go to **Settings** and select **Dashboards** > **Preset settings**.
2. Turn on **Enable presets**.

## Step 2 Publish the dashboard as a preset

To publish a preset dashboard, you need the environment-wide **Change monitoring settings** permission.

1. [Create a dashboard](/managed/analyze-explore-automate/dashboards/create-a-dashboard "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF."), or open an existing dashboard for which you have editing rights.
2. Select **Edit**.
3. Switch to the **Settings** tab, and then select **Configure more**.
4. On the **Manage access** tab, turn on **Publish as preset**.
5. Select **Save changes**.

## Step 3 Verify the preset dashboard

1. Go to **Dashboards**.
2. Filter the table by preset, using one of these methods:

   * Under **Preset** in the left column, select `Yes`.
   * On the **Filter by** line, select `Preset: Yes`.
3. Check that your dashboard appears in the table.

Each preset dashboard shows a `Preset` tag after its name in the table.

## Step 4 optional Limit preset visibility

Use preset rules to make a specific preset dashboard visible only to specific user groups instead of all users in the environment.

1. Go to **Settings** and select **Dashboards** > **Preset settings**.
2. In the **Limit preset visibility** section, select **Add item**.

   * Set **Preset dashboard** to the preset dashboard for which you want to manage group access.
   * Set **User group** to the user group that should have access to the selected preset dashboard.
3. Select **Save changes**.

## Step 5 optional Assign a home dashboard

If you have admin privileges, you can assign a preset dashboard as the home dashboard for a user group. The selected dashboard becomes that group's default landing page.

1. Go to **Settings** and select **Dashboards** > **General settings**.
2. Select **Configure home dashboard**.
3. Set **User group** to the group whose home dashboard you want to set.
4. Set **Home dashboard** to one of the preset dashboards in the list.  
   If your dashboard isn't listed, check that you published it as a preset.
5. Select **Save changes**.

Members of the user group now see the preset dashboard as their landing page.

## What's next

* To see all global dashboard settings, see [Dashboard settings](/managed/analyze-explore-automate/dashboards/dashboard-settings "Look up every dashboard setting, from global sharing, preset, and image URL rules to the timeframe, report, and access options of a single dashboard.").
* To share a dashboard with specific users instead of all users, see [Share a dashboard](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.").