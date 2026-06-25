---
title: Email integration for security notifications
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/security-notifications-rap/email-integration
scraped: 2026-05-12T12:10:32.546438
---

# Email integration for security notifications

# Email integration for security notifications

* How-to guide
* Published Aug 11, 2022

Integrate security notifications with Dynatrace to pass security issues and/or attacks to your email account for alerting and remediation purposes.

To integrate security notifications via email, follow the instructions below.

## Set up notifications for attacks

To set up notifications for attacks

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an alerting profile**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration#profile "Integrate security notifications for vulnerabilities via email.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Link the alerting profile**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration#link "Integrate security notifications for vulnerabilities via email.")

### Step 1 Create an alerting profile

Create an alerting profile that allows you to set up alert-filtering rules that are based on the state of detected attacks.

1. Go to **Settings** and select **Alerting** > **Attack alerting profiles**.
2. Select **Add alerting profile**.
3. Enter a **Name** for the profile on which you want to receive security notifications.
4. Turn on the switch of any attack status for which you want to receive notifications. You can select more than one.
5. Select **Save changes** to save your configuration.

### Step 2 Link the alerting profile to an email security notifications integration

Link the alerting profile to a security notifications integration via email. You can define the email integration and configure the payload (in the form of a message template) that you want to receive with your security notifications.

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Add integration** and enter the following information.

   * **Security alert type:** Select **Attack alert**.
   * **Notification type:** Select **Email**.
   * **Display name:** Enter a name for the email integration. This name will be displayed on **Settings** > **Integration** > **Security notifications** after you save this configuration.
   * Select **Add recipient** to add the email address of the recipient (required), carbon copy recipient (optional), and blind carbon copy recipient (optional). The total number of email addresses mustn't exceed 50.
   * **Subject:** Enter the title of the attack.
   * **Body:** Enter the attack description. HTML formatting is supported.

   Besides plain text, your attack description can include placeholders. Select the **Info** icon for a list of **Available placeholders** that you can use for this integration. Placeholders are automatically replaced with information related to the attack when the notification is generated.

   * **Alerting profile:** Select the [alerting profile](#profile-create) on which you want to receive security notifications.
3. Optional To verify your configuration, select **Send test notification**. If your configuration is correct:

   * You should receive a test email on your desired email account
   * The following info message should be displayed on the Dynatrace settings page: `Test notification sent successfully`.
4. **Save changes**.

**Example email reporting**

![Email notification for attacks](https://dt-cdn.net/images/2023-04-19-10-25-55-1200-70c5af2e5c.png)

Email notification for attacks

## Verify your configuration

To verify that your integration is set up correctly

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Details** for the integration you want to check.
3. Select **Send test notification**. If your configuration is incorrect and the test notification hasn't been sent via email, you'll receive an error message that will help you identify the problem.

## Related topics

* [Email integration for security notifications](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration "Integrate security notifications for vulnerabilities via email.")
* [Application Security FAQ](/managed/secure/faq "Frequently asked questions about Dynatrace Application Security.")