---
title: Set up IBM MQ tracing on z/OS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/ibm-mq-monitoring
scraped: 2026-02-21T21:17:12.321533
---

# Set up IBM MQ tracing on z/OS

# Set up IBM MQ tracing on z/OS

* Latest Dynatrace
* 1-min read
* Updated on May 16, 2022

With Dynatrace you can get observability for IBM MQ on z/OS:

* The CICS, IMS, and z/OS Java modules can trace messages in your applications initiated by IBM MQ clients, including their producer and consumer services across tiers. To learn more about messages queues in Dynatrace, see [Queues](/docs/observe/infrastructure-observability/queues "Monitor and analyze your message queues with Dynatrace.").
* The ActiveGate extension can collect metrics from IBM MQ servers. To learn more about it, see [IBM MQ ActiveGate extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.").

## Tracing

Dynatrace can automatically create a continuous [service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") for IBM MQ when the producer and consumer services use the same queue or topic name. If the producer and consumer services refer to different queue or topic names, IBM MQ configuration might be required to create a continuous service flow.

Without IBM MQ configuration, Dynatrace can still trace all messages, but the service flow will be broken.

The table lists the available IBM MQ configuration items for queues and topics.

Item

Description

Your action

Queue manager

Queue manager with its queues

Define your queue managers, including alias queues, remote queues, and cluster queues within a single configuration item.

z/OS Queue sharing group

Group of queue managers that access the same shared queues

Specify which queue managers and shared queues belong to a queue-sharing group within a single configuration item.

z/OS IMS bridge

The IBM MQ component that allows direct access to the IMS system

Specify which queue managers and queues belong to an IMS bridge within a single configuration item.

## Manage IBM MQ configuration

You can manage an IBM MQ configuration automatically by installing an [IBM MQ extension](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") and activating **Retrieve topology for improved transaction tracing** to retrieve the IBM MQ configuration of your environment and send it to the Settings API. This can also be done manually via the web UI or the Settings API.

### Manual configuration via web UI

To manage the IBM MQ configuration via the Dynatrace web UI, go to **Settings** > **Mainframe** to find the following menu options:

* IBM MQ queue managers
* IBM MQ queue sharing groups
* IBM MQ IMS bridges

### Manual configuration via Settings API

You can manage the IBM MQ configuration via the Dynatrace [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

Settings API for IBM MQ tracing:

* [Create queue manager configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qm-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Update queue manager configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qm-api-update "Configure Dynatrace for IBM MQ tracing.")
* [Create queue sharing group configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qsg-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Update queue sharing group configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qsg-api-update "Configure Dynatrace for IBM MQ tracing.")
* [Create IMS bridge configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#ims-bridge-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Update IMS bridge configuration](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#ims-bridge-api-update "Configure Dynatrace for IBM MQ tracing.")

## Related topics

* [IBM MQ tracing](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing "Configure Dynatrace for IBM MQ tracing.")