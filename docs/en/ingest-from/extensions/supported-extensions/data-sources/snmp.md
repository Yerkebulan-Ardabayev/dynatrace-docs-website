---
title: Manage SNMP extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/snmp
scraped: 2026-02-17T05:01:05.206728
---

# Manage SNMP extensions

# Manage SNMP extensions

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on May 08, 2023

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly from your SNMP-monitored devices. To this end, Dynatrace enables you to bring SNMP data into Dynatrace at scale and within the context of all other data.

You can also extend your insights into data related to SNMP traps issued in your infrastructure.

First, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=snmp) to see if your device is covered by an existing extension. If it isn't, you can build your own [Dynatrace SNMP extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Learn how to create an SNMP extension using the Extensions framework.") to cover your SNMP device.

## Before you begin

1. Decide which SNMP will provide data for the extension. Dynatrace Extensions framework supports SNMP v2c and v3. Depending on the SNMP version, prepare the necessary authentication details.
2. Designate an ActiveGate group or groups that will remotely connect to your SNMP devices to pull data. All ActiveGates in each designated group need to be able to connect to your SNMP devices.
3. Learn [hardware requirements](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions#hw "Learn how to create an SNMP extension using the Extensions framework.") for an ActiveGate performing SNMP monitoring.

## Manage SNMP extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest SNMP data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, search for "snmp" to find an SNMP or SNMP traps extension.
2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.
3. Add a monitoring configuration so that the extension can begin collecting data.

Next, perform the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**ActiveGate group**](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#step-1 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Define devices**](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#step-2 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Advanced properties**](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#step-3 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp#step-4 "Learn how to extend observability in Dynatrace with declarative SNMP metrics and event ingestion.")

### Step 1 ActiveGate group

Select the ActiveGate group to determine which ActivGates will run the extension. When done, select **Next step**.

### Step 2 Define devices

Select **Add device** to define the devices from which you want to pull data and provide the device connection details:

* IP address or device name
* Port
* SNMP version and related authentication details. Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

### Step 3 optional Advanced properties Optional

SNMP extensions only

Select **Define** to configure optional advanced properties:

* **Timeout in seconds**  
  The maximum time (in seconds) to wait for an SNMP query to return data. Default = `2` seconds.
* **Retries**  
  The maximum number of retries for a query if it fails (total time for a query is `timeoutSecs` x `retries`). Default = `3` retries.
* **Max repetitions**  
  Can be used to limit the amount of data returned for a single query and might in turn increase the number of requests sent to the device until all required data is collected. Default = `50` repetitions.
* **Max OIDs per query**  
  Number of OIDs that can be queried in one SNMP request. Default = `60` OIDs. For most extensions, you don't need to change it. For the [F5 BIG-IP LTMï»¿](https://dt-url.net/jl036z9) extension, we recommend that you set it to `5`.
* **Enable unconnected UDP**
  When enabled, the UDP socket becomes unconnected. This allows it to accept responses from a different address than the one the request was sent to, or to ignore ICMP packets. Default value is `false`.

SNMP Traps extensions only

Select **Add varbinding rule** to configure variable binding trimming:

* **Variable binding (OID) prefix**  
  The part of the OID that is matched for trimming.
* **Number of octets trimmed**  
  The number of octets at the end of the OID that you want to trim.

When done, select **Next step**

### Step 4 Activate extension

Provide final configuration details.

* **Description**  
  Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, this can give your teams details of this particular monitoring configuration.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension. For SNMP traps extensions, select the **Events** feature set to enable the forwarding of trap messages as log events.
* **Variables**  
  Some extensions offer variables with which you can pass custom strings to your extension and report them in the environment, for example, as your dimension. Some extensions contain the `ext.activationtag` variable that is passed as a dimension to your monitoring configuration. You can use it to associate the reported metrics with a particular version of your monitoring configuration.

When done, select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Custom MIB files

Management Information Base (MIB) is the database managing the entities in a network identified by OIDs. MIB provides a source of additional information related to OIDs declared in your extension.

ActiveGate comes with a default set of MIB files. If some of the OIDs used in your custom SNMP extension are not available in the default MIB files, you can add your own MIB file to the ActiveGate running the extension.

Custom MIB files are only applicable when you build your own SNMP extension. Dynatrace out-of-the-box SNMP extensions come with a predefined set of OIDs and do not dynamically load additional MIB files placed in the `mib-files-custom` directory.

When you create a custom SNMP or SNMP traps extension, the MIB files located in the `mib-files-custom` directory will be used by all such custom extensions running on the ActiveGate.

Place your custom MIB files in the `mib-files-custom` directory:

* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/mib-files-custom/`
* Windows: `C:\%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata\mib-files-custom\`

The files stored in the `mib-files-custom` directory are preserved between updates.

## Explore SNMP extensions

Filter by

Select an option

Type to filter

Unable to render DataTable. Check configuration.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")