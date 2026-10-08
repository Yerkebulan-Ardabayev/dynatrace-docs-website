---
title: Share a dashboard
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/share-a-dashboard
---

# Share a dashboard

# Share a dashboard

* How-to guide
* 5-min read
* Updated on Oct 05, 2026

To give other people access to a dashboard, follow the steps below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Turn on sharing**](/managed/analyze-explore-automate/dashboards/share-a-dashboard#turn-on-sharing "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Grant access**](/managed/analyze-explore-automate/dashboards/share-a-dashboard#grant-access "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Save your changes**](/managed/analyze-explore-automate/dashboards/share-a-dashboard#save-changes "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Set up email reports**](/managed/analyze-explore-automate/dashboards/share-a-dashboard#email-reports "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.")

## Step 1 Turn on sharing

1. Go to **Dashboards** and select the name of the dashboard you want to share.
2. Select **More** > **Share** in the upper-right corner of the dashboard.
3. Select **Advanced settings** to open **Dashboard settings** to the **Manage access** tab.
4. Turn on **Share dashboard**.

## Step 2 Grant access

Grant access with one or more of the options below. You can combine them. For example, you might grant `Edit` access to dashboard developers and `View` access to other users or groups in your organization.

Be careful about granting `Edit` permission:

* Changes someone else makes to a dashboard affect all users who share the dashboard.
* When two users edit the same dashboard at the same time, the most recently saved changes take precedence. If you try to edit a dashboard that another user is currently editing, you see a notification.

### Grant access to a specific user

1. Under **Access permissions**, select **Grant access permission**.
2. From the **Who to grant access to** list, select **Specific user**.
3. From the **User** list, select the user.
4. From **What they should be able to do with the dashboard**, select `Edit` or `View`.

Dynatrace adds the user to the list under **Grant access permission**. To change the access level later, select **Details** for that user. To revoke access, select **Delete** for that user.

### Grant access to a specific group

1. Under **Access permissions**, select **Grant access permission**.
2. Under **Who to grant access to**, select **Specific group**.
3. Under **User group**, select the group.
4. From **What they should be able to do with the dashboard**, select `Edit` or `View`.

Dynatrace adds the group to the list under **Grant access permission**, and everyone in it gets the access you selected. To change the access level later, select **Details** for that group. To revoke access, select **Delete** for that group.

### Grant access to any user with the link

1. Under **Access permissions**, select **Grant access permission**.
2. Under **Who to grant access to**, select **Any user with the link**.
3. Select **Copy link**, and share the link with the users who should view the dashboard.

Any authenticated Dynatrace user with a copy of the link can view the dashboard. The dashboard appears in the user's **Dashboards** table only after they use the link for the first time. To revoke this access, select **Delete** in the **Any user with the link has permission** row.

### Grant anonymous access

An anonymous link lets anyone view the dashboard without signing in, even people without Dynatrace access. Anonymous access grants view permission only, and you can create one link per management zone.

Anonymous links require you to turn on **Allow anonymous access** under **Settings** > **Dashboards** > **General settings**. That global setting determines whether anyone can share dashboards publicly.

1. Under **Anonymous access**, select **Add anonymous access link**.
2. From the management zone list for the link, select a management zone or leave it set to `default`. The management zones available depend on your permissions when you create the link.
3. After you save your changes, expand the link's entry (**Details**) and select **Copy link**.

Repeat these steps to create more anonymous links.

* If a [default timeframe and management zone](/managed/analyze-explore-automate/dashboards/how-dashboards-scope-and-refresh-data#default "Learn how timeframe, management zone, and dynamic filter settings decide which data dashboard tiles show, and how often each tile refreshes.") are set for the dashboard, the link uses them. Otherwise, the link uses the last two hours as its timeframe and the **All** management zone.
* If the link uses the **All** management zone, a recipient has access to the management zones you had access to when you created the link.

A shared link carries the creator's permissions, not the recipient's. Anyone using a link you create can see everything you see through it, such as management zones. If you lose permissions, people using your link lose them too. For stricter control, grant access per user or group instead.

## Step 3 Save your changes

Select **Save changes**.

The users, groups, and links you added appear in the **Manage access** tab and can access the dashboard as you specified.

## Step 4 optional Set up email reports

Users with access to a dashboard can subscribe to weekly or monthly email reports for it. Anyone can view a report without Dynatrace credentials, so you can forward report emails to people who don't have Dynatrace access.

Reports require **Allow anonymous access** under **Settings** > **Dashboards** > **General settings**. If it's turned off, accessing a dashboard report anonymously returns a 403 error.

1. Enable reports for the dashboard. Reports are turned off by default.

   1. Display the dashboard and select **Edit**.
   2. Select the **Settings** tab, turn on **Enable reports**, and select **Done**.
2. Select **More** > **Subscribe**.

   If reports are turned off and you have edit permission, select **Enable reports** when it's displayed, and then continue. Without edit permission, ask someone who has it to enable reports, or clone the dashboard and subscribe to the clone.
3. Select `Weekly`, `Monthly`, or both.

To subscribe other people, even people without Dynatrace access, use the [Reports API](/managed/dynatrace-api/configuration-api/reports-api "Manage reports via the Dynatrace configuration API.") to add any valid email address as a recipient. To unsubscribe, select the **unsubscribe** link included in every report email.

Reports are generated for Monday morning, every Monday for weekly reports or the first Monday of the month for monthly reports. Each report is generated after the preceding midnight, in the time zone set on the tenant, and the email is sent within the following six hours. If sending fails, it's retried after a wait period.

The email doesn't contain the report contents. Instead, the email contains a public link to the report, with a timeframe that matches the report frequency. The subject line is based on the dashboard name, with special characters escaped for security reasons. For example, `&` becomes `&amp`.

## Stop sharing a dashboard

1. Go to **Dashboards** and select the name of the dashboard.
2. Select **More** > **Share** in the upper-right corner of the dashboard.
3. Turn off **Share this dashboard**.

Dynatrace keeps your share settings and reactivates them if you turn sharing back on.

To revoke a single anonymous link, locate it under **Anonymous access**, select **X** in the **Delete** column, and select **Save changes**.

To stop all subscribed users from receiving reports, display the dashboard, select **Edit**, select the **Settings** tab, turn off **Enable reports**, and select **Done**.