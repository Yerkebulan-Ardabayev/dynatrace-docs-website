---
title: NAM monitor metrics
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/nam-monitor-metrics
scraped: 2026-02-19T21:19:36.819125
---

# NAM monitor metrics

# NAM monitor metrics

* Explanation
* 12-min read
* Published Jun 19, 2024

## Metrics and dimensions

### Dimensions (all network availability monitors)

| Name | Type | Description | Example value |
| --- | --- | --- | --- |
| `dt.entity.multiprotocol_monitor` | string | Monitor ID (monitored entity ID) | `MULTIPROTOCOL_MONITOR-3F6C9D500287BBAF` |
| `dt.entity.synthetic_location` | string | Synthetic location ID (monitored entity ID) | `SYNTHETIC_LOCATION-A4F834D72840EFC1` |
| `dt.entity.host` | string | If available, monitored entity ID for target | `HOST-024C103F7F86A290` |
| `dt.maintenance_window_ids` | array | UUIDs of maintenance windows | `c715d677-eb1b-3e1b-8dbc-db06cad5b8eb` |
| `dt.synthetic.monitored_entity_ids` | array | IDs of monitored entities | `APPLICATION-EA7C4B59F27D43EB` |
| `dt.security_context` | string | The security context is used in access permissions to limit the visibility | `mySecurityContext` |
| `step.id` | numeric | Step sequential ID | `1` |
| `request.id` | numeric | Request sequential ID | `2` |
| `request.type` | string | Type of request | `icmp`, `tcp` |
| `request.target_address` | string | Address of target entity | `54.171.216.19` |
| `result.state` | string | Result state of monitor execution | `SUCCESS`, `FAIL` |
| `result.status.message` | string | Execution status | `HEALTHY`, `CONSTRAINT_VIOLATED` |
| `result.status.code` | numeric | Numeric representation of the execution status | `0`, `1401` |
| `interpolated` | boolean | Information whether monitor availability was interpolated | `false` |
| `multi_protocol.step.id` | numeric | Step sequential ID (deprecated, use `step.id`) | `1` |
| `multi_protocol.request.id` | numeric | Request sequential ID (deprecated, use `request.id`) | `2` |
| `multi_protocol.request.type` | string | Type of request (deprecated, use `request.type`) | `icmp`, `tcp` |
| `multi_protocol.request.target_address` | string | Address of target entity (deprecated, use `request.target_address`) | `54.171.216.19` |
| `multi_protocol.result.state` | string | Result state of monitor execution (deprecated, use `result.state`) | `SUCCESS` |
| `multi_protocol.result.status` | string | Execution status (deprecated, use `result.status.message`) | `HEALTHY`, `CONSTRAINT_VIOLATED` |
| `multi_protocol.result.status.code` | numeric | Numeric representation of the execution status (deprecated, use `result.status.code`) | `0`, `1401` |

### Monitor metrics (all network availability monitors)

