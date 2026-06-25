---
title: Jira integration for security notifications
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/security-notifications-rap/jira-integration
scraped: 2026-05-12T12:10:30.586378
---

# Jira integration for security notifications

# Jira integration for security notifications

* How-to guide
* Published Dec 29, 2021

With Dynatrace Jira integration, issue tickets are generated automatically for all new attacks in your Dynatrace environments. Direct integration of Dynatrace and Atlassian Jira saves you a lot of manual work and completely automates the reporting of Dynatrace-detected attacks in your monitored environments into your organization's Jira project.

To integrate security notifications with Jira, follow the instructions below.

## Set up notifications for attacks

To set up notifications for attacks

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an alerting profile**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/jira-integration#profile "Integrate security notifications for vulnerabilities and/or attacks using Jira.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Link the alerting profile**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/jira-integration#link "Integrate security notifications for vulnerabilities and/or attacks using Jira.")

### Step 1 Create an alerting profile

Create an alerting profile, which allows you to set up alert-filtering rules that are based on the state of detected attacks.

1. Go to **Settings** and select **Alerting** > **Attack alerting profiles**.
2. Select **Add alerting profile**.
3. Enter a **Name** for the profile on which you want to receive security notifications.
4. Turn on the switch of any attack status for which you want to receive notifications. You can select more than one.
5. Select **Save changes** to save your configuration.

### Step 2 Link the alerting profile to a Jira security notifications integration

Link the alerting profile to a security notifications integration with Jira. You can define the Jira integration and configure the payload (in the form of a message template) that you want to receive with your security notifications.

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Add integration** and enter the following information.

   * **Security alert type:** Select **Attack alert**.
   * **Notification type:** Select **Jira**.
   * **Display name:** Enter a name for the Jira integration. This name will be displayed on **Settings** > **Integration** > **Security notifications** after you save this configuration.
   * **Jira endpoint URL:** Enter the URL of the webhook API endpoint using the following syntax: `https://{instancename}.atlassian.net/rest/api/2`. Be sure to replace `{instancename}` with your Atlassian instance.
   * **Username:** Enter the username of the Jira profile.
   * **API token:** Enter the API token for the Jira profile. To create an API token, in your Jira account, go to **API tokens** and select **Create API token**.
   * **Project key:** Enter the key of the Jira project where new issues are to be created and tracked. To find the project key, in your Jira account, go to **Project settings** > **Details**.
   * **Issue type:** Enter the issue type, such as `task` or `story`, that should be used for issues detected by Dynatrace. Be sure to specify an issue type that's already been set up in Jira or your integration will fail. To find all available issue types or create a new one, in your Jira account, go to **Project settings** > **Issue types**.
   * **Summary:** Enter a brief summary of the issue.
   * **Issue description:** Enter details of the issue.

   Besides plain text, your summary and issue description can both include placeholders. Select the **Info** icon for a list of **Available placeholders** that you can use for this integration. Placeholders are automatically replaced with information related to the attack when the notification is generated.

   * **Alerting profile:** Select the [alerting profile](#profile) on which you want to receive security notifications.
3. Optional To verify your configuration, select **Send test notification**. If your configuration is correct:

   * You should receive a ticket in Jira.
   * The following info message should be displayed on the Dynatrace settings page: `Test notification sent successfully`.
4. **Save changes**.

**Example reporting to a Jira ticket**

![jira-payload-attacks](https://dt-cdn.net/images/image-6-975-fab7baa100.png)

jira-payload-attacks

Dynatrace doesn't automatically close resolved issues. You need to close Jira issues manually.

## Verify your configuration

To verify that your integration is set up correctly

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Details** for the integration you want to check.
3. Select **Send test notification**. If your configuration is incorrect and the test notification hasn't been sent to Jira, you'll receive an error message that will help you identify the problem.

## Related topics

* [Jira integration for security notifications](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/jira-integration "Integrate security notifications for vulnerabilities and/or attacks using Jira.")
* [Application Security FAQ](/managed/secure/faq "Frequently asked questions about Dynatrace Application Security.")