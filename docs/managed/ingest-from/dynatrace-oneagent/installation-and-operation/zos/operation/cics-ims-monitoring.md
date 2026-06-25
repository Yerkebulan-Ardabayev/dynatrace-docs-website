---
title: Customize CICS and IMS monitoring
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/cics-ims-monitoring
scraped: 2026-05-12T12:15:52.356721
---

# Customize CICS and IMS monitoring

# Customize CICS and IMS monitoring

* 6-min read
* Updated on Dec 05, 2025

Define additional monitoring settings for CICS and IMS transactions. Go to **Settings** > **Mainframe** to find the following menu options:

* [Transaction monitoring](#transaction-monitoring)
* [Transaction start filters](#transaction-start-filters)
* [IBM MQ filters](#ibm-mq-filters)

## Transaction monitoring

Define additional monitoring settings for CICS and IMS transactions.

| Parameter | Description |
| --- | --- |
| Monitor all incoming web requests | Dynatrace automatically traces incoming web requests when they are called by monitored services. Enable this setting to trace all incoming web requests regardless of whether they are called from monitored or unmonitored services.  We recommend enabling it only over a short period of time. |
| Group CICS regions that belong to the same CICSPlex | Enable this setting to group CICS regions belonging to the same CICSPlex into a single process group. If disabled, a process group is created for every CICS region.  You may instruct the CICS region to wait for the CICSPlex to become available before proceeding. See [CICSPlex name grouping](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics#plexname-grouping "Install the Dynatrace CICS module.").  This setting is enabled by default. |
| Create CICS services based on transaction IDs | Enable this setting to create a CICS service for each monitored transaction ID within a process group. If disabled, a CICS service will be created for each monitored CICS region within a process group.  This setting is enabled by default. We recommend enabling it only when the CICS regions are grouped by their CICSPlex. |
| Group IMS regions that belong to the same subsystem | Enable this setting to group IMS regions belonging to the same subsystem into a single process group. If disabled, a process group will be created for each IMS region.  This setting is enabled by default. |
| Create IMS services based on transaction IDs | Enable this setting to create an IMS service for each monitored transaction ID within a process group. If disabled, an IMS service will be created for each monitored IMS region within a process group.  This setting is enabled by default. We recommend enabling it only when the IMS regions are grouped by their subsystem. |
| PurePathÂ® distributed trace node limit | The maximum number of nodes in the distributed trace, which will be captured for a single CICS or IMS program call. We recommend the limit of 500, which is the default. Increasing the default limit might cause more overhead to process the additional data.  The value of `0` means unlimited number of nodes. |

## Transaction start filters

Dynatrace traces CICS and IMS transactions when they are called by monitored services. Dynatrace also traces transactions where they are started through a supported protocol by CICS Transaction Gateway, z/OS Connect Enterprise Edition, or IBM MQ (unless they are limited by the IBM MQ filters).

Transactions that start on the mainframe or on a terminal (for example, IBM 3270 green screen terminal), or are called by unmonitored services, need to be explicitly listed in order to be traced.

### CICS terminal transaction start filter

To trace CICS transactions that start on a terminal (for example, IBM 3270 green screen terminal), add their transaction IDs to the CICS terminal transaction start filter. You can use the asterisk (`*`) wildcard. For example, use `TN*` to trace all transaction IDs that start with `TN`, or use `*` to trace all transactions starting on a terminal.

Activate the required [OneAgent feature](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **z/OS CICS terminal transaction sensor**.

### CICS transaction start filter

To trace CICS transactions that start on the mainframe or are called by unmonitored services, add their transaction IDs to the CICS transaction start filter. You can use as a suffix the asterisk (`*`) wildcard. For example, use `TN*` to trace all transaction IDs that start with `TN`.

This sensor ignores transactions that are captured by another sensor at the start of the transaction (CICS Transaction Gateway and z/OS Connect Enterprise Edition, as well as transaction start and DPL requests from other CICS transactions). It interferes with transactions that are recognized later in the chain, so if a listed transaction is called through IBM MQ, SOAP, JSON, HTTP, or the CICS/IMS SDK, a new trace will start for this transaction and it will not be linked to the previous trace.

If you have any transaction IDs listed here that belong to a terminal (for example, IBM 3270 green screen terminal), we recommend that you move them to the **CICS terminal transaction start filter** list.

In the CICS transaction start filter:

* You can use an asterisk (`*`) in the transaction ID suffix, but it can't be only an asterisk.
* We do not recommend setting transaction ID as `C*`, as this would capture CICS internal transactions.

### IMS terminal transaction start filter

To trace IMS transactions that start on a terminal (for example, IBM 3270 green screen terminal), add their transaction IDs to the IMS terminal transaction start filter. You can use the asterisk (`*`) wildcard. For example, use `TN*` to trace all transaction IDs that start with `TN`, or use `*` to trace all transactions starting on a terminal.

You need to enable the **z/OS IMS terminal transaction sensor** [OneAgent feature](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") to trace such transactions.

### IMS transaction start filter

To trace IMS transactions that start on the mainframe or are called by unmonitored services, add their transaction IDs to the IMS transaction start filter. You can use as a suffix the asterisk (`*`) wildcard. For example, use `TN*` to trace all transaction IDs that start with `TN`.

Unlike the CICS transaction start sensor, the IMS transaction start sensor will not interfere with a trace captured from another sensor (MQ, SOAP, ITRA, IMS Connect, and zOS Connect).

If you have any transaction IDs listed here that belong to a terminal (for example, IBM 3270 green screen terminal), move them to the **IMS terminal transaction start filter** list.

## IBM MQ filters

Dynatrace traces CICS and IMS transactions that originate from IBM MQ queues. To limit tracing to certain queues, specify their names in the include lists. To exclude queues from tracing, specify their names in the exclude lists. For IMS, these lists apply to message processing regions.

| Parameter | Description |
| --- | --- |
| CICS: Included MQ queues | A list of MQ queue names associated with CICS that can start a trace. |
| CICS: Excluded MQ queues | A list of MQ queue names associated with CICS that should not start a trace. |
| IMS: Included MQ queues | A list of MQ queue names associated with IMS message process region that can start a trace. |
| IMS: Excluded MQ queues | A list of MQ queue names associated with IMS message process region that should not start a trace. |
| IMS bridge: Included transaction IDs | To only trace specific transactions submitted via the IMS bridge, specify their transaction IDs in the include list. |
| IMS bridge: Excluded transaction IDs | To exclude specific transactions submitted via the IMS bridge from tracing, specify their transaction IDs in the exclude list. |