| Name | Type | Dimensions | Description |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.availability` (latest Dynatrace) `builtin:synthetic.multiProtocol.availability` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `interpolated` | Availability calculated based on the execution status of visits - 100% for code=`0`: `HEALTHY`, `SCRIPT_FINISH`, `SKIPPED` - 0% for error status codes such as `1401 - CONSTRAINT_VIOLATED` |
| `dt.synthetic.multi_protocol.execution_time` (latest Dynatrace) `builtin:synthetic.multiProtocol.executionTime` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` | Duration between start and end time of visit execution (in milliseconds) Metric available only if visit execution took place; both start time and end time must be available. |
| `dt.synthetic.multi_protocol.executions` (latest Dynatrace) `builtin:synthetic.multiProtocol.executions` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `dt.maintenance_window_ids` `result.state` `result.status.code` `result.status.message` `multi_protocol.result.state` (deprecated, use `result.state`) `multi_protocol.result.status.code`(deprecated, use `result.status.code`) `multi_protocol.result.status` (deprecated, use `result.status.message`) | Number of monitor executions in time |
| `dt.synthetic.multi_protocol.success_rate` (latest Dynatrace) `builtin:synthetic.multiProtocol.successRate` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` | Ratio of executed steps that didn't fail (successes + skips) to all executed steps We take into account steps that were actually executed rather than steps intended to be executed. For example, with 2 successful steps, 1 failed step, and 8 not started, the ratio is 2/3, or 66.67%. |

### Step metrics (all network availability monitors)

| Name | Type | Dimensions | Description |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.step.availability` (latest Dynatrace) `builtin:synthetic.multiProtocol.step.availability` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.type` (deprecated, use `request.type`) | Availability calculated based on the execution status of steps - 100% for code=`0`: `HEALTHY`, `SCRIPT_FINISH`, `SKIPPED` - 0% for error status codes such as `1401 - CONSTRAINT_VIOLATED` |
| `dt.synthetic.multi_protocol.step.execution_time` (latest Dynatrace) `builtin:synthetic.multiProtocol.step.executionTime` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.type` (deprecated, use `request.type`) | Duration between start and end time of step execution (in milliseconds) Metric available only if step execution took place, with a well-defined end time; therefore, it's not available for [skipped](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#nam-setup "Learn how to set up a NAM monitor to check the performance and availability of your site.") steps. |
| `dt.synthetic.multi_protocol.step.executions` (latest Dynatrace) `builtin:synthetic.multiProtocol.step.executions` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.type` `result.state` `result.status.code` `result.status.message` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.type` (deprecated, use `request.type`) `multi_protocol.result.state` (deprecated, use `result.state`) `multi_protocol.result.status` (deprecated, use `result.status.message`) `multi_protocol.result.status.code`(deprecated, use `result.status.code`) | Number of step executions in time |
| `dt.synthetic.multi_protocol.step.success_rate` (latest Dynatrace) `builtin:synthetic.multiProtocol.step.successRate` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.type` (deprecated, use `request.type`) | Ratio of executed requests that didn't fail to all executed requests. If a step doesn't have executed requests (because [nothing matches](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#nam-setup "Learn how to set up a NAM monitor to check the performance and availability of your site.") its definition in a monitor configuration), we return the value 100%. For example, with 2 successful requests and 1 failed request, the ratio is 2/3, or 66.67%. |

### Request metrics (all network availability monitors)

| Name | Type | Dimensions | Description |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.request.availability` (latest Dynatrace) `builtin:synthetic.multiProtocol.request.availability` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) | Availability calculated based on the execution status of requests - 100% for code=`0`: `HEALTHY`, `SCRIPT_FINISH`, `SKIPPED` - 0% for error status codes such as `1401 - CONSTRAINT_VIOLATED` |
| `dt.synthetic.multi_protocol.request.executions` (latest Dynatrace) `builtin:synthetic.multiProtocol.request.executions` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `result.state` `result.status.code` `result.status.message` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) `multi_protocol.result.state` (deprecated, use `result.state`) `multi_protocol.result.status` (deprecated, use `result.status.message`) `multi_protocol.result.status.code`(deprecated, use `result.status.code`) | Number of request executions in time |

### ICMP monitor metrics

| Name | Type | Dimensions | Description |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.icmp.success_rate` (latest Dynatrace) `builtin:synthetic.multiProtocol.icmp.successRate` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) | Ratio of received packets to sent packets Doesn't take into account the configured number of packets to be sent. For example, out of 10 packets to be sent, if 5 were sent and 4 were received, the ratio is 4/5, or 80.00%. |
| `dt.synthetic.multi_protocol.icmp.packets_sent` (latest Dynatrace) `builtin:synthetic.multiProtocol.icmp.packetsSent` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) | Total number of packets sent |
| `dt.synthetic.multi_protocol.icmp.packets_received` (latest Dynatrace) `builtin:synthetic.multiProtocol.icmp.packetsReceived` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) | Number of packets that were returned successfully |
| `dt.synthetic.multi_protocol.icmp.round_trip_time` (latest Dynatrace) `builtin:synthetic.multiProtocol.icmp.roundTripTime` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) | Round-Trip Time for received packets |
| `dt.synthetic.multi_protocol.icmp.request_execution_time` (latest Dynatrace) `builtin:synthetic.multiProtocol.icmp.requestExecutionTime` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) | Duration between start and end time of request handling (in milliseconds) This metric is always provided, even if actual request execution did not take place (for example, because of exceptions or timeouts). Diagnostic metricâallows for validation of external ping process execution time. |

### TCP monitor dimensions

| Name | Type | Description | Example value |
| --- | --- | --- | --- |
| `request.tcp_port_number` | string | TCP request port number, as provided in monitor configuration | `665` |
| `multi_protocol.request.tcp_port_number` | string | TCP request port number, as provided in monitor configuration (deprecated, use `request.tcp_port_number`) | `665` |

### TCP monitor metrics

| Name | Type | Dimensions | Description |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.tcp.connection_time` (latest Dynatrace) `builtin:synthetic.multiProtocol.tcp.connectionTime` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) `request.tcp_port_number` `multi_protocol.request.tcp_port_number` (deprecated, use: `request.tcp_port_number`) | Duration between start time (socket creation and connection) and end time (when confection is successfully established) in milliseconds Metric available only if request execution took place (with no exceptions or timeouts), with a well-defined end time |

