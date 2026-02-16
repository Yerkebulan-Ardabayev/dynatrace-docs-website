---
title: Monitor PostgreSQL database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/postgres
scraped: 2026-02-16T21:29:07.895141
---

# Monitor PostgreSQL database

# Monitor PostgreSQL database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

Monitor PostgreSQL databases with the Dynatrace Extension Framework to collect performance data and understand database impact on your applications.

## Prerequisites

* Designate an ActiveGate group or groups that will remotely connect to your PostgreSQL database server to pull data. All ActiveGates in each group must connect to your PostgreSQL database server.
* For self-hosted Postgres:

  + Postgres [additional supplied modules](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#monitor-self-hosted-postgres "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.") must be installed.
* For cloud-managed Postgres services:

  + Ensure that [specific extensions and settings are enabled](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#setup-cloud-monitoring-capabilities "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.").
* Create a dedicated database user in your database instance. Dynatrace uses this user to run monitoring queries against your PostgreSQL database.

  ```
  CREATE USER dynatrace WITH PASSWORD '<PASSWORD>' INHERIT;
  ```

### Compatibility information

* Supported from PostgreSQL version 11+.
* Postgres 14, 15, 16, and 17 are fully supported.

## Set up the PostgreSQL extension for monitoring

To set up and activate the extension, go to ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** and follow these steps for each instance.

### Add a database instance

1. Open the **Add DB instance** wizard from the top-right corner of ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases**.
2. Select **PostgreSQL** as the database vendor.
3. Select **Next**.

### Select hosting type

Select a hosting type from the options. This choice determines which script generates the necessary database objects later in the process.

1. Select the host type that matches your requirement.
2. Select **Next**.

### Select an ActiveGate group

1. Select the [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.") to determine which ActiveGates run the extension.
2. Select **Next**.

### Create a connection

Set up the connection to your database instance. Provide the required credentials directly in the wizard or use secure alternatives:

1. Add a name for the connection so you can identify it later.
2. Add the details in the **Configure connection** section.

   1. Choose **Select from existing hosts** or **Enter manually** to add connection details.
   2. Add the **Database name**.
3. Provide the **Authenticate** credentials for the `dynatrace` monitoring user you created directly or use secure alternatives.

   * Basic credentials: Authentication details passed to Dynatrace when activating monitoring configuration are masked to prevent them from being retrieved.
   * Credential vault: Use [vault credentials](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring#authentication "PostgreSQL extensions in the Extensions framework.") to securely store and retrieve database credentials.
4. Select **Next**.

### Install the instance

Run the provided script to create the necessary objects on the database instance. The agent requires these objects to collect monitoring data.

1. Complete the manual setup for the required instances.
2. Complete manual setup for required instances.
3. Select **Create DB instance monitoring**.

You must run this script to retrieve metrics from the database. To learn more, refer to the helper function details in the [install the instance](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#install-instance "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.") section.

Recommended

After running the creation script, run the validation script to confirm all required objects were created. This ensures the monitoring setup will work as expected.

### Open the Databases app in Explorer

1. Go to the ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** app and select the **Explorer** tab.
2. View the added database in the **Database instances** list. The Explorer view displays all monitored database instances.
3. Select any monitored database instance to view its details. Metrics and performance data appear in the app within 2 to 3 minutes after you complete the setup.

## Use cases

Learn more about PostgreSQL monitoring in these [use cases](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#use-cases "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.").

## Feature sets

[Feature sets](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#feature-sets "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.") restrict which metrics are collected when you activate the extension.

## FAQ and troubleshooting

For complete details, go to the [FAQ](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#faq "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.") section.

## Related topics

* [PostgreSQL extension](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.")