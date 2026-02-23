---
title: Send Dynatrace notifications to xMatters
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration
scraped: 2026-02-23T21:20:22.840880
---

# Send Dynatrace notifications to xMatters

# Send Dynatrace notifications to xMatters

* 2-min read
* Updated on Jul 17, 2024

xMatters is a digital service availability platform that prevents technology issues from becoming business problems. With this xMatters integration, Dynatrace actively pushes problem alerts, along with all related metadata, into your xMatters instance. You can acknowledge xMatters alerts and comment on Dynatrace-detected problems via your preferred device. xMatters automatically records your responses in Dynatrace.

## Configure xMatters

For configuring xMatters, see the [Dynatraceï»¿](https://help.xmatters.com/integrations/monitoring/dynatrace.htm?cshid=Dynatrace) page in the xMatters Workflows documentation.

The built-in version of xMatters integration that requires an API token is no longer available. If you require it as a reference, see the [Previous versionsï»¿](https://help.xmatters.com/integrations/monitoring/dynatrace.htm?cshid=Dynatrace#PreviousVersions) section of the Dynatrace integration in the official xMatters documentation.

## Configure Dynatrace

1. Go to **Settings** and select **Integration** > **Problem notifications**.
2. Select **Add notification**.  
   Ignore **Save changes** until the end.
3. Select **xMatters** from the available notification types.
4. Configure the notification:

   * **Display name**âthe freeform name of this integration that will be displayed in Dynatrace on the **Problem notifications** page when you finish this configuration.
   * **xMatters URL**âthe xMatters webhook URL.
   * Optional Turn on **Accept any SSL certificate** option. We recommend that you use a valid SSL certificate (even for internal installations), but you can ignore the certificate for convenience.
   * Optional **Additional HTTP headers**âcustom HTTP header fields such as 'Content-Type' or 'Authorization' that can be used if the target endpoint needs an authentication token within the HTTP header or if you would like to send a different content type such as 'text/plain' or 'application/xml'.
   * **Custom payload**âonce a problem is detected or resolved, this customizable payload is pushed through an **HTTP POST** to the target system. Use specific placeholders to dynamically populate the payload with problem-related information, such as problem state or title.
   * Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
5. Select **Send test notification** to make sure your xMatters integration is working.
6. Select **Save changes**.

After youâve finished integration with Dynatrace, youâll see your newly created xMatters integration in your list of integrations on the **Problem notifications** page.