### DNS monitor dimensions

| Name | Type | Description | Example value |
| --- | --- | --- | --- |
| `request.dns_record_type` | string | DNS record type to be queried by request, as provided in configuration | `A`, `AAAA`, `CNAME` |
| `multi_protocol.request.dns_record_type` | string | DNS record type to be queried by request, as provided in configuration (deprecated, use `request.dns_record_type`) | `A`, `AAAA`, `CNAME` |

### DNS monitor metrics

| Name | Type | Dimensions | Description |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.dns.resolution_time` (latest Dynatrace) `builtin:synthetic.multiProtocol.dns.resolutionTime` (previous Dynatrace) | numeric | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (only for monitors with filter defined) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (deprecated, use `step.id`) `multi_protocol.request.id` (deprecated, use `request.id`) `multi_protocol.request.target_address` (deprecated, use `request.target.address`) `multi_protocol.request.type` (deprecated, use `request.type`) `request.dns_record_type` `multi_protocol.request.dns_record_type` (deprecated, use: request.dns\_record\_type) | Duration between start and end time of the request to the DNS server, in milliseconds Metric available only if request execution took place (with no exceptions or timeouts), with a well-defined end time |

## DQL queries to extract data

Use [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") queries to extract data with metrics and dimensions.

The following examples use [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") to demonstrate how to work with the results of network availability monitors. They use result metrics as a starting point to explore possibilities of extracting and interpreting data with DQL.

### Host entity status for ICMP requests

The monitor `MULTIPROTOCOL_MONITOR-5C2F92334DF71A90` executes ICMP requests and filters monitored hosts with `"targetFilter": "hostGroup == e2e-synthetic-private-location"` (which resolves to about 26 hosts).

By using the `dt.synthetic.multi_protocol.request.executions` metric and splitting it by the `dt.entity.host` and `result.status.message` dimensions, we can display the status of the connection to a particular monitored host entity in this host group. Some hosts do not fulfill the expected success rate; instead of being `HEALTHY`, their requests are marked as `CONSTRAINT_VIOLATED`.

```
Timeseries status = avg(dt.synthetic.multi_protocol.request.executions),



by:{dt.entity.host, result.status.message},



filter: dt.entity.multiprotocol_monitor == "MULTIPROTOCOL_MONITOR-5C2F92334DF71A90"
```

![Host entity status for ICMP requests](https://dt-cdn.net/images/nam-tcp-connect-ports-notebooks-dql-1920-06e2eeb631.webp)

### Number of ICMP packets sent and received

The monitor `MULTIPROTOCOL_MONITOR-548C3CD54183CED9` executes ICMP requests to hosts with the explicitly defined IP addresses, `18.x.x.x`, `10.x.x.x`, and `34.x.x.x`. Each of these IP addresses maps to a distinct host.

We use the sum of the `dt.synthetic.multi_protocol.icmp.packets_sent` and the sum of the `dt.synthetic.multi_protocol.icmp.packets_received` metrics to get insight into how many packets were sent and received.

We split results by the `request.target_address` dimension and filter data for `18.x.x.x` and `10.x.x.x` only.

For `18.x.x.x`, the same number of packets were received as were sent, but for `10.x.x.x`, all packets are lost and none were received.

```
timeseries {



packets_sent = sum(dt.synthetic.multi_protocol.icmp.packets_sent),



packets_received= sum(dt.synthetic.multi_protocol.icmp.packets_received)



},



by:{request.target_address},



filter: dt.entity.multiprotocol_monitor == "MULTIPROTOCOL_MONITOR-548C3CD54183CED9"



