---
title: SQL data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql
scraped: 2026-03-06T21:31:46.228065
---

# SQL data source

# SQL data source

* Latest Dynatrace
* Overview
* 2-min read
* Published Apr 11, 2022

Dynatrace provides you with a framework that you can use to extend your observability into data acquired from a database using SQL queries.

We assume the following:

* You possess sufficient database subject matter expertise to create an extension. In particular, you know how to build and execute SQL queries.
* You're familiar with [Extensions basic concepts](../../concepts.md "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](../extension-yaml.md "Learn how to create an extension YAML file using the Extensions framework.").

Learn about the prerequisites and scope of the supported technologies. For limits applying to your extension, see [Extensions limits](../../concepts.md "Learn more about the concept of Dynatrace Extensions.").

## Supported Dynatrace versions

* Dynatrace version 1.295+
* Environment ActiveGate version 1.295+

## Supported database providers

* Oracle
* Microsoft SQL Server
* IBM DB2
* MySQL
* PostgreSQL
* SAP Hana
* Snowflake
* Any database vendor that provides a JDBC driver that allows applications to connect a database and execute queries. For example MariaDB, Sybase, or Informix.

## Remote monitoring

The SQL data source supports remote database access using various authentication schemes. While basic authentication is supported, more advanced schemes such as Kerberos and NTLM are also supported for Microsoft SQL data source.

## Create extension

* See [SQL data source reference](sql/sql-reference.md "Learn about SQL extensions in the Extensions framework.") to learn about the structure of the extension YAML file.

## Monitoring configuration

* See [Oracle Database monitoring configuration](sql/oracle-monitoring.md "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.") to learn how to create an Oracle Databaseâspecific monitoring configuration.
* See [Microsoft SQL Server monitoring configuration](sql/microsoft-sql-monitoring.md "Microsoft SQL extensions in the Extensions framework.") to learn how to create a Microsoft Databaseâspecific monitoring configuration.
* See [IBM Database monitoring configuration](sql/ibm-monitoring.md "IBM DB2 extensions in the Extensions framework.") to learn how to create an IBM Databaseâspecific monitoring configuration.
* See [MySQL monitoring configuration](sql/mysql-monitoring.md "MySQL extensions in the Extensions framework.") to learn how to create a MySQL Databaseâspecific monitoring configuration.
* See [PostgreSQL monitoring configuration](sql/postgresql-monitoring.md "PostgreSQL extensions in the Extensions framework.") to learn how to create a PostgreSQL Databaseâspecific monitoring configuration.
* See [SAP Hana Database monitoring configuration](sql/sap-hana-monitoring.md "SAP Hana extensions in the Extensions framework.") to learn how to create a SAP Hana Databaseâspecific monitoring configuration.
* See [Snowflake Database monitoring configuration](sql/snowflake-monitoring.md "Snowflake Database extensions in the Extensions framework.") to learn how to create a Snowflake Databaseâspecific monitoring configuration.
* See [JDBC monitoring configuration](sql/jdbc-monitoring.md "JDBC extensions in the Extensions framework.") to learn how to create a JDBC Databaseâspecific monitoring configuration.