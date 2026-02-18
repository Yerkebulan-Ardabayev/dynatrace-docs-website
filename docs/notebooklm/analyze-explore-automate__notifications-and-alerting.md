# Документация Dynatrace: analyze-explore-automate/notifications-and-alerting
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 13
---

## analyze-explore-automate/notifications-and-alerting/alerting-profiles.md

---
title: Problem alerting profiles
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles
scraped: 2026-02-18T21:22:31.986093
---

# Problem alerting profiles

# Problem alerting profiles

* 4-min read
* Updated on Aug 26, 2025

Problem alerting profiles control the delivery of problem notifications across your organization's alerting channels based on consideration of predefined filters that are based on problem severity, problem duration, custom events, and tags. Problem alerting profiles allow you to control exactly which conditions result in problem notifications and which don't. This includes all problem-push notifications that are sent via the [Dynatrace mobile app](/docs/analyze-explore-automate/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app "Learn how you can connect your Dynatrace environments with the Dynatrace mobile app to receive problem alerts.") and displayed in the Dynatrace web UI. Problem alerting profiles can also be used to set up filtered problem-notification integrations with third-party messaging systems like [Slack](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration "Set up a Slack problem-notification integration that can keep you updated on all Dynatrace problems."), [Opsgenie](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration "Configure Opsgenie integration with Dynatrace."), and [PagerDuty](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration "Learn how to send problem notifications from Dynatrace to PagerDuty.").

Each of your monitoring environments has a default alerting profile that defines the severity level that must be met before an alert is sent out for a detected problem.

Your environment administrator can create new problem alerting profiles that provide fine-grained control over the routing of problem alerts for individual teams or for third-party problem notification integrations, such as Slack, HipChat, and others.

To view your environment's problem alerting profiles, go to **Settings** > **Alerting** > **Problem alerting profiles**. The `Default` profile is always presented in the list. You can modify it but not delete it.

## Alerting profile scope

Alerting profiles provide a powerful filtering mechanism for problem notifications. By combining filter criteria, you can create custom profiles that, for example, delay notification of problems in development environments while immediately alerting on problems detected in production environments. The scope of an alerting profile is defined by

* The management zone.
* Severity rules.
* Event filters.

These conditions are combined by the **AND** logic. An event must fulfill **all** conditions to trigger a notification based on the profile.

Tag matching

Tag matching in alerting profiles is exact. If you provide only a key, the tag will match entities with a given key that has no value. For example, if you specify the key `Apps` without providing any value, it will match an entity with the key `Apps` and an empty value. However, it will not match the entity `AppsRedis` that has the same key, but has a non-empty value.

To match key-value tags, you need to provide both the key and the value.

### Management zone

The management zone filter reduces the amount of data the alerting profile evaluates. Instead of checking all the data your environment generates, you can focus on just the parts coming from the specified management zone.

By default a new alerting profile uses `All` management zones, which means that no filter is applied. In most cases you should apply the management zone filter to reduce the profile scope to the scope of your teams' responsibility. Keep in mind that management zones can overlap. If a problem is detected on a service that is defined within multiple management zones, multiple filters will be applied.

### Severity rules

Severity rules filter events based on their severity level. For each alerting profile, you can specify up to 100 severity rules. These rules are combined by the **OR** logic. An event fulfilling **any** of the rules triggers a notification based on the profile.

You can use the following criteria:

