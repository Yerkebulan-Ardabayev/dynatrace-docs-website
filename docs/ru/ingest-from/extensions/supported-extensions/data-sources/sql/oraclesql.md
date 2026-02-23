---
title: Manage Oracle Database extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql
scraped: 2026-02-23T21:28:06.194126
---

# Manage Oracle Database extensions

# Manage Oracle Database extensions

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Apr 11, 2022

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your Oracle Database layer, so that you can monitor how database server tasks impact your app.

To get started, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=oracle+sql) to see if the Dynatrace-provided Oracle Database extension satisfies your requirements. If this is not the case, you can build your own [Dynatrace Oracle Database extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql "Learn how to create an SQL data source-based extension using the Extensions framework.").

## Before you begin

1. Decide which Oracle Database server you want to monitor. The Oracle Database extension supports Oracle Database versions 12.2+ with the following setups:

   * Oracle standalone servers
   * Oracle Multitenant (CDB/PDB)
   * Oracle RAC
   * Oracle AWS RDS
2. Designate an ActiveGate group or groups that will remotely connect to your Oracle Database server to pull data. All ActiveGates in each designated group need to be able to connect to your Oracle Database server.
3. Create a dedicated user account for monitoring and grant it permissions as in the [Oracle Databaseï»¿](https://dt-url.net/7f03qwp) extension description under the **Get started with Oracle Database servers** section.

## Manage Oracle SQL extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest Oracle Database data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install the **Oracle Database** extension. (You can use "Oracle SQL" to filter search results.) This enables the extension in your environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

Next, perform the following steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Accept Oracle JDBC driver redistribution license**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-1 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Define endpoints**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-2 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**ActiveGate group**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-3 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-4 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")

### Step 1 Accept Oracle JDBC driver redistribution license

An Oracle Database extension requires that you accept the [Dynatrace redistribution license agreement for Oracle JDBC Driverï»¿](https://dt-url.net/0s1n0pw9).

### Step 2 Define endpoints

Select **Add Oracle endpoint** to define the Oracle Database servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

* Host
* Port
* Database identifier, either **Service Name** or **SID**.
* Authentication credentials. Note that only basic authentication is supported. Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

  + You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring#credential-vault "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.") to provide a more secure approach of storing and managing user credentials.

When done, select **Next step**

### Step 3 ActiveGate group

Select the ActiveGate group to determine which ActiveGates will run the extension. When done, select **Next step**.

### Step 4 Activate extension

Provide final configuration details.

* **Description**  
  Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, this can give your teams details of this particular monitoring configuration.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.

When done, select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")