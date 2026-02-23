---
title: Monitor file access of CICS applications
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access
scraped: 2026-02-23T21:24:32.106159
---

# Monitor file access of CICS applications

# Monitor file access of CICS applications

* Latest Dynatrace
* 1-min read
* Published Jan 13, 2023

With Dynatrace, you can monitor the VSAM and BDAM file access calls from your CICS applications using the CICS module. Each accessed file in a CICS region is represented as a database service on the [Databases](/docs/observe/infrastructure-observability/databases "Track the database performance and resources to create and maintain a high performing and available application infrastructure.") page, including metrics like response time, failure rate, and throughput.

![File access on the Database page](https://dt-cdn.net/images/file-sensor-db-3052-6d5ec51cdd.png)

The [Distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") page lists the file operations and logical file names that are being accessed on the [PurePath method-level](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces."). The file operations are aggregated per logical file name (for example, in the image below, the `READNEXT` operation was executed 21 times on the file `EXMPCAT`).

![File access calls in the Distributed traces page](https://dt-cdn.net/images/file-sensor-pp-3142-684de155b6.png)

## Get started

To start monitoring the file access calls from your CICS applications

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Activate the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **z/OS CICS file monitoring sensor**.
3. Restart your CICS region or allow [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") to pick up the new configuration setting in the next 5 minutes interval.

## Remote files

In the application program, if the file control API has a `SYSID` clause with the remote `SYSID`, the file is recognized as a remote file. However, if the file is defined as remote in the `CEDA` definition, the CICS module doesn`t recognize the file as a remote file.

## Turn off File access monitoring

To turn off file access monitoring, toggle the `z/OS CICS file monitoring` sensor and the `Instrumentation enabled (change needs a process restart)` to off. The CICS region need not have to be restarted for the settings to take effect. The DTAX transaction picks up the file sensor changes (on/off) within 5 minutes.