* [Severity level](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.").
* How long the problem is open before an alert is sent outâthis enables you to avoid alerts for low-severity problems that don't affect customer experience and therefore don't require immediate attention.
* Optional Monitoring entities that have any or all of the specified tags

Rule criteria are combined by the **AND** logic. **All** of them must be fulfilled for the rule to be invoked.

### Event filters

Event rules filter events based on their properties. For each alerting profile, you can specify up to 20 event rules. Particularly for auto-remediation use cases, itâs helpful to trigger specific actions based on detailed information thatâs captured during abnormal situations, for example, triggering alerts in cases where problems are related to process crashes.

You can use the following criteria:

* Predefined events Event type
* Custom events Title, description, and properties of the event

Each of criteria can be inverted by using the **negate** option. For example, it turns the **begins with** criterion into **does not begin with**.

The rules are combined by the following logic:

1. All rules that contain negated criteria are grouped by the **AND** logic.
2. All other rules are grouped by the **OR** logic.
3. These two groups (negated and non-negated) are grouped by the **AND** logic.

![Event filter grouping](https://dt-cdn.net/images/alerting-profile-event-filter-2-524-60d54806d2.png)

## Create an alerting profile

To create an alerting profile

1. Go to **Settings** > **Alerting** > **Problem alerting profiles** and select **Add alerting profile**.
2. Type a name for the new profile in the **Create new alerting profile** field and select **Create**.
3. Define the [management zone](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") filter.
4. Define the [severity-level](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.") rules for the profile.
5. Define the event filter. You can base it one one of the following:

   * `Predefined`: a specific built-in event type
   * `Custom`: a title, description, and properties of an event
6. Review the summary of criteria for your new alerting profile and adapt them if needed.
7. Select **Done** in the upper-right corner to save the new alerting profile.

## Alerting profiles API

In addition to the Dynatrace web UI, you can manage your problem alerting profiles via the [Settings API](/docs/dynatrace-api/configuration-api/alerting-profiles-api "Learn what the Dynatrace alerting profiles API offers."). Look for the **Problem alerting profiles** (`builtin:alerting.profile`) schema.

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration.md

---
title: Send Dynatrace notifications via email
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration
scraped: 2026-02-18T21:16:19.360247
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

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration.md

---
title: Send Dynatrace notifications to Jira
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration
scraped: 2026-02-18T21:16:26.861853
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

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration.md

---
title: Send Dynatrace notifications to Microsoft Teams
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration
scraped: 2026-02-18T21:16:25.627333
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

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration.md

---
title: Send Dynatrace notifications to Opsgenie
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration
scraped: 2026-02-18T21:16:29.366589
---

# Send Dynatrace notifications to Opsgenie

# Send Dynatrace notifications to Opsgenie

* 2-min read
* Updated on Oct 10, 2022

Dynatrace offers an out-of-the-box Opsgenie integration that automatically pushes Dynatrace problem notifications to your Opsgenie environment in multiple regions.

To set up Opsgenie problem-notification integration

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **Opsgenie** from the available notification types.
4. Configure the notification:

   * Enter a **Display name** for this integration. This is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * **Opsgenie API key**  
     Switch over to your Opsgenie account and set up Dynatrace integration. Insert the generated Opsgenie API key into this field.
   * **Opsgenie region domain**  
     Select any Opsgenie region by starting to type the regionâs endpoint. If this field is left empty, the US region is selected by default.
   * **Message**  
     Enter text and problem-related placeholders.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Problem notifications automatically fill in the placeholder values and include them in the corresponding Opsgenie incidents. Opsgenie incidents are automatically created when problems are detected and closed when problems are resolved. Incident details contain the detailed problem information as well as a direct link to the problem in Dynatrace.
5. Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
6. Select **Send test notification** to make sure your OspGenie integration is working.
7. **Save changes**.

## Priority levels

Dynatrace availability problems are mapped to Opsgenie P1 incidents, error problems are mapped to P2, slowdowns are mapped to P3, and so on. Dynatrace also pushes the tags of all problem-affected components along with each Opsgenie incident.

The problem URL contains the pure backlink to the Dynatrace environment that pushed the problem incident.

The following image shows a Dynatrace-detected problem pushed over to Opsgenie. The alert includes:

* tags of all problem-affected entities
* a link back to the problem in Dynatrace
* the problem severity detected by Dynatrace mapped to the corresponding Opsgenie priority value.

![Opsgenie card](https://dt-cdn.net/images/opsgenie-card-1557-319ec81575.png)

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration.md

---
title: Send Dynatrace notifications to PagerDuty
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration
scraped: 2026-02-18T21:16:28.123286
---

# Send Dynatrace notifications to PagerDuty

# Send Dynatrace notifications to PagerDuty

* 3-min read
* Updated on Apr 25, 2024

For extended capabilities and workflow automation (for example, enabling targeted notification and problem remediation), see [Workflows Connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").

Dynatrace offers an [out-of-the-box integration](#out-of-the-box-integration) that automatically pushes Dynatrace problem notifications to your PagerDuty environment. This integration provides PagerDuty responders with the link to the Dynatrace problem card.

Custom webhook

If you want more custom notification fields, you can set up a [custom webhook](#custom-integration) instead of the out-of-the-box integration.

## Out-of-the-box integration

To set up PagerDuty problem-notification integration

1. In **Dynatrace**, go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **PagerDuty** from the available notification types.

3. Enter the following information:

   * **Display name** is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * **Account** is your PagerDuty account name. Informational only. Not used in the API call.
   * **Service name**  
     Enter 'Dynatrace' as the target service name. Informational only. Not used in the API call.
   * **Service key**  
     Paste your auto-generated PagerDuty service key here.

     This value is used in the API call and must match the PagerDuty Integration Key created by PagerDuty. A PagerDuty Integration Key is unique and associated with a PagerDuty Service defined in the PagerDuty service directory.
4. Finalize and save.

## Webhook custom integration

If you want more custom notification fields, use this procedure to integrate Dynatrace and PagerDuty with a custom webhook.

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Set up notifications** and then select **Custom integration**.
3. Configure the integration.
   Example PagerDuty custom integration settings

   ![PagerDuty webhook configuration](https://dt-cdn.net/images/pagerduty-webhook-356-b94d1693cf.png)

   * **Name**  
     Informational only. Not used in the API call.
   * **Webhook URL**  
     Must be `https://events.pagerduty.com/v2/enqueue`.
   * **Custom payload**  
     Follows the PagerDuty enqueue API payload structure.

### More information

* For general information on configuring a custom integration in Dynatrace, see [Webhook integration](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration "Learn how to integrate problem-notifications using a custom webhook.").
* For the PagerDuty documentation on how to integrate PagerDuty with Dynatrace via a custom webhook, see PagerDuty's [Dynatrace Integration Guideï»¿](https://www.pagerduty.com/docs/guides/dynatrace-integration-guide/).

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration.md

---
title: Send Dynatrace notifications to ServiceNow
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration
scraped: 2026-02-18T21:16:30.503996
---

# Send Dynatrace notifications to ServiceNow

# Send Dynatrace notifications to ServiceNow

* 9-min read
* Updated on Apr 15, 2025

For extended capabilities and workflow automation (for example, enabling targeted notification and problem remediation), see [Workflows Connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.").

To connect your Dynatrace monitoring environment to your ServiceNow instance, configuration is required both on the ServiceNow instance and in the Dynatrace web UI.

For ServiceNow, Dynatrace offers:

* [Incident integration](#incident-integration)
* [Event management integration](#event-integration)
* [Configuration Management Database (CMDB) integration](#cmdb-integration)

## Incident integrations

There are several integration options for incident management:

* Dynatrace Workflows
* Dynatrace Incident integration app

Once you configure Dynatrace incident integration, Dynatrace automatically creates an incident within your ServiceNow instance for every auto-discovered problem.

### Dynatrace Workflows

Dynatrace Workflows allows you to model incident creation and management processes directly within Dynatrace. For more information about configuration and usage details, see [ServiceNow](/docs/analyze-explore-automate/workflows/actions/service-now "Automate creation of incidents in ServiceNow based on your monitoring data and events.") workflow documentation.

### Dynatrace Incident Integration app

Dynatrace Incident Integration is a ServiceNow environment application that accepts and processes Dynatrace problems and allows you to create incidents within ServiceNow.

If you have installed the ServiceNow Service Graph Connector for Dynatrace, the CIs (Configuration Items) will automatically be associated within the incident.

#### Prerequisites

* You have an active ServiceNow ITSM module and license
* Your ServiceNow user has `web_service_admin` and `x_dynat_ruxit.Integration` roles

#### Set up a ServiceNow configuration

1. Go to [Dynatrace Incident Integration page in the ServiceNow Storeï»¿](https://dt-url.net/fg03qnx) and select **Get** to install Dynatrace Incident Integration in your ServiceNow instance.
2. Follow the **Guided Setup** for an initial configuration of the application.

   ![Guided setup](https://dt-cdn.net/images/2020-11-20-09-31-17-1232-dfc605d001.png)
3. After the application is installed, go to the new **Dynatrace Incident Integration** menu on your ServiceNow instance to further configure (**Setup**, **Settings**) and explore (**Problems**, **ServiceNow Incidents**) the application.

   ![Main modules](https://dt-cdn.net/images/2020-11-20-09-34-57-1853-d333a1780e.png)
4. Use the **Problem to Incident Transform Map** module to transform the incoming Dynatrace data in the **Problems** import set table (`x_dynat_ruxit_problems`) into a ServiceNow **Incident** table.

   ![Transform map](https://dt-cdn.net/images/2020-11-20-09-37-50-1866-f2d395ffed.png)

#### Set up a Dynatrace configuration

To create a ServiceNow problem notification

1. In Dynatrace, go to **Settings**.
2. Select **Integration** > **Problem notifications**.
3. Select **Add notification**.
4. In **Notification type**, select **ServiceNow**.
5. Enter the requested information::

   * **ServiceNow instance identifier** refers to the "instance identifier" part of your own ServiceNow URL (`https://<instance indentifier>.service-now.com`) that is used by the ServiceNow API call. This ServiceNow instance identifier is mutually exclusive to the OnPremise URL field, so you can only use one of them.
   * In the **Description field**, you can customize the text message associated with problem notifications by combining any of the placeholders from **Available placeholders** list in any order according to your needs.
6. Turn on **Send incidents into ServiceNow ITSM**.
7. Select **Send test notification** to make sure your ServiceNow integration is working.
8. Select **Save changes**.

## Event management integration

There are several integration options for event management that use Dynatrace problem notifications. You can:

* Send events using Dynatrace custom integration problem notifications
* Send events using Dynatrace ServiceNow problem notifications

### Send events using Dynatrace custom integration problem notifications

ServiceNow Event Management provides an inbound event API for third party tools to receive events.

This configuration uses a custom integration Dynatrace problem notifications. You can configure custom integration notifications with the ServiceNow inbound event API URL and the JSON payload it expects.

When configured, the Dynatrace problem notification will send grouped events related to a problem.

If you have **ServiceNow Service Graph Connector for Observability - Dynatrace**, see [Set up push notifications from Dynatraceï»¿](https://www.servicenow.com/docs/bundle/xanadu-servicenow-platform/page/product/configuration-management/task/setup-push-notifications-dynatrace.html) for configuration and usage details. Otherwise, see [Integrate Dynatrace platform eventsï»¿](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/event-management/concept/dynatrace-events-integration.html).

### Send events using Dynatrace ServiceNow problem notifications

ServiceNow Event Management provides a general purpose webhook API for receiving events the populates the ServiceNow ITOM event table (`em_event`).

This configuration uses a ServiceNow Dynatrace problem notification. You can configure ServiceNow notification with the ServiceNow webhook API URL and the JSON payload it expects. For more information about the webhook API, see [Pushing events to the instance using web service APIï»¿](https://www.servicenow.com/docs/csh?topicname=send-events-via-web-service.html).

When configured, the Dynatrace problem notification will send all events related to a problem.

#### Prerequisites

* You have an active ServiceNow ITOM module and license
* Your ServiceNow user has a `snc_platform_rest_api_access` role
* Your ServiceNow Event filters and alerting rules are set to react to incoming events sent by Dynatrace

#### Set up a ServiceNow configuration

Your ServiceNow ITOM module and license need to be active to use this integration option.

#### Set up a Dynatrace configuration

1. Go to **Settings**.
2. Select **Integration** > **Problem notifications** > **Add notification**.
3. In **Notification type**, select **ServiceNow**.
4. Enter the requested information:

   * **ServiceNow instance identifier** refers to the "instance identifierâ part of your own ServiceNow URL and is used by the ServiceNow API call `https://<instance indentifier>.service-now.com`. This ServiceNow instance identifier is mutually exclusive to the OnPremise URL field, so you can only use one of them.
5. Turn on **Send events into ServiceNow ITOM**
6. Select **Send test notification**.
7. Select **Save changes**.

After you enable the push of ITOM events, all events for any problem detected by Dynatrace will be automatically pushed to the ITOM event API.

### View events

You can create event filters and alerting rules in the **Event table** view to flexibly react to incoming Dynatrace-detected events, as shown in the example below:

![Events-SN](https://dt-cdn.net/images/2020-11-26-12-33-17-1493-31560df605.png)

## Configuration Management Database (CMDB) integration

ServiceNow offers a dedicated **Service Graph Connector for Observability â Dynatrace** application for pulling Dynatrace observability information into your ServiceNow CMDB.

**Service Graph Connector for Observability â Dynatrace** pulls the following types of topology information data:

* Hosts
* Processes
* Services
* Applications

Service Graph Connector for Observability uses the relationship between various applications, application services, and infrastructure elements to create a Service Map.

Some of the Dynatrace entity types are not imported into ServiceNow. For configuration and usage details, see [Service Graph Connector for Observability - Dynatraceï»¿](https://www.servicenow.com/docs/bundle/xanadu-servicenow-platform/page/product/configuration-management/concept/cmdb-integration-dynatrace.html).

## FAQ

### General

Which Dynatrace IP addresses are allowed for ServiceNow integration?

For your Dynatrace instance to communicate with ServiceNow, you need to provide ServiceNow with a list of Dynatrace IP addresses that will be allowed to send information to ServiceNow. Dynatrace servers are distributed throughout various regions. The best way to ensure that you get the right IP addresses for your region is to look up the IP addresses by running the `nslookup` command. You must first create your environment in Dynatrace and then execute `nslookup`.

Example:

```
C:\>nslookup abc.live.dynatrace.com
```

Optionally, you can review the OneAgent download page to see the IP addresses for your region.

### Dynatrace Incident integration



How does the integration work?

You can see an overview Dynatrace Incident integration in the flowchart below:

![Incident flow](https://dt-cdn.net/images/1-914-942bc926e8.png)

After configuring the application on both sides, problem notifications are pushed from Dynatrace to your ServiceNow instance.

![Incident creation](https://dt-cdn.net/images/2020-11-20-10-04-46-1873-71a111a8db.png)

The **Scripted REST APIs** module is the entry point of the Dynatrace information into ServiceNow. It pushes the data into the **Problems** import set table.

![Problem notification](https://dt-cdn.net/images/2020-11-20-09-46-29-1872-86d224c470.png)

The **Problems** import set table automatically transforms any incoming Dynatrace-detected problem into an incident within the ServiceNow incident table.

![Transform map](https://dt-cdn.net/images/2020-11-20-09-37-50-1866-f2d395ffed.png)

When a problem is closed in Dynatrace, the incident is marked as `Resolved` in ServiceNow.

Which ServiceNow tables are filled by the ServiceNow Dynatrace application?

* Dynatrace sends all detected problems into the ServiceNow incident table (`incident`).
* All single events that are correlated with a Dynatrace-detected problem are sent to the ITOM event table (`em_event`).
* The relationship between a CI and a Dynatrace-detected problem is sent into the CIs Affected table (`task_ci`).
* If enabled, Dynatrace synchronizes all auto-discovered web services into the CMDB application services table (`cmdb_ci_services_discovered`).
* All hosts and process groups running on those hosts are synchronized into the CMDB server table and derived Linux and Windows server tables (`cmdb_ci_server`), and into the process groups related tables in ServiceNow (`cmdb_ci_appl`).

How can I change the table or field where Dynatrace pushes the data?

Incidents are imported through an import set table (`x_dynat_ruxit_problems`). You can reconfigure the default transformation map **Problem to Incident Transformation Map** to route the information to different tables or fields.

Is there support for multiple environments in Dynatrace integration?

Multiple Dynatrace environments can be configured within the Dynatrace environments table in ServiceNow.

### Send events using Dynatrace ServiceNow problem notifications

How does the integration work?

You can see an overview Dynatrace Incident integration in the flowchart below:

![Event flow](https://dt-cdn.net/images/5-921-8ae4cf85e4.png)

### Configuration Management Database (CMDB) integration

Which scheduled jobs pull the CMDB information from Dynatrace?

Dynatrace introduces one scheduled job that pulls a subset of the topology information from Dynatrace Smartscape at regular intervals. The SG-Dynatrace scheduled job pulls all web application information along with their relation to software services, all host and process group information, and all software services and relationships. The information pull is performed using the official Dynatrace REST API.

How can I automatically merge existing CIs with Dynatrace discovered CIs?

Deduplication is done through **ServiceNow CMDB Identification and Reconciliation**. Custom CI identification rules are used to merge identical CIs based on a given attribute (for example, host names).

## Troubleshoot

Check out the following articles in the [Troubleshooting forum in the Dynatrace Communityï»¿](https://dt-url.net/dy122xtf).

### General

* [Events don't show up in the ITOM events tableï»¿](https://dt-url.net/7t42xdu)
* [HTTP 403 Forbidden Access Restricted Not Authorized Error when sending a test notificationï»¿](https://dt-url.net/eq62xe9)
* [Problem link is broken in the ServiceNow incidentï»¿](https://dt-url.net/fcc2x29)

### Dynatrace Incident integration

* [Incidents aren't created correctlyï»¿](https://dt-url.net/o682xbl)

### Configuration Management Database (CMDB) integration

* [Dynatrace-detected hosts, process groups, applications and services don't show up in the CMDBï»¿](https://dt-url.net/km02xrc)
* [Dynatrace-monitored servers don't show up in the CMDBï»¿](https://dt-url.net/n222x11)
* [Incoming incidents aren't mapped to the affected server in the CMDBï»¿](https://dt-url.net/8ia2xbr)

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration.md

---
title: Send Dynatrace notifications to Slack
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration
scraped: 2026-02-18T21:16:24.346035
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

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/trello-integration.md

---
title: Send Dynatrace notifications to Trello
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/trello-integration
scraped: 2026-02-18T21:16:21.860450
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

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration.md

---
title: Send Dynatrace notifications to VictorOps
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration
scraped: 2026-02-18T21:16:20.579220
---

# Send Dynatrace notifications to VictorOps

# Send Dynatrace notifications to VictorOps

* 2-min read
* Updated on Oct 10, 2022

Dynatrace offers an out-of-the-box VictorOps integration that automatically pushes Dynatrace problem notifications to your VictorOps environment.

To set up VictorOps problem-notification integration

1. Go to **Settings** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **VictorOps** from the available notification types.
4. Configure the notification:

   * **Display name**  
     This is the freeform name of this integration that will be displayed in Dynatrace on **Settings** > **Integration** > **Problem notifications** when you finish this configuration.
   * **API key**  
     Enter the auto-generated VictorOps API key here.

     To get your VictorOps API key

     1. Switch to your VictorOps account.
     2. Go to **Settings** > **Integrations** > **Rest Endpoint** > **Dynatrace** and copy the API key.
     3. Return to Dynatrace and paste it into **API key**.
   * **Routing key**  
     Set a routing key to send problem notifications to the responsible team.
   * **Message**  
     Insert a custom message that includes text and problem-related placeholders.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Placeholders are automatically replaced with values in the message.
   * Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
5. Select **Send test notification** to make sure your VictorOps integration is working.
6. **Save changes**.

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration.md

---
title: Send Dynatrace notifications via webhooks
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration
scraped: 2026-02-18T21:16:18.127436
---

# Send Dynatrace notifications via webhooks

# Send Dynatrace notifications via webhooks

* 3-min read
* Updated on Sep 11, 2024

Dynatrace offers several out-of-the-box integrations that automatically push problem notifications to third-party incident-management and ChatOps systems.
If however your third-party system isn't supported with an out-of-the-box integration, you can easily set up a customizable webhook integration. Using this approach, whenever Dynatrace detects a problem in your environment that affects real users, a webhook triggers an `HTTP POST` request to a target URL that you specify.

The payload message of the `HTTP POST` request is completely customizable. By default, requests use valid JSON syntaxâexcept when you define a different HTTP content type header, in which case you define a different HTTP content type header and Dynatrace skips the JSON validation and doesn't escape the payload based on JSON syntax.

Information placeholders, such as **{ProblemTitle}** and **{State}**, are used to fill the custom JSON with the dynamic information of each detected problem.

To integrate problem-notifications using a custom webhook:

1. Go to **Settings Classic** > **Integration** > **Problem notifications**.
2. Select **Add notification**.
3. Select **Custom integration** from the available notification types.
4. Configure the notification:

   * **Display name**  
     This is the freeform name of this integration that will be displayed in Dynatrace on **Settings Classic** > **Integration** > **Problem notifications** when you finish this configuration.
   * Optional Turn on **Secret webhook URL**.
     Turn on this option to obfuscate the webhook URL (the webhook endpoint) in the notification settings, providing an additional layer of security by hiding sensitive information from display.
   * **Webhook URL**  
     Target URL where the **HTTP POST** should push the payload. This URL can contain HTTP parameters such as an authentication token, in case the destination system works with authentication tokens instead of basic authentication.
   * Optional **Additional HTTP headers**  
     Specify additional HTTP header fields, such as 'Content-Type' or 'Authorization'. These custom HTTP header fields can be used if the target endpoint needs an authentication token within the HTTP header or if you would like to send different content type such as 'text/plain' or 'application/xml'.
   * **Custom payload**  
     Once a problem is detected or resolved, this customizable payload is pushed through an **HTTP POST** to the target system.

     Placeholders

     The **Available placeholders** section of the configuration page lists placeholders you can use for this integration. Placeholders are automatically replaced with problem-related information such as problem state or title.
   * Optional Turn on **Accept any SSL certificate**.
   * Optional Turn on **Call webhook if new events merge into existing problems**.
   * Assign an [Alerting profile](/docs/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
5. Select **Send test notification** to make sure your webhook integration is working.
6. **Save changes**.

## Example JSON with placeholders

Here is a valid JSON web hook problem-notification definition example:

```
{



"ImpactedEntities": {ImpactedEntities},



"ImpactedEntity": "{ImpactedEntity}",



"PID": "{PID}",



"ProblemDetailsHTML": "{ProblemDetailsHTML}",



"ProblemDetailsJSON": {ProblemDetailsJSON},



"ProblemID": "{ProblemID}",



"ProblemImpact": "{ProblemImpact}",



"ProblemTitle": "{ProblemTitle}",



"Problem URL": "https://example.com",



"State": "{State}",



"Tags": "{Tags}"



}
```

`{ImpactedEntities}` and `{ProblemDetailsJSON}` are JSON data types and must not have quotes around them.

After a problem has been detected, the placeholders are populated with the actual values and results, as shown in this example payload:

```
{



"ImpactedEntities": [



{"type": "HOST", "name": "MyHost1", "entity": "HOST-XXXXXXXXXXXXX" },



{"type": "SERVICE", "name": "MyService1", "entity": "SERVICE-XXXXXXXXXXXXX"}



],



"ImpactedEntity": "MyHost1, MyService1",



"PID": "99999",



"ProblemDetailsHTML": "<h1>Dynatrace problem notification test run details</h1>",



"ProblemDetailsJSON": {"ID" : "99999" },



"ProblemID": "999",



"ProblemImpact": "INFRASTRUCTURE",



"ProblemTitle": "Dynatrace problem notification test run",



"Problem URL": "https://example.com",



"State": "OPEN",



"Tags": "testtag1, testtag2"



}
```

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration.md

---
title: Send Dynatrace notifications to xMatters
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration
scraped: 2026-02-18T21:16:23.079512
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

---

## analyze-explore-automate/notifications-and-alerting/problem-notifications.md

---
title: Problem notifications
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications
scraped: 2026-02-18T21:15:25.513232
---

# Problem notifications

# Problem notifications

* 2-min read
* Updated on Oct 10, 2022

Dynatrace provides full-stack monitoring insights into your complete IT operation and automatically detects if any part of your deployment doesnât fulfill the required quality in terms of performance or error rates. Whenever Dynatrace detects such abnormal system behavior, it creates a single problem that contains all incidents that share the same root cause.

Dynatrace enables you to automatically push problem notifications to your preferred third-party incident management or ChatOps service. Open problems are continuously updated based on evolving impact and correlating events. To avoid notification spam, problem notifications are only pushed to third-party systems when problems are initially detected and when they are ultimately resolved.

Incident management

ChatOps

Enterprise service management

Custom integrations

These systems help organizations manage large amounts of incidents across multiple teams. Incident management systems offer features such as incident-notification tracking, escalation-level definition, and on-duty schedules. Typically, incident management systems offer a wide range of notification channels, such as call centers, pagers, and mobile push notifications. Dynatrace offers out-of-the-box integrations for major incident management systems such as [Opsgenie](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration "Configure Opsgenie integration with Dynatrace."), [VictorOps](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration "Learn how to configure VictorOps integration with Dynatrace."), [PagerDuty](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration "Learn how to send problem notifications from Dynatrace to PagerDuty."), [xMatters](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration "Learn how to create problem notifications by adding an xMatters webhook URL from your xMatters instance to Dynatrace settings."), and [Jira](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration "Configure Jira integration with Dynatrace.").

[Jira](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/jira-integration) [Opsgenie](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/opsgenie-integration) [PagerDuty](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/pagerduty-integration) [Trello](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/trello-integration) [VictorOps](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/victorops-integration) [xMatters](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/xmatters-integration)

Today, chat systems are widely used by DevOps teams to triage incoming issues, discuss follow-up actions and to archive lessons learned. Dynatrace offers out-of-the-box integrations for popular ChatOps systems such as [Slack](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration "Set up a Slack problem-notification integration that can keep you updated on all Dynatrace problems.") and [Microsoft Teams](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration "Set up a Microsoft Teams problem-notification integration that can keep you updated on all Dynatrace-detected problems.").

[Microsoft Teams](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/microsoft-teams-integration) [Slack](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/slack-integration)

Enterprise service-management systems are widely used by large enterprises to organize all types of IT and non-IT related services and resources. These systems are used by companies to organize their IT services according to global standards, such as ITIL (Information Technology Infrastructure Library). All hardware and software service-related incidents are tracked and trigger workflows. Dynatrace offers a certified integration with [ServiceNow](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration "Connect your monitoring environment with your ServiceNow instance."), the most popular SaaS enterprise service-management system.

[ServiceNow](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration)

If Dynatrace doesnât yet offer an out-of-the-box integration for your specific system, you can set up an [email integration](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Get email whenever Dynatrace detects a problem in your environment that affects real users.") or [webhook integration](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration "Learn how to integrate problem-notifications using a custom webhook.").

[Email](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration) [Webhook](/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/webhook-integration)

---
