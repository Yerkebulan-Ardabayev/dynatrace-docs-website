---
title: Send Dynatrace notifications to Slack
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration
scraped: 2026-02-28T21:07:31.589765
---

# Send Dynatrace notifications to Slack

# Send Dynatrace notifications to Slack

* 2-min read
* Updated on Apr 25, 2024

For extended capabilities and workflow automation (for example, enabling targeted notification and problem remediation), see [Workflows Connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").

With a Slack problem-notification integration, your teams will always be aware of potential risks within applications, services, and infrastructure. Your teams can also use a Dynatrace-integrated Slack channel to discuss incidents, evaluate solutions, and link to similar problems.

## Set up Slack integration

1. In Slack, create an Incoming Webhook, as [described in the Slack documentationï»¿](https://api.slack.com/messaging/webhooks).
2. Copy the generated Webhook URL to your clipboard. The Webhook URL should look like this: `<SLACK_WEBHOOK_URL_PLACEHOLDER>`.
3. In Dynatrace, go to **Settings** > **Integration** > **Problem notifications**.
4. Select **Add notification**.
5. Select **Slack** from the available notification types.
6. Enter the following information:

   * **Display name**
     This is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * **URL**
     Paste the webhook URL
   * **Channel**
     Enter the name of a Slack channel
   * **Message**
     Enter a custom message; it can contain text and problem-related placeholders

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Placeholders are automatically replaced with actual values.
7. Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
8. Select **Send test notification** to make sure your Slack integration is working.
9. **Save changes**.

You will receive Dynatrace problem notifications on your Slack channel with your custom message.

Example

![An example of Slack integration](https://dt-cdn.net/images/example-1664-91d9af0698.png)

## Troubleshooting

* [Slack problem notifications from Dynatrace don't arriveï»¿](https://dt-url.net/ti03ks4)