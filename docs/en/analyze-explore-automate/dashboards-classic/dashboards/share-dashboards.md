---
title: Share Dynatrace dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/share-dashboards
scraped: 2026-02-16T21:26:12.377218
---

# Share Dynatrace dashboards

# Share Dynatrace dashboards

* How-to guide
* 7-min read
* Published Jul 19, 2017

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

You can share your dashboards with anyone, even if they don't have their own accounts within the same Dynatrace environment.

Limitations

* It is not possible to use an anonymous dashboard link to access Grail data.

## Quick start

To share a dashboard

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.
4. Turn on **Share dashboard** and specify the sharing details as described below.

   * [Grant access to a specific user](#access-user)
   * [Grant access to a specific group](#access-group)
   * [Grant access to any user with the link](#access-all-authenticated)
   * [Grant anonymous access](#access-anonymous)

   You can combine these options. For example, you might grant `Edit` access to dashboard developers and grant `View` access to other users or groups in your organization.
5. Select **Save changes**.

To stop sharing a dashboard

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. In the pop-up, turn off **Share this dashboard**.

Any share settings you made previously are preserved and will be reactivated if you turn **Share this dashboard** back on.

## Configure global dashboard sharing settings

With public sharing, even users who don't have access to the related Dynatrace environment or any Dynatrace access at all can view (but not change) your dashboard.

1. Go to **Settings** and select **Dashboards** > **General settings**.
2. Turn **Allow anonymous access** on or off to determine at the global (account) level whether dashboards can be shared publicly.
3. Select **Save changes**.

## Grant access to a specific user

To grant access to an authenticated Dynatrace user

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

1. Turn on **Share dashboard**.
2. Under **Access permissions**, select **Grant access permission**.
3. From the **Who to grant access to** list, select **Specific user**.
4. From the **User** list, select the user to whom you want to grant access.
5. From the **What they should be able to do with the dashboard**, select `Edit` or `View`.
6. Select **Save changes**.  
   The specified user is added to the list under **Grant access permission**.

   * When **Share dashboard** is turned on, the selected user has access to your dashboard as you specified above (`Edit` or `View`).
   * To change the access type (`Edit` or `View`), select **Details** for that user and change **What they should be able to do with the dashboard**.
   * To revoke this access, select **Delete** for that user.

   Users assigned the `Edit` permission can edit shared dashboards. Be careful about sharing `Edit` permission:

   * Changes someone else makes to a dashboard will affect all users who share the dashboard.
   * When two users edit the same dashboard at the same time, the most recently saved changes take precedence over earlier changes. If you attempt to edit a dashboard that is currently being edited by another user, you'll see a notification.

## Grant access to a specific group

To grant access to everyone in a Dynatrace user group

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

1. Turn on **Share dashboard**.
2. Under **Access permissions**, select **Grant access permission**.
3. Under **Who to grant access to**, select **Specific group**.
4. Under **User group**, select the group to whom you want to grant access to your dashboard.
5. From the **What they should be able to do with the dashboard**, select `Edit` or `View`.
6. Select **Save changes**.  
   The specified user group is added to the list under **Grant access permission**.

   * When **Share dashboard** is turned on, everyone in the selected user group has access to your dashboard as you specified above (`Edit` or `View`).
   * To change the access type (`Edit` or `View`), select **Details** for that user group and change **What they should be able to do with the dashboard**.
   * To revoke this access, select **Delete** for that user group.

   Users assigned the `Edit` permission can edit shared dashboards. Be careful about sharing `Edit` permission:

   * Changes someone else makes to a dashboard will affect all users who share the dashboard.
   * When two users edit the same dashboard at the same time, the most recently saved changes take precedence over earlier changes. If you attempt to edit a dashboard that is currently being edited by another user, you'll see a notification.

## Grant access to any user with the link

To grant access to any authenticated Dynatrace user who has a copy of the shared link

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

1. Turn on **Share dashboard**.
2. Under **Access permissions**, select **Grant access permission**.
3. Under **Who to grant access to**, select **Any user with the link**.
4. Select **Copy link** to get the link you need to share the dashboard.
5. Select **Save changes**.  
   **Any user with the link has permission** is added to the list of permissions under the **Grant access permission** button.
6. Share the link (address) with users who should view the dashboard.

   * When **Share dashboard** is turned on, any user who has a copy of the link can use it to view the dashboard.
   * The dashboard will not be visible on the user's **Dashboards** table in Dynatrace until they use the link for the first time.
   * To revoke this access, select **Delete** in the **Any user with the link has permission** row.

## Grant anonymous access

You can grant **anonymous access** to your dashboard based on distributable links to the dashboard:

* Anonymous access grants view permission only
* You can specify links per management zone
* To enable or disable anonymous access for your environment, see **Settings** > **Dashboards** > **General settings**.

* It is not possible to use an anonymous dashboard link to access Grail data.

### Create a shareable link to your dashboard

To create a shareable link to your dashboard that can be used by anyone (with no authentication)

1. Display the dashboard you want to share.

   * To display a dashboard, go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and select the name of the dashboard.
2. Select **More** (**â¦**) > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.

1. Turn on **Share dashboard**.
2. Under **Anonymous access**, select **Add anonymous access link**.
3. From **Management Zone for anonymous access link**, select a management zone or leave it set to `default`.

   * Which management zones are available depends on your permissions when you create the link.
4. Select **Save changes**.  
   A shareable link is added to the list displayed under **Add anonymous access link**.
5. Expand the list entry (**Details**) and select **Copy link** to copy the link to your clipboard. Paste the link to any message you send referring to the dashboard.

Repeat this procedure to create multiple anonymous links.

* If a [default timeframe and management zone](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe#default "Learn about Dynatrace dashboard timeframe and management zone settings.") are set for the dashboard, the link is shared with those settings. Otherwise, the link is shared with the timeframe of **last 2 hours** and **All** management zone.
* If the dashboard is shared with the **All** management zone, a recipient of the link has access to the management zones that you had access to when you created the link.

### Revoke a shareable link to your dashboard

To revoke a shareable link to your dashboard that can be used by anyone (with no authentication)

1. Under **Anonymous access**, locate the link.
2. Select **X** in the **Delete** column for that row and then select **Save changes**.

### Caution on shared links

A shared link has the creator's permissions, not the recipient's permissions.

* Anyone using a link you create can see everything you see through that link (such as management zones).
* If you lose permissions, people using your link also lose those permissions.

To maintain stricter control over who can see your dashboard, use the authenticated options per user, group, or environment.