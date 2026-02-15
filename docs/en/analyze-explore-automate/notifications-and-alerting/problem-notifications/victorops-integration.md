---
title: Send Dynatrace notifications to VictorOps
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration
scraped: 2026-02-15T08:56:00.349028
---

# Send Dynatrace notifications to VictorOps

# Send Dynatrace notifications to VictorOps

* 2-min read
* Updated on Oct 10, 2022

Dynatrace offers an out-of-the-box VictorOps integration that automatically pushes Dynatrace problem notifications to your VictorOps environment.

To set up VictorOps problem-notification integration

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **VictorOps** from the available notification types.
4. Configure the notification:

   * **Display name**  
     This is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * **API key**  
     Enter the auto-generated VictorOps API key here.

     To get your VictorOps API key

     1. Switch to your VictorOps account.
     2. Go to **Settings** > **Integrations** > **Rest Endpoint** > **Dynatrace** and copy the API key.
     3. Return to Dynatrace and paste it into **API key**.
   * **Routing key**  
     Set a routing key to send problem notifications to the responsible team.
   * **Message**  
     Insert a custom message that includes text and problem-related placeholders.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Placeholders are automatically replaced with values in the message.
   * Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
5. Select **Send test notification** to make sure your VictorOps integration is working.
6. **Save changes**.