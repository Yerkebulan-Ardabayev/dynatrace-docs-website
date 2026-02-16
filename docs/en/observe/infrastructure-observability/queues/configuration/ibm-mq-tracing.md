---
title: IBM MQ tracing
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing
scraped: 2026-02-16T09:33:37.740595
---

# IBM MQ tracing

# IBM MQ tracing

* How-to guide
* 6-min read
* Updated on Jun 21, 2022

Dynatrace can automatically create a continuous [service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") for IBM MQ when the producer and consumer services use the same queue or topic name. If the producer and consumer services refer to different queue or topic names, IBM MQ configuration might be required to create a continuous service flow.

Without IBM MQ configuration, Dynatrace can still trace all messages, but the service flow will be broken.

Technology

IBM MQ message

IBM MQ configuration required

z/OS Java .NET

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

IBM App Connect EnterpriseIBM Integration Bus

`MQRFH2.usr` folder not present

`MQRFH2.usr` folder present

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

IBM MQ continuous service flow example

![IBM MQ service flow](https://dt-cdn.net/images/ibm-mq-service-flow-1938-06750bfc7d.png)

IBM MQ distributed trace example

![IMB MQ distributed trace](https://dt-cdn.net/images/ibmmq-distributed-traces-3772-59101a2b00.png)

### FAQ

Should I create the MQRFH2 header when it is not present in my IBM MQ messages?

We recommend that you create the `MQRFH2` header for IBM MQ messages. The presence of the `MQRFH2` header in your IBM MQ messages allows Dynatrace to use [identifiers instead of unique keys](/docs/observe/infrastructure-observability/queues/queue-concepts#producer-consumer-service "Basic concepts of message queue monitoring in Dynatrace.") to trace messages across queues and topics of IBM App Connect Enterprise and IBM Integration Bus.

Benefits of creating the `MQRFH2` header for IBM MQ messages include:

* Consistent [Adaptive Traffic Management](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.") across your monitoring environment, lowering the volume on IBM MQ traces.
* An accurate and continuous service flow without the need to configure IBM MQ mapping when the messages are solely processed by IBM App Connect Enterprise and IBM Integration Bus.

How can I create the MQRFH2 header when it is not present in my IBM MQ messages?

When the `MQRFH2` header is present in your messages before an `MQOutput` node is called by IBM App Connect Enterprise or IBM Integration Bus, Dynatrace uses [identifiers instead of unique keys](/docs/observe/infrastructure-observability/queues/queue-concepts#producer-consumer-service "Basic concepts of message queue monitoring in Dynatrace.") to trace IBM MQ messages.

If this isn't the case in your environment, you can create an empty `MQRFH2` header by, for example, executing the following ESQL command by a preceding `Compute` node

```
CREATE LASTCHILD of OutputRoot DOMAIN 'MQRFH2';
```

For Dynatrace, an empty `MQRFH2` header is enough to automatically create the `usr` folder and to add Dynatrace identifiers to it. If a `usr` folder is already present, Dynatrace reuses it.

Specifications

* Dynatrace creates the `usr` folder within the existing `MQRFH2` header, not the `MQRFH2` header itself.
* When creating the `usr` folder, Dynatrace adds it at the beginning of the `MQRFH2` header.
* If the `usr` folder exists, Dynatrace adds its identifiers at the beginning of the `usr` folder.

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

## Configuration items

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

Follow the procedures below to create or update a configuration item. Note that the scope of these items is always an environment. Before starting, learn the format of the settings object by querying its schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") call.

Create a configuration item

Update an existing configuration item

### New queue manager

The ID of the queue manager schema is `builtin:ibmmq.queue-managers`.

1. Create the JSON object for your settings.

   The `aliasQueues` object can be a local queue owned by this queue manager, a local definition of a remote queue, or a cluster queue visible by this queue manager but owned by another queue manager.

   Example JSON

   ```
   [



   {



   "schemaId": "builtin:ibmmq.queue-managers",



   "scope": "environment",



   "value": {



   "name": "Queue Manager 1",



   "clusters": [



   "Name of the cluster this Queue Manager 1 is part of"



   ],



   "aliasQueues": [



   {



   "aliasQueue": "Alias Queue",



   "baseQueue": "Base queue which the Alias Queue should point to",



   "clusterVisibility": [



   "Name of a cluster this Alias Queue should be visible in (the queue manager must be part of this cluster)"



   ]



   }



   ],



   "remoteQueues": [



   {



   "localQueue": "Local definition of the Remote Queue",



   "remoteQueue": "Remote Queue",



   "remoteQueueManager": "Remote Queue Manager",



   "clusterVisibility": [



   "Name of a cluster this local definition of the Remote Queue should be visible in (the queue manager must be part of this cluster)"



   ]



   }



   ],



   "clusterQueues": [



   {



   "localQueue": "Local Queue",



   "clusterVisibility": [



   "Name of a cluster this Local Queue should be visible in (the queue manager must be part of this cluster)"



   ]



   }



   ]



   }



   }



   ]
   ```
2. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### New queue sharing group

The ID of the queue sharing group schema is `builtin:ibmmq.queue-sharing-group`.

1. Create the JSON object for your settings.

   Example JSON

   ```
   [



   {



   "schemaId": "builtin:ibmmq.queue-sharing-group",



   "scope": "environment",



   "value": {



   "name": "Queue Sharing Group",



   "queueManagers": [



   "Queue Manager 1",



   "Queue Manager 2"



   ],



   "sharedQueues": [



   "Shared Queue 1",



   "Shared Queue 2"



   ]



   }



   }



   ]
   ```
2. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### New IMS bridge

The ID of the IMS bridge schema is `builtin:ibmmq.ims-bridges`.

1. Create the JSON object for your settings.

   Example JSON

   ```
   [



   {



   "schemaId": "builtin:ibmmq.ims-bridges",



   "scope": "environment",



   "value": {



   "name": "IMS Bridge",



   "queueManagers": [



   {



   "name": "Queue Manager",



   "queueManagerQueue": [



   "Queue 1",



   "Queue 2"



   ]



   }



   ]



   }



   }



   ]
   ```
2. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update queue manager

The ID of the queue manager schema is `builtin:ibmmq.queue-managers`.

The `aliasQueues` object can be a local queue owned by this queue manager, a local definition of a remote queue, or a cluster queue visible by this queue manager but owned by another queue manager.

1. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
2. Create the JSON for your update.

   * Use the **updateToken** value from the previous step.
   * Modify the values as needed.

     Example JSON

     ```
     {



     "updateToken": "vu9U3hXY3q0ATAAkMG",



     "value": {



     "name": "Queue Manager A",



     "clusters": [



     "Name of a cluster this Queue Manager A is part of"



     ],



     "aliasQueues": [



     {



     "aliasQueue": "Alias Queue",



     "baseQueue": "Base queue which the Alias Queue should point to",



     "clusterVisibility": [



     "Name of a cluster this Alias Queue should be visible in (the queue manager must be part of this cluster)"



     ]



     }



     ],



     "remoteQueues": [



     {



     "localQueue": "Local definition of the Remote Queue",



     "remoteQueue": "Remote Queue",



     "remoteQueueManager": "Remote Queue Manager",



     "clusterVisibility": [



     "Name of a cluster this local definition of the Remote Queue should be visible in (the queue manager must be part of this cluster)"



     ]



     }



     ],



     "clusterQueues": [



     {



     "localQueue": "Local Queue",



     "clusterVisibility": [



     "Name of a cluster this Local Queue should be visible in (the queue manager must be part of this cluster)"



     ]



     }



     ]



     }



     }
     ```
3. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update sharing group

The ID of the queue sharing group schema is `builtin:ibmmq.queue-sharing-group`.

1. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
2. Create the JSON for your update.

   * Use the **updateToken** value from the previous step.
   * Modify the values as needed.
     Example JSON

     ```
     {



     "updateToken": "vu9U3hXY3q0ATAAkMG",



     "value": {



     "name": "Queue Sharing Group",



     "queueManagers": [



     "Queue Manager A",



     "Queue Manager B"



     ],



     "sharedQueues": [



     "Shared Queue A",



     "Shared Queue B"



     ]



     }



     }
     ```
3. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

### Update IMS bridge

The ID of the IMS bridge schema is `builtin:ibmmq.ims-bridges`.

1. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
2. Create the JSON for your update.

   * Use the **updateToken** value from the previous step.
   * Modify the values as needed.

     Example JSON

     ```
     {



     "updateToken": "vu9U3hXY3q0ATAAkMG",



     "value": {



     "name": "IMS Bridge",



     "queueManagers": [



     {



     "name": "Queue Manager",



     "queueManagerQueue": [



     "Queue A",



     "Queue B"



     ]



     }



     ]



     }



     }
     ```
3. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") endpoint to send your configuration.

## Related topics

* [Set up IBM MQ tracing on z/OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/ibm-mq-monitoring "Trace IBM MQ messages with Dynatrace on z/OS.")