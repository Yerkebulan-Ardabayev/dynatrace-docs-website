---
title: Send Dynatrace notifications to PagerDuty
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration
---

# Send Dynatrace notifications to PagerDuty

# Send Dynatrace notifications to PagerDuty

* 3-min read
* Updated on Apr 25, 2024

Dynatrace offers an [out-of-the-box integration](#out-of-the-box-integration) that automatically pushes Dynatrace problem notifications to your PagerDuty environment. This integration provides PagerDuty responders with the link to the Dynatrace problem card.

Custom webhook

If you want more custom notification fields, you can set up a [custom webhook](#custom-integration) instead of the out-of-the-box integration. For further information on configuring a custom webhook integration in Dynatrace, see [Webhook integration](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration "Learn how to integrate problem-notifications using a custom webhook.").

## Out-of-the-box integration

To set up PagerDuty problem-notification integration

1. In **Dynatrace**, go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **PagerDuty** from the available notification types.

3. Enter the following information:

   * **Display name** is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * **Account** is your PagerDuty account name. Informational only. Not used in the API call.
   * **Service name**  
     Enter 'Dynatrace' as the target service name. Informational only. Not used in the API call.
   * **Service key**  
     Paste your auto-generated PagerDuty service key here.

     This value is used in the API call and must match the PagerDuty Integration Key created by PagerDuty. A PagerDuty Integration Key is unique and associated with a PagerDuty Service defined in the PagerDuty service directory.
4. Finalize and save.

## Webhook custom integration

If you want more custom notification fields, use this procedure to integrate Dynatrace and PagerDuty with a custom webhook.

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Set up notifications** and then select **Custom integration**.
3. Configure the integration.
   Example PagerDuty custom integration settings

   ![PagerDuty webhook configuration](https://dt-cdn.net/images/pagerduty-webhook-356-b94d1693cf.png)

   PagerDuty webhook configuration

   * **Name**  
     Informational only. Not used in the API call.
   * **Webhook URL**  
     Must be `https://events.pagerduty.com/v2/enqueue`.
   * **Custom payload**  
     Follows the PagerDuty enqueue API payload structure.