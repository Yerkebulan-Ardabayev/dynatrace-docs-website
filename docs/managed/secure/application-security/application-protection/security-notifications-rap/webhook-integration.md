---
title: Webhook integration for security notifications
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/security-notifications-rap/webhook-integration
---

# Webhook integration for security notifications

# Webhook integration for security notifications

* How-to guide
* Published Oct 21, 2021

Integrate security notifications with Dynatrace to pass security issues and/or attacks to your teams for alerting and remediation purposes.

To integrate security notifications using webhooks, follow the instructions below.

## Set up notifications for attacks

To set up notifications for attacks

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an alerting profile**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration#profile "Integrate security notifications for vulnerabilities and/or attacks using webhooks.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Link the alerting profile**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration#link "Integrate security notifications for vulnerabilities and/or attacks using webhooks.")

### Step 1 Create an alerting profile

Create an alerting profile, which allows you to set up alert-filtering rules that are based on the state of detected attacks.

1. Go to **Settings** and select **Alerting** > **Attack alerting profiles**.
2. Select **Add alerting profile**.
3. Enter a **Name** for the profile on which you want to receive security notifications.
4. Turn on the switch of any attack status for which you want to receive notifications. You can select more than one.
5. Select **Save changes** to save your configuration.

### Step 2 Link the alerting profile to a webhook security notifications integration

Link the alerting profile to a security notifications integration using webhooks. You can define the webhook integration and configure the payload (in the form of a message template) that you want to receive with your security notifications.

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Add integration** and enter the following information.

   * **Security alert type:** Select **Attack alert**.
   * **Notification type:** Select **Custom integration**.
   * **Display name:** Enter a name for the webhook integration. This name will be displayed on **Settings** > **Integration** > **Security notifications** after you save this configuration.
   * **Webhook endpoint URL:** Enter the URL of the webhook API endpoint.
3. Optional Choose whether you want to accept any SSL certificate.

   * **On** = Accept any SSL certificate (including self-signed and invalid certificates)
   * **Off** = Dynatrace verifies the SSL certificate of the URL. (Recommended)
4. Select **Add HTTP header** to specify additional HTTP header fields, such as `Content-Type` or `Authorization`. These custom HTTP header fields can be used if the target endpoint needs an authentication token within the HTTP header or if you would like to send different content types such as `application/json`, `application/xml`, `text/plain`.

   The **Content-Type** field is required, others are optional.
5. In the **Custom payload** field, customize your notification format and content. Once an attack is detected, this customizable payload is pushed through an **HTTP POST** to the target system. Select the **Info** icon for a list of **Available placeholders** that you can use for this integration. Placeholders are automatically replaced with information related to the attack when the notification is generated.

**Example message template:**

```
{



"text": "Notification for ATTACK *{AttackDisplayId}*. \nTitle: *{Title} - ({Type}) - {State}*\n{AttackUrl}\n* Process group: {ProcessGroupId}, \n* Entry point: {EntryPoint}, \n* Timestamp: {Timestamp}, \n* Vulnerability: {VulnerabilityName}.  \n\n *from test system* :dynatrace:"



}
```

**Example payload:**

![webhook-attacks](https://dt-cdn.net/images/image-4-640-79cfc484d6.png)

webhook-attacks

6. From the **Alerting profile** list, select the [alerting profile](#profile) on which you want to receive security notifications.
7. Optional To verify your configuration, select **Send test notification**. If your configuration is correct:

   * You should receive a notification on your organization's endpoint.
   * The following info message should be displayed on the Dynatrace settings page: `Test notification sent successfully`.
8. **Save changes**.

## Verify your configuration

To verify that your integration is set up correctly

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Details** for the integration you want to check.
3. Select **Send test notification**. If your configuration is incorrect and the test notification hasn't been sent to your organization's selected endpoint, you'll receive an error message that will help you identify the problem.

## Related topics

* [Webhook integration for security notifications](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration "Integrate security notifications for vulnerabilities and/or attacks using webhooks.")
* [Application Security FAQ](/managed/secure/faq "Frequently asked questions about Dynatrace Application Security.")