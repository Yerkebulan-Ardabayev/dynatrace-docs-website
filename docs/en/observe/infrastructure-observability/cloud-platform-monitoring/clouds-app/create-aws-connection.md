---
title: Create a new AWS connection
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app/create-aws-connection
scraped: 2026-02-16T21:19:54.294538
---

# Create a new AWS connection

# Create a new AWS connection

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Aug 19, 2025
* Preview

If this is the first time you are creating a connection, first see the [onboarding instructions](/docs/ingest-from/amazon-web-services/create-an-aws-connection "See the differences between creating your AWS connections via API or ::app-settings::.") and its prerequisites.

If you have an existing classic connection and want to start the new cloud platform monitoring, delete the classic connection first and only then create a new cloud connection for the respective AWS Account or Azure subscription.

To set up a new AWS connection

1. Go to ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.
2. In the upper-right corner of the page, select  **Create connection** > **AWS New**.

   Note: If it's your first cloud connection, you can also select **Create connection** > **AWS New** on the Overview page.
3. Follow the steps outlined in **New connection** to start the onboarding process for a new AWS cloud connection.

   ![Clouds app | Create a new AWS connection](https://dt-cdn.net/images/clouds-app-create-an-aws-connection-3840-485c4caab2.png)
4. After youâve successfully deployed the CloudFormation stack within AWS, it takes up to 15 minutes to see your cloud inventory on the new **Explorer New** tab view within ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.
5. Optional Check the state and health of your cloud connection in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Cloud and virtualization**.
   2. Select **AWS**.
6. Optional Set up and configure health alerts and warning signals in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Alerts** > **Cloud services**.
   2. Select **New Alerts**.
   3. Follow the steps in the wizard to create health alerts for your newly onboarded AWS Account.

   ![Settings | Ready-made alerts](https://dt-cdn.net/images/settings-ready-made-alerts-3840-d19f21a2a8.png)![Settings | Health alert details](https://dt-cdn.net/images/settings-health-alert-details-3840-f4fc0982c7.png)

   1 of 2