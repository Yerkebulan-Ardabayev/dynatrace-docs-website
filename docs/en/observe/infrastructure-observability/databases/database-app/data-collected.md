---
title: Data collected with Dynatrace database monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-app/data-collected
scraped: 2026-02-24T21:32:02.092932
---

# Data collected with Dynatrace database monitoring

# Data collected with Dynatrace database monitoring

* Latest Dynatrace
* Reference
* Published Jan 20, 2026

When you enable a DB Extension, it automatically collects all metrics defined in the corresponding integration documentation. These include metrics related to database configuration, activity, uptime, connections, buffer pools, query performance, and many others used by the Databases app.

All collected data can also be used in dashboards, alerts, notebooks, and any other metric-based workflows within Dynatrace.

For a complete list of metrics collected, select your database vendor from the list below.

* [IBM DB2](/docs/observe/infrastructure-observability/databases/extensions/ibm-db2-for-luw-remote-monitoring#feature-sets "Remotely collect monitoring metrics from your DB2 databases.")
* [MariaDB](/docs/observe/infrastructure-observability/databases/extensions/mariadb-1#feature-sets "Remotely monitor your MariaDB instances, collect key KPIs & slow queries details")
* [Microsoft SQL Server](/docs/observe/infrastructure-observability/databases/database-app/get-started/microsoft-sql#feature-sets "How to set up monitoring for Microsoft SQL databases in Dynatrace.")
* [MySQL](/docs/observe/infrastructure-observability/databases/extensions/mysql-remote-monitoring-v2#feature-sets "Monitor your MySQL instances remotely, collect key KPIs, and slow query details.")
* [Oracle](/docs/observe/infrastructure-observability/databases/extensions/oracle-database#feature-sets "Observe, analyze, and optimize the usage, health, and performance of your database.")
* [PostgreSQL](/docs/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#feature-sets "Observe, analyze, and optimize the usage, health, and performance of your PostgreSQL database.")
* [SAP HANA](/docs/observe/infrastructure-observability/databases/extensions/sap-hana-database-remote-monitoring#feature-sets "Monitor SAP HANA databases remotely to analyze SQL performance and database health.")
* [Snowflake](/docs/observe/infrastructure-observability/databases/extensions/snowflake#feature-sets "Expand visibility to improve health and performance monitoring of your Snowflake database.")

## Data collection details

### Normalized queries

To protect sensitive information and improve analysis, queries are normalized before storage. This process replaces literal parameter values with placeholders, ensuring that Personally Identifiable Information (PII) is removed.

For example:

**Before normalization**

```
SELECT * FROM customers WHERE email = 'john.doe@example.com';



SELECT * FROM customers WHERE email = 'J.I.Jane@other_example.com';
```

**After normalization**

```
SELECT * FROM customers WHERE email = ?;
```

This approach also applies to execution plans, where parameter values are stripped out to prevent exposure of sensitive data.

### Monitored database instances

Database monitoring supports multiple database technologies through Extensions. However, only the first 70 databases discovered or configured are actively monitored. This limit ensures optimal performance and resource usage.

### Monitored database queries

Monitoring focuses on the top 200 queries based on resource consumption and execution time. Since data is sampled every 1 minute, the list of top queries may vary between samples. However, over time, clear trends emerge, making it easy to analyze overall usage patterns and identify consistently expensive queries.

### Control feature sets and data collection frequency

You can control certain feature sets, which determine what data is collected. For example:

* **Query metrics**: Enable or disable query-level monitoring.
* **Execution plans**: Enable or disable the collection of query plans.
* **Activity metrics**: Control instance-level data frequency.

For selected feature sets, you can adjust the collection frequency to balance detail and overhead. For example:

* Collect query metrics every 1 minute or every 5 minutes.
* Adjust instance activity polling intervals.

However, not all feature sets can be disabled, as some are essential for core functionality.

### Remove PII

To comply with privacy standards:

* Query parameters are replaced with placeholders during normalization.
* Execution plans are sanitized to remove sensitive values.

This ensures that no PII is stored or exposed in monitoring data.

### Data retention

Collected data is retained based on the configuration of the data bucket. By default, data is stored for 35 days, after which it is automatically purged. You can adjust retention settings according to your organizationâs compliance and storage requirements.

## Supported database vendors

The Dynatrace ![Databases](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Databases") **Databases** is designed to minimize impact on monitored database instances and follows industry best practices for low-overhead observability.

To ensure efficient data collection:

* Database instance metrics are collected every 1 minute and use lightweight system tables that avoid performance penalties.
* Host metrics are sourced from the operating system or cloud monitoring services. This approach doesn't require direct polling from the database.
* Database-level metrics are also gathered every 1 minute, but only display for a limited number of databases to reduce load.
* Query metrics are collected every 1 minute, but only for a limited set of queries, selected to balance insight with performance.
* Slow query log collection is optional (only for Postgres and MySQL). To minimize overhead, configure a high threshold and enable sampling to limit the number of queries logged as slow.
* Configuration data (only for Postgres and MySQL) is retrieved every 24 hours to ensure visibility without frequent access.

This architecture ensures that monitoring remains lightweight and scalable, even in environments with multiple databases per instance.