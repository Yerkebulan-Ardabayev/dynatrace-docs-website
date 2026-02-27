---
title: Global Dynatrace dashboard settings
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-settings
scraped: 2026-02-27T21:28:44.980421
---

# Global Dynatrace dashboard settings

# Global Dynatrace dashboard settings

* How-to guide
* 2-min read
* Published Mar 05, 2021

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

This page refers to classic dashboards created using the ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** functionality integrated with Dynatrace Classic.

* If you're already using the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") for related documentation.
* If you're still using classic dashboards, we encourage you to [upgrade your dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") and benefit from all the latest dashboarding possibilities made available by the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** app in the latest Dynatrace.

Use the **Global dashboard settings** page to configure dashboard global settings and global settings for dashboard sharing and preset dashboards.

## General settings

### Allow anonymous access

With public sharing, even users who don't have access to the related Dynatrace environment or any Dynatrace access at all can view (but not change) your dashboard.

1. Go to **Settings** and select **Dashboards** > **General settings**.
2. Turn **Allow anonymous access** on or off to determine at the global (account) level whether dashboards can be shared publicly.
3. Select **Save changes**.

### Home dashboards

You can assign a preset dashboard as the home dashboard for any user group. The selected dashboard will become that group's default landing page.

1. Go to **Settings** and select **Dashboards** > **General settings**.
2. Select **Configure home dashboard**.
3. Select **User group**.
4. Select a preset dashboard from the **Home dashboard** list.  
   If your dashboard isn't listed, make sure it's a [preset dashboard](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-preset "Learn about out-of-the-box Dynatrace dashboards and how to create your own preset dashboards.").
5. Select **Save changes**.

## Preset settings

Use this page to configure preset dashboard settings at the global level.

Preset dashboards are visible to all users by default. You can use the global settings to turn them off entirely or to limit visibility to certain user groups.

### Enable presets

Use **Enable preset** to turn preset dashboards on or off globally. If you turn it off, any dashboard marked as a preset will no longer be displayed on other users' **Dashboard** tables.

### Limit preset visibility

Use preset rules to ensure that specific preset dashboards are visible only to specific user groups and not to all users in the environment.

1. Go to **Settings** and select **Dashboards** > **Preset settings**.
2. In the **Limit preset visibility** section, **Add item**.

   * Set **Preset dashboard** to the preset dashboard for which you want to manage group access.
   * Set **User group** to the user group that should have access to the selected preset dashboard.
3. Select **Save changes**.

For more on preset dashboards, see [Preset dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-preset "Learn about out-of-the-box Dynatrace dashboards and how to create your own preset dashboards.").

## Allowed URL pattern rules

To add an image to your dashboard via URL, you first need to add a URL rule to the allowlist.

1. Go to **Settings** and select **Dashboards** > **Allowed URL pattern rules**.
2. Select **Add item**.
3. Set **Rule**, which specifies how to process this allowlist entry.

   * **Starts with**âallow any image whose URL starts with the contents of **Pattern**.
   * **Exact**âallow the specific image whose URL matches the contents of **Pattern** exactly.
4. Set **Pattern**:

   * To specify a URL start, enter enough of the URL to make sure any matching image URLs will be suitable for your dashboards.  
     Example: enter `https://example.com/images/` to allow any image whose URL starts with `https://example.com/images/`, such as  
     `https://example.com/images/image-x.jpg` and
     `https://example.com/images/my-picture.svg`
   * To specify an exact URL, enter the entire URL of the image you want to allow.  
     Example: enter `https://example.com/images/my-image-file-name.jpg` to allow only that image
5. Select **Save changes** to add the specified rule to the allowlist.

Then you can add a dashboard image via URL.

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select the name of a dashboard to display that dashboard.
3. Select **Edit** in the upper-right corner of the dashboard. The dashboard opens in edit mode.

   * If you don't see an **Edit** option, you don't have permission to edit that dashboard.
4. Drag an **Image** tile into position.
5. On the **Image** panel, select the **Add image URL** tab.
6. Enter the URL of the image file you want to display in the tile. It needs to match one of the rules on the allowlist.
7. Size and position the tile as needed.