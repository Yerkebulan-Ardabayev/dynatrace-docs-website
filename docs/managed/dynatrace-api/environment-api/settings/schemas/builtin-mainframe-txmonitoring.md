---
title: Settings API - Transaction monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-mainframe-txmonitoring
---

# Settings API - Transaction monitoring schema table

# Settings API - Transaction monitoring schema table

* Published Dec 05, 2023

### Transaction monitoring (`builtin:mainframe.txmonitoring)`

Define additional monitoring settings for CICS and IMS transactions.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:mainframe.txmonitoring` | * `group:mainframe` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.txmonitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:mainframe.txmonitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.txmonitoring` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor all incoming web requests `monitorAllIncomingWebRequests` | boolean | Dynatrace automatically traces incoming web requests when they are called by already-monitored services. Enable this setting to monitor all incoming web requests. We recommend enabling it only over a short period of time. | Required |
| Monitor all EXCI requests from CICS Transaction Gateway `monitorAllCtgProtocols` | boolean | If enabled, the CICS Transaction Gateway sensor will trace all EXCI requests including those that are using the TCP/IP or SNA protocol. | Required |
| Group CICS regions that belong to the same CICSPlex `groupCicsRegions` | boolean | If enabled, CICS regions belonging to the same CICSPlex will be grouped into a single process group. If disabled, a process group will be created for each CICS region. | Required |
| Create CICS services based on transaction IDs `zosCicsServiceDetectionUsesTransactionId` | boolean | If enabled, a CICS service will be created for each monitored transaction ID within a process group. If disabled, a CICS service will be created for each monitored CICS region within a process group. We recommend enabling it only when the CICS regions are grouped by their CICSPlex. | Required |
| Group IMS regions that belong to the same subsystem `groupImsRegions` | boolean | If enabled, IMS regions belonging to the same subsystem will be grouped into a single process group. If disabled, a process group will be created for each IMS region. | Required |
| Create IMS services based on transaction IDs `zosImsServiceDetectionUsesTransactionId` | boolean | If enabled, an IMS service will be created for each monitored transaction ID within a process group. If disabled, an IMS service will be created for each monitored IMS region within a process group. We recommend enabling it only when the IMS regions are grouped by their subsystem. | Required |
| PurePath node limit: maximum number of nodes per CICS/IMS program call `nodeLimit` | integer | We recommend the default limit of 500 nodes. The value 0 means unlimited number of nodes. | Required |