AND (



request.target_address == "18.x.x.x"



OR request.target_address == "10.x.x.x"



)
```

![ICMP packets sent and received](https://dt-cdn.net/images/nam-icmp-packets-notebooks-dql-1638-3577d87f09.webp)

### Target status for TCP requests

The monitor `MULTIPROTOCOL_MONITOR-74E68F22FF5E9227` executes TCP requests to hosts from a host group that resolves to the IP addresses `18.x.x.x`, `34.x.x.x`, and `44.x.x.x`.

To display the status of the TCP connection for an IP-port pair, we use the `dt.synthetic.multi_protocol.request.executions` metric and splitting it by the dimensions:

* `request.target_address`
* `request.tcp_port_number`
* `result.status.message`

In this example:

* Each host has the ports `22` (SSH) and `8080` (HTTP server) open, and each connection to the hosts on these ports succeeds with the `HEALTHY` status.
* No service uses the standard HTTP port `80`. Therefore, connections to all hosts on that port fail with the `TCP socket connection error` status.

Note that results of this query can be limited to just successful requests by filtering by the `multi_protocol.result.status.code` dimension (`code == 0`).

```
timeseries status = sum(dt.synthetic.multi_protocol.request.executions),



by: {request.target_address, request.tcp_port_number, result.status.message},



filter: dt.entity.multiprotocol_monitor == "MULTIPROTOCOL_MONITOR-74E68F22FF5E9227"



//  and result.status.code == 0
```

![Target status for TCP requests](https://dt-cdn.net/images/nam-target-status-tcp-requests-notebooks-dql-1727-4326a4411c.webp)

### TCP connection time to target port

The monitor `MULTIPROTOCOL_MONITOR-74E68F22FF5E9227` executes TCP requests to hosts from a host group that resolves to the IP addresses `18.x.x.x`, `34.x.x.x`, and `44.x.x.x`.

In this example, instead of IP addresses, we split the results by monitored host entity IDs.

To check typical time taken for a successful connection to the target port for a host, we use the average of the `dt.synthetic.multi_protocol.tcp.connection_time` metric split by the dimensions:

* `dt.entity.host`
* `request.target_address`
* `request.tcp_port_number`

Only ports `22` (SSH) and `8080` (HTTP server) are open, and these are the only ports for which `dt.synthetic.multi_protocol.tcp.connection_time` is available. The hosts are effectively in different geographical locations (Ohio, Oregon, and North Virginia in the United States), so a difference in connection times is expected.

```
timeseries duration = avg(dt.synthetic.multi_protocol.tcp.connection_time),



by:{dt.entity.host, request.target_address, request.tcp_port_number},



filter: dt.entity.multiprotocol_monitor == "MULTIPROTOCOL_MONITOR-74E68F22FF5E9227"
```

![TCP connection time to target port](https://dt-cdn.net/images/nam-tcp-connect-time-notebooks-dql-1720-3e3235b23d.webp)

## Execution statuses

### All network availability monitors

| Code / message | Example | Description |
| --- | --- | --- |
| `0 HEALTHY` | - | All is well. |
| `-1 UNEXPECTED_ERROR` | Resource saturation | Unexpected problem that's usually related to monitor's execution components. |
| `1401 CONSTRAINT_VIOLATED` | - | Constraint conditions that were defined in monitor's configuration were not met. |
| `1604 VALIDATION_ERROR` | - | Improper monitor configuration detected. |
| `12013 UNKNOWN_HOST` | Error in the hostname | IP address of the host cannot be determined. Possible causes: - Invalid hostname - DNS server unreachable - DNS cache issues - Firewall or proxy interference |
| `12033 Execution timeout` | Server operates slowly. | Timeout of request execution. Possible causes: - Network issues - Slow or unresponsive server or service - Connection blocked by firewall rules - Timeout is too small. |

### TCP monitor execution statuses

| Code / message | Example | Description |
| --- | --- | --- |
| `22000 TCP socket connection error` | Service is not listening on a specified port. | This status means that the host was identified and available but the TCP connection could not be established or was unexpectedly closed. Additional explanation for the exact exception is provided. The status is used if a `java.net.SocketException` is thrown during the connection attempt. Possible causes: - Service is not listening on the specified port. - Service reached resource or connection limit. - Service became unavailable during the socket connection process. |