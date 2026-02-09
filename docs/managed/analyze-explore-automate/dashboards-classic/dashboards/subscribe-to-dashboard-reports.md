---
title: "Subscribe to Dynatrace dashboard reports"
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports
updated: 2026-02-09
---

# Subscribe to Dynatrace dashboard reports

# Subscribe to Dynatrace dashboard reports

* How-to guide
* 3-min read
* Published Oct 29, 2019

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

Users with access to a classic dashboard can subscribe to email reports (weekly, monthly, or both) that are specific to that dashboard.

## Report access

Reports can be viewed without entering Dynatrace credentials. With this approach, report emails can be forwarded to external recipients who don't have access to Dynatrace.

To allow users to grant such anonymous access to dashboards

1. Go to **Settings** and select **Dashboards** > **General settings**.
2. Turn on **Allow anonymous access**.

   This global (account-level) setting determines whether dashboards can be shared publicly. If you turn it off, an attempt to access a dashboard report anonymously returns a 403 error.
3. Select **Save changes**.

## Email contents

The email doesn't contain the report contents.

Each report email contains a public link (credentials are not required) to the report. The link includes a timeframe corresponding to the selected report frequency (weekly or monthly).

The subject line of the email is based on the dashboard name. If your dashboard name has special characters, they are escaped (for example, `&` becomes `&amp`). This is done for security reasons and can't be modified.

## Report generation and delivery

The aim is to email a link to a Monday morning report, either weekly (every Monday morning) or monthly (on the first Monday morning of every month).

* The report is generated at some point after the midnight preceding that Monday morning (00:00 or 12:00 AM). Midnight is computed using the timezone set on the tenant.
* The email linking to that report is sent within the subsequent six hours. If sending fails, sending is re-attempted after a wait period.

## Enable dashboard reports

Dashboard reports are disabled by default. If you enable them for a dashboard, users with access to that dashboard can subscribe to reports and can view them without signing in to Dynatrace.

1. Display the dashboard.
2. Select **Edit**.
3. Select the **Settings** tab.
4. Turn on **Enable reports**.
5. Select **Done**.

## Disable dashboard reports

To prevent all subscribed users from receiving reports from a dashboard

1. Display the dashboard.
2. Select **Edit**.
3. Select the **Settings** tab.
4. Turn off **Enable reports**.
5. Select **Done**.

## Subscribe to a dashboard report

To subscribe yourself to a dashboard report

1. Display the dashboard.
2. Select **More** (**â¦**) > **Subscribe**.

   If reports are disabled for a dashboard, you can't subscribe to it.

   * If you have edit permission, Dynatrace displays an **Enable reports** button when you try to subscribe. Select it to enable reports for this dashboard, and then continue.
   * If you don't have edit permission, you can ask someone with edit permission to enable reports, or you can clone the dashboard and then subscribe to the clone.
3. Select how often you want to receive a dashboard report in email (`Weekly`, `Monthly`, or both).

### Subscribe others to a dashboard

To subscribe other people to a dashboard, even if they don't have access to Dynatrace, use the [Reports API](/managed/dynatrace-api/configuration-api/reports-api "Manage reports via the Dynatrace configuration API.") to specify any valid email address as a dashboard report recipient.

## Unsubscribe from a dashboard report

To unsubscribe from a dashboard report, select the **unsubscribe** link that's included in every report email.

## Related topics

* [Reports API](/managed/dynatrace-api/configuration-api/reports-api "Manage reports via the Dynatrace configuration API.")
