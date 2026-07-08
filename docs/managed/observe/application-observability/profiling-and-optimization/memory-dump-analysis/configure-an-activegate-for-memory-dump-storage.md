---
title: Configure ActiveGate for memory dump storage
source: https://docs.dynatrace.com/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage
---

# Configure ActiveGate for memory dump storage

# Configure ActiveGate for memory dump storage

* How-to guide
* 4-min read
* Published Jan 08, 2019

Applicable to Environment ActiveGate and Cluster ActiveGate

The following configuration of ActiveGate for memory dump storage is applicable to both Environment ActiveGate and Cluster ActiveGate.

When your application experiences memory leaks or high object churn, it’s important that you get memory dumps so you can analyze these issues. In production environments, this is often a challenge when you can’t log into the environment and you have no other means of triggering memory dumps. Dynatrace enables you to both trigger and securely download memory dumps to the analysis tool of your choice. To enable memory dumps, you need to configure your ActiveGate as described below.

If you configure an ActiveGate to collect memory dumps, and then restart the ActiveGate service, all instances of OneAgent will automatically reconnect and recognize that the ActiveGate can now store memory dumps. From now on, whenever a memory dump is successfully triggered, the dump will be uploaded automatically to the correct ActiveGate. Once safely stored on the ActiveGate, the OneAgent deletes the local file from its storage. Note that OneAgent automatically deletes a memory dump on the original host after one hour.

## Before you begin

Familiarize yourself with the [basic rules for working with ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#basic-rules "Learn which ActiveGate properties you can configure based on your needs and requirements.").

## Activate dump functionality

Create the `[collector]` section in the `custom.properties` file, if it doesn't already exist.
Specify the `DumpSupported` property in this section and set the value to `true`.

```
[collector]



DumpSupported = true
```

## Specify dedicated dump directory (Optional)

Unless configured otherwise, ActiveGate saves memory dumps in a [default directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

To use a custom path, specify the path in the properties file and create the directory with appropriate permissions:

Create the `[dump]` section in `custom.properties` (if it doesn't already exist) and then specify the `dumpDir` property in this section. For example:

```
[dump]



dumpDir = dump
```

The `dumpDir` property can contain a relative path, for example, `dumpDir = mydir`. In this case, the directory will be a subdirectory of the default location. It can also be an absolute path, for example, `dumpDir = C:\data\memory-dumps`.

Create the directory, if it does not already exist, and make sure that it has correct access permissions for the user running the ActiveGate service. This is by default `dtuserag` for Linux, and `Local Service` for Windows:

* Linux systems:  
  `Read`, `Write`, and `Execute`
* Windows systems:  
  `Read`, `Write`, and `Modify`

  Example of dump directory permissions on Windows

  ![Dump directory permissions](https://dt-cdn.net/images/memdump7-441-a577bfb9a0.png)

  Dump directory permissions

### Use of `/temp` or `/tmp` under Linux

Because of possible automatic purging, we recommend that you not use the Linux directories `/temp`, `/tmp`, or their subdirectories to install ActiveGate or store any data generated or used by ActiveGate.

## Specify parameters for managing dump files (Optional)

Also in the `[dump]` section, you can specify the following properties:

| Property | Default value | Description |
| --- | --- | --- |
| `dumpDir` | `dump` | Valid path of the storage directory used for dump storage |
| `maxSizeGb` | `100` | Storage quota in GBs. If full, the oldest dumps are overwritten until enough space is available to store a new dump. |
| `maxAgeDays` | `7` | Maximum age of a memory dump in days until the dump is automatically overwritten |
| `maxConcurrentUploads` | `5` | Maximum number of concurrent dump uploads from OneAgents |
| `downloadUrl` | unset | A custom download URL. This is particularly useful if ActiveGate is behind a load balancer to manage end-user traffic or if ActiveGate only detects an IP address and an FQDN is required by the user. Note that a load balancer should not be placed between ActiveGate and OneAgent, as this can disrupt memory dump functionality. The URL must contain the correct schema and port. |

## Restart ActiveGate

If you modify your ActiveGate configuration, you must [restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.") to put your changes into effect.

## Example custom.properties file contents

```
[collector]



DumpSupported = true



[dump]



# relative to collector root dir or absolute path



dumpDir = dump



# maximum size in GB for stored memory dump



maxSizeGb = 100



# maximum age in days for keeping stored memory dumps



maxAgeDays = 7



# maximum number of concurrent file uploads supported



maxConcurrentUploads = 5
```