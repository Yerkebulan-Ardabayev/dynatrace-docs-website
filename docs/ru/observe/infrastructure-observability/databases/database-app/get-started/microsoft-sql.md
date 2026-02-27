---
title: Monitor Microsoft SQL database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/microsoft-sql
scraped: 2026-02-27T21:28:20.803058
---

# Monitor Microsoft SQL database

# Monitor Microsoft SQL database

* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

There are three Microsoft SQL extensions supported in Dynatrace:

* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#overview "Improve the health and performance monitoring of your Microsoft SQL Servers."): Uses a modern extension architecture with AIOps capabilities to simplify database monitoring and improve cross-team collaboration. This extension provides real-time and automatic insights into database performance metrics and business KPIs.
* [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#overview "Improve the health and performance monitoring of your Microsoft SQL Servers."): Uses WMI queries to collect key performance and health metrics from the SQL Server instance running on the host, extending your visibility.
* [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#overview "Improve the health and performance monitoring of your Microsoft SQL Servers."): Uses Windows Performance Counters to collect key performance and health metrics for all SQL Server instances on the host.

Depending on your particular use case, such as the environmentâs access restrictions, performance needs, and monitoring goals, you might choose one or both extensions to get complete visibility.

## Prerequisites

Ensure your system meets the requirements and has the necessary compatibility information for full feature support.

* For Microsoft SQL Server, refer to the [requirements](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#requirements "Improve the health and performance monitoring of your Microsoft SQL Servers.") and [compatibility information](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#compatibility-information "Improve the health and performance monitoring of your Microsoft SQL Servers.") information.
* For Microsoft SQL Server (local), refer to [compatibility information](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#compatibility-information "Improve the health and performance monitoring of your Microsoft SQL Servers.") information.
* For Microsoft SQL Server local counters, refer to the [requirements and compatibility](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#requirements "Improve the health and performance monitoring of your Microsoft SQL Servers.") information.

## Set up Microsoft SQL extension for monitoring

To set up and activate the extension:

* For Microsoft SQL Server, refer to [Microsoft SQL Server activation and setup](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#activation-and-setup "Improve the health and performance monitoring of your Microsoft SQL Servers.").
* For Microsoft SQL Server (local) and Microsoft SQL Server local counters, follow these steps.

  1. Install OneAgent on the SQL Server host.
  2. Enable log monitoring.
  3. Activate the extension from the Hub.

  To learn more, refer to [Microsoft SQL Server (local) activation steps](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#activation-and-setup "Improve the health and performance monitoring of your Microsoft SQL Servers.") and [Microsoft SQL Server local counters activation steps](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#activation-and-setup "Improve the health and performance monitoring of your Microsoft SQL Servers.").

## Feature sets

Feature sets restrict which metrics are collected when you activate the extension.
Refer to the sections below to learn more about each feature set.

* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#feature-sets "Improve the health and performance monitoring of your Microsoft SQL Servers.") feature sets.
* [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#feature-sets "Improve the health and performance monitoring of your Microsoft SQL Servers.") feature sets.
* [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#feature-sets "Improve the health and performance monitoring of your Microsoft SQL Servers.") feature sets.

## Use cases

Check these use case scenarios for more details.

* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2#use-cases "Improve the health and performance monitoring of your Microsoft SQL Servers.") use cases.
* [Microsoft SQL Server (local)](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local#use-cases "Improve the health and performance monitoring of your Microsoft SQL Servers.") use cases.
* [Microsoft SQL Server local counters](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters#use-cases "Improve the health and performance monitoring of your Microsoft SQL Servers.") use cases.

## Related topics

* [Microsoft SQL Server extension](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-2 "Improve the health and performance monitoring of your Microsoft SQL Servers.")
* [Microsoft SQL Server local counters extension](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local-counters "Improve the health and performance monitoring of your Microsoft SQL Servers.")
* [Microsoft SQL Server (local) extension](/docs/observe/infrastructure-observability/databases/extensions/microsoft-sql-server-local "Improve the health and performance monitoring of your Microsoft SQL Servers.")