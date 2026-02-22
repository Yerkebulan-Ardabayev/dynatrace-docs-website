---
title: Send Dynatrace notifications to ServiceNow
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration
scraped: 2026-02-22T21:08:18.929671
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