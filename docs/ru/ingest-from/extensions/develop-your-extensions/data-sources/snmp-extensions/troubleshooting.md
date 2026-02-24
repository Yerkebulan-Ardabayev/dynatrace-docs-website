---
title: Troubleshooting
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions/troubleshooting
scraped: 2026-02-24T21:30:52.030053
---

# Troubleshooting

# Troubleshooting

* Latest Dynatrace
* Troubleshooting
* 3-min read
* Published Jul 10, 2023

When working with Dynatrace extensions that utilize the SNMP data source, you may encounter issues that require troubleshooting.

## Configuration status not OK

Whenever a monitoring configuration is created or updated, it can take a few minutes to fully activate and start monitoring. Until then, the configuration status may change to Warning or Error as the configuration is scheduled to the endpoint, queued for downloading, activated, validated, and started. Allow at least 5 minutes for this. If the status is still not OK, select the colored dot next to it; this opens a Log Viewer interface for more details.

### Fastcheck failures

Fastcheck is a simple SNMP Get query that aims to retrieve one OID from the device representing its system name. The device has 18 seconds to respond or the check fails. This is the very first step before any other detail is collected from the device.

Fastcheck failures point to an issue with communicating with the device

* Wrong credentials for connecting to the device
* Network firewalls not allowing communication
* Misconfigured devices not allowing SNMP queries

### GetBulk returned an error

GetBulk is the SNMP query operation used to retrieve data from the device. When this appears in the error message, it means the device is reachable (FastCheck passed) but the data could not be retrieved.

This type of error can have multiple causes:

* The credentials provided (for example, community string) are invalid
* The network is unreliable, causing communication issues
* There is too much data to retrieve; try reducing the feature sets or optimizing the advanced settings

### Invalid config errors

Invalid config will point back to the details entered in the monitoring configuration fields. While the device details are self-explanatory, the variables filters must follow the syntax mentioned in the previous section.

### High CPU

`HIGH_CPU` status means the maximum allowed CPU consumption for the datasource module of the Extension Execution Controller (EEC) has been reached on the ActiveGate.

* The amount of data cannot be collected and processed without going above the 5% CPU usage built-in resource limit.
* Try initially enabling fewer feature sets (implying fewer metrics, so fewer requests to process) or spread the feature sets over multiple configurations.

### Extension logs

Extension logs can be found in the [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."). Look for the `Extensions configuration, logs` in **Purpose of** column.

## Optimization for large devices

Monitoring configurations are provided with a set of advanced settings that affect how the data is requested from the device via SNMP. The default values work in most cases, but you can adjust them if you experience issues such as missing data.

* Timeout and Retries refer to the maximum time to wait for an SNMP query to return and the number of times to retry a query in case of failures.
* Max. repetitions refers to how many times an OID (metric identifier in SNMP) can be repeated as part of a single SNMP GetBulk query response when the same metric is collected for multiple objects/instances. A lower value means more requests between the extension and the device to collect a large dataset.

  Due to the speed and unreliability of the SNMP protocol, it is more effective to use a smaller value (for example, 20). Default = 50.
* Max. OIDs per query refers to the maximum number of OIDs that can be requested for each SNMP GetBulk query.

  In very large environments, we recommend that you set it to 5. This improves performance by further splitting the workload into more requests.