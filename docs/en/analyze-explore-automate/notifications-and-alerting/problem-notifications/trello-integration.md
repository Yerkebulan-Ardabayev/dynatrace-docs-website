---
title: Send Dynatrace notifications to Trello
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/trello-integration
scraped: 2026-02-24T21:15:06.438484
---

# Send Dynatrace notifications to Trello

# Send Dynatrace notifications to Trello

* 2-min read
* Updated on Oct 10, 2022

Atlassian Trello offers a great visual way to organize your projects, no matter which kind of agile process you are following. Everything in Trello is organized in cards. Cards show the details about tasks and stories or bugs your team must solve.

Dynatrace offers convenient integration with Trello that lets you visually organize all the automatically discovered incidents directly within your Trello boards. Connect your Dynatrace monitoring environment with your Trello board and directly push Dynatrace discovered problems into a specified list.

To set up Trello problem-notification integration

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **Trello** from the available notification types.
4. Configure the integration:

   * **Display name** is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * Enter your Trello application key.

     Trello application key

     Sign in to Trello and have Trello automatically generate an [application keyï»¿](https://trello.com/app-key) that you can use here.
   * Enter your Trello authorization token.
   * Specify the Trello board to which problem cards should be assigned.
   * Specify the Trello list to which new problem cards should be assigned.
   * Specify the Trello list to which resolved problem cards should be assigned.
   * Enter the card text and problem placeholders that should appear on new problem cards.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Placeholders are automatically replaced with actual values in the card text.
   * Enter the card description.
   * Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
5. Select **Send test notification** to make sure your Trello integration is working. It should send a test notification to Trello.
6. If the test was successful, **Save changes**.