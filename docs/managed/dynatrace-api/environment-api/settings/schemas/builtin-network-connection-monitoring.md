---
title: Settings API - Network connection monitoring schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-network-connection-monitoring
---

# Settings API - Network connection monitoring schema table

# Settings API - Network connection monitoring schema table

* Published Sep 25, 2025

### Network connection monitoring (`builtin:network-connection-monitoring)`

OneAgent automatically monitors the critical network traffic on your hosts. These settings can be overridden at a host group and host level.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:network-connection-monitoring` | * `group:network-and-discovery` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:network-connection-monitoring` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:network-connection-monitoring` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:network-connection-monitoring` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable OneAgent network connection monitoring `enabled` | boolean | When disabled, OneAgent will not collect network data about critical traffic. Enabled by default. Consumes Events powered by Grail licensing. Requires OneAgent version 1.337+ | Required |
| IP Filter `ipFilterMode` | enum | Choose which IP addresses will be included in network connection monitoring. Available options: all, public traffic only (all globally routable addresses), private traffic only (addresses within IPv4 or IPv6 Private Address Ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, fd00::/8), custom exclusion, or custom inclusion The element has these enums * `all` * `private` * `public` * `inclusion` * `exclusion` | Required |
| IP addresses: `IPaddresses` | text | Use comma separated CIDR notation, e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16  IP addresses to include or exclude | Required |
| Reported connections `reportedConnections` | enum | Defines which connections should be reported. Defaults to Critical connections, which reports only connection refused for new connections and connection reset for existing. Optionally, log all connections or set custom thresholds. The element has these enums * `all` * `auto` * `custom` | Required |
| Reported connections thresholds `reportedConnectionsThresholds` | [reportedConnectionsThresholds](#reportedConnectionsThresholds) | If any of the thresholds are exceeded, then connection is reported. | Required |
| Aggregation `aggregation` | [aggregationParams](#aggregationParams) | - | Required |
| Enable classic OneAgent process connection monitoring `enabledClassic` | boolean | Classic OneAgent process connection monitoring is not compatible with Grail and will be removed at a later time. These metrics are only used on the Process Connections screen within Classic Host Networking. Defaults to off. | Required |

##### The `reportedConnectionsThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Bytes threshold [bytes] `bytesThreshold` | integer | - | Required |
| Connectivity threshold [%] `connectivityThreshold` | float | - | Required |
| Retransmissions threshold [%] `retransmissionsThreshold` | float | - | Required |
| RTT (round trip time) threshold [ms] `rttThreshold` | integer | - | Required |

##### The `aggregationParams` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Aggregation interval [min.] `interval` | integer | Aggregate similar connections records across an interval. Allowed range: 1-10 min.  Aggregate similar connection records across an interval. For example, 20 connections from the same source process to the same destination IP and port, would be aggregated into one log with count=20. 1 minute is the default and recommended. | Required |
| Rate limit `rateLimit` | integer | Rate limit for connections reported per host per minute. Default 100. | Required |