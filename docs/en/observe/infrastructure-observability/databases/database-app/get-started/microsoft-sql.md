---
title: Monitor Microsoft SQL database
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/get-started/microsoft-sql
scraped: 2026-03-03T21:22:02.020530
---

# Monitor Microsoft SQL database


* Latest Dynatrace
* How-to guide
* Published Jan 20, 2026

There are three Microsoft SQL extensions supported in Dynatrace:

* Microsoft SQL Server: Uses a modern extension architecture with AIOps capabilities to simplify database monitoring and improve cross-team collaboration. This extension provides real-time and automatic insights into database performance metrics and business KPIs.
* Microsoft SQL Server (local): Uses WMI queries to collect key performance and health metrics from the SQL Server instance running on the host, extending your visibility.
* Microsoft SQL Server local counters: Uses Windows Performance Counters to collect key performance and health metrics for all SQL Server instances on the host.

Depending on your particular use case, such as the environmentâs access restrictions, performance needs, and monitoring goals, you might choose one or both extensions to get complete visibility.

## Prerequisites

Ensure your system meets the requirements and has the necessary compatibility information for full feature support.

* For Microsoft SQL Server, refer to the requirements and compatibility information information.
* For Microsoft SQL Server (local), refer to compatibility information information.
* For Microsoft SQL Server local counters, refer to the requirements and compatibility information.

## Set up Microsoft SQL extension for monitoring

To set up and activate the extension:

* For Microsoft SQL Server, refer to Microsoft SQL Server activation and setup.
* For Microsoft SQL Server (local) and Microsoft SQL Server local counters, follow these steps.

  1. Install OneAgent on the SQL Server host.
  2. Enable log monitoring.
  3. Activate the extension from the Hub.

  To learn more, refer to Microsoft SQL Server (local) activation steps and Microsoft SQL Server local counters activation steps.

## Feature sets

Feature sets restrict which metrics are collected when you activate the extension.
Refer to the sections below to learn more about each feature set.

* Microsoft SQL Server feature sets.
* Microsoft SQL Server (local) feature sets.
* Microsoft SQL Server local counters feature sets.

## Use cases

Check these use case scenarios for more details.

* Microsoft SQL Server use cases.
* Microsoft SQL Server (local) use cases.
* Microsoft SQL Server local counters use cases.

## Related topics

* Microsoft SQL Server extension
* Microsoft SQL Server local counters extension
* Microsoft SQL Server (local) extension