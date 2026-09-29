---
title: Manage Microsoft SQL Server extensions
source: https://docs.dynatrace.com/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql
---

# Manage Microsoft SQL Server extensions

# Manage Microsoft SQL Server extensions

* How-to guide
* 2-min read
* Published Sep 05, 2022

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your Microsoft SQL Database layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hub﻿](https://www.dynatrace.com/hub/?query=microsoft+sql) to see if the Dynatrace-provided Microsoft SQL Server extension satisfies your requirements. If you need something different, you can build your own [Microsoft SQL Server extension](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql#microsoft-sql-monitoring "Learn how to create an SQL data source-based extension using the Extensions framework.").

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your Microsoft SQL Database server to pull data. All ActiveGates in each designated group need to be able to connect to your Microsoft SQL Database server.

## Manage Microsoft SQL extensions

Dynatrace Hub provides a unified workflow to enable and manage extensions that ingest Microsoft SQL Server data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install the **Microsoft SQL Server** extension. This enables the extension in your environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

Define endpoints](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

Select ActiveGates](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

Activate the extension](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")

### Step 1 Define endpoints

1. Select **Add Sql Server endpoint** to define the servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

   * Host
   * Optional Port
   * Optional Instance name
   * Optional Database name
   * Authentication scheme. You can choose from the following [authentication schemes](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#authentication "Microsoft SQL extensions in the Extensions framework."):

     + Basic authentication
     + Kerberos authentication
     + NTLM authentication
   * You can [enable SSL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#ssl "Microsoft SQL extensions in the Extensions framework.") to establish a secure connection for your configuration.
   * You can [use credential vault](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#credential-vault "Microsoft SQL extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
2. Select **Next step**.

### Step 2 Select ActiveGates

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 3 Activate the extension

1. Give your monitoring configuration a distinctive label in **Description**.
2. Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. To learn how to use it to activate an extension using the Dynatrace API, see [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

## Related topics

* [Troubleshooting extensions﻿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")