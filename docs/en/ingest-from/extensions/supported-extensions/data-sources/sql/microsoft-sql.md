---
title: Manage Microsoft SQL Server extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql
scraped: 2026-02-16T21:22:13.160045
---

# Manage Microsoft SQL Server extensions

# Manage Microsoft SQL Server extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 05, 2022

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your Microsoft SQL Database layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=microsoft+sql) to see if the Dynatrace-provided Microsoft SQL Server extension satisfies your requirements. If you need something different, you can build your own [Microsoft SQL Server extension](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql#microsoft-sql-monitoring "Learn how to create an SQL data source-based extension using the Extensions framework.").

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your Microsoft SQL Database server to pull data. All ActiveGates in each designated group need to be able to connect to your Microsoft SQL Database server.

## Manage Microsoft SQL extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that ingest Microsoft SQL Server data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install the **Microsoft SQL Server** extension. This enables the extension in your environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

Define endpoints](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

Select ActiveGates](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

Activate the extension](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")

### Step 1 Define endpoints

1. Select **Add Sql Server endpoint** to define the servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

   * Host
   * Optional Port
   * Optional Instance name
   * Optional Database name
   * Authentication scheme. You can choose from the following [authentication schemes](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#authentication "Microsoft SQL extensions in the Extensions framework."):

     + Basic authentication
     + Kerberos authentication
     + NTLM authentication
   * You can [enable SSL](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#ssl "Microsoft SQL extensions in the Extensions framework.") to establish a secure connection for your configuration.
   * You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#credential-vault "Microsoft SQL extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
2. Select **Next step**.

### Step 2 Select ActiveGates

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 3 Activate the extension

1. Give your monitoring configuration a distinctive label in **Description**.
2. Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. To learn how to use it to activate an extension using the Dynatrace API, see [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.").

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")