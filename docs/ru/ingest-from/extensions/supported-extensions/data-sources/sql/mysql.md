---
title: Manage MySQL extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/mysql
scraped: 2026-02-24T21:22:22.711842
---

# Manage MySQL extensions

# Manage MySQL extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Apr 19, 2023

Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your MySQL Database server layer, so that you can monitor how database server tasks impact your app.

Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=mysql) to see if the Dynatrace-provided MySQL Database Server extension satisfies your requirements.

## Before you begin

Designate an ActiveGate group or groups that will remotely connect to your MySQL Database server to pull data. All ActiveGates in each designated group need to be able to connect to your MySQL Database server.

## Manage MySQL extensions

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Now you can use the dedicated Extensions app to manage your extensions. It provides a similar activation and configuration workflow as Dynatrace Hub in the previous Dynatrace. Additionally, it gives you direct access to extension health monitoring.

* To use the app:

  + In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), select and install the app.
  + The Hub listing provides information on the permissions required to use the app (the **Technical information** tab).

Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest MySQL Database data into your Dynatrace environment.

Required permission: **Change monitoring settings**

1. In Dynatrace Hub, select and install the **MySQL (remote monitoring)** extension. This enables the extension in your environment.
2. Add a monitoring configuration so that the extension can begin collecting data.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Define endpoints**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/mysql#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from MySQL Database server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**ActiveGate group**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/mysql#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from MySQL Database server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Activate extension**](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/mysql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from MySQL Database server.")

### Step 1 Define endpoints

1. Select **Add MySQL endpoint** to define the servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:

* Host
* Port
* Database name
* Authentication credentials

  + Only basic authentication is supported.
  + Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.
  + You can [use credential vault](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring#authentication "MySQL extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.
* Select **Next step**

### Step 2 Select ActiveGates

1. Select the ActiveGate group to determine which ActiveGates will run the extension.
2. Select **Next step**.

### Step 3 Activate extension

1. Provide final configuration details:

* **Description**  
  Text explaining details of this particular monitoring configuration. When your teams are troubleshooting monitoring, this can give them important details.
* **Feature sets**  
  In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.
* Select **Activate**.

## Monitoring configuration as JSON

The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Manage Extensions](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.") to learn how to use it to activate an extension using the Dynatrace API.

## Related topics

* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")