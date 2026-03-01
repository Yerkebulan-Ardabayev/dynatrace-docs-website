---
title: Send Dynatrace notifications via email
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration
scraped: 2026-03-01T21:08:34.867152
---

# Send Dynatrace notifications via email

# Send Dynatrace notifications via email

* 2-min read
* Updated on Apr 25, 2024

For extended capabilities and workflow automation (for example, enabling targeted notification and problem remediation), see [Workflows Connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").

Dynatrace offers several out-of-the-box integrations that automatically push Dynatrace problem notifications to your third-party messaging or incident-management systems. If, however, your third-party system isn't supported with an out-of-the-box integration, you can easily set up email integration. Using this approach, an email is sent out whenever Dynatrace detects a problem in your environment that affects real users.

Short-lived problems

Short-lived problems do not generate open problem notifications. For such problems, Dynatrace sends out only resolved problem notifications to inform you that such a problem occurred.

You can customize the subject line of problem-notification emails by defining a text template that includes placeholders that are dynamically populated with relevant problem details, such as problem ID, problem impact, or problem state. By default, the body of email notifications contain an HTML-formatted description of the detected problem and a direct link to the corresponding [problem details](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") page in Dynatrace.

To set up email-based problem notifications

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **Email** from the available notification types.
4. Configure the notification:

   * Enter a **Display name** for this integration. This is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * In the **To** section, select **Add recipient** to add the email address that should receive notifications. To add more recipients, select **Add recipient** for each additional **To** address.
   * In the **CC** field, select **Add recipient** to add additional email addresses that should receive notifications.
   * In the **BCC** field, select **Add recipient** to add additional email addresses that should receive notifications but should not be displayed in the email header.
   * In the **Subject** field, type text and/or insert placeholders that will be automatically populated with relevant problem details, such as problem ID, state, or impact.
   * In the **Body** field, configure the problem alert message that is to appear in the body of problem-notification emails.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Placeholders are automatically replaced with actual values in the message.
   * Select an [alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.") to filter the problem feed.
5. Select **Send test notification** to make sure your email integration is working.
6. **Save changes**.