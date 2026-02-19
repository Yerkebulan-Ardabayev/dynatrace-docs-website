---
title: Send Dynatrace notifications to Microsoft Teams
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration
scraped: 2026-02-19T21:13:33.691217
---

# Send Dynatrace notifications to Microsoft Teams

# Send Dynatrace notifications to Microsoft Teams

* 2-min read
* Updated on Jan 22, 2026

For extended capabilities and workflow automation (for example, enabling targeted notification and problem remediation), see [Workflows Connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").

Deprecation

Due to the [retirement of Office 365 connectors within Microsoft Teamsï»¿](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/), this integration is deprecated, and it won't be possible to create new connectors after August 15th, 2024. Existing connectors will continue to work until the end of March 2026.

Follow the Microsoft transition instructions to switch from Office 365 connectors to Microsoft Workflows.

Dynatrace notifications can be sent to your Microsoft Teams channels so that your teams are always aware of any problems in your applications, services, and infrastructure. Integrating a Microsoft Teams channel with Dynatrace gives your teams the ability to discuss incidents, evaluate solutions, and link to similar problems while remaining up to date regarding problem status and severity.

To set up integration of Microsoft Teams and Dynatrace

1. In Microsoft Teams, create an Incoming Webhook, as described in the [Microsoft official documentationï»¿](https://dt-url.net/w3237oc).
2. In Dynatrace, go to **Settings** > **Integration** > **Problem notifications**.
3. Select **Add notification**.
4. Select **Custom integration** from the list of available notification types.
5. Configure the notification:

   * Enter a **Display name** for this integration. This is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * Paste the Microsoft Teams webhook URL (Microsoft Teams Connector URL) into the **Webhook URL** field.
   * Optional Turn on **Accept any SSL certificate**. We recommend that you use a valid SSL certificate (even for internal installations), but you can ignore the certificate for convenience.
   * Enter the Microsoft Teams-specific JSON payload in the format:

     ```
     {



     "title":"{ProblemTitle}",



     "text":"{ProblemDetailsHTML}",



     "themeColor":"EA4300"



     }
     ```

     The connector payload format can be completely customized. To read more about the Microsoft Teams Connector format, please refer to this [Microsoft Documentation pageï»¿](https://docs.microsoft.com/en-us/outlook/actionable-messages/message-card-reference/).
6. Select **Send test notification** to make sure your Teams integration is working.
7. **Save changes**.

After youâve integrated Dynatrace and Microsoft Teams, youâll receive all Dynatrace-detected problems directly within your Teams channels.

Example

![Microsoft Teams screen integrated with Dynatrace](https://dt-cdn.net/images/msteams-integrated-1380-16dcf8dd22.png)