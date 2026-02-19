---
title: Configure a NAM monitor
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor
scraped: 2026-02-19T21:32:17.634830
---

# Configure a NAM monitor

# Configure a NAM monitor

* How-to guide
* 1-min read
* Updated on Jan 19, 2026

With network availability monitors (NAM), you can check the availability of your hosts, devices, and services.

There are three types of NAM monitors: ICMP, TCP, and DNS. To learn more about them, see [NAM types](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/network-availability-monitoring#NAM-types "ICMP, TCP, and DNS synthetic monitors").
You can create NAM monitors in [![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") Synthetic](#monitor-configuration) in latest Dynatrace or through [API](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#nam-api "Learn how to set up a NAM monitor to check the performance and availability of your site.").

## NAM setup

With NAM monitors, you can include more than one step.

* Each step can contain one or multiple requests.
* Like for HTTP and browser monitors, steps are executed sequentially.
* Unlike for HTTP and browser monitors, NAM monitors can contain multiple requests within a single step. All requests assigned to a particular step are executed in parallel. If one request fails, it doesn't affect the execution of other requests within that step.
* A step is skipped if nothing matches its definition in a monitor configuration. For example, when a tag is specified in the [target filters](#target-filter) list but nothing matches the tag.
* Concept of requests executed in parallel exists for NAM monitors only

For example, if you want to monitor a group of 4 hosts with an ICMP test, you want to apply the same conditions (such as frequency, location executing test, and number of packets) for each host from your group.

NAM offers you the possibility of addressing this in multiple ways:

* You can define 4 separate tests, one per host. The benefit of this approach is that Dynatrace triggers a separate problem for each host and you can assign separate notifications for each one. You can also adjust test parameters for each host separately.
* You can define a single test with 4 requests (within 1 step). The same ICMP checks are executed, but there will be differences in reporting and alerting. The number or percentage of hosts that are down is reported with the Requests Success rate metric. You can configure a customized threshold for failing the whole monitor. For example, if it's OK that 1 out of 4 hosts is down, because of rolling out an update, you can define it on the `>=75%` level. There's always a single problem generated for a monitor, yet still, it contains detailed info about hosts that don't respond. Another benefit of this approach is easier maintenance (adjusting single setting for all 4 hosts).

  Finally, filters offer defining tests against dynamically changing structure, for example if you want to define ICMP tests against a given host group, you don't need to adjust the NAM monitor test after the host group configuration change.

You need to define constraints for each monitor. Constraints are conditions that need to be met to consider the monitorâs execution successful. It is obligatory to define the **Success rate** constraint. See [step-level constraints](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#step-level-constraints "Learn how to set up a NAM monitor to check the performance and availability of your site.") to learn more.

## Create a NAM monitor

To create a NAM monitor in latest Dynatrace

1. Go to ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic** and select **Create monitor**.
2. Follow the on-screen steps as outlined in the sections below.

### Select type

The **Create synthetic monitor** page shows the types of synthetic monitor you can create.

Select **Network monitor (NAM)** to get started.

### General

* Required **Name this monitor**âThe name of the monitor as it will be displayed in the web UI (up to 500 characters).
* Required **Select a protocol**âChoose the monitor type: `DNS`, `ICMP`, or `TCP`.
* Optional **Set a description**âDescribe your monitor.
* Optional **Add tags to this monitor**âTo manually create a new tag, select **Add tag**, type the key, optionally provide a value, and select **Add**.

After you specify the general settings, select **Continue**.

### Requests

The **Requests** section has two editing modes. You can switch back and forth between these modes.

* default **Visual**âto view and configure NAM requests through web UI settings.
* **Script**âto view and edit request settings as JSON. The script you provide also serves as payload for API requests.

Settings per request (you can add multiple requests) are:

* Required **Request name**âThe name of the request.
* Required **List of targets** or **Filter expression**

  + You can provide targets for requests as an explicit list, or filter monitored hosts using a filter expression.

    - If you want to provide targets as IP or domain names, use **List of targets** to specify a comma-separated list of targets. Use this to monitor single or multiple hosts, devices, or services.
    - If you want to select some of the monitored hosts or custom devices, use **Filter expression** to specify a filter expression. This allows you to monitor a group of hosts or custom devices that meet the filter criteria. To learn more about available filters, see [target filter](#target-filter).

    You can combine both the **List of targets** and the **Filter expression** in a single monitor step. When used together, the monitor step will include the combined set of targets from both fields.
* Required **Execution attributes**âExecution attributes are essentially key/value pairs that are associated with your request. Define **Request timeout**, **Number of packets**, **Data length**, **Time to live**, **Timeout to reply**, you can also turn on or turn off **Do not fragment data**. Execution attributes are available for ICMP only.
* Required **Constraints**âConstraints are conditions that need to be met to consider monitorâs execution successful. You need to define **Constraint type**, **Operator** and **value**.

If you want to create another request, select **Add next request** and specify the above for the next request.

Use **Duplicate** ![Duplicate](https://dt-cdn.net/images/dashboards-app-tile-duplicate-f0d63fb901.svg "Duplicate") to duplicate a request and then edit it from that point instead of starting from scratch each time you add a request.

After you specify all requests, select **Continue**.

### Frequency and locations

In the **Frequency and locations** section, specify the frequency and locations.

* Required **Select frequency**âYou can choose a frequency (every `1 min`, `2 min`, `5 min`, `10 min`, `15 min`, `30 min`, or `1 h`) or select `On demand only` for manual execution.
* Required **n selected locations**âSpecify one or more locations.

After you specify the frequency and locations, select **Continue**.

### Outage and Performance

In **Outage handling**, you can enable and configure the following settings related to problem and alert generation:

* Optional "Generate a problem and send an alert when the monitor is unavailable at all configured locations (global outage)."
* Optional "Generate a problem and send an alert when the monitor is unavailable only when at least two locations are assigned." Note that this option is only possible if you selected two or more locations.
* Optional "Generate a problem and send an alert on performance threshold violations."

After you specify the outage and performance settings, select **Continue**.

### Summary

In the **Summary** section, verify your settings.

After you review the summary, select **Save** to create your monitor or **Back** to go back and adjust your monitor settings.

## Target filter

Target filter gives an option to filter **hosts monitored by Dynatrace** or **custom devices having IP addresses**. With this filter, you can select those two types of targets based on:

* type (`type`)
* tags (`tag`)
* host ID (`hostId`) (deprecated, works for hosts only, use entity ID instead)
* entity ID (`entityId`)
* host groups (`hostGroup`)
* management zones (`managementZone`)
* IP mask (`ipMask`)
* IP range (`ipRange`)
* process group instance (`processGroupInstance`)
* network interfaces of particular custom device (`interfacesOf`)
* extension name (`extensionName`)

IP range and IP mask are filters for hosts or devices known for the Dynatrace server, not an option to scan the network.

### Syntax

* Logical operators: `AND` and `OR` (case insensitive)
* Parentheses
* Expression operators: `==` and `!=`
* Tag names and values
* Negation ("not"): `!=`.
* Wildcard: `*` (selects all hosts monitored by Dynatrace)

### Examples

* `tag == tagname or hostGroup == group1`
* `(tag == tagname1:tagvalue1 or tag == tagname1:tagvalue2) and (hostGroup == group1 or managementZone == zone1)`
* `tag != tagname1 and tag != tagname2:tagvalue`
* `tag == tagname:tagvalue and (managementZone == zone1 or managementZone == zone2)`
* `tag == "[tagwithbrackets and spaces]":"value, with, commas, and, spaces"`
* `ipMask == 127.0.0.1/24`
* `hostId == HOST-000123`
* `type == CUSTOM_DEVICE and ipMask == 172.17.0.2/24`
* `entityId == HOST-045BFCDA3F507D30 or entityId == CUSTOM_DEVICE-13081D4B74B3E2C8`
* `type == HOST and processGroupInstance == PROCESS_GROUP_INSTANCE-07611353BB98908C`
* `type == CUSTOM_DEVICE and interfacesOf == CUSTOM_DEVICE-E1A88946BF04D5E7`
* `type == CUSTOM_DEVICE and extensionName == "Docker devices"`

## Performance thresholds



The performance threshold metric is compared to metric calculated for each request within monitor/step. For example, if TCP port check monitor, tests on the same host port `80` and `443` separately, Dynatrace compares threshold TCP connection establishment time twice, once for port `80` and once for port `443`.

There are three performance metrics for three types of NAM monitors:

* RTT for ICMP
* TCP connection establishment time for TCP
* DNS resolution time for DNS

Violating defined performance triggers a Problem (Slowdown).

Similarly to availability problems:

* Problems are opened per monitor
* Contains information about all requests responsible for problem

You can configure the way Dynatrace aggregates results for each packet for ICMP requests with single execution. Dynatrace supports AVG, MAX and MIN with `AVG` as the default method.

### Define thresholds

You can define performance thresholds when configuring the request for your synthetic monitor. The defined performance threshold is the same for all requests within a single step. In cases, where there's a need to build a multi-step NAM monitor, it's possible to define various thresholds for each step.

To define thresholds

1. Follow the steps described in [Create a NAM monitor](#monitor-configuration) section.
2. In the **Requests** step, scroll down the page and see **Performance thresholds alerting** section.
3. Select **Generate a problem and send an alert on performance threshold violations.** check box.
4. Turn on **Advanced performance thresholds settings** toggle.

   In this section you can set the **Number of request executions in analyzed sliding window** and the **Number of violating request executions in analyzed sliding window**. For de-alerting samples we require `n` most recent non-violating request executions.

### Violation reporting

Red color annotation over performance charts indicates the period of time during which the performance threshold is raised. Additionally, a threshold is drawn on the performance chart, and you can examine which requests are above the threshold.

You may narrow down the time range only to that for which the problem was active using zoom functionality.

## Manage NAM monitors with API

To manage your NAM monitors via REST API

1. Search for and select **Dynatrace API**.
2. In the **Select a definition** field, select **Synthetic - Network availability monitors**.
3. Authenticate with your API token.

   For details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.").
4. Perform one of the following actions.

   | To do this | Go to **Synthetic - Network availability monitors** and select this |
   | --- | --- |
   | Get all synthetic monitors | **GET /synthetic/monitors** |
   | Create a synthetic monitor definition | **POST /synthetic/monitors** |
   | Delete a synthetic monitor definition for the given monitor ID | **DELETE /synthetic/monitors/{monitorId}** |
   | Get all synthetic monitor definition for the given monitor ID | **GET /synthetic/monitors/{monitorId}** |
   | Update a synthetic monitor definition for the given monitor ID. | **PUT /synthetic/monitors/{monitorId}** |

See [Synthetic monitors API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-network-availability-monitors "Create, read, update and delete synthetic monitors. Currently network availability monitors only.") for more details.

## Available script configuration properties

Optional

Monitors consist of requests, always of the same type (ICMP, TCP, or DNS).

If you don't provide the value, defaults will apply.

Duration format examples

* 100 milliseconds = `PT0.1S`
* 500 milliseconds = `PT0.5S`
* 1 second = `PT1S`
* 10 seconds = `PT10S`
* 90 seconds = `PT1M30S`
* 1 minute = `PT1M`
* 2 minutes = `PT2M`
* 5 minutes = `PT5M`

### ICMP

Name

Type

Description

Values

Default value

`EXECUTION_TIMEOUT`

string:duration

Timeout for the execution of a single request.

Valid duration, for example, `PT1S`.

Range = `0`â`PT2M`

`ICMP_NUMBER_OF_PACKETS` Ã `ICMP_TIMEOUT_FOR_REPLY` + `1s`

`ICMP_NUMBER_OF_PACKETS`

integer

Number of echo requests. The equivalent of the ping process are the `-c` (Linux) and `-n` (Windows) parameters.

Range = `1`â`10`

`1`

`ICMP_PACKET_SIZE`

integer

Data length. The equivalent of the ping process are the `-s` (Linux) and `-l` (Windows) parameters.

Range = `0`â`65500`

`32`

`ICMP_TIME_TO_LIVE`

integer

Time to live (TTL). The equivalent of the ping process are the `-t` (Linux) and `-i` (Windows) parameters.

Range = `1`â`255`

`ICMP_TYPE_OF_SERVICE`

integer

Type of service. The equivalent of the ping process are the `-Q` (Linux) and `-v` (Windows) parameters.

Range = `0`â`255`

`ICMP_DO_NOT_FRAGMENT_DATA`

boolean

Do not fragment. The equivalent of the ping process are the `-M do` (Linux) and `-f` (Windows) parameters.

`true` or `false`

`ICMP_TIMEOUT_FOR_REPLY`

string:duration

Wait for the echo reply message.

The equivalent of the ping process are the `-W` (Linux) and `-w` (Windows) parameters.

Valid duration, for example, `PT1S`. On Windows values like `PT1.1S` are accepted (granularity in milliseconds).

On Linux, values like `PT1S` are required (granularity in seconds).

Range = `PT1S`â`PT2S`

`PT1S`

The packet transmission interval is hardcoded to `200ms`, which corresponds to the minimum value allowed for the `-i` option of the Linux ping command without requiring elevated privileges.

### TCP

Name

Type

Description

Values

Default value

`TCP_PORT_RANGES`

string

Comma-separated list of port ranges

A single range can be either a single port number or a range of ports, defined as two port numbers with a hyphen.

The final list of requests to be executed is the product of all defined ports and target hosts. For example, if a step has two target hosts (`1.1.1.1` and `2.2.2.2`) and a range of two ports (`80-81`), four requests are executed within such a step.

* Request to `1.1.1.1` on port `80`
* Request to `1.1.1.1` on port `81`
* Request to `2.2.2.2` on port `80`
* Request to `2.2.2.2` on port `81`

Sample values

* `8080`
* `8000-9000`
* `80,443,90-100`

`EXECUTION_TIMEOUT`

string:duration

Connection timeout

Valid duration, for example, `PT1S`

Range = `0`â`PT2M`

`1s`

### DNS

Name

Type

Description

Values

Default value

`DNS_RECORD_TYPES`

string

Comma-separated list of DNS record types.

The final list of requests executed is the product of all defined record types and target hosts. For example, if a step has two record types (`A,AAAA`) and two target hosts (`host1.domain.com` and `host2.domain.com`), four requests are executed within such a step.

* Request for `A` record contents for `host1.domain.com`
* Request for `AAAA` record contents for `host1.domain.com`
* Request for `A` record contents for `host2.domain.com`
* Request or `AAAA` record contents for `host2.domain.com`

Sample values

* `A`
* `A,AAAA`
* `A,AAAA,CNAME`

`EXECUTION_TIMEOUT`

string:duration

Connection timeout

Valid duration, for example, `PT1S`

Range = `0`â`PT2M`

`2s`

`DNS_SERVER`

string

Address of the DNS server to query, with optional port

If a hostname is provided, it's resolved to an IP address using the system default DNS server.

Valid address, such as:

* `1.1.1.1`
* `8.4.4.8:53`
* `dns.google`
* `dns9.quad9.net:53`

If only host is provided, the default port `53` is used.

If no value is provided, the system default DNS server and port are used.

`DNS_FORCE_TCP`

boolean

By default, the DNS server is queried over a UDP connection, unless the message is too large to fit the UDP datagram. This option allows you to specify a TCP connection instead.

`true` or `false`

`false`

## Script configuration constraints

Constraints are conditions that need to be met to consider monitorâs execution successful. You need to define constraints for each monitor.

### Step-level constraints

#### `SUCCESS_RATE_PERCENT`

Required

This is an obligatory constraint for all monitors' request success rate. The default value is `>=80%`.

Percentage of successful requests in a step.

Actual success rate = ratio of the number of requests that didn't fail to all requests.

For example, if 1 request out of 6 has failed, the ratio is (6-1)/6 = 83.33%.

| Property | Type | Description | Value | Default value |
| --- | --- | --- | --- | --- |
| `operator` | string | Comparison operator to compare actual and expected value | `>=`, `>`, `<=`, `<`, `=`, or `!=` | `>=` |
| `value` | integer | Expected value of success rate to use for comparison | Range = `0`â`100` | `80` |

```
{



"type": "SUCCESS_RATE_PERCENT",



"properties": {



"value": "80",



"operator": ">"



}



}
```

For requests with only one target, we suggest setting the constraints values to `100`.

### Request-level constraints



#### ICMP request constraints

##### `ICMP_SUCCESS_RATE_PERCENT`

Required

This is an obligatory constraint for ICMP monitors request success rate. The default value is `>=80%`.

Percentage of successful pings (echo requests) in a request.

Actual success rate = ratio of number of the packets received to number of packets sent.

For example, if 5 packets were sent and 4 packets were received, the ratio is 4/5 = 80.00%.

| Property | Type | Description | Value | Default value |
| --- | --- | --- | --- | --- |
| `operator` | string | Comparison operator to compare actual and expected value | `>=`, `>`, `<=`, `<`, `=`, or `!=` | `>=` |
| `value` | integer | Expected value of success rate to use for comparison | Range = `0`â`100` | `80` |

```
{



"type": "ICMP_SUCCESS_RATE_PERCENT",



"properties": {



"value": "80",



"operator": ">"



}



}
```

#### TCP request constraints

##### `TCP_PORT_UNREACHABLE`

Optional

This is an optional constraint for TCP monitors.
This is a special constraint that inverts the [execution status](#execution-statuses) for TCP requests. It should be applied if it's expected that the port being checked is unreachable.

This constraint has no configuration properties.

If this constraint is applied:

* When the `Execution timeout (12033)` and `TCP socket connection error (22000)` statuses are detected after performing a connection attempt, they are interpreted as `HEALTHY (0)`.
* The `HEALTHY (0)` connection status is interpreted as `CONSTRAINT_VIOLATED (1401)` because we expected a failure.
* The `UNEXPECTED_ERROR (-1)` and `UNKNOWN_HOST (12013)` statuses are preserved and reported as is.

```
{



"type": "TCP_PORT_UNREACHABLE",



"properties": {}



}
```

#### DNS request constraints

At least one required

DNS constraints are **optional**, but at least one must be defined to indicate what is a successful query.

##### `DNS_STATUS_CODE`

`DNS_STATUS_CODE` by default is `1`, having status code `=0` is the simplest example of a successful query.

| Property | Type | Description | Value | Default value |
| --- | --- | --- | --- | --- |
| `operator` | string | Comparison operator to compare actual and expected value | `=` or `!=` | `=` |
| `statusCode` | integer | Numeric code indicating status of DNS response Exclusive with `status` | Valid code, for example, `0` Range = `0`â`65535` | `0` |
| `status` | string | Mnemonic representing DNS status code Exclusive with `statusCode` | Valid status, for example, `NOERROR` | `NOERROR` |

```
{



"type": "DNS_STATUS_CODE",



"properties": {



"operator": "=",



"statusCode": "0"



}



}
```

```
{



"type": "DNS_STATUS_CODE",



"properties": {



"operator": "=",



"status": "NOERROR"



}



}
```

##### `DNS_IP_ADDRESS`

Verifies the IP address value returned in A/AAAA records.

| Property | Type | Description | Value | Default value |
| --- | --- | --- | --- | --- |
| `quantifier` | string | How many records must match the condition for the constraint to pass | `any` (at least one) or `all` | `any` |
| `operator` | string | Comparison operator | `=`, `!=` or `in` | `=` for an address, `in` for a subnet |
| `recordType` | string | DNS record type | `A` or `AAAA` | `A` if address/subnet is IPv4 `AAAA` if address/subnet is IPv6 |
| `address` | string | IPv4 address in dot notation or IPv6 address in colon notation Only with the operators `=`, `!=` Exclusive with `subnet` | Valid address, for example, `192.168.0.1`, `2001:db8::2:1` |  |
| `subnet` | string | IPv4 subnet in dot notation or IPv6 subnet in colon notation, followed by network prefix length Only with the operator `in` Exclusive with `address` | Valid subnet, for example, `172.22.80.0/20`, `2001:db8:85a3::0/48` |  |

```
{



"type": "DNS_IP_ADDRESS",



"properties": {



"quantifier": "any",



"recordType": "A",



"operator": "=",



"address": "54.208.9.71"



}



}
```

```
{



"type": "DNS_IP_ADDRESS",



"properties": {



"quantifier": "all",



"recordType": "A",



"operator": "in",



"subnet": "10.102.44.0/24"



}



}
```

##### `DNS_RECORD_COUNT`

Verifies the count of records of a given type.

| Property | Type | Description | Value | Default value |
| --- | --- | --- | --- | --- |
| `operator` | string | Comparison operator | `>=`, `>`, `<=`, `<`, `=`, or `!=` | `>` |
| `recordType` | string | DNS record type | Valid record type, for example, `MX` |  |
| `value` | integer | Expected record count | Valid count, for example `2` Range = `0`â`65535` | `80` |

```
{



"type": "DNS_RECORD_COUNT",



"properties": {



"recordType": "A",



"operator": ">",



"value": "80"



}



}
```

##### `DNS_TIME_TO_LIVE`

Verifies the time to live (TTL) of records of a given type.

| Property | Type | Description | Value | Default value |
| --- | --- | --- | --- | --- |
| `quantifier` | string | How many records must match the condition for the constraint to pass | `any` (at least one) or `all` | `any` |
| `operator` | string | Comparison operator | `>=`, `>`, `<=`, `<`, `=`, or `!=` | `>` |
| `recordType` | string | DNS record type | Valid record type, for example, `NS` |  |
| `value` | integer | Expected TTL in seconds | Valid TTL, for example `3600` Range = `0`â`2147483647` | `80` |

```
{



"type": "DNS_TIME_TO_LIVE",



"properties": {



"quantifier": "any",



"recordType": "A",



"operator": ">=",



"value": "80"



}



}
```

##### `DNS_RECORD_VALUE`

Verifies the raw value of records of a given type, with the value format depending on the record type.

Constraints process all records in a response, regardless of the section to which they belong (`answer`, `authority`, or `additional`).

| Property | Type | Description | Value | Default value |
| --- | --- | --- | --- | --- |
| `quantifier` | string | How many records must match the condition for the constraint to pass | `any` (at least one) or `all` | `any` |
| `operator` | string | Comparison operator - `contains` checks if the record value contains a given sequence. - `matches` checks if record value matches a given pattern. | `contains` or `matches` | `contains` |
| `recordType` | string | DNS record type | Valid record type, for example, `TXT` |  |
| `sequence` | string | Sequence of characters that the record value should contain Only with the operator `contains` Exclusive with `pattern` | Non-empty sequence, for example, `ms71815323` |  |
| `pattern` | string | Pattern to be matched against the record value, with `*` denoting 0 or more characters Only with the operator `matches` Exclusive with `sequence` | Non-empty pattern, for example, `"v=spf1 include:*` |  |

```
{



"type": "DNS_RECORD_VALUE",



"properties": {



"quantifier": "any",



"recordType": "TXT",



"operator": "contains",



"sequence": "ms71815323"



}



}
```

```
{



"type": "DNS_RECORD_VALUE",



"properties": {



"quantifier": "any",



"recordType": "TXT",



"operator": "matches",



"pattern": "\"v=spf1 include:*"



}



}
```

## Related topics

* [Synthetic Monitors API](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.")