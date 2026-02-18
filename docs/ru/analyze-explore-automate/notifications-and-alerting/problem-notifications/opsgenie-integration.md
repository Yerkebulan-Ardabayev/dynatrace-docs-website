---
title: Send Dynatrace notifications to Opsgenie
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration
scraped: 2026-02-18T21:16:29.366589
---

# Send Dynatrace notifications to Opsgenie

# Send Dynatrace notifications to Opsgenie

* 2-min read
* Updated on Oct 10, 2022

Dynatrace offers an out-of-the-box Opsgenie integration that automatically pushes Dynatrace problem notifications to your Opsgenie environment in multiple regions.

To set up Opsgenie problem-notification integration

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **Opsgenie** from the available notification types.
4. Configure the notification:

   * Enter a **Display name** for this integration. This is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * **Opsgenie API key**  
     Switch over to your Opsgenie account and set up Dynatrace integration. Insert the generated Opsgenie API key into this field.
   * **Opsgenie region domain**  
     Select any Opsgenie region by starting to type the regionâs endpoint. If this field is left empty, the US region is selected by default.
   * **Message**  
     Enter text and problem-related placeholders.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Problem notifications automatically fill in the placeholder values and include them in the corresponding Opsgenie incidents. Opsgenie incidents are automatically created when problems are detected and closed when problems are resolved. Incident details contain the detailed problem information as well as a direct link to the problem in Dynatrace.
5. Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
6. Select **Send test notification** to make sure your OspGenie integration is working.
7. **Save changes**.

## Priority levels

Dynatrace availability problems are mapped to Opsgenie P1 incidents, error problems are mapped to P2, slowdowns are mapped to P3, and so on. Dynatrace also pushes the tags of all problem-affected components along with each Opsgenie incident.

The problem URL contains the pure backlink to the Dynatrace environment that pushed the problem incident.

The following image shows a Dynatrace-detected problem pushed over to Opsgenie. The alert includes:

* tags of all problem-affected entities
* a link back to the problem in Dynatrace
* the problem severity detected by Dynatrace mapped to the corresponding Opsgenie priority value.

![Opsgenie card](https://dt-cdn.net/images/opsgenie-card-1557-319ec81575.png)