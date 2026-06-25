---
title: Settings API - IBM MQ queue managers schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ibmmq-queue-managers
scraped: 2026-05-12T11:49:34.739855
---

# Settings API - IBM MQ queue managers schema table

# Settings API - IBM MQ queue managers schema table

* Published Dec 05, 2023

### IBM MQ queue managers (`builtin:ibmmq.queue-managers)`

Dynatrace needs to know the IBM MQ definition of your alias queues, remote queues, and cluster queues for the end-to-end tracing. Without this information, Dynatrace can still trace all requests but producer and consumer services would not be stitched together.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ibmmq.queue-managers` | * `group:mainframe` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.queue-managers` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ibmmq.queue-managers` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ibmmq.queue-managers` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Queue manager name `name` | text | - | Required |
| Clusters `clusters` | set | Name of the cluster(s) this queue manager is part of | Required |
| Alias queues `aliasQueues` | Set<[AliasQueue](#AliasQueue)> | - | Required |
| Remote queues `remoteQueues` | Set<[RemoteQueue](#RemoteQueue)> | - | Required |
| Cluster queues `clusterQueues` | Set<[ClusterQueue](#ClusterQueue)> | - | Required |

##### The `AliasQueue` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Alias queue name `aliasQueue` | text | - | Required |
| Base queue name `baseQueue` | text | - | Required |
| Cluster visibility `clusterVisibility` | set | Name of the cluster(s) this alias should be visible in | Required |

##### The `RemoteQueue` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Local queue name `localQueue` | text | - | Required |
| Remote queue name `remoteQueue` | text | - | Required |
| Remote queue manager name `remoteQueueManager` | text | - | Required |
| Cluster visibility `clusterVisibility` | set | Name of the cluster(s) this local definition of the remote queue should be visible in | Required |

##### The `ClusterQueue` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Local queue name `localQueue` | text | - | Required |
| Cluster visibilities `clusterVisibility` | set | Name of the cluster(s) this local queue should be visible in | Required |