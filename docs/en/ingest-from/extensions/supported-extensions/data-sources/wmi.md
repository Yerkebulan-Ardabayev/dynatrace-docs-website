---
title: Manage WMI extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/wmi
scraped: 2026-02-15T09:03:49.418937
---

# Manage WMI extensions

# Manage WMI extensions

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Feb 01, 2022

Dynatrace provides you with a framework that you can use to extend your observability into data acquired directly for WMI-monitored Windows services and components. To this end, Dynatrace offers the facility to bring WMI data into Dynatrace at scale and in the context to all other data. This works best if you have OneAgent on the monitored Windows box, but it also works in an agentless manner.

First, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=wmi) to see if your technology is covered by an existing extension. If it isn't, you can build your own [Dynatrace WMI extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") to cover your Windows technology.

## Before you begin

1. Decide which of your Windows-based hosts will provide data for the extension.
2. WMI extensions can run locally on an OneAgent (recommended) or remotely on an ActiveGate.

   * When run locally on a Windows host, the extension will connect to the WMI interface automatically. Make sure Extension Execution Controller is enabled at the environment or selected host level. For more information, see [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.")
   * When monitored remotely, make sure your Windows-based ActiveGates belonging to the ActiveGate groups you designated for remote monitoring have remote permissions enabled. See [WMI data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") for more information.

## Manage WMI extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest WMI data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, search for a WMI extension. You can use the "WMI" keyword to filter results.
2. Select and install the extension you're interested in. This enables the extension in your monitoring environment.
3. Add a monitoring configuration so that the extension can begin collecting data.

Next, perform the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define monitoring source**](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi#step-1 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Advanced properties**](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi#step-2 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi#step-3 "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.")

### Step 1 Define monitoring source

#### Local monitoring

1. Select the host, host group or management zone for which you will run the extension, or choose to monitor the whole environment. The host needs to be running a OneAgent that is [enabled to run extensions](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.").
2. Select **Next step**.

#### Remote monitoring

1. Select **Monitor remotely** and choose the ActiveGate group to determine which ActiveGate or ActiveGates will run the extension. A Windows-based ActiveGate host needs to have remote permissions enabled. See [WMI data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions "Learn how to create a WMI extension using the Extensions framework.") for more information
2. Select **Next step**.
3. Select **Add host** and provide connection details.

   * Host name or IP address
   * Username with permissions to access WMI data remotely
   * Password

You can add up to 100 hosts.

Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them. When done, select **Next step**.

### Step 2 optional Advanced properties Optional

Some WMI extensions may require additional configuration. When done, select **Next step**

### Step 3 Activate extension

Provide final configuration details.

* **Description**  
  Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, it can give your teams details of this particular monitoring configuration.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension
* **Variables**  
  Some extensions offer variables with which you can pass custom strings to your extension and report them in the environment, for example, as your dimension. Some extensions contain the `ext.activationtag` variable that is passed as a dimension to your monitoring configuration. You can use it to associate the reported metrics with a particular version of your monitoring configuration.

When done, select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Explore WMI extensions

Filter by

Select an option

Type to filter

Unable to render DataTable. Check configuration.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")