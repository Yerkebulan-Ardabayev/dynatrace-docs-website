---
title: Send Dynatrace notifications to Jira
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration
scraped: 2026-02-17T21:14:14.104194
---

# Send Dynatrace notifications to Jira

# Send Dynatrace notifications to Jira

* 3-min read
* Updated on Apr 25, 2024

For extended capabilities and workflow automation (for example, enabling targeted notification and problem remediation), see [Workflows Connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").

With Dynatrace and Jira integration, issue tickets are generated automatically for all new problems that are auto-detected in your Dynatrace environments.

Atlassian Jira is the most popular issue tracking system available today. A high percentage of development and operations departments worldwide use Jira for issue management. The ability of Jira to manage issues, trigger workflows, and track code and production changes is crucial for modern DevOps departments.

Easy, direct integration of Dynatrace and Atlassian Jira saves you a lot of manual work and completely automates the reporting of Dynatrace-detected problems in your monitored environment into your organization's Jira project.

## Configure Jira integration

This integration supports Jira REST API v2. Jira REST API v3 isn't supported.

To configure Jira integration with Dynatrace

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **Jira** from the available notification types.
4. Configure the notification:

   * Enter a **Display name** for this integration. This is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * Enter the **Jira endpoint URI**.
   * Enter the corresponding **Username** and **API token** for this Jira project.

     Personal Access Tokens

     **Personal Access Tokens** aren't supported for the classic Jira integration. You can only use the basic authentication method.
   * Enter the Jira **Project key** (not the project name) of the Jira project where new issues should be created and tracked.

     + To find all available project keys: in Jira, go to **Projects** > **View all projects**.
   * Enter the Jira **Issue type** that should be used for issues detected by Dynatrace.

     + You must specify an issue type that's already been set up in Jira or your integration will fail.
     + To find all available issue types or create a new issue type: in Jira, go to **Options** > **Issues**.
   * Enter a brief **Summary** of the issue and a more detailed **Issue description**.  
     Besides plain text, your summary and issue description can both include placeholders.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Placeholders are automatically replaced with problem-related information.

   You can see the example of the working JIRA configuration below:

   ![A configuration example of Jira integration for notifications and alerting](https://dt-cdn.net/images/example-of-jira-integration-1686-50bc46b6d7.png)
5. Select **Send test notification** to make sure your Jira integration is working.
6. **Save changes**.

## After integration

With your Jira integration complete, Jira tickets are now automatically created within your Jira project for all Dynatrace auto-detected problems.

Example ticket

![Jiraintegration 4](https://dt-cdn.net/images/jiraintegration-4-1646-ae8a48e8c0.png)

Dynatrace automatically updates the severity levels of issues in Jira based on their impact to your applications and customer experience.

Dynatrace does not automatically close resolved issues. You need to close Jira issues manually.